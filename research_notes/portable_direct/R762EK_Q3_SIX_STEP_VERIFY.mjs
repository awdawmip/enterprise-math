#!/usr/bin/env node
// R762EK: self-contained exact BigInt verifier, Node.js >=18; no dependencies.
function verify(){
  const q=3, N=78, dirs=[[0,0,0],[1,0,0],[0,0,1],[1,1,0],[0,1,1],[1,1,1]];
  function conv(a){
    const b=Array(27).fill(0n);
    for(let z=0;z<3;z++)for(let y=0;y<3;y++)for(let x=0;x<3;x++){
      const v=a[x+3*y+9*z];if(v===0n)continue;
      for(const [dx,dy,dz] of dirs)b[((x+dx)%3)+3*((y+dy)%3)+9*((z+dz)%3)]+=v;
    }
    return b;
  }
  function gcd(a,b){while(b!==0n){const t=a%b;a=b;b=t;}return a<0n?-a:a;}
  function valuation(a){
    let c=0n;for(const t of a)c=gcd(c,t);
    let v=0;while(c!==0n&&c%3n===0n){c/=3n;v++;}
    return {v,content:c.toString()};
  }
  const powers=[Array(27).fill(0n)];powers[0][0]=1n;
  for(let n=1;n<=N;n++)powers.push(conv(powers[n-1]));
  const omega=[[1,0],[0,1],[-1,-1]];
  const counts={};
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)for(let k=0;k<3;k++){
    const exp=[0,i,k,i+j,j+k,i+j+k];let a=0,b=0;
    for(const e of exp){a+=omega[e%3][0];b+=omega[e%3][1];}
    const name=`${a},${b}`;counts[name]=(counts[name]||0)+1;
  }
  const expected={"0,0":12,"6,0":1,"3,0":4,"0,3":1,"-3,-3":1,"0,-3":4,"3,3":4};
  if(JSON.stringify(Object.entries(counts).sort())!==JSON.stringify(Object.entries(expected).sort()))throw Error("character-spectrum-mismatch");
  let formulaChecks=0,recurrenceChecks=0,massChecks=0,contentChecks=0;
  const base=[null,0,0,1,2,3,4];
  const first=[];
  for(let n=0;n<=N;n++){
    const p=powers[n];
    const sum=p.reduce((a,b)=>a+b,0n);
    if(sum!==6n**BigInt(n))throw Error(`mass-${n}`);
    massChecks++;
    const r=n===0?0:1+(n-1)%6,k=n===0?0:(n-r)/6;
    const contentVal=valuation(p).v;
    const expectedVal=n===0?0:6*k+base[r];
    if(contentVal!==expectedVal)throw Error(`valuation-${n}:${contentVal}!=${expectedVal}`);
    contentChecks++;
    if(n<=6)first.push({n,v3:contentVal});
    if(n>0){
      const b=(6n**BigInt(r))*(64n**BigInt(k)-1n)/27n;
      if((6n**BigInt(r))*(64n**BigInt(k)-1n)!==27n*b)throw Error(`nonintegral-${n}`);
      const factor=3n**BigInt(6*k);
      for(let t=0;t<27;t++){
        if(p[t]!==factor*(powers[r][t]+b))throw Error(`formula-${n}-${t}`);
        formulaChecks++;
      }
    }
    if(n>=1 && n+6<=N){
      const val=7n*3n**5n*6n**BigInt(n);
      for(let t=0;t<27;t++){
        if(powers[n+6][t]-729n*p[t]!==val)throw Error(`recurrence-${n}-${t}`);
        recurrenceChecks++;
      }
    }
  }
  return {
    schema:"R762EK_EXACT_EVIDENCE_V1",
    model:"G=(Z/3)^3; P=1+X+Z+XY+YZ+XYZ; six distinguishable positive unit branches",
    method:"exact Eisenstein-character enumeration and bigint cyclic coefficient convolution",
    basis:"27 endpoint coefficients; integer arithmetic only",
    exponent_range:"0..78 inclusive",
    character_cases:Object.values(counts).reduce((a,b)=>a+b,0),
    character_spectrum:counts,
    initial_valuations:first,
    coefficient_closed_formula_checks:formulaChecks,
    six_step_recurrence_coefficient_checks:recurrenceChecks,
    mass_conservation_checks:massChecks,
    content_valuation_checks:contentChecks,
    final_n78_content_valuation:valuation(powers[78]).v,
    independent_review:"NOT_REVIEWED",
    all_pass:true
  };
}
const result=verify();
process.stdout.write(JSON.stringify(result,null,2)+"\n");
