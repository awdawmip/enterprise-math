#!/usr/bin/env node
'use strict';
// Independent native-X6 enumeration of the residual 32 H7 key schedules and
// a 4-color minimum-new-edge prefix-tree DP over *optimistically* free earlier prefixes.
const fs=require('fs');
const alphabet={a:[-1,-1], b:[-2,-2], c:[1,2,-1,-2], d:[2,1,-2,-1],e:[3,1,1,-3], f:[1,-1],g:[2,-2]};
const states=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const buckets=['N','A','B','AB','BA'];
const path = w => Array.from(w).flatMap(c=>alphabet[c]);
function positive(s){const v=[0,0,0,0,0,0];for(let x of s)if(x>0)v[x-1]++;return v.join(',')}
function returnX6(s){const v=[0,0,0,0,0,0];for(let x of s)v[Math.abs(x)-1]+=Math.sign(x);return v[0]===2&&v.slice(1).every(x=>x===0)}
function observe(s){return states.map(([old,oldStep])=>{let o=old;for(let q of s){if(oldStep===1&&q===2){if(o==='N')o='A';else if(o==='B')o='BA'}else if(oldStep===2&&q===1){if(o==='N')o='B';else if(o==='A')o='AB'}oldStep=q}return buckets.indexOf(o)}).join(',')}
function assert(ok,msg){if(!ok)throw Error(msg)}
const BASE=['ce','de','ec','ed'];const sigs=BASE.map(w=>observe(path(w)));
assert(new Set(sigs).size===4,'base signature collision');
const sigidx=new Map(sigs.map((v,i)=>[v,i]));
const source=JSON.parse(fs.readFileSync('EC49EXC_H6_BOUNDED_COMPLETE.json','utf8'));
const screened=JSON.parse(fs.readFileSync('EC49EXC_SCREENED.json','utf8'));
const target=screened.unresolved.filter(row=>{
 const k=row.h3to6.map(p=>p.join(',')).join(':');return source[k]!==null
});
assert(target.length===32,`expected 32 residual schedules, got ${target.length}`);
const keys=Array.from(new Set(target.flatMap(r=>r.h3to6.concat([r.p7]).map(p=>p.join(',')))));
const setKeys=new Set(keys);const fibers={};
for(let h=3;h<=7;h++)fibers[h]=new Map();
const tokens=Object.entries(alphabet);
for(let h=3;h<=7;h++){
 function recur(w,st){if(w.length===h){if(!returnX6(st))return;const p=positive(st);if(!setKeys.has(p))return;const si=sigidx.get(observe(st));if(si===undefined)return;
  const kk=p+'|'+si;if(!fibers[h].has(kk))fibers[h].set(kk,[]);fibers[h].get(kk).push(st);return}
  for(const [c,steps] of tokens)recur(w+c,st.concat(steps));
 }
 recur('',[]);
}
function addPrefixes(words){const res=new Set();for(const st of words)for(let j=1;j<=st.length;j++)res.add(st.slice(0,j).join(','));return res}
let results=[];
for(let row of target){
 const old=addPrefixes(BASE.map(path));
 for(let h=3;h<=6;h++)for(let si=0;si<4;si++){
  const p=row.h3to6[h-3].join(',');for(const st of fibers[h].get(p+'|'+si)||[])
   for(let j=1;j<=st.length;j++)old.add(st.slice(0,j).join(','));
 }
 const root={kids:new Map(),mask:0};const p7=row.p7.join(',');let numWords=0;
 for(let si=0;si<4;si++)for(const st of fibers[7].get(p7+'|'+si)||[]){
  numWords++;let n=root;for(const x of st){if(!n.kids.has(x))n.kids.set(x,{kids:new Map(),mask:0});n=n.kids.get(x)}n.mask|=1<<si;
 }
 assert(numWords>0,'missing H7 words');
 function visit(n,steps){let best=Array(16).fill(Infinity);best[0]=0;
  for(const [step,child] of n.kids){const d=visit(child,steps.concat([step]));const next=Array(16).fill(Infinity);
   for(let a=0;a<16;a++)for(let b=0;b<16;b++){
    const cc=best[a]+d[b];if(cc<next[a|b])next[a|b]=cc;
   }best=next;
  }
  if(steps.length){const charge=old.has(steps.join(','))?0:1;
   const out=Array(16).fill(Infinity);out[0]=0;
   for(let a=0;a<16;a++)if(Number.isFinite(best[a])){
    const mask=a|n.mask;if(mask)out[mask]=Math.min(out[mask],best[a]+charge);
   }best=out;
  }return best;
 }
 const min=visit(root,[])[15];assert(min===12,`expected 12 but got ${min} on ${JSON.stringify(row)}`);
 results.push({p7,lower_min:12,old_prefix_count:old.size,word_count7:numWords});
}
const report={unit:'EC49EXC',status:'PASS',verifier:'Independent JS enumeration with signed-X6 vectors, inherited 32 residual schedules and new four-color native-prefix DP',cases:results.length,minimum_extra_edges_histogram:{'12':results.length},h7_unique_keys:[...new Set(results.map(x=>x.p7))],no_optimistic_h7_cost_below_12:true};
fs.writeFileSync('EC49EXC_INDEPENDENT_EXECUTED.json',JSON.stringify(report,null,2));
console.log(JSON.stringify(report,null,2));
