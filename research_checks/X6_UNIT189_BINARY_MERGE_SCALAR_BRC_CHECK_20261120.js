#!/usr/bin/env node
/* Unit189: source-equivalent binary merge scalar reconstruction under signed X6 BRC.
   The frozen production module is not imported; R063 native benchmark is not rerun.
   Exact BigInt native DP is crosschecked against an independent factorial path formula. */
function run(){
 const ms=[[1,1,1,1,1,1],[1,2,1,2,1,2],[2,3,4,5,6,7]],maxN=5;
 const fac=[1n];for(let i=1;i<=maxN;i++)fac[i]=fac[i-1]*BigInt(i);
 const key=z=>z.join(",");
 const F=(z,m)=>m.map((mi,i)=>m.map((mj,j)=>mj*z[i]-mi*z[j]));
 const K=F=>{let s=[];for(let i=0;i<F.length;i++)for(let j=i+1;j<F.length;j++)s.push(F[i][j]);return s.join(",")};
 function nxt(states){let out=new Map();for(let [k,v] of states){let z=k.split(",").map(Number);for(let i=0;i<6;i++)for(let d of [-1,1]){let x=z.slice();x[i]+=d;let kk=key(x);out.set(kk,(out.get(kk)||0n)+v)}}return out}
 function cmp(k,n,s=[],out=[]){if(n===1){out.push([...s,k]);return out}for(let i=0;i<=k;i++)cmp(k-i,n-1,[...s,i],out);return out}
 function B(z,n){let p=z.map(x=>Math.max(x,0)),q=z.map(x=>Math.max(-x,0)),L=z.reduce((a,b)=>a+Math.abs(b),0);if(L>n||(n-L)%2)return 0n;let t=0n;for(let x of cmp((n-L)/2,6)){let den=1n;for(let i=0;i<6;i++)den*=fac[p[i]+x[i]]*fac[q[i]+x[i]];if(fac[n]%den)throw Error("invalid integer BRC");t+=fac[n]/den}return t}
 function merge(z,m,l,r){let fine=F(z,m),other=[0,1,2,3,4,5].filter(x=>x!==l&&x!==r),groups=[...other.map(x=>[x]),[l,r]],mC=groups.map(A=>A.reduce((s,i)=>s+m[i],0)),c=groups.map(A=>A.reduce((s,i)=>s+z[i],0)),W=groups.map(A=>groups.map(D=>A.reduce((s,i)=>s+D.reduce((v,j)=>v+fine[i][j],0),0)));
 if(JSON.stringify(W)!==JSON.stringify(F(c,mC)))throw Error("source coarsen disagree");
 return {fine,other,W,delta:fine[l][r]}}
 function restore(m,l,r,T){let {other,W,delta}=T,J=other.length,S=m[l]+m[r],result=Array.from({length:6},()=>Array(6).fill(0));
 for(let i=0;i<J;i++)for(let j=0;j<J;j++)result[other[i]][other[j]]=W[i][j];
 result[l][r]=delta;result[r][l]=-delta;
 for(let i=0;i<J;i++){let j=other[i],a=m[l]*W[J][i]+m[j]*delta,b=m[r]*W[J][i]-m[j]*delta;
 if(a%S||b%S)throw Error("noninteger original-field reconstruction");
 result[l][j]=a/S;result[j][l]=-a/S;result[r][j]=b/S;result[j][r]=-b/S}
 return result}
 const dps=[new Map([[key([0,0,0,0,0,0]),1n]])];
 for(let n=1;n<=maxN;n++)dps.push(nxt(dps[n-1]));
 let counts={capacity_vectors:ms.length,pairs_per_vector:15,horizons:maxN+1,native_dp_endpoints_checked_against_independent_factorial_brc:0,direct_source_coarsen_operations:0,exact_source_formula_field_reconstructions:0,exact_source_grand_total_reconstructions:0,original_field_fiber_vs_coarse_field_plus_scalar_brc_mass_checks:0,coarse_field_support_compares:0,full_native_12n_mass_checks:0,primitive_one_step_missing_scalar_witnesses:0,ordered_branch_history_nonrecoverability_witnesses:0,violations:0};
 for(let n=0;n<=maxN;n++){let sum=0n;for(const [k,v] of dps[n]){if(B(k.split(",").map(Number),n)!==v)throw Error("factorial BRC != primitive DP");counts.native_dp_endpoints_checked_against_independent_factorial_brc++;sum+=v}if(sum!==12n**BigInt(n))throw Error("total word count");counts.full_native_12n_mass_checks++}
 for(const m of ms)for(let l=0;l<6;l++)for(let r=l+1;r<6;r++){
  for(let n=0;n<=maxN;n++){
   const full=new Map(),reduced=new Map(),mapFull=new Map(),mapReduced=new Map();
   for(const [k,v] of dps[n]){
    let z=k.split(",").map(Number),T=merge(z,m,l,r);counts.direct_source_coarsen_operations++;
    let restored=restore(m,l,r,T);if(JSON.stringify(restored)!==JSON.stringify(T.fine))throw Error("full source field loss");counts.exact_source_formula_field_reconstructions++;
    const G=z.reduce((a,b)=>a+b,0),sumM=m.reduce((a,b)=>a+b,0);
    for(let i=0;i<6;i++){let x=m[i]*G+restored[i].reduce((a,b)=>a+b,0);if(x%sumM||x/sumM!==z[i])throw Error("source grand total inverse failed")}
    counts.exact_source_grand_total_reconstructions++;
    const fk=K(T.fine),rk=K(T.W)+"|"+T.delta;
    if(mapFull.has(fk)&&mapFull.get(fk)!==rk||mapReduced.has(rk)&&mapReduced.get(rk)!==fk)throw Error("field quotient inverse failed");
    mapFull.set(fk,rk);mapReduced.set(rk,fk);full.set(fk,(full.get(fk)||0n)+v);reduced.set(rk,(reduced.get(rk)||0n)+B(z,n));
   }
   if(full.size!==reduced.size)throw Error("field support size");
   for(const [fk,v] of full){if(reduced.get(mapFull.get(fk))!==v)throw Error("BRC field distribution mismatch");counts.original_field_fiber_vs_coarse_field_plus_scalar_brc_mass_checks++}
   counts.coarse_field_support_compares+=reduced.size;
  }
  let a=[0,0,0,0,0,0],b=a.slice();a[l]=1;b[r]=1;
  const Ta=merge(a,m,l,r),Tb=merge(b,m,l,r);
  if(K(Ta.W)!==K(Tb.W)||Ta.delta!==m[r]||Tb.delta!==-m[l])throw Error("one-step residual witness");
  counts.primitive_one_step_missing_scalar_witnesses++;
  let z=[0,0,0,0,0,0];z[l]=1;z[r]=1;
  if(B(z,2)!==2n||dps[2].get(key(z))!==2n)throw Error("ordered two-path witness");
  counts.ordered_branch_history_nonrecoverability_witnesses++;
 }
 return {schema:"X6_UNIT189_FROZEN_BINARY_MERGE_SCALAR_REPAIR_BRC_CHECK_V1",frozen_science_pin:"59538f585d037d09ef687b28715c4bc1a3f9fe03",historical_source_pin:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",capacity_vectors:ms,lengths:"0..5",counts,witness_one_step:{source_capacities:[1,2,1,2,1,2],left_index:0,right_index:1,coarse_field_equal_for_e_left_and_e_right:true,discarded_scalar_e_left:2,discarded_scalar_e_right:-1},witness_two_step:{endpoint:"e_left+e_right",two_named_ordered_words:true,brc_multiplicity:2,coarse_field_and_discarded_scalar_equal:true},actual_frozen_module_imported:false,original_native_R063_benchmark_rerun:false,independent_driver_review:false,violations:0}
}
const result=run();
console.log(JSON.stringify(result,null,2));
