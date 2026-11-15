'use strict';
// Exact finite enumeration of row-family augmentations of four P000-compatible
// FCC/K4 carrier STAR coordinate observers; no force-event permissions assumed.
const fs = require('fs');
const assert = require('assert').strict;
const triples = [];
for (let a = 0; a < 6; a++) for (let b = a + 1; b < 6; b++)
  for (let c = b + 1; c < 6; c++) triples.push([a,b,c]);
const label = triple => triple.map(v => v + 1).join('');
const find = s => triples.findIndex(t => label(t) === s);
const star = ['123', '145', '246', '356'];
const face = ['124', '135', '236', '456'];
const starIdx = star.map(find), faceIdx = face.map(find);
const baseMask = starIdx.reduce((m,i) => m | (1 << i), 0);
const available = triples.map((_,i)=>i).filter(i=>!starIdx.includes(i));
const pathIdx = available.filter(i=>!faceIdx.includes(i));
assert.equal(starIdx.length,4); assert.equal(faceIdx.length,4); assert.equal(pathIdx.length,12);
function popcount(x) {
  x -= (x >>> 1) & 0x55555555;
  x = (x & 0x33333333) + ((x >>> 2) & 0x33333333);
  return (((x + (x >>> 4)) & 0x0f0f0f0f) * 0x01010101) >>> 24;
}
const cuts=[];
for (let s=1;s<32;s++) { // one of complementary cuts: 31
  let crossing=0;
  for (let i=0;i<20;i++) {
    const k=triples[i].reduce((count,v)=>count+((s>>v)&1),0);
    if (k>0 && k<3) crossing |= 1<<i;
  }
  cuts.push(crossing);
}
assert.equal(cuts.length,31);
const degree = mask => Array.from({length:6},(_,v)=>triples.reduce((count,t,i)=>count+(((mask>>i)&1)&&t.includes(v)?1:0),0));
const distance = mask => cuts.reduce((min,cut)=>Math.min(min,popcount(mask&cut)),Infinity);
assert.deepEqual(degree(baseMask),[2,2,2,2,2,2]);
assert.equal(distance(baseMask),2);
const report = {schema:'EM_R762BM_FCC_STAR_AUGMENTATION_V1',
  frozen_pin:'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
  prior_math:'R762BL_X6_TRIAD_HYPERGRAPH_CUT_THEOREM.md@35f7fe654506441106e5c64dd9a15c78acd0c358',
  axes_as_K4_edges:['12','13','14','23','24','34'],
  all_triplets_lex:triples.map(label), carrier_star_rows:star, face_rows:face,
  path_rows:pathIdx.map(i=>label(triples[i])), base_distance:2,
  examined_augmentations:1<<available.length,
  by_q:{}, one_error_minimal_additions:[], s4_invariant_families:[]};
let counts=Array(11).fill(0);
const templates=Array.from({length:11},()=>null);
const q3Candidates=[];
for (let sm=0;sm<(1<<available.length);sm++) {
  let mask=baseMask;
  for (let j=0;j<available.length;j++) if ((sm>>j)&1) mask |= 1<<available[j];
  const added = popcount(sm);
  const d = distance(mask);
  const deg = degree(mask);
  for (let q=2;q<=10;q++) {
    if (added === 2*(q-2) && d>=q) {
      assert.ok(deg.every(x=>x===q),'nonregular minimum for q='+q);
      counts[q]++;
      if (!templates[q]) templates[q]=available.filter((_,j)=>(sm>>j)&1).map(i=>label(triples[i]));
      if(q===3)q3Candidates.push(available.filter((_,j)=>(sm>>j)&1).map(i=>label(triples[i])));
    }
    if (added < 2*(q-2)) assert.ok(d<q,'degree lower bound violation q='+q);
  }
}
const expected=[null,null,1,6,30,84,114,84,30,6,1];
for(let q=2;q<=10;q++){
  assert.equal(counts[q],expected[q],'exact enumeration q='+q);
  report.by_q[q]={minimal_added:2*(q-2),minimal_total:2*q,optimal_extension_count:counts[q],witness_added:templates[q]};
}
const sortedPairs=q3Candidates.map(pair=>pair.slice().sort()).sort((a,b)=>a.join().localeCompare(b.join()));
assert.equal(sortedPairs.length,6);
const pathNames=new Set(pathIdx.map(i=>label(triples[i])));
for(const [a,b] of sortedPairs){
  assert.ok(pathNames.has(a)&&pathNames.has(b),'every optimal pair is PATH');
  assert.equal(new Set((a+b).split('')).size,6,'added triples complement one another');
}
report.one_error_minimal_additions=sortedPairs;
for(const addFace of [false,true])for(const addPath of [false,true]){
 let mask=baseMask;
 if(addFace)for(const i of faceIdx) mask|=1<<i;
 if(addPath)for(const i of pathIdx) mask|=1<<i;
 report.s4_invariant_families.push({add_face_orbit:addFace,add_path_orbit:addPath,rows:popcount(mask),min_distance:distance(mask),degree:degree(mask)[0]});
}
assert.deepEqual(report.s4_invariant_families.map(x=>[x.rows,x.min_distance]),[[4,2],[16,8],[8,4],[20,10]]);
const incident=star.filter(s=>s.includes('1'));
assert.deepEqual(incident,['123','145']);
assert.equal(popcount(baseMask & cuts[0]),2);
report.ambiguity={source_difference:'e_1',differing_rows:incident,received_construction:'take one differing STAR row from each source; remaining two rows agree'};
report.claim_scope='Entire-row Hamming errors/known erasures of coordinate-triad observers on signed Z^6 / diagonal, not TRIADIC_CLOSURE_E force-event permissions';
const out=JSON.stringify(report,null,2)+'\n';
if(process.argv[2])fs.writeFileSync(process.argv[2],out);
process.stdout.write(JSON.stringify({examined:report.examined_augmentations,counts:report.by_q,one_error_additions:report.one_error_minimal_additions,s4:report.s4_invariant_families},null,2)+'\n');
