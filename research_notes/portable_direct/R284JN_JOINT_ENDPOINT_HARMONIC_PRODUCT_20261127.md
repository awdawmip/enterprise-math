# R284JN — Shared endpoint/harmonic product carrier and sublinear field evaluation

2026-11-27. Independent directed continuation, EM-DIRECT-0C386E / TASK_RESEARCH, NOT_REVIEWED. Own session MCP-8cd6c4fa26b9459d923ff73ba0082220 recovery r1-20261127-1603-recovery confirmed original open registration, no formal runs. Prior owner request r1-20261127-1504-owner SUCCEEDED, as of 07:29:29 UTC no LEASED rows; current r1-20261127-1603-owner submitted, pending at initial check. No shared task/claim mutation. Current normative refs: EM 87e752dcba1ee8245bdabdbb80d18d732ffbbd25 and GK a4bb2277a25da290cfdedb0e493d8f242c71eed4, P000 V5, ACTIVE worldview, joint/residual observer contracts. Auxiliary arithmetic observer only. Frozen scientific sources: R284JM at 7c96cb0b46e8d69f8c2b70b9c7903fe025ff79bc:research_notes/portable_direct/R284JM_RESONANCE_COEFFICIENT_TRIPLE_20261127.md and R284JL at e700b37ddcbcd90bf7ae887bea7d3f2795c6df9c:research_notes/portable_direct/R284JL_RESONANT_MOMENTS_AND_ENDPOINT_CHARACTER_CERTIFICATES_20261127.md. Preserve all signed coefficients and both residuals.

## 1. Exact shared product / jet identity

For odd 3<=r<=d, put w=(r-2)/2, t_0=1, t_(k+1)=t_k(k-w)/(k+w+3), T=t_(r+1), H=sum_(k=0)^r 1/(k+w+2) (JL).
Set a=r+2, b=3r+4, sigma=(-1)^((r-1)/2), S=(r-2)!! and

 D(X)=prod_(k=0)^r (a+2k+X), D=D(0), E=D'(0).

Then exactly over Q:
 T=sigma*S^2*r*a^2/(b*D), H=2E/D.
For every prime p>4d+6, all displayed factors, including S,D,b, are units, and
 chi_p(T)=chi_p(sigma*r*b*D).
Proof: clearing 2 in each t-step gives numerator prod_(k=0)^r(2k-r+2)=sigma*(r-2)!!*(r+2)!!=sigma*S^2*r*a, and denominator prod_(k=0)^r(2k+r+4)=b*D/a. Logarithmic derivative of the full composite product gives H=2E/D. The character discards only the explicitly square factors and uses chi(u^-1)=chi(u). For full T,H one inversion u=(bD)^-1 suffices: T=sigma*S^2*r*a^2*u, H=2bEu. For character plus H, omit S, retain D,E; for full value retain S. No projection to character alone is claimed to determine T. For even r JL already gives T=0 and H coefficient zero, so no odd endpoint evaluation is needed for those declared observers.

This is a joint BRC-style product/first-jet observer, not a native spatial operation. Its exact serial composition on blocks is (D,E)*(D2,E2)=(DD2,ED2+DE2); equivalently multiplication in F_p[e]/(e^2). This preserves the value and first derivative of the full composite product and is sufficient for the stated T,H observations when S is retained. Higher derivatives or individual factors cannot be recovered from this pair and are not claimed redundant. All original V,Q,A,Z and G(T,H) remain evaluable by the frozen affine coefficients.

## 2. Sublinear exact finite-field evaluation

