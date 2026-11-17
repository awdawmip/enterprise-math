'use strict';
// Exhaustive exact-integer certificate for a conditional six-source K4 BRC.
const E=['01','02','03','12','13','23'], full=63;
const popcount=m=>m.toString(2).replace(/0/g,'').length;
const triples=Array.from({length:64},(_,m)=>m).filter(m=>popcount(m)===3).map(m=>Math.min(m,full^m));
const states=[...new Set(triples)].sort((a,b)=>a-b);
const index=new Map(states.map((m,i)=>[m,i]));
const stars=new Set(Array.from({length:4},(_,v)=>{
 let m=0;E.forEach((e,i)=>{if(e.includes(String(v)))m|=1<<i});return Math.min(m,full^m);
}));
const F=states.map(x=>stars.has(x)?1:0),P=F.map(x=>1-x);
function* partitions(prefix=[0],mx=0){
 if(prefix.length===6){yield prefix;return}
 for(let j=0;j<=mx+1;j++)yield* partitions([...prefix,j],Math.max(mx,j));
}
function adjacency(part){return states.map(m=>{
 const out=[];
 for(let x=0;x<6;x++)if(m&(1<<x))for(let y=0;y<6;y++)if(!(m&(1<<y))&&part[x]===part[y]){
   const t=m^(1<<x)^(1<<y);out.push([index.get(Math.min(t,full^t)),part[x]]);
 }
 return out;
});}
function signature1(rows,k,s){
 const f=Array(k).fill(0),p=Array(k).fill(0);
 for(const [t,c] of rows[s]){f[c]+=F[t];p[c]+=P[t]}
 return JSON.stringify([F[s],P[s],f,p]);
}
function classIds(signatures){const ids=new Map();return signatures.map(s=>{
  if(!ids.has(s))ids.set(s,ids.size);return ids.get(s);
});}
function unitUncoloredO2(rows){
 let f=F.slice(),p=P.slice();const o=states.map((_,i)=>[[f[i],p[i]]]);
 for(let h=1;h<=2;h++){
  f=rows.map(row=>row.reduce((sum,[to])=>sum+f[to],0));
  p=rows.map(row=>row.reduce((sum,[to])=>sum+p[to],0));
  states.forEach((_,i)=>o[i].push([f[i],p[i]]));
 }
 return o.map(x=>JSON.stringify(x));
}
function certificate(){
 if(states.length!==10||F.reduce((a,b)=>a+b,0)!==4)throw Error('wrong state enumeration');
 const counts={partitions:0,state_observations:0,same_class_pairs:0,source_channel_lump_checks:0,
   distinct_signature_classes:{},fibre_repair:{},strict_source_refinements:0,
   source_classes_for_unit_uncolored:{},all_state_rows:0};
 for(const part of partitions()){
  counts.partitions++;
  const k=Math.max(...part)+1, rows=adjacency(part),
   colored=classIds(states.map((_,s)=>signature1(rows,k,s))),
   uncolored=classIds(unitUncoloredO2(rows));
  const n=new Set(colored).size;
  counts.distinct_signature_classes[n]=(counts.distinct_signature_classes[n]||0)+1;
  counts.state_observations+=10;counts.all_state_rows+=rows.length;
  const fibers=new Map();
  for(let s=0;s<10;s++){
   if(!fibers.has(uncolored[s]))fibers.set(uncolored[s],new Set());
   fibers.get(uncolored[s]).add(colored[s]);
  }
  const largest=Math.max(...[...fibers.values()].map(s=>s.size));
  counts.fibre_repair[largest]=(counts.fibre_repair[largest]||0)+1;
  if(largest>1)counts.strict_source_refinements++;
  const uN=new Set(uncolored).size;
  const pair=`${uN}->${n}`;
  counts.source_classes_for_unit_uncolored[pair]=(counts.source_classes_for_unit_uncolored[pair]||0)+1;
  for(let s=0;s<10;s++)for(let t=s+1;t<10;t++)if(colored[s]===colored[t]){
   counts.same_class_pairs++;
   for(let channel=0;channel<k;channel++){
    const left=Array(n).fill(0),right=Array(n).fill(0);
    for(const [to,c] of rows[s])if(c===channel)left[colored[to]]++;
    for(const [to,c] of rows[t])if(c===channel)right[colored[to]]++;
    counts.source_channel_lump_checks++;
    if(left.some((x,i)=>x!==right[i]))throw Error(`failed equitability ${part.join('')}: ${s},${t}; channel ${channel}`);
   }
  }
 }
 if(counts.partitions!==203)throw Error('partitions not exhaustive');
 const expectedHist={'2':2,'3':27,'4':28,'5':66,'6':24,'7':24,'10':32};
 if(JSON.stringify(counts.distinct_signature_classes)!==JSON.stringify(expectedHist))throw Error('histogram mismatch');
 // Exact separating witness for loss of source-query information.
 const part=[0,0,0,0,1,1],rows=adjacency(part),s=4,t=6;
 const u=unitUncoloredO2(rows);
 if(u[s]!==u[t])throw Error('witness not uncolored-equivalent');
 const sourceF=state=>Array.from({length:2},(_,c)=>rows[state].filter(([to,k])=>k===c&&F[to]).length);
 if(sourceF(s).join()!=[2,0].join()||sourceF(t).join()!=[1,1].join())throw Error('witness failed');
 return {schema:'R762CT_SOURCE_RESOLVED_K4_BRC_EXACT_CERTIFICATE_V1',date:'2026-11-17',model:'conditional K4 10-state source-matched swap, channel-selective positive N-BRC',state_masks:states,
  source_class_order:E,observer:'F/P terminal counts of every specified source-class word',result:'O1_color(s)=O1_color(t) iff all future color-word F/P counts agree, for all 203 equality partitions and all positive source weights',
  counts,unit_uncolored_comparison:'O2 of uncolored unit-weight sum transition',witness:{partition:'000011',state_indices:[s,t],masks:[states[s],states[t]],uncolored_O2:JSON.parse(u[s]),source_selected_F_counts:[sourceF(s),sourceF(t)]},
  proof_scope:'Exhaustive partition and exact equitable quotient arithmetic; extends to arbitrary positive weight per source by wordwise nonzero common scaling',independent_review:'NOT_REVIEWED'};
}
if(require.main===module)console.log(JSON.stringify(certificate(),null,2));
module.exports={certificate};
