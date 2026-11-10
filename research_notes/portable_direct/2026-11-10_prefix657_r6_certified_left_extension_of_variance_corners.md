# PREFIX-657-R6 — Certified left extension of the BRC variance-maximizing corners

Date: 2026-11-10 (Asia/Shanghai). Researcher-ID: EM-DIRECT-9A3F15 / TASK_RESEARCH. Activity: RA-E8E056342FF60C4A19714BAE.
Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Exact problem, state and observer

Use the frozen signed 189-layer BRC two-informative-direction first-stop statistical observer (PREFIX-621/622). Its multiplicity-preserving survivor rows generate the moments `mu(p,z)=E[Y]`, `H(p,z)=E[Y²]/2`, `W(p,z)=2H(p,z)-mu(p,z)^2` and sampled variance `V_q(p,z)=q² W(p,z)-q mu(p,z)`. The two variables are *statistical observer parameters*, not native spatial coordinates. The actual slot counts are q=12,24; the polynomial interpolation treats real q in [12,24].

Put `L=3/20`, `R=1/6`, `I=[L,R]`, `z0=19/128`, `h=2^-18`, `a=z0-h=38911/262144`, `b=z0+h=38913/262144`, `Z=[a,b]`, `d=2^-22`, `a'=a-d=622575/4194304`, and `Z'=[a',b]`.

**Inherited version-pinned premises** (these are existing strict, model-internal author certificates, rather than new numerical claims):

* PREFIX-643: `F_q=W-mu/q`, `F_{q,pp}>1930` on I×Z; `|F_{q,ppz}|<K=6598084500`, `|mu_{pz}|<=75600` on I×[37/256,39/256], and `mu_p<322` on I×Z for q in [12,24]. Signed-binomial event score bounds `|s_n'|<20`, `|s_n''|<1500` apply where the displayed exact product tests hold.
* PREFIX-654: `D_12(z)<-226`, `D_24(z)<-785` on Z, for `D_q(z)=V_q(R,z)-V_q(L,z)`.
* PREFIX-655: `V_{12,z}(L,z)<-9476`, `V_{24,z}(L,z)<-31590` on Z; `103<mu(L,z0)<104`. Gamma dominance supplies `mu(p,z)<197`.
* PREFIX-655: old-corner bands `47425.459<V_12(L,a)<47425.460` and `192190.134<V_24(L,a)<192190.135`.

Research question: can one *strictly extend* the solved rectangles and improve the certified variance baseline without a new 189-layer replay?

## Theorem 657.1 (new continuous rectangle and two symmetric maximizers)

For every real `12<=q<=24`, `V_q` has the **unique** maximizer `(L,a')=(3/20,622575/4194304)` over I×Z'. On `B'=(I×Z')∪(Z'×I)`, exactly the two distinct points `(L,a')` and `(a',L)` are global maximizers, attaining the same value.

Across I×Z' the following are rigorously valid:

```
V_{q,pp}(p,z)>356 q²,
D_12(z)<-199, D_24(z)<-678,
V_{12,z}(L,z)<-4600, V_{24,z}(L,z)<-12090.
```

For any (p,z) in I×Z' except the maximizing corner, with `M'_q=V_q(L,a')`:

```
M'_q-V_q(p,z) >
  995q(p-L)+(1150/3)q(z-a')+178q²(p-L)(R-p).
```

The symmetric statement follows by interchanging the two informative-direction observers. At the corner both sides of the deficit formula vanish.

## Proof

**1. Score and curvature transfer.** Z' lies inside [37/256,39/256]. The exact comparisons `a'(1-a')>188/1500` and `1600a'(1-a')>188` validate the inherited score bounds `|s_n'(z)|<20` and `|s_n''(z)|<1500` for n=0,...,188. From the nonnegative negative-binomial moment kernel identities, at p=L: `|mu_z|<3780`, `|mu_zz|<283500`, `|H_zz|<26932500`. The center cap implies `mu(L,z)<104+3780(h+d)<105`. Differentiating W=2H-mu² gives `|W_zz(L,z)|<141976800` and therefore `|V_{q,zz}(L,z)|<M_q:=141976800q²+283500q` on all Z'.

