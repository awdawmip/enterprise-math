'use strict';
// R762DC, 2026-11-17: exact finite symbolic checks for signed X6 pair-area diagnostic frame horizons.
const assert = require('node:assert/strict');
const n = 6;
const E0 = [[0,1],[1,2],[0,2]];
const cyc = Array.from({length:n},(_,i)=>(i+1)%n);
const swap = Array.from({length:n},(_,i)=>i); [swap[0],swap[1]]=[swap[1],swap[0]];
const id = Array.from({length:n},(_,i)=>i);
const pair=(a,b)=>[Math.min(a,b),Math.max(a,b)].join('-');
function framePairs(p){return E0.map(([a,b])=>pair(p[a],p[b]));}
function apply(g,p){return g.map(i=>p[i]);} // new axis labels for old chart axes
function cyclicCover(){const sets=[],covered=new Set();let p=id;for(let h=0;h<=6;h++){framePairs(p).forEach(x=>covered.add(x));sets.push(covered.size);p=apply(cyc,p);}return sets;}
function twoGeneratorCover(){const seen=new Set(),frontiers=[];let layer=[id],covered=new Set();seen.add(id.join(','));for(let h=0;h<=10;h++){frontiers.push(layer.length);layer.forEach(p=>framePairs(p).forEach(x=>covered.add(x)));if(covered.size===15)return {firstFull:h,frontiers,covered:covered.size};const next=[];for(const p of layer)for(const gen of [cyc,swap]){const v=apply(p,gen),k=v.join(',');if(!seen.has(k)){seen.add(k);next.push(v);}}layer=next;}throw Error('No full cover');}
function area(word){const c=Array.from({length:n},()=>Array(n).fill(0));for(let a=0;a<word.length;a++)for(let b=a+1;b<word.length;b++){let [i,si]=word[a],[j,sj]=word[b];if(i<j)c[i][j]+=si*sj;}return c;}
function B(i,j){return [[i,1],[i,-1],[j,1],[j,-1]];}
function L(i,j){return [[i,1],[j,1],[i,-1],[j,-1]];}
function hist(word){const a=Array.from({length:n},()=>[0,0]);for(const [i,s] of word)a[i][s===1?0:1]++;return a;}
let unitChecks=0;
for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
  const b=B(i,j),l=L(i,j),base=area(b),changed=area(l);
  assert.equal(b.length,4);assert.deepEqual(hist(b),hist(l));
  for(let a=0;a<n;a++)for(let z=a+1;z<n;z++){
    assert.equal(base[a][z],0);assert.equal(changed[a][z],a===i&&z===j?1:0);unitChecks+=2;
  }
}
function rotateWord(word,p){return word.map(([i,s])=>[p[i],s]);}
let covarianceChecks=0;
for(let a=0;a<n;a++)for(let b=a+1;b<n;b++)for(const p of [id,cyc,swap]){
  let raw=area(L(a,b)),trans=area(rotateWord(L(a,b),p));
  for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
    const x=p[i],y=p[j],left=x<y?trans[x][y]:-trans[y][x];
    assert(left===raw[i][j]);covarianceChecks++;
  }
}
assert.deepEqual(cyclicCover(),[3,5,7,9,11,12,12]);
const two=twoGeneratorCover();assert.equal(two.firstFull,5);assert.deepEqual(two.frontiers,[1,2,3,5,8,13]);
let witnessChecks=0;
for(let q=2;q<=5;q++)for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let t=0;t<q;t++){
  const words=Array.from({length:q},(_,s)=>s<t?L(i,j):B(i,j)).flat();
  const c=area(words);const hs=hist(words);
  assert.equal(words.length,4*q);
  for(let a=0;a<n;a++)for(let b=a+1;b<n;b++)assert.equal(((c[a][b]%q)+q)%q,a===i&&b===j?t:0);
  for(let k=0;k<n;k++)assert.deepEqual(hs[k],k===i||k===j?[q,q]:[0,0]);
  witnessChecks++;
}
function signatureCheck(q,d){
  const seen=new Set(); const count=q**d;
  for(let z=0;z<count;z++){
    let x=z,signature='';
    for(let k=0;k<d;k++){
      const val=x%q;x=Math.floor(x/q);
      for(let p=0;p<q;p++)signature+=((val+p)%q===0?'1':'0');
    }
    assert(!seen.has(signature));seen.add(signature);
  }
  return seen.size;
}
const signatures={q2d12:signatureCheck(2,12),q3d8:signatureCheck(3,8)};
const evidence={schema:'R762DC_VERIFY_V1',date:'2026-11-17',task:'RS-X6-TRIADIC-CLOSURE-DYNAMICS',proof_scope:'conditional passive S6 signed-frame pair-area diagnostic; not native TRIADIC_CLOSURE_E event licence',cycle_cover:cyclicCover(),cycle_plus_swap:two,unit_checks:unitChecks,covariance_checks:covarianceChecks,witness_checks:witnessChecks,unique_signatures:signatures,verified:'PASS',review:'NOT_REVIEWED'};
process.stdout.write(JSON.stringify(evidence,null,2)+'\n');
