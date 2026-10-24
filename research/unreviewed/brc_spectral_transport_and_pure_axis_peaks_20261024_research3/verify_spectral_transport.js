"use strict";
// Exact verification for unreviewed BRC transport theorem (Node.js BigInt)
const verifier=function verifier() {
 "use strict";
 const acts=["0","2","3"];
 const Q={"0":[1n,665n,1n,333n],"2":[333n,333n,1n,333n],"3":[1n,1n,1n,997n]};
 const edges=[[0,1],[1,2],[1,3],[2,3]],deg=[1n,3n,2n,2n];
 const requireTrue=(v,s)=>{if(!v)throw Error(s)};
 const weight=(c,f)=>acts.reduce((p,a,k)=>p*f(a)**BigInt(c[k]),1n);
 const Wv=(c,i)=>weight(c,a=>Q[a][i]);
 const We=(c,i,j)=>weight(c,a=>Q[a][i]+Q[a][j]);
 const N=(c)=>c.reduce((s,v)=>s+v,0)===0?0n:edges.reduce((s,[i,j])=>s+We(c,i,j),0n)-deg.reduce((s,d,i)=>s+d*Wv(c,i),0n);
 const next=(c,a)=>{let x=c.slice();x[acts.indexOf(String(a))]++;return x};
 const G=(c,a)=>N(next(c,a))-1000n*N(c);
 const put=(m,b,v)=>{if(v)m.set(Number(b),(m.get(Number(b))||0n)+v)};
 const atoms=(c,a,r)=>{
  let P=new Map(),M=new Map(),q=Q[String(a)],rho=BigInt(r);
  for(let i=0;i<4;i++){
   let b=q[i],v=deg[i]*(1000n-b)*Wv(c,i)*(b-rho);
   if(v>0n)put(P,b,v);else put(M,b,-v);
  }
  for(let [i,j] of edges){
   let b=q[i]+q[j],v=-(1000n-b)*We(c,i,j)*(b-rho);
   if(v>0n)put(P,b,v);else put(M,b,-v);
  }
  return {P,M};
 };
 const flow=(P,M)=>{
  let p=0n,m=0n;
  for(let b of [...new Set([...P.keys(),...M.keys()])].sort((x,y)=>y-x)){
   p+=P.get(b)||0n;m+=M.get(b)||0n;
   if(p>m)return false;
  }
  return true;
 };
 const total=(map)=>[...map.values()].reduce((s,v)=>s+v,0n);
 let rec=0,fl=0;
 for(let x=0;x<=5;x++)for(let y=0;y<=5;y++)for(let z=0;z<=5;z++){
  if(x+y+z===0)continue;const c=[x,y,z];
  for(let a of acts){
   const r=a==="0"?334:a==="2"?334:2;
   const {P,M}=atoms(c,a,r);
   requireTrue(G(next(c,a),a)-BigInt(r)*G(c,a)===total(P)-total(M),"recurrence "+c+":"+a);
   rec++;
   if((a==="0"&&y+z>0)||(a==="2")||(a==="3"&&x+y>0)){
    requireTrue(flow(P,M),"transport "+c+":"+a);fl++;
   }
  }
 }
 const mask=(c)=>{
  let dp=Array(16).fill(0n);dp[0]=1n;
  for(let j=0;j<3;j++)for(let t=0;t<c[j];t++){
   let v=Array(16).fill(0n);
   for(let m=0;m<16;m++)if(dp[m])for(let i=0;i<4;i++)v[m|(1<<i)]+=dp[m]*Q[acts[j]][i];
   dp=v;
  }
  return [3,6,10,12].reduce((s,m)=>s+dp[m],0n);
 };
 const samples=[[0,0,0],[12,0,0],[13,0,0],[14,0,0],[0,1,0],[0,2,0],[0,3,0],[0,0,1],[0,0,3],[0,0,404],[0,0,405],[0,0,406],[4,2,7],[5,1,0],[1,3,2],[6,4,5]];
 for(let c of samples)requireTrue(mask(c)===N(c),"mask "+c);
 let a0plus=G([12,0,0],"0"),a0minus=G([13,0,0],"0");
 let a2plus=G([0,1,0],"2"),a2minus=G([0,2,0],"2");
 let a3plus=G([0,0,404],"3"),a3minus=G([0,0,405],"3");
 requireTrue(a0plus>0n&&a0minus<0n&&a2plus>0n&&a2minus<0n&&a3plus>0n&&a3minus<0n,"boundary signs");
 for(let t=1;t<=6;t++)requireTrue(G([t,0,0],"0")>0n,"initial0");
 for(let t=1;t<=3;t++)requireTrue(G([0,0,t],"3")>0n,"initial3");
 for(let t of [1,2,3,404,405]){
  let J=-1996n*2n**BigInt(t)-4n*998n**BigInt(t)+6n*997n**BigInt(t)+5994n;
  requireTrue(J===G([0,0,t],"3"),"pure3 closed form");
 }
 let p0=atoms([6,0,0],"0",665),p3=atoms([0,0,3],"3",997);
 requireTrue(flow(p0.P,p0.M)&&flow(p3.P,p3.M),"pure tail flow");
 let tail0=998n**6n-331n*334n**6n,tail3=499n**3n-496505n;
 requireTrue(tail0>0n&&tail3>0n,"pure tail inequalities");
 requireTrue(!flow(new Map([[5,2n]]),new Map([[4,1n],[6,1n]])),"transport not necessary");
 for(let t=0;t<36;t++)requireTrue(4n**BigInt(t)+6n**BigInt(t)>=2n*5n**BigInt(t),"spectral counterexample");
 return {schema:"EM_BRC_SPECTRAL_TRANSPORT_EXACT_EVIDENCE_V1",date:"2026-10-24",weights:{"0":[1,665,1,333],"2":[333,333,1,333],"3":[1,1,1,997]},denominator:1000,good_edges:edges,grid:"0<=x,y,z<=5, excluding zero",recurrence_checks:rec,transport_checks:fl,independent_16mask_checks:samples.length,pure_axis_peaks:{"0":13,"2":2,"3":405},boundary_integer_numerators:{a0_at12:a0plus.toString(),a0_at13:a0minus.toString(),a2_at1:a2plus.toString(),a2_at2:a2minus.toString(),a3_at404:a3plus.toString(),a3_at405:a3minus.toString()},tail_inequalities:{"998^6-331*334^6":tail0.toString(),"499^3-496505":tail3.toString()},pure_tail_transport:true,transport_not_necessary_example:"4^t+6^t>=2*5^t but threshold 5 has positive mass 2>negative mass 1",classification:"AUTHOR_PROVED_EXACT_CHECKED_UNREVIEWED"};
};
console.log(JSON.stringify(verifier(),null,2));
