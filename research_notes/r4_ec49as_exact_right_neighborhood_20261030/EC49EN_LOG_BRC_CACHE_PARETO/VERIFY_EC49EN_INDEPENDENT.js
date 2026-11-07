"use strict";
// EC49EN independent finite exhaustive p-fiber set-cover check.
// This does not import the first-event/trie word constructor from VERIFY_EC49EN.js.
function check(x,txt){if(!x)throw Error(txt);}
function exactCover(H,eventOnly){
 const n=H-1,target=(1<<n)-1,masks=new Set();let fibers=0;
 for(let e=1;2*e-1<=H;e++)for(let p1=2*e;p1<=H+1;p1++){
  for(let p2=0;p2<=H+1;p2++){
   const m=Math.min(p1-2*e,p2);if(m===0)continue;
   const start=p1+p2-1-m;
   const end=p1+p2-(eventOnly?2:1);
   if(start>H||end<2)continue;
   fibers++;let mask=0;
   for(let h=Math.max(2,start);h<=Math.min(H,end);h++)mask|=1<<(h-2);
   if(mask)masks.add(mask);
  }
 }
 const d=new Array(1<<n).fill(n+1);d[0]=0;
 for(const mask of masks)for(let state=target;state>=0;state--){
  if(d[state]===n+1)continue;const next=state|mask;
  if(d[next]>d[state]+1)d[next]=d[state]+1;
 }
 const ceilLog2=k=>{let j=0,v=1;while(v<k){v*=2;j++;}return j;};
 const predicted=eventOnly?ceilLog2(H):ceilLog2(H+1)-1;
 check(d[target]===predicted,"DP mismatch H="+H+" eventOnly="+eventOnly);
 return {H,eventOnly,candidate_positive_fibers:fibers,
  distinct_horizon_intervals:masks.size,exact_min_fibers:d[target]};
}
const rows=[];for(let H=2;H<=12;H++){
 rows.push(exactCover(H,false));rows.push(exactCover(H,true));
}
return {status:"PASS",unit:"EC49EN_INDEPENDENT_EXACT_COVER",
 method:"complete bounded nonnegative integer p-fiber enumeration and exact bitmask set cover",
 range_H:[2,12],number_of_certified_subproblems:rows.length,
 completeness_bound:"Any fiber touching h<=H has A=max(p1-1,p2+2e-1)<=H; thus e<=(H+1)/2, p1<=H+1, p2<=H-2e+1.",
 rows,conclusion:"All 22 finite minima equal analytic formulas; see README_EC49EN.md for proof at every H."};
