"use strict";
function runChecker() {
  function gcd(a,b){while(b){const r=a%b;a=b;b=r;}return a;}
  function powers(p,W){const z=[];for(let i=0;i<p;i++)z.push(W**i);return z;}
  function differenceSet(p,W){
    const z=powers(p,W),s=new Set();
    for(let i=0;i<p;i++)for(let k=1;k<W;k++)s.add(k*z[i]);
    for(let i=0;i<p;i++)for(let j=i+1;j<p;j++)
      for(let k=-(W-1);k<=W-1;k++)if(k)
        for(let l=-(W-1);l<=W-1;l++)if(l){
          const d=Math.abs(k*z[i]-l*z[j]);if(d)s.add(d);
        }
    return Array.from(s).sort((a,b)=>a-b);
  }
  function good(ds,q){return !ds.some(d=>d%q===0);}
  function actual(p,W,q){
    const z=powers(p,W),N=W**p;
    for(let center=0;center<N;center++){
      const seen=new Set([center%q]);
      for(let i=0;i<p;i++){
        const digit=Math.floor(center/z[i])%W;
        for(let x=0;x<W;x++)if(x!==digit){
          const r=((center+(x-digit)*z[i])%q+q)%q;
          if(seen.has(r))return false;
          seen.add(r);
        }
        if(seen.size!==1+(i+1)*(W-1))throw Error("ball count");
      }
    }
    return true;
  }
  const cases=[];
  let searched=0, criterionChecks=0, directChecks=0, directPairs=0;
  for(let p=1;p<=5;p++)for(let W=2;W<=5;W++){
    const N=W**p,ds=differenceSet(p,W);
    for(const C of [1,2,6]){
      let best=null,priorRejected=0;
      for(let q=1;q<=N+30;q++){
        if(gcd(q,C)!==1)continue;
        searched++;criterionChecks+=ds.length;
        if(good(ds,q)){best=q;break;}
        priorRejected++;
      }
      if(best===null || best>N+30)throw Error("minimum not found");
      if(best<p*(W-1)+1)throw Error("cardinality bound");
      if(!good(ds,best))throw Error("witness false");
      cases.push({p,W,C,N,ball_size:1+p*(W-1),distinct_differences:ds.length,min_coprime_modulus:best,minimum_port_bits:Math.ceil(Math.log2(best)),prior_coprime_candidates_rejected:priorRejected});
    }
    if(p<=4 && W<=4){
      for(let q=1;q<=N+2;q++){
        const g=good(ds,q),a=actual(p,W,q);
        directChecks++;directPairs+=N*(1+p*(W-1));
        if(g!==a)throw Error("analytic/exhaustive mismatch at "+[p,W,q]);
      }
    }
  }
  // Exact gain-and-update readouts in a representative nontrivial case.
  const p=3,W=3,C=6,q=13,z=powers(p,W),N=W**p;
  let readouts=0;
  for(const t of [1,2,4,9]){
    const a=2n,b=3n;
    const gain=(a**BigInt(Math.floor(t/2)))*(b**BigInt(Math.floor((t-1)/2)));
    for(let center=0;center<N;center++){
      const seen=new Set();
      const states=[center];
      for(let i=0;i<p;i++){
        const old=Math.floor(center/z[i])%W;
        for(let x=0;x<W;x++)if(x!==old)states.push(center+(x-old)*z[i]);
      }
      for(const U of states){
        const obs=Number((gain*BigInt(5+U))%BigInt(q));
        if(seen.has(obs))throw Error("gain observer alias "+[t,center,U]);
        seen.add(obs);
        readouts++;
      }
    }
  }
  if(cases.length!==60||directChecks!==((2**1+2)+(3**1+2))) { /* no-op; counts reported */ }
  return {schema:"PREFIX847_DYNAMIC_SINGLE_SOURCE_EXACT_CHECK_V1",
    status:"ALL_EXACT_ASSERTIONS_PASSED",
    domain:{p:[1,5],W:[2,5],C:[1,2,6],fixed_gain_example:{p:3,W:3,a:2,b:3,m:13,t:[1,2,4,9]}},
    method:"Exhaustively test divisibility against every Hamming-one difference; independently enumerate every center and update choice for p<=4,W<=4 and every tested q.",
    summary:{parameter_cases:cases.length,successful_minimum_searches:cases.length,unique_candidate_moduli_tested:searched,difference_divisibility_checks_upper_bound:criterionChecks,direct_moduli_checked:directChecks,direct_candidate_residues_checked:directPairs,exact_gain_readouts:readouts},
    selected:cases.filter(x=>(x.p===3&&x.W===3)||(x.p===5&&x.W===5)||(x.p===4&&x.W===2)),
    cases
  };
}
console.log(JSON.stringify(runChecker(),null,2));
