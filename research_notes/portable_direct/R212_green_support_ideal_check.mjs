#!/usr/bin/env node
'use strict';
const run = function run(){
 const assert=(x,msg)=>{if(!x)throw Error(msg)};
 const key=x=>JSON.stringify(x),countPerm=(n,j)=>{let x=1n;for(let i=0;i<j;i++)x*=BigInt(n-i);return x};
 const S=(n,r)=>{let rows=Array.from({length:n+1},()=>Array(r+1).fill(0n));rows[0][0]=1n;for(let i=1;i<=n;i++)for(let j=1;j<=Math.min(i,r);j++)rows[i][j]=BigInt(j)*rows[i-1][j]+rows[i-1][j-1];return rows[n][r]};
 const C=(r,L)=>{let v=0n;for(let j=0;j<=Math.min(r,L);j++)v+=S(L+1,j+1);return v};
 const N=n=>{let v=0n;for(let j=0;j<=n;j++)v+=countPerm(n,j);return v};
 const popcount=n=>n.toString(2).split("1").length-1;
 function observe(w,k,L){let s=[];for(const z of w){const p=z%(k+1);if(p){s=s.filter(a=>a!==p);s.push(p)}}return{s,t:w.slice(-L)}}
 function mul(x,y,L){return{s:x.s.filter(z=>!y.s.includes(z)).concat(y.s),t:x.t.concat(y.t).slice(-L)}}
 function enumFull(m,k,L){
  const a=m*(k+1),seen=new Map(),stack=[[]];
  while(stack.length){let w=stack.pop();let z=observe(w,k,L);if(z.t.length===L)seen.set(key(z),z);if(w.length<k+L)for(let i=0;i<a;i++)stack.push([...w,i]);}
  return [...seen.values()];
 }
 let models=0,states=0,rightIdeals=0,leftIdeals=0,operationChecks=0;
 for(let m=1;m<=2;m++)for(let k=0;k<=2;k++)for(let L=1;L<=3;L++){
  let E=enumFull(m,k,L);
  let rIdeals=new Map(),lIdeals=new Map();
  for(const e of E){
   const supp=e.s.reduce((s,z)=>s|(1<<(z-1)),0),r=popcount(supp);
   const right=new Set(),left=new Set();
   for(const f of E){right.add(key(mul(e,f,L)));left.add(key(mul(f,e,L)));operationChecks+=2}
   let rightExpected=0n;for(let u=r;u<=k;u++){
    let comb=1n;for(let j=0;j<u-r;j++)comb=comb*BigInt(k-r-j)/BigInt(j+1);
    rightExpected+=comb*countPerm(u,u)*BigInt(m)**BigInt(L)*C(u,L);
   }
   assert(BigInt(right.size)===rightExpected,`right count ${m},${k},${L}: ${r}`);
   assert(BigInt(left.size)===N(k-r),`left count ${m},${k},${L}: ${r}`);
   const rk=[...right].sort().join("|"),lk=[...left].sort().join("|");
   if(!rIdeals.has(supp))rIdeals.set(supp,rk);
   assert(rIdeals.get(supp)===rk,`right classes by support ${m},${k},${L}`);
   assert(!lIdeals.has(lk),`L singleton violation ${m},${k},${L}`);
   lIdeals.set(lk,e);
   rightIdeals++;leftIdeals++;
  }
  assert(rIdeals.size===2**k,`R classes count ${m},${k},${L}`);
  assert(E.length===Number([...Array(k+1)].reduce((s,_,r)=>s+countPerm(k,r)*BigInt(m)**BigInt(L)*C(r,L),0n)),`total E ${m},${k},${L}`);
  models++;states+=E.length;
 }
 const m=12,k=6,L=2,sizes=[];
 let total=0n;
 for(let r=0;r<=k;r++){
   const perClass=countPerm(r,r)*BigInt(m)**2n*C(r,L);
   let choose=1n;for(let i=0;i<r;i++)choose=choose*BigInt(k-i)/BigInt(i+1);
   let right=0n;for(let u=r;u<=k;u++){
    let choose2=1n;for(let i=0;i<u-r;i++)choose2=choose2*BigInt(k-r-i)/BigInt(i+1);
    right+=choose2*countPerm(u,u)*BigInt(m)**2n*C(u,L);
   }
   sizes.push({support_size:r,R_class_count:String(choose),R_class_size:String(perClass),
     left_ideal_size:String(N(k-r)),right_ideal_size:String(right)});
   total+=choose*perClass;
 }
 assert(total===1407600n,"X6 total band size");
 return{status:"PASS",models,full_tail_states_checked:states,right_ideal_checks:rightIdeals,left_ideal_checks:leftIdeals,semigroup_operations_checked:operationChecks,
 X6:{full_tail_band_size:String(total),number_of_R_classes:64,L_classes:1407600,by_support_size:sizes},
 proof_scope:"all m>=1,k>=0,L>=1; finite exhaustive m=1..2,k=0..2,L=1..3"};
};
console.log(JSON.stringify(run(), null, 2));
