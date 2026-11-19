// R762GA: exact S6 / fixed K4-S4 / marked K4-S3 signed STAR orbit checker.
// Node.js (no dependencies), positive BRC branch metadata, not native event permission.
'use strict';
const assert = require('node:assert/strict');
function permutations(arr) {
  return arr.length === 0 ? [[]] :
    arr.flatMap((v, i) => permutations(arr.filter((_, j) => j !== i)).map(q => [v, ...q]));
}
const E = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
const s6 = permutations([0,1,2,3,4,5]);
const s4 = permutations([0,1,2,3]);
function star(v) { return E.map((e,i)=>e.includes(v)?i:null).filter(x=>x!==null); }
function edgePerm(q) {
  return E.map(([a,b]) => {
    const u=Math.min(q[a],q[b]),v=Math.max(q[a],q[b]);
    const i=E.findIndex(([x,y])=>x===u&&y===v);
    assert(i>=0); return i;
  });
}
const k4 = s4.map(edgePerm);
const frame = [0,1,2,3].map(star);
const excluded = frame[0];
function stableSet(a) { return [...a].sort((x,y)=>x-y).join(','); }
const markedStabilizer = k4.filter(p=>stableSet(excluded.map(i=>p[i]))===stableSet(excluded));
assert.equal(markedStabilizer.length,6);
function rotate(c) {const j=c.indexOf(Math.min(...c));return c.slice(j).concat(c.slice(0,j));}
function signedStates(triples) {
  const ret=[];
  for(const t of triples) {
    const [a,b,c]=t;
    for(const cycle of [[a,b,c],[a,c,b]])
      for(let bits=0;bits<8;bits++) {
        const signs=Object.fromEntries(t.map((x,j)=>[x,((bits>>j)&1)?-1:1]));
        const key=cycle.map(i=>i+(signs[i]<0?'-':'+')).join('/');
        ret.push({cycle,signs,key,neg:Object.values(signs).filter(x=>x<0).length});
      }
  }
  return ret;
}
function transport(s,p) {
  const c=rotate(s.cycle.map(i=>p[i]));
  const signs=Object.fromEntries(Object.entries(s.signs).map(([i,x])=>[p[Number(i)],x]));
  return c.map(i=>i+(signs[i]<0?'-':'+')).join('/');
}
function orbits(states,group) {
  const byKey=new Map(states.map(s=>[s.key,s]));
  assert.equal(byKey.size,states.length);
  const remain=new Set(byKey.keys()), out=[];
  while(remain.size) {
    const s=byKey.get(remain.values().next().value);
    const orb=new Set(group.map(p=>transport(s,p)));
    for(const k of orb){assert(byKey.has(k));remain.delete(k);}
    out.push({negative_count:s.neg,orbit_size:orb.size});
  }
  return out.sort((a,b)=>a.negative_count-b.negative_count||a.orbit_size-b.orbit_size);
}
const allTriples=[];
for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)for(let k=j+1;k<6;k++)allTriples.push([i,j,k]);
const all=orbits(signedStates(allTriples),s6);
const full=orbits(signedStates(frame),k4);
const marked=orbits(signedStates(frame.filter(t=>stableSet(t)!==stableSet(excluded))),markedStabilizer);
assert.deepEqual(all,[0,1,2,3].map((k)=>({negative_count:k,orbit_size:[40,120,120,40][k]})));
assert.deepEqual(full,[0,1,2,3].map((k)=>({negative_count:k,orbit_size:[8,24,24,8][k]})));
assert.deepEqual(marked,[0,1,1,1,2,2,2,3].map(k=>({negative_count:k,orbit_size:6})));
const result={
  schema:'R762GA_EXACT_FINITE_ORBIT_EVIDENCE_V1',
  status:'PASS', S6_size:s6.length, K4_S4_size:k4.length,
  marked_S3_size:markedStabilizer.length, all_signed_states:320,
  frame_signed_states:64, marked_signed_states:48,
  S6_signed_orbits:all, fixed_frame_S4_signed_orbits:full,
  marked_frame_S3_signed_orbits:marked,
  exact_scope:'Signed metadata on positive BRC branch labels; no native signed-force closure/event authorization',
  review:'NOT_REVIEWED'
};
console.log(JSON.stringify(result,null,2));
