// PREFIX-828 — exact integer delayed BRC count observer verification
// Run: node PREFIX828_R6_DELAYED_OBSERVER_CHECK.js
function check828(){
 const f=n=>{let v=1n;for(let i=2;i<=n;i++)v*=BigInt(i);return v};
 const pop=n=>{let k=0;for(;n;n&=n-1)k++;return k};
 const moments=(v,n)=>{const e=Array(n+1).fill(0n);e[0]=1n;let z=0;for(const x of v){z++;for(let j=Math.min(z,n);j>=1;j--)e[j]+=BigInt(x)*e[j-1]}return e};
 const trace=(weights,n)=>{
  const p=weights.length,full=(1<<p)-1,a=2n,b=3n;
  let states=new Map([[full*2,1n]]),out=[];
  for(let t=0;t<=n;t++){
   const h=Array(p+1).fill(0n);
   for(const [key,x] of states)h[pop(Math.floor(key/2))+key%2]+=x;
   out.push(h);if(t===n)break;
   const next=new Map(),add=(k,x)=>next.set(k,(next.get(k)||0n)+x);
   for(const [key,x] of states){
    const mask=Math.floor(key/2),mark=key%2;
    for(let j=0;j<p;j++)if(mask&(1<<j))add((mask&~(1<<j))*2+mark,x*BigInt(weights[j]));
    if(mark)add(mask*2,x*b);
    else if(pop(mask)<p)add(mask*2+1,x*a);
   }
   states=next;
  }
  return out;
 };
 let profileChecks=0, powerChecks=0, directComparisons=0, firstGapChecks=0;
 const cases=[];
 for(let n=1;n<=10;n++){
  const A=[],B=[];
  for(let j=0;j<2**n;j++)(pop(j)%2?B:A).push(j+1);
  const p=A.length,eA=moments(A,n),eB=moments(B,n);
  for(let k=0;k<n;k++){
   if(eA[k]!==eB[k])throw Error(`e${k} mismatch at n${n}`);
   const delta=A.reduce((s,x)=>s+BigInt(x)**BigInt(k),0n)-B.reduce((s,x)=>s+BigInt(x)**BigInt(k),0n);
   if(delta!==0n)throw Error(`powers${k} mismatch at n${n}`);
   profileChecks++;powerChecks++;
  }
  const sign=n%2?-1n:1n;
  const targetPower=sign*f(n)*2n**BigInt(n*(n-1)/2);
  const powerN=A.reduce((s,x)=>s+BigInt(x)**BigInt(n),0n)-B.reduce((s,x)=>s+BigInt(x)**BigInt(n),0n);
  if(powerN!==targetPower)throw Error(`power n mismatch at n${n}`);powerChecks++;
  const deltaE=-f(n-1)*2n**BigInt(n*(n-1)/2);
  if(eA[n]-eB[n]!==deltaE)throw Error(`elementary n mismatch at n${n}`);profileChecks++;
  const gap=f(n)*deltaE;
  if(n<=5){
   const x=trace(A,n),y=trace(B,n);
   for(let t=0;t<n;t++){
    if(x[t].some((v,i)=>v!==y[t][i]))throw Error(`early distinguish n${n},t${t}`);
    directComparisons++;
   }
   const diff=x[n].map((v,i)=>v-y[n][i]);
   if(diff[p-n]!==gap||diff.some((v,i)=>i!==p-n&&v!==0n))throw Error(`wrong first gap n${n}`);
   directComparisons++;firstGapChecks++;
  }
  cases.push({n,source_count_per_state:p,capacity:p,first_different_step:n,elementary_gap:deltaE.toString(),first_trace_gap:gap.toString(),gap_bin:p-n,branch_enumerated:n<=5});
 }
 return {schema:"PREFIX828_R6_DELAYED_NAMED_OBSERVER_V1",status:"ALL_EXACT_ASSERTIONS_PASSED",scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",profile_checks:profileChecks,power_checks:powerChecks,direct_histogram_comparisons:directComparisons,first_gap_checks:firstGapChecks,range:"n=1..10 profile and power sums; n=1..5 direct named Q-branch enumeration; all exact BigInt",scope:"unnormalized positive-count BRC Q-only observer; operator time, not native X6 or physical time",cases};
}
console.log(JSON.stringify(check828(),null,2));
