# R284HB — Exact polynomial sign certificates on unbounded diagonal strips

2026-11-25. Independent auxiliary four-phase binary-tag model; author computational proof, NOT_REVIEWED. Frozen science: R284HA at 82c1bbab0211958259cb233833a8b2d2ea9d0675, path research_notes/portable_direct/R284HA_BINOMIAL_PORT_MOMENTS_AND_DIAGONAL_CORRECTION_20261125.md, blob 256e77c033ef0c975173c818cdfdeb18ea3bc983; its GV/GY/GX/GL dependencies remain frozen. Current control entry and P000 V5, ACTIVE worldview, portable protocol, joint observer and research-method sources read. Gateway em_status returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. Historical researcher EM-DIRECT-0C386E is provenance, not current authenticated identity. Owner inventory unavailable in this run. No shared task claim or protected mutation.

## 1. Exact rational polynomial transport

Let d=u-q>=1, m=u+q, H=2q+u+1, J=q+3u. HA gives M_n(k)=(k+1)/(n+1) C(2n+2,n-k), and the three positive convolutions defining S,P,Q. K=PQ(J+1)^2/(S^2 H). We reuse those exact total-count observations only; full joint distribution and path identities retain the GY/GZ kernel.

For fixed d set g=d+1. Use common positive denominator D_n=(4n+2) product_{i=0}^g(n+2+i). For each k=0..g define polynomial
A_n(k)=(k+1)(4n+2)(n+2) product_{i=0}^{k-1}(n-i) product_{i=k}^{g-1}(n+3+i),
a_n(k)=(k+1)(n+2) product_{i=0}^{k-1}(n-1-i) product_{i=k}^{g}(n+2+i).
Empty products equal 1. By HA's adjacent rational moment recurrence and Catalan ratio, A_n(k)=D_n M_n(k)/M_n(0), a_n(k)=D_n M_(n-1)(k)/M_n(0) for n>=1. If k exceeds inventory the falling product contains zero, so exact boundary values are preserved.

Write T(X,Y,j)=sum_{k=0}^j X(k)Y(j-k), zero when j<0. Construct
Q*=T(A_u,A_m,d-1),
S*=Q*+T(A_u,A_m,d)+q[T(a_u,A_m,d)+T(a_u,A_m,d-1)],
P*=sum_{j=0}^3 C(3,j)T(a_u,a_m,d+1-j).
These equal the original counts multiplied by the SAME positive factor D_u D_m/[M_u(0)M_m(0)]. Consequently define N_d(u)=P*Q*(J+1)^2 and B_d(u)=S*^2 H; K(u-d,u)=N_d(u)/B_d(u), B_d(u)>0 on the physical integer domain. This removes the huge common Catalan factors while retaining the declared joint count exactly. Polynomial evaluation can use x=u-d, x>=0.

## 2. Certified infinite strips

For d=2,...,48 form the exact polynomial
R_d(x)=N_d(d+x) B_(d-1)(d+x)-N_(d-1)(d+x) B_d(d+x).
An executed integer coefficient calculation found EVERY coefficient strictly positive: 10,622 coefficients across 47 polynomials, degrees 8d+25 (41 through 409). Hence for every integer u>=d, 2<=d<=48,
K(u-d,u)>K(u-d+1,u).
This is an unbounded-in-u theorem in 47 strips, not a finite rectangle scan. No assumption about the sign of individual original branch differences is needed. Cross-multiplication is exact with positive denominators. All coefficients are computed by the code below; the theorem is conditional only on the frozen HA identity as the existing scientific dependency. No independent review claimed.

For each d=1..48 also consider L_d(x)=N_d(d+x)-B_d(d+x). Its nonzero coefficient signs in ascending degree have exactly one change from + to -. Its constant is positive and leading coefficient negative. By Descartes' rule (or dividing by x^j at the first negative exponent, giving a strictly decreasing sum for x>0), L_d has a unique positive real zero. This refers to the polynomial comparison; it does not require a noninteger interpretation of actual paths. On the integer domain there is a unique crossover, no ties, with first q=x where K<1 given by the following list for d=1..48:
1,4,6,7,9,10,11,12,13,14,15,15,16,17,17,18,19,19,20,21,21,22,22,23,23,24,24,25,25,26,26,26,27,27,28,28,29,29,29,30,30,31,31,31,32,32,33,33.
For fixed d and all integer u>=d, asymmetric wins iff u-d is strictly less than this threshold. Direct integer evaluation of the two neighboring values proves absence of ties; unique root certifies all others. Example d=48: q=32 (u=80) asymmetric wins; q=33 (u=81) symmetric wins, and remains so for all larger u at fixed d. This is a different one-parameter trajectory from fixed u; keep them separate.

## 3. Executed exact certificate

