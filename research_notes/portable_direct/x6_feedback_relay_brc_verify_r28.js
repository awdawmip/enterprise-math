#!/usr/bin/env node
// X6 R28 finite Boolean-BRC exact successful-word-language verifier.
// No packages required. A labelled event word is represented by a recursively interned trie.
"use strict";
function verify(k,t,q) {
  if (!(k>=2 && t>=1 && q>=0)) throw Error("Bad parameters");
  const m=k+t, triggerMask=(1<<k)-1, numHistories=1<<m, maxH=2*k+q+5;
  const intern=new Map([["",0]]);
  const memo=new Map();
  let nextSignature=1;
  function sig(theta,phase,returned,triggerUsed,relayDone,probeUsed,h) {
    if (h===0) return 0;
    const key=[theta,phase,returned,triggerUsed,relayDone,probeUsed,h].join(",");
    if (memo.has(key)) return memo.get(key);
    const actions=[];
    for(let i=0;i<m;i++) {
      const b=1<<i;
      if(!(phase&b)) actions.push(["B"+i+"+",sig(theta,phase|b,returned,triggerUsed,relayDone,probeUsed,h-1)]);
      else actions.push(["B"+i+"-",sig(theta,phase&~b,returned|b,triggerUsed,relayDone,probeUsed,h-1)]);
    }
    if(!triggerUsed && (theta&triggerMask)===triggerMask && (returned&triggerMask)===triggerMask)
      actions.push(["A+",sig(theta,phase,returned,1,relayDone,probeUsed,h-1)]);
    if(triggerUsed && relayDone<q)
      actions.push(["R"+(relayDone+1)+"+",sig(theta,phase,returned,triggerUsed,relayDone+1,probeUsed,h-1)]);
    if(triggerUsed && relayDone===q)
      for(let j=k;j<m;j++) {
        if((theta&(1<<j)) && (returned&(1<<j)) && !(probeUsed&(1<<(j-k))))
          actions.push(["D"+j+"+",sig(theta,phase,returned,triggerUsed,relayDone,probeUsed|(1<<(j-k)),h-1)]);
      }
    const serialized=JSON.stringify(actions);
    if(!intern.has(serialized)) intern.set(serialized,nextSignature++);
    const ans=intern.get(serialized);
    memo.set(key,ans);
    return ans;
  }
  const counts=[];
  let checkedPairs=0;
  for(let h=0;h<=maxH;h++) {
    const forward=new Map(), reverse=new Map();
    for(let theta=0;theta<numHistories;theta++) {
      const isTrigger=(theta&triggerMask)===triggerMask;
      const predicted=h<=2*k ? "all" :
          h<2*k+q+4 ? (isTrigger?"on":"off") :
          (isTrigger?"on"+(theta>>k):"off");
      const signature=sig(theta,0,0,0,0,0,h);
      if(forward.has(signature) && forward.get(signature)!==predicted)
        throw Error("Missing distinction: "+[k,t,q,h,theta].join(","));
      if(reverse.has(predicted) && reverse.get(predicted)!==signature)
        throw Error("False distinction: "+[k,t,q,h,theta].join(","));
      forward.set(signature,predicted);
      reverse.set(predicted,signature);
    }
    const predictedCount=h<=2*k?1:h<2*k+q+4?2:1+(1<<t);
    if(forward.size!==predictedCount) throw Error("Wrong quotient count");
    counts.push(forward.size);
    checkedPairs+=numHistories*(numHistories-1)/2;
  }
  return {k,t,q,m,first_trigger:2*k+1,first_probe:2*k+q+4,
    histories:numHistories,horizon:maxH,class_counts_h0_to_maxH:counts,
    history_pair_horizon_comparisons:checkedPairs,
    recursively_memoized_states:memo.size,interned_signatures:intern.size,
    result:"PASS"};
}
const cases=[[2,1,0],[2,1,1],[2,1,2],[2,1,3],[2,2,0],[2,2,2],[3,1,0],[3,1,2]];
const runs=cases.map(c=>verify(...c));
const summary={schema:"ENTERPRISE_X6_R28_FEEDBACK_RELAY_EXACT_TEST_V1",
  model:"CONDITIONAL_SIGNED_PORT_FEEDBACK_CONTROLLER_NOT_NATIVE_ADMISSION",
  cases:runs,exact_tests_passed:runs.length,
  total_pair_horizon_comparisons:runs.reduce((a,r)=>a+r.history_pair_horizon_comparisons,0),
  total_recursively_memoized_states:runs.reduce((a,r)=>a+r.recursively_memoized_states,0),
  result:"PASS"};
if(require.main===module) console.log(JSON.stringify(summary,null,2));
module.exports={verify,summary};
