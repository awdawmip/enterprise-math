# R4-EC29 — Exact one-bit future-safe repair for a positive-count X6 BRC path observer

**2026-10-26 · author-side exact derivation and independent integer checks; not a native Result, independent Driver review, or promoted Foundation theorem.**

## Source, status, and method

This unit resumes the explicitly unfinished X6 source-provenance transfer question from R4-EC28 (immutable source commit `7d6096b8cbd2bbcf2a7cf9c799009c11dc5374ed`), and retains EC27's auxiliary positive-count theorem (commit `da477200d78b9f32243cfd0024b1607659c50ced`) **without claiming that its native lift has been found**.

Pinned account canonical snapshot: `awdawmip/chatgpt-global-knowledge main@e8d65b2492cf35be071c32b0c9852487f100be07`. Read its two entry files, `projects/enterprise-math/P000_REALITY_FOUNDATION.json` (`ACTIVE_LOCKED`), ACTIVE protected worldview, and applicable math, code, BRC and research-activity rules from this same snapshot.

Pinned Enterprise Math source: `awdawmip/enterprise-math main@520517d398d10a46c55d6f106cee1db5a0e82a69`. Read current `PROJECT_DEFINITION.md`, `p000_reality_foundation.json`, native X6 foundation router, joint-observer preservation contract, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md`, BRC-only arithmetic scope, and research persistence/activity rules.

Connected GitHub repository access has push permission; native tasks/active-owner query returned `CONTROL_QUOTA`. A live native Owner, Researcher session or formal CLAIM has **not** been verified. Work is separately labelled **author-side**.

**Exact BRC carrier:** positive integer multiplicity of distinct, source-labelled ordered primitive paths, with endpoint-/grade-resolved counts and declared possible future concatenations. This is *actual finite Path-formal/N-BRC counting*, not a name assigned to an unrelated numerical propagator. No signed/phase cancellations, trigonometric values, physical residual attribution, or matrix exponential are involved.

## 1. Native-X6 typed test model

Choose a Cell anchor `c_*` in the P000 six-axis affine torsor, and its **RAW_X6 signed displacement chart**. Consider the restricted three-axis sub-torsor `c_*+Z E1+Z E2+Z E3`; coordinates along E4–E6 are explicitly unchanged by all test paths. This restricted coordinate construction is *not* asserted to be a complete native crystal-packet layer or actual heartbeat dynamics. The raw six-tuples below are **not** registered final nonnegative Cell addresses.

An ordered primitive path uses three legal native-coordinate displacements:

| step | spatial displacement | grade increment |
|---|---|---|
| A | +E1 | 0 |
| B | +E2 | 1 |
| C | +E3 | 0 |

The index `n` is the number/order of *test path steps*, carried separately from spatial axes. It is not a calibrated heartbeat interval.

Each A step has source-label `A0`; each B step has `B0`; each C has source-label `C0`, and has a second, distinct source `C1` **exactly when the immediately preceding primitive letter was A**. Initially there is no preceding A. Set `q=1` iff the last primitive letter was A, else `q=0`. A updates q to 1; B and C update q to 0. This is an explicitly **chosen test** branching law consistent with primitive signed-axis coordinate adjacency; it is *not derived from a P000 heartbeat update rule*.

The declared observation of a source-labelled path is `(n, raw X6 endpoint, grade j=#B, positive source count)`. The allowed future operations are all finite compositions of A/B/C transitions with their actual source choices. For a provenance-sensitive observer, retain the full source-label history, not just `q`.

## 2. Theorem A: exact all-depth endpoint-resolved N-BRC law

Let `W(a,b,c)` be the number of distinct source-labelled paths using a A-steps, b B-steps and c C-steps, ending at raw displacement `(a,b,c,0,0,0)` with `n=a+b+c` and grade `j=b`.

**For all integers a,b,c >= 0,**

\[
\boxed{W(a,b,c)=\sum_{r=0}^{\min(a,c)}
 \frac{(a+b+c-r)!}{r!(a-r)!\,b!\,(c-r)!}.}\tag{A1}
\]

With commuting endpoint markers `x,y,z`, grade marker `u`, and step marker `t`,

\[
\boxed{
F(t;x,y,z,u)=\sum_{a,b,c\ge0}W(a,b,c)t^{a+b+c}x^ay^bz^cu^b
=\frac1{1-t(x+uy+z)-t^2xz}.}\tag{A2}
\]

**First proof, direct source bijection.** For each undecorated A/B/C primitive word, every adjacent `AC` occurrence admits C0 or C1; other C occurrences admit only C0. Distinct `AC` occurrences cannot overlap since A and C are different symbols. Encode an occurrence with choice C1 as one *marked two-step AC atom*, and each remaining A/B/C as an unmarked single-step atom. This is a **bijection of distinct labelled BRC sources** with ordered atom words over weights `tx, tuy, tz, t²xz`. Summing all finite atom words gives the geometric series (A2). Choosing exactly r marked AC atoms leaves a-r single A, b B and c-r single C, thus n-r atoms and precisely the multinomial summand of (A1). This proves both formulas without negative source weights or truncation. QED.

**Second proof, independent typed transition.** For endpoint-/grade-graded generating polynomials, let `v_n=(v_n(0),v_n(1))^T` count the two memory states. Direct positive-branch transition enumeration gives

\[
v_{n+1}=
\begin{pmatrix}uy+z&uy+2z\\x&x\end{pmatrix}v_n,\qquad
v_0=(1,0)^T.
\]

Thus `F=(1,1)(I-tM)^{-1}v_0` equals (A2) because `det(I-tM)=1-t(x+uy+z)-t²xz` and the relevant adjugate numerator is 1. The inverse is a **formal power series identity**, not a classical physical propagation operator.

Setting x=y=z=1 yields the independent scalar count recurrence

\[
\boxed{\sum_{n\ge0}H_n(u)t^n=\frac1{1-(2+u)t-t^2},\quad
H_0=1,\ H_1=2+u,\ H_n=(2+u)H_{n-1}+H_{n-2}.}\tag{A3}
\]

For n=2 this is `5+4u+u²`; for n=3 it is `12+14u+6u²+u³`. All are positive BRC counts, not signed amplitudes.

## 3. Theorem B: matching present support AND exact current count is still insufficient

Consider the two ordered primitive paths `AB` and `BA` from the same chosen Cell. Both have `n=2`, raw X6 endpoint `(1,1,0,0,0,0)`, grade `j=1`, and **one current source-labelled realization each**. Their only difference relevant to future count transport is `q`: after AB it is 0, after BA it is 1.

Appending the **same** third native step `+E3` gives:

| history | next source branches | number | resulting raw X6 displacement |
|---|---|---:|---|
| AB + C | C0 | 1 | (1,1,1,0,0,0) |
| BA + C | C0, C1 | 2 | (1,1,1,0,0,0) |

Both updated traces have n=3, grade j=1 and the same full endpoint, yet their positive source multiplicities differ. Therefore quotienting by `(n, full RAW_X6 endpoint, grade, **current individual source multiplicity**)` does **not** preserve all declared future BRC-count observations. This improves EC28's source-multiplicity obstruction by showing that even equal current counts do not certify future safety. It is **not** a counterexample to the EC27 auxiliary kernel or to a specified native heartbeat law. QED.

## 4. Theorem C: necessary and sufficient one-bit repair, in declared scope

Augment the current observation with `q=1_{last primitive letter=A}`. The next labelled transition choices, spatial increments, grade increments and successor q depend **only** on q and the chosen next primitive letter. Induction over any finite suffix proves this augmented state is sufficient for all endpoint-/grade-resolved positive future **counts**. Conversely, q=0 and q=1 have different one-step C multiplicity (1 versus 2), witnessed at the same present spatial state and grade by AB/BA. No one-state identification can preserve that observation. Hence these two q-classes are the **minimal future-distinguishable memory partition** for this automaton's declared positive-count BRC observable.

Neither full labelled path identity, actual P000 physical dynamics, nor EC27-to-X6 source fibres are reconstructed from this bit. Such stronger observations require a stronger retained carrier. q is a *relational/history coordinate*, not an additional spatial axis.

## 5. Exact execution and limitations

Two different exact-integer implementations were run: a local Python program with explicit source-label-word enumeration, independent dynamic recurrence and factorial closed form; and the repository's executable JavaScript BigInt program `EC29_verify.js`. Both used positive labelled path transitions, not a surrogate dynamics.

In the committed JavaScript verifier, exact dynamic programming covered **all endpoint-memory states through n=25** (6,176 state entries), checked the factorial endpoint formula at **3,276 endpoint entries**, checked **351 graded coefficients** against (A3), and independently counted **165 endpoint histograms via 18,602 individually labelled histories** through n=8. All checks passed, including the exact AB/BA witness. The local Python `EC29_verify.py` and `EC29_report.json` independently reproduced these counts and the same sample rows.

The universal identities are proved by the explicit bijection, formal transfer identity and induction, **not extrapolated from n<=25**. No real native heartbeat transition was executed; no native source-to-EC27 map, Researcher CLAIM, native Result or independent Driver mathematical review exists.

## 6. Smallest independent next unit (R4-EC30)

Identify the currently declared **actual** X6 heartbeat source transition, legitimate three-dimensional layer selection and separately typed time/update. Preserve explicit third-axis increments and source labels. For candidate correspondence with EC27's auxiliary ordered-binary BRC kernel, enumerate n=2 and n=3 source fibres, test operation commutation and grade-wise multiplicity, and determine a future-safe memory repair if necessary. Until these inputs and exact fibre laws exist, `EC27_TO_NATIVE_X6_TRANSFER=UNPROVED`. Do not rebrand this toy automaton as the actual native update.

**BRC reuse:** REUSE_APPLIED to Path-formal/N-BRC and the P000 primitive X6 step carrier; COMPOSE_APPLIED to a fully exact source-memory repair theorem. No claim of external literature priority.