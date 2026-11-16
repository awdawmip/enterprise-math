'use strict';
// R703 exact group-algebra/shuffle checker for two verified V38 based packet types.
// Run: node research_notes/portable_direct/R703_V39_TWO_PACKET_HOLO_COUNT_VERIFY.js
// Prints full verified JSON to stdout (redirect to a file if desired).
const assert = require('node:assert/strict');
const E=[0,1,2], A=[0,2,1], B=[1,0,2];
const compose=(next,prev)=>next.map(i=>prev[i]); // native V17/V37 slot tuple: A then B -> 201
const key=x=>x.join(''), unpack=s=>[...s].map(Number);
const parity=x=>{let n=0;for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)n+=(x[i]>x[j])?1:0;return n%2;};
const choose=(n,k)=>{let p=1n;for(let i=1;i<=k;i++)p=p*BigInt(n-i+1)/BigInt(i);return p;};
const expect=(a,b)=>(a===0||b===0)?1:(Math.min(a,b)===1?2:3);
const N=24, dp=Array.from({length:N+1},()=>Array.from({length:N+1},()=>new Map()));
dp[0][0].set(key(E),1n);
const rows=[]; let checks=0;
for(let total=0;total<=2*N;total++){
  for(let a=Math.max(0,total-N);a<=Math.min(N,total);a++){
    const b=total-a, m=dp[a][b], sum=[...m.values()].reduce((x,y)=>x+y,0n);
    assert.equal(sum,choose(total,a),'binomial count at '+a+','+b);
    assert.equal(m.size,expect(a,b),'S3 support at '+a+','+b);
    for(const h of m.keys())assert.equal(parity(unpack(h)),total%2,'parity');
    rows.push({a,b,counts:Object.fromEntries([...m].sort().map(([h,v])=>[h,v.toString()]))});
    checks++;
    if(a<N)for(const[h,v] of m){const g=key(compose(A,unpack(h)));dp[a+1][b].set(g,(dp[a+1][b].get(g)||0n)+v);}
    if(b<N)for(const[h,v] of m){const g=key(compose(B,unpack(h)));dp[a][b+1].set(g,(dp[a][b+1].get(g)||0n)+v);}
  }
}
const holo=word=>word.reduce((h,x)=>compose(x==='A'?A:B,h),E);
const witnesses={AABB:holo('AABB'),ABAB:holo('ABAB'),BABA:holo('BABA')};
assert.equal(new Set(Object.values(witnesses).map(key)).size,3);
assert.equal(dp[2][2].get(key(E)),4n);
for(const x of Object.values(witnesses))assert.equal(parity(x),0);
const result={research_unit:'R703',status:'R703_S3_TWO_PACKET_SUPPORT_EXACT_PASS',
  a_range:[0,N],b_range:[0,N],complete_count_pairs:checks,
  v38_generators:{A,B},v39_composition:'native V17/V37 slot-tuple (A then B -> 201)',
  support_theorem:'1 if a*b=0; 2 if min(a,b)=1 and a*b>0; 3 if min(a,b)>=2',
  zero_current_four_packet_witness_holonomies:witnesses,
  four_oriented_packet_histogram:{identity:16,cycle1:4,cycle2:4},
  complete_exact_shuffles:rows,
  source_blobs:{V29:'6849ebd3fc776fb7da3b46627376490aba3dad99',
    V38:'b627dd6265744669c438417bb19e896814a94be1',
    V39:'8151d0b6a4b65225b93d858bbc8a5d7037bf9cef'},
  proof_scope:'V38 based loop packets composed sequentially; intermediate scheduler not asserted.',
  original_scientific_task_pins:'unchanged'};
console.log(JSON.stringify(result,null,2));
