'use strict';
// Exact finite positive branch enumeration. No floating arithmetic, no external packages.
const assert=require('node:assert/strict');
const n=6, A=[0,1,2,3,4,5];
function* permutations(a){
  if(a.length===0){yield [];return;}
  for(let i=0;i<a.length;i++) for(const r of permutations(a.filter((_,j)=>j!==i)))yield[a[i],...r];
}
const G=[...permutations(A)];
function pow(g,r){let out=A.slice();for(let t=0;t<r;t++)out=out.map(x=>g[x]);return out;}
const tuples=(i,j)=>{const others=A.filter(x=>x!==i&&x!==j);return [...others.map(k=>[i,j,k]),...others.map(k=>[j,i,k])];};
const pairHistogram={0:0,2:0,4:0,8:0},signatureCounts={};
const perPair=[];
const canonicalSignatures=new Map();
for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){
  const fiber=tuples(i,j);
  assert.equal(fiber.length,8);
  const K=G.filter(g=>[g[i],g[j]].sort().join(',')===[i,j].join(','));
  assert.equal(K.length,48);
  let counts={0:0,2:0,4:0,8:0};
  for(const g of K){
    const seq=[];
    for(let r=1;r<=12;r++){
      const h=pow(g,r);
      const fixed=fiber.filter(t=>t.every(x=>h[x]===x)).length;
      seq.push(fixed);
      assert.ok([0,2,4,8].includes(fixed));
    }
    const signature=seq.join(',');
    signatureCounts[signature]=(signatureCounts[signature]||0)+1;
    if(!canonicalSignatures.has(signature))canonicalSignatures.set(signature,seq);
    counts[seq[0]]++;pairHistogram[seq[0]]++;
    // Immediate count formula: visible-swap => 0, otherwise 2 * hidden fixed points.
    const visibleFixed=g[i]===i&&g[j]===j;
    const hiddenFixed=A.filter(x=>x!==i&&x!==j&&g[x]===x).length;
    assert.equal(seq[0],visibleFixed?2*hiddenFixed:0);
  }
  assert.deepEqual(counts,{0:33,2:8,4:6,8:1});
  perPair.push({pair:[i+1,j+1],count:48,first_return_histogram:counts});
}
assert.equal(perPair.length,15);
assert.deepEqual(pairHistogram,{0:495,2:120,4:90,8:15});
const unique=[...canonicalSignatures.values()];
assert.equal(unique.length,6);
const prefix2=new Set(unique.map(s=>s.slice(0,2).join(',')));
const prefix1=new Set(unique.map(s=>s[0]));
assert.equal(prefix2.size,6);
assert.equal(prefix1.size,4);
const labels=[...Object.entries(signatureCounts)].map(([signature,multiplicity])=>({first_two:signature.split(',').slice(0,2).map(Number),multiplicity,multiplicity_per_pair:multiplicity/15,period_signature:signature.split(',').map(Number)})).sort((a,b)=>a.first_two[0]-b.first_two[0] || a.first_two[1]-b.first_two[1]);
assert.deepEqual(labels.map(x=>x.multiplicity_per_pair).sort((a,b)=>a-b),[1,6,8,8,12,13]);
// A fixed point in the eight-sheet fiber requires both ordered visible legs and the hidden axis to return.
// That scalar fixed-point sequence cannot distinguish all group elements nor all conjugacy classes.
const example={pair:[1,2],identity_visible_double_hidden:{g:[0,1,3,2,5,4],first_two:[0,8]},swapped_visible_identity_hidden:{g:[1,0,2,3,4,5],first_two:[0,8]}};
for(const ex of [example.identity_visible_double_hidden,example.swapped_visible_identity_hidden]){
  const fiber=tuples(0,1);assert.deepEqual([1,2].map(r=>{const h=pow(ex.g,r);return fiber.filter(t=>t.every(x=>h[x]===x)).length}),ex.first_two);
}
const evidence={schema:'R762BB_EXACT_BRC_UNORDERED_PAIR_HOLONOMY_V1',model:'S6 ordered triples over unordered visible pair; K=S2 x S4; positive named-source BRC fiber size 8',complete_domains:{axis_labels:6,unordered_visible_pairs:15,full_group_permutations:720,stabilizer_elements_per_pair:48,checked_based_loops:720,repeated_power_window:12,source_records_per_pair:8,signature_classes:6},first_return_histogram:pairHistogram,signatures:labels,minimum_signature_horizon:2,all_assertions_passed:true,example};
console.log(JSON.stringify(evidence,null,2));
