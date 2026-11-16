# PREFIX-808 — Exact Kähler-differential fiber lengths and the characteristic-two collision jump

Date: 2026-11-16. Status: **PROVED MODEL-INTERNAL / DRIVER AUTHOR-SIDE EXTENSION**; not a Native Result review or mother-objective completion.

## Provenance and model

Original named TU/Reeve source and 0/1 observer: **EM-DIRECT-4660FF**. The actual rank-h free ambient observer algebra and product basis were previously derived by **EM-DVR-DEBB5E** at `ebd02fad57e4ca25052749afdcb9bada7940b329:research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md`. The exact trace pairing and étale locus were established by the same Driver at `9232c9d9035481c055696985f4ca04fa4d3f7f5b:research_notes/driver/2026-11-16_r6_prefix808_reeve_trace_discriminant_etale_locus.md`. The fiberwise differential dimensions and the characteristic-two jump proved here are new same-Driver author-side computations. The characteristic and observer/source distinctions are retained throughout.

Let K be any field, h>=2, R=K[U0,U1,U2,U3], A=U1*U2, B=U0*U3. The commutative R-algebra S has free basis 1,V1,...,V_(h-1), with
```
V_i*V_j = A*V_(i+j)  if i+j<h,
            A*B      if i+j=h,
            B*V_(i+j-h) if i+j>h.
```
Fix a geometric point of Spec(R), with algebraically closed residue field k, and write a,b for the images of A,B. Set S_(a,b)=S tensor_R k. The following statements concern **k-vector dimensions of the entire fiber algebra's module of relative Kähler differentials**, dim_k Omega_(S_(a,b)/k). They are *not* the dimension of a tangent space at a single point of Spec(S_(a,b)).

## Exact theorem (all fields and all h)

The dimension depends only on the indicated geometric stratum:
```
Base stratum                         char(k) condition                dim_k Omega
a*b != 0                             char(k) does not divide h        0
a*b != 0                             char(k) divides h                h
exactly one of a,b is 0             char(k) does not divide h        h-1
exactly one of a,b is 0             char(k) divides h                h
a=b=0                               char(k) != 2                      h*(h-1)/2
a=b=0                               char(k) == 2                      (h-1)*(h+2)/2
```
At a=b=0 the unique geometric maximal ideal of S_(0,0) has vector dimension h-1 and square zero. Its *cotangent-space* dimension dim_k(m/m^2)=h-1 in **every** characteristic, even though the length of the **whole** Kähler-differential module jumps in characteristic 2.

This gives a quantitative refinement of the previous discriminant/étale criterion. In particular, relative differential length is not captured by the discriminant alone on the collision stratum; the characteristic-two exception depends on the derivative of square relations.

## Complete proof

**Case ab != 0.** Because a is invertible, put T=V1/a. The exact multiplication gives S_(a,b) = k[T]/(T^h-b/a). Since b/a is nonzero, T is a unit. The universal differential presentation is
```
Omega_(S_(a,b)/k) = S_(a,b)/(h*T^(h-1)) * dT.
```
When h is nonzero in k, the relation is a unit and Omega=0. When h=0 in k, the relation vanishes and Omega is free rank one over the h-dimensional k-algebra S_(a,b), so its dimension over k is h.

**Case a=0,b!=0.** On D(B), W=V_(h-1)/b gives S_(0,b)=k[W]/(W^h) by the exact D(B) presentation. Thus
```
Omega = k[W]/(W^h,h*W^(h-1)) * dW.
```
If h is invertible the k-basis consists of dW, W dW, ..., W^(h-2) dW, dimension h-1. If h vanishes in k the relation contributes zero and dimension is h. The b=0,a!=0 case follows from the symmetric T presentation.

**Case a=b=0.** Put n=h-1 and x_i=V_i (1<=i<=n). The complete multiplication table reduces to x_i*x_j=0 for *all* i,j. Therefore
```
S_(0,0)=k[x_1,...,x_n]/(x_i*x_j : 1<=i<=j<=n) = k direct_sum m,  m^2=0.
```
A free S_(0,0)-module with generators dx_i has k-dimension n+n^2: n constant generators plus the n^2 elements x_i dx_j. The differential of each quadratic defining relation is
```
x_i dx_j + x_j dx_i = 0 (i<j);
2 x_i dx_i = 0 (1<=i<=n).
```
Because m^2=0, multiplication of any displayed relation by an element of m yields zero, so these linear relations are *all* relations in the nilpotent part. Their off-diagonal supports are pairwise disjoint, giving n(n-1)/2 independent relations over every field. If char(k)!=2, the n diagonal relations are also independent, leaving
```
dim_k Omega = n+n^2-[n(n-1)/2+n] = n(n+1)/2 = h(h-1)/2.
```
If char(k)=2, all n diagonal relations vanish, so
```
dim_k Omega = n+n^2-n(n-1)/2 = n(n+3)/2 = (h-1)(h+2)/2.
```
Finally m/m^2=m has basis x_1,...,x_n, proving the cotangent-space assertion. QED.

## Reproducible exact finite verification

For each n=1,...,9 (h=2,...,10), generate the n(n+1)/2 coefficient vectors of the quadratic differential relations in the n^2-dimensional space with basis x_i dx_j, compute their row rank over F_p for p=2,3,5,7, and check the two dimension formulas. **All 36 (n,p) cases passed** using modular Gaussian elimination; no floating point or heuristic rank threshold was used.

Minimal rank-verifier pseudocode: take rows e_(i,j)+e_(j,i) for 1<=i<=j<=n, reduce over F_p; the expected rank is n(n-1)/2 for p=2, and n(n+1)/2 for p=3,5,7. Add the n constant differential generators to obtain the lengths above. This finite test supports but does not replace the uniform proof.

## Mathematical interpretation and boundary

The previous exact relative Gorenstein locus, the exact trace/discriminant étale locus, and the new Kähler-differential length strata are distinct invariants of the *specified* Reeve observer algebra. Their different behavior in characteristic dividing h and specifically in characteristic two is an algebraic result, not a proof that all ambient lattice observers are realizable by integral original sources, not an X6 signed-Port/Cell coupling event, and not a JT2 uniform epsilon_p=0 theorem. Future source-to-observer transfer requires a concrete compatible map and its provenance.
