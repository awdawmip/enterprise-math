"use strict";
// R618: exact auxiliary signed BRC source-code and permutation-fiber checks.
const BASE = 12n;
function assert(v, msg) { if (!v) throw new Error(msg); }
function choose(n,k) {
  if(k<0 || k>n) return 0n; k=Math.min(k,n-k);
  let r=1n; for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j); return r;
}
function encode(word) {
  let z=1n; for(const i of word){ assert(Number.isInteger(i)&&i>=1&&i<=12,"branch"); z=12n*z+BigInt(i-1); } return z;
}
function decode(input) {
  assert(typeof input==="bigint"&&input>=1n,"positive integer tag"); let z=input,w=[];
  while(z>1n){ assert(z>=12n,"invalid tag"); w.push(Number(z%12n)+1); z/=12n; }
  return w.reverse();
}
function joinTag(left,right) { return 12n**BigInt(right.length)*(encode(left)-1n)+encode(right); }
function add(a,b) {let v=Array(Math.max(a.length,b.length)).fill(0n); a.forEach((x,j)=>v[j]+=x);b.forEach((x,j)=>v[j]+=x);return v;}
function mul(a,b) {let v=Array(a.length+b.length-1).fill(0n);a.forEach((x,j)=>b.forEach((y,k)=>v[j+k]+=x*y));return v;}
function eq(a,b) {let n=Math.max(a.length,b.length);for(let j=0;j<n;j++)if((a[j]||0n)!==(b[j]||0n))return false;return true;}
function kernel(i) {
  const d=[-choose(4,i)+choose(2,i-1),choose(5,i-1)-choose(5,i-2),choose(7,i-2),-choose(9,i-3)];
  let z=[0n];
  for(let j=1;j<=4;j++){let power=i+1-j;if(power<0||d[j-1]===0n)continue;
    let part=Array(i-1).fill(0n);for(let k=0;k<=power;k++)part.push(-d[j-1]*choose(power,k));
    z=add(z,part);
  }return z;
}
function endpoint(word) {
  const z=[0,0,0,0,0,0];
  for(const i of word)z[Math.floor((i-1)/2)]+=i%2===1?1:-1;
  return z;
}
function enumerate(letters,counts,visit,word=[]) {
  if(counts.every(n=>n===0)){visit(word);return;}
  for(let j=0;j<letters.length;j++)if(counts[j]>0){counts[j]--;word.push(letters[j]);enumerate(letters,counts,visit,word);word.pop();counts[j]++;}
}
function run() {
  const k1=kernel(1),k2=kernel(2),b0=[1n,1n];
  assert(eq(k1,[2n,3n])&&eq(k2,[0n,-1n,4n,4n]),"frozen kernel source");
  assert(eq(mul(mul(k1,k2),b0),[0n,-2n,3n,25n,32n,12n]),"R612/R614 two-history coefficient");
  const byLength={},globalKeys=new Set();let tested=0,joins=0;
  function recurse(w,max) {
    const z=encode(w),m=w.length;
    assert(z>=12n**BigInt(m)&&z<2n*12n**BigInt(m),"range");
    assert(decode(z).join(",")===w.join(","),"roundtrip");
    assert(!globalKeys.has(z.toString()),"collision");globalKeys.add(z.toString());tested++;
    byLength[m]=(byLength[m]||0)+1;
    if(m<max){for(let i=1;i<=12;i++){const v=w.concat(i);assert(joinTag(w,[i])===encode(v),"concat");joins++;recurse(v,max);}}
  }
  recurse([],4);
  assert(tested===22621 && joins===22620,"complete length <= 4");
  const fibers=[];
  for(let n=1;n<=6;n++){
    const count=Number(choose(2*n,n)),observed=new Set(),targetBase=mul(k1,k2);
    let target=[1n];for(let j=0;j<n;j++)target=mul(target,targetBase);target=mul(target,b0);
    let seen=0,first=null,last=null;
    enumerate([1,2],[n,n],w=>{
      const key=encode(w).toString();assert(!observed.has(key),"fiber collision");
      observed.add(key);const xy=endpoint(w);assert(xy.every(x=>x===0),"zero endpoint");
      let coef=[1n];for(let i of w)coef=mul(coef,i===1?k1:k2);
      coef=mul(coef,b0);assert(eq(coef,target),"signed source multiplicativity");
      assert(decode(BigInt(key)).join(",")===w.join(","),"fiber decode");
      if(!first)first={word:w.join(","),tag:key};last={word:w.join(","),tag:key};seen++;
    });
    assert(seen===count,"binomial fiber complete");
    assert(BigInt(count)*BigInt(2*n+1)>=2n**BigInt(2*n),"central binomial lower bound");
    fibers.push({n,level_s:3*n,word_count:seen,endpoint_trial:"0^6",signed_coeff_equal:true,first,last});
  }
  return {schema:"EM_R618_SIGNED_BRC_AFFINE_TAG_EVIDENCE_V1",source_pin:"R462@18783e01e3646c72b7aab3b16d3f565e83e6446f",source_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",
    arithmetic:"JavaScript BigInt only; exact integer polynomials",checked_word_lengths:byLength,
    full_word_roundtrips:tested,append_concatenations:joins,distinct_tags:globalKeys.size,
    frozen_K1:k1.map(String),frozen_K2:k2.map(String),two_word_B0_coefficient:mul(mul(k1,k2),b0).map(String),
    permutation_fibers:fibers,success_marker:"R618_EXACT_AFFINE_TAG_FIBER_PASS"};
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
