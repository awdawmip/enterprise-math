'use strict';
// EC49EXM independent integer subset-DP/Hall-style crosscheck.
// Reuses EC49EXL's *proved finite* rank9 key eligibility; no native word/rank replay.
const H=[2,3,4,5,6,7,8];
function options(h){
  const S=new Set();
  for(let r=0;r<=h;r++)for(let a=0;a<=Math.floor((h-1)/2);a++){
    const w=a+1;
    for(let f=0;f<=h;f++){
      const g=h-2*a-1-r-f;
      if(g<0)continue;
      if(r===0 && (f===0 || g===0))continue;
      const u=r+2*w+f,v=r+g;
      S.add(`${u},${v},${w}`);
    }
  }
  return S;
}
const S=Object.fromEntries(H.map(h=>[h,options(h)]));
const expected=[1,4,9,17,28,43,62];
if(H.some((h,i)=>S[h].size!==expected[i]))throw Error('eligible key counts differ');
const partitions=[];
function enumRGS(seq,num){
  if(seq.length===7){if(num===5)partitions.push(seq);return;}
  for(let v=0;v<=num&&v<5;v++)enumRGS(seq.concat(v),Math.max(num,v+1));
}
enumRGS([0],1);
if(partitions.length!==140)throw Error('partition mismatch');
const result=[];
for(const p of partitions){
  const blocks=Array.from({length:5},()=>[]);
  H.forEach((h,i)=>blocks[p[i]].push(h));
  if(!blocks.some(b=>b.length===3))continue;
  const eligible=blocks.map(b=>[...S[b[0]]].filter(k=>b.slice(1).every(h=>S[h].has(k))));
  const U=[...new Set(eligible.flat())];
  const dp=Array(32).fill(0);dp[0]=1;
  for(const key of U){
    const nd=dp.slice();
    for(let m=0;m<32;m++)if(dp[m])for(let b=0;b<5;b++)if(!(m&(1<<b))&&eligible[b].includes(key))nd[m|1<<b]+=dp[m];
    for(let m=0;m<32;m++)dp[m]=nd[m];
  }
  if(dp[31])result.push({p,count:dp[31],triple:blocks.find(b=>b.length===3),triple_options:eligible[blocks.findIndex(b=>b.length===3)].length});
}
const expectedWays=[71799,23502,4983,2905,10158,3015,1917,4868];
if(result.length!==8 || result.some((r,i)=>r.count!==expectedWays[i]) || result.reduce((s,r)=>s+r.count,0)!==123147)throw Error(JSON.stringify(result));
console.log(JSON.stringify({status:'PASS',triple_skeletons:result.length,total_full_key_schedules:123147,families:result},null,2));
