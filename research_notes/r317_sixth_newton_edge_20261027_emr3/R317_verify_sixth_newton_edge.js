'use strict';

// R317 exact test. Execute using: node R317_verify_sixth_newton_edge.js
function verifyR317(){
  const N=192;
  function C(n,k){if(n<0||k<0||k>n)return 0n;let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-i+1)/BigInt(i);return a;}
  function add(a,b,sgn=1n){const x=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<a.length;i++)x[i]+=a[i];for(let i=0;i<b.length;i++)x[i]+=sgn*b[i];while(x.length>1&&x[x.length-1]===0n)x.pop();return x;}
  function mul(a,b){const x=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)if(a[i]!==0n)for(let j=0;j<b.length;j++)if(b[j]!==0n)x[i+j]+=a[i]*b[j];while(x.length>1&&x[x.length-1]===0n)x.pop();return x;}
  const oneMinusPower=(r)=>Array.from({length:r+1},(_,j)=>(j%2?-1n:1n)*C(r,j));
  const numerator=(i)=>[0n,-C(3,i-1),-C(6,i-1),C(8,i-2)];
  const delta=(i)=>[0n,-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)];
  const M=[[1n]],counts={degree:0,moments0to4:0,moment5:0,moment5_difference:0,newton_q5:0,recovery:0,positive_bound:0};const samples={};
  const p5=S=>81n*S**5n-225n*S**4n-5295n*S**3n+43385n*S**2n-134746n*S+162800n;
  const q5=S=>625n*S**5n-3125n*S**4n+4425n*S**3n-14275n*S**2n-9250n*S+18192n;
  const dif=S=>81n*S**4n-342n*S**3n-2745n*S**2n+20270n*S-36624n;
  function moment(p,r){let sum=0n;for(let j=r;j<p.length;j++){let ff=1n;for(let v=0;v<r;v++)ff*=BigInt(j-v);sum+=p[j]*ff;}return sum;}
  let previousFifth=null;
  for(let n=0;n<=N;n++){
    if(n>0){
      let x=mul(numerator(n),oneMinusPower(n));
      for(let i=1;i<=Math.min(n,12);i++)x=add(x,mul(mul(delta(i),M[n-i]),oneMinusPower(i-1)),-1n);
      M.push(x);
    }
    const poly=M[n];if(poly.length-1>2*n+1)throw Error(`degree ${n}`);counts.degree++;
    const S=BigInt(n),pow=2n**S;
    const m=Array.from({length:6},(_,i)=>moment(poly,i));
    const eq=(label,l,r)=>{if(l!==r)throw Error(`${label} at ${n}: ${l} != ${r}`);};
    eq("m0",m[0],pow);counts.moments0to4++;
    if(n>=1){eq("m1",4n*m[1],3n*(S+1n)*pow);counts.moments0to4++;}
    if(n>=2){eq("m2",16n*m[2],(9n*S*S+11n*S-26n)*pow);counts.moments0to4++;}
    if(n>=3){eq("m3",64n*m[3],3n*(9n*S**3n+6n*S*S-119n*S+220n)*pow);counts.moments0to4++;}
    if(n>=4){eq("m4",256n*m[4],3n*(27n*S**4n-18n*S**3n-911n*S*S+4070n*S-6184n)*pow);counts.moments0to4++;}
    if(n>=5){
      eq("m5",1024n*m[5],3n*pow*p5(S));counts.moment5++;
      if(n>=6){eq("m5 recurrence",1024n*(m[5]-2n*previousFifth),15n*pow*dif(S));counts.moment5_difference++;}
      let a=0n;for(let j=0;j<poly.length;j++)a+=poly[j]*C(2*n+1-j,5);
      eq("q5",24576n*a,pow*q5(S));counts.newton_q5++;
      let recovered=4n*S*(S-1n)*(2n*S-3n)*(2n*S-1n)*(2n*S+1n)*m[0]
        -20n*S*(S-1n)*(2n*S-3n)*(2n*S-1n)*m[1]
        +20n*(S-1n)*(2n*S-3n)*(2n*S-1n)*m[2]
        -20n*(S-1n)*(2n*S-3n)*m[3]
        +5n*(2n*S-3n)*m[4]-m[5];
      eq("recovery",120n*a,recovered);counts.recovery++;
      if(!(32n*a>=219n*pow))throw Error(`positivity ${n}`);counts.positive_bound++;
      if([5,6,7,8,128,192].includes(n))samples[n]={fifth_moment:String(m[5]),newton_q5:String(a)};
    }
    previousFifth=m[5];
  }
  return {schema:"ENTERPRISE_MATH_R317_EXACT_EVIDENCE_V1",status:"PASS",tested_s_range:[0,N],arithmetic:"JavaScript BigInt exact integer; no floating arithmetic in proof checks",counts,samples,source_recurrence:"R313 (D/E) as quoted in immutable R316 author proof",theorem_claim:"For s>=5 a_{s,s-5}=2^s*(625s^5-3125s^4+4425s^3-14275s^2-9250s+18192)/24576 >= (219/32)*2^s>0",limitations:"Finite test s<=192; infinite statement uses algebraic induction, not numerical extrapolation; no native Driver verification."};
}

const evidence=verifyR317();
if(typeof process!== 'undefined' && process.stdout)process.stdout.write(JSON.stringify(evidence,null,2)+'\n');
