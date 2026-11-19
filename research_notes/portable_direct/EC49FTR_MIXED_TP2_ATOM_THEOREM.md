# EC49FTR — Sharp atom compatibility for nonconstant TP2 price kernels

**2026-11-19 | AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED**

## Provenance and scientific scope

This is independent portable research on external price priors for frozen BRC16943, not a native Bellman rerun or a new X6 Cell/Link/Port theorem. Frozen scientific input: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The 228-observer native optimum is inherited, author-proved and NOT_REVIEWED: [EC49FTH PR #2774](https://github.com/awdawmip/enterprise-math/pull/2774) @ `999bf1069403306b3813e0e390dae4435d7b4b8c`. Parent [EC49FTQ PR #2793](https://github.com/awdawmip/enterprise-math/pull/2793) @ `724a00032034a5f038c632096908444cc963adf8` supplied the flat-kernel criterion and smooth correlated counterexample. This note proves its nonconstant TP2 extension and a sharp universal pairwise test.

On `I=(1469/64,187/8)`, the inherited high-gap external-prior transform is:

```text
L(m)=(8m+173)/480; U=3/4.
K_h(m,z)=(16/945) h((47-m)/945+(44/45)z, 1/27-m/54+(10/9)z).
B_h(m)=(1/54) ∫_{(740-m)/945}^{49/64} h(a,(47-m)/54) da.
```

For each m, the conditional law of optimal q140 discount Z at optimized exchange gap M=m has continuous joint-M density K on L(m)<z<U plus atom with joint-M mass density B(m) at U. A positive common normalization of h cancels.

## Theorem A — exact pairwise criterion for any positive continuous kernel

Let m vary over a totally ordered set; let L(m)<U be nondecreasing, K(m,z)>0 integrable for L(m)<z<U, and B(m)>=0 finite. Set

```text
A(m) = ∫_{L(m)}^U K(m,z) dz > 0,
r(m) = B(m)/A(m),
H_m(t) = 0 (t<=L(m)),
         ∫_{L(m)}^{min(t,U)} K(m,z) dz / A(m) (L(m)<t<U),
         1 (t>=U).
Q(m,m') = sup_{L(m)<t<U} H_{m'}(t)/H_m(t),  m<m'.
```

Then **Z|m <=_st Z|m' iff (1+r(m'))/(1+r(m)) >= Q(m,m')**. There is no undefined ratio for t where H_m(t)=0: ordered L gives H_{m'}(t)=0 there too. For t<U the full conditional CDF is F_m(t)=H_m(t)/(1+r(m)); the criterion is exactly F_m(t)>=F_{m'}(t) for every t. As t approaches U from below, each H tends to 1, so Q>=1 and **r nondecreasing is always necessary**, without a TP2 hypothesis.

## Theorem B — sharp iff criterion for nonconstant TP2 kernels

Suppose in addition that K is TP2 on common supports: whenever m<m' and L(m')<s<t<U,

```text
K(m,s) K(m',t) >= K(m,t) K(m',s).
```

Then on the chosen m-domain,

```text
Z|M=m is stochastically nondecreasing in m
   IF AND ONLY IF
r(m)=B(m)/A(m) is nondecreasing.
```

**Proof.** On the overlap (L(m'),U), K(m',z)/K(m,z) is nondecreasing in z, hence the normalized later continuous density dominates the earlier overlap-normalized density in monotone likelihood ratio order and first-order stochastic order. The earlier distribution also has extra mass on (L(m),L(m')), further shifting it left. Thus H_m(t)>=H_{m'}(t) for all t, and since both tend to 1 at U, Q(m,m')=1. Apply Theorem A. Conversely the top-atom probability equals r/(1+r), which must not decrease under stochastic increase. This proof permits arbitrary nonconstant positive K and needs neither differentiability nor a uniform conditional fiber. For twice-differentiable positive K, ∂m∂z log K>=0 is sufficient for TP2 on common supports. TP2 alone does not guarantee mixed stochastic order (EC49FTQ).

## Theorem C — exact nonconstant strictly TP2 and nonproduct correlated example

Take a strictly positive joint price density, up to normalization,

```text
h(a,b)=1+a+b,  a∈[3/4,49/64], b∈[7/16,57/128].
```

This is not a product density: h*h_ab-h_a*h_b=-1. On the nonclipped region,

```text
K(m,z)=(16/945)*(2054-37m+3948z)/1890,
∂m∂z log K = 146076/(2054-37m+3948z)^2 > 0.
```

Exact integration of the inherited transform gives

```text
A(m)=(8m-187)(328m-339677)/4286520000,
B(m)=-(64m-1055)(256m-35545)/43893964800,
r(m)=-25(64m-1055)(256m-35545)/
       [256(8m-187)(328m-339677)],
r'(m)=175(86716736m²-4206719534m+128240419955)/
       [4(8m-187)²(328m-339677)²].
```

Here A(m),B(m)>0 throughout I. The numerator quadratic of r' has positive leading coefficient and discriminant **-26785873329330290364<0**, so r'(m)>0 for every real m where defined. By Theorem B the conditional optimal discount Z is strictly stochastically increasing with M throughout the high-gap interior. The continuous kernel is genuinely nonconstant and the prior genuinely dependent.

A fully rational witness uses p=23<q=93/4, t=719/960:

```text
r(p)=103058075/85026048 < r(q)=320344225/85005056;
F_p(t)=212459840/564252369;
F_q(t)=42481472/405349281;
F_p(t)-F_q(t)=20716724056922624/76239764025565563 > 0.
```

The attached standard-library Python verifier re-integrates the moving affine fibers with exact Fraction arithmetic, checks the polynomial/rational coefficients, derivative algebra, 396 TP2 minors, 99 rational parameter samples, discriminant, and the displayed witness. The analytic proof supplies the all-real conclusion; the finite checks are reproducibility evidence, not a replacement proof.

## Boundaries and next question

Theorem A is the full pairwise condition without TP2; Theorem B is the simpler necessary-and-sufficient atom ratio criterion under TP2 and ordered support, which is strictly broader than the flat-kernel case. The native BRC optimum and six-dimensional Heartbeat World assumptions are inherited unchanged, not newly tested or promoted. No formal CLAIM, Source Result, independent Review, Activity association, or canonical-main merge is asserted.

Next: obtain checkable conditions directly on the joint price prior h(a,b) implying that B_h/A_h increases; study exact strictly TP2 kernels whose atom ratio decreases; independently preserve the original native Bellman region z<11/16.
