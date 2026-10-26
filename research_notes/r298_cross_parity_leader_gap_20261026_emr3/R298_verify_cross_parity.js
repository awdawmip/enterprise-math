#!/usr/bin/env node
'use strict';
// Source-preserving BRC auxiliary integer verifier; Node >=18; no external dependencies.
function verify(){
  const mon=(i,j,c=1n)=>new Map([[`${i},${j}`,BigInt(c)]]);
  const add=(...ps)=>{const z=new Map();for(const p of ps)for(const [k,v] of p)z.set(k,(z.get(k)||0n)+v);for(const [k,v] of z)if(v===0n)z.delete(k);return z};
  const mul=(a,b)=>{const z=new Map();for(const [k,v] of a){const [i,j]=k.split(',').map(Number);for(const [l,u] of b){const [ii,jj]=l.split(',').map(Number),key=`${i+ii},${j+jj}`;z.set(key,(z.get(key)||0n)+v*u)}}for(const [k,v] of z)if(!v)z.delete(k);return z};
  const neg=(a)=>new Map([...a].map(([k,v])=>[k,-v]));
  const pow=(a,n)=>{let x=mon(0,0);for(let i=0;i<n;i++)x=mul(x,a);return x};
  const y=mon(1,0),w=mon(0,1),one=mon(0,0);
  const H=add(one,neg(y),neg(mul(mon(0,0,2),pow(y,3))),pow(y,4));
  const q=add(mul(y,pow(w,2)),mul(add(pow(y,3),neg(mul(mon(0,0,2),pow(y,2))),neg(one)),w),one);
  const T=add(mul(pow(y,2),pow(w,3)),mul(add(neg(pow(y,3)),pow(y,2),neg(y),one),pow(w,2)),mul(add(one,neg(pow(y,2))),w),y);
  const dminus=add(one,neg(mul(y,w))),dplus=add(one,neg(y),pow(y,2),neg(mul(y,w)));
  const L=add(mul(y,add(dminus,neg(mul(mul(y,pow(w,4)),dplus)))),neg(mul(mul(w,H),add(mul(pow(w,2),dplus),neg(dminus)))));
  const diff=add(L,neg(mul(q,T)));if(diff.size)throw Error("polynomial certificate mismatch "+JSON.stringify([...diff].map(([k,v])=>[k,v.toString()])));
  const edges={0:[[2,-1,-1],[2,1,-1]],1:[[0,-1,-1],[0,1,-1]],2:[[1,1,1],[2,1,-1]]};
  let states=new Map([["0,1,0,0",1n]]),a=[],b=[],samples={},gap_checks=0,good_count=0;
  for(let n=0;n<=220;n++){
    const ct=new Map();for(const [key,count] of states){const [q,e,k]=key.split(',').map(Number);if(q!==0)continue;const kk=`${e},${k}`;ct.set(kk,(ct.get(kk)||0n)+count)}
    const count=(e,k)=>ct.get(`${e},${k}`)||0n;
    if(n%2===0)a.push(count(1,-4)-count(-1,-4));else b.push(count(-1,-3)-count(1,-5));
    if([80,81,82,83,220].includes(n)){
      const w=n%2===0?[1,-4]:[-1,-3],s=n%2===0?[-1,-4]:[1,-5];
      samples[n]={winner_effect:w,second_effect:s,winner_count:String(count(...w)),second_count:String(count(...s)),gap:String(count(...w)-count(...s))}
    }
    if(n>=81){const w=n%2===0?[1,-4]:[-1,-3],s=n%2===0?[-1,-4]:[1,-5];const aa=count(...w),bb=count(...s);let third=0n;for(const [key,v] of ct)if(key!==w.join(',')&&key!==s.join(',')&&v>third)third=v;if(!(aa>bb&&bb>third))throw Error("rank at "+n);good_count++;}
    if(n==220)break;
    const next=new Map();for(const [key,count] of states){const [q,e,k,lastzero]=key.split(',').map(Number);for(let bit=0;bit<=1;bit++){if(bit===0&&lastzero)continue;const [qq,eta,c]=edges[q][bit];const kk=`${qq},${eta*e},${eta*k+c},${bit===0?1:0}`;next.set(kk,(next.get(kk)||0n)+count)}}states=next;
  }
  for(let r=0;r<=108;r++){let rhs=a[r+2]-a[r+1]-(r>=1?2n*a[r-1]:0n)+(r>=2?a[r-2]:0n);if(b[r]!==rhs)throw Error("parity transfer at "+r);gap_checks++}
  for(let r=41;r<=109;r++)if(a[r+1]<2n*a[r])throw Error("prefix doubling fail at "+r);
  if(samples[80].gap!=="-727277462"||samples[81].gap!=="13329931025"||samples[82].gap!=="1985689179")throw Error("known raw source samples mismatch");
  return {schema:"EM_R298_CROSS_PARITY_LEADER_GAP_V1",status:"PASS",scope:"positive ordered six-edge BRC auxiliary counts only",algebraic_certificate:"exact identity L(y,w)=Q(y,w)*T(y,w) over Z[y,w]",source_generator_dependency:"R294 author-side fixed-effect C_m formula, NOT independently admitted",dp_max_n:220,cross_parity_coefficients_checked:gap_checks,top_two_raw_dp_checked_n:"81..220",top_two_raw_dp_layers:good_count,even_gap_doubling_checked_index:"41..110",samples,limitations:"finite DP does not prove N_peak=81; exact all-length parity identity is conditional on R294 source-to-kernel correspondence; no native Source Result or Driver review"};
}
console.log(JSON.stringify(verify(),null,2));
