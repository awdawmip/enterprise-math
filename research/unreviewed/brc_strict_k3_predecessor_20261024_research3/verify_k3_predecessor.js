// Author-side exact integer verifier for two-action strict K3 BRC witness.
// Execute: node verify_k3_predecessor.js
function verifyBRC() {
  "use strict";
  const weights=[[1n,22n,2n,3n],[1n,22n,2n,4n]];
  const denominators=[28n,29n];
  const edges=[[0,1],[0,2],[0,3],[2,3]];
  const degrees=[3n,1n,2n,2n];
  const pow=(a,n)=>a**BigInt(n);
  const invariant=(ok,msg)=>{if(!ok)throw Error(msg)};
  function P(x,y) {
    let edgeSum=0n,vertexSum=0n;
    for(const [i,j] of edges)edgeSum+=pow(weights[0][i]+weights[0][j],x)*pow(weights[1][i]+weights[1][j],y);
    for(let i=0;i<4;i++)vertexSum+=degrees[i]*pow(weights[0][i],x)*pow(weights[1][i],y);
    return edgeSum-vertexSum;
  }
  function U(x,y,a){return a===0?P(x+1,y)-denominators[0]*P(x,y):P(x,y+1)-denominators[1]*P(x,y)}
  const signs=[];
  for(let n=1;n<=4;n++)for(let x=0;x<=n;x++){
    const y=n-x,a=U(x,y,0),b=U(x,y,1),wanted=n===1?1:-1;
    invariant((a>0n?1:a<0n?-1:0)===wanted && (b>0n?1:b<0n?-1:0)===wanted,`increment sign n=${n} x=${x}`);
    signs.push({c:[x,y],U_alpha:a.toString(),U_beta:b.toString(),strict_sign:n===1?"POSITIVE":"NEGATIVE"});
  }
  const cuts=[];
  for(let n=1;n<=4;n++){
    const gap=6n*pow(22n,n)-5n*pow(23n,n);
    invariant(gap>0n,"strict K0 exclusion cut "+n);
    cuts.push({total_count:n,alpha_big_vertex_deficit:gap.toString(),number_of_count_states:n+1});
  }
  for(let a=0;a<2;a++)for(let i=0;i<4;i++){
    const s=weights[a].reduce((p,v)=>p+v,0n);
    invariant(s===denominators[a],"normalized action");
    invariant(weights[a][i]>0n,"strictly positive kernel");
  }
  invariant(weights[0][3]*denominators[1]!==weights[1][3]*denominators[0],"different action kernels");
  // Every positive demand follows one explicitly permitted spectral arc:
  // 0 -> 02, 1 -> 01, 2 -> 02, 3 -> 23.
  const route=[1,0,1,3];
  for(let i=0;i<4;i++)for(let a=0;a<2;a++){
    const [j,k]=edges[route[i]];
    invariant(weights[a][i]<=weights[a][j]+weights[a][k],"cross-action spectral order");
  }
  // The big label 1 has no other permitted outgoing arc.
  for(let j=1;j<4;j++){
    invariant(weights[0][1]>weights[0][edges[j][0]]+weights[0][edges[j][1]],"unique big-label arc");
  }
  const flowCertificates=[];
  let minimumMargin=null;
  for(let x=0;x<=5;x++){
    const y=5-x;
    for(let a=0;a<2;a++){
      const D=weights[a].map((wa,i)=>degrees[i]*(denominators[a]-wa)*pow(weights[0][i],x)*pow(weights[1][i],y));
      const C=edges.map(([i,j])=>(denominators[a]-weights[a][i]-weights[a][j])*pow(weights[0][i]+weights[0][j],x)*pow(weights[1][i]+weights[1][j],y));
      const used=[D[1],D[0]+D[2],0n,D[3]];
      const margin=C.map((c,j)=>c-used[j]);
      invariant(margin.every(z=>z>0n),"strict K0 flow margin "+x+","+y+"; next="+a);
      for(const z of margin)if(minimumMargin===null||z<minimumMargin)minimumMargin=z;
      flowCertificates.push({c:[x,y],next_action:a===0?"alpha":"beta",vertex_demand:D.map(String),edge_capacity:C.map(String),edge_used:used.map(String),edge_margin:margin.map(String)});
    }
  }
  function dpNumerator(word) {
    let states=Array(16).fill(0n);states[0]=1n;
    for(const a of word){
      const next=Array(16).fill(0n);
      for(let m=0;m<16;m++)if(states[m]!==0n)for(let i=0;i<4;i++)next[m|(1<<i)]+=states[m]*weights[a][i];
      states=next;
    }
    return edges.reduce((total,[i,j])=>total+states[(1<<i)|(1<<j)],0n);
  }
  let wordChecks=0,incrementChecks=0;
  for(let n=1;n<=8;n++)for(let code=0;code<2**n;code++){
    const word=Array.from({length:n},(_,k)=>(code>>k)&1);
    const x=word.filter(a=>a===0).length,y=n-x;
    const observed=dpNumerator(word);
    invariant(observed===P(x,y),"16-mask independent DP numerator for word="+word.join(""));
    wordChecks++;
    if(n<=4)for(let a=0;a<2;a++){
      invariant(dpNumerator([...word,a])-denominators[a]*observed===U(x,y,a),"16-mask independent DP delta");
      incrementChecks++;
    }
  }
  invariant(wordChecks===510 && incrementChecks===60,"exhaustive coverage counts");
  invariant(P(2,0)===66n,"explicit starting probability numerator");
  return {
    schema:"EM_BRC_STRICT_K3_EXACT_EVIDENCE_V1",
    model:{actions:{alpha:["1/28","22/28","2/28","3/28"],beta:["1/29","22/29","2/29","4/29"]},good_edges:["01","02","03","23"],degree:[3,1,2,2],start_count:[2,0]},
    proof_target:"K0={n>=5}, K1={n>=4}, K2={n>=3}, K3=S={n>=2}, strict negative increments for all n>=2",
    p_start_fraction:"33/392",
    all_count_state_increment_signs_n1_through_n4:signs,
    alpha_big_label_strict_K0_cuts_n1_through_n4:cuts,
    positive_K0_flows_for_all_count_states_at_n5:flowCertificates,
    min_positive_scaled_flow_margin:minimumMargin.toString(),
    independent_support_mask_dp:{all_action_words_length_1_through_8:wordChecks,independent_increment_comparisons_base_words_length_1_through_4:incrementChecks},
    algebra:"P(x,y)=23^(x+y)+3^(x+y)+4^x 5^y+5^x 6^y-22^(x+y)-2^(x+y+1)-2 3^x 4^y-3; delta=P/(28^x 29^y); U_a=P(c+e_a)-d_a P(c)",
    boundary:"empty history excluded from nonempty inclusion-exclusion; arbitrary-future result is proven by hereditary K0 and predecessor induction, not finite experiment",
    mathematical_status:"AUTHOR_SIDE_EXACT_VERIFIED_UNREVIEWED_NOT_ADMITTED"
  };
}
console.log(JSON.stringify(verifyBRC(), null, 2));
