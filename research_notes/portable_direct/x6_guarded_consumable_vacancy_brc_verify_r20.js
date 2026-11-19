#!/usr/bin/env node
/* R20: source-labelled Boolean BRC of intact triadic carriers on a declared
   finite six-coordinate Cell chart. Only nonnegative, nonreplenishing,
   globally shared resource credits are admitted by this conditional model.
   Standard-library Node.js; deterministic and exact integer arithmetic. */
'use strict';
const assert = require('node:assert/strict');
const W=[[0,0,0,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[1,1,0,0,0,0],[1,0,1,0,0,0]];
const N=W.length, FULL=(1<<N)-1;
const dirs=[];
for(let u=0;u<N;u++)for(let v=0;v<N;v++){
  if(u===v)continue;
  if(W[u].reduce((s,a,k)=>s+Math.abs(a-W[v][k]),0)===1)dirs.push([u,v]);
}
const named=[dirs,dirs.filter(([u,v])=>u<v),dirs.filter(([u,v])=>u>v),
  dirs.filter(([u,v])=>W[v][0]>W[u][0]),dirs.filter(([u,v])=>v!==0),
  dirs.filter(([u,v])=>u!==0)];
let seed=20261119;
const rnd=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;};
for(let i=0;i<18;i++){let es=dirs.filter(()=>rnd()%4!==0);named.push(es);}
const graphs=named.map((es,g)=>{
  let edges=es.map(([u,v],j)=>({u,v,c:[(j+g)%3===0?1:0, (j+g)%4===0?1:0]}));
  if(g%5===0)edges=edges.map((e,j)=>({...e,c:[j%2, (j+2*g)%3===0?1:0]}));
  return edges;
});
const affordable=(c,used,C)=>used[0]+c[0]<=C[0]&&used[1]+c[1]<=C[1];
function constrainedPath(edges, start, goal, C) {
  const q=[{v:start,c:[0,0],path:[start]}], seen=new Set([`${start}|0|0`]);
  for(let h=0;h<q.length;h++){
    const s=q[h]; if(goal(s.v))return s.path;
    for(const e of edges){if(e.u!==s.v||!affordable(e.c,s.c,C))continue;
      const nc=[s.c[0]+e.c[0],s.c[1]+e.c[1]];
      const key=`${e.v}|${nc[0]}|${nc[1]}`;
      if(!seen.has(key)){seen.add(key);q.push({v:e.v,c:nc,path:[...s.path,e.v]});}
    }
  }
  return null;
}
function actualFirstMove(edges,S,z,C) {
  const q=[{mask:S,p:z,c:[0,0],depth:0}], seen=new Set([`${S}|${z}|0|0`]);
  for(let h=0;h<q.length;h++){
    const x=q[h];
    for(const e of edges){if(!(x.mask&(1<<e.u))||(x.mask&(1<<e.v))||!affordable(e.c,x.c,C))continue;
      if(e.u===x.p)return x.depth+1;
      const mask=x.mask^(1<<e.u)^(1<<e.v),nc=[x.c[0]+e.c[0],x.c[1]+e.c[1]];
      const key=`${mask}|${x.p}|${nc[0]}|${nc[1]}`;
      if(!seen.has(key)){seen.add(key);q.push({mask,p:x.p,c:nc,depth:x.depth+1});}
    }
  }
  return Infinity;
}
function replay(edges,S,C,word,a,b,swap) {
  let who=new Map();for(let z=0;z<N;z++)if(S&(1<<z))who.set(z,`s${z}`);
  if(a!==null){who.set(a,swap?'B':'A');who.set(b,swap?'A':'B');}
  let used=[0,0];
  for(const [label,u,v] of word){
    if(who.get(u)!==label||who.has(v))return false;
    const edge=edges.find(e=>e.u===u&&e.v===v&&affordable(e.c,used,C));
    if(!edge)return false;
    used=[used[0]+edge.c[0],used[1]+edge.c[1]];
    who.delete(u);who.set(v,label);
  }
  return true;
}
let firstChecks=0,witnesses=0,shieldChecks=0,infPairs=0,zeroExamples=0;
const representative=[];
for(let g=0;g<graphs.length;g++){
  const edges=graphs[g];
  for(let S=1;S<=FULL;S++){
    const occ=Array.from({length:N},(_,z)=>z).filter(z=>S&(1<<z));
    for(let c0=0;c0<=2;c0++)for(let c1=0;c1<=2;c1++){
      const C=[c0,c1], ds=new Map();
      for(const z of occ){
        const path=constrainedPath(edges,z,v=>!(S&(1<<v)),C);
        const predicted=path?path.length-1:Infinity;
        const measured=actualFirstMove(edges,S,z,C);
        assert.equal(measured,predicted,`g=${g} mask=${S} z=${z} C=${C}`);
        ds.set(z,{predicted,path});firstChecks++;
        for(let r=0;r<=3;r++){
          const ball=[];
          for(let v=0;v<N;v++){let p=constrainedPath(edges,z,x=>x===v,C);
            if(p&&p.length-1<=r)ball.push(v);
          }
          const covered=ball.every(v=>S&(1<<v));
          assert.equal(predicted>r,covered);shieldChecks++;
        }
      }
      for(let i=0;i<occ.length;i++)for(let j=i+1;j<occ.length;j++){
        const a=occ[i],b=occ[j],da=ds.get(a).predicted,db=ds.get(b).predicted;
        if(da===Infinity&&db===Infinity){infPairs++;continue;}
        if(da===db)continue;
        const source=da<db?a:b,other=da<db?b:a,d=ds.get(source).predicted;
        const path=ds.get(source).path;
        assert(!path.includes(other),`short feasible path enters more distant source ${other}`);
        const word=[];
        for(let k=path.length-2;k>=1;k--)word.push([`s${path[k]}`,path[k],path[k+1]]);
        word.push([source===a?'A':'B',source,path[1]]);
        // The same common prefix and final original-label event distinguish
        // the placements with a,b exchanged (choose the appropriate side).
        const p=replay(edges,S,C,word,a,b,false),q=replay(edges,S,C,word,a,b,true);
        assert.notEqual(p,q,`distinguishing word g=${g} S=${S} C=${C}`);
        assert.equal(p, true);
        assert.equal(q, false);
        assert.equal(word.length,d);
        witnesses++;
        if(representative.length<5)representative.push({g,S,C,a,b,da:Number.isFinite(da)?da:'INF',db:Number.isFinite(db)?db:'INF',word});
      }
      if(g===0&&S===FULL&&c0===0&&c1===0)zeroExamples++;
    }
  }
}
// Shared one-credit obstruction: two independent one-event migrations are
// each possible, but the two-event joint word consumes 2 credits and fails.
const credits=[[0,2],[1,4]].map(([u,v])=>({u,v,c:[1,0]}));
const initial=(1<<0)|(1<<1),C=[1,0];
assert.equal(replay(credits,initial,C,[['s0',0,2]],null,null,false),true);
assert.equal(replay(credits,initial,C,[['s1',1,4]],null,null,false),true);
assert.equal(replay(credits,initial,C,[['s0',0,2],['s1',1,4]],null,null,false),false);
const result={schema:'ENTERPRISE_X6_R20_CONSUMABLE_PORT_BRC_EXACT_V1',status:'PASS',date:'2026-11-19',
  chart:{dimension:6,points:W.length,signed_unit_edges:dirs.length},
  graph_count:graphs.length,occupied_subsets:FULL,credit_vectors:9,
  comparisons:{actual_first_move_vs_budgeted_path:firstChecks,
    strict_transposition_event_witnesses:witnesses,
    guarded_ball_cover_checks:shieldChecks,both_immobile_pairs_observed:infPairs},
  global_credit_nonfactorization:true,representative,
  scope:'All occupied nonempty subsets of six stated X6 sites; 24 fixed directed graph/cost patterns; credits (0..2)^2. Conditional whole-triad source-neutral relocation, not an admitted native triadic controller.',
  independent_math_review:'NOT_REVIEWED'};
console.log(JSON.stringify(result,null,2));
