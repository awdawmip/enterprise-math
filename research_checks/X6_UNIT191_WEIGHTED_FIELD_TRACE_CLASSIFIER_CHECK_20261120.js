"use strict";
// Unit191: independent exact source-equivalent finite enumeration.
// Run with Node: node X6_UNIT191_WEIGHTED_FIELD_TRACE_CLASSIFIER_CHECK_20261120.js
function partitions(n){const out=[],lab=Array(n).fill(0);function rec(i,k){if(i===n){const P=Array.from({length:k},()=>[]);for(let j=0;j<n;j++)P[lab[j]].push(j);out.push(P);return;}for(let b=0;b<=k;b++){lab[i]=b;rec(i+1,Math.max(k,b+1));}}rec(0,0);return out;}
function verify(){
const P=partitions(6),ms=[[1,1,1,1,1,1],[1,2,1,2,1,2],[2,3,5,7,11,13]];
const dir=d=>({i:d%6,s:d<6?1:-1}),key=a=>a.join(","),equal=(a,b)=>key(a)===key(b),add=(a,b)=>a.map((x,i)=>x+b[i]);
function fine(m,d){const {i,s}=dir(d),a=[];for(let j=0;j<6;j++)for(let k=j+1;k<6;k++)a.push(m[k]*(j===i?s:0)-m[j]*(k===i?s:0));return a;}
function coarse(m,p,d){const {i,s}=dir(d),A=p.findIndex(g=>g.includes(i)),M=p.map(g=>g.reduce((v,j)=>v+m[j],0)),out=[];for(let a=0;a<p.length;a++)for(let b=a+1;b<p.length;b++)out.push((a===A?s*M[b]:0)-(b===A?s*M[a]:0));return out;}
function producer(m,p,d){const {i,s}=dir(d),z=Array.from({length:6},(_,j)=>j===i?s:0),F=Array.from({length:6},(_,a)=>Array.from({length:6},(_,b)=>m[b]*z[a]-m[a]*z[b])),out=[];for(let a=0;a<p.length;a++)for(let b=a+1;b<p.length;b++){let v=0;for(const i of p[a])for(const j of p[b])v+=F[i][j];out.push(v);}return out;}
function expect(m,p,d,e){const k=p.length;if(k===1)return true;const da=dir(d),db=dir(e),A=p.findIndex(g=>g.includes(da.i)),B=p.findIndex(g=>g.includes(db.i));if(A===B&&da.s===db.s)return true;if(k===2&&A!==B&&da.s===-db.s){const M=p.map(g=>g.reduce((v,j)=>v+m[j],0));return M[0]===M[1];}return false;}
if(P.length!==203)throw Error("Bell6 mismatch");
let direct=0,pairs=0,fullPairs=0,seq=0,collisions=0,cases=0,ambiguous=0,balanced=0,withinBlock=0;const byK={};
for(const p of P)for(const m of ms){const k=p.length;cases++;byK[k]??={cases:0,aliasPairs:0,traceCollisionPairs:0};byK[k].cases++;
const f=Array.from({length:12},(_,d)=>fine(m,d)),w=Array.from({length:12},(_,d)=>coarse(m,p,d));
for(let d=0;d<12;d++){if(!equal(w[d],producer(m,p,d)))throw Error("source coarsening discrepancy");direct++;
for(let e=0;e<12;e++){pairs++;const eq=equal(w[d],w[e]);if(eq!==expect(m,p,d,e))throw Error("wrong coarse alias classification");if(eq&&d!==e)byK[k].aliasPairs++;if(d!==e&&equal(f[d],f[e]))throw Error("full field primitive collision");fullPairs++;}}
const M=p.map(g=>g.reduce((v,j)=>v+m[j],0));if(k===2&&M[0]===M[1])balanced++;
const seen=new Map();let local=0;
for(let d=0;d<12;d++)for(let e=0;e<12;e++){const identity=key(w[d])+"|"+key(add(w[d],w[e]))+"#"+key(add(f[d],f[e]));
if(seen.has(identity)){local++;collisions++;byK[k].traceCollisionPairs++;}else seen.set(identity,[d,e]);seq++;}
if(p.some(g=>g.length>1)&&local===0)throw Error("missing order ambiguity");if(k===6&&local!==0)throw Error("false full-field ambiguity");
if(k>=2&&p.some(g=>g.length>1))withinBlock++;if(local>0)ambiguous++;}
return {schema:"X6_UNIT191_EXACT_COARSE_TRACE_CLASSIFIER_V1",status:"EXACT_FINITE_EXECUTED",frozen_A3_commit:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",frozen_X6_commit:"59538f585d037d09ef687b28715c4bc1a3f9fe03",partitions:203,capacity_vectors:ms,cases,coarsening_source_formula_checks:direct,distinct_signed_primitive_pair_checks:pairs,full_field_distinct_pair_checks:fullPairs,two_step_signed_words:seq,two_step_order_aliases:collisions,ambiguous_partition_capacity_cases:ambiguous,balanced_two_group_cases:balanced,within_block_nontrivial_cases:withinBlock,by_k:byK,violations:0,original_R063_benchmark_reexecuted:false,scope:"independent exact integer source-equivalent checker; no native runtime import; no independent review or admission"};}
const result=verify();
if(typeof console!=="undefined")console.log(JSON.stringify(result,null,2));
if(typeof module!=="undefined")module.exports={verify};
