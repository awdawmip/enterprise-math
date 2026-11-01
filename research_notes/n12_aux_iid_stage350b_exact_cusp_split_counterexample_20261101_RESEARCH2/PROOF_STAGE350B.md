# Enterprise Math Stage350-B — exact rational counterexample beyond the tag cusp

**Date:** 2026-11-01 (Asia/Shanghai). **Scientific class:** `PORTABLE_AUTHOR_COUNTEREXAMPLE / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.

**Source pins verified within this run:** GLOBAL_KNOWLEDGE_V1 canonical `main@7d7a66283e85dfad85849dd29e6b42cd9f0408c4`; Enterprise Math canonical `main@85f90349600ef59f4cf9fcda5201d50be257772e`; portable predecessor Stage349-B in draft PR #1736 at `e6e88125099f1b829cc09733b17b1e4a9f0c9290`. The global P000 startup projection's original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` was verified; source `p000_reality_foundation.json` blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488` was also verified. `ACTIVE` worldview, real X6/three-dimensional-slice, residual fidelity and independent time are unchanged. This document concerns an **external auxiliary Bernoulli/BRC source-tag observer**, not a native X6 slice or full future-operation preserving map.

## Exact model and the question

For `k=0,1,2,3`, set `B_k(z)=z^k(1-z)^(3-k)`, `w=(1,3,3,1)`, `m=(61,21,9,9)`, and

\[
r_k(x,y)=(4B_k(x)+B_k(y))/5-m_k/160,
\qquad b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|.
\]
\[
D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,
\quad c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

Every source tag and all four words are retained (16 tagged comparisons). The two-source objective is `T=33/1024+c(q_1)+c(q_2)`. Write `q_*` for the unique solution in the small star rectangle of `r_0=r_1=0` and `β_*=b(q_*)`. For `E=11/5000`, write `q_E` for the right `r_1=0` arc point with `b(q_E)=β_*+E`.

**Exact counterexample theorem.** At `E=11/5000=0.0022`, the ordered rational configuration

\[
Q_1=\left(\frac{231139116642}{10^{12}},\frac{555684475793}{10^{12}}\right),\qquad
Q_2=\left(\frac{237806870832}{10^{12}},\frac{575693818922}{10^{12}}\right)
\]

satisfies `b(Q_1)+b(Q_2)<2β_*+11/5000` and

\[
\boxed{T(Q_1,Q_2)<T(q_*,q_E).}
\]

Therefore the Stage349 endpoint allocation **cannot extend unchanged to `E=0.0022`**. This is a constructive counterexample against that exact candidate, not a proof of the global optimum among all alternatives. It uses exact rational evaluations and certified algebraic-root enclosures, not a floating-point optimizer. The result does not require the inherited global optimality lemmas of Stages336/342/347/348.

## Lemma 1: exact double-zero star isolator

Let

```
a0 = 2310839408/10^10,   a1 = 2310839409/10^10
z0 = 555508855/10^9,    z1 = 555508860/10^9.
```

On this rectangle, `r_{1,x}>0` (since `x<1/3`), `r_{1,y}<0` (since `1/3<y<2/3`). Thus `r_1(x,Y_1(x))=0` has a unique continuous increasing graph `Y_1`. Also `r_{0,x}<0` and `r_{0,y}<0`, so `x↦r_0(x,Y_1(x))` is strictly decreasing. The exact fractions below isolate its endpoint roots:

```
for a0:  r1(a0, 555508857100/10^12)>0>r1(a0, 555508857101/10^12)
          r0(a0, 555508857101/10^12)>0
for a1:  r1(a1, 555508857418/10^12)>0>r1(a1, 555508857419/10^12)
          r0(a1, 555508857418/10^12)<0
```

The `r_1` signs at `(a_i,z0)` and `(a_i,z1)` also bracket the graph. Hence IVT and monotonicity give a unique root `q_*` in `(a0,a1)×(z0,z1)`. By `Σw_k r_k=0`, `r_0=r_1=0`, `r_2>0`, one has `β_*=15r_2(q_*)/16`. Since `B_2'(z)=z(2-3z)>0` on this box, exact rational bounds are

\[
\frac{15}{16}r_2(a_0,z_0)<\beta_*<\frac{15}{16}r_2(a_1,z_1).
\tag{A}
\]

The checker calls the two endpoints `beta_lo` and `beta_hi`.

## Lemma 2: right-arc incumbent root enclosure

Put

```
XL = 23786633/10^8, XH = 23786635/10^8
YLlo = 575862128811/10^12, YLhi = 575862128812/10^12
YHlo = 575862185396/10^12, YHhi = 575862185397/10^12.
```

Exact signs in the attached executable proof show `r1(XL,YLlo)>0>r1(XL,YLhi)` and `r1(XH,YHlo)>0>r1(XH,YHhi)`. Throughout the enclosing rectangle `r0<0<r2` and `r3<0` on `r1=0`; therefore `b=15r2/16` there. As `Y1` and `r2` increase in each argument, `x↦b(x,Y1(x))` is strictly increasing. The checker proves both endpoint inequalities **with the beta uncertainty from (A) retained**:

