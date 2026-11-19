# EC49FTQ — Smooth TP2 continuous kernel does not ensure stochastic order with a clipping atom

**2026-11-19 | AUTHOR_PROVED / EXACT_RATIONAL_BOUND_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED**

## Provenance, assumptions, and scientific boundary

- Frozen native BRC16943 science: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original 310 configurations, 141 named profiles, 228 observations remain intact.
- Native optimizer is inherited from EC49FTH [PR #2774](https://github.com/awdawmip/enterprise-math/pull/2774) @ `999bf1069403306b3813e0e390dae4435d7b4b8c`, an author proof not independently reviewed.
- Earlier postprocessing and conjecture under test: EC49FTP [PR #2791](https://github.com/awdawmip/enterprise-math/pull/2791) @ `a6984e3d8694406a09b90c266a739d85ff1afd55`.
- This theorem concerns *external price priors* on the same frozen optimizer. All rational checks are analytic pricing postprocessing, not new native heartbeat/BRC scientific input, native Bellman computation, native residual attribution, or classical Shor simulation.

The price box is `A=[3/4,49/64]`, `B=[7/16,57/128]`. Let `M=max_z(D-S)` and `Z=z_*(a,b)`. On the inherited high-gap stratum `m2=1469/64<m<m3=187/8`, the nonclipped density in (m,z) coordinates is

```
K_h(m,z) = (16/945) h((47-m)/945 + (44/45)z,
                      1/27-m/54 + (10/9)z),
L(m) = (8m+173)/480 < z < 3/4.
```

The clipping atom at `Z=3/4` has joint-M density

```
B_h(m) = (1/54) ∫_{x(m)}^{49/64} h(a,b(m)) da,
x(m)=(740-m)/945, b(m)=(47-m)/54.
```

In particular, for `L(m)<z<3/4` the conditional CDF is

```
F_h(z|m) = ∫_{L(m)}^z K_h(m,t)dt
           / [ ∫_{L(m)}^{3/4} K_h(m,t)dt + B_h(m) ].
```

Any positive constant normalizing the joint prior cancels.

## General smooth counterexample theorem

For *any* `m2<p<q<m3` and `L(q)<z0<3/4`, put

```
b_p=b(p), b_q=b(q), d_p=49/64-x(p)>0,
a_c(b)=(77+6b)/105,
Phi(s)=0 for s<=0, exp(-1/s^2) for s>0.
h_C(a,b)=1+C * ((b-b_q)/(b_p-b_q))^2
                 * Phi((a-a_c(b))/d_p),  C>0.
```

Then `h_C` is strictly positive and C-infinity on the whole box, with a finite positive normalizer. It is genuinely correlated: on `b=b_q`, `h_C=1` for all a; at `b=b_p` it varies with a.

On the entire nonclipped sector `a<=a_c(b)`, `h_C=1`. Hence the continuous kernel is exactly `K_h=16/945`, and all its TP2 determinants vanish (equivalently its log mixed derivative is zero), for every C. The nonclipped fiber boundaries are unchanged.

At `m=q` the perturbation vanishes everywhere, including the clipping atom, so `F_{h_C}(z0|q)>0` is the ordinary uniform-prior value independent of C. At `m=p`, however,

```
B_{h_C}(p) = (d_p/54)(1+C J),
J=∫_0^1 exp(-1/s^2) ds > 0.
```

The nonclipped numerator and denominator contributions are independent of C, so `F_{h_C}(z0|p) -> 0` as C tends to infinity. Consequently a finite C gives

```
p<q, but F_{h_C}(z0|p) < F_{h_C}(z0|q).
```

This violates the claimed conditional first-order stochastic increase of Z with M. In particular, continuous TP2 and increasing nonclipped support endpoints **alone** cannot imply the mixed stochastic order when a top clipping atom is present. Its mass must be controlled separately.

## Explicit C-infinity witness with fully rational strict certificate

Take `p=23`, `q=93/4`, `z0=719/960`, `C=1000`. These values lie in the above domain, with exact geometry

```
b_p=4/9, b_q=95/216, b_p-b_q=1/216.
x(p)=239/315, d_p=139/20160.
x(q)=2867/3780, d_q=433/60480.
L(p)=119/160, T(p)=3/4-L(p)=1/160, z0-L(p)=1/192.
L(q)=359/480, T(q)=1/480, z0-L(q)=1/960.
```

At q, h=1 identically on the relevant complete fiber, and the CDF is exactly

```
F(z0|q) = [(16/945)(1/960)] /
          [(16/945)(1/480)+(433/60480)/54]
        = 288/2741.
```

For `s in [1/2,1]`, `exp(-1/s^2)>=exp(-4)>1/81`, using `e<3`; therefore `J>1/162`. The continuous mass at p is unchanged, whereas the atom is strictly larger than `(d_p/54)(1+1000/162)`. Thus

```
F(z0|p) <
 [(16/945)(1/192)] /
 [(16/945)(1/160)+(139/20160)/54*(1+1000/162)]
 = 38880/450451
 < 288/2741 = F(z0|q).
```

The strict comparison has a positive *rational* lower margin

```
288/2741 - 38880/450451 = 23159808/1234686191 > 0.
```

No numerical quadrature, approximate exponential value, or Monte Carlo is used. The standard inequality `e<3` is only about a mathematically constructed external probability density, never a native BRC evolution operator, residual or physical comparison. Smoothness follows from flatness of `exp(-1/s^2)` at the nonpositive boundary.

## Independent all-rational C^3 witness

Replace `Phi(s)` by `max(s,0)^4`, and take `C=100`. The density is positive and globally C^3 (not C-infinity). At p, the extra atom integral is exactly `C/5` times its uniform baseline; at q it vanishes. Direct rational integration gives

```
F_poly(z0|p) = 160/5057,
F_poly(z0|q) = 288/2741,
F_poly(z0|q)-F_poly(z0|p) = 1017856/13861237 > 0.
```

It supplies an exact independent witness to the same top-atom mechanism without any nonrational integral.

## Verification and next problem

`EC49FTQ_SMOOTH_TP2_ATOM_VERIFY.py` (Python standard library) checks the exact inverse geometry, continuous density contributions, polynomial integral, C-infinity rational bound, and both strict reversals; `EC49FTQ_SMOOTH_TP2_ATOM_CERT.json` records a successful run. This check verifies the rational instances; the general theorem uses the proof above. Neither source proves independent acceptance of its inherited native Bellman parent.

**Next:** characterize necessary/sufficient mixed-law stochastic order through its continuous tail and clipping-atom ratio, without assuming global TP2. Separately, keep the genuine native BRC optimal-tree phase below `z=11/16` as an open scientific unit. Do not infer formal Task CLAIM, Result, Review, Activity or canonical-main acceptance from this independent portable branch.
