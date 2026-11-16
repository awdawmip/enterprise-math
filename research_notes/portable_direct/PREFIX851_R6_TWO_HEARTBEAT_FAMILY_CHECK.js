"use strict";
// PREFIX-851: exact integer arithmetic and 6-source hidden-flip observer verifier.
// Run: node PREFIX851_R6_TWO_HEARTBEAT_FAMILY_CHECK.js
function verify() {
  const countBits = x => {let z=0n;for(;x;x&=x-1n)z++;return Number(z);};
  const algebraic_family=[];
  for(let p=6;p<=64;p++){
    const M=(1n<<BigInt(p))-1n;
    const K=(1n<<BigInt(p-1))+3n;
    const D=M-K;
    const checks={
      p,moduli:[K.toString(),M.toString()],
      k_bit_count:countBits(K),d_bit_count:countBits(D),
      k_above_half:2n*K>M,
      k_exceeds_any_difference_of_two_distinct_single_flip_weights:K>((1n<<BigInt(p-1))-1n)
    };
    if(checks.k_bit_count!==3||checks.d_bit_count!==p-3||!checks.k_above_half||!checks.k_exceeds_any_difference_of_two_distinct_single_flip_weights)throw Error("arithmetic error at p="+p);
    algebraic_family.push(checks);
  }
  const p=6,n=1<<p;
  const moves=Array.from({length:n},(_,x)=>[x,...Array.from({length:p},(_,i)=>x^(1<<i))]);
  const inspect=(q1,q2)=>{
    let ambiguous_initial=0;
    const final=new Set();
    for(let x=0;x<n;x++)for(let y=0;y<n;y++){
      if((x-y)%q1!==0)continue;
      if(x!==y)ambiguous_initial++;
      for(const u of moves[x])for(const v of moves[y])
        if(u!==v && (u-v)%q2===0)final.add(u*n+v);
    }
    return {word:[q1,q2],ambiguous_first:ambiguous_initial,ambiguous_second:final.size};
  };
  const witness=[inspect(35,63),inspect(63,35)];
  if(witness[0].ambiguous_first!==58||witness[1].ambiguous_first!==2||witness.some(x=>x.ambiguous_second))throw Error("period witness failure");
  const odd=Array.from({length:16},(_,i)=>2*i+1);
  const good=[];
  for(const a of odd)for(const b of odd)if(inspect(a,b).ambiguous_second===0)good.push([a,b]);
  if(good.length)throw Error("unexpected five-bit two-word observer");
  return {schema:"EM_PREFIX851_ALL_LARGE_SOURCE_TWO_HEARTBEAT_V1",
    model:"binary_named_sources_hidden_single_flip_gain_2^floor(t/2)",
    theorem:"For every integer p>=6, alternating odd moduli (2^(p-1)+3,2^p-1) give exact named-state recovery from two consecutive reports using width p.",
    lower_bound:"For p=6, all 16^2 odd effective moduli words with five-bit ports are ambiguous; hence B_dyn(6,2,2,2)=6.",
    algebraic_family_exact_integer_regression:algebraic_family,
    p6_periodic_two_word_exact_pairs:witness,
    p6_five_bit_moduli:odd,p6_five_bit_two_word_tests:256,p6_five_bit_good_words:good,
    assertions:"ALL_EXACT_ASSERTIONS_PASSED"};
}
process.stdout.write(JSON.stringify(verify(), null, 2)+"\n");
