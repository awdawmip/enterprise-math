#!/usr/bin/env node
"use strict";
// Exact finite calculation for the analytic moment bounds of X6 R105.
// All arithmetic uses small, exactly represented integers.
const den=[10,68,50,60,42,100], L=35700, threshold=5355;
const q=([x,y,z])=>Math.max([x,y,z].reduce((s,t)=>s+Math.max(t,0),0),[x,y,z].reduce((s,t)=>s+Math.max(-t,0),0));
const canonical=([x,y,z])=>x>0||(x===0&&(y>0||(y===0&&z>0)))?[x,y,z]:[-x,-y,-z];
const score=([x,y,z])=>{
  const u=x+3*y+6*z,v=3*x+12*y+30*z,h=7*x+39*y+126*z;
  return Math.max(...[u,v,h,v-u,h-u,h-v].map((t,i)=>Math.abs(t)*(L/den[i])));
};
let congruent=0,rejected=0;
const directions=new Map();
for(let u=-1;u<=1;u++) for(let v=-10;v<=10;v++) for(let h=-7;h<=7;h++){
  if(v%3 || (h-u)%6 || (h-u-6*v)%12) continue;
  const xn=h+19*u-8*v,yn=-h-14*u+7*v,zn=h+11*u-6*v;
  if(xn%2||yn%3||zn%12) continue;
  const a=[xn/2,yn/3,zn/12];
  if(a.every(t=>t===0))continue;
  congruent++;
  const f=score(a);
  if(f>threshold){rejected++;continue;}
  const c=canonical(a);
  directions.set(c.join(","),{a:c,q:q(c),score_numerator:f});
}
const rows=[...directions.values()].sort((a,b)=>a.q-b.q||a.a[0]-b.a[0]);
const expected=[[[1,0,0],1,5100],[[5,-4,1],6,5100],[[9,-5,1],10,5100],[[10,-5,1],11,3570],[[14,-9,2],16,3570],[[15,-9,2],17,5100],[[19,-10,2],21,5100],[[23,-14,3],26,5100],[[24,-14,3],27,3570],[[25,-14,3],28,5100],[[29,-18,4],33,5100],[[33,-19,4],37,5355],[[34,-19,4],38,4165],[[39,-23,5],44,5355]];
if(L!==35700 || congruent!==32 || rejected!==4 || rows.length!==14 ||
  JSON.stringify(rows.map(r=>[r.a,r.q,r.score_numerator]))!==JSON.stringify(expected))
  throw new Error("exact R105 certificate mismatch");
console.log(JSON.stringify({
 schema:"X6_R105_SHARP_THRESHOLD_EXACT_V1",
 common_denominator:L,minimum_numerator:3570,threshold_numerator:threshold,
 congruent_oriented:congruent,rejected_oriented:rejected,
 closed_unoriented:rows.length,strict_unoriented:rows.filter(r=>r.score_numerator<threshold).length,
 directions:rows,assertions:"PASS"
},null,2));
