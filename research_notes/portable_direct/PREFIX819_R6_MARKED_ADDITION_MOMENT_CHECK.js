'use strict';
// Exact single-marked-addition BRC future-count trace and conditional-moment regression.
const run=function run(){
const ck=(p,m)=>{if(!p)throw Error(m)};
const bc=x=>{let k=0;while(x){x&=x-1;k++}return k};
const esym=arr=>{let a=[1n];for(const v of arr){let n=Array(a.length+1).fill(0n);for(let j=0;j<a.length;j++){n[j]+=a[j];n[j+1]+=a[j]*BigInt(v)}a=n}return a};
const ss=(m,q)=>Array.from({length:2**m},(_,i)=>i).filter(x=>bc(x)<=q);
function named(m,q,beta,j,alpha,initial,H){
 let masses=new Map([[initial,1n]]),out=[];
 for(let h=0;h<=H;h++){
  const counts=Array(q+1).fill(0n);
  for(const [s,w]of masses)counts[bc(s)]+=w;
  out.push(counts);
  let next=new Map();
  for(const [s,w]of masses){
   for(let i=0;i<m;i++){
    const has=!!(s&(2**i)),rate=has?beta[i]:(i===j&&bc(s)<q?alpha:0);
    if(rate){let t=s^(2**i);next.set(t,(next.get(t)||0n)+w*BigInt(rate))}
   }
  }
  masses=next;
 }
 return out;
}
function compressed(m,q,beta,j,alpha,initial,H){
 let M=[0,1].map(z=>Array.from({length:Math.max(0,q-z+1)},(_,k)=>Array(k+1).fill(0n)));
 const z=+(!!(initial&(2**j))),unmarked=[];for(let i=0;i<m;i++)if(i!==j&&(initial&(2**i)))unmarked.push(beta[i]);
 M[z][unmarked.length]=esym(unmarked);
 const out=[];
 for(let step=0;step<=H;step++){
  out.push(Array.from({length:q+1},(_,k)=>(M[0][k]?.[0]||0n)+(k>=1?(M[1][k-1]?.[0]||0n):0n)));
  let N=[0,1].map(z=>Array.from({length:Math.max(0,q-z+1)},(_,k)=>Array(k+1).fill(0n)));
  for(let z=0;z<=1;z++)for(let k=0;k<M[z].length-1;k++)for(let h=0;h<=k;h++)
   N[z][k][h]+=BigInt(h+1)*M[z][k+1][h+1];
  for(let k=0;k<M[1].length;k++)for(let h=0;h<=k;h++)N[0][k][h]+=BigInt(beta[j])*M[1][k][h];
  for(let k=0;k<M[1].length;k++)for(let h=0;h<=k;h++)N[1][k][h]+=BigInt(alpha)*M[0][k][h];
  M=N;
 }
 return out;
}
const eq=(a,b)=>a.length===b.length&&a.every((x,i)=>x===b[i]);
let r={schema:"PREFIX819_R6_EXACT_REGRESSION_V1",arithmetic:"BigInt",cases:0,initial_named_states:0,horizon_histogram_matches:0,explicit_witness_validated:false};
for(let m=1;m<=7;m++)for(let q=0;q<=Math.min(m,4);q++)for(let pat=0;pat<3;pat++)for(let mark of new Set([0,m-1]))for(let alpha=1;alpha<=3;alpha++){
 const beta=Array.from({length:m},(_,i)=>pat===0?i+1:pat===1?2*i+3:m+1-i);
 for(const s of ss(m,q)){
  let a=named(m,q,beta,mark,alpha,s,q+3);
  let b=compressed(m,q,beta,mark,alpha,s,q+3);
  for(let h=0;h<=q+3;h++){ck(eq(a[h],b[h]),"marker moment mismatch "+[m,q,pat,mark,alpha,s,h]);r.horizon_histogram_matches++}
  r.initial_named_states++;
 }
 r.cases++;
}
const m=3,q=2,bet=[1,2,3],j=0,alpha=1;
function mix(list){
 const outs=Array.from({length:2},()=>Array(q+1).fill(0n));
 for(let v=0;v<list.length;v+=2){
  const s=list[v],cnt=BigInt(list[v+1]),tr=named(m,q,bet,j,alpha,s,1);
  for(let h=0;h<=1;h++)for(let k=0;k<=q;k++)outs[h][k]+=cnt*tr[h][k];
 }
 return outs;
}
const A=mix([1,1,4,1]),B=mix([2,2]);
ck(eq(A[0],B[0]),"witness initial different");
ck(A[1][2]===1n&&B[1][2]===2n&&A[1][0]===B[1][0]&&A[1][0]===4n,"witness future mismatch");
r.explicit_witness={m,q,alpha_j:alpha,marked_branch:1,beta:bet,mu:{"{1}":1,"{3}":1},nu:{"{2}":2},old_pure_removal_moments:{M_1_0:2,M_1_1:4},h0_count_hist:[0,2,0],h1_mu:[4,0,1],h1_nu:[4,0,2]};
r.explicit_witness_validated=true;r.all_exact_assertions_passed=true;
return r;
};
process.stdout.write(JSON.stringify(run(),null,2)+'\n');
