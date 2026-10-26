"use strict";
/* R311 exact BigInt verifier for the A>U majorant threshold (NOT the true D_d sign).
   No floating arithmetic is used for certificate decisions. */
function verifyR311() {
  function choose(n,k) {
    if(k<0||k>n)return 0n;
    k=Math.min(k,n-k);
    let a=1n;
    for(let i=1;i<=k;i++)a=a*BigInt(n-k+i)/BigInt(i);
    return a;
  }
  function weights(d) {
    const w=Array(d-1).fill(0n);
    for(let r=1;r<d;r++){
      const end=Math.min(r,d-r);
      let a=1n,b=1n;
      for(let t=1;t<=end;t++){
        a=a*BigInt(d-r-t+1)/BigInt(t);
        w[d-r-t]+=a*b;
        if(t<end)b=b*BigInt(r-t)/BigInt(t);
      }
    }
    return w;
  }
  function gap(d,n,w) {
    if(n<4*d+4)throw Error("outside primary certificate domain");
    let v=1n,U=w[0],j=0;
    for(j=1;j<=d-2;j++){
      v=v*BigInt(n-j+1)/BigInt(j);
      U+=v*w[j];
    }
    return choose(n-2*d-4,d-1)-U;
  }
  function threshold(d) {
    const w=weights(d);
    let lo=4*d+4, hi=Math.floor((12*d*d+4)/5);
    if(gap(d,hi,w)<=0n)throw Error("R309 upper bracket failed: "+d);
    if(gap(d,lo,w)>0n) return {n:lo,left:null,right:gap(d,lo,w)};
    while(hi-lo>1){
      const mid=Math.floor((lo+hi)/2);
      if(gap(d,mid,w)>0n)hi=mid; else lo=mid;
    }
    return {n:hi,left:gap(d,hi-1,w),right:gap(d,hi,w)};
  }
  let c=2.35;
  for(let i=0;i<12;i++){
    const e=Math.exp(-2/c);
    c-=(c*e-1)/(e*(1+2/c));
  }
  const beta=(4*c+3.5-2*c*c)/(c+2);
  const gamma=(6*c**6-30*c**5-327*c**4-283*c**3-54*c*c+18*c+1)/(6*c*c*(c+2)**3);
  const expected=[[3,20],[4,36],[5,57],[10,235],[20,942],[30,2119],[60,8466],[100,23496],[150,52839],[250,146712],[400,375488],[600,844725],[800,1501621],[1000,2346178],[1500,5278582]];
  const checks=[];
  for(const [d,want] of expected){
    const got=threshold(d);
    if(got.n!==want||got.right<=0n||(got.left!==null&&got.left>0n))throw Error("threshold mismatch d="+d);
    const candidate=Math.floor(c*d*d+beta*d+gamma)+1;
    checks.push({d,n_star:got.n,previous_sign:got.left===null?"OUT_OF_DOMAIN":got.left<0n?"NEGATIVE":"ZERO",at_sign:"POSITIVE",
      previous_gap_digits:got.left===null?null:got.left.toString().replace("-","").length,
      at_gap_digits:got.right.toString().length,
      second_order_predicted_integer:candidate,
      prediction_matches: candidate===got.n});
  }
  return {schema:"EM_R311_MAJORANT_SECONDARY_THRESHOLD_EXACT_EVIDENCE_V1",
    status:"PASS",arithmetic:"JavaScript BigInt, all threshold crossing signs exact; Math.exp only display asymptotic predictions",
    definition:"A=binom(n-2d-4,d-1), U=sum_r,t binom(d-r,t)binom(r-1,t-1)binom(n,d-r-t), n>=4d+4",
    samples:checks,checked_count:checks.length,
    approximations_only:{c_star:c,beta,gamma},
    scope:"These are complete certificate crossing thresholds for the listed d only, not a proof of the d->infinity asymptotic and not the true BRC fibre D_d sign",
    proof_status:"Author-side symbolic derivation supplied separately; independent Driver review pending"};
}
if(typeof module!=="undefined")module.exports={verifyR311};
