// X6 R61: exact positive-branch repeated-A star moments and sharp lower-bound witnesses.
// Requires Node.js 18+; no dependencies.
'use strict';
const assert = require('node:assert/strict');
function fact(n) { let x = 1n; for (let j=2; j<=n; j++) x*=BigInt(j); return x; }
function choose(n,k) { let x=1n; for(let i=1;i<=k;i++) x=x*BigInt(n-i+1)/BigInt(i); return x; }
function fall(n,k) { let x=1n; for(let i=0;i<k;i++) x*=BigInt(n-i); return x; }
function moment(rows,t) { return rows.reduce((a,d)=>a+BigInt(d)**BigInt(t),0n); }
function inverse(m,D) {
  const s=Array.from({length:D+1},()=>Array(D+1).fill(0n)); s[0][0]=1n;
  for(let k=1;k<=D;k++) for(let j=1;j<=k;j++)
    s[k][j]=s[k-1][j-1]-BigInt(k-1)*s[k-1][j];
  const F=Array(D+1).fill(0n);
  for(let k=0;k<=D;k++) for(let j=0;j<=k;j++) F[k]+=s[k][j]*m[j];
  const c=Array(D+1).fill(0n);
  for(let k=D;k>=0;k--) {
    let residual=F[k]; for(let d=k+1;d<=D;d++) residual-=c[d]*fall(d,k);
    assert.equal(residual%fact(k),0n);
    c[k]=residual/fact(k); assert(c[k]>=0n);
  }
  return c;
}
let graphs=0;
for (let p=1;p<=3;p++) {
  const total=2**(p*p);
  for(let mask=0;mask<total;mask++) {
    const rows=Array(p).fill(0);
    for(let i=0;i<p;i++) for(let j=0;j<p;j++)
      rows[i]+=(mask>>(i*p+j))&1;
    const m=Array.from({length:p+1},(_,t)=>moment(rows,t));
    const recovered=inverse(m,p);
    const expected=Array.from({length:p+1},(_,d)=>BigInt(rows.filter(r=>r===d).length));
    assert.deepEqual(recovered,expected);
    graphs++;
  }
}
let witnesses=0;
let sample=null;
for(let D=1;D<=10;D++) {
  const p=2**(D-1);
  let even=[],odd=[];
  for(let d=0;d<=D;d++) for(let j=0n;j<choose(D,d);j++) {
    (d%2===0?even:odd).push(d);
  }
  assert.equal(even.length,p); assert.equal(odd.length,p); assert(p>=D);
  for(let t=0;t<D;t++) assert.equal(moment(even,t),moment(odd,t));
  const delta=moment(even,D)-moment(odd,D);
  assert.equal(delta,BigInt((D%2===0?1:-1))*fact(D));
  assert.deepEqual(inverse(Array.from({length:D+1},(_,t)=>moment(even,t)),D),
    Array.from({length:D+1},(_,d)=>BigInt(even.filter(r=>r===d).length)));
  assert.deepEqual(inverse(Array.from({length:D+1},(_,t)=>moment(odd,t)),D),
    Array.from({length:D+1},(_,d)=>BigInt(odd.filter(r=>r===d).length)));
  if(D===4) sample={D,p,even_hist:[1,0,6,0,1],odd_hist:[0,4,0,4,0],moments_even:Array.from({length:5},(_,t)=>moment(even,t).toString()),moments_odd:Array.from({length:5},(_,t)=>moment(odd,t).toString())};
  witnesses++;
}
console.log(JSON.stringify({status:'PASS',enumerated_binary_graphs:graphs,degree_bound_witnesses:witnesses,range_graph_p:[1,3],range_delta:[1,10],sample,scope:'exact integer arithmetic; conditional AB reset and repeated-A-port equality, not native triadic admission'},null,2));
