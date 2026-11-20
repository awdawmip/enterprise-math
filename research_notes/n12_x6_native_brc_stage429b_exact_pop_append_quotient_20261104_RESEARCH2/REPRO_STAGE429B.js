#!/usr/bin/env node
'use strict';
// Complete 12-native-direction exact future observer; proof Stage429-B.
const verifyStage429B=function verifyStage429B() {
  const D = 12, letters = [0,1,2];
  function words(n) {
    let arr=[[]]; for(let k=0;k<n;k++){const b=[];for(const a of arr)for(const s of letters)b.push([...a,s]);arr=b;}return arr;
  }
  function ep(w) {
    const a=Array(6).fill(0);for(const d of w)a[Math.floor(d/2)]+=(d%2===0?1:-1);return a.join(",");
  }
  function directed(w) {
    const h=new Map();for(let i=1;i<w.length;i++){const key=w[i-1]*D+w[i];h.set(key,(h.get(key)||0)+1);}
    return [...h].sort((a,b)=>a[0]-b[0]).map(([k,c])=>k+":"+c).join(",");
  }
  function K(p,q) {let v=0;for(let i=0;i<Math.min(p.length,q.length);i++)v+=+(p[i]===q[i]);return v;}
  function base(p,q) {
    return [p.length,q.length,ep(p),ep(q),directed(p),directed(q),K(p,q)].join("|");
  }
  function qSnap(p,q) {return [q.length,ep(q),directed(q),K(p,q)].join("|");}
  function sig(p,q) {
    const out=[qSnap(p,q)];
    const pop=q.slice(0,-1);
    out.push(qSnap(p,pop));
    for(let x=0;x<D;x++)out.push(qSnap(p,[...q,x]));
    for(let x=0;x<D;x++)out.push(qSnap(p,[...pop,x]));
    for(let x=0;x<D;x++)out.push(qSnap(p,q)); // APPEND(x), then POP, restores q
    return out.join(";");
  }
  const cases=[]; let histories=0, fibers=0, nontrivialFibers=0, observedClasses=0, signatures=0;
  for (let n=2;n<=3;n++)for (let m=n+3;m<=6;m++) {
    const pf=words(m),qf=words(n),groups=new Map();let batch=0;
    for(const p of pf)for(const q of qf){
      batch++;histories++;
      const b=base(p,q);
      let g=groups.get(b);
      if(!g){g={keys:new Map(),sigs:new Map(),count:0};groups.set(b,g);}
      const key=[q[n-2],q[n-1],p[n-1],p[n]].join(",");
      const future=sig(p,q);
      g.count++;
      const priorSig=g.keys.get(key),priorKey=g.sigs.get(future);
      if(priorSig!==undefined && priorSig!==future) throw Error("Sufficiency failed at n="+n+",m="+m);
      if(priorKey!==undefined && priorKey!==key) throw Error("Necessity failed at n="+n+",m="+m);
      g.keys.set(key,future);g.sigs.set(future,key);
    }
    let nontriv=0,cl=0;
    for(const g of groups.values()){if(g.count>1)nontriv++;cl+=g.keys.size;}
    fibers+=groups.size;nontrivialFibers+=nontriv;observedClasses+=cl;
    cases.push({n,m,p_words:pf.length,q_words:qf.length,histories:batch,observer_fibers:groups.size,nontrivial_fibers:nontriv,future_classes:cl});
  }
  const q=Array(5).fill(2), witness=[];
  let initial=null, futures=new Set();
  for(const j of [3,4,5,6]){
    const p=Array(12).fill(0);p[j-1]=1;p[j]=1;
    const b=base(p,q);
    if(initial===null)initial=b;
    if(initial!==b)throw Error("4-way full observer not equal");
    const kAtN=K(p,[...q.slice(0,-1),0]);
    const kAtN1=K(p,[...q,0]);
    const row={B_block_start_1_based:j,P_at_5:p[4],P_at_6:p[5],K_after_POP_APPEND_A:kAtN,K_after_APPEND_A:kAtN1};
    witness.push(row);
    futures.add(kAtN+","+kAtN1);
  }
  if(futures.size!==4)throw Error("4-way distinguishability failed");
  return {
    marker:"STAGE429B_EXACT_TWO_OPERATION_QUOTIENT_PASS",
    native_alphabet:"12 signed X6 directions, integer endpoints, full typed directed J, absolute positional K",
    scoped_language:"P frozen; Q one independent POP and one independent APPEND in either order; Q length >=2; |P|-|Q|>=3",
    frozen_science:{global:"bf84bd7c61a2444b59b1da96be57df0e9ae47e53",em:"2af3fc484eb11060b69e0afc1b562bcaf5ad1419",p000_blob:"bcc2590d3168a28f72e8b9f0f9b1f76faadcd488"},
    checker:"exhaustive all P,Q over 3-symbol subset embedded into native 12, all 12 APPEND probes, both orderings",
    histories_checked:histories,initial_observer_fibers:fibers,nontrivial_observer_fibers:nontrivialFibers,future_quotient_classes:observedClasses,
    continuations_per_history:38,
    batches:cases,
    four_way_full_observer_fiber:{P_length:12,Q_length:5,Q_word:"CCCCC",P_word_family:"A^(j-1) B B A^(11-j), j in {3,4,5,6}",four_distinct_future_K_signatures:witness},
    theorem_scope:"infinite/all-words exact algebraic proof; computed tests finite and independent",
    authority:"AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED"
  };
};
if (require.main===module) console.log(JSON.stringify(verifyStage429B(),null,2));
module.exports={verifyStage429B};
