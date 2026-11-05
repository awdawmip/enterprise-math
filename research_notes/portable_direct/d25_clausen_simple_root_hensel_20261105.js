#!/usr/bin/env node
"use strict";
// D25 signed Clausen simple-root/Hensel checker. Exact BigInt arithmetic only.
// Arithmetic scope: all primes 7<=p<=1200 with p=1(mod6).
// Mathematical proof is in 20261105_hourly20_d25_clausen_simple_root_hensel_p3.md.
// No native H0/B0 computation or Source admission is performed.
const mod = (a, m) => ((a % m) + m) % m;
function inverse(a,m) {
  let b=m, x=1n, y=0n; a=mod(a,m);
  while(b!==0n) {
    const q=a/b;
    [a,b]=[b,a-q*b];
    [x,y]=[y,x-q*y];
  }
  if(a!==1n) throw Error("nonunit denominator");
  return mod(x,m);
}
function prime(q) {
  if(q<2) return false;
  for(let d=2;d*d<=q;d++) if(q%d===0) return false;
  return true;
}
function check(q) {
  const p=BigInt(q), n=BigInt((q-1)/6), m=p**3n;
  let t=1n, G=1n, J=0n, K=0n, K3=0n, pow2=1n;
  const coefficients=[1n];
  // t_k=the exact hypergeometric summand at z=1/2 in Z/(p^3).
  for(let k=0n;k<n;k++){
    const j=k+1n;
    t=mod(t*(k-n)*(k-2n*n)*inverse(j*(2n*k+2n-p),m),m);
    G=mod(G+t,m);
    J=mod(J+j*t,m);
    K=mod(K+j*(j-1n)*t,m);
    K3=mod(K3+j*(j-1n)*(j-2n)*t,m);
    pow2=mod(pow2*2n,m);
    coefficients.push(mod(t*pow2,m));
  }
  const gd=mod(2n*J,m), gdd=mod(4n*K,m), gddd=mod(8n*K3,m);
  const L=mod(G+6n*gd,m);
  const Ld=mod(13n*gd+6n*gdd,m);
  const Ldd=mod(25n*gdd+6n*gddd,m);
  const f=mod(G*L,m), a=mod(gd*L+G*Ld,m);
  const fdd=mod(gdd*L+2n*gd*Ld+G*Ldd,m);
  const g0=G%p, l0=L%p, j0=J%p;
  if(f%p!==0n) throw Error(q+" first digit is not zero");
  if((g0===0n)===(l0===0n)) throw Error(q+" factor exclusivity");
  const expected=g0===0n ? mod(24n*j0*j0,p)
    : mod(g0*g0*inverse(6n,p),p);
  if(a%p===0n || a%p!==expected) throw Error(q+" derivative identity");
  // Hensel-Taylor: delta=f/a+(f''/2a)*(f/a)^2 mod p^3.
  const d1=mod(f*inverse(a,m),m);
  const delta=mod(d1+fdd*inverse(2n*a,m)*d1*d1,m);
  const x=mod(inverse(2n,m)-delta,m);
  // Independent polynomial evaluation at x via Horner; derivative too.
  let Y=0n, DY=0n;
  for(let k=coefficients.length-1;k>=0;k--){
    DY=mod(DY*x+Y,m);
    Y=mod(Y*x+coefficients[k],m);
  }
  const checkValue=mod(Y*(Y+12n*x*DY),m);
  if(checkValue!==0n) throw Error(q+" Hensel root failed");
  if(mod(2n*x-1n,p)!==0n) throw Error(q+" wrong residue class");
  return {p:q, G_mod_p:String(g0), L_mod_p:String(l0), J_mod_p:String(j0),
    Psi_derivative_mod_p:String(a%p), root_mod_p3:String(x),
    branch:g0===0n?"G":"L"};
}
let total=0, gBranch=0, lBranch=0;
const examples=[];
for(let p=7;p<=1200;p++){
  if(!prime(p)||p%6!==1) continue;
  const result=check(p);total++;
  if(result.branch==="G")gBranch++;else lBranch++;
  if([7,13,19,31,37,373].includes(p)) examples.push(result);
}
if(total!==94) throw Error("unexpected scope size: "+total);
const expectedRoots={13:"1918",19:"675",373:"31342631"};
for(const row of examples){
  if(expectedRoots[row.p] && row.root_mod_p3!==expectedRoots[row.p])
    throw Error("reference value drift p="+row.p);
}
console.log(JSON.stringify({status:"PASS",total,branches:{G:gBranch,L:lBranch},
  examples,claim:"finite exact computational validation only"},null,2));
