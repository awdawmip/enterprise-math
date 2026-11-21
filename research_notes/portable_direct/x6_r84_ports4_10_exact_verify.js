'use strict';
// R84 exact integer proof, conditional 4-channel BRC star observer.
const assert=require('node:assert/strict');
const V={
u1:[[1,0,0],[2,1,1,4]],u3:[[3,-1,0],[1,1,9,38]],u4m:[[1,3,-1],[1,1,3,1]],
s4:[[3,-4,1],[7,7,1,1]],t4:[[4,-1,0],[1,7,1,7]],u5:[[3,2,-1],[26,1,1,61]],
s5:[[4,-4,1],[1,1,4,1]],t5:[[5,-1,0],[1,2,2,2]],s6:[[5,-4,1],[2,1,4,10]],
t6:[[6,-1,0],[3,1,1,1]],s7m:[[3,-7,2],[1,7,19,1]],s7:[[6,-4,1],[1,1,4,24]],
t7:[[7,-1,0],[20,9,1,2]],s9:[[7,2,-1],[2,22,21,1]],s10:[[9,-5,1],[1,1,1,2]]};
const S={
4:['u1','u3','u4m','s4','t4'],
5:['u1','u3','s4','t4','u5','s5','t5'],
6:['u1','u3','s4','t4','u5','s5','t5','s6','t6'],
7:['u1','s4','t4','s5','t5','s6','t6','s7m','s7','t7'],
8:['u1','s4','t4','s5','t5','s6','t6','s7m','s7','t7'],
9:['u1','s4','t4','s5','t5','s6','t6','s7m','s7','t7','s9'],
10:['u1','s4','t4','s5','t5','s6','t6','s7m','s7','t7','s9','s10']};
function q(a){return Math.max(a.reduce((s,x)=>s+Math.max(x,0),0),a.reduce((s,x)=>s+Math.max(-x,0),0));}
function g(a){const [x,y,z]=a,v=[0,2*x+6*y+12*z,6*x+24*y+60*z,14*x+78*y+252*z];
return [0,1,2].flatMap(i=>Array.from({length:3-i},(_,k)=>Math.abs(v[i]-v[i+k+1])/2));}
const den=w=>[w[0]+w[1],w[0]+w[2],w[0]+w[3],w[1]+w[2],w[1]+w[3],w[2]+w[3]];
function F(a,w){const G=g(a),D=den(w);let n=BigInt(G[0]),d=BigInt(D[0]);
for(let i=1;i<6;i++){let x=BigInt(G[i]),y=BigInt(D[i]);if(x*d>n*y){n=x;d=y;}}return [n,d];}
const cmp=(x,y)=>x[0]*y[1]-y[0]*x[1];
function gcd(x,y){while(y){[x,y]=[y,x%y]}return x;}
function fmt([n,d]){const z=gcd(n,d);return String(n/z)+'/'+String(d/z);}
function* domain(p){for(let x=-p;x<=p;x++)for(let y=-p;y<=p;y++)for(let z=-p;z<=p;z++){
const a=[x,y,z],k=a.find(t=>t!==0);if(k===undefined||k<0||q(a)>p)continue;yield a;}}
const out={schema:'X6_R84_LOW_PORT_EXACT_V1',model:'conditional degree-four BRC histogram with common additive bias',frozen_p000:'a72226e2430ffa4786321ac86e7f0c599d5f0389',vectors:V,cores:S,checks:{}};
for(let p=4;p<=10;p++){
const pool=[...domain(p)],ids=S[p],counts=ids.map(()=>0),winners=[];
for(const a of pool){const G=g(a),i=ids.findIndex(k=>g(V[k][0]).every((t,j)=>t<=G[j]));assert(i>=0,'gap uncovered p='+p+', a='+a);counts[i]++;}
for(const id of ids){const [a,w]=V[id];assert(q(a)<=p);const v=F(a,w);let equal=0,better=0,next=null;
for(const b of pool){const cost=F(b,w),c=cmp(cost,v);
if(c===0n)equal++;else if(c<0n)better++;else if(next===null||cmp(cost,next)<0n)next=cost;}
assert.equal(equal,1,'nonunique p='+p+', id='+id);assert.equal(better,0,'better p='+p+', id='+id);
winners.push({id,w,eta:fmt(v),runner_up:fmt(next)});}
out.checks[p]={unoriented:pool.length,minimum_core:ids.length,first_domination_allocation:counts,unique_winner_checks:winners};
}
console.log(JSON.stringify(out,null,2));