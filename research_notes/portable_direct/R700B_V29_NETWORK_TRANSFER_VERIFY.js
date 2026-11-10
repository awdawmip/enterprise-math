/* R700b native V29 matched-TRANSFER repair of positive-BRC PASS ring observer.
   Run: node R700B_V29_NETWORK_TRANSFER_VERIFY.js. */
const result=(function certifyB() {
  const N=[24,18,6,12];
  const base=(v)=>[v[0]-v[3],v[1]-v[0],v[2]-v[1],v[3]-v[2]];
  const recover=(u,s)=>{
    const e=(s+u[0]-2*u[1]-u[2])/4;
    return [e,e+u[1],e+u[1]+u[2],e-u[0]];
  };
  let states=0, balancedTransferCases=0;
  for(let e=0;e<=N[0];e++)for(let t=0;t<=N[1];t++)
  for(let c=0;c<=N[2];c++)for(let z=0;z<=N[3];z++) {
    const v=[e,t,c,z],s=e+t+c+z;if(s===0)continue;
    states++;
    const original=base(v);
    for(let outPort=0;outPort<4;outPort++)for(let inPort=0;inPort<4;inPort++){
      const Rin=[0,0,0,0],Rout=[0,0,0,0];Rin[inPort]++;Rout[outPort]++;
      const b=Rin.map((n,i)=>n-Rout[i]), observed=original.map((n,i)=>n+b[i]);
      const corrected=observed.map((n,i)=>n-Rin[i]+Rout[i]);
      const got=recover(corrected,s);
      if(got.some((x,i)=>x!==v[i])||observed.reduce((a,b)=>a+b,0)!==0)
        throw Error("R700b transfer correction failed");
      balancedTransferCases++;
    }
  }
  if(states!==43224||balancedTransferCases!==691584)throw Error("coverage");
  const vA=[1,0,0,0],vB=[0,1,0,0];
  const observedA=base(vA).map((n,i)=>n+(i===1?1:0)-(i===0?1:0));
  const observedB=base(vB).map((n,i)=>n+(i===2?1:0)-(i===1?1:0));
  if(observedA.join()!=="0,0,0,0"||observedB.join()!=="0,0,0,0")throw Error("collision witness");
  return {schema:"EM_R700B_V29_BOUNDARY_REPAIR_V1",status:"R700B_BOUNDARY_REPAIR_EXACT_PASS",
    parent:"R700@4bcc0f651f15c681e07520d50553897ad395aeb4",
    source_model:{capacities:N,group_to_PASS:["0->1","1->2","2->3","3->0"]},
    histograms_checked:states,one_in_one_out_matched_transfer_cases:balancedTransferCases,
    counterexample:{caseA:{group_counts:vA,ring_PASS:"0->1",outgoing_transfer:"x:0 -> y:0",incoming_transfer:"y:1 -> x:1",observed_u:observedA,P:1},
      caseB:{group_counts:vB,ring_PASS:"1->2",outgoing_transfer:"x:1 -> y:1",incoming_transfer:"y:2 -> x:2",observed_u:observedB,P:1}},
    exact_repair:"u_internal = u_observed - Rin + Rout; s = P_after - P_baseline; v=R700 inverse(u_internal,s)",
    interpretation:"Full V29 network transfer counts must be retained or compensated to recover ring source histogram. V29 grammar specified, physical X6 Link/Port path realization unresolved."};
})();
console.log(JSON.stringify(result,null,2));
