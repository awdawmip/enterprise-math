# R818 — Branching separator residuals: centered multiplicative cut and irreducible high-order parity

2026-11-26. AUTHOR_ANALYTIC_PROOF / EXACT_JS_CHECKED / NOT_REVIEWED. Independent portable TASK_RESEARCH, EM-DIRECT-82A007; own registration metadata verified by r3-20261126-r818-own-read, no run or execution authority. RUNNING inventory r3-20261126-r818-running-read was pending during derivation; no shared claim or ownership change. Frozen scientific input a72226e2430ffa4786321ac86e7f0c599d5f0389: P000 V5 blob dc84bdae6595b5e237a2ad50d8b21916adb2e447 and joint observer blob 3923890d77a02d84b772f789e6912dd14f220d14 read. Frozen Heartbeat human companion returned 404; no native phase/time computation in this auxiliary observer. Current global entry snapshot 7a4d8905da9cc4dca3d9afe8b8deb5bf0b905902; ACTIVE worldview, math/BRC/residual policies. R817 predecessor original recorded commit db15561ccc445eb80bb9eef5bdd2b2c8032954 returned 404 in this connector; its actual full text at current immutable Source a64888948bdacb5ba4e691d3eb2b783ed43f56ea:research_notes/portable_direct/R817_PROJECTIVE_PATH_RESIDUAL_AND_LONG_CHAIN_CORE_FPTAS.md (blob 941059397fcda44f8f9f33d1ac637428a03d81ae) was read. Use that actual readable copy; do not assert the inaccessible historical commit is verified.

## 1. Exact branching coordinates

Extend R817's two-terminal rational rank-one times one-entry residual factor to a star of b internally disjoint contracted arms. The center is one nonnegative joint interface group with polynomial unary-weighted/pinned observer as in R813. The external endpoint tensors are arbitrary nonnegative and may belong to a cyclic common environment. Each arm has exact factor B_i(u_i,x_i)(1-D_i I_{u_i=s_i} I_{x_i=t_i}), with B_i rank one, 0<=D_i<1, after R817. Deficient rectangular support is absorbed exactly as unary factors, zero tensors separately give zero; all supported external bits are relabeled so x_i=1 means t_i. Absorb the B_i unary weights into center and exterior. Normalize the center's full joint law mu (if its normalization is zero the original contraction is zero). Put A_i=I_{u_i=s_i}, a_i=1-D_i. The exact remaining star tensor is
 F(x)=E_mu prod_i (1-D_i A_i x_i), x in {0,1}^b.
Its multilinear extension F(t) for 0<=t_i<=1 is strictly positive (>=prod a_i). Evaluating F(t) is one unary-weighted center oracle call divided by the center normalization, not an explicit 2^b table. All underlying signed/native BRC paths, phases, branches, time order, common depth and original joint interfaces remain stored. This concerns only the fixed-charge nonnegative auxiliary Port observer.

## 2. Sharp conditional pair cross-ratio

For arbitrary frozen values of other t coordinates, absorb those factors into a probability law. For i,j with endpoints varying between 0 and 1, let X=1-D_i A_i, Y=1-D_j A_j. The conditional cross ratio is R=E(XY)/(EX EY). Then
 C_ij^(-1)<=R<=C_ij, C_ij=(1+sqrt(a_i a_j))^2/(sqrt(a_i)+sqrt(a_j))^2
 =1+D_i D_j/(a_i+a_j+2sqrt(a_i a_j)).
This bound is sharp over arbitrary central laws. Proof: let p=P(A_i=1), q=P(A_j=1), s=P(A_i=A_j=1). R=1+D_i D_j(s-pq)/((1-D_i p)(1-D_j q)). For maximization take s=min(p,q). If p<=q, the excess decreases with q at fixed p, because (1-q)/(1-D_j q) decreases; similarly for q<=p. Thus take p=q. At odds u=p/(1-p), the ratio is (1+u)(1+a_i a_j u)/((1+a_i u)(1+a_j u)); its excess is D_i D_j u/((1+a_i u)(1+a_j u)), maximized at u=1/sqrt(a_i a_j). For the reciprocal, tilt mu by Y/EY and replace Y by a_j/Y; then the same expression equals 1/R and the new variables have the same endpoint ranges. The transformation is invertible, so both extremes attainable. D_i=0 or D_j=0 gives R=1. A rational upper bound is 1+D_i D_j/(a_i+a_j+2a_i a_j).

