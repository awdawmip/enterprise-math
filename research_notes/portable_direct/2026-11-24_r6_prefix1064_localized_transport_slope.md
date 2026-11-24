# PREFIX-1064 — Localized smooth transport: an asymptotic negative-order slope bound of 79

Date 2026-11-24. AUTHOR_CONDITIONAL_EXACT_PROOF / EXACT_INTEGER_BOUND_CHECKED / NOT_REVIEWED. Independent portable continuation, original researcher EM-DIRECT-780BBE, own SID MCP-f6d93209fc8e4c5bb2c3b44f69a47174 (recovery read confirms original registration SUCCEEDED, no own run, execution_authorized=false). No formal Task CLAIM. Current owner read r6-20261124-2258-owner-read last RUNNING, no owner conclusion assumed.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; same Stage46 candidate X6 chart anchor O, incoming -e1, reversal weight -5 (phase cover 5q), other weight 1, next incoming -d, blocked Link {O,e1} both orientations without renormalization, exactly two negative steps. Full Cell, terminal port, grade, phase and branch/source relations preserved before the inherited pair contraction. Parents d91f254e8f1fc36e8f974fd5452a91144e46f570:research_notes/portable_direct/2026-11-24_r6_prefix1062_no_finite_shift_complete_monotonicity.md (blob ebc75a30458e675070dcfceef8eae9a86aa04832) and 406f0a940c3c97fc795712a8c4d5875feb4e523d:research_notes/portable_direct/2026-11-24_r6_prefix1063_linear_negative_order_bound.md (main read blob de7ab623d7409e86d6f8848c2a6ea30be4756532). No new native trajectory, external comparison or physical attribution. Exact polynomial coefficient norms below are proof bounds on the inherited observer.

## Theorem
With p_n, D(n,k), k_min(n) as in PREFIX-1063,
    
    limsup_{n->infinity} k_min(n)/n <= 79.

More precisely there exists an integer H0 such that for all h>=H0, k_min(21+h)<=26+79h. This asymptotic bound is much smaller than 10^35. The previous all-n explicit bound remains valid separately; this proof does not give a numerical H0.

## 1. Inherited discrete observer and negative witness
Write x=SS*/36, S=sum of six marked positive translations, E=x d/dx. The inherited functional is

    L(F)=36^-8 sum_{a=0}^4 CT[J_a (E+8)^a F(x)],
    D(n,k)=L(x^(n-8)(1-x)^k).

The bounded positive paired-translation contraction in PREFIX-1062 gives
    |L(F)| <= 36^-8 sum_a ||J_a||_1 sup |(E+8)^a F|.
The same inequality extends uniquely to C^4([0,1]) by polynomial approximation in C^4 (approximate fourth derivative uniformly and integrate with matching first four initial values). This extends the auxiliary observer on tests only, not the native state space.
Reuse the executed PREFIX-1062 row n=21,k=27:
    W=33922141958582819526007294811085273952324118416517596358880,
    f=x^13(1-x)^27, L(f)=-W/36^48.

## 2. Localized transport lemma (general finite order)
Let chi in C^q([0,1]) vanish for x<=a, a>0, and be nonnegative. Let w(u)=chi(1/(1+u)) for u>=0, w_j=w(j/h). For h positive integer set
    R_h(x)=x^h sum_{j>=0} binom(h+j-1,j) w(j/h)(1-x)^j.
Only j<h(1/a-1) may contribute. For x in (0,1], the binomial weights sum to one. For fixed r, Q_(h+r) denotes the same normalized binomial sum with shape h+r. The exact derivative identity from PREFIX-1063 gives
    E^l R_h = sum_{r=1}^l (-1)^(l-r) Stirling2(l,r)
        h^(rising r) x^-r Q_(h+r)[delta^r w_j], l>=1,
where delta w_j=w_j-w_(j+1). For l=0 use Q_h[w].
Repeated interval integration yields
    h^r delta^r w_j = (-1)^r integral_[0,1]^r
         w^(r)((j+s1+...+sr)/h) ds.
The functions w^(r), r<=q, are bounded and uniformly continuous on [0,infinity), since w is C^q with compact support. Under the normalized binomial weights with shape h+r the variable j/h has mean (1+r/h)(1-x)/x and variance (h+r)(1-x)/(h^2 x^2). These two identities follow by differentiating the binomial generating sum. For any epsilon>0 both the mean error and variance vanish uniformly on [epsilon,1]. Chebyshev's inequality plus uniform continuity therefore proves
    h^r Q_(h+r)[delta^r w_j] -> (-1)^r w^(r)((1-x)/x)
uniformly there, including r=0. Since h^(rising r)/h^r->1, substitution in the derivative identity shows E^l R_h->E^l chi uniformly on [epsilon,1]. The matching chain formula follows by differentiating u=(1-x)/x, Eu=-1/x, and the same signed Stirling recurrence.

Moreover the exact difference integral bounds |h^r delta^r w_j| by sup|w^(r)|, and h^(rising r)/h^r<=r!. Thus |E^l R_h|<=constant*x^-l for l<=q (l=0 bounded by sup|w|). For f=x^m(1-x)^k with m>q, every (E+c)^b f is O(x^m) near zero. Leibniz yields a uniform O(epsilon^(m-q)) bound on [0,epsilon] for all derivatives (E+c)^l(fR_h), l<=q; f chi vanishes near zero. Polynomial endpoints are interpreted by continuity. Let epsilon decrease after h grows. Therefore fR_h->f chi in all the weighted derivative seminorms sup|(E+c)^l .|, l<=q, and L(fR_h)->L(f chi) for the inherited functional (the same proof applies to any functional bounded by these seminorms). If L(f chi)<0, then for every sufficiently large h,
    L(fR_h)=sum_j binom(h+j-1,j) w(j/h) D(n0+h,k+j)<0.
