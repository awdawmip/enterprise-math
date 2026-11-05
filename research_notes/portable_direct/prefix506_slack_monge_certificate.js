"use strict";
// PREFIX-506: standalone, exact safe-integer certificate for slack-Monge block optimizer.
// Node 22: node prefix506_slack_monge_certificate.js
function sums(k) {
 const f=[0],t=[0]; k.forEach((w,i)=>{f.push(f.at(-1)+w);t.push(t.at(-1)+(i+1)*w)});return {f,t};
}
function cost(p,i,j){return p.t[j]-p.t[i]-i*(p.f[j]-p.f[i]);}
function optimize(k,b){
 const L=k.length; b=Math.min(L,b); const B=Math.ceil(L/b),r=B*b-L,p=sums(k);
 let prev=Array(r+1).fill(null);prev[0]=0;const back=[];let trials=0;
 for(let a=1;a<=B;a++){
   const dp=Array(r+1).fill(null),ptr=Array(r+1).fill(null),beg=a===B?r:0;
   function solve(lo,hi,optlo,opthi){
     if(lo>hi)return;
     const s=(lo+hi)>>1,j=a*b-s;let best=null,bst=null;
     for(let t=optlo;t<=Math.min(opthi,s);t++){
       if(prev[t]===null)continue;
       const i=(a-1)*b-t,v=prev[t]+cost(p,i,j);trials++;
       if(best===null||v<best||(v===best&&t<bst)){best=v;bst=t;}
     }
     if(bst===null)throw Error('unreachable state');
     dp[s]=best;ptr[s]=bst;
     solve(lo,s-1,optlo,bst);solve(s+1,hi,bst,opthi);
   }
   solve(beg,r,0,r);prev=dp;back.push(ptr);
 }
 let slack=r,cuts=[L];for(let a=B;a>0;a--){slack=back[a-1][slack];cuts.push((a-1)*b-slack)}cuts.reverse();
 return {cost:prev[r],cuts,trials,B,r};
}
function direct(k,b){
 const L=k.length;b=Math.min(L,b);const B=Math.ceil(L/b),p=sums(k);
 let prev=Array(L+1).fill(null);prev[0]=0;
 for(let a=1;a<=B;a++){
   let cur=Array(L+1).fill(null);
   for(let j=a;j<=L;j++)for(let i=Math.max(a-1,j-b);i<j;i++)if(prev[i]!==null){
     let v=prev[i]+cost(p,i,j);if(cur[j]===null||v<cur[j])cur[j]=v;
   }
   prev=cur;
 }
 return prev[L];
}
function exhaustive(k,b){
 const L=k.length,p=sums(k);b=Math.min(L,b);const B=Math.ceil(L/b);let best=null,count=0;
 function visit(i,a,v){
   if(a===B){if(i===L){count++;best=best===null?v:Math.min(v,best)}return;}
   let left=B-a-1;
   for(let j=i+1;j<=Math.min(L,i+b);j++)if(left<=L-j&&L-j<=left*b)
     visit(j,a+1,v+cost(p,i,j));
 }
 visit(0,0,0);return {best,count};
}
let seed=506;
function next(){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;}
let cases=0,exhaustiveCases=0,largeCases=0,maxTrials=0;
for(const L of [...Array.from({length:26},(_,i)=>i+1),32,56,65,97,144]){
 for(const b of [1,2,3,4,5,7,9,13,24,L,L+4])for(let pattern=0;pattern<4;pattern++){
   const k=Array.from({length:L},(_,i)=>pattern===0?0:pattern===1?(i%7===0?11:0):pattern===2?next()%16:(i%3===0?next()%1000:0));
   const x=optimize(k,b),y=L<=12?exhaustive(k,b).best:direct(k,b);
   if(x.cost!==y||x.cuts.length!==x.B+1||x.cuts[0]!==0||x.cuts.at(-1)!==L)throw Error('optimality');
   if(x.cuts.some((v,i)=>i&&!(v>x.cuts[i-1]&&v-x.cuts[i-1]<=b)))throw Error('block width');
   const p=sums(k),real=x.cuts.slice(1).reduce((a,v,j)=>a+cost(p,x.cuts[j],v),0);
   if(real!==x.cost)throw Error('backtracking');
   const rankPrefix=[0];for(let i=0;i<L;i++)rankPrefix.push(rankPrefix.at(-1)+k[i]);
   // Every positive-weight state has one and only one rank and inverse V label.
   for(let v=0;v<L;v++)for(let q=0;q<k[v];q++){
     const r=rankPrefix[v]+q;let found=-1;
     for(let h=0;h<L;h++)if(rankPrefix[h]<=r&&r<rankPrefix[h+1]){found=h;break;}
     if(found!==v)throw Error('inverse V');
   }
   cases++;maxTrials=Math.max(maxTrials,x.trials);
   if(L<=12)exhaustiveCases++;else largeCases++;
 }
}
console.log(JSON.stringify({research:'PREFIX-506',status:'ALL_CHECKS_PASS',arithmetic:'JavaScript exact safe integers under tested bounds',cases,exhaustiveCases,largeCases,maxTrials,source:'standalone synthetic certificate; extended native X6 Python certificate is separately bundled'},null,2));
