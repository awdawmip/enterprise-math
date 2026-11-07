'use strict';
// Stage438-B: exact finite audit of protected-overlap joint quotients.
// Native X6 has six signed axes, encoded a,b,c,d,e,f,g,h,i,j,k,l.
const assert = require('node:assert/strict');
const D = [...'abcdefghijkl'];
const A = 'a', B = 'b', C = 'c';
function vec(word) {
  const v = Array(6).fill(0);
  for (const d of word) {
    const t = D.indexOf(d);
    assert(t >= 0);
    v[Math.floor(t/2)] += t % 2 === 0 ? 1 : -1;
  }
  return v;
}
function one(word) {
  const J = Array(144).fill(0);
  for (let i = 1; i < word.length; i++) J[12*D.indexOf(word[i-1])+D.indexOf(word[i])]++;
  return [word.length, ...vec(word), ...J];
}
function observation(P,Q) {
  let K=0;
  for (let i=0;i<Math.min(P.length,Q.length);i++) K+=+(P[i]===Q[i]);
  return JSON.stringify([...one(P),...one(Q),K]);
}
function quotientKey(P,Q,pP,pQ,rQ) {
  const bits=[];
  for(let i=Q.length-pQ;i<Q.length;i++) bits.push(+(P[i]===Q[i]));
  return JSON.stringify([P.slice(-pP-1),Q.slice(-pQ-1),rQ>0 ? P.slice(Q.length-pQ,Q.length+rQ) : bits]);
}
function words(alpha,n) {
  let a=[''];
  for(let j=0;j<n;j++) a=a.flatMap(s=>alpha.map(c=>s+c));
  return a;
}
function futures(P,Q,pP,rP,pQ,rQ) {
  const out=[];
  function rec(x,y,a,b,c,d,trace) {
    out.push(trace+':'+observation(x,y));
    if(a>0&&x.length>1)rec(x.slice(0,-1),y,a-1,b,c,d,trace+'P-;');
    if(b>0)for(const z of D)rec(x+z,y,a,b-1,c,d,trace+'P+'+z+';');
    if(c>0&&y.length>1)rec(x,y.slice(0,-1),a,b,c-1,d,trace+'Q-;');
    if(d>0)for(const z of D)rec(x,y+z,a,b,c,d-1,trace+'Q+'+z+';');
  }
  rec(P,Q,pP,rP,pQ,rQ,'');
  out.sort();
  return out.join('\n');
}
const tests=[];
function auditAll(m,n,pP,rP,pQ,rQ,alpha) {
  assert(m-pP>=n+rQ);
  const fibers = new Map();
  for(const P of words(alpha,m))for(const Q of words(alpha,n)) {
    const o=observation(P,Q);
    if(!fibers.has(o))fibers.set(o,[]);
    fibers.get(o).push([P,Q]);
  }
  let checked=0, multi=0, distinct=0, futureWords=0;
  for(const F of fibers.values()) {
    if(F.length===1)continue;
    multi++;
    const byKey=new Map(),byFuture=new Map();
    for(const [P,Q] of F) {
      const key=quotientKey(P,Q,pP,pQ,rQ),sig=futures(P,Q,pP,rP,pQ,rQ);
      if(byKey.has(key))assert.equal(byKey.get(key),sig);
      else byKey.set(key,sig);
      if(byFuture.has(sig))assert.equal(byFuture.get(sig),key);
      else byFuture.set(sig,key);
      checked++;
      if(futureWords===0)futureWords=sig.split('\n').length;
    }
    distinct += byKey.size;
  }
  tests.push({kind:'exhaustive_initial_three_symbols_all_twelve_append',m,n,pP,rP,pQ,rQ,initialHistories:alpha.length**(m+n),observerFibers:fibers.size,nontrivialFibers:multi,checkedHistories:checked,distinctFutureClassesInNontrivialFibers:distinct,futureWordsPerHistory:futureWords});
}
auditAll(5,3,1,1,1,0,[A,B,C]);
auditAll(6,3,1,0,1,0,[A,B,C]);
auditAll(5,3,0,1,1,0,[A,B,C]);
auditAll(5,3,1,0,1,1,[A,B,C]);
auditAll(6,3,1,1,1,1,[A,B]);
function defect(m,j) {return A.repeat(j-1)+B+A.repeat(m-j);}
function corridor(P,Q,pP,rP,pQ,rQ) {
  const m=P.length,n=Q.length,c=Math.min(m-pP,n-pQ);
  return JSON.stringify([P.slice(c,Math.min(m,n+rQ)),Q.slice(c,Math.min(n,m+rP)),P.slice(-pP-1),Q.slice(-pQ-1)]);
}
let checkedParam=0;
for(let n=4;n<=7;n++)for(let p=1;p<=n-2;p++)for(let m=n+2;m<=n+4;m++) {
  const PCs=Array.from({length:m-2},(_,z)=>defect(m,z+2));
  const Qc=C.repeat(n),Qa=A.repeat(n);
  assert.equal(new Set(PCs.map(P=>observation(P,Qc))).size,1);
  const sigC=new Set(PCs.map(P=>futures(P,Qc,0,1,p,0)));
  const corC=new Set(PCs.map(P=>corridor(P,Qc,0,1,p,0)));
  assert.equal(sigC.size,1);
  assert.equal(corC.size,p+1);
  const PA=PCs.slice(0,n-1);
  assert.equal(new Set(PA.map(P=>observation(P,Qa))).size,1);
  assert.equal(new Set(PA.map(P=>futures(P,Qa,0,1,p,0))).size,p+1);
  const populations = new Map();
  for(const P of PA) {
    const k=quotientKey(P,Qa,0,p,0);
    populations.set(k,(populations.get(k)||0)+1);
  }
  assert.deepEqual([...populations.values()].sort((a,b)=>b-a),[n-p-1,...Array(p).fill(1)].sort((a,b)=>b-a));
  checkedParam++;
}
// One Q APPEND changes the C^n family from a single class to p+rQ+1 classes.
let checkedOneAppend = 0;
for(let n=3;n<=5;n++)for(let p=1;p<=n-2;p++)for(let m=n+3;m<=n+5;m++){
  const PCs=Array.from({length:m-2},(_,z)=>defect(m,z+2)),Q=C.repeat(n);
  const q0=new Set(PCs.map(P=>futures(P,Q,0,1,p,0))).size;
  const q1=new Set(PCs.map(P=>futures(P,Q,0,1,p,1))).size;
  assert.equal(q0,1);
  assert.equal(q1,p+2);
  checkedOneAppend++;
}
// Concrete two-boundary examples with the same current complete observer.
const m=7,n=4,p=1;
const cHist=Array.from({length:5},(_,j)=>defect(m,j+2));
const aHist=cHist.slice(0,3);
assert.equal(new Set(cHist.map(P=>futures(P,C.repeat(n),0,1,p,0))).size,1);
assert.equal(new Set(aHist.map(P=>futures(P,A.repeat(n),0,1,p,0))).size,2);
assert.equal(observation(defect(7,3),A.repeat(4)),observation(defect(7,4),A.repeat(4)));
assert.notEqual(observation(defect(7,3),A.repeat(3)),observation(defect(7,4),A.repeat(3)));
const result={marker:'STAGE438B_PROTECTED_OVERLAP_EXACT_QUOTIENT_PASS',model:'native_X6_12_signed_directions_positive_unit_BRC_K',tests,parameterFamilies:checkedParam,oneAppendTransitionFamilies:checkedOneAppend,compressionWitness:{m:7,n:4,budgets:{pP:0,rP:1,pQ:1,rQ:0},PdefectPositions:[2,3,4,5,6],Q:'cccc',histories:5,corridorStates:2,exactFutureClasses:1},oneAppendWitness:{m:7,n:4,budgets:{pP:0,rP:1,pQ:1,rQ:1},PdefectPositions:[2,3,4,5,6],Q:'cccc',histories:5,exactFutureClasses:3},matchingWitness:{m:7,n:4,budgets:{pP:0,rP:1,pQ:1,rQ:0},PdefectPositions:[2,3,4],Q:'aaaa',histories:3,exactFutureClasses:2,populations:[2,1]}};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
