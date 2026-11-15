'use strict';
// Exact typed BRC: each named branch is a permutation consisting only of 3-cycles,
// with independent branch identity/provenance and unit positive-rational weight 1/1.
// No physical force law, floating point, pi, or classical propagator is invoked.
const assert = require('node:assert/strict');
const fs = require('node:fs');
function branches(n) {
  if (n % 3 !== 0) throw Error('n divisible by three required');
  const out = [];
  function build(remaining, sigma) {
    if (!remaining.length) { out.push(sigma.slice()); return; }
    const a = remaining[0];
    for (let j = 1; j < remaining.length; j++) for (let k = j+1; k < remaining.length; k++) {
      const b = remaining[j], c = remaining[k];
      const tail = remaining.filter(x => x !== a && x !== b && x !== c);
      for (const [v,w] of [[b,c],[c,b]]) {
        const next = sigma.slice(); next[a] = v; next[v] = w; next[w] = a;
        build(tail,next);
      }
    }
  }
  build(Array.from({length:n},(_,i)=>i),Array(n).fill(-1));
  return out;
}
function factorial(n) { let v=1n; for(let i=2;i<=n;i++) v*=BigInt(i); return v; }
function countFormula(k) { return factorial(3*k)/(3n**BigInt(k)*factorial(k)); }
function histogram(rows, observer) {
  const m = new Map();
  for(const state of rows) {
    const key=JSON.stringify(observer(state));
    m.set(key,(m.get(key)||0n)+1n); // exact weight 1/1 in N[Q_{>0}^X]
  }
  return m;
}
function sameCycle(sigma,a,b) { return sigma[a]===b || sigma[sigma[a]]===b; }
function permutations(n) {
  const out=[];
  function visit(rem,p){if(!rem.length){out.push(p);return;} for(const x of rem)visit(rem.filter(y=>y!==x),p.concat(x));}
  visit(Array.from({length:n},(_,i)=>i),[]);return out;
}
function conjugate(sig,h) {const out=Array(sig.length);for(let i=0;i<sig.length;i++)out[h[i]]=h[sig[i]];return out;}
const stats=[];
for(const k of [1,2,3]){
  const n=3*k, all=branches(n), unique=new Set(all.map(x=>x.join(',')));
  assert.equal(unique.size,all.length);
  assert.equal(BigInt(all.length),countFormula(k));
  for(const s of all) for(let i=0;i<n;i++) { assert.notEqual(s[i],i); assert.equal(s[s[s[i]]],i); }
  const link=all.filter(s=>s[0]===1).length;
  const same=all.filter(s=>sameCycle(s,0,1)).length;
  const expectedLink=factorial(n-2)/(3n**BigInt(k-1)*factorial(k-1));
  assert.equal(BigInt(link),expectedLink); assert.equal(same,2*link);
  stats.push({n,triads:k,branch_count:all.length,observer_edge_0_to_1:link,observer_same_triad_0_1:same});
}
const all6=branches(6), group6=permutations(6), base=all6[0];
const orbit=new Set(group6.map(h=>conjugate(base,h).join(',')));
assert.equal(orbit.size,40);
const stabilizer=group6.filter(h=>conjugate(base,h).join(',')===base.join(',')).length;
assert.equal(stabilizer,18);
const bset=new Set(all6.map(x=>x.join(',')));
for(const b of all6)for(const h of group6)assert(bset.has(conjugate(b,h).join(',')));
const outdist=histogram(all6,s=>s[0]);
assert.equal(outdist.size,5);for(const count of outdist.values())assert.equal(count,8n);
const visibleLink=all6.filter(s=>s[0]===1);
const hiddenSigns=[];
for (const s of visibleLink) for (let mask=0;mask<16;mask++){
  const signs=[1,1,...Array.from({length:4},(_,j)=>(mask>>j&1)?-1:1)];
  hiddenSigns.push({sigma:s,signs,weight:'1/1'});
}
assert.equal(hiddenSigns.length,128);
assert.equal(histogram(hiddenSigns,x=>[x.sigma,x.signs]).size,128);
// All 40 cycle decompositions decorated by six independent named signs.
// An S6 relabelling conjugates the 3-cycle permutation and transports signs.
const signedStates=[];
for(const sigma of all6)for(let mask=0;mask<64;mask++)
  signedStates.push({sigma,signs:Array.from({length:6},(_,i)=>(mask>>i&1)?1:-1)});
function cycleSignType(state) {
  const seen=new Set(), counts=[];
  for(let a=0;a<6;a++)if(!seen.has(a)) {
    const b=state.sigma[a],c=state.sigma[b];
    seen.add(a);seen.add(b);seen.add(c);
    counts.push([a,b,c].filter(x=>state.signs[x]===1).length);
  }
  return counts.sort((a,b)=>a-b).join(',');
}
const signOrbits=histogram(signedStates,cycleSignType);
assert.equal(signOrbits.size,10);
const expectedOrbitSizes={'0,0':40n,'0,1':240n,'0,2':240n,'0,3':80n,'1,1':360n,'1,2':720n,'1,3':240n,'2,2':360n,'2,3':240n,'3,3':40n};
for(const [key,size] of Object.entries(expectedOrbitSizes)) {
  assert.equal(signOrbits.get(JSON.stringify(key)),size);
  assert.equal(720n%size,0n);
}
const representatives=new Map();
for(const state of signedStates) {
  const type=cycleSignType(state);
  if(!representatives.has(type))representatives.set(type,state);
}
let orbitImages=0;
for(const [type,baseState] of representatives) {
  const observed=new Set();
  for(const h of group6) {
    const sigma=conjugate(baseState.sigma,h),signs=Array(6);
    for(let i=0;i<6;i++)signs[h[i]]=baseState.signs[i];
    observed.add(sigma.join(',')+'|'+signs.join(','));
    assert.equal(cycleSignType({sigma,signs}),type);
    orbitImages++;
  }
  assert.equal(BigInt(observed.size),expectedOrbitSizes[type]);
}
const evidence={schema:'R762BP_EXACT_BRC_TYPED_ENUMERATION_V1',scope:'AUTHOR_BUILT_EXPLICIT_POSITIVE_RATIONAL_LABELLED_BRANCH_CARRIER; CANDIDATE_3_CYCLE_PORT_NETWORK; NOT_NATIVE_FORCE_ADMISSION',branch_weight:'1/1',observer:'named directed Link and optional six named sign queries',checks:stats,six_axis:{S6_size:group6.length,orbit_size:orbit.size,stabilizer_size:stabilizer,edge_outgoing_histogram:Object.fromEntries(Array.from(outdist,([k,v])=>[k,v.toString()])),fixed_directed_link_0_to_1_count:visibleLink.length,visible_signs_fixed_plus_plus_hidden_sign_states:hiddenSigns.length,min_full_link_residual_bits:3,min_signed_hidden_residual_bits:7,all_signed_cycle_states:signedStates.length,signed_S6_orbits:Object.fromEntries(Array.from(signOrbits,([key,v])=>[JSON.parse(key),Number(v)])),signed_orbit_representative_permutations_checked:orbitImages},result:'PASS',independent_review:'NOT_REVIEWED'};
if(process.argv[2])fs.writeFileSync(process.argv[2],JSON.stringify(evidence,null,2)+'\n');
console.log(JSON.stringify(evidence,null,2));
