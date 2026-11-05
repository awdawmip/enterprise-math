// D25 p^4 Clausen one-jet exact checker. Node.js BigInt; no dependencies.
// The polynomial coefficients are streamed twice, preserving O(1) auxiliary memory.
"use strict";
const mod = (a, m) => { const r = a % m; return r < 0n ? r + m : r; };
function inv(a, m) {
  let x = 0n, y = 1n, b = m, c = mod(a, m);
  while (c !== 0n) { const q = b / c; [x, y] = [y, x-q*y]; [b, c] = [c, b-q*c]; }
  if (b !== 1n) throw Error("non-unit denominator");
  return mod(x, m);
}
function jets(p, z, m) {
  const n = (p-1n)/6n, iz = inv(z, m), iz2=mod(iz*iz,m), iz3=mod(iz2*iz,m), iz4=mod(iz3*iz,m);
  let a=1n, zk=1n, g=0n, v=0n, q=0n, r=0n, s=0n;
  for(let k=0n;k<=n;k++){
    g=mod(g+a*zk,m);
    if(k>=1n) v=mod(v+a*zk*k*iz,m);
    if(k>=2n) q=mod(q+a*zk*k*(k-1n)*iz2,m);
    if(k>=3n) r=mod(r+a*zk*k*(k-1n)*(k-2n)*iz3,m);
    if(k>=4n) s=mod(s+a*zk*k*(k-1n)*(k-2n)*(k-3n)*iz4,m);
    if(k<n) {
      a=mod(a*2n*(k-n)*(k-2n*n)*inv((2n+2n*k-p)*(k+1n),m),m);
      zk=mod(zk*z,m);
    }
  }
  return {g,v,q,r,s};
}
function checkPrime(P) {
  const p=BigInt(P),m=p**4n,u=p-1n,x=inv(2n,m),{g,v,q,r,s}=jets(p,x,m);
  const i3=inv(3n,m),i9=inv(9n,m),i81=inv(81n,m);
  const q2=mod(u*v+2n*u*u*i9*g,m);
  const q3=mod((11n*u*u*i9-2n*u+4n)*v+2n*u**3n*i9*g,m);
  const q4=mod((13n*u**3n*i9-6n*u*u+20n*u)*v+
    (22n*u**4n*i81-8n*u**3n*i9+32n*u*u*i9)*g,m);
  if(q!==q2 || r!==q3 || s!==q4) throw Error("derivative disagreement at "+P);
  const f=mod(g*(g+6n*v),m);
  const A=mod(6n*v*v+(8n+6n*p)*g*v+4n*u*u*i3*g*g,m);
  if(f%p!==0n || A%p===0n) throw Error("simple-root premise fails at "+P);
  const B=mod((26n*(v*v+g*q2)+18n*v*q2+6n*g*q3)*inv(2n,m),m);
  const C=mod((114n*v*q2+38n*g*q3+18n*q2*q2+24n*v*q3+6n*g*q4)*inv(6n,m),m);
  const ai=inv(A,m),d=mod(f*ai,m),b=mod(B*ai,m),c=mod(C*ai,m);
  const cubic=mod(2n*b*b-c,m);
  const branch=g%p===0n?"G":"L";
  const expectedC=mod((branch==="G"?58n:70n)*inv(27n,p),p);
  const expectedCubic=mod((branch==="G"?-34n:530n)*inv(27n,p),p);
  if(c%p!==expectedC || cubic%p!==expectedCubic) throw Error("cubic branch mismatch at "+P);
  const root=mod(x-d-b*d*d-cubic*d**3n,m);
  const again=jets(p,root,m);
  if(mod(again.g*(again.g+12n*root*again.v),m)!==0n) throw Error("root failure at "+P);
  return {p:P,branch,c:Number(c%p),cubic:Number(cubic%p),root:root.toString()};
}
function prime(p) {for(let k=2;k*k<=p;k++)if(p%k===0)return false;return true;}
const results=[];
for(let p=7;p<=1200;p+=6)if(prime(p))results.push(checkPrime(p));
console.log("PASS",results.length,"/ 94");
for(const p of [7,13,19,373])console.log(JSON.stringify(results.find(r=>r.p===p)));
