// X6 R37: exact trace-language certificates for partial deterministic and
// nondeterministic finite labelled systems. Node.js 18+, no dependencies.
// Rows are bitsets of successor states. A word succeeds if at least one branch
// survives all letters; events Q0/Q1 remain distinct named labels.
'use strict';
const ALPHABET = ['Q0', 'Q1'];
function machines(n, deterministic) {
  const base = deterministic ? n + 1 : (1 << n);
  const total = base ** (2*n), result=[];
  for (let code=0; code<total; code++) {
    let x=code, rows=[];
    for (let s=0;s<n;s++) {
      const row=[];
      for (let a=0;a<2;a++) {
        const v=x%base; x=Math.floor(x/base);
        row.push(deterministic ? (v === 0 ? 0 : (1 << (v-1))) : v);
      }
      rows.push(row);
    }
    result.push({n,rows});
  }
  return result;
}
function step(rows,mask,a) {
  let out=0;
  for(let i=0;i<rows.length;i++) if(mask & (1<<i)) out|=rows[i][a];
  return out;
}
function exactSignatures(m,depth) {
  const layers=[], masks=1<<m.n;
  layers.push(Array.from({length:masks},(_,s)=>s ? 'A' : 'D'));
  for(let h=1;h<=depth;h++) {
    const prev=layers[h-1];
    layers.push(Array.from({length:masks},(_,s)=>
      s ? JSON.stringify(['A',prev[step(m.rows,s,0)],prev[step(m.rows,s,1)]]) : 'D'));
  }
  return layers;
}
function shortest(m,p,n,q) {
  const initial=[1<<p,1<<q,[]], queue=[initial], seen=new Set([initial[0]+','+initial[1]]);
  for(let cursor=0;cursor<queue.length;cursor++) {
    const [x,y,w]=queue[cursor];
    for(let a=0;a<2;a++) {
      const xx=step(m.rows,x,a), yy=step(n.rows,y,a);
      if((xx===0)!==(yy===0)) return w.concat(a);
      if(xx && yy) {
        const key=xx+','+yy;
        if(!seen.has(key)) {seen.add(key);queue.push([xx,yy,w.concat(a)]);}
      }
    }
  }
  return null;
}
function verifyFamily(n,deterministic) {
  const models=deterministic?[...machines(1,true),...machines(2,true)]:machines(n,false);
  const maxDepth=deterministic?3:(2**n+2**n-3);
  const signatures=models.map(m=>exactSignatures(m,maxDepth));
  let comparisons=0, distribution={equivalent:0}, max=0, witness=null;
  for(let i=0;i<models.length;i++)for(let j=0;j<models.length;j++) {
    const a=models[i], b=models[j], bound=deterministic?a.n+b.n-1:(2**a.n+2**b.n-3);
    for(let p=0;p<a.n;p++)for(let q=0;q<b.n;q++) {
      comparisons++;
      const w=shortest(a,p,b,q), len=w===null?null:w.length;
      const equal=signatures[i][bound][1<<p]===signatures[j][bound][1<<q];
      if(equal!==(w===null))throw Error('wrong full-future cutoff');
      if(w!==null) {
        if(len>bound)throw Error('cutoff violated');
        for(let h=0;h<len;h++)if(signatures[i][h][1<<p]!==signatures[j][h][1<<q])throw Error('non-shortest witness');
        if(signatures[i][len][1<<p]===signatures[j][len][1<<q])throw Error('witness not distinguished');
        distribution[len]=(distribution[len]||0)+1;
        if(len>max) {max=len;witness={left:a.rows,left_state:p,right:b.rows,right_state:q,word:w.map(t=>ALPHABET[t])};}
      }else distribution.equivalent++;
    }
  }
  return {automata:models.length,compared_initial_pairs:comparisons,
    distribution,maximum_witness_depth:max,maximal_witness:witness};
}
function main() {
  const det=verifyFamily(2,true), nfa=verifyFamily(2,false);
  const expectedD={equivalent:3384,1:19128,2:4884,3:160};
  const expectedN={equivalent:54224,1:159744,2:45328,3:2624,4:224};
  function assertEqual(x,y,label){if(JSON.stringify(x)!==JSON.stringify(y))throw Error(label+' mismatch');}
  assertEqual([det.automata,det.compared_initial_pairs,det.maximum_witness_depth],[85,27556,3],'DFA totals');
  assertEqual(det.distribution,expectedD,'DFA histogram');
  assertEqual([nfa.automata,nfa.compared_initial_pairs,nfa.maximum_witness_depth],[256,262144,4],'NFA totals');
  assertEqual(nfa.distribution,expectedN,'NFA histogram');
  if(nfa.maximal_witness.word.join(',')!=='Q0,Q1,Q0,Q1')throw Error('missing length-four witness');
  return {
    schema:'X6_R37_LINEAR_AND_SUBSET_FUTURE_CERTIFICATE_V1',
    frozen_science:'P000 V5 @ a72226e2430ffa4786321ac86e7f0c599d5f0389',
    language_observer:'Boolean support of source/Port-named successful event words Q0,Q1; no independent state readout',
    deterministic_cutoff:'nA+nB-1',
    nondeterministic_cutoff:'reachable_nonempty_subsets_A + reachable_nonempty_subsets_B - 1; <= 2^nA + 2^nB - 3',
    deterministic_exhaustive_one_two_state:det,
    nondeterministic_exhaustive_two_state:nfa,
    checks:{all_small_DFA_pairs:true,all_two_state_NFA_pairs:true,all_shorter_horizons_agree_before_shortest_witness:true},
    reviewed:'NOT_INDEPENDENTLY_REVIEWED',pass:true
  };
}
if(require.main===module)console.log(JSON.stringify(main(),null,2));
module.exports={main,step,shortest,exactSignatures};
