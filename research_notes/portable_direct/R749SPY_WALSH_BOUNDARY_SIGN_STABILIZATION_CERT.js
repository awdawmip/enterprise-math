#!/usr/bin/env node
// R749SPY exact finite-deficit all-n provenance saturation certificate.
// Usage: node R749SPY_WALSH_BOUNDARY_SIGN_STABILIZATION_CERT.js > R749SPY_WALSH_BOUNDARY_SIGN_STABILIZATION_RESULTS.json
function verifyInfinite(){
  const fail=(condition,what)=>{if(!condition)throw Error(what)};
  const facets=[[-1,-1,-1,-2],[-1,-1,1,-2],[-1,1,-1,-2],[-1,1,1,-2],[1,-1,-1,-2],[1,-1,1,-4],[1,1,-1,-4],[1,1,1,-2]];
  let P=[];
  for(let h=-2;h<=2;h++)for(let u=-2;u<=2;u++)for(let v=-2;v<=2;v++)if(facets.every(([a,b,c,d])=>a*h+b*u+c*v>=d))P.push([h,u,v]);
  fail(P.length===33,"expected K lattice points");
  const pairs=new Map(),key=x=>x.join(",");
  for(let i=0;i<P.length;i++)for(let j=i;j<P.length;j++){
    const s=key(P[i].map((v,d)=>v+P[j][d]));let a=pairs.get(s);
    if(!a){a={count:0,i,j};pairs.set(s,a)}a.count++;
  }
  let fids=new Set();for(const a of pairs.values())if(a.count===1){fids.add(a.i);fids.add(a.j)}
  const F=[...fids].sort((a,b)=>a-b).map(i=>P[i]);
  fail(F.length===25,"expected forced set");
  const zero=F.filter(([h,u,v])=>u===2),positive=F.filter(([h,u,v])=>u<2);
  fail(zero.length===2&&zero.some(x=>key(x)==="-1,2,-1")&&zero.some(x=>key(x)==="0,2,0"),"zero-deficit alphabet");
  fail(positive.length===23&&positive.every(([h,u,v])=>v<=2-u),"deficit bounds v <= d");
  const dp=Array.from({length:7},()=>new Map());
  dp[0].set("0,0,0",1);
  for(const [h,u,v] of positive){
    const d=2-u;
    for(let D=d;D<=6;D++)for(const [s,c] of dp[D-d]){
      const [m,H,V]=s.split(",").map(Number),target=key([m+1,H+h,V+v]);
      dp[D].set(target,(dp[D].get(target)||0)+c);
    }
  }
  const accepted=[],profile=new Map();
  for(let k=0;k<=3;k++){
    const D=6-2*k;let sum=0,max_min_n=0,states=0;
    for(const [s,count] of dp[D]){
      const [m,H,V]=s.split(",").map(Number);
      if(V<0)continue;
      states++;sum+=count;
      max_min_n=Math.max(max_min_n,k+m+V);
      if(k>0){
        let h=H-V;
        profile.set(h,(profile.get(h)||0)+count);
        profile.set(h-k,(profile.get(h-k)||0)-count);
      }
    }
    accepted.push({optional_k:k,positive_deficit:D,positive_multisets:sum,max_required_n:max_min_n,aggregated_states:states});
  }
  fail(accepted.map(x=>x.positive_multisets).join(",")==="1292,161,14,1","exact accepted patterns");
  fail(accepted.map(x=>x.max_required_n).join(",")==="12,9,6,3","finite saturation cutoff");
  const signed=[...profile].filter(([h,d])=>d!==0).sort((a,b)=>a[0]-b[0]);
  const expected=[[-5,-15],[-4,-9],[-3,-13],[-2,3],[-1,-6],[0,18],[1,9],[2,9],[3,1],[4,3]];
  fail(JSON.stringify(signed)===JSON.stringify(expected),"stable signed fiber coefficients");
  const mass=accepted.reduce((a,x)=>a+x.positive_multisets,0);
  const ksum=accepted.reduce((a,x)=>a+x.optional_k*x.positive_multisets,0);
  fail(mass===1468&&ksum===192,"saturated slice statistics");
  fail(signed.reduce((a,x)=>a+x[1],0)===0,"signed profile conservation");
  return {schema:"R749SPY_EVENTUAL_SIGN_REENTRY_EXACT_V1",status:"PASS",frozen_input:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",scope:"auxiliary 16-atom Walsh center, fixed t=1/10,s=1/2",first_grid_points:P.length,forced_letters:F,zero_deficit_letters:zero,positive_deficit_letter_count:positive.length,deficit_cap:6,accepted,stable_signed_profile_for_U_equal_2n_minus_6_V0_n_ge9:signed,for_all_n_ge9:{D_n_H_minus2:3,D_n_H_minus1:-6,D_n_H_zero:18},for_all_n_ge12:{slice_mass:mass,optional_count_sum:ksum,conditional_expected_K:"48/367",conditional_W1_WalshTV:"12/(1835*n)"},proof_logic:"deficiency d=2-u>=0; if k>=1 optional letters, remaining D=6-2k; every positive-deficit F letter has v<=d. Forced zero-deficit (-1,2,-1) multiplicity must equal V>=0, and (0,2,0) supplies filler. Max n needed for difference is 9; for both distributions, 12.",review:"AUTHOR_EXACT_NOT_REVIEWED"};
}
process.stdout.write(JSON.stringify(verifyInfinite(),null,2)+'\n');
