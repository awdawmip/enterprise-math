#!/usr/bin/env node
'use strict';
// Run: node research_checks/X6_TIME_UNIT247_PORT_PRECISION_C24_COSET_CHECK_20261122_0000.js research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json
const fs = require('fs');
function calculate(source){
 const g=Array.from({length:12},(_,k)=>k===5||k===10?3:0);
 const gcd=(a,b)=>{a=Math.abs(a);b=Math.abs(b);while(b){const q=a%b;a=b;b=q}return a};
 const mod=(x,n)=>(x%n+n)%n;
 const expect=(v,msg)=>{assertions++;if(!v)throw Error(msg)};
 const levels=[6,12,24,48,96,192],entry=[0,2,4,6,8,10],rows=[];
 let assertions=0,reachableStates=0;
 expect(source.cases.length===36,"36 source cases required");
 for(const item of source.cases){
  const i=item.ingress,j=item.egress,d=mod(j-i,12);
  const arc=Array.from({length:d},(_,r)=>g[(i+r)%12]).reduce((s,v)=>s+v,0);
  let pos=[0,2],ringNet=[0,0],spokes=[0,0],weight=[0,0],count=0;
  for(const ch of item.route){
   const t=ch>="A"&&ch<="M"?0:1, dst=ch.charCodeAt(0)-(t?97:65),cur=pos[t];
   expect(dst!==pos[1-t],"occupied target "+i+","+j);
   let step=0;
   if(cur===12){expect(dst===j,"bad exit");spokes[t]++}
   else if(dst===12){expect(cur===i,"bad entry");spokes[t]++}
   else if(dst===(cur+1)%12){ringNet[t]++;step=g[cur]}
   else if(dst===(cur+11)%12){ringNet[t]--;step=-g[dst]}
   else throw Error("invalid signed ring/Port event");
   weight[t]+=step;pos[t]=dst;count++;
  }
  expect(pos[0]===0&&pos[1]===2,"terminal Cells");
  expect(ringNet[0]===-12&&ringNet[1]===12,"signed net ring events");
  expect(spokes.every(v=>v%2===0),"paired center excursions");
  expect(count===item.cost,"source shortest witness length");
  const c=spokes.map(x=>x/2),ratio=6/gcd(6,arc);
  for(const N of levels){
   const theory=N/gcd(gcd(N,6),arc);
   const seen=new Set([i* N]),queue=[[i,0]];
   for(let t=0;t<queue.length;t++){
    const [cell,z]=queue[t];
    const options=[];
    if(cell===12)options.push([j,0]);
    else{
     options.push([(cell+1)%12,g[cell]],[(cell+11)%12,-g[(cell+11)%12]]);
     if(cell===i)options.push([12,0]);
    }
    for(const [to,w] of options){
     const z2=mod(z+w,N),key=to*N+z2;
     if(!seen.has(key)){seen.add(key);queue.push([to,z2])}
    }
   }
   reachableStates+=queue.length;
   const atStart=queue.filter(([x])=>x===i).map(([,z])=>z);
   expect(atStart.length===theory,"BFS subgroup count "+i+","+j+" mod"+N);
   for(let t=0;t<2;t++){
    const z=(ringNet[t]+d*c[t])/12;
    expect(Number.isInteger(z),"integer winding invariant");
    expect(mod(weight[t],N)===mod(6*z-arc*c[t],N),"weighted BRC cocycle");
   }
   if(d===6){
    expect(arc===3,"every diameter crosses one weight-3 edge");
    for(let t=0;t<2;t++)expect(mod(weight[t],N)===mod(6*(ringNet[t]/12),N),"terminal-observer collision");
    expect(theory===2*(N/6),"diameter doubles precision orbit");
    expect(mod(-arc,N)===mod(-3,N),"8-event same-Cell loop detects hidden coset");
   }
   expect(theory/(N/6)===ratio,"ratio independent of precision level");
  }
  rows.push({ingress:i,egress:j,cost:item.cost,clockwise_arc_weight:arc,precision_orbit_ratio:ratio,precision_orbit_C24:4*ratio,excursions_A:c[0],excursions_B:c[1],precision_delta_C24:weight.map(v=>mod(v,24))});
 }
 const table=entry.map(i=>entry.map(j=>rows.find(v=>v.ingress===i&&v.egress===j).precision_orbit_ratio));
 expect(table.flat().filter(v=>v===2).length===18,"18 doubled precision cosets");
 expect(table.flat().filter(v=>v===1).length===18,"18 unchanged precision cosets");
 return {schema:"X6_TIME_UNIT247_PORT_PRECISION_C24_COSSET_CERTIFICATE_V1",date:"2026-11-22",task_id:"RS-X6-NATIVE-TIME-DYNAMICS",source_case_commit:"f56840285cafeb9f5767ea91e903e1f53808186f",source_case_path:"research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json",conditional_model:"12 bidirectional signed OUTER ring events; one directed centre ingress and one directed centre egress; serial target-empty guarded whole triads; additive speculative precision cochain g5=g10=3, all other ring g=0, reversed edges negative, centre increments zero",precision_moduli:levels,ring_only_states_at_fixed_cell:levels.map(N=>N/6),diameter_states_at_fixed_cell:levels.map(N=>N/3),orbit_ratio_matrix:table,ratio_distribution:{unchanged:18,doubled:18},sharp_diameter_observer:{primitive_events:8,path:"x_i -> P -> x_(i+6) -> x_(i+5) -> ... -> x_i",precision_delta_C24:21,full_ring_forward_delta_C24:6},diameter_source_optima:rows.filter(x=>mod(x.egress-x.ingress,12)===6),rows,exact_integer_assertions:assertions,reachable_graph_states_explored:reachableStates,failures:0,admission:"AUTHOR_EXACT_CHECKED / CONDITIONAL_CANDIDATE / NO_NATIVE_PORT_ADMISSION / UNREVIEWED / NOT_ADMITTED"};
}
const input = JSON.parse(fs.readFileSync(process.argv[2] || 'research_checks/X6_TIME_UNIT245_DIRECTED_CENTER_PORT_PAIR_RESULTS_20261121_2200.json','utf8'));
console.log(JSON.stringify(calculate(input),null,2));
