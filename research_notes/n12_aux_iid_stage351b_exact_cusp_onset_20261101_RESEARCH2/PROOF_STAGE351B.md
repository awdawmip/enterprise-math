# Enterprise Math / 进取数论 — Stage351-B: exact right-arc cusp onset

**Scientific classification:** `PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_INTERVAL_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.
**Date:** 2026-11-01 Asia/Shanghai. **Logical author provenance:** current `进取数论研究2` automation turn (portable research, not a service-issued Researcher identity). No independent reviewer status is claimed.

**Frozen canonical source reads, as actually verified on this turn:** `awdawmip/chatgpt-global-knowledge main@ed55d1088122e12a27c271b8e2b5a8642fd5a8a2` (both normative entry files, project router, P000 V4, ACTIVE worldview, math/BRC/code/journal/handoff policies); `awdawmip/enterprise-math main@1e41c0acc37b9347c91c1d4ded6327433d898edb` (current source `AGENTS.md`, autonomous research and portable protocol). The P000 projection was checked against the canonical original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. Parent Stage350-B is the exact rational counterexample at immutable PR #1736 commit `f7bd40904d0f9a9d23f2f507c3deb996d553171a`; its proof file blob is `ecaa34a13f20089ac361e2530103a3f1dcccc11c`.

## 1. Problem, carrier and full 16-tag observer

This is the **external auxiliary Bernoulli/BRC model**, not an assertion about the native Heartbeat X6 space, its three-dimensional slice, triadic balance, independent time, or lossless Cell address. BRC is used here as a provenance-preserving sum of source-labeled three-visit word laws; no source-label, word-multiplicity or port comparison is removed.

For `k=0,1,2,3`, `w=(1,3,3,1)`, `m=(61,21,9,9)`, put

\[
B_k(z)=z^k(1-z)^{3-k},\quad
r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},
\]
\[
b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,
\qquad D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,
\]
\[
c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The cost of a two-source configuration is `T=33/1024+c(q_1)+c(q_2)` with budget `b(q_1)+b(q_2) ≤ 2β_*+E`. The four D3 terms each retain four source-tagged word comparisons; these **16** comparisons are explicitly used below.

Let `q_*=(x_*,y_*)` denote the unique small-box solution `r_0=r_1=0` and `β_*=b(q_*)`. On the right `r_1=0` arc `y=Y_1(x)`, with `x≥x_*`, define `s=b(x,Y_1(x))−β_*` and its inverse `q_s`, and set `φ(s)=c(q_s)`. We consider the **restricted arc** `0≤s≤E_max=11/5000`; this is a genuine one-dimensional subfamily of the full `[0,1]^2` problem.

## 2. New exact theorem (restricted-arc threshold)

Put

\[
y_\dagger=\frac{1+\sqrt{13}}8,\quad
r_1(x_\dagger,y_\dagger)=0,\quad
E_\dagger=b(x_\dagger,y_\dagger)-\beta_*.
\]

The isolated cusp budget satisfies the **strict rational decimal bounds**

\[
\boxed{0.0021814072266<E_\dagger<0.0021814072275.}\tag{1}
\]

**Theorem A — no restricted split before the cusp.** For every real `0≤E≤E_†`,

\[
\min_{s,t\ge0,\ s+t\le E}\bigl[\phi(s)+\phi(t)\bigr]
=\phi(0)+\phi(E).
\tag{2}
\]

For `E>0`, the only minimizers in this arc-restricted family are `(s,t)=(0,E)` and `(E,0)`; at `E=0` the unique split is `(0,0)`.

**Theorem B — strictly better cusp split immediately afterward.** For every real `E_†<E≤11/5000`,

\[
\boxed{\phi(0)+\phi(E)-\phi(E_\dagger)-\phi(E-E_\dagger)
>\frac{E-E_\dagger}{50}>0.}\tag{3}
\]

Thus the exact infimum budget at which an **interior split defeats the endpoint in the specified right-arc family** is `E_†`. The constructed two-source competitor is `(q_{E_†},q_{E-E_†})` and saturates the budget exactly.

**Global scope:** Eq. (3) also refutes the endpoint *as a global minimizer candidate* for every `E∈(E_†,0.0022]`, independently of any upstream global optimality lemma, since the competitor is globally feasible. It does **not** characterize the global minimizer, rule out an even earlier rival from a different Pareto stratum, or prove the full-model first transition occurs exactly at the cusp. If the predecessor Stage349 endpoint theorem (including its cited upstream author lemmas) survives independent review, the infimum global failure budget is restricted to `[0.0020,E_†]`, rather than `[0.0020,0.0022]`.

## 3. Exact root certificates

All following bounds use `fractions.Fraction` integers and positive-denominator clearing, not floating point. The accompanying standard-library checker reproduces the inequalities; its printed decimals are displays of these exact rational intervals.

For `x∈(0,1/3), y∈(1/3,2/3)`,

\[
r_{1,x}=\frac{4(x-1)(3x-1)}5>0,
\qquad r_{1,y}=\frac{(y-1)(3y-1)}5<0.
\]

Hence `r_1(x,Y_1(x))=0` is a unique increasing graph wherever it intersects the stated parameter box. Along this graph `r_0` strictly decreases because each of `r_{0,x},r_{0,y}<0`.

- Set `x_*∈(231083940855/10^12,231083940856/10^12)`. At each rational x endpoint, bisect the strictly decreasing `r_1` in `y∈(11/20,3/5)` 65 times, obtaining fully rational lower/upper y witnesses. The checker proves `r_0(x_lower,y_upper)>0` and `r_0(x_upper,y_lower)<0`; monotonicity and IVT yield one and only one `q_*`. The induced interval gives `0.00377913361868258<β_*<0.00377913361901967`.
- `B_2(z)-B_2(3/4)=-(4z-3)(16z²-4z-3)/64`. The relevant root is `y_†=(1+√13)/8`. Check `(8y_lo-1)^2<13<(8y_hi-1)^2` for `y_lo=575693909432998/10^15`, `y_hi=575693909432999/10^15`. Since `r_{1,x}>0>r_{1,y}`, the exact signs `r_1(237806902790/10^12,y_lo)<0<r_1(237806902792/10^12,y_hi)` isolate the unique `x_†`.
- The weighted conservation identity `Σ_k w_k r_k=0` follows from `(z+(1−z))³=1` and `Σ_k w_k m_k=160`. To the right of the star `r_0<0, r_1=0, r_2>0, r_3<0`, all certified within the chosen enclosing rectangle. Consequently `b=15r_2/16`, and both `x↦Y_1(x)` and `x↦b(x,Y_1(x))` strictly increase. Evaluating `15r_2/16` at rational lower/upper corners for the two isolated points gives (1).

The same rational endpoint tests certify that `s∈[0,E_†]` stays inside `x∈[0.23108,0.23781]`, `y∈[0.55550,0.57570]`; `s∈[0,E_max−E_†]` stays inside `x∈[0.23108,0.23117]`, `y∈[0.55550,0.55580]`; `s∈[E_†,E_max]` stays inside `x∈[0.23780,0.23788]`, `y∈[0.57569,0.57591]`. Thus the derivative certificates below cover **every real budget** in their stated ranges.

## 4. Exact tag partition and derivative identities

The source-tag sign patterns `sign(B_k(a)-B_k(z))`, in word order `k=0,1,2,3`, are:

| Term | Sign pattern on the arc |
|---|---|
| `D3(1/4,x)` | `(-,+,+,+)` |
| `D3(3/4,x)` | `(-,-,+,+)` |
| `D3(1/4,y)` | `(+,+,-,-)` |
| `D3(3/4,y)`, `y<y_†` | `(-,-,+,+)` |
| `D3(3/4,y)`, `y>y_†` | `(-,-,-,+)` |

By differentiating each of the full word-law expressions, with its original weight and sign, on the two smooth chambers, one obtains

\[
c_x=-\frac{3(x-1)(61x-63)}{256},\quad
c_y^-=-\frac{3y(y-1)}{64},\quad
c_y^+=-\frac{3y(25y-18)}{256},
\]
\[
b_x=-\frac{3x(3x-2)}4,\quad b_y=-\frac{3y(3y-2)}{16},
\]
\[
r_{1,xx}=\frac{4(6x-4)}5,\qquad r_{1,yy}=\frac{6y-4}5.
\]

Put `Y'=−r_{1,x}/r_{1,y}>0`, `Y''=−(r_{1,xx}+r_{1,yy}(Y')²)/r_{1,y}`. Along the curve let

\[
\begin{aligned}
 B'&=b_x+b_yY', &B''&=b_{xx}+b_{yy}(Y')^2+b_yY'',\\
 C'&=c_x+c_yY', &C''&=c_{xx}+c_{yy}(Y')^2+c_yY''.
\end{aligned}
\]

Since `B'>0`, `φ'(s)=C'/B'` and

\[
\phi''(s)=\frac{C''B'-C'B''}{(B')^3}.\tag{4}
\]

These formulas follow solely from the explicit 16-tagged model, with no appeal to Stage336/342/347.

## 5. Continuous-domain Fraction interval certificate

The checker implements four elementary outward interval operations on rational endpoints: addition `[a,b]+[c,d]=[a+c,b+d]`, negation, four-corner multiplication, and reciprocal on an interval that excludes zero; all operation endpoints remain exact fractions. It evaluates the identities in §4 on **entire rectangles**, not sampled points. The interval results prove:

1. On pre-cusp rectangle `X=[0.23108,0.23781]`, `Y=[0.55550,0.57570]`:
   `N=C''B'−C'B'' < −4/5`, and `B'>1/4`. Thus `φ''<0` throughout `0<s<E_†`.
