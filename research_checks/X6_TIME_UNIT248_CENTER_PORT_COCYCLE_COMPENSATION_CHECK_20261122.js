#!/usr/bin/env node
// Exact reproducible conditional X6 Unit248 checks. No remote dependencies.
const certificate=(function(){

"use strict";
const g = Array.from({length:12},(_,k)=>(k===5||k===10)?3:0);
const B = [0]; for(let k=0;k<12;k++) B.push(B[k]+g[k]);
const ingress = [0,2,4,6,8,10], mod=(a,n)=>(a%n+n)%n;
const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b)[a,b]=[b,a%b];return a;};
let assertions=0, states=0;
const check=(value,msg)=>{assertions++;if(!value)throw Error(msg)};
function reach(N, i, j, compensated=false, allSpokes=false) {
 const q=[[0,0]], seen=new Set(["0:0"]); let index=0;
 while(index<q.length) {
  const [x,z]=q[index++], options=[];
  if(x===12) {
   for(const dest of (allSpokes?ingress:[j]))options.push([dest,compensated?B[dest]:0]);
  } else {
   options.push([(x+1)%12,g[x]],[(x+11)%12,-g[(x+11)%12]]);
   if(allSpokes ? ingress.includes(x) : x===i) options.push([12,compensated?-B[x]:0]);
  }
  for(const [y,delta] of options) {
   const n=mod(z+delta,N), key=y+":"+n;
   if(!seen.has(key)){seen.add(key);q.push([y,n]);}
  }
 }
 states+=q.length;
 return q.filter(v=>v[0]===0).length;
}
const layers=[6,12,24,48,96,192], rows=[], fullStar=[];
for(const N of layers){
 let unchanged=0,doubled=0;
 for(const i of ingress)for(const j of ingress){
  const d=mod(j-i,12);
  const A=Array.from({length:d},(_,r)=>g[(i+r)%12]).reduce((s,x)=>s+x,0);
  const anomaly=mod(-A,6);
  const expectedZero=N/gcd(N,gcd(6,A));
  const fixedZero=reach(N,i,j,false,false);
  const fixedRepair=reach(N,i,j,true,false);
  check(fixedZero===expectedZero,"zero-centre pair orbit "+N+":"+i+":"+j);
  check(fixedRepair===N/6,"compensated pair orbit "+N+":"+i+":"+j);
  check(mod((-B[i]+B[j])-A,6)===0,"pair potential congruence");
  if(anomaly===0)unchanged++; else {check(anomaly===3,"anomaly not ±3");doubled++;}
  if(N===24)rows.push({ingress:i,egress:j,A,uncompensated_fixed_cell_states:fixedZero,compensated_fixed_cell_states:fixedRepair,centre_ingress_weight:-B[i],centre_egress_weight:B[j]});
 }
 check(unchanged===18&&doubled===18,"18/18 split");
 const zeroStar=reach(N,0,0,false,true), repairedStar=reach(N,0,0,true,true);
 check(zeroStar===N/3&&repairedStar===N/6,"full-star orbit");
 fullStar.push({modulus:N,zero_spokes_fixed_cell_states:zeroStar,compensated_spokes_fixed_cell_states:repairedStar});
}
check(B[5]===0&&B[6]===3&&B[10]===3&&B[12]===6,"potentials");
check(mod(-3,24)===21&&mod(3-3,24)===0,"diameter 8 event discriminator");
return {schema:"X6_TIME_UNIT248_DIRECTED_CENTER_PORT_COCYCLE_COMPENSATION_CERTIFICATE_V1",date:"2026-11-22",task_id:"RS-X6-NATIVE-TIME-DYNAMICS",science_source_commit:"a72226e2430ffa4786321ac86e7f0c599d5f0389",prior_unit:"Unit247",precision_moduli:layers,ring_weights:g,potential:B,ports:ingress,model:"Conditional signed bidirectional native ring and whole-triad directed centre; independent additive C_N precision observer; no physical law/admission inferred",exact_result:"For arbitrary one-pair centre edge weights alpha_i,beta_j, fixed-Cell precision image is <6,alpha_i+beta_j-A(i,j)>; for all six ingress and six egress simultaneous preservation iff alpha_i=t-B(i),beta_j=B(j)-t mod6 for one t in Z6.",example:"x0->P->x6->x5->...->x0, 8 primitive events: zero centre weights yields C24 delta 21, compensated beta6=3 yields 0.",zero_vs_repair_single_pair_C24:rows,full_star:fullStar,exact_integer_assertions:assertions,BFS_states_total:states,failures:0,execution:"V8 JavaScript exact integer BFS and congruence assertions in initiating research run",status:"AUTHOR_EXACT_EXECUTED / CONDITIONAL_PORT_WEIGHT_MODEL / UNREVIEWED / NOT_ADMITTED"};

})();
console.log(JSON.stringify(certificate,null,2));
