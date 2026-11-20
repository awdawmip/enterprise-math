#!/usr/bin/env node
/* X6 Unit188 source-equivalent frozen A3 coarsening and exact signed six-axis BRC pushforward.
 * No production import; no R063 native benchmark; finite exact BigInt checks.
 * Execute: node X6_UNIT188_FROZEN_COARSEN_BRC_PUSHFORWARD_CHECK_20261120.js
 */
function numericCheck(){
  const d=6;
  const capacityVectors=[[1,1,1,1,1,1],[1,2,1,2,1,2],[2,3,2,3,2,4]];
  const partitions=[[[0,1],[2,3,4,5]],[[0,1,2],[3,4,5]],[[0,2],[1,3],[4,5]],[[0],[1,2,3,4,5]],[[0],[1],[2],[3],[4],[5]],[[0,1,2,3,4,5]]];
  const horizonMax=6;
  function evolve(states,multiplicities){
    const next=new Map();
    for(const [key,count] of states){
      const z=key.split(",").map(Number);
      for(let a=0;a<multiplicities.length;a++)for(const sign of [-1,1]){
        const w=z.slice();w[a]+=sign;const k=w.join(",");
        next.set(k,(next.get(k)||0n)+count*BigInt(multiplicities[a]));
      }
    }
    return next;
  }
  function field(z,m){
    return m.map((mi,i)=>m.map((mj,j)=>mj*z[i]-mi*z[j]));
  }
  function fieldKey(z,m){
    const out=[];
    for(let i=0;i<z.length;i++)for(let j=i+1;j<z.length;j++)out.push(m[j]*z[i]-m[i]*z[j]);
    return out.join(",");
  }
  const native=[new Map([[Array(d).fill(0).join(","),1n]])];
  for(let n=1;n<=horizonMax;n++)native.push(evolve(native[n-1],Array(d).fill(1)));
  let counts={capacity_vectors:capacityVectors.length,partitions:partitions.length,horizons:horizonMax+1,coarse_field_fibers:0,grouped_endpoint_states:0,production_coarsen_checks:0,source_total_recovery_checks:0,grouped_vs_native_disagreements:0,coarsen_source_disagreements:0,total_mass_violations:0,maximum_native_states:native[horizonMax].size};
  let witness=null,capacityVsMultiplicity=null;
  for(const m of capacityVectors)for(const partition of partitions){
    const r=partition.map(g=>g.length);
    const mCoarse=partition.map(g=>g.reduce((s,i)=>s+m[i],0));
    let groupStates=new Map([[Array(partition.length).fill(0).join(","),1n]]);
    for(let M=0;M<=horizonMax;M++){
      if(M)groupStates=evolve(groupStates,r);
      const actual=new Map(),theoretical=new Map();
      let fineZeroCount=0n;
      for(const [key,count] of native[M]){
        const z=key.split(",").map(Number);
        const C=partition.map(g=>g.reduce((s,i)=>s+z[i],0));
        const W=fieldKey(C,mCoarse);
        actual.set(W,(actual.get(W)||0n)+count);
        const fine=field(z,m);
        const reconstructedCoarse=partition.map(A=>partition.map(B=>A.reduce((s,i)=>s+B.reduce((q,j)=>q+fine[i][j],0),0)));
        const directCoarse=field(C,mCoarse);
        if(JSON.stringify(reconstructedCoarse)!==JSON.stringify(directCoarse)){
          counts.coarsen_source_disagreements++;
          throw new Error("Production coarsening mismatch: "+JSON.stringify({m,partition,M,z}));
        }
        counts.production_coarsen_checks++;
        const sumCapacity=mCoarse.reduce((a,b)=>a+b,0);
        const fullTotal=C.reduce((a,b)=>a+b,0);
        const recovered=C.map((_,i)=>{
          const num=mCoarse[i]*fullTotal+directCoarse[i].reduce((a,b)=>a+b,0);
          if(num%sumCapacity!==0)throw new Error("Nonintegral source grand total");
          return num/sumCapacity;
        });
        if(JSON.stringify(recovered)!==JSON.stringify(C))throw new Error("Source grand total recovery mismatch");
        counts.source_total_recovery_checks++;
        if(fine.every(row=>row.every(x=>x===0)))fineZeroCount+=count;
      }
      for(const [key,count] of groupStates){
        const C=key.split(",").map(Number);
        const W=fieldKey(C,mCoarse);
        theoretical.set(W,(theoretical.get(W)||0n)+count);
      }
      if(actual.size!==theoretical.size)throw new Error("Field support disagreement");
      let total=0n;
      for(const [W,mass] of actual){
        if(mass!==theoretical.get(W)){
          counts.grouped_vs_native_disagreements++;
          throw new Error("Native versus grouped BRC coefficient mismatch "+JSON.stringify({m,partition,M,W,native:String(mass),grouped:String(theoretical.get(W))}));
        }
        counts.coarse_field_fibers++;
        total+=mass;
      }
      counts.grouped_endpoint_states+=groupStates.size;
      if(total!==12n**BigInt(M)){
        counts.total_mass_violations++;
        throw new Error("Total path words failed to equal 12^M");
      }
      if(m.every(x=>x===1)&&partition.length===2&&partition[0].length===2&&partition[1].length===4&&M===3){
        witness={M,capacities:m,partition,coarse_capacities:mCoarse,primitive_group_multiplicities:r,coarse_field:"0",coarse_zero_field_native_path_count:String(actual.get("0")),full_fine_zero_field_native_path_count:String(fineZeroCount),coarse_zero_field_lifts:[[1,2],[-1,-2]],paths_per_lift:"96"};
      }
      if(m.join(",")==="1,2,1,2,1,2"&&partition.length===2&&partition[0].length===2&&partition[1].length===4&&M===1){
        const c="1,0";capacityVsMultiplicity={native_group_A_plus_paths:String(groupStates.get(c)),incorrect_using_coarse_capacity:String(mCoarse[0]),actual_group_multiplicity:r[0],coarse_capacity:mCoarse[0]};
      }
    }
  }
  if(!witness||witness.coarse_zero_field_native_path_count!=="192"||witness.full_fine_zero_field_native_path_count!=="0"||!capacityVsMultiplicity||capacityVsMultiplicity.native_group_A_plus_paths!=="2")throw new Error("Explicit witness check failed");
  return {schema:"X6_UNIT188_COARSEN_NATIVE_BRC_PUSHFORWARD_CHECK_V1",scientific_pin:"59538f585d037d09ef687b28715c4bc1a3f9fe03",historical_source_pin:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",counts,explicit_witness:witness,nonuniform_capacity_vs_branch_multiplicity:capacityVsMultiplicity,primitive_event_model:"12 directed signed unit axes on chosen X6 Cell chart",original_R063_benchmark_rerun:false,real_frozen_production_module_directly_imported:false,author_check_status:"FINITE_EXACT_BIGINT_DP_CROSSCHECK; NOT_INDEPENDENT_REVIEW",violations:0};
}

const certificate=numericCheck();
console.log(JSON.stringify(certificate,null,2));
