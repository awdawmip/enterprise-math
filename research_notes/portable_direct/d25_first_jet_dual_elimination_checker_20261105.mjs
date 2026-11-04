// D25 original-216 first-jet dual reduction, exact finite-field regression.
// Standard JavaScript only. Every modulus p here is prime, so denominators 1..(p-1)/2, 2,3 are units.
"use strict";
function isPrime(p) {
  if (p < 2) return false;
  for (let j=2; j*j<=p; j++) if (p%j===0) return false;
  return true;
}
function check(p) {
  if (!isPrime(p) || p<7 || p%6!==1) throw new Error("invalid p");
  const n=(p-1)/6, K=2*n, N=3*n;
  const mod=x=>((x%p)+p)%p;
  const mul=(...xs)=>xs.reduce((a,b)=>mod(a*mod(b)),1);
  function pow(a,b) {
    let z=1;
    while (b>0) {
      if (b%2) z=mul(z,a);
      a=mul(a,a);
      b=Math.floor(b/2);
    }
    return z;
  }
  const inv=x=>pow(mod(x),p-2), half=inv(2), third=inv(3);
  const P0=x=>mul(x-3*n,x-2*n,x-4*n);
  const P1=x=>mod(mul(half,x-2*n,x-4*n)+mul(third,x-3*n,x-4*n)+mul(2,third,x-3*n,x-2*n));
  const P2=x=>mod(mul(13,inv(18),x)-2*n);
  const w=[1], v=[0], u=[0]; // coefficients [eps^0],[eps^1],[eps^2] of original centered 3F2
  for (let k=1; k<=N+1; k++) {
    const d=inv(k*k*k), a=mul(P0(k-1),d), b=mul(P1(k-1),d), c=mul(P2(k-1),d);
    w[k]=mul(a,w[k-1]);
    v[k]=mod(mul(a,v[k-1])+mul(b,w[k-1]));
    u[k]=mod(mul(a,u[k-1])+mul(b,v[k-1])+mul(c,w[k-1]));
  }
  const h=[], lam=[];
  for (let k=0; k<=N; k++) h[k]=mul(6*k+1,pow(half,k));
  lam[N]=h[N];
  for (let k=N-1; k>=1; k--) lam[k]=mod(h[k]+mul(P0(k),inv((k+1)**3),lam[k+1]));
  let S2_direct=0, S2_dual=0;
  for (let k=1; k<=N; k++) {
    const forcing=mod(mul(P1(k-1),v[k-1])+mul(P2(k-1),w[k-1]));
    S2_direct=mod(S2_direct+mul(h[k],u[k]));
    S2_dual=mod(S2_dual+mul(lam[k],inv(k**3),forcing));
  }
  const f2_endpoint=mul(P1(N),v[N],inv((N+1)**3));
  const U=mod(-mul(f2_endpoint,pow(half,N+1)));
  if (S2_direct!==S2_dual || f2_endpoint!==u[N+1] || P0(K)!==0 ||
      w[N]!==0 || w[N+1]!==0 || v[N+1]!==0 || u[N+1]===0) {
    throw new Error("dual/endpoint failure p="+p);
  }
  return {p,n,S2:S2_dual,endpoint_f2:f2_endpoint,U};
}
const checked=[];
for (let p=7; p<=997; p++) if (p%6===1 && isPrime(p)) checked.push(check(p));
const anchors={7:[4,6,4],13:[0,6,3],19:[18,4,2],139:[4,77,108],373:[240,166,83]};
for (const r of checked) {
  if (Object.prototype.hasOwnProperty.call(anchors,r.p)) {
    const [S2,f2,U]=anchors[r.p];
    if (r.S2!==S2 || r.endpoint_f2!==f2 || r.U!==U) throw new Error("anchor mismatch "+r.p);
  }
}
if (checked.length!==80) throw new Error("unexpected sample coverage "+checked.length);
console.log(JSON.stringify({checked_primes:checked.length, failures:0, anchors:checked.filter(r=>Object.prototype.hasOwnProperty.call(anchors,r.p))}));