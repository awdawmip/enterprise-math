'use strict';
// Exact integer verification of the R62 bounded-degree, truncated-moment lattice theorem.
const assert = require('node:assert/strict');
function choose(n,k){if(k<0||k>n)return 0n;let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-i+1)/BigInt(i);return a;}
function pow(a,e){let b=1n;for(let j=0;j<e;j++)b*=BigInt(a);return b;}
function fac(n){let a=1n;for(let i=2;i<=n;i++)a*=BigInt(i);return a;}
function moments(c,D){return Array.from({length:D+1},(_,t)=>c.reduce((s,x,d)=>s+BigInt(x)*pow(d,t),0n));}
function signedStirling(D){let s=[[1n]];for(let k=1;k<=D;k++){let row=Array(k+1).fill(0n);for(let j=0;j<=k;j++)row[j]=(j? s[k-1][j-1]:0n) - (j<k?BigInt(k-1)*s[k-1][j]:0n);s.push(row);}return s;}
function interval(m,D,p){const s=signedStirling(D),B=[];for(let j=0;j<D;j++){let F=0n;for(let t=0;t<=j;t++)F+=s[j][t]*m[t];assert.equal(F%fac(j),0n);B.push(F/fac(j));}
 const c0=[];for(let k=0;k<D;k++){let z=0n;for(let j=k;j<D;j++)z+= ((j-k)%2?-1n:1n)*choose(j,k)*B[j];c0.push(z);}c0.push(0n);
 let L=0n,U=BigInt(p);for(let k=0;k<D;k++){const b=choose(D,k),a=c0[k];if((D-k)%2===0){while(a+b*L<0n)L++;}else{const v=a/b; // floor division for nonnegative a only; negative a already yields no feasible nonnegative solution.
 if(a<0n)U=-1n;else if(v<U)U=v;}}
 return {L,U,c0,vector:z=>c0.map((a,k)=>a+((D-k)%2?-1n:1n)*choose(D,k)*z)};
}
function* hist(D,p,prefix=[]){if(D===0){yield [...prefix,p];return;}for(let i=0;i<=p;i++)yield* hist(D-1,p-i,[...prefix,i]);}
function sig(m,D){return m.slice(0,D).join(',');}
const checks=[];let histograms=0, ambiguous=0, failures=0;
for(let D=1;D<=6;D++)for(let p=D;p<=Math.min(9,D+4);p++){
 const groups=new Map();let count=0;
 for(const c of hist(D,p)){
  count++;histograms++;
  const m=moments(c,D), inv=interval(m,D,p);
  const z=BigInt(c[D]);assert(inv.L<=z && z<=inv.U);
  assert.deepEqual(inv.vector(z).map(Number),c);
  const key=sig(m,D);const arr=groups.get(key)||[];arr.push({c,m,inv});groups.set(key,arr);
 }
 let thisAmb=0;
 for(const arr of groups.values()){
  const {L,U}=arr[0].inv;
  assert.equal(Number(U-L+1n),arr.length);
  if(arr.length>1){thisAmb++;ambiguous++;const a=arr[0].m[D],b=arr[1].m[D];assert.equal((a-b<0n?b-a:a-b),fac(D));}
  if(p < 2**(D-1))assert.equal(arr.length,1);
 }
 checks.push({D,p,histograms:count,ambiguous_prefix_classes:thisAmb});
}
for(let D=1;D<=10;D++){
 const p=Math.max(D,2**(D-1)); const even=Array(D+1).fill(0),odd=Array(D+1).fill(0);
 for(let j=0;j<=D;j++)(j%2?odd:even)[j]=Number(choose(D,j));
 even[0]+=p-2**(D-1);odd[0]+=p-2**(D-1);
 const e=moments(even,D),o=moments(odd,D);
 for(let t=0;t<D;t++)assert.equal(e[t],o[t]);
 assert.equal(e[D]-o[D],(D%2?-1n:1n)*fac(D));
}
const example={D:4,p:8,even:[1,0,6,0,1],odd:[0,4,0,4,0]};
example.even_moments=moments(example.even,4).map(String);
example.odd_moments=moments(example.odd,4).map(String);
example.prefix_feasible_range=Object.fromEntries(Object.entries(interval(moments(example.even,4),4,8)).filter(([k])=>['L','U'].includes(k)).map(([k,v])=>[k,v.toString()]));
const result={schema:'ENTERPRISE_MATH_X6_R62_MOMENT_LATTICE_EXACT_CHECK_V1',date:'2026-11-20',test_scope:'All histograms with 1<=D<=6, D<=p<=min(9,D+4); Prouhet pairs D=1..10',checks,total_histograms:histograms,ambiguous_prefix_classes:ambiguous,sharpness_cases:10,example,pass:true};
process.stdout.write(JSON.stringify(result,null,2)+'\n');