## 3. Centered rank-one certificate, quadratic rather than linear arm cost

Use center c=(1/2,...,1/2). Set B(x)=F(c) prod_i F(c with t_i=x_i)/F(c). This is a positive rational rank-one tensor, computed using 2b+1 oracle evaluations (normalization common; one of each pair may alternatively be recovered by multilinearity). Define r_i=D_i/a_i and H=sum_{i<j}r_i r_j/16.
 Then exp(-H) B(x)<=F(x)<=exp(H)B(x) for every corner x.
Proof: under the tilted law proportional to prod_i(1-D_i A_i t_i), for distinct i,j,
 partial_ij log F(t) = D_i D_j Cov_t(A_i,A_j)/((1-D_i t_i)(1-D_j t_j)).
The absolute covariance of two Bernoulli variables is <=1/4 by Cauchy-Schwarz. Hence |partial_ij log F|<=r_i r_j/4. Telescope log F(x)-log F(c) by changing coordinates one by one. Compare each single-coordinate change with that same change with all other coordinates at c. The discrepancy is the sum of mixed rectangle integrals for previously changed coordinates. Each side length is 1/2, so each pair contributes at most r_i r_j/16. This proves the sandwich, including arbitrary correlations and zero central weights.

For an exact rational certificate when each h_ij=r_i r_j/16<1, let K0=prod_{i<j}(1-h_ij)^(-1). Since exp(h)<=1/(1-h), A=B/K0 satisfies A<=F<=K0^2 A pointwise. If H<1, a cheaper rational bound K0=1/(1-H) also works. Compute H=((sum r_i)^2-sum r_i^2)/32 in O(b) operations. If H=0, B=F exactly. In any nonnegative exterior contraction, and for any externally specified nonnegative event, Zhat<=Z<=K0^2 Zhat. Over disjoint star interiors, multiply the K0^2 factors. Normalized exterior event probabilities lie within the same overall multiplicative factor; zeros preserved. This applies to external endpoints only, not hidden internal events. Exact original tensor and repair data are retained.

For R817 arms of lengths l_i>=1, D_i<=4*125^(-l_i), so r_i<= (500/121)*125^(-l_i); each pair contribution to H is <= (500/121)^2*125^(-(l_i+l_j))/16. In a branching star this is the two-arm Steiner path length, not the weaker individual-arm linear budget. As a useful sufficient condition, for b>=2, if all l_i>=l then H<=b(b-1)*(500/121)^2*125^(-2l)/32. Thus e.g. b can grow while the certificate remains small. This is a polynomial certificate and a conditional approximation algorithm when the resulting exterior is exactly tractable. It is not an arbitrary-precision FPTAS on a fixed general graph merely because a precision-dependent cut succeeds. Complexity: 2b+1 exact polynomial oracle calls, O(b) arithmetic for H and O(b^2) for optional pair product, rational bit lengths polynomial in explicit input and oracle output length. The exterior computation cost remains explicit.

## 4. Exact higher-order log interaction coordinates

For nonempty S define L_S=sum_{U subset S}(-1)^(|S|-|U|) log F(1_U). Then log F(x)=sum_{S subset supp(x),S nonempty} L_S (F(0)=1). The multiplicative coordinates exp(L_S) are exact rational ratios of pinned oracle values. For |S|=k>=2,
 |L_S| <= k! 2^(k-1) prod_{i in S} r_i,
 and for k=2 the stronger |L_S|<=r_i r_j/4 holds.
Proof: for distinct variables, the mixed derivative of log F is the joint cumulant of the scores -D_i A_i/(1-D_i t_i), under the current tilted law. Indeed F(t+h)/F(t) is the expectation of prod_i (1+h_i score_i); coefficient extraction of its log gives the partition formula for distinct indices. In absolute value each partition contributes (|pi|-1)! prod_i r_i. The sum is <=k!2^(k-1), since (|pi|-1)!<=|pi|!, and ordered set partitions inject into a permutation with marked cuts (sort each block internally). Integrate over the unit k-cube with remaining coordinates zero to get the finite difference. Pair uses the covariance bound. For S=sum r_i with 2S<1 the total absolute log contribution of all sets with size >=m+1 (m>=1) is <= (2S)^(m+1)/(2(1-2S)), since elementary symmetric sum e_k(r)<=S^k/k!. A fixed-order truncation can be computed with O(b^m 2^m) exact rational operations/oracle calls (reuse shared queries). This is a certified multiway approximation, not claimed polynomial when m grows with input/precision. It also certifies selective weighted omission using the per-set products. For R817 path arms each k-way bound pays the sum of all k arm lengths, the star Steiner length.

