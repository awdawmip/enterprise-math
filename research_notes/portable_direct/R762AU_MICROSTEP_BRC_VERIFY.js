'use strict';
const assert=require('node:assert/strict');
const P=[[[0,1],[2,3],[4,5]],[[0,2],[1,4],[3,5]],[[0,3],[1,5],[2,4]],[[0,4],[1,3],[2,5]]], E=[[0,1],[1,2],[2,0]];
const S=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)S.push([i,j,k]);
const key=s=>s.join('');const code=s=>P.map(p=>!p.every(([a,b])=>s.includes(a)!==s.includes(b))?0:p.reduce((v,[a,b])=>v*(s.includes(b)?-1:1),1));
const C=Object.fromEntries(S.map(s=>[key(s),code(s)]));
assert.equal(new Set(Object.values(C).map(x=>x.join(','))).size,20);
const neighbors=s=>S.filter(t=>s.filter(x=>t.includes(x)).length===2);
function score(s,t,n,mask) {
 const M=Array.from({length:4},()=>[0,0,0,0]);
 E.forEach(([a,b],i)=>{M[a][b]=n+((mask>>i)&1)});
 const u=[-2,-4,-3,10].map((v,a)=>v+M[a].reduce((x,y)=>x+y,0)-M.reduce((x,r)=>x+r[a],0));
 let z=0;const c=C[key(s)],d=C[key(t)];for(let i=0;i<4;i++)z+=u[i]*d[i];
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)z+=c[i]*(M[i][j]-M[j][i])*d[j];
 return z;
}
function ab(s,t,m){const b=score(s,t,0,m);return [score(s,t,1,m)-b,b]}
function winners(s,n,m){let N=neighbors(s),v=Math.max(...N.map(t=>score(s,t,n,m)));return N.filter(t=>score(s,t,n,m)===v).map(key).sort()}
const base=Object.fromEntries(S.map(s=>[key(s),winners(s,15,0)]));assert(S.every(s=>base[key(s)].length===1));
let out=[];for(let m=0;m<8;m++){
 let N=0,ties=[],changed=[],crit=[];const asym={};
 for(let s of S){
  const R=neighbors(s).map(t=>{const [a,b]=ab(s,t,m);return {t:key(t),a,b}});
  const A=Math.max(...R.map(x=>x.a)),B=Math.max(...R.filter(x=>x.a===A).map(x=>x.b));
  const L=R.filter(x=>x.a===A&&x.b===B).map(x=>x.t).sort();asym[key(s)]=L;
  if(L.length>1)ties.push({state:key(s),targets:L});
  if(JSON.stringify(L)!==JSON.stringify(base[key(s)]))changed.push({state:key(s),targets:L});
  for(let r of R)if(!L.includes(r.t)){
   const da=A-r.a,db=B-r.b;assert(da>0||(da===0&&db>0));
   if(da>0){const T=Math.max(0,Math.floor(-db/da)+1);
    if(T>N){N=T;crit=[{s:key(s),t:r.t,da,db}]}else if(T===N&&T>0)crit.push({s:key(s),t:r.t,da,db});
   }
  }
 }
 assert(S.every(s=>JSON.stringify(winners(s,N,m))===JSON.stringify(asym[key(s)])));
 if(N>0)assert(S.some(s=>JSON.stringify(winners(s,N-1,m))!==JSON.stringify(asym[key(s)])));
 out.push({mask:m,sharp_onset:N,permanent_ties:ties,changed_from_complete_macro:changed,sharp_witnesses:crit,signature:S.map(s=>asym[key(s)].join('|')).join(';')});
}
assert.deepEqual(out.map(x=>[x.sharp_onset,x.permanent_ties.length,x.changed_from_complete_macro.length]),[[15,0,0],[16,1,1],[15,1,2],[15,2,2],[15,1,2],[16,2,2],[14,3,3],[14,0,0]]);
let coincident=[];for(let i=0;i<8;i++)for(let j=i+1;j<8;j++)if(out[i].signature===out[j].signature)coincident.push([i,j]);assert.deepEqual(coincident,[[0,7]]);
const witness=m=>['014','245'].map(t=>ab([1,4,5],t.split('').map(Number),m));
assert.deepEqual(witness(0),[[0,3],[0,4]]);assert.deepEqual(witness(2),[[0,4],[0,3]]);

const cyc=['012','123','234','034','035','025'];
const cycNext=Object.fromEntries(cyc.map((s,i)=>[s,cyc[(i+1)%cyc.length]]));
let cycleThreshold=0,cycleWitness=[];
for(let m=0;m<8;m++)for(let s of cyc){
 const src=s.split('').map(Number), win=cycNext[s].split('').map(Number);
 for(let t of neighbors(src)){if(key(t)===cycNext[s])continue;
  const [aw,bw]=ab(src,win,m),[at,bt]=ab(src,t,m);
  const da=aw-at, db=bw-bt;assert(da>0||(da===0&&db>0));
  const need=da>0?Math.max(0,Math.floor(-db/da)+1):0;
  if(need>cycleThreshold){cycleThreshold=need;cycleWitness=[{mask:m,S:s,T:key(t),da,db}]}
  else if(need===cycleThreshold&&need>0)cycleWitness.push({mask:m,S:s,T:key(t),da,db});
 }
}
assert.equal(cycleThreshold,2);
for(let m=0;m<8;m++)for(let s of cyc)assert.deepEqual(winners(s.split('').map(Number),2,m),[cycNext[s]]);
const U=Object.fromEntries(S.map(s=>[key(s),new Set()]));
for(let m=0;m<8;m++)for(let s of S)for(let t of winners(s,16,m))U[key(s)].add(t);
for(let s of cyc)assert.deepEqual([...U[s]],[cycNext[s]]);
const stack=new Set(),dist=new Map();
function height(s){
 if(cycNext[s])return 0;
 if(dist.has(s))return dist.get(s);
 if(stack.has(s))throw Error('outside cycle');
 stack.add(s);
 const H=1+Math.max(...[...U[s]].map(height));
 stack.delete(s);dist.set(s,H);
 return H;
}
let maxOutside=Math.max(...S.filter(s=>!cycNext[key(s)]).map(s=>height(key(s))));
assert.equal(maxOutside,3);
assert(U['145'].has('245')&&U['245'].has('024')&&U['024'].has('234'));
const recurrent={uniform_cycle_threshold:cycleThreshold,sharp_witnesses:cycleWitness,
 cycle:cyc,union_edges:Object.values(U).reduce((a,v)=>a+v.size,0),
 outside_states:14,acyclic_outside:true,max_moves_until_cycle:maxOutside,
 three_move_witness:['145','245','024','234'],
 odd_v17_holonomy:'(2,1,0) under canonical shared-axis frame replacement'};

console.log(JSON.stringify({schema:'R762AU_BRC_MICROSTEP_EXACT_CERTIFICATE_V1',status:'PASS',source:'V23/V25/V27 conditional selector + actual V29 PASS updates',states:20,neighbors_per_state:9,masks:8,affine_scores:1440,proof_domain:'all integers n>=per-mask sharp_onset',rho:'any rational >1; exact monotone exponent comparison',sharp_thresholds:out.map(x=>x.sharp_onset),permanent_tie_counts:out.map(x=>x.permanent_ties.length),changed_state_counts:out.map(x=>x.changed_from_complete_macro.length),equal_relation_masks:coincident,reversal_witness:{S:'145',targets:['014','245'],mask0:witness(0),mask2:witness(2)},tables:out,recurrent},null,2));
