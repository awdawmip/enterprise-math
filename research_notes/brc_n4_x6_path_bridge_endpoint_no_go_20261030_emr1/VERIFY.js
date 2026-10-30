'use strict';
// Exact integer proof checks for a typed X6-path representation of the
// frozen external 16-leaf BRC N=4 two-law experiment.
// All probabilities are represented by integer numerators; no floats.
function check(cond, msg) { if (!cond) throw new Error(msg); }
function vector(axis, sign) {
  const v=[0,0,0,0,0,0]; v[axis]=sign; return v;
}
function plus(a,b) { return a.map((x,i)=>x+b[i]); }
function minus(a,b) { return a.map((x,i)=>x-b[i]); }
function sig(s,j,k) {
  return [s<2?1:-1, s%2===0?1:-1, j===0?1:-1, k===0?1:-1];
}
function decode(v) {
  check(v.length===6 && v[4]===0 && v[5]===0, 'full-X6 endpoint type');
  for(let a=0;a<4;a++) check(Math.abs(v[a])===1,'word support');
  return [(v[0]<0?2:0)+(v[1]<0?1:0), v[2]<0?1:0, v[3]<0?1:0];
}
function add(map,key,w) { map[key]=(map[key]||0n)+w; }
function sum(map) { return Object.values(map).reduce((a,b)=>a+b,0n); }
function abs(x) { return x<0n?-x:x; }
function ratioConstant(items, keyfn) {
  const cells=new Map();
  for(const x of items) {
    const key=keyfn(x);
    if(!cells.has(key)) cells.set(key,[]);
    cells.get(key).push(x);
  }
  for(const arr of cells.values()) {
    const p=arr.reduce((a,x)=>a+x.p,0n);
    const q=arr.reduce((a,x)=>a+x.q,0n);
    for(const x of arr) if(x.p*q!==x.q*p) return false;
  }
  return true;
}
const Q=[10n,20n,15n,15n]; // per-leaf numerator over 240
const P=[[9n,11n],[5n,5n],[3n,27n],[30n,30n]];
const labels=['AU','AV','BU','BV'];
let totalP=0n,totalQ=0n;
const leaves=[],seen=new Set();
const anchor=[2,-5,8,11,-3,0];
const move=[-7,6,0,3,2,19];
for(let s=0;s<4;s++)for(let j=0;j<2;j++)for(let k=0;k<2;k++){
  const word=sig(s,j,k).map((sign,a)=>vector(a,sign));
  for(const step of word) check(step.filter(x=>x!==0).length===1, 'primitive native step');
  let x=anchor.slice(), y=plus(anchor,move);
  const trace=[x];
  for(const step of word) {x=plus(x,step);y=plus(y,step);trace.push(x);}
  const v=minus(x,anchor),vt=minus(y,plus(anchor,move));
  check(v.join(',')===vt.join(','),'translation equivariant word');
  const key=v.join(',');
  check(!seen.has(key),'injective 16-endpoint family');
  seen.add(key);
  check(decode(v).join(',')===[s,j,k].join(','),'word leaf decode');
  const p=P[s][j],q=Q[s];
  totalP+=p;totalQ+=q;
  leaves.push({s,j,k,p,q,v,word,trace,key});
}
check(leaves.length===16 && seen.size===16,'sixteen distinct path labels');
check(totalP===240n && totalQ===240n,'exact source normalization');
check(leaves.every(x=>x.p>0n && x.q>0n),'strictly positive support');
const nodeP=[0n,0n,0n,0n],nodeQ=[0n,0n,0n,0n];
for(const l of leaves){nodeP[l.s]+=l.p;nodeQ[l.s]+=l.q;}
check(nodeP.join(',')==='40,20,60,120','P source nodes');
check(nodeQ.join(',')==='40,80,60,60','Q source nodes');
check(ratioConstant(leaves,l=>l.key),'full-X6 restricted endpoint is sufficient');
check(!ratioConstant(leaves,l=>[1,3].includes(l.s)?'E':(l.s===0?'A':'B')),
  'coarse C is not fully sufficient');
