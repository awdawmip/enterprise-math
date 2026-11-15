'use strict';
// Exact finite verification for the conditional S6-equivariant triad-witness theorem.
const n=6;
const range=Array.from({length:n},(_,i)=>i);
function permutations(xs){if(!xs.length)return [[]];const out=[];for(let i=0;i<xs.length;i++)for(const tail of permutations([...xs.slice(0,i),...xs.slice(i+1)]))out.push([xs[i],...tail]);return out;}
const P=permutations(range); if(P.length!==720)throw Error('S6 cardinality');
const comp=(r,s)=>range.filter(x=>x!==r&&x!==s);
const apply=(p,x)=>p[x];
const compose=(q,p)=>range.map(x=>q[p[x]]);
const transpose=(i)=>range.map(x=>x===i?i+1:x===i+1?i:x);
const gens=Array.from({length:5},(_,i)=>transpose(i));
const index=(p,r,s,j)=>{
 const t=comp(r,s)[j];return comp(apply(p,r),apply(p,s)).indexOf(apply(p,t));
};
const pairs=range.flatMap(r=>range.filter(s=>s!==r).map(s=>[r,s]));
let transportChecks=0, cocycleChecks=0, stabilizerChecks=0, fixedSelectorCandidates=0, sourceEquivarianceChecks=0;
let nontrivialTransportWitness=null;
for(const [r,s] of pairs){
 const k=comp(r,s);
 const stab=P.filter(p=>p[r]===r&&p[s]===s);
 if(stab.length!==24)throw Error('Wrong stabilizer size');
 for(const t of k){
   stabilizerChecks++;
   if(stab.every(p=>p[t]===t))fixedSelectorCandidates++;
 }
 for(const p of P){
   for(let j=0;j<4;j++){
     const b=index(p,r,s,j);transportChecks++;
     if(!(b>=0&&b<4)) throw Error('Transport out of range');
     if(!nontrivialTransportWitness&&r===0&&s===1&&b!==j)nontrivialTransportWitness={pair:[r+1,s+1],permutation:p.map(x=>x+1),before:j,after:b,third_before:k[j]+1,third_after:p[k[j]]+1};
     if(comp(p[r],p[s])[b]!==p[k[j]])throw Error('Source witness not covariant');
     sourceEquivarianceChecks++;
     for(const q of gens){
       const lhs=index(compose(q,p),r,s,j);
       const rhs=index(q,p[r],p[s],b);
       cocycleChecks++;
       if(lhs!==rhs)throw Error('Cocycle failed');
     }
   }
 }
}
if(fixedSelectorCandidates!==0||transportChecks!==86400||cocycleChecks!==432000||stabilizerChecks!==120||sourceEquivarianceChecks!==86400)throw Error('count mismatch');
const triples=pairs.reduce((acc,[r,s])=>acc+comp(r,s).length,0);
if(triples!==120)throw Error('wrong ordered triple count');
const output={schema:'R762BN_S6_TRIAD_WITNESS_EXACT_V1',domain:{native_axes:6,permutations:P.length,ordered_visible_pairs:pairs.length,third_axis_candidates_per_pair:4,third_sign_sectors:2},checks:{stabilizer_fixed_candidate_tests:stabilizerChecks,stabilizer_fixed_candidates:fixedSelectorCandidates,transport_source_covariance:sourceEquivarianceChecks,transport_range:transportChecks,group_action_cocycle_generator_checks:cocycleChecks,ordered_distinct_axis_triples_per_sign:triples},witness:nontrivialTransportWitness,conclusions:{no_deterministic_equivariant_third_axis_selector_without_extra_state:true,conditional_orbit_sizes_per_sign:[0,4],local_witness_min_bits_for_one_sign:2,local_witness_min_bits_if_both_signs_admitted:3,scope:'P000 signed X6 axes plus S6 coordinate skeleton; force-closure and force covariance are explicitly conditional; no native Source event authorization inferred'},validation:'EXACT_FINITE_ENUMERATION_NODE_JS; AUTHOR_CHECKED; NOT_INDEPENDENTLY_REVIEWED'};
console.log(JSON.stringify(output,null,2));
