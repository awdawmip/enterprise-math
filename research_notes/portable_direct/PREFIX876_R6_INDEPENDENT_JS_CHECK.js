'use strict';
// Independent exact integer count for PREFIX-876. Integers are within 2^53.
const B=19, Q=2**B-1;
const near=new Set();
for(let i=1;i<B;i++) near.add(2**i);
for(let i=2;i<B;i++) for(let j=1;j<i;j++) near.add(2**i+2**j);
for(let i=2;i<=B;i++) for(let j=1;j<i;j++) near.add(2**i-2**j);
const all=new Set([...near,2**19,2**20]);
const odds=(lo,hi)=>{const first=lo+(lo%2===0?1:0);return first>hi?0:Math.floor((hi-first)/2)+1;};
const valid=(x,y)=>Number.isInteger(x)&&x>=1&&x<=Q&&x%2===1&&y>=1&&y<=Q&&y%2===1;
let total=0,diagonal=0,intersection=0;
for(const d of all){
  const lo=Math.max(1,Math.ceil((d+1)/3)),hi=Math.min(Q,Math.floor((Q+d)/3));
  total+=odds(lo,hi);
  if(d%4===2&&valid(d/2,d/2)) diagonal++;
  for(const h of near) for(const sign of [-1,1]){
    const x=(d+sign*h)/2, y=x+sign*h;
    if(x>=lo&&x<=hi&&valid(x,y)) intersection++;
  }
}
const outside=total-diagonal-intersection;
const result={
  status:'ALL_EXACT_ASSERTIONS_PASSED',
  differences:all.size,
  three_to_one_including_diagonal:total,
  diagonal,
  intersection_with_PREFIX874:intersection,
  new_beyond_PREFIX874:outside,
  strict_increment_over_PREFIX874_875:outside-1746491,
  confirmed_union_PREFIX874_875_876:136052720+outside
};
if(all.size!==309||total!==27000811||diagonal!==34||
   intersection!==25427||outside!==26975350||
   result.confirmed_union_PREFIX874_875_876!==163028070) throw Error('mismatch');
console.log(JSON.stringify(result));
