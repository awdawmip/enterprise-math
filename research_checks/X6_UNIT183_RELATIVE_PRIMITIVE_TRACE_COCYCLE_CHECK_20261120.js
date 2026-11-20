// X6 Unit183: independent exact integer checks for relative primitive-step reconstruction.
// Frozen mathematical input: native signed six-coordinate steps and can6.
'use strict';
const N=6;
const vectors=[];
for(let i=0;i<N;i++) for(let sg of [1,-1]) {
  const v=Array(N).fill(0);v[i]=sg;
  vectors.push({tag:`${sg===1?'+':'-'}e${i+1}`,v});
}
const min=v=>Math.min(...v);
const eq=(a,b)=>a.length===b.length&&a.every((x,i)=>x===b[i]);
const add=(a,b)=>a.map((x,i)=>x+b[i]);
const normalize=z=>{const h=min(z);return {r:z.map(x=>x-h),h};};
const addDepth=(r,h)=>r.map(x=>x+h);
function relativeStep(r, v){const w=add(r,v),d=min(w);return {r:w.map(x=>x-d),depth_delta:d};}
function recoverDirection(before,after){let res=[];for(const {tag,v} of vectors){if(eq(relativeStep(before,v).r,after))res.push({tag,v});}return res;}
function check(ok,msg){if(!ok)throw new Error(msg);}
// All can6 states in a fully declared box [0,2]^6: exactly 3^6 - 2^6 = 665.
let box_states=0,edge_tests=0,depth_translation_tests=0,nonzero_depth_moves=0;
for(let code=0;code<3**N;code++){
  let t=code; const a=[];for(let i=0;i<N;i++){a.push(t%3);t=Math.floor(t/3);}
  if(min(a)!==0)continue;
  box_states++;
  const successors=new Set();
  for(const {tag,v} of vectors){
    const nxt=relativeStep(a,v);
    check(min(nxt.r)===0,`noncanonical ${a} ${tag}`);
    check([-1,0,1].includes(nxt.depth_delta),`invalid cocycle ${a} ${tag}`);
    const possibilities=recoverDirection(a,nxt.r);
    check(possibilities.length===1&&possibilities[0].tag===tag,`non-unique direction ${a} ${tag}`);
    successors.add(nxt.r.join(','));
    edge_tests++;
    if(nxt.depth_delta!==0)nonzero_depth_moves++;
    for(const h of [-5,0,8]){
      const direct=normalize(add(addDepth(a,h),v));
      check(eq(nxt.r,direct.r)&&direct.h===h+nxt.depth_delta,`depth mismatch ${a} ${tag} ${h}`);
      depth_translation_tests++;
    }
  }
  check(successors.size===12,`duplicate outgoing observer edge from ${a}`);
}
// Entire primitive labelled trace from 0: no event identities are stored in the reconstruction.
let paths_checked=0,trace_steps_checked=0,max_depth_seen=0;
function traceAll(full, relative, seen, depth, length, limit){
  const reconstructed=addDepth(relative,depth);
  check(eq(full,reconstructed),'reconstruction mismatch');
  paths_checked++;
  max_depth_seen=Math.max(max_depth_seen,Math.abs(depth));
  if(length===limit)return;
  for(const {tag,v} of vectors){
    const nextFull=add(full,v),nextObs=normalize(nextFull);
    const possibilities=recoverDirection(relative,nextObs.r);
    check(possibilities.length===1&&possibilities[0].tag===tag,'label lost');
    const e=relativeStep(relative,possibilities[0].v);
    check(eq(e.r,nextObs.r)&&depth+e.depth_delta===nextObs.h,'trace lift wrong');
    trace_steps_checked++;
    traceAll(nextFull,nextObs.r,seen.concat([tag]),nextObs.h,length+1,limit);
  }
}
for(const h0 of [-2,3])traceAll(Array(N).fill(h0),Array(N).fill(0),[],h0,0,4);
check(paths_checked===2*(1+12+12**2+12**3+12**4),'unexpected trace count');
// A six-step all-positive diagonal cycle is invisible to can6 but has depth shift +1.
let r=Array(N).fill(0),h=0;
for(let i=0;i<N;i++){const x=relativeStep(r,vectors[2*i].v);r=x.r;h+=x.depth_delta;}
check(eq(r,Array(N).fill(0))&&h===1,'positive diagonal cycle failed');
// Shift-dependent signed direction selector gives different observer successors.
const z0=Array(N).fill(0),z1=Array(N).fill(1);
const selected0=normalize(add(z0,vectors[1].v)).r; // -e1 at z1<=0
const selected1=normalize(add(z1,vectors[0].v)).r; // +e1 at z1>0
check(!eq(selected0,selected1),'absolute sign selector unexpectedly descended');
// For a labelled Markov kernel, +e1 probability depending on h is not quotient-lumpable.
const certificate={
 schema:'X6_UNIT183_RELATIVE_PRIMITIVE_TRACE_CHECK_V1',
 arithmetic:'exact signed integers, deterministic exhaustive finite cases',
 frozen_science_commit:'59538f585d037d09ef687b28715c4bc1a3f9fe03',
 model:'Z^6, +/-e_i, can6, h=min(z)',
 canonical_box:'min(a)=0, each a_i in {0,1,2}',box_states,
 observed_successor_pairs:edge_tests,depth_translation_tests,nonzero_depth_moves,
 trace_limit:4,initial_depths:[-2,3],traces_checked:paths_checked,trace_steps_checked,
 positive_diagonal_cycle:{length:6,relative_returns:true,native_common_depth_increment:h},
 absolute_sign_selector_counterexample:{z0,z1,from_same_relative_zero:true,successors_unequal:true},
 violations:0,
 scope:'Finite tests corroborate a separately written universal integer proof; no native R063 benchmark or original runtime executed',
 conclusion:'SOURCE_AUTHOR_EXACT_CHECKED_NOT_INDEPENDENTLY_REVIEWED'
};
console.log(JSON.stringify(certificate,null,2));