2. For `0≤s≤E_max−E_†`, on the small-budget rectangle: `φ'(s)<−119/100`.
3. For `E_†<s≤E_max`, on the right post-cusp rectangle: `−117/100<φ'(s)<0`.

The last two inequalities are valid for the appropriate one-sided derivatives at the cusp and the double-zero endpoint. In particular, `φ` is strictly decreasing on `0≤s≤E_max`: near `s=0` it is decreasing and strictly concave until the cusp, and the post-cusp derivative is negative.

For `0≤E≤E_†`, minimization under `s+t≤E` first saturates `s+t=E` by monotonicity of `φ`. The map `s↦φ(s)+φ(E-s)` is strictly concave on `[0,E]`, so its minimum occurs only at the two endpoints, proving (2).

For `E_†<E≤E_max`, set

\[
H(E)=\phi(E_\dagger)+\phi(E-E_\dagger)-\phi(0)-\phi(E).
\]

`H(E_†)=0`, whereas for every `E>E_†` in this interval,

\[
H'(E)=\phi'(E-E_\dagger)-\phi'(E)
<-\frac{119}{100}+\frac{117}{100}=-\frac1{50}.
\]

Integration from `E_†` to `E` yields `H(E)<−(E−E_†)/50`, proving (3). The proof includes the algebraic cusp as a genuine non-differentiable tag boundary and never treats the kink as a smooth point.