## 5. Pure high-order residual obstruction, sharp multiplicative cost

Let b>=2 and the central bits be uniform on odd-parity configurations. Let all D_i in (0,1); every proper subset of A_i is independent fair Bernoulli. Then for every x except all ones, F(x)=prod_i(1-D_i x_i/2); at all ones,
 F(1)=prod_i(1-D_i/2)*(1-P), P=prod_i D_i/(2-D_i).
Proof: the odd-parity law is 2^(-b)(1-prod_i(-1)^A_i) relative to counting; factor the two expectations under independent fair bits. Every proper-subset interaction L_S with |S|>=2 is exactly zero, but L_[b]=log(1-P) is strictly negative. Thus all pairwise or lower-order readouts can miss a genuine multiway residual, even with arbitrarily small D_i. This is an auxiliary interface counterexample, not asserted to be physically realized by every Port block.

For this tensor the optimal uniform one-sided rank-one factor K* is (1-P)^(-(b-1)/b). Divide out the independent unary product. Any positive rank-one A<=F<=K A must satisfy the invariant
 prod_i F(1-e_i)/(F(1)^(b-1) F(0))=(1-P)^(-(b-1))<=K^b,
 because the same ratio for A is 1, and each numerator F/A<=K while each denominator F/A>=1. Attainment: put A(x)=(1-P)^(|x|/b) after dividing out unary product. For |x|<b, F/A=(1-P)^(-|x|/b); at all ones it equals 1. This proves sharpness including b=2. The retained high-order interaction is required even though all proper subset directions are exactly independent.

## 6. Exact verification

Deterministic JS BigInt rational comparisons were actually executed. Cases: 200 seeded nonnegative center weight tables of arity 2..6, allowing zeros, D_i in {1/8,1/32,1/128,1/512}; all external corner assignments, all pair contexts, and all eligible higher-order multiplicative inequalities (when bound <=1/2 use 1-C <= exp(L_S)<=1/(1-C)). Pair sharp inequality tested by rational squaring rather than floating square roots: for R>=1 and s=R-1>0 require D_i D_j/s-a_i-a_j >=0 and its square >=4a_i a_j. Odd parity arity 2..8 all corners and invariant checked. General theorem rests on the analytic proof; test is finite auxiliary data only. No end-to-end production algorithm, native BRC phase replay, or independent review.

```json
{
  "stats": {
    "pairSharp": 14040,
    "centerSandwich": 4960,
    "highOrder": 3960,
    "parity": 508,
    "exactParityLoss": 7
  },
  "total": 23475,
  "randomCases": 200,
  "parityCases": 7
}
```

