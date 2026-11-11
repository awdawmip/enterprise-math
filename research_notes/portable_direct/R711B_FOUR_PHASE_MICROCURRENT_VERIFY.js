"use strict";
// R711b: exact phase-time residual census for every optimal four-phase full even cycle.
function must(ok,why){if(!ok)throw Error(why);}
function chooseEvenPhases(){
 const out=[];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){
  let s=Array(4).fill(1);s[i]=0;s[j]=0;out.push(s);}
 return out;
}
function verify(m,pattern,bits){
 const occurrences=Array(m).fill(0),j=Array(m).fill(0),norms=[],first=[];
 let stages=0;
 for(let p=0;p<4;p++){
  const occupied=new Set(),edges=[];
  for(let e=0;e<m;e++)if(e%2===pattern[p]){
   const i=e,k=(e+1)%m;
   must(!occupied.has(i)&&!occupied.has(k),"Cell conflict");
   occupied.add(i);occupied.add(k);edges.push(e);
   const firstPlus=((bits>>e)&1)===0;
   const sign=(occurrences[e]++===0?1:-1)*(firstPlus?1:-1);
   j[e]+=sign;
   must(Math.abs(j[e])<=1,"edge current amplitude");
  }
  must(edges.length===m/2&&occupied.size===m,"perfect matching");
  stages++;
  norms.push(j.reduce((a,b)=>a+Math.abs(b),0));
  if(p===0)first.push(...j);
 }
 must(occurrences.every(x=>x===2),"two typed events each edge");
 must(j.every(x=>x===0),"net current zero");
 must(norms[0]===m/2&&norms[2]===m/2&&norms[3]===0,"odd microphase readout");
 const grouped=pattern[0]===pattern[1];
 must(norms[1]===(grouped?0:m),"second phase peak");
 const peak=Math.max(...norms),exposure=norms.slice(0,3).reduce((a,b)=>a+b,0);
 must(peak===(grouped?m/2:m),"sharp peak");
 must(exposure===(grouped?m:2*m),"sharp total exposure");
 return {grouped,peak,exposure,first:first.join(",")};
}
function main(){
 const cases={};let checked=0;const patterns=chooseEvenPhases();
 for(let m=4;m<=12;m+=2){
  const seen=new Set();let grouped=0,mixed=0;
  for(const pattern of patterns)for(let b=0;b<(1<<m);b++){
   const r=verify(m,pattern,b);checked++;
   seen.add(r.first);
   if(r.grouped)grouped++;else mixed++;
  }
  must(grouped===2*(1<<m)&&mixed===4*(1<<m),"schedule census");
  must(seen.size===2*(1<<(m/2)),"first-phase micro-current fiber");
  cases[m]={distinct_full_micro_schedules:6*(1<<m),
    grouped_low_peak_schedules:grouped,interleaved_high_peak_schedules:mixed,
    smallest_peak:m/2,largest_peak:m,
    smallest_three_boundary_exposure:m,largest_three_boundary_exposure:2*m,
    first_boundary_distinct_current_vectors:seen.size,
    first_boundary_raw_repair_bits:m/2+1};
 }
 must(checked===32736,"exact census size");
 return {verdict:"R711B_FOUR_PHASE_MICROCURRENT_RESIDUAL_PASS",
   n_range_even:[4,12],complete_typed_schedules_checked:checked,
   claims:"Every 4-phase full-even-ring execution uses two copies of each alternating perfect matching; phase-time L1 profile (m/2,0,m/2,0) if first matching repeats, otherwise (m/2,m,m/2,0).",
   first_phase_repair:"Exactly m/2+1 bits from the completed macro-boundary ledger to recover first-phase edge-current vector",
   science_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",cases,
   scope:"frozen old-state, candidate at-most-one-incident-event-per-Cell microphases; j is derived signed physical edge incidence, V29 counts remain positive"};
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(main(),null,2));
