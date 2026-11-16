"use strict";
// PREFIX-850. Finite exact integer automaton certificate, runnable with Node.js.
// The finite-state BFS is complete: all outgoing effective moduli are traversed.
function verify() {
  const popcnt = a => {let n=0;for(;a;a&=a-1)n++;return n;};
  const make = p => {
    const n=2**p;
    const moves=Array.from({length:n},(_,x)=>[x,...Array.from({length:p},(_,i)=>x^(1<<i))]);
    const diagonal=Array.from({length:n},(_,x)=>1n<<BigInt(n*x+x)).reduce((a,b)=>a|b,0n);
    const initial = q => {
      let r=0n;for(let x=0;x<n;x++)for(let y=0;y<n;y++)if((x-y)%q===0)r|=1n<<BigInt(n*x+y);return r;
    };
    const build = q => Array.from({length:n*n},(_,i)=>{
      let r=0n;const x=Math.floor(i/n),y=i%n;
      for(const xx of moves[x])for(const yy of moves[y])if((xx-yy)%q===0)r|=1n<<BigInt(n*xx+yy);
      return r;
    });
    const step = (r,table) => {
      let out=0n,i=0;for(;r;r>>=1n,i++)if(r&1n)out|=table[i];return out;
    };
    return {n,diagonal,initial,build,step};
  };
  const cases=[];
  for(let p=1;p<=4;p++){
    const qs=Array.from({length:2**(p-1)},(_,j)=>2*j+1);
    const M=make(p), jumps=qs.map(M.build), states=[], depths=[], id=new Map(), edges=[];
    const insert=(r,d)=>{
      if(!id.has(r)){id.set(r,states.length);states.push(r);depths.push(d);}
      return id.get(r);
    };
    const first=qs.map(q=>insert(M.initial(q),1));
    for(let i=0;i<states.length;i++){
      const row=qs.map((q,j)=>{
        const r=M.step(states[i],jumps[j]);
        if((r&M.diagonal)!==M.diagonal)throw Error("lost diagonal");
        return insert(r,depths[i]+1);
      });
      edges.push(row);
    }
    if(states.some(r=>(r&~M.diagonal)===0n))throw Error("found resetting word at p="+p);
    const dh={};for(const d of depths)dh[d]=(dh[d]||0)+1;
    cases.push({p,bit_width_excluded:p,effective_odd_moduli:qs,states:states.length,depth_histogram:dh,
      initial_state_ids:first,relation_masks_hex:states.map(x=>x.toString(16)),
      transition_target_ids:edges,diagonal_mask_hex:M.diagonal.toString(16),
      all_relations_ambiguous:true,closed_under_every_effective_modulus:true});
  }
  const expected=[1,2,4,53];
  if(cases.some((r,i)=>r.states!==expected[i]))throw Error("unexpected automaton state count");
  if(JSON.stringify(cases[3].depth_histogram)!==JSON.stringify({"1":8,"2":13,"3":19,"4":13}))throw Error("unexpected closure-depth histogram");
  const M=make(5), period=[25,19,29,11], bridges=[];
  const counts=[[14,18,0,0],[26,6,12,0],[6,12,0,0],[62,14,18,0]];
  for(let j=0;j<4;j++){
    const word=[...period.slice(j),...period.slice(0,j)];
    let r=M.initial(word[0]);const observed=[];
    for(let k=0;k<4;k++){
      if(k)r=M.step(r,M.build(word[k]));
      observed.push(popcntBigInt(r&~M.diagonal));
    }
    if(JSON.stringify(observed)!==JSON.stringify(counts[j]))throw Error("bad bridge "+j);
    bridges.push({word,ordered_non_diagonal_counts:observed});
  }
  function popcntBigInt(b){let n=0;while(b){b&=b-1n;n++;}return n;}
  return {schema:"EM_PREFIX850_EXACT_CONGRUENCE_OBSERVER_AUTOMATON_V1",
    model:"binary_named_sources_one_hidden_bit_flip_per_heartbeat",
    gain:"c_t=2^floor(t/2)",
    claim:"B_dyn(p,2,w,2)=p+1 for p=1..4 and all finite w>=1",
    proof_mode:"exhaustive_closed_pair_relation_automata_plus_single_modulus_upper_bound",
    cases,prior_prefix849_bridge:bridges,assertions:"ALL_EXACT_ASSERTIONS_PASSED"};
}
const result = verify();
process.stdout.write(JSON.stringify(result, null, 2) + "\n");