```javascript
function verify(){
 const gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a<0n?-a:a};
 const f=(a,b=1n)=>{if(b<0n){a=-a;b=-b}if(!b)throw Error("division by zero");let g=gcd(a,b);return[a/g,b/g]};
 const add=(a,b)=>f(a[0]*b[1]+b[0]*a[1],a[1]*b[1]),neg=a=>[-a[0],a[1]],sub=(a,b)=>add(a,neg(b)),mul=(a,b)=>f(a[0]*b[0],a[1]*b[1]),div=(a,b)=>f(a[0]*b[1],a[1]*b[0]),le=(a,b)=>a[0]*b[1]<=b[0]*a[1],eq=(a,b)=>le(a,b)&&le(b,a);
 const one=f(1n),zero=f(0n),prod=a=>a.reduce(mul,one),pop=x=>{let k=0;for(;x;x&=x-1)k++;return k};
 let seed=818,st={pairSharp:0,centerSandwich:0,highOrder:0,parity:0,exactParityLoss:0},rnd=()=>((seed=(Math.imul(seed,1664525)+1013904223)>>>0)>>>16);
 const ck=(b,k)=>{if(!b)throw Error(k);st[k]++};
 function calc(w,D,t){let n=D.length,s=0n,den=w.reduce((a,b)=>a+b,0n);for(const d of D)den*=2n*d[1];for(let x=0;x<w.length;x++){let a=w[x];if(!a)continue;for(let i=0;i<n;i++)a*=2n*D[i][1]-(((x>>i)&1)?BigInt(t[i])*D[i][0]:0n);s+=a}return f(s,den)}
 function analyze(w,D){
  let n=D.length,N=1<<n,a=D.map(d=>sub(one,d)),F=Array.from({length:N},(_,x)=>calc(w,D,Array.from({length:n},(_,i)=>2*((x>>i)&1))));
  let K=one;for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){let b=div(mul(D[i],D[j]),mul(f(16n),mul(a[i],a[j])));if(!le(b,zero)&&!le(one,b))K=div(K,sub(one,b));else throw Error("bad test domain")}
  let c=Array(n).fill(1),Fc=calc(w,D,c),U=Array.from({length:n},(_,i)=>[0,2].map(t=>{let x=c.slice();x[i]=t;return div(calc(w,D,x),Fc)}));
  for(let x=0;x<N;x++){
   let B=mul(Fc,prod(U.map((u,i)=>u[(x>>i)&1])));ck(le(div(B,K),F[x])&&le(F[x],mul(B,K)),"centerSandwich");
   for(let i=0;i<n;i++)if(!(x&(1<<i)))for(let j=i+1;j<n;j++)if(!(x&(1<<j))){
    let R=div(mul(F[x],F[x|(1<<i)|(1<<j)]),mul(F[x|(1<<i)],F[x|(1<<j)]));if(le(R,one))R=div(one,R);
    let s=sub(R,one),ok=true;if(s[0]){let L=sub(div(mul(D[i],D[j]),s),add(a[i],a[j]));ok=le(zero,L)&&le(mul(f(4n),mul(a[i],a[j])),mul(L,L))}ck(ok,"pairSharp");
   }
   let k=pop(x);if(k<2)continue;
   let R=one;for(let y=x;;y=(y-1)&x){R=(k-pop(y))%2?div(R,F[y]):mul(R,F[y]);if(!y)break}
   let C=f(1n);for(let i=0;i<n;i++)if(x&(1<<i))C=mul(C,div(D[i],a[i]));let fact=1n;for(let j=2;j<=k;j++)fact*=BigInt(j);C=mul(C,f(fact*2n**BigInt(k-1)));if(k===2)C=div(prod(D.filter((_,i)=>x&(1<<i)).map((d,j)=>d)),f(1n)); // override with sharp covariance below
   if(k===2){let I=Array.from({length:n},(_,i)=>i).filter(i=>x&(1<<i));C=div(mul(D[I[0]],D[I[1]]),mul(f(4n),mul(a[I[0]],a[I[1]])))}
   if(le(C,f(1n,2n)))ck(le(sub(one,C),R)&&le(R,div(one,sub(one,C))),"highOrder");
  }
  return F;
 }
 for(let n=2;n<=6;n++)for(let rep=0;rep<40;rep++){
  let w=Array.from({length:1<<n},()=>BigInt(rnd()%10));if(w.every(x=>!x))w[0]=1n;
  let D=Array.from({length:n},()=>f(1n,BigInt([8,32,128,512][rnd()%4])));analyze(w,D)
 }
 for(let n=2;n<=8;n++){
  const N=1<<n,w=Array.from({length:N},(_,i)=>BigInt(pop(i)%2)),D=Array.from({length:n},(_,i)=>f(1n,BigInt([32,128,512][i%3]))),a=D.map(d=>sub(one,div(d,f(2n)))),p=prod(D.map(d=>div(d,sub(f(2n),d))));
  for(let x=0;x<N;x++){let B=prod(a.filter((_,i)=>x&(1<<i))),Y=calc(w,D,Array.from({length:n},(_,i)=>2*((x>>i)&1)));ck(eq(Y,x===N-1?mul(B,sub(one,p)):B),"parity")}
  // Multiplicative invariant of any rank-one approximation: product at k near-full corners divided by full^ (k-1) and empty.
  let full=calc(w,D,Array(n).fill(2)),near=prod(Array.from({length:n},(_,i)=>calc(w,D,Array.from({length:n},(_,j)=>i===j?0:2)))),power=prod(Array(n-1).fill(full));
  ck(eq(div(near,power),div(one,prod(Array(n-1).fill(sub(one,p))))),"exactParityLoss")
 }
 return {stats:st,total:Object.values(st).reduce((a,b)=>a+b,0),randomCases:200,parityCases:7};
}
console.log(JSON.stringify(verify(),null,2));
```

Next: generalize the star's Steiner-length bound to an arbitrary branching separator tree with intermediate correlated groups; seek a connected multivariate expansion avoiding b^m enumeration and establish a genuine fixed-class FPTAS. Keep general complete Port FPTAS open.
