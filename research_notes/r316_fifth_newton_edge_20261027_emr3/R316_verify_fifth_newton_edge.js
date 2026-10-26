'use strict';
// R316 author-side exact BigInt verification. Scientific input: R313 Eq(D,E,H)
// as reproduced/extended from R315's published source formulae.
function choose(n,k){
  if(k<0||k>n)return 0n;
  k=Math.min(k,n-k);let v=1n;
  for(let i=1;i<=k;i++)v=v*BigInt(n-k+i)/BigInt(i);
  return v;
}
function mul(a,b){
  const out=Array(a.length+b.length-1).fill(0n);
  for(let i=0;i<a.length;i++)if(a[i]!==0n){
    for(let j=0;j<b.length;j++)if(b[j]!==0n)out[i+j]+=a[i]*b[j];
  }
  return out;
}
function num(s){return [0n,-choose(3,s-1),-choose(6,s-1),choose(8,s-2)];}
function den(i){return [0n,-choose(4,i)+choose(2,i-1),choose(5,i-1)-choose(5,i-2),choose(7,i-2),-choose(9,i-3)];}
function fail(label,s,got,expected){throw Error(label+" s="+s+" got="+got+" expected="+expected);}
function eq(label,s,a,b){if(a!==b)fail(label,s,a,b);}
function verify(S=192){
  const pow=[[1n]];
  for(let i=1;i<=S;i++)pow.push(mul(pow.at(-1),[1n,-1n]));
  const M=[[1n]], moms=[];
  const checks={polynomial_degree:0,previous_moments:0,fourth_moment_closed_form:0,fourth_moment_recurrence:0,fifth_edge_direct:0,fifth_edge_moment_reconstruction:0,strict_lower_bound:0};
  const samples={};
  for(let s=0;s<=S;s++){
    if(s>0){
      let m=s<=10?mul(num(s),pow[s]):[0n];
      for(let i=1;i<=Math.min(s,12);i++){
        const term=mul(mul(den(i),M[s-i]),pow[i-1]);
        while(m.length<term.length)m.push(0n);
        for(let j=0;j<term.length;j++)m[j]-=term[j];
      }
      while(m.length>1&&m.at(-1)===0n)m.pop();
      if(m.length>2*s+2)fail('degree',s,m.length-1,2*s+1);
      M.push(m);
    }
    checks.polynomial_degree++;
    const m=M[s], ss=BigInt(s), pow2=1n<<ss;
    const moment=q=>m.reduce((acc,coef,j)=>{
      let fall=1n;
      for(let v=0;v<q;v++)fall*=BigInt(j-v);
      return acc+coef*fall;
    },0n);
    const A=moment(0),B=moment(1),C=moment(2),E=moment(3),F=moment(4);
    moms.push({A,B,C,E,F});
    eq('M(1)',s,A,pow2);checks.previous_moments++;
    if(s>=1){eq('M prime',s,4n*B,3n*(ss+1n)*pow2);checks.previous_moments++;}
    if(s>=2){eq('M double prime',s,16n*C,(9n*ss**2n+11n*ss-26n)*pow2);checks.previous_moments++;}
    if(s>=3){eq('M triple prime',s,64n*E,3n*(9n*ss**3n+6n*ss**2n-119n*ss+220n)*pow2);checks.previous_moments++;}
    if(s>=4){
      const fpoly=27n*ss**4n-18n*ss**3n-911n*ss**2n+4070n*ss-6184n;
      eq('M fourth prime formula',s,256n*F,3n*pow2*fpoly);checks.fourth_moment_closed_form++;
      const p=625n*ss**4n-1750n*ss**3n-205n*ss**2n-5294n*ss-2424n;
      let a=0n;
      for(let j=0;j<m.length;j++)a+=m[j]*choose(2*s+1-j,4);
      eq('Newton fifth-edge formula',s,6144n*a,pow2*p);checks.fifth_edge_direct++;
      const moments=4n*ss*(ss-1n)*(2n*ss-1n)*(2n*ss+1n)*A
        -16n*ss*(ss-1n)*(2n*ss-1n)*B
        +12n*(ss-1n)*(2n*ss-1n)*C-8n*(ss-1n)*E+F;
      eq('Newton moment reconstruction',s,24n*a,moments);checks.fifth_edge_moment_reconstruction++;
      const gap=16n*a-55n*pow2;
      if(gap<0n||(s>4&&gap===0n))fail('lower-bound gap',s,gap,'positive');
      checks.strict_lower_bound++;
      if([4,5,6,7,8,9,16,32,64,128,192].includes(s)){
        samples[s]={fourth_derivative:F.toString(),a_s_s_minus_4:a.toString(),gap_numerator:gap.toString()};
      }
    }
    if(s>=5){
      const x=moms;
      const prevF=2n*x[s-1].F+4n*x[s-1].E-12n*x[s-1].C
        +4n*x[s-2].E+84n*x[s-2].C+168n*x[s-2].B+24n*x[s-2].A
        -96n*x[s-3].C-576n*x[s-3].B-480n*x[s-3].A
        +264n*x[s-4].B+624n*x[s-4].A+144n*x[s-5].A;
      eq('fourth-derivative recurrence',s,F,prevF);checks.fourth_moment_recurrence++;
    }
  }
  return {schema:'EM_R316_ALL_S_FIFTH_NEWTON_EDGE_EXACT_V1',status:'PASS',max_s:S,
    checks,samples,scientific_scope:'R313 positive-weight ordered six-edge BRC auxiliary count model, Newton edge q=4',
    proof_scope:'Author proof for all integer s>=4 from R313 recurrence; machine cross-check only s=0..'+S,
    math_admission:'NOT_REVIEWED',arithmetic:'JavaScript BigInt exact integer polynomial recurrence; no floating point sign decisions'};
}
if(require.main===module){
  const S=process.argv[2]?Number(process.argv[2]):192;
  console.log(JSON.stringify(verify(S),null,2));
}
module.exports={verify};
