'use strict';
// X6 R79. Run: node x6_r79_nine_core_exact_verify.js
// Exact BigInt comparisons; the universal two-exception inequality is proved in the companion paper.
const atlas=[[1,1,0,0],[2,0,2,-1],[3,1,-3,1],[3,2,-3,1],[3,3,-1,0],[4,1,3,-1],[4,3,-4,1],[4,4,-1,0],[5,3,2,-1],[5,4,-4,1],[5,5,-1,0],[6,5,-4,1],[6,6,-1,0],[7,3,-7,2],[7,6,-4,1],[7,7,-1,0],[9,7,2,-1],[10,9,-5,1],[11,10,-5,1],[16,15,-6,1],[22,21,-7,1],[27,24,-14,3],[39,36,-16,3],[43,39,-20,4],[47,42,-24,5],[49,45,-21,4],[71,66,-28,5],[125,114,-56,11]];
const core=[14,17,18,19,21,22,23,25,27];
function certify(){
 const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
 function gap(row){
   const [q,x,y,z]=row;
   const obs=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z];
   const demand=Math.max([x,y,z].reduce((s,t)=>s+Math.max(t,0),0),[x,y,z].reduce((s,t)=>s+Math.max(-t,0),0));
   if(demand!==q)throw Error("q mismatch "+JSON.stringify(row));
   return pairs.map(([i,j])=>Math.abs(obs[j]-obs[i])/2);
 }
 const gaps=atlas.map(gap);
 const dominated=[];
 for(let i=0;i<atlas.length;i++){
  if(core.includes(i)||i===24||i===26)continue;
  const k=core.find(k=>gaps[k].every((v,j)=>v<=gaps[i][j]));
  if(k===undefined)throw Error("No coordinatewise domination for "+i);
  dominated.push({excluded_index:i,dominating_core_index:k,excluded_q:atlas[i][0],dominating_q:atlas[k][0]});
 }
 if(dominated.length!==17)throw Error("Not exactly 17");
 const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 if(!same(gaps[21],[0,6,0,6,0,6])||!same(gaps[22],[6,6,6,0,0,0])||!same(gaps[24],[0,12,12,12,12,0])||!same(gaps[26],[12,12,0,0,12,12]))throw Error("Exceptional symbolic gap input changed");
 function cmp(a,b){const v=a[0]*b[1]-b[0]*a[1];return v<0n?-1:v>0n?1:0;}
 function objective(ds,w){
   let ans=[0n,1n];
   for(let k=0;k<6;k++){
     const [i,j]=pairs[k], current=[BigInt(ds[k]),BigInt(w[i]+w[j])];
     if(cmp(current,ans)>0)ans=current;
   }
   return ans;
 }
 function best(ixs,w){
  let ans=null;
  for(const i of ixs){const cost=objective(gaps[i],w);if(!ans||cmp(cost,ans)<0)ans=cost;}
  return ans;
 }
 const ids=atlas.map((_,i)=>i);
 let grid=0;
 for(let A=1;A<=6;A++)for(let B=1;B<=6;B++)for(let C=1;C<=6;C++)for(let D=1;D<=6;D++){
   const w=[A,B,C,D];
   if(cmp(best(ids,w),best(core,w))!==0)throw Error("Grid discrepancy: "+w);
   for(const e of [24,26]) {
     const c=objective(gaps[e],w), bound=best([21,22],w);
     if(cmp(bound,c)>0)throw Error("exception failure "+e+" "+w);
   }
   grid++;
 }
 const profiles=[[14,[8,8,26,187]],[17,[3,3,20,34]],[18,[2,2,2,2]],[19,[1447,167,166,1850]],[21,[163,165,1809,388]],[22,[199,41,18,18]],[23,[41,46,4,4]],[25,[413,4334,3265,364]],[27,[2,47,3,2]]];
 function format(x){return x[0].toString()+"/"+x[1].toString();}
 const strict_winners=[];
 for(const [k,w] of profiles) {
  const costs=ids.map(i=>objective(gaps[i],w));
  const win=costs[k];
  if(costs.some((v,i)=>i!==k&&cmp(win,v)>=0))throw Error("non-strict winning profile "+k);
  strict_winners.push({atlas_index:k,q:atlas[k][0],w,cost_fraction_unreduced:format(win)});
 }
 return {schema:"X6_R79_NINE_CORE_CERTIFICATE_V1",date:"2026-11-21",model:"Conditional D=4 four-positive-moment BRC star observer; all real weights>0; p>=125",frozen_p000_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",atlas_size:atlas.length,core_size:core.length,core_indices:core,core_q:core.map(i=>atlas[i][0]),coordinatewise_dominated_count:dominated.length,coordinatewise_dominance:dominated,exceptional_indices:[24,26],exceptional_pair_witnesses:[21,22],exceptional_symbolic_inequality:"min(F_27,F_39)<=6/max(A,C)<=12/(A+C)<=min(F_47,F_71) pointwise for any A,B,C,D>0",exact_integer_weight_profiles_tested:grid,independent_strict_core_witness_count:strict_winners.length,strict_winners,conclusion:"Nine entries suffice for arbitrary strictly positive real weights when p>=125; nine is the smallest subset of the R72 28-entry atlas with this property.",independent_review:"NOT_REVIEWED",scope:"Observer-only finite atlas reduction; global integer-difference coverage depends on R72 author certificate."};
}
console.log(JSON.stringify(certify(),null,2));
