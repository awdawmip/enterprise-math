#!/usr/bin/env node
"use strict";
/* Independent exact native-X6 key-schedule enumerator; no Python import. */
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],
 e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const STATES=[['N',0],['N',1],['N',2],['A',0],['A',2],
 ['B',0],['B',1],['AB',0],['BA',0]];
const BUCKETS=['N','A','B','AB','BA'];
function signature(q){
 const out=[];
 for(const [initial,previous] of STATES){
  let event=initial,prev=previous;
  for(const s of q){
   if(prev===1&&s===2){if(event==='N')event='A';else if(event==='B')event='BA';}
   else if(prev===2&&s===1){if(event==='N')event='B';else if(event==='A')event='AB';}
   prev=s;
  }
  out.push(BUCKETS.indexOf(event));
 }
 return out.join(',');
}
const expand=w=>w.split('').flatMap(c=>OPS[c]);
const T4=new Set(['ce','de','ec','ed'].map(w=>signature(expand(w))));
if(T4.size!==4)throw Error('base signature count');
const P={},returnCounts={};
for(let h=2;h<=7;h++){
 const map=new Map(),current=[],alpha=Object.keys(OPS);let returned=0;
 function rec(i,delta){
  if(i===h){
   if(delta[0]!==2||delta.slice(1).some(x=>x!==0))return;
   returned++;
   const q=current.flatMap(x=>OPS[x]),s=signature(q);
   if(!T4.has(s))return;
   const p=[1,2,3,4,5,6].map(a=>q.filter(v=>v===a).length).join(',');
   if(!map.has(p))map.set(p,new Set());
   map.get(p).add(s);return;
  }
  for(const c of alpha){
   current.push(c);const next=delta.slice();
   for(const v of OPS[c])next[Math.abs(v)-1]+=Math.sign(v);
   rec(i+1,next);current.pop();
  }
 }
 rec(0,[0,0,0,0,0,0]);
 returnCounts[h]=returned;
 P[h]=[...map].filter(([k,v])=>v.size===4).map(([k])=>k).sort();
}
const exp=[1,3,7,13,22,34];
for(let h=2;h<=7;h++)if(P[h].length!==exp[h-2])throw Error('fiber count');
let scanned=0,nM5=0;const counts=new Map(),seq=[P[2][0]];
function walk(h){
 if(h===8){
  scanned++;if(new Set(seq).size!==5)return;
  nM5++;const pairs=[];
  for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)if(seq[i]===seq[j])pairs.push((i+2)+','+(j+2));
  if(pairs.length!==1)throw Error('duplicate count');
  const p=pairs[0];counts.set(p,(counts.get(p)||0)+1);return;
 }
 for(const key of P[h]){seq.push(key);walk(h+1);seq.pop();}
}
walk(3);
const out=Object.fromEntries([...counts].sort()),target={
 '3,4':9257,'4,5':6513,'4,6':1215,'5,6':4598,'5,7':1251,'6,7':3203};
if(JSON.stringify(out)!==JSON.stringify(target)||scanned!==204204||nM5!==26037)throw Error('enumeration mismatch');
const late=out['5,7']+out['6,7'];if(late!==4454||nM5-late!==21583)throw Error('split mismatch');
console.log(JSON.stringify({unit:'EC49EXB_JS',status:'PASS',returning_words:returnCounts,
 eligible_key_counts:Object.fromEntries(Object.entries(P).map(([k,v])=>[k,v.length])),
 schedules_examined:scanned,M5_schedules:nM5,repeat_pair_counts:out,
 early_repeat:nM5-late,late_repeat:late,
 limitation:'Finite key scheduling only; no exhaustive late-repeat primitive-prefix minimization'},null,2));
