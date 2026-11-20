"use strict";
// Stage455-B: native X6 BRC grouped C/T/U exact counter and signed POP-only checker.
// Original binary letters: 0=+E1, 1=-E1. Endpoints 0, nonadjacent defects.
function add(M,k,v){M.set(k,(M.get(k)||0n)+v)}
const ky=JSON.stringify,pa=JSON.parse,Tcache=new Map(),Ucache=new Map();
function geom(m,n,pP,pQ,rP,rQ){
 const a=Math.min(pP,m),b=Math.min(pQ,n),c=Math.min(m-a,n-b);
 if(m<2||n<=m||pP<1||c>=m||c<0)throw Error("implemented regime");
 const t=Math.min(n,m+rP),u=Math.max(1,n-b),g=Math.max(0,u-t-1),P=new Set(),Q=new Set();
 for(let i=Math.max(1,m-a);i<m;i++)P.add(i);
 for(let i=c+1;i<=m;i++)P.add(i);
 for(let i=Math.max(1,n-b);i<n;i++)Q.add(i);
 for(let i=c+1;i<=t;i++)Q.add(i);
 return {c,t,u,g,P,Q};
}
function T(c,pc,qc,fp,fq,kP,kQ,d){
 const h=ky([c,pc,qc,fp,fq,kP,kQ,d]);if(Tcache.has(h))return Tcache.get(h);
 let D=new Map([[ky([0,0,0,0,0]),1n]]);
 for(let i=1;i<=c;i++){
  const E=new Map();
  for(const [z,v] of D){
   const [x,y,e,lp,lq]=pa(z);
   for(let p=0;p<2;p++)for(let q=0;q<2;q++){
    if(i===1&&(p||q))continue;
    if(i===c&&((pc>=0&&p!==pc)||(qc>=0&&q!==qc)))continue;
    if(i>1&&((lp&&p)||(lq&&q)))continue;
    const xx=x+p,yy=y+q,ee=e+(p!==q?1:0);
    if(xx<=kP&&yy<=kQ&&ee<=d)add(E,ky([xx,yy,ee,p,q]),v);
   }
  }D=E;
 }
 const E=new Map();
 for(const [z,v] of D){
  const [x,y,e,p,q]=pa(z);
  if(c>0&&(p&&fp||q&&fq))continue;
  add(E,ky([x,y,e]),v);
 }
 Tcache.set(h,E);return E;
}
function U(g,l,r,kQ){
 if(!g)return new Map([["0",1n]]);
 const h=ky([g,l,r,kQ]);if(Ucache.has(h))return Ucache.get(h);
 let D=new Map([[ky([l,0]),1n]]);
 for(let i=0;i<g;i++){
  const E=new Map();
  for(const [z,v] of D){const [old,k]=pa(z);
   for(let q=0;q<2;q++)if(!(old&&q)&&k+q<=kQ)add(E,ky([q,k+q]),v);
  }D=E;
 }
 const E=new Map();
 for(const [z,v] of D){const [last,k]=pa(z);if(!(last&&r))add(E,String(k),v)}
 Ucache.set(h,E);return E;
}
function grouped(m,n,kP,kQ,d,pP,pQ,rP,rQ){
 const {c,t,u,g,P,Q}=geom(m,n,pP,pQ,rP,rQ);
 let D=new Map();
 for(const pc of c&&P.has(c)?[0,1]:[-1])for(const qc of c&&Q.has(c)?[0,1]:[-1])
  add(D,ky([0,0,0,pc,qc,-1,-1,-1,-1,-1,-1,-1]),1n);
 const ix=[];
 for(let i=c+1;i<=m;i++)ix.push([i,1]);
 for(let i=m+1;i<=n;i++)if(i<=t||i>=u)ix.push([i,0]);
 for(const [i,both] of ix){
  const E=new Map();
  for(const [z,count] of D){
   const [x,y,e,pc,qc,fp,fq,lp,lq,left,right,last]=pa(z);
   for(const p of both?[0,1]:[-1])for(let q=0;q<2;q++){
    if(both&&i===m&&p)continue;
    if(i===1&&(p||q))continue;
    if(i===n&&q)continue;
    if(both&&fp>=0&&lp&&p)continue;
    if(last===i-1&&lq&&q)continue;
    const xx=x+(p===1?1:0),yy=y+q,ee=e+(both&&p!==q?1:0);
    if(xx>kP||yy>kQ||ee>d)continue;
    add(E,ky([xx,yy,ee,pc,qc,fp<0?p:fp,fq<0?q:fq,
        both?p:lp,q,g&&i===t?q:left,g&&i===u?q:right,i]),count);
   }
  }D=E;
 }
 let qF=0n,pop=0n,summaries=0;
 for(const [z,cnt] of D){
  const [x,y,e,pc,qc,fp,fq,lp,lq,l,r,last]=pa(z);
  const H=T(c,pc,qc,fp,fq,kP,kQ,d),G=U(g,l,r,kQ);
  let mass=0n;
  for(const [tz,a] of H){
   const [bp,bq,dd]=pa(tz);
   if(bp===kP-x&&dd===d-e)mass+=a*(G.get(String(kQ-y-bq))||0n);
  }
  if(mass){qF+=cnt;pop+=cnt*mass;summaries++}
 }
 return {qF:String(qF),population:String(pop),summaries,visible_dp_states:D.size,c,t,u,g};
}
function words(L,k){
 const out=[];function go(i,b,w){
  if(i>L){if(b===k)out.push(w);return}
  for(let x=0;x<2;x++)if(!(x&&(i===1||i===L||w.endsWith("1")))&&b+x<=k)
   go(i+1,b+x,w+String(x));
 }go(1,0,"");return out;
}
function brute(x){
 const [m,n,kP,kQ,d,pP,pQ,rP,rQ]=x,{P,Q}=geom(m,n,pP,pQ,rP,rQ),seen=new Map();
 for(const p of words(m,kP))for(const q of words(n,kQ)){
  let e=0;for(let i=0;i<m;i++)e+=(p[i]!==q[i]);
  if(e!==d)continue;
  const k=ky([[...P].sort((a,b)=>a-b).map(i=>[i,p[i-1]]),
    [...Q].sort((a,b)=>a-b).map(i=>[i,q[i-1]])]);
  add(seen,k,1n);
 }
 let pop=0n;for(const v of seen.values())pop+=v;
 return [String(seen.size),String(pop)];
}
let seed=455,cases=0,nonempty=0,raw=0n,classes=0n;
function random(n){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n}
for(let k=0;k<1100;k++){
 const m=3+random(7),n=m+1+random(13-m),kP=random(Math.min(3,Math.floor((m-1)/2)+1)),
 kQ=random(Math.min(3,Math.floor((n-1)/2)+1)),d=random(Math.min(m,5)+1);
 const x=[m,n,kP,kQ,d,1+random(m+1),random(n+1),random(5),random(4)],
       a=grouped(...x),b=brute(x);
 if(a.qF!==b[0]||a.population!==b[1])throw Error("grouped/brute mismatch "+ky(x));
 cases++;if(BigInt(a.population))nonempty++;raw+=BigInt(a.population);classes+=BigInt(a.qF);
}
const large=[[64,80,15,17,1,10,5,3,0],[64,80,15,17,1,24,10,8,5],
 [92,126,20,25,3,12,9,7,4]].map(x=>({parameters:x,result:grouped(...x)}));
