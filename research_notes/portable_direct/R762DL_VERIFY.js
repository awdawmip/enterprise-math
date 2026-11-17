"use strict";
function verifyR762DL(){
 const B=[[1,1,1],[1,1,0],[0,1,1],[0,0,1],[1,0,0],[0,0,0]];
 const steps=new Map();
 for(const a of B)for(const b of B){
  const t=a.map((v,i)=>v+b[i]-1).join(",");
  steps.set(t,(steps.get(t)||0n)+1n);
 }
 const gcd=(a,b)=>{while(b){let c=a%b;a=b;b=c}return a};
 const purePower=(q,p)=>{if(q<2)return false;while(q%p===0)q/=p;return q===1};
 const expected=(q,k)=>{
  if(q===1)return "trivial";
  const p=purePower(q,2)?2:purePower(q,3)?3:0;
  return p&&2*k>=q?`divisible-${p}`:"unit";
 };
 const mod=(a,q)=>(a%q+q)%q;
 const convolve=(dist,step,q)=>{
  const out=new Map();
  for(const [key,c] of dist){
   const a=key.split(",").map(Number);
   for(const [str,n] of step){
    const b=str.split(",").map(Number);
    const t=a.map((v,i)=>mod(v+b[i],q)).join(",");
    out.set(t,(out.get(t)||0n)+c*n);
   }
  }
  return out;
 };
 const cases=[2,3,4,5,6,7,8,9,10,12,16,18,25];
 let checks=0,states=0,comparisons=0;
 const digest=[];
 for(const Q of cases){
  let dist=new Map([["0,0,0",1n]]), g=0n;
  const limit=Q===25?7:Q>=16?9:Q===9?12:10;
  for(let k=1;k<=limit;k++){
   dist=convolve(dist,steps,Q);
   let total=0n;g=0n;
   for(const c of dist.values()){total+=c;g=gcd(g,c);states++}
   if(total!==36n**BigInt(k))throw Error(`mass Q=${Q} k=${k}`);
   const exp=expected(Q,k);
   if(exp==="unit"&&g!==1n)throw Error(`unit Q=${Q},k=${k},g=${g}`);
   if(exp.startsWith("divisible")&&g%BigInt(exp.slice(-1))!==0n)throw Error(`divisible Q=${Q},k=${k},g=${g}`);
   if(purePower(Q,2)||purePower(Q,3)){
    const p=purePower(Q,2)?2n:3n;
    if(g%p**BigInt(Math.floor(2*k/Q))!==0n)throw Error(`lower bound Q=${Q},k=${k}`);
    let gtmp=g;while(gtmp%p===0n&&gtmp>1n)gtmp/=p;
    if(gtmp!==1n)throw Error(`unexpected prime factor Q=${Q},k=${k},g=${g}`);
   }
   checks++;
  }
  digest.push({Q,lastK:limit,lastGCD:String(g),reachableOutcomes:dist.size});
 }
 for(const Q of [2,3,4,5,6,7,9]){
  let incdist=new Map([["0,0,0",1n]]);
  let poly=new Map([["0,0,0",1n]]);
  const bSteps=new Map(B.map(b=>[b.join(","),1n]));
  for(let k=1;k<=4;k++){
   incdist=convolve(incdist,steps,Q);
   poly=convolve(convolve(poly,bSteps,Q),bSteps,Q);
   for(const [key,val] of incdist){
    const v=key.split(",").map(Number);
    const target=v.map(a=>mod(a+k,Q)).join(",");
    if((poly.get(target)||0n)!==val)throw Error(`two-method Q=${Q},k=${k},state=${key}`);
    comparisons++;
   }
   if(poly.size!==incdist.size)throw Error(`support Q=${Q},k=${k}`);
  }
 }
 return {schema:"ENTERPRISE_MATH_R762DL_AUTHOR_EVIDENCE_V1",status:"PASS",date:"2026-11-18",
  computation_type:"Positive named BRC-branch integer group-algebra convolution; no classical pi/trigonometric/native physical simulation",
  branch_population:36,single_block_area_outcomes:steps.size,configuration_checks:checks,integer_state_count_checks:states,
  independent_polynomial_count_comparisons:comparisons,normalized_moduli:cases,case_digest:digest,
  theorem:"For Q>=2, gcd=1 unless Q is a power of 2 or 3 AND 2k>=Q. For Q=p^a (p=2 or 3), gcd is a positive p-power and p^floor(2k/Q) divides gcd. Q=1 has gcd 36^k.",
  independent_mathematical_review:"NOT_REVIEWED",native_triadic_event_license:"NOT_ESTABLISHED"};
}
if (typeof require !== 'undefined' && require.main === module) console.log(JSON.stringify(verifyR762DL(),null,2));
