#!/usr/bin/env node
"use strict";
// D25 original-216 Clausen weighted high-tail: exact p-adic strip and O(p) prefix readout.
// TASK_RESEARCH author-side; frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3.
// Node 18+, standard BigInt only. No native experiment or reviewer admission.
const rem=(x,m)=>{let r=x%m;return r<0n?r+m:r;};
const pow=(a,e,m)=>{let r=1n;a=rem(a,m);while(e){if(e&1n)r=r*a%m;a=a*a%m;e>>=1n;}return r;};
const prime=x=>{if(x<2)return false;for(let d=2;d*d<=x;d++)if(x%d===0)return false;return true;};
function check(p0){
  if(p0<7||p0%6!==1||!prime(p0))throw Error("prime p=6m+1 required");
  const p=BigInt(p0),P=p**3n,m=(p0-1)/6,inv3=x=>pow(x,p*p*(p-1n)-1n,P);
  let b=[1n],w=[1n],v=[1n];
  for(let k=1;k<p0;k++){
    const q=BigInt(k-1),d=BigInt(k);
    b[k]=rem(b[k-1]*(6n*q+1n)*(3n*q+1n)*inv3(36n*d*d),P);
    w[k]=rem(w[k-1]*(2n*q+1n)*(3n*q+1n)*(3n*q+2n)*inv3(36n*d**3n),P);
    v[k]=rem(v[k-1]*(4n*q+1n)*(4n*q+2n)*(4n*q+3n)*(4n*q+4n)*inv3(2304n*d**4n),P);
  }
  let F=rem(b.reduce((s,x)=>s+x,0n),P),
      h=rem(b.reduce((s,x,k)=>s+BigInt(12*k+1)*x,0n),P),
      W=rem(w.reduce((s,x,k)=>s+BigInt(6*k+1)*x,0n),P),
      V=rem(v.reduce((s,x,k)=>s+BigInt(8*k+1)*x,0n),P);
  let T=0n;
  for(let i=1;i<p0;i++)for(let j=p0-i;j<p0;j++)
    T=rem(T+BigInt(6*(i+j)+1)*b[i]*b[j],P);
  if(rem(W+T-F*h,P)!==0n||T%(p*p)!==0n)throw Error("Clausen/valuation "+p0);
  const inv=[0n,1n];
  for(let k=2;k<p0;k++)inv[k]=rem(p-(p/BigInt(k))*inv[Number(p%BigInt(k))],p);
  const inv36=pow(36n,p-2n,p),c=[1n];
  for(let k=1;k<p0;k++){
    let a=6n*BigInt(k)-5n,s=3n*BigInt(k)-2n;
    if(k===m+1){if(a!==p)throw Error("p factor1");a=1n;}
    if(k===2*m+1){if(s!==p)throw Error("p factor2");s=1n;}
    c[k]=rem(c[k-1]*a*s*inv36*inv[k]*inv[k],p);
    let nu=k<=m?0:k<=2*m?1:2,d=p**BigInt(nu);
    if(b[k]%d!==0n||b[k]/d%p!==c[k])throw Error("unit quotient "+p0+"/"+k);
  }
  let X=0n,Y=0n,t=0n;
  for(let i=1;i<=m;i++){
    let r=c[p0-i];X=rem(X+r,p);Y=rem(Y+BigInt(i)*r,p);
    t=rem(t+2n*c[i]*((6n*BigInt(i)+1n)*X-6n*Y),p);
  }
  if(t!==T/(p*p)%p)throw Error("linear prefix "+p0);
  let target=p0%24===13||p0%24===19, delta=null;
  if(target){
    if(F%p!==0n||h%p===0n||W%(p*p)!==p)throw Error("first digit "+p0);
    delta=rem((rem((F/p)*h,p*p)-1n)/p,p);
    if(delta!==rem((W-p)/(p*p)+t,p))throw Error("LIFT split "+p0);
  }
  return {p:p0,m,tail_digit:Number(t),target,delta:delta===null?null:Number(delta),
    W_eq_p_modp3:W===p,V_eq_p_modp3:V===p,
    T_modp3:T.toString(),F_modp3:F.toString(),h_modp3:h.toString()};
}
const rows=[];for(let p=7;p<=373;p++)if(p%6===1&&prime(p))rows.push(check(p));
const target=rows.filter(x=>x.target);
console.log(JSON.stringify({status:"PASS",total:rows.length,target:target.length,
  W_target_p3:target.every(x=>x.W_eq_p_modp3),
  V_target_p3:target.every(x=>x.V_eq_p_modp3),
  samples:target.filter(x=>[13,19,37,61,373].includes(x.p))}));
