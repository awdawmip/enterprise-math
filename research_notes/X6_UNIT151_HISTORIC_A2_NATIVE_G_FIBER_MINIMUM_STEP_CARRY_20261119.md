# X6 Unit151 — Historical A2 carrier metric, exact native-G fiber minimum, and primitive-step common-depth carry

**Status:** AUTHOR_EXACT_PROOF / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED (2026-11-19). **Task:** RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2; mother PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905.

## Exact historical and current provenance

Historical `definitions/ENTERPRISE_TRIPLE_INTERSECTION_CIRCLE_CELL_COORDINATE_SYSTEM_20260818.md` @ `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, blob `f80a9c2ebf84d0cb4feeb787493102d57d104a0c`, lines 24–28, calls three positive rays and diagonal-shift-normalized min-zero addresses native; lines 27–28 identify native length squared with `a²+b²+c²-ab-bc-ca`. The file itself declares SUPERSEDED/HISTORICAL. Its current main revision, blob `744a6d670b442447e1e9c99653fbc55c64f17579`, lines 26–33 explicitly confines these claims to the intermediate carrier era and points to the signed X6 Cell foundation. **No current source repair is needed.** The new result below supplies an exact mathematical bridge for this actual previously unitemized historical metric consumer.

The comparison uses the *selected three-axis signed slice* (z=(a,b,c,0,0,0)), not a claim that the old carrier labels were already native signed Cell labels. The task's immutable scientific baseline is `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison is `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. P000 remains unchanged. Define native signed squared length `G=a²+b²+c²`, sum `S=a+b+c`, historical A2 carrier form `Q=a²+b²+c²-ab-bc-ca`, and derived diagonal `D=(1,1,1)`. This is the 3-axis slice quotient `Z³/ZD`, **not a two-dimensional native spatial plane** and not a new native axis.

## Theorem A — exact quotient-to-native metric fiber minimum

For every integer triple (z) and (k\in\mathbb Z),

```
2Q(z) = 3G(z)-S(z)^2;
Q(z+kD) = Q(z);
G(z+kD) = [2Q(z)+(S(z)+3k)^2]/3.
```

The identity `2Q=(a-b)²+(b-c)²+(c-a)²` shows `Q>=0` and `Q=0 iff z∈ZD`, so (Q) has rank two and is a positive quadratic form only after taking the *derived* diagonal quotient. `G` is positive definite on signed (\mathbb Z^3). Consequently the historical `Q` is **not** a native metric under identity-of-coordinates, nor can the full quotient identify native Cell states.

Because `Q≡S² (mod 3)`, its residue modulo 3 is always 0 or 1. In each diagonal coset there is a **unique** representative `c([z])=z+kD` with coordinate sum in `{-1,0,1}`. Minimizing the displayed exact square over (k\in\mathbb Z) gives the universal integer formula

```
min_{k∈Z} G(z+kD) = [2Q(z)+(Q(z) mod 3)]/3 = ceil(2Q(z)/3).
```

With remaining selected signed X6 coordinates (z_4,z_5,z_6) held fixed, simply add (z_4²+z_5²+z_6²) to both sides. The metric minimum is a **derived gauge-choice on the declared quotient**, not the native length of the original (z). The integer common-depth (k), actual Cell identity and path/order/provenance remain necessary for native reconstruction and future operations.

## Theorem B — exact primitive-step carry

Let (w=c([z])), `sigma=sum(w)∈{-1,0,1}`, and `e_i` one of the first three signed unit native axes. Then

```
c([w+e_i]) = w+e_i-D * 1_{sigma=+1};
c([w-e_i]) = w-e_i+D * 1_{sigma=-1}.
```

Proof: the candidate coordinate sum changes from sigma to sigma±1. It stays in {-1,0,1} except at +2 or -2, where a unique correction by -D or +D restores the canonical range. This proves the formula for all integer triples. The canonical minimum-G section is *not* additive: `c([e_1])=e_1`, `c([e_2])=e_2`, while `c([e_1+e_2])=-e_3`. Its correction is a three-state discrete integer carry, a precise observer residual, not an extra spatial dimension or physical force.

**Smallest operational BRC witness.** Two ordered native primitive paths to `e_1+e_2=(1,1,0)` exist, native `G=2`, `N=2`, `BRC=2`; the quotient's minimal-G representative is `-e_3=(0,0,-1)` with `G=1`, `N=1`, `BRC=1`. Thus the gauge section does **not** preserve native primitive word count or endpoint identity, even though `Q(e_1+e_2)=1`. For `D=(1,1,1)`, `Q(D)=0` whereas native `G(D)=3` and signed shortest-path `BRC(D)=6`; a carrier zero class is not a native Cell return.

## Independent bounded validation

A standalone Python checker, using explicit always-on exception-based invariants, exhaustively examined all **4,913** signed triples in `[-8,8]^3`, **24,565** diagonal shifts `k=-2..2`, and **29,478** signed primitive-step transitions. Among those, **9,828** transitions exercised the carry; **16** nonzero diagonal triples had Q=0. The checker independently verified the polynomial identity, quadratic nonnegativity, quotient invariance, exact fiber minimum against nearby integer shifts, uniqueness, mod-three classification and the two BRC witnesses. Python normal, `-O`, and `-OO` outputs matched SHA256 `ba5aa3b17910aa7073f8349aa536f26abc6649c2575a3d1f086bfd6bf380647d`.

The general theorems are proved algebraically above; finite checks are regressions only. The historical executable and the original R063 six-file 512-case native benchmark were **not executed**. This report neither accepts its own mathematics on behalf of an independent Driver nor claims full 28-LP coverage.

## Claim-level classification and continuation

- **SUPERSEDE_AS_NATIVE:** intermediate 2026-08-18 `Q` as native Cell squared length, three positive-only axes and complete min-zero identity.
- **PRESERVE_CARRIER / PRESERVE_OBSERVER:** integer `A2` form and diagonal quotient, now with an exact metric-minimum and future native-step carry relation.
- **PRESERVE_PATH_BRC:** native ordered signed paths, step count, provenance and original Cell depth; do not infer these from `Q` or the min-G section.
- **NO_CURRENT_PATCH_REQUIRED:** 2026-11-19 main revision already states correct historical typing.
- **UNRESOLVED_PROVENANCE:** LP011 alleged erroneous original signed-argmax caller and LP019 alleged erroneous original natural-N-BRC subtraction caller have no established `commit:path:line`. Do not infer their existence or absence from this file.

**Next action:** consume the original Unit149 Native publish request `onhour-20261119-1000-x6-own-unit149-native-progress-v1` (failed GITHUB_PRIMARY_RATE_LIMIT); do not resubmit its failed write by ID substitution. Coordinate its legitimate retry/repair only under current control contract and actual permission. Continue exact historical/current downstream source:line inspection; Unit150 Native association remains outstanding; independent Driver review and original R063 benchmark remain separate.
