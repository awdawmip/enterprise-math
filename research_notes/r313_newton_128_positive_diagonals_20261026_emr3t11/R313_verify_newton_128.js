'use strict';
// Reproducible R313 checker. Coefficient-sign tests are exact BigInt.
function verifyR313(S) {
  const maxN=Math.max(3*S+8,205);
  const pascal=[[1n]];
  for(let n=1;n<=maxN;n++){
    const a=Array(n+1).fill(1n);
    for(let k=1;k<n;k++)a[k]=pascal[n-1][k-1]+pascal[n-1][k];
    pascal.push(a);
  }
  const C=(n,k)=>{
    if(!Number.isInteger(n)||!Number.isInteger(k))throw Error("Noninteger binomial index");
    if(n<0||k<0||k>n)return 0n;
    if(n>maxN)throw Error("Pascal range insufficient: "+n);
    return pascal[n][k];
  };
  const mul=(a,b)=>{
    const out=Array(a.length+b.length-1).fill(0n);
    for(let i=0;i<a.length;i++)if(a[i]!==0n)
      for(let j=0;j<b.length;j++)if(b[j]!==0n)out[i+j]+=a[i]*b[j];
    return out;
  };
  const dCoef=i=>[0n,-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)];
  const nCoef=i=>i===0?[1n]:[0n,-C(3,i-1),-C(6,i-1),C(8,i-2)];
  const pows=[[1n]];
  for(let i=1;i<=S;i++)pows.push(mul(pows[i-1],[1n,-1n]));
  const M=[[1n]];
  const samples={};
  let checked=0,strict=0,equal=0;
  for(let s=0;s<=S;s++){
    if(s>0){
      const m=mul(nCoef(s),pows[s]);
      for(let i=1;i<=Math.min(s,12);i++){
        const term=mul(mul(dCoef(i),M[s-i]),pows[i-1]);
        while(m.length<term.length)m.push(0n);
        for(let j=0;j<term.length;j++)m[j]-=term[j];
      }
      while(m.length>1&&m[m.length-1]===0n)m.pop();
      if(m.length-1>2*s+1)throw Error("Degree bound failed at s="+s);
      M.push(m);
    }
    const m=M[s], floor=1n<<BigInt(s), coeff=[];
    for(let k=0;k<=s;k++){
      let a=0n;
      for(let j=0;j<m.length;j++)if(m[j]!==0n)
        a+=m[j]*C(2*s+1-j,s-k);
      if(a<floor)throw Error("Counterexample at s="+s+" k="+k+" coefficient="+a);
      coeff.push(a);
      if(a===floor)equal++;else strict++;
      checked++;
    }
    if(coeff[s]!==floor)throw Error("Top Newton difference drift at s="+s);
    if([0,1,5,6,16,32,64,96,128].includes(s))
      samples[String(s)]={
        degree_m:m.length-1,
        min_relative_bound:floor.toString(),
        k0:coeff[0].toString(),
        kmiddle:coeff[Math.floor(s/2)].toString(),
        ks:coeff[s].toString(),
        all_ge_two_to_s:true
      };
  }
  if(checked!==(S+1)*(S+2)/2)throw Error("Coverage count wrong");
  const qMul=[[[1,1n],[2,-1n],[3,1n]],[[3,1n],[4,-3n],[5,2n]],[[6,-1n],[7,2n],[8,-1n]],[[8,1n],[9,-3n],[10,3n],[11,-1n]]];
  const Q=[[0n,0n,0n,1n],[0n,0n,0n,0n,0n,0n,1n]];
  let independentChecks=0;
  for(let d=2;d<=40;d++){
    const q=Array(3*d+4).fill(0n);
    for(let r=1;r<=4;r++)if(d>=r)for(const [shift,mulval] of qMul[r-1])
      for(let j=0;j<Q[d-r].length;j++)
        if(Q[d-r][j]!==0n)q[j+shift]+=Q[d-r][j]*mulval;
    if(d===2){q[6]-=1n;q[7]+=1n;}
    if(d===3){q[8]+=1n;q[9]-=2n;q[10]+=1n;}
    Q.push(q);
    for(let s=0;s<d;s++){
      let fromQ=0n,fromM=0n;
      for(let j=0;j<q.length;j++)if(q[j]!==0n)fromQ+=q[j]*C(5*d+3-j,s);
      for(let j=0;j<M[s].length;j++)if(M[s][j]!==0n)
        fromM+=M[s][j]*C(d+s-j,s);
      if(fromQ!==fromM)throw Error("Independent R307 recurrence mismatch d="+d+" s="+s);
      independentChecks++;
    }
  }
  if(independentChecks!==819)throw Error("Crosscheck scope changed");
  return {
    schema:"EM_R313_NEWTON_128_DIAGONALS_EXACT_EVIDENCE_V1",
    status:"PASS",
    model:"Positive ordered six-edge BRC complete effect fibre difference, R305/R307 rational generating kernel",
    arithmetic:"JavaScript BigInt only, exact integer Pascal binomial recurrence and polynomial arithmetic; no floating point for signs",
    theorem:"For every integer 0<=s<=128 and every integer d>=max(2,s+1), K_s(d) >= 2^s * sum_{k=0}^s binom(d-s-1,k) > 0",
    transformed_kernel:"G(u,z)=(1-u(1+u)^3 z-u(1+u)^6 z^2+u^2(1+u)^8 z^3)/((1+u(1+u)^2 z)(1-(1+u)^4 z+2u(1+u)^5 z^2-u^2(1+u)^7 z^3))",
    coefficient_recursion:"M_0=1; M_s=n_s*(1-z)^s-sum_{i=1}^{min(s,12)} delta_i*M_{s-i}*(1-z)^{i-1}; deg M_s<=2s+1",
    tested_s_range:[0,S],
    certificate_cells:checked,
    strict_over_2_to_s:strict,
    equal_to_2_to_s:equal,
    every_certificate_a_s_k_at_least_2_to_s:true,
    independent_old_Q_recurrence_crosscheck:{d_min:2,d_max:40,all_s_less_d:true,exact_comparisons:independentChecks,result:"PASS"},
    samples,
    scope:"Finite s-index 0..128, unbounded d by proven Newton-polynomial identity; not all unbounded s",
    source_state:{account_snapshot:"6b84efafacb760e2e0733177c29040fdc3d87b5c",em_snapshot:"feb91b5fff944892e8e96f61e75bacfea47c4cb2",native_owner:"UNVERIFIED_CONTROL_QUOTA",native_session:"STATIC_READONLY_SCOPE_DENIED_OPERATION_NOT_SENT",formal_claim:false,source_result:false,driver_review:false,physical_x6_transfer:false}
  };
}
if(typeof require!=='undefined'&&require.main===module){process.stdout.write(JSON.stringify(verifyR313(128),null,2)+'\n');}
if(typeof module!=='undefined')module.exports={verifyR313};