JavaScript BigInt coefficient arithmetic; arrays in ascending degree, trimmed. 47 difference polynomials, 10,622 coefficients, zero nonpositive coefficients. 282 independent evaluations against direct binomial HA counts (d=2..48, x=0,1,7, both adjacent gaps). Separate sign scan of 48 L_d polynomials and exact integer crossover evaluations yielded the thresholds above. No floating arithmetic in sign/cross-product comparisons. Reproduction below combines the two executed calculations. For each fixed d the finite polynomial sign check proves the indicated infinite integer strip. It is not an analytic proof uniform in arbitrary d.

```javascript
const trim=a=>{while(a.length>1&&a[a.length-1]===0n)a.pop();return a};
const add=(a,b,s=1n)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+s*(b[i]||0n)));
const mul=(a,b)=>{let c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return trim(c)};
const lin=(a,b)=>trim([BigInt(a),BigInt(b)]);
const prod=ps=>ps.reduce(mul,[1n]);
const seq=(n,v,g,off)=>Array.from({length:g+1},(_,k)=>prod([lin(k+1,0),lin(n+2,v),...(off?[]:[lin(4*n+2,4*v)]),...Array.from({length:k},(_,i)=>lin(n-off-i,v)),...Array.from({length:g+off-k},(_,i)=>lin(n+3-off+k+i,v))]));
// D is gap; U is constant term of u=U+x.
const calc=(D,U)=>{let q=U-D,m=2*U-D,g=D+1;let A=seq(U,1,g,0),a=seq(U,1,g,1),B=seq(m,2,g,0),b=seq(m,2,g,1);let T=(X,Y,j)=>j<0?[0n]:Array.from({length:j+1},(_,k)=>mul(X[k],Y[j-k])).reduce((a,b)=>add(a,b),[0n]);let Q=T(A,B,D-1),S=add(add(Q,T(A,B,D)),mul(lin(q,1),add(T(a,B,D),T(a,B,D-1)))),P=[1n,3n,3n,1n].reduce((v,c,j)=>add(v,T(a,b,D+1-j),c),[0n]);let J=lin(q+3*U+1,4),H=lin(2*q+U+1,3);return [prod([P,Q,J,J]),prod([S,S,H])]};
const ev=(a,x)=>a.reduceRight((v,c)=>v*x+c,0n);
function bin(n,k){if(k<0||k>n)return 0n;k=Math.min(k,n-k);let a=1n;for(let i=1;i<=k;i++)a=a*BigInt(n-k+i)/BigInt(i);return a}
function direct(q,u){let d=u-q,m=u+q,g=d+1;const M=n=>Array.from({length:g+1},(_,k)=>BigInt(k+1)*bin(2*n+2,n-k)/BigInt(n+1));let A=M(u),a=M(u-1),B=M(m),b=M(m-1);let T=(X,Y,j)=>j<0?0n:Array.from({length:j+1},(_,k)=>X[k]*Y[j-k]).reduce((a,b)=>a+b,0n);let Q=T(A,B,d-1),S=Q+T(A,B,d)+BigInt(q)*(T(a,B,d)+T(a,B,d-1)),P=[1n,3n,3n,1n].reduce((v,c,j)=>v+c*T(a,b,d+1-j),0n);return [P*Q*BigInt(q+3*u+1)**2n,S*S*BigInt(2*q+u+1)]}
let total=0,checks=0;
for(let d=2;d<=48;d++){
 let [n,b]=calc(d,d),[p,c]=calc(d-1,d),diff=add(mul(n,c),mul(p,b),-1n);
 if(diff.some(v=>v<=0n)||diff.length!==8*d+26)throw Error("coefficient");
 total+=diff.length;
 for(let x of [0,1,7])for(let [a,z,D] of [[n,b,d],[p,c,d-1]]){
  let [r,s]=direct(d+x-D,d+x);
  if(ev(a,BigInt(x))*s!==ev(z,BigInt(x))*r)throw Error("cross-check");
  checks++;
 }
}
let thresholds=[];
for(let d=1;d<=48;d++){
 let [n,b]=calc(d,d),a=add(n,b,-1n),signs=a.filter(x=>x!==0n).map(x=>x>0n?1:-1);
 if(signs[0]!==1||signs.at(-1)!==-1||signs.slice(1).filter((s,i)=>s!==signs[i]).length!==1)throw Error("sign");
 let x=0n;while(ev(a,x)>0n)x++;
 if(ev(a,x)===0n)throw Error("tie");thresholds.push(Number(x));
}
console.log({total,checks,thresholds});
```

## 4. Next

Prove coefficient positivity uniformly for arbitrary d, ideally after removing common positive rising-factor polynomials or comparing normalized adjacent port moments; current certificates establish 47 unbounded strips but not the universal q-monotonicity conjecture. The separate fixed-gap root sign pattern also suggests a possible full parameter transition theorem. Activity association of this independent note and prior outstanding notes is pending current genuine identity/authorization. No formal Result or Review.
