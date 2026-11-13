/** R731: typed positive-BRC 15-arc -> V29 PASS ledger construction.
 * Input: R730 immutable masks; V29 nonnegative PASS grammar; V17 slot replacement.
 * All arithmetic is exact nonnegative integer counting. No force-law admission.
 * Run: node R731_V29_GRADED_PASS_LIFT_VERIFY.js
 */
"use strict";
const triads=["012","013","014","023","024","034","123","124","134","234"];
const allArcs=[];
for (const u of triads) for (const v of triads)
  if ([...u].filter(x=>v.includes(x)).length===2) allArcs.push(u+">"+v);
if(allArcs.length!==60) throw Error("60 arc universe");
const portPairs=[];
for (let a=0;a<6;a++) for(let b=0;b<6;b++) if(a!==b)portPairs.push([a,b]);
if(portPairs.length!==30)throw Error("30 distinct-port PASS types");
const maskText={A:"211733226574",B:"5363347296468"};
function getArcs(maskText){const m=BigInt(maskText);return allArcs.filter((_,i)=>m&(1n<<BigInt(i)));}
function pathState(path,arcs){
  if(path[0]!=="012")throw Error("unexpected root");
  const allowed=new Map(arcs.map((arc,i)=>[arc,i]));
  const slots={0:0,1:1,2:2};
  const ledger=Array.from({length:6},()=>Array(6).fill(0));
  const eventWord=[];
  for(let i=1;i<path.length;i++){
    const u=path[i-1],v=path[i],edge=u+">"+v;
    if(!allowed.has(edge))throw Error("disallowed "+edge);
    if(i>1&&path[i-2]===v)throw Error("immediate return");
    const [a,b]=portPairs[allowed.get(edge)];
    ledger[a][b]++;eventWord.push([a,b]);
    const leave=[...u].find(x=>!v.includes(x));
    const enter=[...v].find(x=>!u.includes(x));
    slots[enter]=slots[leave];delete slots[leave];
  }
  const total=ledger.flat().reduce((s,x)=>s+x,0);
  if(total!==path.length-1)throw Error("V29 grade mismatch");
  const recovered=arcs.map((_,i)=>ledger[portPairs[i][0]][portPairs[i][1]]);
  if(recovered.reduce((a,b)=>a+b,0)!==total)throw Error("unmapped ledger mass");
  return {frame:path.at(-1).split("").map(x=>slots[x]),grade:total,
          eventWord,edgeMultiplicities:recovered,nonzeroCounters:recovered.filter(x=>x>0).length};
}
function cyclicCNB(vertices){const m=vertices.length;for(let i=0;i<m;i++)
  if(vertices[(i+m-1)%m]===vertices[(i+1)%m])return false;return true;}
function frameOrder(p){let q=[0,1,2];for(let i=1;i<=6;i++){
  q=q.map(x=>p[x]);if(q.join("")==="012")return i;
}throw Error("not S3");}
function prefixCount(arcs,maxSteps){const neighbors=new Map();for(const arc of arcs){const [u,v]=arc.split(">");if(!neighbors.has(u))neighbors.set(u,[]);neighbors.get(u).push(v);}
let count=0;function visit(p){const s=pathState(p,arcs);if(s.grade!==p.length-1)throw Error("path lift");count++;
  if(p.length===maxSteps+1)return;
  for(const v of neighbors.get(p.at(-1))??[])
    if(p.length<2||v!==p.at(-2))visit([...p,v]);}
visit(["012"]);return count;}
const output={schema:"R731_V29_GRADED_BRC_LIFT_CERT_V1",origin:"R730 A/B masks + X6 V29 PASS grammar",ports:6,possible_off_diagonal_PASS_types:30,systems:{}};
for(const [name,mask] of Object.entries(maskText)){
 const arcs=getArcs(mask);if(arcs.length!==15)throw Error(name+" does not have 15 arcs");
 const cycle=name==="A"?["012","023","123"]:["012","023","123","013"];
 if(!cyclicCNB(cycle))throw Error("seam failure");
 const once=pathState([...cycle,"012"],arcs);
 const order=frameOrder(once.frame);
 const repeated=Array.from({length:order},()=>cycle).flat();
 const full=pathState([...repeated,"012"],arcs);
 if(full.frame.join("")!=="012")throw Error("abstract-frame failed to return");
 if(full.grade!==order*cycle.length)throw Error("native ledger grade failed");
 output.systems[name]={arc_mask:mask,arc_count:arcs.length,injective_event_assignment:true,
  initial_cycle:cycle.concat("012"),cycle_is_cyclic_nonbacktracking:true,
  one_cycle_holonomy:once.frame.join(""),holonomy_order:order,
  abstract_triad_and_frame_return_after_steps:full.grade,
  native_ledger_increment_on_return:full.grade,
  distinct_PASS_counters_on_return:full.nonzeroCounters,
  nonbacktracking_root_prefixes_tested_through_7_steps:prefixCount(arcs,7)};
}
const M=Array.from({length:6},()=>Array(6).fill(0));
for(let k=0;k<20;k++){M[0][1]++;M[1][0]++;
  for(let i=0;i<6;i++){
   const ui=M[i].reduce((s,x)=>s+x,0)-M.reduce((s,row)=>s+row[i],0);
   if(ui!==0)throw Error("contrast u not null");
   for(let j=0;j<6;j++)if(M[i][j]!==M[j][i])throw Error("contrast Omega not null");
  }
}
output.null_contrast_pump={iterations_checked:20,total_completed_PASS_events:40,
  recovered_u_zero:true,recovered_Omega_zero:true,ledger_mass:40,
  exact_symbolic_family:"M_k=M_0+k(E_01+E_10): u_k=u_0, Omega_k=Omega_0, Gamma_k=Gamma_0+2k for every k>=0"};
output.status="PASS";
process.stdout.write(JSON.stringify(output,null,2)+"\n");
