#!/usr/bin/env node
'use strict';
/* Exact independent validator for the EC49FBU witness; no search code imported. */
const fs=require('fs');
const r=JSON.parse(fs.readFileSync(__dirname+'/EXACT_REPORT_EC49FBU.json','utf8'));
const OPS='acdefg';
const STEP={a:[-1,-1],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const T=[[1,2,3,1,4,5],[1,6,7,1,1,1],[2,2,8,2,2,2],[3,8,3,3,3,3],[4,2,7,4,4,4],[5,6,3,5,5,5],[6,6,8,6,6,6],[7,8,7,7,7,7],[8,8,8,8,8,8]];
const SIGN=[0,0,4,1,16,32,8,2,0];
const COV={1:[0],2:[3],4:[1],8:[2],16:[0,1],32:[2,3]};
function assert(v,msg){if(!v)throw new Error(msg)}
function check(){
 const primitive=new Set(),tree=new Map(),keys=new Set(),cumulative={},observed={};
 let nwords=0;
 for(let h=2;h<=9;h++){
  const clauses=new Set(),seen=new Set(),ws=r.chosen[String(h)];
  assert(Array.isArray(ws),'missing H'+h);
  for(const w of ws){
   assert(w.length===h,'wrong word length '+w);nwords++;
   let state=0,prefix='',opPrefix='';
   const raw=Array(6).fill(0),pos=Array(6).fill(0);
   for(const c of w){
    const j=OPS.indexOf(c);assert(j>=0,'unknown operation '+c);
    state=T[state][j];assert(state!==8,'observer rejection '+w);
    if(!tree.has(opPrefix))tree.set(opPrefix,new Set());
    tree.get(opPrefix).add(c);opPrefix+=c;
    for(const v of STEP[c]){
     prefix+=v+',';primitive.add(prefix);
     const k=Math.abs(v)-1;raw[k]+=Math.sign(v);
     if(v>0)pos[k]++;
    }
   }
   assert(raw.join(',')==='2,0,0,0,0,0','signed-X6 endpoint mismatch '+w);
   assert(pos.slice(3).every(v=>v===0),'unexpected BRC key axes '+w);
   if(h>=4) assert(pos.slice(0,3).join(',')===(h<=5?r.schedule.H4_H5_L:r.schedule.H6_H9_M).join(','),'BRC key mismatch '+w);
   keys.add(pos.join(','));
   const sig=SIGN[state];assert(COV[sig],'invalid terminal '+w);
   seen.add(sig);for(const k of COV[sig])clauses.add(k);
  }
  assert(clauses.size===4,'rank coverage missing H'+h);
  assert(r.observation_requirements['H'+h].every(v=>seen.has(v)),'signature missing H'+h);
  observed['H'+h]=Array.from(seen).sort((a,b)=>a-b);
  cumulative['H'+h]=primitive.size;
 }
 assert(nwords===24,'word-count mismatch');
 assert(keys.size===5,'BRC-key-budget mismatch');
 let weighted=0,cf=0,dg=0,opEdges=0;
 for(const s of tree.values()){
  for(const c of s){opEdges++;weighted+=STEP[c].length}
  if(s.has('c')&&s.has('f'))cf++;
  if(s.has('d')&&s.has('g'))dg++;
 }
 const compressed=weighted-cf-dg;
 assert(compressed===primitive.size,'lossless compression identity mismatch');
 assert(primitive.size===158,'primitive edge count mismatch');
 assert(Object.entries(r.validation.cumulative_edges).every(([h,v])=>cumulative[h]===v),'horizon edge count mismatch');
 assert(r.native_signed_primitive_union_edges===primitive.size,'reported edge cost mismatch');
 return {status:'PASS',word_count:nwords,primitive_union_edges:primitive.size,distinct_BRC_keys:keys.size,
 cumulative_edges:cumulative,observed,compressed:{operation_edges:opEdges,weighted,overlap_cf:cf,overlap_dg:dg,total:compressed}};
}
console.log(JSON.stringify(check(),null,2));
