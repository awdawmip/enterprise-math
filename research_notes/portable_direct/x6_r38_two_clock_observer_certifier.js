'use strict';
// X6 R38: finite exact observer congruence check on the previously published OUTER C12 microcycle.
// This is Boolean, symbolic state-partition verification, not a numerical native triadic law or BRC physical execution.
const N = 6;
const states = Array.from({length: 2*N}, (_,q) => [-1,1].map(eps => ({q,eps}))).flat();
function index(s){return s.q*2+(s.eps === 1 ? 1:0)}
function residue(x,m){return ((x % m) + m)%m}
function obs(s, mode){
  const phase = Math.floor(s.q/2);
  if(mode === 'coarse') return JSON.stringify([phase]);
  if(mode === 'coarse_root6') return JSON.stringify([phase,residue(3*s.eps,6)]);
  if(mode === 'coarse_root12') return JSON.stringify([phase,residue(3*s.eps,12)]);
  throw Error('unknown mode');
}
function next(s, a){return {q:residue(s.q+(a==='T'?1:2),12),eps:s.eps};}
function canonicalClassIds(signatures){
  const ids=new Map();
  return signatures.map(s=>{if(!ids.has(s)) ids.set(s,ids.size);return ids.get(s)});
}
function quotient(mode, actions){
 let ids=canonicalClassIds(states.map(s=>obs(s,mode)));
 const generations=[new Set(ids).size];
 while(true){
   const newIds=canonicalClassIds(states.map((s,i)=>JSON.stringify([obs(s,mode),...actions.map(a=>ids[index(next(s,a))])])));
   if(newIds.every((z,i)=>z===ids[i])) break;
   ids=newIds;
   generations.push(new Set(ids).size);
   if(generations.length > states.length) throw Error('partition did not stabilize');
 }
 const count=new Set(ids).size;
 function shortestWitness(s,t){
   let work=[[s,t,[]]]; const seen=new Set();
   for(let head=0;head<work.length;head++){
     const [x,y,w]=work[head];const key=index(x)+','+index(y);
     if(seen.has(key))continue;seen.add(key);
     if(obs(x,mode)!==obs(y,mode))return w;
     for(const a of actions) work.push([next(x,a),next(y,a),[...w,a]]);
   }
   return null;
 }
 let checked=0;
 for(const x of states)for(const y of states){
   const w=shortestWitness(x,y);const eq=ids[index(x)]===ids[index(y)];
   if(eq !== (w===null))throw Error('witness and partition disagree '+JSON.stringify([x,y,w,eq]));
   checked++;
 }
 const chiralityErasure=Array.from({length:12},(_,q)=>ids[index({q,eps:1})]===ids[index({q,eps:-1})]);
 const gateErasure=Array.from({length:6},(_,k)=>ids[index({q:2*k,eps:1})]===ids[index({q:2*k+1,eps:1})]);
 return {
   count, bits:Math.ceil(Math.log2(count)), partition_sizes:Array.from(new Set(ids)).map(g=>ids.filter(x=>x===g).length).sort((a,b)=>a-b),
   refinement_block_counts:generations, exhaustive_ordered_pairs:checked,
   chirality_identification_safe:chiralityErasure.every(Boolean),
   gate_identification_safe:gateErasure.every(Boolean),
   gate_witness:shortestWitness({q:0,eps:1},{q:1,eps:1}),
   chirality_witness:shortestWitness({q:0,eps:1},{q:0,eps:-1})
 };
}
const cases=[
 ['fine_coarse', 'coarse',['T'],12,4],
 ['coarse_step_coarse','coarse',['U'],6,3],
 ['fine_coarse_root6','coarse_root6',['T'],12,4],
 ['fine_coarse_root12','coarse_root12',['T'],24,5],
 ['coarse_step_root12','coarse_root12',['U'],12,4]
];
const result={schema:'X6_R38_FINITE_OBSERVER_CERTIFICATE_V1', scope:'C12 OUTER finite phase and two formal chirality labels; readout and event models explicitly typed; no native TRIADIC_CLOSURE_E full-carrier claim',states:states.length, verification:'EXHAUSTIVE_ALL_ORDERED_STATE_PAIRS_AND_PARTITION_FIXPOINT',cases:{}};
for(const [id,mode,actions,count,bits] of cases){
 const r=quotient(mode,actions);
 if(r.count!==count||r.bits!==bits)throw Error('unexpected count for '+id);
 result.cases[id]={observer:mode,actions,...r};
}
if(result.cases.fine_coarse.gate_witness.join(',')!=='T')throw Error('one fine-step gate witness missing');
if(result.cases.coarse_step_coarse.gate_witness!==null)throw Error('coarse-step gate erasure invalid');
if(result.cases.fine_coarse_root12.chirality_witness.length!==0)throw Error('C12 chirality should be currently visible');
if(result.cases.fine_coarse_root6.chirality_witness!==null)throw Error('C6 chirality should be invisible');
result.total_ordered_pair_checks=cases.length*states.length*states.length;
result.all_assertions='PASS';
process.stdout.write(JSON.stringify(result,null,2)+'\n');
