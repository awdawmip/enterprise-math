// PREFIX-468 exact BRC base-state rational-series certificate.
// Run: node prefix468_exact_base_series_certificate.js
// Model: P000 native X6 signed chart, 11 letters, "ab" gate, valuation A,C.
// All computations use exact JavaScript integer arithmetic; no floating-point equality.
"use strict";
function certificate() {
  const fail=(msg)=>{throw Error(msg);};
  const P=[1n,3n,5n,6n,4n,-1n,-4n,-2n];
  const D=[1n,-8n,28n,-57n,78n,-84n,84n,-78n,57n,-28n,8n,-1n];
  const N=20, series=[];
  for(let n=0;n<=N;n++){
    let v=P[n]||0n;
    for(let k=1;k<=Math.min(n,11);k++)v-=D[k]*series[n-k];
    series.push(v);
  }
  const key=(count)=>count.join(",");
  function base(count) {
    const y=[], p=[];
    for(let i=0;i<5;i++){
      const plus=count[1+2*i],minus=count[2+2*i];
      y.push(plus-minus);p.push(Math.min(plus,minus));
    }
    return [count[0],...y,p[1]+2*p[3]+p[4],p[2]+p[4]].join(",");
  }
  const initial=Array(11).fill(0);
  let active=new Map([[key(initial)+"|2",{count:initial,q:2}]]);
  const lines=["PREFIX-468 EXACT EXECUTION; integer certificate",
    "scientific_pin=f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "G(z)=(1+2z^2)(1+z)^2(1+z-z^3)/((1-z)^8(1-z^3))",
    "n | rational_series_Bn | reachable_parikh_count | legal_DFA_parikh_count | direct_base_Bn"];
  for(let n=0;n<=8;n++){
    const dfaParikh=new Set(),dfaBase=new Set();
    for(const item of active.values()){
      dfaParikh.add(key(item.count));
      dfaBase.add(base(item.count));
    }
    const predictedParikh=new Set(), predictedBase=new Set();
    const cnt=Array(11).fill(0);
    function enumerate(i,left){
      if(i===10){
        cnt[i]=left;
        const s=cnt[0],aplus=cnt[1],bplus=cnt[3];
        if(s>Math.min(aplus,bplus)+1)return;
        predictedParikh.add(key(cnt));
        predictedBase.add(base(cnt));
        return;
      }
      for(let j=0;j<=left;j++){cnt[i]=j;enumerate(i+1,left-j);}
    }
    enumerate(0,n);
    if(dfaParikh.size!==predictedParikh.size) fail("Parikh size mismatch n="+n);
    for(const k of dfaParikh) if(!predictedParikh.has(k))fail("DFA -> Parikh mismatch n="+n);
    for(const k of predictedParikh)if(!dfaParikh.has(k))fail("Parikh -> DFA mismatch n="+n);
    if(dfaBase.size!==predictedBase.size || BigInt(dfaBase.size)!==series[n])
      fail("B_n mismatch n="+n);
    for(const k of dfaBase)if(!predictedBase.has(k))fail("base mismatch n="+n);
    lines.push([n,String(series[n]),predictedParikh.size,dfaParikh.size,dfaBase.size].join(" | "));
    if(n===8)break;
    const next=new Map();
    for(const item of active.values()){
      const c=item.count, q=item.q;
      for(let j=0;j<11;j++){
        if(j===0 && n>0 && q!==2)continue;
        const nq=j===1?1:(j===3 && q===1?2:0);
        const nc=c.slice();nc[j]++;
        const k=key(nc)+"|"+nq;
        if(!next.has(k))next.set(k,{count:nc,q:nq});
      }
    }
    active=next;
  }
  lines.push("coefficient_B9_to_B20="+series.slice(9).map(String).join(","));
  lines.push("recurrence=denominator D(z) coefficients: "+D.map(String).join(","));
  lines.push("ALL_CHECKS_PASS");
  return lines.join("\n")+"\n";
}
console.log(certificate());
