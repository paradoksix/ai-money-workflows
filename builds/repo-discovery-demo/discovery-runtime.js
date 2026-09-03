import {synthesizeQueries,synthesizeRefinementQueries,coverageByPattern,scoreRepository,diversify} from './discovery-core.js';

const API='https://api.github.com';
function keyRepo(r){return `repo:${r.id}`}

async function github(path,token,onRate,search=false){
  const headers={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'};
  if(token) headers.Authorization=`Bearer ${token}`;
  const res=await fetch(API+path,{headers});
  onRate?.({remaining:res.headers.get('x-ratelimit-remaining'),limit:res.headers.get('x-ratelimit-limit'),resource:res.headers.get('x-ratelimit-resource')||(search?'search':'core')});
  if(!res.ok) throw new Error(`GitHub API ${res.status}`);
  return res.json();
}

function mergeCandidate(map,repo,query){
  if(!map.has(repo.id)) repo._discovery={lineage:[]};
  const item=map.get(repo.id)||repo;
  if(!item._discovery) item._discovery={lineage:[]};
  if(!item._discovery.lineage.some(x=>x.queryId===query.id)) item._discovery.lineage.push({queryId:query.id,queryText:query.text,stage:query.stage,patternId:query.patternId,caseIds:query.caseIds||[]});
  map.set(repo.id,item);
}

async function executeBatch(queries,{token,onRate,archiveRepos,seen,cycle,candidates,executed}){
  const page=1+(cycle%3);
  for(const q of queries){
    const data=await github(`/search/repositories?q=${encodeURIComponent(q.text)}&sort=updated&order=desc&per_page=50&page=${page}`,token,onRate,true);
    executed.push({...q,resultCount:data.items?.length||0,page});
    for(const repo of data.items||[]){
      if(repo.archived||repo.fork||archiveRepos.has(repo.full_name.toLowerCase())||seen.has(keyRepo(repo))) continue;
      mergeCandidate(candidates,repo,q);
    }
  }
}

export async function runDiscoveryPipeline({model,token='',archiveRepos=new Set(),seen=new Set(),cycle=0,onRate}){
  const budgets=token?{seed:7,refine:3}:{seed:4,refine:2};
  const starSteps=[3,1,0];
  const stars=starSteps[cycle%starSteps.length];
  const candidates=new Map(),executed=[];
  const seed=synthesizeQueries(model,{limit:budgets.seed,stars});
  await executeBatch(seed,{token,onRate,archiveRepos,seen,cycle,candidates,executed});
  const coverage=coverageByPattern([...candidates.values()]);
  const refine=synthesizeRefinementQueries(model,coverage,seed,{limit:budgets.refine});
  await executeBatch(refine,{token,onRate,archiveRepos,seen,cycle:cyleFix(cycle),candidates,executed});
  const pool=[...candidates.values()].filter(r=>scoreRepository(r,model,r._discovery?.lineage||[]).score>=.18);
  return {candidates:diversify(pool,model,24),queryPlan:[...seed,...refine],executed,coverage,stars,nextCycle:cycle+1};
}
function cyleFix(cycle){return cycle+1}
