#!/usr/bin/env node
'use strict';
// Stage428-B — exact integer witness and bounded K-frontier update checks.
const assert=require('node:assert/strict');
const D=Array.from({length:12},(_,j)=>'D'+j);
const A='D0', B='D1', C='D2'; // native +E1,-E1,+E2; 12 signed directions remain distinct
function vec(word){let v=Array(6).fill(0);for(const x of word){const j=D.indexOf(x);assert(j>=0);v[Math.floor(j/2)]+=j%2?-1:1;}return v;}
function edges(word){let j=Array.from({length:12},()=>Array(12).fill(0));for(let k=1;k<word.length;k++)j[D.indexOf(word[k-1])][D.indexOf(word[k])]++;return j;}
function K(p,q){let s=0;for(let k=0;k<Math.min(p.length,q.length);k++)s+=+(p[k]===q[k]);return s;}
function initial(p,q){return JSON.stringify([p.length,q.length,vec(p),vec(q),edges(p),edges(q),K(p,q)]);}
function gadgets(bits,L){let p=[];for(const bit of bits){p.push(...(bit? [A,B,A,A,A]:[A,A,A,B,A]));}return p.concat(Array(L).fill(A));}
function lowerBound(){let observed=0,maxB=10, all=[];
 for(const L of [1,3,7]) for(let b=1;b<=maxB;b++) {
   const signatures=new Set();let ref=null;
   for(let mask=0;mask<(1<<b);mask++){
     let bits=Array.from({length:b},(_,j)=>(mask>>j)&1),p=gadgets(bits,L),q=[A];
     let o=initial(p,q);if(ref===null)ref=o;else assert.equal(o,ref);
     const trace=[K(p,q)];for(let k=2;k<=5*b;k++){q.push(A);trace.push(K(p,q));}
     assert.equal(trace.at(-1),4*b);
     const key=trace.join(',');assert(!signatures.has(key),'future-trace collision');signatures.add(key);
     assert.equal(p.length-q.length,L);
     observed++;
   }
   assert.equal(signatures.size,1<<b);
   all.push({b,L,width:5*b-1,distinct_carriers:signatures.size,minimum_binary_bits:b});
 }
 return {range_b:[1,maxB],suffixes:[1,3,7],all_fibers:all,enumerated_histories:observed};
}
function sharpW(){let checked=0;
 for(let n=1;n<=128;n++)for(let L of [1,7,31]){
   let prefix=Array(n-1).fill(A),p=prefix.concat([A,A,A,B,A],Array(L).fill(A)),p2=prefix.concat([A,B,A,A,A],Array(L).fill(A)),q=Array(n).fill(A);
   assert.equal(initial(p,q),initial(p2,q));
   assert.deepEqual(p.slice(-L),p2.slice(-L));
   assert(p.length-q.length>=3);
   let c=Math.min(p.length,n-1),h=Math.min(p.length,n+1),W=h-c;
   assert.equal(W,2);
   let q2=q.concat(A);
   assert.equal(K(p,q2),n+1);assert.equal(K(p2,q2),n);
   checked++;
 }
 return {profiles_checked:checked,n_range:[1,128],L_values:[1,7,31],W:2,append_distinguishes:true};
}
function updateLaw(oldP,oldQ,newP,newQ){let oldH=Math.min(oldP.length,oldQ.length),newH=Math.min(newP.length,newQ.length),oldK=K(oldP,oldQ),value=oldK;
 if(newH>oldH)for(let i=oldH;i<newH;i++)value+=+(newP[i]===newQ[i]);
 else if(newH<oldH)for(let i=newH;i<oldH;i++)value-=+(oldP[i]===oldQ[i]);
 return {value,compared:Math.abs(newH-oldH)};
}
function checkTransition(p,q,p2,q2){let {value,compared}=updateLaw(p,q,p2,q2);assert.equal(value,K(p2,q2));assert(compared<=2);return compared;}
function verifyBoundary(){const alphabet=[A,B,C];let states=0,transitions=0,comparisons=0;
 function words(len){let a=[[]];for(let i=0;i<len;i++)a=a.flatMap(w=>alphabet.map(x=>w.concat(x)));return a;}
 let full=[[],...Array.from({length:4},(_,i)=>words(i+1)).flat()];
 for(const p of full)for(const q of full){states++;
   for(const x of D){comparisons+=checkTransition(p,q,p.concat(x),q);transitions++;
     comparisons+=checkTransition(p,q,p,q.concat(x));transitions++;
     for(const y of D){comparisons+=checkTransition(p,q,p.concat(x),q.concat(y));transitions++;}
   }
   if(p.length){comparisons+=checkTransition(p,q,p.slice(0,-1),q);transitions++;}
   if(q.length){comparisons+=checkTransition(p,q,p,q.slice(0,-1));transitions++;}
   if(p.length&&q.length){comparisons+=checkTransition(p,q,p.slice(0,-1),q.slice(0,-1));transitions++;}
   const inv=x=>D.indexOf(x)^1;
   if(p.length>=2&&q.length>=2&&p.at(-2)===D[inv(p.at(-1))]&&q.at(-2)===D[inv(q.at(-1))]){
     comparisons+=checkTransition(p,q,p.slice(0,-2),q.slice(0,-2));transitions++;
   }
 }
 return {word_pairs:states,legal_transition_checks:transitions,boundary_comparisons:comparisons,alphabet_size:12,word_generation_alphabet_size:3,max_initial_length:4};
}
function main(){const res={marker:'STAGE428B_SHARP_CORRIDOR_ENTROPY_PASS',frozen_science:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',em:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},arithmetic:'exact signed integer vectors, integer directed edge counts, integer K and exact Boolean equality',sharp_asymmetric_profile:sharpW(),trace_entropy:lowerBound(),constant_cost_boundary_law:verifyBoundary(),scope:'finite exact cross-check; general n,L,b bounds and carrier lower bound follow from symbolic proof; native X6 typed path observer only; not physical heartbeat evolution; not native admitted'};console.log(JSON.stringify(res,null,2));}
if(require.main===module)main();
module.exports={K,vec,edges,initial,gadgets,updateLaw,main};
