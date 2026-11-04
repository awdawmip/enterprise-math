#!/usr/bin/env node
"use strict";
// D25 Sun defect full support + z-jet transport. Exact BigInt only.
const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
const mod=(x,m)=>{x%=m;return x<0n?x+m:x};
const inv=(a,m)=>{let u=mod(a,m),v=m,s=1n,t=0n;while(v){let q=u/v;[u,v]=[v,u-q*v];[s,t]=[t,s-q*t]};assert(u===1n,"nonunit");return mod(s,m)};
function primes(n){let a=Array(n+1).fill(true);a[0]=a[1]=false;for(let i=2;i*i<=n;i++)if(a[i])for(let j=i*i;j<=n;j+=i)a[j]=false;return a.map((b,i)=>b?i:0).filter(x=>x>=5)}
function audit(p,d){
 const P=BigInt(p),M=P**3n,D=BigInt(d),m=x=>mod(x,M),f=x=>mod(x,P);
 let c=[1n],b=[1n],val=0,L=null,R=null;
 for(let k=1;k<p;k++){
  const n=BigInt(k-1),a=D*n+1n,z=D*n+D-1n,den=D*D*BigInt(k*k);
  c.push(m(c[k-1]*a*z*inv(den,M)));
  let hit=(a%P===0n?1:0)+(z%P===0n?1:0);val+=hit;
  if(val===1&&L===null)L=k;if(val===2&&R===null)R=k;
  b.push(b[k-1]*(4n*BigInt(k)-2n)/BigInt(k));
 }
 assert(L!==null&&R!==null,"missing valuation breaks");
 const K=2*R-2,J=K-p;assert(J>=1&&p+L<=2*R,"support precondition");
 let a=Array(2*p-1).fill(0n);
 for(let i=0;i<p;i++)for(let j=0;j<p;j++)a[i+j]=m(a[i+j]+c[i]*c[j]);
 for(let k=0;k<p;k++){
  let q=1n;
  for(let t=0;t<=k;t++){
   a[k+t]=m(a[k+t]-((t%2)?-1n:1n)*b[k]*c[k]*q);
   if(t<k)q=q*BigInt(k-t)/BigInt(t+1);
  }
 }
 const p2=P*P;
 assert(a.every(v=>v%p2===0n),"Sun p^2 divisibility failed");
 assert(a.slice(0,p+1).every(v=>v===0n),"unexpected initial defect");
 assert(a.slice(K+1).every(v=>v===0n),"degree support failed");
 let corner=c[R-1]**2n+((p+L===2*R)?2n*c[p-1]*c[L-1]:0n);
 let top=m(corner-((R-1)%2?-1n:1n)*b[R-1]*c[R-1]);
 assert(top===a[K],"top boundary formula failed");
 const C=f(BigInt(d-1)*inv(D*D,P));
 const zero=[0n,0n,0n],one=[1n,0n,0n];
 const add=(u,v)=>u.map((x,i)=>f(x+v[i]));
 const scale=(u,v)=>u.map(x=>f(x*v));
 const mul=(u,v)=>[f(u[0]*v[0]),f(u[0]*v[1]+u[1]*v[0]),f(u[0]*v[2]+u[1]*v[1]+u[2]*v[0])];
 const reciprocal=u=>{let t=inv(u[0],P);return [t,f(-u[1]*t*t),f(u[1]*u[1]*t*t*t-u[2]*t*t)]};
 let row=Array.from({length:J+1},()=>zero.slice()),cs=[1n],u=one,v=one;
 for(let i=1;i<=J;i++){let h=BigInt(i-1),k=BigInt(i);cs.push(f(cs[i-1]*(h*(h+1n)+C)*inv(k*k,P)))}
 for(let i=0;i<=J;i++){
  for(let j=i;j<=J;j++)row[j]=add(row[j],scale(u,-2n*cs[j-i]));
  let bj=one;
  for(let n=0;n<=J-i;n++){
   row[i+n]=add(row[i+n],scale(mul(mul(u,v),bj),n%2?-2n:2n));
   if(n<J-i)bj=scale(mul(bj,[f(BigInt(i-n)),1n,0n]),inv(BigInt(n+1),P));
  }
  if(i<J){
   let k=BigInt(i),t=k+1n,den=[f(t*t),f(2n*t),1n],rec=reciprocal(den);
   u=mul(u,mul([f(k*(k+1n)+C),f(2n*k+1n),1n],rec));
   v=mul(v,mul([f((2n*k+1n)*(2n*k+2n)),f(8n*k+6n),4n],rec));
  }
 }
 let e=Array(2*p-1).fill(0n),ej=Array(2*p-1).fill(0n);
 for(let n=0;n<2*p-1;n++)e[n]=f(a[n]/p2);
 for(let j=0;j<=J;j++){
  assert(row[j][0]===0n&&row[j][1]===0n,"Phi has nonzero order-0/1 jet");
  ej[p+j]=f(C*row[j][2]);
 }
 assert(e.every((x,n)=>x===ej[n]),"all-coefficient z^2 transport failed");
 let observed=-1;for(let i=0;i<e.length;i++)if(e[i])observed=i;
 const output={p,d,L,R,degree_bound:K,observed_degree:observed,leading:f(top/p2).toString(),boundary_terms:J,first_three:[1,2,3].filter(j=>j<=J).map(j=>e[p+j].toString())};
 if(p%24===13||p%24===19){
  let den=d===3?4n:6n,t=inv(den,P),xx=d===3?[f(2n*t),t]:[f(3n*t),f(2n*t)];
  const qa=(x,y)=>[f(x[0]+y[0]),f(x[1]+y[1])];
  const qm=(x,y)=>[f(x[0]*y[0]+2n*x[1]*y[1]),f(x[0]*y[1]+x[1]*y[0])];
  function horner(coeff){let value=[0n,0n],der=[0n,0n];for(let i=coeff.length-1;i>=0;i--){der=qa(qm(der,xx),value);value=qa(qm(value,xx),[coeff[i],0n])}return [value,der]}
  const read=(pair)=>pair.map(v=>v.map(x=>x.toString()));
  let actual=horner(e),reduced=horner(ej);assert(JSON.stringify(read(actual))===JSON.stringify(read(reduced)),"observer mismatch");
  output.observer={value:read(actual)[0],derivative:read(actual)[1]};
 }
 return output;
}
function main(){
 const results=[];
 for(const p of primes(151))for(const d of [3,4])results.push(audit(p,d));
 for(const d of [3,4])results.push(audit(373,d));
 return {audits:results.length,failures:0,examples:results.filter(o=>[5,13,19,139,373].includes(o.p)),max_prime:373};
}
if(typeof process!=="undefined" && process.argv&&process.argv[1] && process.argv[1].endsWith(".mjs"))console.log(JSON.stringify(main(),null,2));