/* R749STZ exact finite-scope resource rollback certificate; no dependencies.
 * Run: node R749STZ_RESOURCE_ROLLBACK_CERT.js
 * General theorem is established by the mathematical proof, not this finite test.
 */
"use strict";
function verify() {
  const alphabet="ABCDE", weights=[1,1,2,3,6];
  const machines={
    RESET_FLIP:{A:[0,0],B:[1,0],C:[0,0],D:[0,1],E:[0,1]},
    BIJECTIVE:{A:[1,0],B:[0,1],C:[1,0],D:[0,1],E:[1,0]}
  };
  const result={status:"PASS",frozen_weight_vector:weights,
    domain:"all five-source words of length 0..7; POP budget 0..min(3,length)",
    machines:{},witness:{}};
  for(const name of Object.keys(machines)) {
    const transitions=machines[name], step=(q,c)=>transitions[c][q];
    const groups=new Map(), reachCache=new Map();
    function reachable(n) {
      const key=n.join(",");
      if(reachCache.has(key)) return reachCache.get(key);
      let out=new Set();
      if(n.every(v=>v===0)) out.add(0);
      else for(let i=0;i<5;i++) if(n[i]>0) {
        const old=n.slice(); old[i]--;
        for(const q of reachable(old)) out.add(step(q,alphabet[i]));
      }
      reachCache.set(key,out); return out;
    }
    function suffixes(n,r) {
      const out=[];
      function rec(avail,prefix) {
        if(prefix.length===r){out.push(prefix);return;}
        for(let i=0;i<5;i++) if(avail[i]>0) {
          avail[i]--;rec(avail,prefix+alphabet[i]);avail[i]++;
        }
      }
      rec(n.slice(),""); return out;
    }
    let wordInstances=0;
    function generate(target,word,states) {
      if(word.length===target){
        const n=[0,0,0,0,0];
        for(const c of word)n[alphabet.indexOf(c)]++;
        const q=states[states.length-1];
        const key=n.join(",")+"|"+q;
        if(!groups.has(key))groups.set(key,{n,q,history:[]});
        groups.get(key).history.push([word,states]);
        wordInstances++;return;
      }
      for(const c of alphabet)
        generate(target,word+c,states.concat([step(states[states.length-1],c)]));
    }
    for(let ell=0;ell<=7;ell++)generate(ell,"",[0]);
    let cases=0,classifiedInstances=0,extraBoundaryCases=0,totalClasses=0;
    for(const group of groups.values()) {
      const {n,q,history}=group, ell=n.reduce((x,y)=>x+y,0);
      for(let r=0;r<=Math.min(3,ell);r++) {
        const observed=new Set(),bySuffix=new Map();
        for(const [word,states] of history) {
          const u=word.slice(ell-r), b=states[ell-r];
          observed.add(JSON.stringify([u,b]));
          if(!bySuffix.has(u))bySuffix.set(u,new Set());
          bySuffix.get(u).add(b);
        }
        const predicted=new Set();
        for(const u of suffixes(n,r)) {
          const remaining=n.slice();
          for(const c of u)remaining[alphabet.indexOf(c)]--;
          for(const b of reachable(remaining)){
            let z=b;
            for(const c of u)z=step(z,c);
            if(z===q)predicted.add(JSON.stringify([u,b]));
          }
        }
        if(predicted.size!==observed.size||[...predicted].some(x=>!observed.has(x)))
          throw Error("COUNT_MISMATCH "+JSON.stringify({name,n,q,r}));
        const noExtra=[...bySuffix.values()].every(x=>x.size===1);
        const condition=suffixes(n,r).every(u=>{
          const remaining=n.slice();
          for(const c of u)remaining[alphabet.indexOf(c)]--;
          let hits=0;
          for(const b of reachable(remaining)){
            let z=b;
            for(const c of u)z=step(z,c);
            if(z===q)hits++;
          }
          return hits<=1;
        });
        if(noExtra!==condition)throw Error("INJECTIVITY_FAIL "+JSON.stringify({name,n,q,r}));
        if(name==="BIJECTIVE"&&!noExtra)throw Error("BIJECTIVE_COUNTEREXAMPLE");
        if(!noExtra)extraBoundaryCases++;
        cases++;classifiedInstances+=history.length;totalClasses+=predicted.size;
      }
    }
    result.machines[name]={word_instances:wordInstances,
      endpoint_inventory_fibers:groups.size,
      exact_class_count_cases:cases,
      classified_history_instances:classifiedInstances,
      total_predicted_classes_across_cases:totalClasses,
      exact_injectivity_criterion_checks:cases,
      fibers_with_extra_resource_boundary:extraBoundaryCases};
  }
  function states(word) {
    const trans=machines.RESET_FLIP, out=[0];
    for(const c of word)out.push(trans[c][out[out.length-1]]);
    return out;
  }
  const w1=states("ABC"),w2=states("BAC");
  if(JSON.stringify(w1)!=="[0,0,1,0]"||JSON.stringify(w2)!=="[0,1,0,0]")
    throw Error("EXACT_WITNESS_FAILED");
  const words=["ABC","ACB","BAC","BCA","CAB","CBA"];
  const fibers=new Map();
  for(const word of words){
    const qstates=states(word), q=qstates[3];
    if(!fibers.has(q))fibers.set(q,new Set());
    fibers.get(q).add(JSON.stringify([word[2],qstates[2]]));
  }
  if(fibers.get(0).size!==4||fibers.get(1).size!==1)
    throw Error("FIBER_WITNESS_COUNT_FAILED");
  result.witness={
    word_pair:["ABC","BAC"],inventory:[1,1,1,0,0],
    common_terminal_resource:0, common_suffix_with_one_POP:"C",
    ledger_traces:[w1,w2],after_one_POP_resource:[w1[2],w2[2]],
    terminal_resource_0_number_of_minimal_classes:4,
    terminal_resource_0_number_of_suffixes:2,
    optimal_extra_bits:1
  };
  return result;
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)
  console.log(JSON.stringify(verify(),null,2));
