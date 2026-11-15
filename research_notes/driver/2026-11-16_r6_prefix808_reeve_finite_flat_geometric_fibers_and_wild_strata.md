# PREFIX-808 Reeve observer: geometric fibers and ramification strata of the finite-flat cover

Date: 2026-11-16 (Asia/Taipei). Mathematical extension by `EM-DVR-DEBB5E`, in a source-exposed Driver context. The original named-source PREFIX-808 contribution belongs to `EM-DIRECT-4660FF`. This note is an author-side proof, **not** an independent review or Native Result. It makes no named X6 / signed-Port / Link identification.

## Exact hypotheses and inherited algebra

Use the Reeve observation family and the **proved**, source-pinned free algebra presentation from:

- `research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md`, commit `ebd02fad57e4ca25052749afdcb9bada7940b329`, blob `03e46deb12303dc8dedfb39651ffb4460a653779`.
- `research_notes/driver/2026-11-16_r6_prefix808_reeve_finite_flat_trace_discriminant_etale_locus.md`, commit `ed9518692926b53b1f5d821bcc347fc35f891a44`, blob `bdfcbe80109d7e9b9b27f2dac6c1c5cb53ffba79`.

For an arbitrary field `K` and integer `h >= 2`, let

```
R=K[U0,U1,U2,U3], A=U1 U2, B=U0 U3,
S=R  (+)  R V1  (+) ... (+) R V_(h-1).
```

The direct sum is a free **R-module** decomposition and multiplication is fixed by

```
Vr Vs = A V_(r+s)      if r+s < h,
      = A B            if r+s = h,
      = B V_(r+s-h)    if r+s > h,    (1 <= r,s < h).
```

All statements concern the finite flat morphism `f: Spec(S) -> Spec(R)` of degree `h`. For a geometric point `x` of `Spec(R)`, write `a=A(x)`, `b=B(x)` and `kappa` for an algebraically closed residue field.

## Theorem: every geometric fiber, all characteristics

**(I) The torus stratum `ab != 0`.** There is a canonical presentation after choosing the displayed generator

```
S tensor_R kappa = kappa[T]/(T^h-b/a),  T=V1/a.
```

If the characteristic does not divide `h`, this is a product of exactly `h` copies of `kappa`, hence a reduced geometric fiber with `h` distinct points.

If `char(kappa)=p>0` and `h=p^e q`, where `e>=1`, `p` does not divide `q`, then

```
T^h-b/a = (T^q-c)^(p^e),  c^(p^e)=b/a.
```

There are exactly `q` distinct geometric points, each of local length `p^e`; every such point is nonreduced. In particular, the generic cover is inseparable of inseparable degree `p^e` and separable degree `q`.

**(II) Exactly one of `a,b` vanishes.** The geometric fiber is a *single* length-`h` fat point:

```
a != 0, b=0:    kappa[T]/(T^h),  T=V1/a.
a=0, b != 0:    kappa[W]/(W^h),  W=V_(h-1)/b.
```

The maximal nilpotent ideal has nilpotence index `h`. This description is independent of the field characteristic.

**(III) Both `a,b` vanish.** The geometric fiber is the local square-zero algebra

```
kappa[Z1,...,Z_(h-1)]/(Zi Zj : 1<=i,j<=h-1).
```

It has length `h`, maximal ideal of vector-space dimension `h-1`, and square-zero maximal ideal. Hence the deepest intersection has a different infinitesimal structure from the singly branched stratum for `h>=3`. For `h=2` both presentations reduce to the length-two dual-number algebra.

**(IV) Codimension-one boundary behavior.** At the generic point of each of the four coordinate hyperplanes `Ui=0`, the induced extension of discrete valuations is totally ramified with ramification index `h`. When the residue characteristic does not divide `h`, this is tame. When it divides `h`, the generic extension has inseparable degree `p^e` as in (I). The étale-base locus remains precisely `D(U0 U1 U2 U3)` when `char K` does not divide `h`, and is empty when `char K` divides `h`, agreeing with the previously proved trace discriminant.

## Proof

First invert `A`. The inherited multiplication rule gives `Vr=A T^r` for `1<=r<h` with `T=V1/A` and `T^h=B/A`. The resulting map from `R[A^(-1)][T]/(T^h-B/A)` to `S[A^(-1)]` sends the displayed monomial basis to the fixed free basis; it is an isomorphism. Specialization at `a != 0` proves (I) and the first half of (II). Over an algebraically closed field the Frobenius factorization in (I) has `q` distinct roots because `p` does not divide `q`. Each is repeated exactly `p^e` times.

Symmetrically, invert `B` and set `W=V_(h-1)/B`. The multiplication rule, applied repeatedly, gives `W^k=V_(h-k)/B` for `1<=k<h` and `W^h=A/B`; thus

```
S[B^(-1)] ~= R[B^(-1)][W]/(W^h-A/B).
```

The basis `1,W,...,W^(h-1)` maps invertibly to `1,V_(h-1),...,V1` after inverting `B`. Specializing to `a=0,b != 0` proves the second half of (II).

If `a=b=0`, every product `Vr Vs` vanishes by its three-case definition. The surviving classes `1,V1,...,V_(h-1)` are linearly independent because `S` is free of rank `h` over `R`. This establishes the complete square-zero presentation and length in (III), not just a surjection onto it.

For (IV), at the generic point of `U0=0`, the values `U1,U2,U3` are units, so `A` is a unit and `B/A` has discrete valuation one. The polynomial `T^h-B/A` is Eisenstein at this DVR; its root is a uniformizer in the integral extension, with ramification index `h`. The same argument applies at `U3=0`. At `U1=0` or `U2=0`, use the symmetric `W^h-A/B` equation instead. The separability/tameness assertions follow from the derivative `hT^(h-1)` or `hW^(h-1)` and the characteristic. The étale locus follows equivalently from the discriminant calculated in the pinned predecessor. QED.

## Immediate observer interpretation and boundaries

The observer lattice algebra is free of constant rank `h` over the source-realizable polynomial subalgebra, but the *geometric organization* of its `h` sheets changes precisely on the explicitly identified strata. A generic boundary collapses them to one `h`-fold infinitesimal point, while the intersection of the two boundary divisors has `h-1` independent first-order nilpotent directions. In characteristic dividing `h`, the torus fiber itself has a `p^e`-fold Frobenius thickening at each of `q` points.

These are algebraic conclusions for the specified Reeve-source observer family. They do not alter the original PREFIX-808 author credit or assert an identification with an operational X6/Port/Link system. Formal Task completion, independent Result acceptance and mother-objective completion remain separately assessed.
