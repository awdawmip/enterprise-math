'use strict';
// Reproduce R78 exact rational certificate. Run: node x6_r78_nine_open_winner_chambers_verify.js
// No dependencies, no floating-point arithmetic in evidence comparisons.
const atlas=[[1,1,0,0],[2,0,2,-1],[3,1,-3,1],[3,2,-3,1],[3,3,-1,0],[4,1,3,-1],[4,3,-4,1],[4,4,-1,0],[5,3,2,-1],[5,4,-4,1],[5,5,-1,0],[6,5,-4,1],[6,6,-1,0],[7,3,-7,2],[7,6,-4,1],[7,7,-1,0],[9,7,2,-1],[10,9,-5,1],[11,10,-5,1],[16,15,-6,1],[22,21,-7,1],[27,24,-14,3],[39,36,-16,3],[43,39,-20,4],[47,42,-24,5],[49,45,-21,4],[71,66,-28,5],[125,114,-56,11]];
const profiles=[{"candidate_index":14,"w":[8,8,26,187]},{"candidate_index":17,"w":[3,3,20,34]},{"candidate_index":18,"w":[2,2,2,2]},{"candidate_index":19,"w":[1447,167,166,1850]},{"candidate_index":21,"w":[163,165,1809,388]},{"candidate_index":22,"w":[199,41,18,18]},{"candidate_index":23,"w":[41,46,4,4]},{"candidate_index":25,"w":[413,4334,3265,364]},{"candidate_index":27,"w":[2,47,3,2]}];
const verify=function verify(atlas,profiles){
  const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
  const abs=x=>x<0n?-x:x;
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const c=a%b;a=b;b=c}return a}
  function frac(n,d){if(d<=0n)throw Error("bad denominator");const q=gcd(n,d);return [n/q,d/q]}
  const cmp=(a,b)=>a[0]*b[1]===b[0]*a[1]?0:(a[0]*b[1]<b[0]*a[1]?-1:1);
  const add=(a,b)=>frac(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>frac(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
  const div=(a,b)=>frac(a[0]*b[1],a[1]*b[0]);
  const str=a=>a[0]+"/"+a[1];
  function q(a){return Math.max(a.reduce((s,x)=>s+Math.max(x,0),0),a.reduce((s,x)=>s+Math.max(-x,0),0))}
  function f(entry,weights){
    const [a,b,c]=entry.slice(1).map(BigInt);
    const z=[0n,2n*a+6n*b+12n*c,6n*a+24n*b+60n*c,14n*a+78n*b+252n*c];
    let best=[0n,1n];
    pairs.forEach(([i,j])=>{
      const candidate=frac(abs(z[j]-z[i]),2n*(BigInt(weights[i])+BigInt(weights[j])));
      if(cmp(candidate,best)>0)best=candidate;
    });
    return best;
  }
  atlas.forEach((a,i)=>{if(q(a.slice(1))!==a[0])throw Error("Atlas q mismatch @"+i)});
  const rows=[];
  for(const {candidate_index,w} of profiles){
    const costs=atlas.map(a=>f(a,w));
    const winner=costs[candidate_index];
    const others=costs.filter((_,i)=>i!==candidate_index);
    const runner=others.reduce((x,y)=>cmp(x,y)<0?x:y);
    if(cmp(winner,runner)>=0)throw Error("Non-strict profile @"+candidate_index);
    let actual=0;for(let i=1;i<costs.length;i++)if(cmp(costs[i],costs[actual])<0)actual=i;
    if(actual!==candidate_index)throw Error("Unexpected minimum @"+candidate_index);
    const gap=sub(runner,winner),rho=div(gap,add(runner,winner));
    rows.push({atlas_index: candidate_index,q:atlas[candidate_index][0],a:atlas[candidate_index].slice(1),weights:w,eta_winner:str(winner),eta_runner_up:str(runner),strict_gap:str(gap),relative_open_radius:str(rho)});
  }
  if(rows.length!==9||new Set(rows.map(r=>r.atlas_index)).size!==9)throw Error("Wrong winner cardinality");
  return {schema:"X6_R78_NINE_OPEN_CHAMBERS_EXACT_RATIONAL_CERTIFICATE_V1",date:"2026-11-21",source_atlas:"awdawmip/enterprise-math@5f1f790ba37b9be2552ff93662c84936eb031a6e:research_notes/portable_direct/x6_r72_d4_sharp_saturation_results.json",frozen_scientific_input:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json",model:"D=4 conditional positive BRC star histogram; arbitrary w>0; unknown shared additive offset; p>=125",atlas_size:atlas.length,distinct_certified_strict_winners:rows.length,verified:"EXACT_BIGINT_RATIONAL_COMPARISONS_AGAINST_28_ATLAS_ENTRIES",formal_acceptance:false,rows,scope_note:"Nine distinct candidate vectors each have a certified nonempty open winning region within the R72 28-vector atlas; full optimization over all feasible differences relies on R72's existing author finite-cover certificate. No proof that the remaining 19 are always dispensable."};
};
console.log(JSON.stringify(verify(atlas,profiles),null,2));
