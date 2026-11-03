"use strict";
function verify() {
  const POW=(a,n)=>a**BigInt(n);
  const CH=(n,k)=>{let v=1n;for(let i=1;i<=k;i++)v=v*BigInt(n+1-i)/BigInt(i);return v;};
  const gcd=(a,b)=>{while(b!==0n){const t=a%b;a=b;b=t;}return a;};
  const min=(a,b)=>a<b?a:b;
  const cases=[
    {betaE:"0",den:21n,full:[0n,0n,11n,10n]},
    {betaE:"1/4",den:336n,full:[84n,63n,99n,90n]},
    {betaE:"1/2",den:84n,full:[42n,21n,11n,10n]}
  ];
  let checks=0, ternary_cases=0, full_label_cases=0, summary=[];
  function seqMin(n, rowsPlus, rowsMinus, m) {
    let sm=0n;
    function recur(i,u,v){
      if(i===n){sm+=min(u,v);return;}
      for(let t=0;t<m;t++)recur(i+1,u*rowsPlus[i][t],v*rowsMinus[i][t]);
    }
    recur(0,1n,1n);
    return sm;
  }
  function theoretical(n,E,I){
    let ans=0n;
    for(let k=0;k<=n;k++){
      let cond=0n;
      for(let j=0;j<=k;j++){
        const r=CH(k,j);
        cond+=r*min(POW(11n,j)*POW(10n,k-j),POW(10n,j)*POW(11n,k-j));
      }
      ans+=CH(n,k)*POW(E,n-k)*POW(I,k)*POW(21n,n-k)*cond;
    }
    return ans; // denominator 2*den^n*21^n
  }
  for(const C of cases){
    const [A,B,S,F]=C.full, D=C.den, E=A+B, I=S+F;
    if(E+I!==D || S*10n!==F*11n)throw Error("Invalid full-row kernel");
    const ternaryPlus=[E,S,F],ternaryMinus=[E,F,S];
    const plus0=C.full,minus0=[A,B,F,S],plus1=minus0,minus1=plus0;
    const risks={};
    for(let n=0;n<=8;n++){
      let num=seqMin(n,Array(n).fill(ternaryPlus),Array(n).fill(ternaryMinus),3);
      const theory=theoretical(n,E,I);
      if(num*POW(21n,n)!==theory) throw Error(`Ternary likelihood mismatch beta=${C.betaE} n=${n}`);
      checks++;ternary_cases++;
      if(n===1 && num*21n !== 21n*D-I) throw Error("One-sample formula failed");
      if(n===2 && num*21n !== 21n*D*D-(2n*I*D-I*I)) throw Error("Two-sample formula failed");
      if([1,2,3,4,6,8].includes(n)){
        const den=2n*POW(D,n),g=gcd(num,den);
        risks["n"+n]=`${num/g}/${den/g}`;
      }
    }
    for(let n=0;n<=5;n++){
      const trinum=seqMin(n,Array(n).fill(ternaryPlus),Array(n).fill(ternaryMinus),3);
      for(let n0=0;n0<=n;n0++){
        const plus=Array(n0).fill(plus0).concat(Array(n-n0).fill(plus1));
        const minus=Array(n0).fill(minus0).concat(Array(n-n0).fill(minus1));
        const rawNum=seqMin(n,plus,minus,4);
        if(rawNum!==trinum)throw Error(`Full-label allocation mismatch beta=${C.betaE} n=${n} n0=${n0}`);
        checks++;full_label_cases++;
      }
    }
    summary.push({beta_E:C.betaE,erasure_probability:`${E}/${D}`,informative_probability:`${I}/${D}`,exact_Bayes_errors:risks});
  }
  return {verdict:"PASS_BRC_S23_FINITE_SAMPLE_BINARY_ERASURE_20261103",model:"S23 four-outcome stopping mixtures; two-state witness h=1/42",arithmetic:"BigInt exact integers",max_samples_ternary:8,max_samples_full_four_outcome:5,ternary_checks:ternary_cases,full_label_allocation_checks:full_label_cases,total_checks:checks,cases:summary};
}
console.log(JSON.stringify(verify(),null,2));
