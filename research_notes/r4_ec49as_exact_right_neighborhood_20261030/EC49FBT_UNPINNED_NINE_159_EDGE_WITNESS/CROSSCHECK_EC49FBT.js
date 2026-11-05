#!/usr/bin/env node
"use strict";
// Independent witness check for EC49FBT; read EXACT_REPORT_EC49FBT.json.
const fs=require('fs');
const report=JSON.parse(fs.readFileSync(__dirname+'/EXACT_REPORT_EC49FBT.json','utf8'));
const OPS='acdefg',STEP={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const TRANS=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7],[8,8,8,8,8,8]];
const SIGN=[0,0,4,1,16,32,8,2,0];
const CLAUSES={1:[0],4:[1],8:[2],2:[3],16:[0,1],32:[2,3]};
function assert(test,description){if(!test)throw new Error(description)}
let all=new Set(),operationTree=new Map(),keys=new Set(),perWindow={};
for(let h=2;h<=9;h++){
 let rank=new Set(),ww=report.chosen[String(h)]; assert(Array.isArray(ww)&&ww.length>0,'missing H'+h);
 let n0=all.size;
 for(let rec of ww){
  let w=rec.word,ns=0,raw=Array(6).fill(0),positive=Array(6).fill(0),prefix='';
  assert(w.length===h,'wrong length '+w);
  let up='';
  for(const op of w){
   const opid=OPS.indexOf(op); assert(opid>=0,'wrong op '+op);
   ns=TRANS[ns][opid]; assert(ns!==8,'rejected observer '+w);
   if(!operationTree.has(up))operationTree.set(up,new Set()); operationTree.get(up).add(op);up+=op;
   for(const axis of STEP[op]){
    prefix+=String(axis)+',';all.add(prefix);
    raw[Math.abs(axis)-1]+=Math.sign(axis);
    if(axis>0)positive[axis-1]++;
   }
  }
  let sig=SIGN[ns]; assert(sig===rec.signature,'wrong signature '+w);
  assert(raw.join(',')==='2,0,0,0,0,0','wrong native endpoint '+w);
  assert(positive.slice(3).every(x=>x===0),'unexpected positive key '+w);
  let key=positive.slice(0,3).join(','); keys.add(key);
  if(h>=4){let expected=(h<=5?report.L:report.M).join(',');assert(key===expected,'wrong schedule key '+w)}
  assert(CLAUSES[sig],'invalid observer terminal '+w);
  for(const k of CLAUSES[sig])rank.add(k);
 }
 for(let k=0;k<4;k++)assert(rank.has(k),'uncovered clause H'+h+' '+k);
 perWindow[h]={words:ww.length,added_native_edges:all.size-n0,cumulative_native_edges:all.size};
}
assert(keys.size===5,'wrong BRC five-key budget, saw '+keys.size);
let weighted=0,cf=0,dg=0,edges=0;
for(const children of operationTree.values()){
 edges+=children.size;
 for(const op of children)weighted+=STEP[op].length;
 if(children.has('c')&&children.has('f'))cf++;
 if(children.has('d')&&children.has('g'))dg++;
}
assert(weighted-cf-dg===all.size,'compressed/primitive cost mismatch');
assert(all.size===report.native_union_edges,'union cost mismatch');
console.log(JSON.stringify({schema:'EC49FBT_SIGNED_NATIVE_WITNESS_CHECK_V1',status:'PASS',union_edges:all.size,distinct_BRC_keys:keys.size,per_window:perWindow,compressed:{operation_edges:edges,weighted,overlap_cf:cf,overlap_dg:dg,cost:weighted-cf-dg}},null,2));
