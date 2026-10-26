"use strict";
/* EC45: exact positive-integer source counts. Run: node EC45_verify.js.
   This is an auxiliary BRC observer model, not a native X6 update. */
function* words(base, length, prefix=[]) {
  if(prefix.length===length){yield prefix;return;}
  for(let i=0;i<base;i++) yield* words(base,length,[...prefix,i]);
}
function score(encoded, actions, nextMem, terminal) {
  const P=[8,1,4], Q=[1,8,4], Py=[3,1], Qy=[1,3];
  let errorNumerator=0, continuedSourceCount=0;
  for(let h=0;h<3;h++){
    const m=encoded[h], a=actions[m];
    if(a===0) errorNumerator+=4*Q[h];        // stage 2 declare P
    else if(a===1) errorNumerator+=4*P[h];   // stage 2 declare Q
    else {
      continuedSourceCount+=P[h]+Q[h];
      const dest=nextMem[m];
      for(let y=0;y<2;y++){
        const verdict=terminal[2*dest+y];   // 0=P, 1=Q
        errorNumerator+=verdict===0?Q[h]*Qy[y]:P[h]*Py[y];
      }
    }
  }
  // Error sum=errorNumerator/52; depths sum=4+continuedSourceCount/13.
  // Thus J=eP+eQ+(tP+tQ)/8=(52+2*errorNumerator+continuedSourceCount)/104.
  return 52+2*errorNumerator+continuedSourceCount;
}
function enumerate(k) {
  let count=0, best=Infinity, witness=null;
  for(const encoded of words(k,3))
    for(const actions of words(3,k))
      for(const nextMem of words(k,k))
        for(const terminal of words(2,2*k)) {
          count++;
          const n=score(encoded,actions,nextMem,terminal);
          if(n<best){best=n;witness={encoded,actions,nextMem,terminal};}
        }
  return {memory_states:k,deterministic_policies_checked:count,best_cost_numerator_over_104:best,witness};
}
function run(){
  const k1=enumerate(1), k2=enumerate(2);
  const k3={encoded:[0,1,2],actions:[0,1,2],nextMem:[0,1,2],terminal:[0,0,1,1,0,1]};
  const n3=score(k3.encoded,k3.actions,k3.nextMem,k3.terminal);
  if(k1.best_cost_numerator_over_104!==130 || k2.best_cost_numerator_over_104!==100 || n3!==92)
    throw Error("exact score mismatch");
  return {schema:"EC45_EXACT_INTEGER_SOURCE_CHECK_V1",
    source_counts_P:[8,1,4],source_counts_Q:[1,8,4],
    terminal_source_counts_P:[3,1],terminal_source_counts_Q:[1,3],
    stage1:"mandatory continue; root observed",
    stage2:"root forgotten; common x; optional stop-P, stop-Q, continue",
    stage3:"visible y; terminal P/Q",
    cost:"e_P + e_Q + (t_P+t_Q)/8",
    arithmetic:"exact positive integers, objective scaled by 104",
    k1,k2,k3_witness:k3,k3_witness_cost_numerator_over_104:n3,
    k3_proved_lower_bound_numerator_over_104:92,
    result:"PASS",
    limitations:"finite auxiliary positive-source BRC model; no native X6 or formal Guard"};
}
if(typeof module!=="undefined" && typeof require!=="undefined" && require.main===module)
  console.log(JSON.stringify(run(),null,2));
if(typeof module!=="undefined") module.exports={run,score};
