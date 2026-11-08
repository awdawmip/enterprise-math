# PREFIX-608-R2 — Unknown-source gate gauge and sharp excitation criterion for native X6-BRC

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR-SIDE EXACT PROOF + EXECUTED SYMPY RATIONAL CHECKS; independent review pending.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. P000 and ACTIVE worldview unchanged.
Dependencies: PREFIX-596 (original 96-port phase-sum observer), PREFIX-602 (16D common image), PREFIX-604 (12+4 split), PREFIX-605 (four residue products), PREFIX-606/607 (known-source identifiability; PR #1834, commit 066d8165a9fd9ed24c70684f99580945226d81c9).

## 1. Exact observer and initial-state model

Retain the original native 48 STAR phases, 96 bit ports, 576 labelled actions and six X6 axes, with axis weights (1,1,1,1,0,0) and arbitrary nonnegative gates. Let Q(q) be the exact native-derived 48-phase operator and D=Q(0)Q(1) its *known* two-step transient. The original nonnegative phase-sum input v is now **unknown**. Let y_0=Dv, y_t=Q(q_t)y_(t-1), q_t≥0.

From PREFIX-602 and PREFIX-604, V=im(D) has dimension 16, and there are exact rational E (48×16), K (16×48), W (16×4), L (4×16), P=WL with KE=I, LW=I. Every y∈V is E(Wc+f), c=LKy and f=(I-P)Ky. For any gate sequence:

$$
c_t=B(q_t)c_{t-1},\quad f_t=T^tf_0,\qquad
B(q)=\begin{pmatrix}
0&0&0&4(q+3)\\1&0&0&0\\0&1&0&0\\0&0&1&0
\end{pmatrix}.
$$

The factor f is gate independent and T^4=16I on it. This is the original native phase-sum **linear observation** and does not equate 48-phase summaries with entire 96-port labelled histories.

## 2. Theorem 608.1: exact gate excitation and observability

Assume the complete consecutive 48-phase states y_(t-1), y_t are observed. The gate q_t is identifiable from this pair **if and only if** c_(t-1),3 is nonzero; then

$$q_t=\frac{c_{t,0}}{4c_{t-1,3}}-3.$$

If c_(t-1),3=0, changing only q_t to any other nonnegative number changes neither y_t nor any later full 48-phase state under identical future gates.

**Proof.** The first output coordinate of B(q)c is 4(q+3)c_3; its other three outputs are c_0,c_1,c_2. If c_3≠0, the displayed inverse is unique. If c_3=0, B(q)c is independent of q. The complement f also has no gate dependence; the exact E reconstruction and future deterministic transitions preserve equality. QED.

Since all q+3 are positive, the four-cycle implies for every t≥1:

$$c_{t-1,3}\neq0\quad\Longleftrightarrow\quad c_{0,(4-t)\bmod4}\neq0.$$

Thus the nonzero initial gate coordinates select exactly the observable congruence classes of gate positions mod four. If all four coordinates of c_0 are nonzero, all gates are uniquely recovered from full states at times 0,...,n. A zero coordinate makes its corresponding infinite gate-position class unobservable even if every later complete phase output is measured.

**Nonnegative source certificate.** For the zero-based phase-basis input v=e_4, the native D gives c_0=(0,2,0,0). Thus only gate steps t≡3 mod 4 are excited. The two nonnegative eleven-gate words
(0,2,1,7,4,0,3,5,2,6,1) and (8,2,1,7,9,0,3,5,0,6,1)
have identical complete 48-phase outputs at every time from the same nonnegative original phase input; the differing steps are 1,5,9.

## 3. Theorem 608.2: unknown-source first-gate gauge

Now suppose the complete states y_1,...,y_n are observed but y_0 is not known or observed. For any c_(0,3)≠0, changing the first gate q_1 to q'_1≥0 and the initial four-coordinate component to

$$c'_{0,3}=\frac{q_1+3}{q'_1+3}\,c_{0,3}$$

while holding c_(0,0..2) and f_0 fixed leaves B(q'_1)c'_0=B(q_1)c_0. Consequently **all** complete observed phase vectors y_t, t≥1, coincide when later gates agree. The gauge is realizable with strictly positive original 48-phase sources near an interior source: D maps R^48 onto V and thus has a linear right inverse on V; sufficiently small changes of a strictly positive preimage remain strictly positive.

**Exact strictly positive witness.** Let v_i=1 for every i=0,...,47. Let v'_i=1 except v'_{28}=2501/2500 and v'_{32}=2499/2500. Both sources are strictly positive. With the same D, exact native calculation yields

$$
c_0=(9/2,4,3/2,3/4),\quad
c'_0=(9/2,4,3/2,7499/10000),\quad f'_0=f_0.
$$

Choose q_1=1 and q'_1=7503/7499. Then the first B-output coordinate is 12 for both sources and the other three coordinates agree. The initial output difference D(v'-v) is supported on zero-based phase indices 4,5,29 with values -1/1250,-1/625,-1/625, respectively. Thus distinct strictly positive sources and distinct nonnegative first gates give identical complete 48-phase output from step 1 through **arbitrary future steps**. The checker tests an explicit 12-gate continuation and all 576 coordinate equalities. Either phase-sum source can be realized as a nonnegative original 96-port source by assigning its mass to one designated bit port per phase. The underlying source-path histories are not asserted equal.

## 4. Corollary 608.3: one pre-first-step scalar is necessary and sufficient in the full-state setting

Suppose all four initial c_0 coordinates are nonzero. If full phase states y_1,...,y_n are observed, Theorem 608.1 reconstructs q_2,...,q_n from consecutive pairs. One additional scalar calibration c_(0,3) recovers

$$q_1=\frac{(LKy_1)_0}{4c_{0,3}}-3.$$

The strictly positive gauge witness proves that **zero** pre-first-step source calibrations cannot identify the first gate on a full-dimensional neighborhood of admissible sources and parameters. Therefore one real scalar is sharp *as additional pre-step calibration*, conditional on complete later phase-state observations and nonzero excitation. This is a different measurement budget from PREFIX-607's known-source n-scalar sparse-sensor scheme.

## 5. Verification and continuation

Executed exact checker: PREFIX608_R2_blind_gate_identifiability_checker.py, using original frozen STAR source construction from PREFIX-602 and the exact PREFIX-604 16D Krylov projector. Its results JSON records:
- D rank 16, the exact B(q), the split/intertwining equalities;
- explicitly positive blind-source pair, its rational gate values, the two-coordinate input perturbation and minimum source entry 2499/2500;
- 576 exact coordinate equalities for the blind pair across 12 time steps;
- 10 exact inverse-gate checks including zero and rational gates under full excitation;
- 528 phase-output equalities for 11 steps with an unexcited genuine nonnegative native source.

The universal statements follow from the displayed matrix identities and four-cycle induction; finite tests corroborate the executable and witnesses. Reuse classification: REUSE_APPLIED / REUSE_EXECUTED (PREFIX-602 native phase generator and PREFIX-604 Krylov split). No formal task CLAIM, Native Result, independent Driver review or Foundation admission is asserted.

**Next precise problem:** For an unknown gate-independent 12D initial component, determine the minimum fixed raw phase-sensor set and one-time calibration that permit sparse gate recovery; test whether a second controlled native positive probe can eliminate the first-gate source/gate gauge. Report the phase observer and original tagged-provenance scope separately; measure bit complexity when proposing an algorithm.
