'use strict';
const assert=require('node:assert/strict');
const n=6,E=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i<j?[i,j]:null)).flat().filter(Boolean);
const dirs=Array.from({length:n},(_,i)=>[[i,1],[i,-1]]).flat();
function data(w){const v=Array(n).fill(0),c=Array.from({length:n},()=>Array(n).fill(0));for(let i=0;i<w.length;i++){const [a,s]=w[i];v[a]+=s;for(let j=0;j<i;j++){const [b,t]=w[j];c[b][a]+=t*s;}}return {v,c,A:E.map(([a,b])=>c[a][b]-c[b][a])};}
function wedge(v,w){return E.map(([i,j])=>v[i]*w[j]-v[j]*w[i]);}
function B(i,j){return [[i,1],[i,-1],[j,1],[j,-1]];}
function L(i,j){return [[i,1],[j,1],[i,-1],[j,-1]];}
function M(i,j){return [[j,1],[i,1],[j,-1],[i,-1]];}
function eq(a,b){assert.deepEqual(a,b);}
function checkWord(w){const x=data(w);E.forEach(([i,j],k)=>{assert((x.A[k]-x.v[i]*x.v[j])%2===0);assert.equal((x.A[k]+x.v[i]*x.v[j])/2,x.c[i][j]);});return x;}
let words=[[]],parityChecks=0;
for(let size=0;size<=4;size++){
 for(const w of words){checkWord(w);parityChecks++;}
 if(size!==4){const next=[];for(const w of words)for(const d of dirs)next.push([...w,d]);words=next;}
}
let composeChecks=0;
const two=[[]];for(const a of dirs)for(const b of dirs)two.push([a,b]);
for(const H of two)for(const K of two){const x=data(H),y=data(K),z=data([...H,...K]),w=wedge(x.v,y.v);E.forEach((e,k)=>assert.equal(z.A[k],x.A[k]+y.A[k]+w[k]));composeChecks++;}
let generatorChecks=0;
for(const [i,j] of E){const b=data(B(i,j)),l=data(L(i,j)),m=data(M(i,j));assert(b.v.every(x=>x===0)&&l.v.every(x=>x===0)&&m.v.every(x=>x===0));E.forEach((p,k)=>{assert.equal(b.A[k],0);assert.equal(l.A[k],p[0]===i&&p[1]===j?2:0);assert.equal(m.A[k],p[0]===i&&p[1]===j?-2:0);});generatorChecks++;}
let modulusChecks=0;const modulus=[];
for(let q=2;q<=10;q++){
 const m0=q%2?q:2*q;
 for(let m=1;m<m0;m++){
  const t=m/(m%2?1:2);assert.equal((2*t)%m,0);assert.notEqual(t%q,0);
  const b=data(Array.from({length:t},()=>B(0,1)).flat()),l=data(Array.from({length:t},()=>L(0,1)).flat());
  eq(b.v,l.v);assert.equal(b.A[0]%m,l.A[0]%m);assert.notEqual(b.c[0][1]%q,l.c[0][1]%q);
  modulusChecks++;
 }
 const g=(a,b)=>b?g(b,a%b):a;assert.equal(m0/g(m0,2)%q,0);
 modulus.push({q,minimal_m:m0,strictly_smaller_moduli_refuted:m0-1});
}
const evidence={schema:'R762DD_VERIFY_V1',task:'RS-X6-TRIADIC-CLOSURE-DYNAMICS',date:'2026-11-17',coverage:{all_signed_words_length_0_to_4:22621,word_parity_checks:parityChecks,composition_pairs:composeChecks,elementary_loop_pairs:generatorChecks,modulus_smaller_counterexamples:modulusChecks},modulus,verification:'PASS',review:'NOT_REVIEWED',scope:'signed native-axis path algebra; no licensed TRIADIC_CLOSURE_E event asserted'};
process.stdout.write(JSON.stringify(evidence,null,2)+'\n');
