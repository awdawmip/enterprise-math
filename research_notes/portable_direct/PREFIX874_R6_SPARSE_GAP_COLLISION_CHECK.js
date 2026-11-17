"use strict";
// PREFIX-874: exact single-toggle collisions for two fixed odd moduli.
// Usage: node PREFIX874_R6_SPARSE_GAP_COLLISION_CHECK.js
const bit=(x,i)=>Math.floor(x/2**i)%2;
function witness(p,a,b){
 let B=Math.ceil(Math.log2(a+1)),d=a-b;
 for(let i=1;i<B;i++) if(d===2**i){
  let u=bit(a,i)?0:2**i;return [[u,u],[u+a,u+b]];
 }
 for(let i=2;i<B;i++)for(let j=1;j<i;j++)if(d===2**i+2**j){
  let u=bit(a,i)?0:2**i;return [[u,u+2**j],[u+a,u+b+2**j]];
 }
 for(let i=2;i<=B;i++)for(let j=1;j<i;j++)if(d===2**i-2**j){
  let u=2**j;if(!bit(u+a,i))u+=2**i;
  return [[u,u-2**j],[u+a,u+b-2**j]];
 }
 return null;
}
function verify(p,a,b){
 let w=witness(p,a,b);if(!w)return false;
 const [[u,v],[U,V]]=w;
 const valid=([x,y])=>x>=0&&y>=0&&x<2**p&&y<2**p&&
  ((x^y)===0||(((x^y)&((x^y)-1))===0));
 if(!valid(w[0])||!valid(w[1])||u===U||
     u%a!==U%a||v%b!==V%b)throw Error(JSON.stringify({p,a,b,w}));
 return true;
}
function gaps(B){
 let D=new Set();
 for(let i=1;i<B;i++)D.add(2**i);
 for(let i=2;i<B;i++)for(let j=1;j<i;j++)D.add(2**i+2**j);
 for(let i=2;i<=B;i++)for(let j=1;j<i;j++)D.add(2**i-2**j);
 return [...D].sort((x,y)=>x-y);
}
function main(){
 let small=[];
 for(const [p,B] of [[7,5],[8,6],[9,7]]){
  let Q=2**B-1,D=new Set(gaps(B)),n=0;
  for(let a=3;a<=Q;a+=2)for(let b=1;b<a;b+=2)
   if(D.has(a-b)){verify(p,a,b);n++;}
  if(n*2!==2**(B-2)*(4*B*B-24*B+50)-16)throw Error("count");
  small.push({p,B,unordered:n,ordered:2*n});
 }
 let B=19,Q=2**B-1,D=gaps(B),
     sum=D.reduce((s,d)=>s+d,0),
     total=D.reduce((s,d)=>s+2**B-d,0),samples=0;
 if(D.length!==307||sum!==24903696||total!==136052720)
  throw Error("formula");
 for(let d of D)for(let k=0;k<=32;k++){
  let a=d+1+2*Math.floor(((Q-d-1)/2)*k/32);
  verify(32,a,a-d);samples++;
 }
 return {status:"ALL_EXACT_ASSERTIONS_PASSED",p:32,B,
  differences:D.length,sum,excluded_ordered_pairs:total,
  high_first_samples:samples,small};
}
if(require.main===module)console.log(JSON.stringify(main(),null,2));
module.exports={witness,verify,gaps,main};