Given r and an eligible prime p, let m=ceil(sqrt(r+1)), P(X)=prod_(i=0)^(m-1)(X+2i). A block of m consecutive factors starting at x has exact jet (P(x),P'(x)). For D use x=a+2m*i for 0<=i<floor((r+1)/m), for S use x=1+2m*i for 0<=i<floor(((r-1)/2)/m). The two lists together have O(m) points. Build P once via a balanced polynomial product tree; use one point-product tree to evaluate P and P' on these lists by recursively reducing modulo products of (X-x). Remaining fewer than m factors for each list are multiplied directly (for D also propagate derivative). Compose block jets by the exact multiplication law above. All arithmetic is modulo p; no approximation, prime-distribution assumption, or dropped residual. At an individual fixed eligible prime, both residuals and the square class follow without traversing all r+1 factors.

Complexity in FIELD operations: using Karatsuba multiplication M(n)=O(n^alpha), alpha=log_2(3), the polynomial product tree costs O(M(m) log m) (indeed the geometric sum is O(M(m))). A polynomial remainder for degree O(n) dividend and divisor can be computed by reversing polynomials, obtaining the needed truncated reciprocal via Newton g<-g(2-fg) (error squares), reversing the truncated quotient, and subtracting quotient*divisor. This costs O(M(n) log n); monic divisor guarantees its reversed constant coefficient is 1. Each evaluation tree level contains total O(m) degree and balanced sizes; summing a safe bound over levels gives O(M(m) log^2 m) field operations for the evaluations. O(m) additional scalar multiplications; final inversion and Euler character take O(log p) with binary powers. Hence O(r^(log_2(3)/2) log^2(r+2)+log p) field operations, sublinear in r in the r-dependent part, compared with direct O(r) field multiplications (using one final inversion and product jets). With near-linear polynomial multiplication the same construction gives soft-O(sqrt(r)+log p) field operations. This is an arithmetic complexity bound for residual acquisition only, not a bit-complexity, runtime-speedup or prime discovery claim; full observer coefficient construction may still dominate, especially at deep resonance.

## 3. Exact replay and evidence

Executed the JavaScript BigInt modular implementation below. Each test compares blocked D,E,S and recovered T,H,chi with independent linear numerator/denominator recurrence and direct product-jet recurrence. Small scope: odd r=3..101 and every prime 4r+7<=p<4r+87 (d=r); larger scope: r=1001,10001,100001,1000001 and first prime >=4r+7. Primes checked by complete trial division. The direct loop is only verification, excluded from algorithm complexity. Results:

```json
{
  "small": 716,
  "large": [
    {
      "r": 1001,
      "p": "4013",
      "m": 32,
      "blocks": 46,
      "T": "1086",
      "H": "1798",
      "eps": "4012"
    },
    {
      "r": 10001,
      "p": "40013",
      "m": 101,
      "blocks": 148,
      "T": "14943",
      "H": "21035",
      "eps": "40012"
    },
    {
      "r": 100001,
      "p": "400031",
      "m": 317,
      "blocks": 472,
      "T": "126693",
      "H": "108507",
      "eps": "400030"
    },
    {
      "r": 1000001,
      "p": "4000037",
      "m": 1001,
      "blocks": 1498,
      "T": "1908316",
      "H": "3876507",
      "eps": "1"
    }
  ]
}
```

```javascript
function replay(){
function calculate(r,p,check=true){
  p=BigInt(p); const mod=x=>(x%p+p)%p;
  const add=(a,b)=>{let c=Array(Math.max(a.length,b.length)).fill(0n);for(let i=0;i<c.length;i++)c[i]=mod((a[i]??0n)+(b[i]??0n));return trim(c)};
  const sub=(a,b)=>add(a,b.map(x=>mod(-x)));
  function trim(a){while(a.length&&a[a.length-1]===0n)a.pop();return a}
  function pow(a,b){let z=1n;for(;b;b>>=1n,a=mod(a*a))if(b&1n)z=mod(z*a);return z}
  function inv(a){if(!a)throw Error("zero inverse");return pow(a,p-2n)}
  function mul(a,b){
    if(!a.length||!b.length)return [];
    if(Math.min(a.length,b.length)<=16){const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]=mod(c[i+j]+a[i]*b[j]);return trim(c)}
    const m=Math.ceil(Math.max(a.length,b.length)/2), a0=a.slice(0,m),a1=a.slice(m),b0=b.slice(0,m),b1=b.slice(m);
    const lo=mul(a0,b0),hi=mul(a1,b1),mid=sub(sub(mul(add(a0,a1),add(b0,b1)),lo),hi);
    const c=Array(a.length+b.length-1).fill(0n);
    for(const [v,k] of [[lo,0],[mid,m],[hi,2*m]])for(let i=0;i<v.length;i++)if(i+k<c.length)c[i+k]=mod(c[i+k]+v[i]);
    return trim(c)
  }
  function seriesInv(f,n){let g=[inv(f[0])],k=1;while(k<n){k=Math.min(2*k,n);let z=mul(f.slice(0,k),g).slice(0,k).map(x=>mod(-x));z[0]=mod((z[0]??0n)+2n);g=mul(g,z).slice(0,k)}return g}
  function rem(f,g){if(f.length<g.length)return f.slice();let k=f.length-g.length+1;let qr=mul(f.slice().reverse().slice(0,k),seriesInv(g.slice().reverse(),k)).slice(0,k);while(qr.length<k)qr.push(0n);return sub(f,mul(qr.reverse(),g)).slice(0,g.length-1)}
  function prod(fs){if(!fs.length)return [1n];if(fs.length===1)return fs[0];let m=fs.length>>1;return mul(prod(fs.slice(0,m)),prod(fs.slice(m)))}
  function tree(xs){if(xs.length===1)return {f:[mod(-xs[0]),1n]};let m=xs.length>>1,l=tree(xs.slice(0,m)),h=tree(xs.slice(m));return {f:mul(l.f,h.f),l,h}}
  function evals(f,t,out=[]){let g=rem(f,t.f);if(!t.l)out.push(g[0]??0n);else{evals(g,t.l,out);evals(g,t.h,out)}return out}
  const m=Math.ceil(Math.sqrt(r+1)), n=r+1, nS=(r-1)/2, a=BigInt(r+2);
  const P=prod(Array.from({length:m},(_,i)=>[BigInt(2*i),1n]));
  const Pd=P.slice(1).map((x,i)=>mod(x*BigInt(i+1)));
  const nd=Math.floor(n/m),ns=Math.floor(nS/m);
  const xs=[...Array.from({length:nd},(_,i)=>a+BigInt(2*m*i)),...Array.from({length:ns},(_,i)=>1n+BigInt(2*m*i))];
  const tr=tree(xs),vals=evals(P,tr),der=evals(Pd,tr);
  let D=1n,E=0n,S=1n;
  for(let i=0;i<nd;i++){E=mod(E*vals[i]+D*der[i]);D=mod(D*vals[i])}
  for(let i=nd*m;i<n;i++){let v=a+BigInt(2*i);E=mod(E*v+D);D=mod(D*v)}
  for(let i=0;i<ns;i++)S=mod(S*vals[nd+i]);
  for(let i=ns*m;i<nS;i++)S=mod(S*BigInt(1+2*i));
  const b=BigInt(3*r+4), rr=BigInt(r), sg=((r-1)/2)%2?-1n:1n, u=inv(mod(b*D));
  const T=mod(sg*S*S*rr*a*a*u),H=mod(2n*b*E*u),eps=pow(mod(sg*rr*b*D),(p-1n)/2n);
  if(check){
    let N=1n,B=1n,DD=1n,EE=0n,SS=1n;
    for(let k=0;k<=r;k++){N=mod(N*BigInt(2*k-r+2));B=mod(B*BigInt(2*k+r+4));let x=a+BigInt(2*k);EE=mod(EE*x+DD);DD=mod(DD*x)}
    for(let k=0;k<nS;k++)SS=mod(SS*BigInt(2*k+1));
    if(D!==DD||E!==EE||S!==SS||T!==mod(N*inv(B))||H!==mod(2n*EE*inv(DD))||eps!==pow(T,(p-1n)/2n))throw Error("mismatch "+r+" "+p);
  }
  return {r,p:String(p),m,blocks:nd+ns,T:String(T),H:String(H),eps:String(eps)};
}
function prime(n){if(n<2)return false;for(let k=2;k*k<=n;k++)if(n%k===0)return false;return true}
function next(n){while(!prime(n))n++;return n}
let small=0;
for(let r=3;r<=101;r+=2)for(let p=4*r+7;p<4*r+87;p++)if(prime(p)){calculate(r,p);small++}
const large=[1001,10001,100001,1000001].map(r=>calculate(r,next(4*r+7)));
return {small,large};
}
console.log(JSON.stringify(replay(),null,2));
```

## Next
Combine this residual acquisition with the JM resonance coefficient carriers and the exact discriminant in H. Investigate whether the H discriminant can be evaluated using a cheaper coefficient representation or restricted T class; do not assume the class alone excludes a general bivariate conic. The remaining cross-window joint exceptional compatibility, all-budget equality exclusion, and inverse-polynomial real separation remain open. No independent review or formal result acceptance.
