#!/usr/bin/env node
// Independent finite-language and witness verifier for EC49EW.
// Does not read the Python model or C++ DP program.
'use strict';
const assert=require('node:assert/strict');
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const STATE=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]], BUCKETS=['N','A','B','AB','BA'],P=1000003;
const native=w=>[...w].flatMap(x=>OPS[x]);
function poscount(seq){const p=[0,0,0,0,0,0];for(const i of seq)if(i>0)p[i-1]++;return p.join(',');}
function disp(seq){const d=[0,0,0,0,0,0];for(const i of seq)d[Math.abs(i)-1]+=Math.sign(i);return d;}
function sig(seq){return STATE.map(([event,last])=>{for(const i of seq){if(last===1&&i===2)event=({N:'A',B:'BA'})[event]||event;else if(last===2&&i===1)event=({N:'B',A:'AB'})[event]||event;last=i;}return BUCKETS.indexOf(event);}).join(',');}
function modpow(x,k){let y=1;while(k>0){if(k&1)y=y*x%P;x=x*x%P;k=Math.floor(k/2);}return y;}
function rank(sigs){let piv={},r=0;for(const s of sigs){const q=s.split(',').map(Number);for(let b=0;b<5;b++){const v=q.map(x=>Number(x===b));for(let i=0;i<9;i++){if(!v[i])continue;if(piv[i]){const d=v[i];for(let j=i;j<9;j++)v[j]=((v[j]-d*piv[i][j])%P+P)%P;}else{const inv=modpow(v[i],P-2);piv[i]=v.map(x=>x*inv%P);r++;break;}}}}return r;}
function contains(a,b){return [...a].every(x=>b.has(x));}
const base=['ce','de','ec','ed'],T4=new Set(base.map(w=>sig(native(w)))),T2=new Set(['feg','gef'].map(w=>sig(native(w))));
assert.equal(T4.size,4);assert.equal(T2.size,2);assert.equal(rank(T4),9);assert.equal(rank(T2),9);
const T4F={},T2F={},returns={};
for(let h=2;h<=7;h++){
 const fibers=new Map();let cnt=0;
 function rec(s,d1,d2){if(s.length===h){if(d1!==2||d2!==0)return;cnt++;
  const n=native(s),p=poscount(n),q=sig(n);
  if(!fibers.has(p))fibers.set(p,new Set());fibers.get(p).add(q);return;}
  for(const [op,seq]of Object.entries(OPS)){
    let a=0,b=0;for(const i of seq){if(Math.abs(i)===1)a+=Math.sign(i);if(Math.abs(i)===2)b+=Math.sign(i);}rec(s+op,d1+a,d2+b);
  }
 }
 rec('',0,0);returns[h]=cnt;
 T4F[h]=[...fibers].filter(([,s])=>contains(T4,s)).map(([p])=>p);
 T2F[h]=[...fibers].filter(([,s])=>contains(T2,s)).map(([p])=>p);
}
assert.deepEqual(Object.values(returns),[8,51,304,1770,10224,58947]);
assert.deepEqual(Object.values(T4F).map(x=>x.length),[1,3,7,13,22,34]);
assert.deepEqual(Object.values(T2F).map(x=>x.length),[0,1,2,4,6,9]);
let s4count=0;
for(const p3 of T4F[3])for(const p4 of T4F[4])for(const p5 of T4F[5])for(const p6 of T4F[6])for(const p7 of T4F[7])if(new Set([T4F[2][0],p3,p4,p5,p6,p7]).size===4)s4count++;
assert.equal(s4count,752);
let subclassCount=0;
for(const p3 of T2F[3])for(const p4 of T2F[4])for(const p5 of T2F[5])for(const p6 of T4F[6])for(const p7 of T2F[7])if(new Set([T4F[2][0],p3,p4,p5,p6,p7]).size===4)subclassCount++;
assert.equal(subclassCount,72);
const witnessS4={2:base,3:['cec','ded','ecc','edd'],4:['cefg','degf','ecfg','edgf'],5:['cefgg','degfg','ecfgg','edgfg'],6:['cefggc','degfgd','ecfggc','edgfgd'],7:['cefggfg','degfggf','ecfggfg','edgfggf']};
const witnessS6={2:base,3:['feg','gef'],4:['fegg','gefg'],5:['feggg','gefgg'],6:['fegggc','fegggd','gefggc','gefggd'],7:['fegggfg','gefggfg']};
function verify(want,E,M,S){const prefixes=new Set(),keys=new Set(),types=new Set(),horizon={};
 for(let h=2;h<=7;h++){
  const ws=want[h],hkeys=new Set(),hsigs=new Set();
  for(const w of ws){assert.equal(w.length,h);const seq=native(w);assert.deepEqual(disp(seq),[2,0,0,0,0,0]);const k=poscount(seq),s=sig(seq);hkeys.add(k);hsigs.add(s);
    for(let i=1;i<=seq.length;i++)prefixes.add(seq.slice(0,i).join(','));}
  assert.equal(hkeys.size,1);assert.equal(rank(hsigs),9);for(const x of hkeys)keys.add(x);for(const x of hsigs)types.add(x);
  horizon[h]={positive:[...hkeys][0],observer_signature_count:hsigs.size,rank:rank(hsigs),words:ws};
 }
 assert.deepEqual([prefixes.size,keys.size,types.size],[E,M,S]);return {E:prefixes.size,M:keys.size,S:types.size,horizons:horizon};
}
const res={status:'PASS',frozen_native_language:'a,b,c,d,e,f,g',fully_enumerated_return_words:returns,fiber_counts:{T4:Object.values(T4F).map(x=>x.length),T2:Object.values(T2F).map(x=>x.length)},exact_S4_M4_key_schedule_count:s4count,exact_T2T2T2T4T2_M4_schedule_count:subclassCount,witness_S4:verify(witnessS4,92,4,4),witness_S6:verify(witnessS6,72,4,6)};
console.log(JSON.stringify(res,null,2));
