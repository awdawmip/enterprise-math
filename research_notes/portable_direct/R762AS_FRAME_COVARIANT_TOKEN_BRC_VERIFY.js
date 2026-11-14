#!/usr/bin/env node
'use strict';

// Exact finite checker for R762AS: three typed port labels; includes loops and empty history.
const verify = function verify() {
  const N=3, identity=[0,1,2], pairs=[];
  const assert=(cond,msg)=>{if(!cond)throw new Error(msg)};
  const eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
  for(let a=0;a<N;a++)for(let b=0;b<N;b++)pairs.push([a,b]);
  function* words(k,p=[]){if(k===0){yield p;return}for(const edge of pairs)yield* words(k-1,[...p,edge])}
  function* permute(v,p=[]){if(p.length===v.length){yield p;return}for(const x of v)if(!p.includes(x))yield* permute(v,[...p,x])}
  function mul(p,q){return q.map(i=>p[i])}
  function act(p,x){const v=Array(N).fill(0);for(let i=0;i<N;i++)v[p[i]]=x[i];return v}
  function R(word) {
    const d=Array(N).fill(0),h=Array(N).fill(0);
    for(const [a,b] of word){h[a]=Math.max(h[a],d[a]+1);d[a]++;d[b]--}
    return {d,h};
  }
  function star(A,B) {
    const dB=act(A.p,B.d),hB=act(A.p,B.h);
    return {d:A.d.map((v,i)=>v+dB[i]),h:A.h.map((v,i)=>Math.max(v,A.d[i]+hB[i])),p:mul(A.p,B.p)};
  }
  function order(p){let z=identity;for(let k=1;k<=6;k++){z=mul(z,p);if(eq(z,identity))return k}throw new Error("invalid perm")}
  function execute(word,starting) {
    const n=starting.slice();
    for(const [a,b] of word){if(n[a]<1)return null;n[a]--;n[b]++}
    return n;
  }
  const perms=[...permute(identity)];
  const stats={schema:"R762AS_FRAME_COVARIANT_TOKEN_BRC_EVIDENCE_V1",scope:"Three-typed-port conditional causal-token BRC with frame-to-port permutation bridge; not P000 physical triadic closure",word_length_max:3,word_alphabet_size:9,words_including_empty:0,permutations_checked:perms.length,macro_pairs_checked:0,replay_prefixes_checked:0,sharp_single_port_failure_checks:0,orbit_balance_checks:0,periodic_cases:0,unbalanced_cases:0,all_assertions_passed:false};
  for(let length=0;length<=3;length++) {
    for(const word of words(length)){stats.words_including_empty++;
      for(const p of perms){
        stats.macro_pairs_checked++;
        const r0=R(word),macro={...r0,p},q=order(p);
        let aggregate={d:Array(N).fill(0),h:Array(N).fill(0),p:identity},expanded=[],frame=identity,afterQ=null;
        for(let r=1;r<=8;r++){
          aggregate=star(aggregate,macro);
          for(const [a,b] of word)expanded.push([frame[a],frame[b]]);
          frame=mul(frame,p);
          const direct=R(expanded);
          assert(eq(aggregate,{...direct,p:frame}),"residual mismatch "+JSON.stringify({word,p,r,aggregate,direct,frame}));
          const final=execute(expanded,direct.h);
          assert(final!==null&&eq(final,direct.h.map((x,i)=>x-direct.d[i])),"sharp seed failed");
          for(let v=0;v<N;v++){if(direct.h[v]){const poor=direct.h.slice();poor[v]--;assert(execute(expanded,poor)===null,"minimality failed");stats.sharp_single_port_failure_checks++}}
          if(r===q)afterQ=aggregate;
          stats.replay_prefixes_checked++;
        }
        let orb=Array(N).fill(0),visited=new Set();
        for(let i=0;i<N;i++)if(!visited.has(i)){
          let cycle=[],j=i;
          do{cycle.push(j);visited.add(j);j=p[j]}while(j!==i);
          let balance=cycle.reduce((s,k)=>s+r0.d[k],0);
          for(const k of cycle)orb[k]=balance;
        }
        const periodBalanced=orb.every(v=>v===0);
        assert(periodBalanced===afterQ.d.every(v=>v===0),"orbit condition error");
        const twice=star(afterQ,afterQ);
        if(periodBalanced){
          assert(eq(twice.h,afterQ.h)&&twice.d.every(v=>v===0),"periodic seed error");
          stats.periodic_cases++;
        }else{
          assert(twice.h.some((v,i)=>v>afterQ.h[i]),"unbalanced growth missing");
          stats.unbalanced_cases++;
        }
        stats.orbit_balance_checks++;
      }
    }
  }
  const cycle=[[0,1],[1,2],[2,0]],extra=[...cycle,[0,1]],swap=[1,0,2],trip=R(extra),two=star({...trip,p:swap},{...trip,p:swap}),baseline=R(cycle);
  assert(eq(trip,{d:[1,-1,0],h:[1,0,0]}),"example residual error");
  assert(eq(two,{d:[0,0,0],h:[1,0,0],p:identity}),"two-period example failed");
  assert(eq(baseline,{d:[0,0,0],h:[1,0,0]}),"cycle witness failed");
  stats.examples={triadic_cycle_sequential_seed:baseline.h,triadic_cycle_atomic_reserve_seed:[1,1,1],triadic_plus_pass_word:extra,slot_transposition:swap,macro_delta:trip.d,macro_H:trip.h,two_macro_delta:two.d,two_macro_H:two.h,two_macro_frame:two.p,minimum_stock_for_all_repetitions:1,minimum_stock_without_frame_permutation_for_r_repetitions:"r"};
  stats.all_assertions_passed=true;
  return stats;
};
const result = verify();
process.stdout.write(JSON.stringify(result,null,2)+'\n');