console.log(JSON.stringify({marker:"STAGE455B_GROUPED_C_T_U_EXECUTED_PASS",
 check:{cases,nonempty,raw:String(raw),classes:String(classes)},large},null,2));

// Signed POP-only, A=+E1, B=+E2, C=+E3; full 6-vector and 12x12 J.
const ABC=["A","B","C"],direction={A:0,B:2,C:4};
function signedWords(L){let ret=[];function go(w){
 if(w.length===L){if(w[L-1]==="A")ret.push(w);return}
 for(const q of ABC)if(!(w.length===0&&q!=="A")&&!(q!=="A"&&w.length&&w[w.length-1]!=="A"))go(w+q)
 }go("");return ret}
function O(p,q){
 const V=w=>{const o=Array(6).fill(0);for(const z of w)o[direction[z]/2]++;return o};
 const J=w=>{const o=Array(144).fill(0);for(let i=0;i+1<w.length;i++)
  o[12*direction[w[i]]+direction[w[i+1]]]++;return o};
 let K=0;for(let i=0;i<Math.min(p.length,q.length);i++)K+=(p[i]===q[i]);
 return [p.length,q.length,V(p),V(q),J(p),J(q),K];
}
function RK(p,q,a,b){
 const m=p.length,n=q.length,c=Math.min(m-a,n-b);
 return ky([p.slice(Math.max(0,m-a-1),m-1),q.slice(Math.max(0,n-b-1),n-1),
  [...p.slice(c)].map((v,i)=>v===q[c+i]?1:0)]);
}
function signatures(p,q,a,b){const z=[];for(let i=0;i<=a;i++)for(let j=0;j<=b;j++)
 z.push(O(p.slice(0,p.length-i),q.slice(0,q.length-j)));return ky(z)}
let configurations=0,fibers=0,histories=0,comparedPairs=0;
for(let m=3;m<=5;m++)for(let n=m+1;n<=7;n++){
 const F=new Map();
 for(const p of signedWords(m))for(const q of signedWords(n)){
  const k=ky(O(p,q));if(!F.has(k))F.set(k,[]);F.get(k).push([p,q]);
 }
 for(let a=0;a<=m;a++)for(let b=0;b<=n;b++){
  configurations++;
  for(const f of F.values())if(f.length>1){
   fibers++;histories+=f.length;comparedPairs+=f.length*(f.length-1)/2;
   const forward=new Map(),backward=new Map();
   for(const [p,q] of f){
    const k=RK(p,q,a,b),sig=signatures(p,q,a,b);
    if(forward.has(k)&&forward.get(k)!==sig)throw Error("POP iff forward");
    if(backward.has(sig)&&backward.get(sig)!==k)throw Error("POP iff reverse");
    forward.set(k,sig);backward.set(sig,k);
   }
  }
 }
}
const P0="AAAAA",Q1="ABACAAA",Q2="ACABAAA";
const witness={
 initial_observation_equal:ky(O(P0,Q1))===ky(O(P0,Q2)),
 matching_bits_equal:[...P0].every((v,i)=>(v===Q1[i])===(v===Q2[i])),
 future_observations_distinct:signatures(P0,Q1,0,3)!==signatures(P0,Q2,0,3),
 third_q_pop_J_equal:ky(O(P0,Q1.slice(0,4))[5])===ky(O(P0,Q2.slice(0,4))[5])
};
if(!witness.initial_observation_equal||!witness.matching_bits_equal||
 !witness.future_observations_distinct||witness.third_q_pop_J_equal)
 throw Error("signed strict witness failed");
console.log(JSON.stringify({marker:"STAGE455B_SIGNED_BOTH_POP_IFF_FINITE_PASS",
 configurations,fibers,histories,comparedPairs,witness},null,2));
