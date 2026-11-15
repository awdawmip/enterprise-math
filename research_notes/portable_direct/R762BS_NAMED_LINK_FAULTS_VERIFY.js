'use strict';
// R762BS: exact, reproducible finite verifier. Node.js >=18; no dependencies.
const assert=(ok,msg)=>{if(!ok)throw new Error(msg);};
const six=[1,2,3,4,5,6];
const permute=a=>a.length===0?[[]]:a.flatMap((v,i)=>permute(a.filter((_,j)=>i!==j)).map(s=>[v,...s]));
const cycleLengths=p=>{const seen=new Set(),lens=[];for(const k of six){if(seen.has(k))continue;let a=k,n=0;while(!seen.has(a)){seen.add(a);n++;a=p[a-1];}lens.push(n);}return lens.sort((a,b)=>a-b).join(',');};
const all=permute(six).filter(p=>cycleLengths(p)==='3,3');
const states=all.filter(p=>p[0]===2).sort((a,b)=>a.join(',').localeCompare(b.join(',')));
assert(all.length===40&&states.length===8,'Incorrect BRC branch population');
const queries=[];for(const a of six)for(const b of six){if(a===b)continue;const bits=states.map(p=>Number(p[a-1]===b));const positives=bits.reduce((s,v)=>s+v,0);if(positives!==0&&positives!==8){assert(positives===2,'A nonconstant Link query must have two positive branches');queries.push({name:a+'->'+b,bits});}}
assert(queries.length===20,'Wrong query count');
const distinct=new Set(queries.map(q=>q.bits.join('')));assert(distinct.size===16,'Wrong unique-query count');
const pairMasks=[];for(let i=0;i<8;i++)for(let j=i+1;j<8;j++){let mask=0;for(let k=0;k<20;k++)if(queries[k].bits[i]!==queries[k].bits[j])mask|=(1<<k);pairMasks.push(mask);}
assert(pairMasks.length===28,'Wrong pair count');
const popcount=x=>{x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0F0F0F0F)*0x01010101)>>>24;};
const histogram=Array.from({length:21},()=>Array(21).fill(0)),best=Array(7).fill(null).map(()=>({length:null,count:0,example:null}));
let examined=0;
for(let H=0;H<(1<<20);H++){
 const size=popcount(H);let distance=20;
 for(const mask of pairMasks){const d=popcount(H&mask);if(d<distance)distance=d;if(distance===0)break;}
 histogram[size][distance]++;examined++;
 for(let threshold=1;threshold<=6;threshold++)if(distance>=threshold){const v=best[threshold];if(v.length===null||size<v.length){v.length=size;v.count=1;v.example=H;}else if(size===v.length)v.count++;}
}
const lengths=[null,5,6,10,12,15,16],counts=[null,1944,52,2270,551,224,16];
for(let d=1;d<=6;d++)assert(best[d].length===lengths[d]&&best[d].count===counts[d],'Threshold '+d+' mismatch');
assert(examined===(1<<20),'Enumeration incomplete');
const maxFullDistance=Math.min(...pairMasks.map(popcount));assert(maxFullDistance===6,'Full-panel distance differs');
for(let k=0;k<=20;k++){const n=histogram[k].reduce((s,x)=>s+x,0);let choose=1;for(let i=1;i<=k;i++)choose=choose*(21-i)/i;assert(n===Math.round(choose),'Binomial class '+k+' incomplete');}
const optima=best.slice(1).map((b,i)=>({target_distance:i+1,min_named_queries:b.length,number_of_minimum_panels:b.count,example_queries:queries.filter((_,j)=>(b.example&(1<<j))!==0).map(q=>q.name),example_actual_distance:Math.min(...pairMasks.map(v=>popcount(v&b.example)))}));
const signed=[0,1,2].map(t=>({adversarial_flips:t,required_distance:2*t+1,min_link_queries:best[2*t+1].length,hidden_sign_calls:4*(2*t+1),total_named_atomic_queries:best[2*t+1].length+4*(2*t+1)}));
const queryTransforms=permute([3,4,5,6]).map(t=>{const g=[0,1,2,...t],toIndex=new Map(queries.map((q,i)=>[q.name,i]));return queries.map(q=>{const [a,b]=q.name.split('->').map(Number);const j=toIndex.get(g[a]+'->'+g[b]);assert(j!==undefined,'S4 action escaped names');return j;});});
const transform=(mask,mapping)=>{let out=0;for(let i=0;i<20;i++)if(mask&(1<<i))out|=1<<mapping[i];return out;};
const orbitCounts=[];
for(let d=1;d<=6;d++){
 const b=best[d],seen=new Set(),sizeHistogram={};
 for(let H=0;H<(1<<20);H++){
  if(popcount(H)!==b.length||seen.has(H))continue;
  let dist=20;for(const p of pairMasks){const v=popcount(H&p);if(v<dist)dist=v;if(dist<d)break;}if(dist<d)continue;
  const orbit=new Set(queryTransforms.map(m=>transform(H,m)));for(const v of orbit)seen.add(v);
  const n=orbit.size;sizeHistogram[n]=(sizeHistogram[n]||0)+1;
 }
 assert(seen.size===b.count,'S4 classification incomplete');
 orbitCounts.push({target_distance:d,orbit_size_counts:sizeHistogram,number_of_orbits:Object.values(sizeHistogram).reduce((a,b)=>a+b,0)});
}
assert(orbitCounts[2].number_of_orbits===112&&orbitCounts[4].number_of_orbits===16,'Orbit count check');
console.log(JSON.stringify({schema:'EM_R762BS_NAMED_LINK_FAULT_CERTIFICATE_V1',source_count:all.length,fixed_link:'1->2',conditional_branches:states.length,named_informative_queries:queries.length,unique_truth_sets:distinct.size,all_named_panels_examined:examined,all_source_pairs:pairMasks.length,full_panel_distance:maxFullDistance,optima,independent_hidden_sign_bits:4,signed_corruption_budgets:signed,S4_orbit_classification:orbitCounts,scope:'CONDITIONAL_DIRECTED_LINK_AND_INDEPENDENT_SIGN_ORACLES',review:'NOT_REVIEWED'},null,2));