All weights are nonnegative. Hence some k+j with j<h(1/a-1) is negative. This is a local-support slope theorem without assuming a signed density, smooth spectral measure or absence of critical points. All continuum tests are auxiliary proof inequalities of the already exact discrete observer.

## 3. Explicit cutoff and certificate
Take B=40, a=1/(2B)=1/80, b=1/B=1/40. Set chi=0 on [0,a], chi=1 on [b,1]; on [a,b] use u=x/a-1 and
    chi=126u^5-420u^6+540u^7-315u^8+70u^9.
Its derivative in u is 630u^4(1-u)^4; hence 0<=chi<=1 and it is C^4 across the joins. The derivative bounds in u for orders 1..4 are (3,79,1260,18900): for order r use Leibniz on 630u^4(1-u)^4 with q=r-1 and bound each u^(4-j)(1-u)^(4-q+j) by 4^-min(4-j,4-q+j). Round up the sum. Since E=(u+1)d/du and u+1<=2, Stirling expansion gives
    sup |E^l(1-chi)| <= cut_l,
    cut=(1,6,322,11034,365098).
All derivatives of the error vanish for x>=b.

For x<=b, (k)_r x^r<=1 for 0<=r<=4 since k=27 and B>=27. Expand (E+8)^l f=x^13(E+21)^l(1-x)^27 using Stirling numbers and bound (1-x)^(27-r)<=1. Thus |(E+8)^l f|<=F_l*x^13, with
    F_l=sum_{j=0}^l binom(l,j)21^(l-j) Bell_j,
    F=(1,22,485,10715,237252).
Leibniz yields |(E+8)^l[f(1-chi)]|<=M_l B^-13,
    M_l=sum_{j=0}^l binom(l,j)F_j cut_(l-j),
    M=(1,28,1071,51731,2767522).

## 4. Exact packet norm refinement
Use the parent PREFIX-1062 checker through its H construction, before the pair loop. The arrays at hs[j] are coefficients of 2H_j for powers n^0,n^1,n^2, retaining full six-axis displacements. Summing absolute coefficients gave
    port 1: (5558600,2060620,209080)
    port 2: (4960624,1960500,209080)
    support: 2072 each.
Since 4J is their signed self-pair difference, convolution of the two norm triples with themselves and addition bounds 4||J_l||_1 by
    V=(55505824429376,42358931368000,12488433742240,1681471539200,87428892800).
This is an upper bound, not a cancellation of unequal fibers. Set Z=sum_l V_l M_l=343562256894669216.
Then
    |L(f)-L(f chi)| <= Z/(4*36^8*40^13) < W/36^48.
The final inequality is verified by exact integer cross multiplication:
    Z*36^40 = 61391108848427496176208410109493956744461783206800808042242841745067587577839616
    4*W*40^13 = 91059056451489122732294720419401093682770469869358989106198924492800000000000000.
Thus L(f chi)<0. The lemma with a=1/80 yields a negative witness in every sufficiently large row 21+h, with j<79h, proving k_min(21+h)<=26+79h.

## 5. Reproduction (actually executed integer norm calculations)
At parent commit d91f254e8f1fc36e8f974fd5452a91144e46f570, in its embedded JS checker, retain code from function check() through construction of hs=Ns.map(H). Replace the remaining code beginning with const hs=Ns.map(H),J=new Map(); by the following (including the replacement hs definition and closing brace), and run console.log(check()). No moment or difference recomputation is needed:
```js
const hs=Ns.map(H), abs=x=>x<0n?-x:x;
const norms=hs.map(h=>[0,1,2].map(i=>h.reduce((s,[k,a])=>s+abs(a[i]),0n)));
const V=Array(5).fill(0n);
for(const a of norms)for(let i=0;i<3;i++)for(let j=0;j<3;j++)V[i+j]+=a[i]*a[j];
const M=[1n,28n,1071n,51731n,2767522n];
const W=33922141958582819526007294811085273952324118416517596358880n;
const Z=V.reduce((s,v,i)=>s+v*M[i],0n);
const lhs=Z*36n**40n,rhs=4n*W*40n**13n;
if(!(lhs<rhs))throw Error("cutoff bound");
return {H:hs.map(h=>h.length),norms:norms.map(a=>a.map(String)),V:V.map(String),Z:String(Z),lhs:String(lhs),rhs:String(rhs)};
}
```
The H construction was actually executed with the copied parent exact integer polynomial routines; output H, norms, V and Z matches section 4. Integer comparison was executed separately, strict=true (ratio displayed approximately 0.67419); derivative-bound integer sums were also executed, producing the listed cut,F,M. No native kernel rerun or new physical calculation. Finite arithmetic supports the infinite asymptotic proof, not a finite sample extrapolation.

## Next
Tighten the cutoff via sharper local coefficient cancellation or direct localization of L on larger x; prove an effective onset H0 if needed. Investigate positive linear lower bound, actual slope/limit and eventual fixed-k signs. The formal native kernel correspondence, independent review and mother problem remain open. Preserve the prior uniform all-n bound and all earlier evidence.