\[
\frac{15}{16}r_2(X_L,Y_{L,hi})<\beta_{lo}+E,
\qquad
\frac{15}{16}r_2(X_H,Y_{H,lo})>\beta_{hi}+E.
\tag{B}
\]

Consequently the exact right-arc point `q_E` exists and is unique in
`(XL,XH)×(YLlo,YHhi)`. The bounds in (B) are checked by integer arithmetic after clearing positive denominators.

## Lemma 3: audit-cost rational bound (no root evaluation)

`D_3` is total variation distance between two complete three-visit binomial word laws. Couple their three Bernoulli coordinates with the same independent uniforms. By the union bound, `D_3(u,v)≤3|u-v|`. The triangle inequality then gives the **global exact Lipschitz bound**

\[
|c(x,y)-c(x',y')|\le\tfrac34|x-x'|+\tfrac3{16}|y-y'|.\tag{C}
\]

Define the following *explicit rational* cost lower bounds:

\[
C_*^{lo}=c(a_0,z_0)-\tfrac34(a_1-a_0)-\tfrac3{16}(z_1-z_0),
\]
\[
C_E^{lo}=c(X_L,Y_{L,lo})-\tfrac34(X_H-X_L)-\tfrac3{16}(Y_{H,hi}-Y_{L,lo}).
\]

By (C), `c(q_*)≥C_*^{lo}` and `c(q_E)≥C_E^{lo}`. All terms are rational and retain the 16 source-label comparisons.

## Lemma 4: two strict exact inequalities

The attached source `REPRO_STAGE350B.py` regenerates all rational data and asserts, with `fractions.Fraction` only:

\[
\boxed{(2\beta_{lo}+11/5000)-[b(Q_1)+b(Q_2)]>\frac9{10^9}>0},\tag{D}
\]
\[
\boxed{C_*^{lo}+C_E^{lo}-[c(Q_1)+c(Q_2)]>\frac1{2\cdot10^6}>0}.\tag{E}
\]

The actual run records a budget slack above `9.81661520079×10^-9` and a **strict certified audit-cost advantage above `5.93912234565×10^-7`**; these decimals display exact rational comparisons and are not the basis of the inequalities. Combining (A)–(E) proves the theorem. The same additive `33/1024` appears in both objectives and cancels exactly.

## Mechanism: a positive tag-cusp marginal jump

The label cusp occurs at `y†=(1+√13)/8` because `B_2(y†)=B_2(3/4)=9/64`; on the right `r1=0` arc, let `x†` denote the corresponding `x` and `s†=b(x†,y†)-β_*`. The sole switching tag in the y-anchored `D_3(3/4,y)` term contributes

\[
\frac{21}{512}\left|B_2(y)-\frac9{64}\right|.
\]

Let `φ(s)=c(q_s)` and `Y'_1=-4 B'_1(x)/B'_1(y)>0`. Since `B'_2(y†)=y†(2-3y†)>0` and `b'_arc>0`, the exact one-sided derivative jump is

\[
\boxed{\phi'(s_\dagger+)-\phi'(s_\dagger-)
=\frac{21}{256}\frac{B'_2(y_\dagger)Y'_1(x_\dagger)}{b'_\text{arc}(x_\dagger)}>0.}
\]

The positive jump identifies an upward marginal kink, explaining why a split that keeps one source near the cusp can beat the endpoint allocation. The rational witness provides the required strict global-candidate comparison regardless of any numerical interpretation of the kink.

## Reproduction, boundaries and next step

Run `python3 -O` **is not permitted** because assertions provide the proof checks; run `python3 REPRO_STAGE350B.py` with assertions enabled. The executed log is `REPRO_STAGE350B_EXECUTED_STDOUT.txt` and prints `STAGE350B_E_11_OVER_5000_STRICT_RATIONAL_SPLIT_COUNTEREXAMPLE_EXACT_PASS`. Re-execution reproduced identical output. The proof is a self-contained paper derivation plus executable exact arithmetic, not formal Lean verification or independent Driver review.

**Proven:** explicit exact-rational defeat of the Stage349 endpoint-only allocation at `E=0.0022`, with certified implicit roots and strict margins. **Conditional prior result:** Stage349 author theorem supports endpoint optimality for every `E≤0.0020`, subject to its inherited Stage336/342/347/348 lemmas and independent review. Combining it with this new *unconditional model-internal counterexample* isolates any first failure of endpoint-only global optimality within `(0.0020,0.0022]` **conditional on the Stage349 theorem**. The precise threshold and global minimizing split remain open. BRC reuse: original complete labeled word laws and 16 comparisons, no total-only observer collapse. X6 native future-operator/slice/time/Cell fidelity map remains a separate unfulfilled proof obligation.

Role/source status at capture: gateway v0.6.11 reported `research_authority_granted=false`, current active-job quota 5/5. The native active owner could not be authoritatively confirmed; no CLAIM, session, Source Result, independent review or Foundation promotion is asserted by this portable artifact. Publication via governed Draft PR is storage/handoff, not native admission. 