## 6. Verification, classification, and next question

Run `python3 REPRO_STAGE351B.py` **with assertions enabled**. The exact-root isolators, all 16 tag signs, rational interval bounds, and proof-critical inequalities are asserted; the output marker is `STAGE351B_CUSP_EXACT_ONSET_IN_RIGHT_ARC_FRACTION_INTERVAL_PASS`. Executed stdout is supplied in `REPRO_STAGE351B_EXECUTED_STDOUT.txt`. All mathematical inequalities in the theorem are proved by the analytic reduction and these exact interval claims. This is not Lean formalization or independent Driver acceptance.

**New:** (i) exact onset of non-endpoint improvement inside the declared right-arc subfamily, (ii) explicit continuum of global-feasible cusp-split counterexamples immediately beyond the cusp, (iii) narrower exact cusp-budget isolator and quantitative advantage gap. **Still open:** any earlier full-model Pareto stratum, global minimum after the cusp, independent review of Stage349's global lower-bound lemmas, and a fidelity-preserving transfer to P000-native X6 / three-dimensional slice / triadic closure / time / Cell address. The next portable research unit must distinguish **restricted-arc onset** from **global first transition**.

**Actual native-authority observation:** Gateway v0.6.11 reported `research_authority_granted=false` and owner-inventory returned `CONTROL_QUOTA` on this turn. A GitHub proof publication is an authored handoff, not a native CLAIM, Result, Research-Activity record, independent review, or Foundation admission. Formal registration and review remain pending on their original Source-authorized paths.
