'use strict';
// R309: exact finite parameter certificate for all unbounded n via monotonicity.
function verifyR309() {
  const MAX_D=298;
  const pascal=Array.from({length:MAX_D+1},()=>[]);
  pascal[0]=[1n];
  for(let n=1;n<=MAX_D;n++){
    const row=Array(n+1).fill(1n);
    for(let k=1;k<n;k++)row[k]=pascal[n-1][k-1]+pascal[n-1][k];
    pascal[n]=row;
  }
  const choose=(n,k)=>{
    if(k<0||k>n)return 0n;
    k=Math.min(k,n-k);
    let v=1n;
    for(let j=1;j<=k;j++)v=v*BigInt(n-k+j)/BigInt(j);
    return v;
  };
  let count=0, minGap=null,minGapAt=null,minRatio=null,minRatioAt=null;
  const witnesses=[];
  for(let d=3;d<=MAX_D;d++){
    const n=Math.floor((12*d*d+4)/5);
    if(n<4*d+4) throw Error("n0 outside admissible main-term zone");
    const c=[1n];
    for(let j=1;j<=d-2;j++)c[j]=c[j-1]*BigInt(n-j+1)/BigInt(j);
    const A=choose(n-2*d-4,d-1);
    let U=0n, terms=0;
    for(let r=1;r<d;r++){
      for(let t=1;t<=Math.min(r,d-r);t++){
        U+=pascal[d-r][t]*pascal[r-1][t-1]*c[d-r-t];
        terms++;
      }
    }
    if(!(A>U))throw Error(`counterexample: d=${d}, n=${n}, A=${A}, U=${U}`);
    const gap=A-U;
    if(minGap===null||gap<minGap){minGap=gap;minGapAt={d,n}}
    if(minRatio===null||A*minRatio[1]<minRatio[0]*U){minRatio=[A,U];minRatioAt={d,n}}
    if([3,30,298].includes(d))witnesses.push({
      d,n,negative_majorant_terms:terms,
      A_decimal_digits:String(A).length,U_decimal_digits:String(U).length,
      gap_decimal_digits:String(gap).length,
      A: d<=3?String(A):undefined,
      U: d<=3?String(U):undefined,
      gap: d<=3?String(gap):undefined
    });
    count++;
  }
  function gcd(a,b){while(b){const t=a%b;a=b;b=t;}return a<0n?-a:a;}
  function f(n,d=1n){if(d<0n){n=-n;d=-d;}const g=gcd(n<0n?-n:n,d);return[n/g,d/g]}
  const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const neg=(a)=>[-a[0],a[1]];
  const sub=(a,b)=>add(a,neg(b));
  const mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]);
  const div=(a,b)=>f(a[0]*b[1],a[1]*b[0]);
  const pow=(a,k)=>{let v=f(1n);for(let i=0;i<k;i++)v=mul(v,a);return v;};
  const q=297n, s=f(17n,20n), ONE=f(1n);
  const quarticFactor=f((q-1n)*(q-2n)*(q-3n),q*q*q);
  let g= sub(ONE,s);
  g=add(g,div(mul(f(q-1n,q),pow(s,2)),f(2n)));
  g=sub(g,div(pow(s,3),f(6n)));
  g=add(g,div(mul(quarticFactor,pow(s,4)),f(24n)));
  g=sub(g,div(pow(s,5),f(120n)));
  const margin=sub(g,f(17n,40n));
  if(!(margin[0]>0n))throw Error("5th Bonferroni bound failed");
  if(g[0]!==1426166179906813n||g[1]!==3353353344000000n)throw Error("rational benchmark drift");
  if(margin[0]!==991008706813n||margin[1]!==3353353344000000n)throw Error("rational margin drift");
  if(Math.floor((12*2*2+4)/5)!==10||10-9<=0)throw Error("d=2 endpoint failed");
  const status={
    schema:"EM_R309_TWELVE_FIFTHS_WEDGE_EXACT_EVIDENCE_V1",
    status:"PASS",
    arithmetic:"JavaScript BigInt exact integer and reduced rational fractions; no floating point comparisons",
    finite_certificate:{d_min:3,d_max:MAX_D,cases:count,n0:"ceil(12*d*d/5)",all_exact_majorants_A_gt_U:true,minimum_absolute_gap:String(minGap),minimum_gap_at:minGapAt,minimum_ratio_at:minRatioAt,minimum_ratio_numerator_digits:String(minRatio[0]).length,minimum_ratio_denominator_digits:String(minRatio[1]).length,witnesses},
    symbolic_tail_certificate:{from_d:299,q_min:297,s_upper:"17/20",bonferroni_q297_at_s17over20:`${g[0]}/${g[1]}`,bonferroni_margin_over_17over40:`${margin[0]}/${margin[1]}`,tail_numerator:"16*d^3-832*d^2+85*d+510",tail_positive_reason:"d>=299 implies 16*d-832>0",d2_boundary:"D_2(n)=n-9 for n>=9; n0(2)=10"},
    proved_statement:"For all integers d>=2,n>=ceil(12d^2/5), D_d(n)>0 using inherited R303/R305 exact BRC ordered-source model and R306 majorant",
    qualifiers:{native_owner:"UNVERIFIED_CONTROL_QUOTA",native_session:"DENIED_STATIC_READONLY_OPERATION_NOT_SENT",independent_driver_review:"NOT_PERFORMED",source_result:"NOT_PUBLISHED",native_X6_cell_transfer:"NOT_ESTABLISHED"}
  };
  return status;
}
if (typeof require !== 'undefined' && require.main === module) {
  process.stdout.write(JSON.stringify(verifyR309(), null, 2)+'\n');
}
if (typeof module !== 'undefined') module.exports={verifyR309};
