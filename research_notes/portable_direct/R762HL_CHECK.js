'use strict';
// R762HL: cyclic-seam positive-source BRC verifier. Run: node R762HL_CHECK.js
const assert = require('node:assert/strict');
const ports=['01','15','12','25','24','04','05','03','04','24','23','25','35','05','01'];
const m=ports.length-1;
assert.equal(ports[0],ports[m]);
const h=ports.slice(0,-1).map((p,t)=>{
  const q=ports[t+1];
  assert.equal([...p].filter(x=>q.includes(x)).length,1);
  const A=new Set([...p,...q].map(Number)); assert.equal(A.size,3);
  return [...A].reduce((v,i)=>v|(1<<i),0);
});
function count(H){
 const n=H.length, linear={}, cyclic={}, incidence=Array(6).fill(0), V=Array(6).fill(0);
 for(let t=0;t<n;t++)for(let i=0;i<6;i++)if(H[t]&(1<<i)){
   incidence[i]++;V[i]+=(t%2?-1:1);
 }
 let solutions=0;
 for(let mask=0;mask<2**n;mask++){
  const D=Array(6).fill(0);
  for(let t=0;t<n;t++){
   const sign=(t%2?-1:1)*(mask&(1<<t)?-1:1);
   for(let i=0;i<6;i++)if(H[t]&(1<<i))D[i]+=sign;
  }
  if(D.some(x=>x!==0))continue;
  solutions++;
  let k=0,r=0;
  for(let t=0;t<n;t++)if(mask&(1<<t)){
    if(t===0 || !(mask&(1<<(t-1))))k++;
    if(!(mask&(1<<((t+n-1)%n))))r++;
  }
  linear[k]=(linear[k]||0)+1;
  cyclic[r]=(cyclic[r]||0)+1;
 }
 return {linear,cyclic,solutions,incidence,V};
}
// Direct cyclic trace transfer via integer coefficient DP.
// Key: prior bit | six-dimensional Laurent exponent | cyclic run count.
function traceDP(H){
 const n=H.length,V=Array(6).fill(0), out={};
 for(let t=0;t<n;t++)for(let i=0;i<6;i++)if(H[t]&(1<<i))V[i]+=(t%2?-1:1);
 if(V.some(v=>v%2!==0))return out;
 const target=V.map(x=>x/2).join(',');
 for(let first=0;first<=1;first++){
  let states=new Map([[first+'|0,0,0,0,0,0|0',1]]);
  for(let t=0;t<n;t++){
   const nxt=new Map(),a=(t%2?-1:1);
   for(const [key,weight] of states){
    const [pStr,vStr,kStr]=key.split('|');
    const p=+pStr,v=vStr.split(',').map(Number),k=+kStr;
    for(let q=0;q<=1;q++){
      const w=v.map((x,i)=>x+((q && (H[t]&(1<<i)))?a:0));
      const j=k+(!p&&q?1:0);
      const z=q+'|'+w.join(',')+'|'+j;
      nxt.set(z,(nxt.get(z)||0)+weight);
    }
   }
   states=nxt;
  }
  for(const [key,weight] of states){
   const [last,v,k]=key.split('|');
   if(+last===first && v===target)out[k]=(out[k]||0)+weight;
  }
 }
 return out;
}
function runs(mask,n){
 let linear=0,cyclic=0;
 for(let t=0;t<n;t++)if(mask&(1<<t)){
  if(t===0 || !(mask&(1<<(t-1))))linear++;
  if(!(mask&(1<<((t+n-1)%n))))cyclic++;
 }
 return {linear,cyclic};
}
for(let n=2;n<=12;n+=2)for(let mask=0;mask<(1<<n);mask++){
 const a=runs(mask,n),b=runs(((1<<n)-1)^mask,n);
 assert.equal(Math.min(a.linear,b.linear),a.cyclic);
}
const base=count(h);
assert.deepEqual(base.incidence,[8,4,8,6,6,10]);
assert.deepEqual(base.V,[2,0,0,0,-2,0]);
assert.equal(base.solutions,104);
assert.deepEqual(base.linear,{'2':20,'3':46,'4':36,'5':2});
assert.deepEqual(base.cyclic,{'2':36,'3':52,'4':16});
assert.deepEqual(traceDP(h),base.cyclic);
const sum={},distinct=new Set();
for(let s=0;s<m;s++){
 const H=h.slice(s).concat(h.slice(0,s)),x=count(H);
 assert.equal(x.solutions,104);
 assert.deepEqual(x.cyclic,base.cyclic);
 assert.equal(Math.min(...Object.keys(x.linear).map(Number)),2);
 distinct.add(JSON.stringify(Object.keys(x.linear).sort().map(k=>[k,x.linear[k]])));
 for(const [k,v] of Object.entries(x.linear))sum[k]=(sum[k]||0)+v;
}
assert.deepEqual(count([...h].reverse()).cyclic,base.cyclic);
assert.deepEqual(sum,{'2':324,'3':700,'4':384,'5':48});
const pred={};
for(const [rS,N] of Object.entries(base.cyclic)){
 const r=+rS;pred[r]=(pred[r]||0)+N*(m/2+r);
 pred[r+1]=(pred[r+1]||0)+N*(m/2-r);
}
assert.deepEqual(pred,sum);
console.log(JSON.stringify({
 schema:'ENTERPRISE_MATH_R762HL_CYCLIC_SEAM_EVIDENCE_V1',
 model:'signed_composite_port_candidate',
 frozen_science_commit:'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 predecessor:'R762HK@0778045cdbe977bf86e1d3f7557162e1ed6b33d8',
 port_walk:ports,event_count:m,incidence:base.incidence,
 alternating_residual:base.V,signed_zero_completions:base.solutions,
 linear_histogram:base.linear,cyclic_histogram:base.cyclic,
 minimum_blocks_all_14_seams:2,
 distinct_linear_histograms_across_seams:distinct.size,
 seam_summed_linear_histogram:sum,
 cyclic_trace_dp_verified:true,reversal_verified:true,
 complement_lemma_verified_even_lengths:[2,4,6,8,10,12],
 verification:'PASS',review:'NOT_REVIEWED',
 primitive_TRIADIC_CLOSURE_E_admission:'NOT_ESTABLISHED'
},null,2));