On the new left interval z∈[a',a], integrate the inherited `|F_{q,ppz}|<K` from z=a: `F_{q,pp}(p,z)>1930-Kd>356`. The old strict convexity holds on Z. Thus `V_{q,pp}>356q²` on the full extended rectangle.

**2. The p-edge remains maximizing.** On the added part `|mu_p(p,z)|<322+75600d<323`, giving `|Delta mu|<323/60` for Delta f=f(R,z)-f(L,z). On I, `|s_n(R)-s_n(L)|<20(R-L)=1/3`. The negative-binomial kernel sums are ≤1 (mu) and ≤m+1 (H). Consequently `|Delta mu_z|<1260` and `|Delta H_z|<119700`. The Gamma bound gives `mu(R,z)+mu(L,z)<394` and the score bound gives `|mu_z(R,z)|+|mu_z(L,z)|<7560`. Hence

```
|Delta W_z| <
  2(119700)+1260(394)+(323/60)(7560)=776538;
|D'_q(z)| < 776538 q²+1260 q.
```

Exact arithmetic verifies `(776538·12²+1260·12)d<27` and `(776538·24²+1260·24)d<107`. Starting from z=a with the inherited strict endpoint gaps, it follows that on the new interval `D_12<-226+27=-199` and `D_24<-785+107=-678`. They remain true on the old Z. The expression `D_q(z)/q=q Delta W(z)-Delta mu(z)` is affine in q, so the two endpoint negative signs prove `D_q(z)<0` for all q∈[12,24]. Since V_q is strictly convex in p on I, its unique maximizing p-edge is L.

**3. The z-edge remains decreasing.** For z∈[a',a], integrating the just established `M_q` curvature bound from z=a gives
```
V_{12,z}(L,z)<-9476+M_12 d<-4600,
V_{24,z}(L,z)<-31590+M_24 d<-12090.
```
These also hold on Z. Since `V_{q,z}(L,z)/q=qW_z(L,z)-mu_z(L,z)` is affine in q, strict negativity at both slots extends to every real q∈[12,24]. Hence z=a' is the unique maximizing point of the p=L edge. The exact moment weights are symmetric under observer exchange (w(n,m)=w(m,n), with the corresponding H weight), so V_q(p,z)=V_q(z,p). Because b<L, the two symmetric rectangles are disjoint and exactly two maximizers occur on their union.

**4. Quantitative deficit.** The strong-convexity chord estimate with `V_{q,pp}>356q²` supplies the quadratic term `178q²(p-L)(R-p)`. By q-affine interpolation,
`[V_q(L,z)-V_q(R,z)]/q>min(199/12,678/24)=199/12`;
using R-L=1/60 yields the coefficient `995q(p-L)`. Similarly
`-V_{q,z}(L,z)/q>min(4600/12,12090/24)=1150/3`; integrate from a' to z for the second linear term. Off the maximizing corner at least one strict deficit is positive. QED.

## Corollary 657.2 (strictly improved certified baseline)

Integrate the negative transverse derivative from a' to a, with `c_12=9476` and `c_24=31590`. The strict gain is

```
V_q(L,a')-V_q(L,a) > c_q d-M_q d²/2.
q=12: 3690149263/2199023255552 > 0.0016780;
q=24: 5725333935/1099511627776 > 0.0052071.
```

The old corner lower bands therefore imply

`V_12(L,a')>47425.460`; `V_24(L,a')>192190.139`.

Both exceed the old *upper* bounds respectively at q=12 and q=24. Thus the older local maximizing corner is strictly dominated on this explicitly larger domain.

## Exact certificate and limitations

The companion Python `Fraction` script checks 37 exact assertions, including score applicability, mean cap, curvature transport, both first-coordinate endpoint gaps, both transverse derivative gaps, affine interpolation coefficients, and strict variance improvements. `ALL_CHECKS_PASS 37` on the local verified execution. Its JSON output records the exact fractions. This is an **author-derived implication certificate**, using pinned earlier strict inequalities; it is not a new run of the 189-layer survivor recurrence or the original 96-port native dynamics. Independent mathematics review and full-domain exclusion remain open.

BRC reuse classification: **REUSE_APPLIED** — frozen signed-survivor multiplicities, symmetric moment kernel, binomial score derivative bounds and observer-coordinate exchange. No source/provenance projection is made.

Pinned dependencies: PREFIX-643 @ `ae7872ca18676397fcc0dd9424fb77e08928bee7`; PREFIX-654 @ `429849fc4985a5e3b475f09b1d446ab853a15b1b`; PREFIX-655 @ `3dc372940c317cf540c96fc02b55284462549bac`; PREFIX-656 @ `5352d203d66148eb8262ff1c38d49d3f1700f510`.

**Next research unit:** use the existing signed-survivor evaluator to compute the exact derivatives at (L,a'), tighten the local curvature bound, iterate the left extension while maintaining the p-convexity, p-edge and z-gradient certificates, and then begin rigorous exclusion of the complement of the two certified boxes. The mother objective remains the full-domain sampled-variance maximum, using the exact intended parameter domain in the frozen task publication.
