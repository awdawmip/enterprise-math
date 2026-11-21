#!/usr/bin/env node
// Independent reproducible Unit249 replay of exact Unit245/Unit247 evidence.
const fs=require("fs");
const source=JSON.parse(fs.readFileSync(process.argv[2]||"research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json","utf8"));
const prior=JSON.parse(fs.readFileSync(process.argv[3]||"research_checks/X6_TIME_UNIT247_PORT_PRECISION_C24_COSET_RESULTS_20261122_0000.json","utf8"));
const cert=(function(source,prior){
"use strict";
const g=Array.from({length:12},(_,k)=>k===5||k===10?3:0),B=[0]; for(let k=0;k<12;k++)B.push(B[k]+g[k]);
const mod=(a,n)=>(a%n+n)%n,gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a};
let assertions=0;const ck=(v,msg)=>{assertions++;if(!v)throw Error(msg)};
const out=[];ck(source.cases.length===36,"original 36 cases");
for(const item of source.cases){
 const i=item.ingress,j=item.egress,d=mod(j-i,12),A=Array.from({length:d},(_,r)=>g[(i+r)%12]).reduce((p,x)=>p+x,0);
 let pos=[0,2],ring=[0,0],zero=[0,0],repair=[0,0],cross=[0,0],length=0;
 for(const ch of item.route){
  const t=ch>="A"&&ch<="M"?0:1, dst=ch.charCodeAt(0)-(t?97:65),cur=pos[t];
  ck(dst!==pos[1-t],"target occupied");
  let incrementZero=0,incrementRepair=0;
  if(cur===12){ck(dst===j,"center exit");incrementRepair=B[dst];}
  else if(dst===12){ck(cur===i,"center ingress");incrementRepair=-B[cur];cross[t]++;}
  else if(dst===(cur+1)%12){ring[t]++;incrementZero=g[cur];incrementRepair=incrementZero;}
  else if(dst===(cur+11)%12){ring[t]--;incrementZero=-g[dst];incrementRepair=incrementZero;}
  else throw Error("invalid native primitive transition");
  zero[t]+=incrementZero;repair[t]+=incrementRepair;pos[t]=dst;length++;
 }
 ck(pos[0]===0&&pos[1]===2,"labelled return");
 ck(ring[0]===-12&&ring[1]===12,"signed ring winding");
 ck(length===item.cost,"original shortest BRC cost preserved");
 ck(cross[0]+cross[1]===12/gcd(12,d),"minimal center passages as Unit246");
 ck(cross.filter(x=>x>0).length===1,"all passages carried by one triad");
 const old=prior.rows.find(x=>x.ingress===i&&x.egress===j);
 ck(Boolean(old),"prior original Unit247 row");
 ck(old.precision_delta_C24.every((x,t)=>x===mod(zero[t],24)),"original fixed-center precision prediction");
 const dz=repair.map((x,t)=>mod(x-zero[t],24));
 for(let t=0;t<2;t++){
  ck(mod(repair[t]-zero[t],24)===mod((B[j]-B[i])*cross[t],24),"source-case centre-weight delta");
  const z=(ring[t]+d*cross[t])/12;ck(Number.isInteger(z),"closed BRC source integer winding");
  ck(mod(zero[t],24)===mod(6*z-A*cross[t],24),"Unit247 source cocycle");
  ck(mod(repair[t],24)===mod(6*z+(-B[i]+B[j]-A)*cross[t],24),"Unit248 compensated source cocycle");
 }
 const differs12=zero.some((x,t)=>mod(x,12)!==mod(repair[t],12));
 const differs24=zero.some((x,t)=>mod(x,24)!==mod(repair[t],24));
 const between=(B[i]!==B[j]);
 ck(differs12===between&&differs24===between,"sharp across-class observer separation");
 out.push({ingress:i,egress:j,shortest_events:item.cost,excursions_by_triad:cross,zero_centre_delta_C24:zero.map(x=>mod(x,24)),compensated_delta_C24:repair.map(x=>mod(x,24)),different_C12:differs12,different_C24:differs24});
}
ck(out.filter(x=>x.different_C12).length===18,"18 distinguish at C12");
ck(out.filter(x=>x.different_C24).length===18,"18 distinguish at C24");
ck(out.filter(x=>x.shortest_events===28).length===2,"two 28-native-event optima");
const opt=out.filter(x=>x.shortest_events===28);
ck(JSON.stringify(opt.map(x=>[x.ingress,x.egress,x.compensated_delta_C24]))===JSON.stringify([[6,0,[12,6]],[8,2,[18,0]]]),"two shortest test predictions");
return {schema:"X6_UNIT249_ORIGINAL_BRC_36CASE_PRECISION_LAW_DISCRIMINATOR_V1",date:"2026-11-22",task_id:"RS-X6-NATIVE-TIME-DYNAMICS",frozen_p000:"a72226e2430ffa4786321ac86e7f0c599d5f0389",unit245_source_commit:"f56840285cafeb9f5767ea91e903e1f53808186f",unit247_source_commit:"0628624fc23d1f34521119b809398c0146ed9bbb",existing_case_count:36,observation:"Same exact chronological two-labelled-triad minimal event certificates; compare zero-centre with Unit248 compensating centre precision weights; ring and occupancy unchanged.",source_case_rows:out,distinguishable_pairs_C12:18,distinguishable_pairs_C24:18,indistinguishable_pairs_C12_C24:18,optimal_28_event_predicted_C24:opt,exact_integer_assertions:assertions,failed_assertions:0,execution:"Actual V8 exact integer checker against two immutable source certificates",status:"AUTHOR_EXACT_EXECUTED / CONDITIONAL_CANDIDATE_COMPARISON / UNREVIEWED / NOT_ADMITTED"};

})(source,prior);
console.log(JSON.stringify(cert,null,2));