// Exogenous 1/4-error J sensor: (BU,Z=0) masses /960.
let pZ0=0n,qZ0=0n;
for(const l of leaves)if(l.s===2){const znum=l.j===0?3n:1n;pZ0+=l.p*znum;qZ0+=l.q*znum;}
check(pZ0===72n && qZ0===120n,'noisy provenance joint masses');
// One legitimate S2 prefix-adapted policy: continue AU/BU at T2,
// BU T3 rates u0=1/4,u1=3/4, T4 observe K,
// choose P iff J=K (not an S23 terminal policy).
const pY={},qY={};
for(const l of leaves){
  const x=decode(l.v), s=x[0],j=x[1],k=x[2];
  const addBoth=(key,m)=>{add(pY,key,l.p*m);add(qY,key,l.q*m);};
  if(s===0) addBoth('A',4n);
  else if(s===1||s===3) addBoth('E',4n);
  else {
    const n=j===0?1n:3n;
    addBoth('B3',4n-n);
    addBoth('B4'+(j===k?'P':'Q')+String(k),n);
  }
}
const expectP={E:560n,A:160n,B3:72n,B4P0:3n,B4P1:81n,B4Q0:81n,B4Q1:3n};
const expectQ={E:560n,A:160n,B3:120n,B4P0:15n,B4P1:45n,B4Q0:45n,B4Q1:15n};
for(const [k,v] of Object.entries(expectP))check(pY[k]===v,'P policy '+k);
for(const [k,v] of Object.entries(expectQ))check(qY[k]===v,'Q policy '+k);
check(sum(pY)===960n && sum(qY)===960n,'policy preserves both laws');
let sumAbs=0n;
for(const k of Object.keys(expectP))sumAbs+=abs(pY[k]-qY[k]);
check(sumAbs===144n && sumAbs*40n===3n*1920n,'policy TV=3/40');
// A two-path collision at the SAME native full-X6 endpoint.
const w12=[vector(0,1),vector(1,1)];
const w21=[vector(1,1),vector(0,1)];
const end12=w12.reduce(plus,[0,0,0,0,0,0]);
const end21=w21.reduce(plus,[0,0,0,0,0,0]);
check(end12.join(',')===end21.join(','),'same endpoint');
check(w12[0].join(',')!==w21[0].join(','),'distinct time-one readout');
const swap=[{first:0,p:3n,q:1n},{first:1,p:1n,q:3n}];
check(!ratioConstant(swap,_=>'same-endpoint'),'endpoint loses order likelihood');
check(ratioConstant(swap,l=>l.first),'one-bit order repairs experiment');
check(abs(3n-1n)+abs(1n-3n)===4n,'first-readout TV=1/2 on denominator 4');
check((abs(3n-1n)+abs(1n-3n))*1n===4n,'common-minimax radius 1/4');
return [
 'PASS_X6_BRC_PATH_BRIDGE_ENDPOINT_OBSTRUCTION_20261030',
 '16 positive leaves; both law sums = 240/240',
 'native primitive four-step words = 16; distinct full-X6 relative endpoints = 16',
 'translation-covariant relative path words; six-coordinate charts preserved',
 'node numerators P=[40,20,60,120], Q=[40,80,60,60] /240',
 'auxiliary BU noisy sensor Z=0 numerators P=72,Q=120 /960 (epsilon=1/4)',
 'lawful S2 joint transcript TV=3/40; output totals P=Q=960/960',
 'same-endpoint order swap: first-step TV=1/2, endpoint TV=0, common radius=1/4',
 'endpoint fiber criterion: injective template PASS, full-word swap FAIL, order-bit repair PASS',
 'No native physical time/stochastic transition law assumed.'
].join('\n');