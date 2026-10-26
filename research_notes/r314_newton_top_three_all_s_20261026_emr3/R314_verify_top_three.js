'use strict';
// R314 exact crosscheck of all-s symbolic top-three formulas using R313 polynomial recurrence.
function verifyR314(S){
  const binom=(n,k)=>{if(n<0||k<0||k>n)return 0n;k=Math.min(k,n-k);let r=1n;for(let i=1;i<=k;i++)r=r*BigInt(n-k+i)/BigInt(i);return r};
  const mul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)if(a[i])for(let j=0;j<b.length;j++)if(b[j])c[i+j]+=a[i]*b[j];return c};
  const ncoef=i=>i===0?[1n]:[0n,-binom(3,i-1),-binom(6,i-1),binom(8,i-2)];
  const dcoef=i=>[0n,-binom(4,i)+binom(2,i-1),binom(5,i-1)-binom(5,i-2),binom(7,i-2),-binom(9,i-3)];
  const powers=[[1n]];for(let i=1;i<=S;i++)powers.push(mul(powers.at(-1),[1n,-1n]));
  const M=[[1n]];
  let edgeChecks=0,momentChecks=0,strict=0,equal=0;let samples={};
  for(let s=0;s<=S;s++){
    if(s){
      const m=mul(ncoef(s),powers[s]);
      for(let i=1;i<=Math.min(s,12);i++){
        const term=mul(mul(dcoef(i),M[s-i]),powers[i-1]);
        while(m.length<term.length)m.push(0n);
        for(let j=0;j<term.length;j++)m[j]-=term[j];
      }
      while(m.length>1&&m.at(-1)===0n)m.pop();
      if(m.length-1>2*s+1)throw Error("degree bound s="+s);
      M.push(m);
    }
    const m=M[s], pow2=1n<<BigInt(s);
    const v0=m.reduce((a,c)=>a+c,0n);
    if(v0!==pow2)throw Error("zeroth moment s="+s);
    momentChecks++;
    if(s>=1){
      const v1=m.reduce((a,c,j)=>a+BigInt(j)*c,0n);
      if(4n*v1!==3n*BigInt(s+1)*pow2)throw Error("first moment s="+s);
      momentChecks++;
    }
    if(s>=2){
      const v2=m.reduce((a,c,j)=>a+BigInt(j)*BigInt(j-1)*c,0n);
      if(16n*v2!==BigInt(9*s*s+11*s-26)*pow2)throw Error("second moment s="+s);
      momentChecks++;
    }
    const these={};
    for(let q=0;q<=Math.min(s,2);q++){
      let a=0n;for(let j=0;j<m.length;j++)a+=m[j]*binom(2*s+1-j,q);
      let expected=q===0?pow2:q===1?(pow2*BigInt(5*s+1)/4n):(pow2*BigInt(25*s*s-5*s-26)/32n);
      if(a!==expected)throw Error(`coefficient mismatch at (s,k)=(${s},${s-q}): ${a} vs ${expected}`);
      if(a<pow2)throw Error("positivity fails at "+s+" "+q);
      if(a===pow2)equal++;else strict++;
      if([0,1,2,3,8,32,64,128].includes(s))these["k="+(s-q)]=a.toString();
      edgeChecks++;
    }
    if([0,1,2,3,8,32,64,128].includes(s))samples[s]=these;
  }
  return {schema:"EM_R314_ALL_S_TOP_THREE_NEWTON_EDGES_EXACT_V1",status:"PASS",max_s:S,checked_edges:edgeChecks,checked_moments:momentChecks,equalities_at_lower_bound:equal,strictly_above:strict,arithmetic:"Pure JavaScript BigInt exact integer-polynomial recurrence E of R313; no floating-point sign testing",formulas:["a_{s,s}=2^s (s>=0)","a_{s,s-1}=2^(s-2)(5s+1) (s>=1)","a_{s,s-2}=2^(s-5)(25s^2-5s-26) (s>=2)"],scope:"All s>=0 proved algebraically; integer verification finite 0..S, independent Driver validation pending",samples};
}
if(typeof require!=='undefined'&&require.main===module)console.log(JSON.stringify(verifyR314(128),null,2));
if(typeof module!=='undefined')module.exports={verifyR314};
