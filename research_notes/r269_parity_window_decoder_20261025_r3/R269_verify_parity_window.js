// R269 exact finite verifier. node R269_verify_parity_window.js
// Universal proof is analytic: tests verify encoding and finite witnesses.
"use strict";
function then(g,h){return [h[0]*g[0],h[0]*g[1]+h[1]];}
function act(g,x,q){return ((g[0]*x+g[1])%q+q)%q;}
function runEvidence(){
  const cases=[];let toeplitz=0,readouts=0,compositions=0;
  for(let L=0;L<=12;L++){
    const N=L+1,q=N%2?N:N+1;
    if(q%2!==1||q<N||q!==(L%2?L+2:L+1))throw Error("dimension");
    for(let i=0;i<N;i++)for(let j=0;j<N;j++){
      const entry=(i===j?1:0);if(entry!==Number(i-j===0))throw Error("toeplitz");
      toeplitz++;
    }
    for(const eps of [-1,1])for(let j=-L;j<=L;j++){
      const got=Number(act([eps,2*j],0,q)===0);
      if(got!==Number(j===0))throw Error("readout");
      readouts++;
    }
    for(const eps of [-1,1])for(let k=0;k<q;k++)
    for(const eta of [-1,1])for(let b=0;b<q;b++)
    for(let x=0;x<q;x++){
      const g=[eps,k],h=[eta,b];
      if(act(then(g,h),x,q)!==act(h,act(g,x,q),q))throw Error("group law");
      compositions++;
    }
    cases.push({L,N,minimal_dimension:q,R267_full_window_dimension:2*L+1});
  }
  const reciprocal_examples=[];
  for(let a=-5;a<=5;a++){
    const A=[[a,1],[a*a-1,a]];
    const B=[0,1].map(i=>[0,1].map(j=>A[i][0]*A[0][j]+A[i][1]*A[1][j]));
    const p=B[0][0]+1,s=B[1][1]+1,det=p*s-B[0][1]*B[1][0];
    if(det!==(2*a)**2)throw Error("SL2 reciprocal square");
    reciprocal_examples.push({a,det_I_plus_A2:det});
  }
  if(toeplitz!==819||readouts!==338||compositions!==38020)throw Error("coverage mismatch");
  return {
    schema:"EM_R269_PARITY_WINDOW_AUTHOR_EVIDENCE_V1",
    classification:"AUTHOR_SIDE_EXACT_FINITE_CHECKS_NOT_UNIVERSAL_PROOF",
    range_L:[0,12],case_count:cases.length,
    toeplitz_entries_checked:toeplitz,
    quotient_readouts_checked:readouts,
    quotient_action_compositions_checked:compositions,
    reciprocal_SL2_determinant_cases:reciprocal_examples,
    cases,
    analytic_obligations:[
      "rank(T)=L+1 on even translations",
      "when N even and rank N, charpoly(A^2)=x^N+1",
      "reflection gives reciprocal rational charpoly(A)",
      "det(I+A^2) is rational square yet would equal 2",
      "odd cyclic quotient realizes bound"
    ],
    native_source_runtime_executed:false,
    driver_reviewed:false
  };
}
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
  console.log(JSON.stringify(runEvidence(),null,2));
