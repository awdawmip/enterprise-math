#!/usr/bin/env node
"use strict";
/* PREFIX-838 standalone exact nonnegative integer / BigInt certificate.
 * Node.js standard library only. Recomputes all finite optima and named Q trajectories.
 * Run: node PREFIX838_R6_EVEN_PARITY_RESOURCE_CHECK.js > results.json
 */
function compute(){
  function profile(w){const [x,y,z]=w;return {s:x+y+z,e2:x*y+x*z+y*z,e3:x*y*z}}
  function evolve(w,last){let state=new Map([[14,1n]]);const frames=[];const pop=m=>(m&1)+((m>>1)&1)+((m>>2)&1);for(let t=0;t<=last;t++){const h=[0n,0n,0n,0n];for(const [id,mass] of state){const mask=id>>1,mark=id&1;h[pop(mask)+mark]+=mass;}frames.push(h);if(t===last)break;const next=new Map;const add=(id,n)=>next.set(id,(next.get(id)||0n)+n);for(const [id,mass]of state){const mask=id>>1,mark=id&1;for(let i=0;i<3;i++)if(mask&(1<<i))add(((mask^(1<<i))<<1)|mark,mass*BigInt(w[i]));if(mark)add(mask<<1,mass*2n);else if(pop(mask)<3)add((mask<<1)|1,mass);}state=next}return frames}
  const cases=[];let totalExamined=0,totalScalarChecks=0;
  for(let T=42;T<=80;T+=2){const seen=new Map();let got=null,examined=0;outer:for(let M=1;M<=110;M++)for(let x=1;x<=M;x++)for(let y=x;y<=M;y++){const w=[x,y,M],d=profile(w),key=`${d.s}:${4*d.e2+3*(T-2)*d.e3}`;examined++;const prev=seen.get(key);if(prev){got={T,M,A:prev,B:w};break outer}seen.set(key,w)}if(!got)throw Error(`missing finite witness T=${T}`);let {A,B,M}=got;let a=profile(A),b=profile(B);if(a.s!==b.s||4*(a.e2-b.e2)+3*(T-2)*(a.e3-b.e3)!==0||a.e2===b.e2)throw Error("collision-key verification fail "+T);const FA=evolve(A,T+2),FB=evolve(B,T+2),same=[];for(let i=0;i<FA.length;i++){let eq=true;for(let j=0;j<4;j++){totalScalarChecks++;if(FA[i][j]!==FB[i][j])eq=false}if(eq)same.push(i)}if(same.join(",")!==`0,1,${T}`)throw Error(`named Q regression failed T=${T}, equal=${same}`);const num=9*(T-2),den=T%4===0?2:4;let root=0;while(den*root*root<num)root++;if(M<root+1)throw Error("bound violated");cases.push({...got,delta_e2:a.e2-b.e2,delta_e3:a.e3-b.e3,lower_bound:root+1,examined_triples:examined,same_frames:same,collision_histogram:FA[T].map(v=>v.toString())});totalExamined+=examined}
  return {schema:"PREFIX838_R6_EVEN_PARITY_RESOURCE_RESULTS_V1",model:"p=q=3, positive named-source BRC Q=R+A a=1 b=2, integer unnormalized histograms",frozen_scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",status:"ALL_EXACT_ASSERTIONS_PASSED",T_range:"even 42..80 inclusive",cases,totals:{finite_exact_optima:cases.length,examined_triples:totalExamined,named_state_scalar_comparisons:totalScalarChecks}}
}
const r=compute();
if(r.status!=="ALL_EXACT_ASSERTIONS_PASSED")throw Error("unexpected regression status");
console.log(JSON.stringify(r,null,2));
