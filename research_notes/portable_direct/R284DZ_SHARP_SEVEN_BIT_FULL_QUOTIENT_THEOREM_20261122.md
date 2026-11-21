# R284DZ — Frozen Port full-population sharp seven-bit affine quotient circuit

Date: 2026-11-22 (Asia/Shanghai)  
Status: `AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED`  
Frozen scientific input: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py` (Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`), frozen codeword SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`. R284DX and R284DY are unchanged prior discoveries.

## Theorem A: seven-bit fixed shift reconstructs all 65,536 original quotients

Let the 12 lower source variables (each in `{1,2}`) be `(u_1,a,x,y,u_2,w,b,z,u_3,g,h,r)`, with four original upper bits unrestricted, the unreduced frozen determinant `T`, and `P=17179869143`. Use the determinant's existing quantities

\[
t=6-a,\ s=13-b,\quad
u=ts-xw,\quad p_1=su_1+xu_2,\quad p_2=tu_2+wu_1.
\]

Then for **every** original 65,536-state input,

\[
\boxed{\left\lfloor\frac TP\right\rfloor=
\left\lfloor\frac{13788u-4799p_1-4854p_2+14}{128}\right\rfloor-
\mathbf1_{\{u_1=a=x=u_2=w=b=2,\ T<2879P\}}.}
\]

The exact frozen circular Port coordinate is `z=T-P\lfloor T/P\rfloor`. This replaces R284DX's 64-entry integer quotient lookup and improves R284DY's nine-bit shift to a **seven-bit fixed shift**. The exceptional correction is required for precisely 446 of the 1,024 inputs of core class 63 (the other 578 take no correction). This circuit removes division/remainder by `P` from the quotient stage, not the cost of computing the original `T` or the farthest-arc readout.

### Finite existence proof

Let `k=(u_1−1)+2(a−1)+4(x−1)+8(u_2−1)+16(w−1)+32(b−1)`. The prior R284DX exact certificate gives a constant integer `Q[k]` for all 1,024 inputs of each core class `k<63`, and the original class 63 split. For each of the 64 possible six-bit keys the companion checker computes the exact integer

`N(k)=13788u-4799p_1-4854p_2+14`

and verifies `128Q[k]≤N(k)<128(Q[k]+1)`. The least lower slack is **0**, the least upper slack is **2**. Hence `floor(N(k)/128)=Q[k]` exactly for every core class. Subtracting the sole R284DX correction proves the displayed identity.

For further verification the code enumerates all 65,536 original source states independently, computes the frozen determinant using exact Python integers, verifies the new formula against `T//P` and its residue against `T%P` on every state, and confirms the original frozen 65,536-codeword SHA-256. All checks passed.

## Theorem B: seven bits is minimal within this precise circuit language

The stated optimality is for **integer-coefficient affine numerators in the fixed feature vector** `(u,p_1,p_2,1)`, divided by `2^s`, where the **core quotient `Q[k]` must be recovered identically** for all 64 six-bit keys before applying the separately specified R284DX exception correction. It does not claim optimality among other features, nonlinear Boolean circuits, arbitrary tables, or all full-state encodings.

Suppose such an affine numerator with integers `(A,B,C,G)` and shift `s≤6` existed. Multiplying the coefficients by `2^{6-s}` would produce a valid representation with denominator **64**. It therefore suffices to disprove a denominator-64 representation.

For every core class `k` this would require

\[
64Q[k]\le Au(k)+Bp_1(k)+Cp_2(k)+G\le64Q[k]+63.
\]

Six explicit witness keys `K={3,26,37,43,61,63}` already make this integer system infeasible. Four keys `{3,26,61,63}` have the following exact feature-row matrix (columns `u,p_1,p_2,1`):

\[
M=\begin{pmatrix}
47&25&6&1\\
46&14&10&1\\
51&26&14&1\\
40&26&12&1
\end{pmatrix},
\quad
926M^{-1}=
\begin{pmatrix}
24&-2&70&-92\\
34&-80&22&24\\
-132&11&78&43\\
-260&2028&-4308&3466
\end{pmatrix}.
\]

Writing each anchor equality as `M(A,B,C,G)^t=(64Q[k]+e_k)_k` with `0≤e_k≤63` and applying the displayed exact inverse proves the **necessary integer bounds**

\[
6888\le A\le6900,\quad
-2404\le B\le-2394,\quad
-2435\le C\le-2418,\quad
-292\le G\le391.
\]

For each of the `13·11·18=2574` possible integer triples `(A,B,C)`, the full six-key system requires a common integer `G` in the intersection

\[
\bigcap_{k\in K}
[64Q[k]-Au(k)-Bp_1(k)-Cp_2(k),\
64Q[k]+63-Au(k)-Bp_1(k)-Cp_2(k)].
\]

**Every one of these 2,574 intersections is empty.** The minimum disjointness `max(lower)-min(upper)` is exactly **1**, attained for example at `(A,B,C)=(6894,-2400,-2427)` where `G≥20` and `G≤19`. The included checker derives the integer bounds from the exact inverse, exhausts all triples, and confirms the zero-feasible count. Thus no denominator 64 (nor any smaller power of two) is possible in the declared affine-feature circuit language; the explicitly verified denominator 128 is minimal.

## Evidence, limitations and next question

The checker is standard-library Python only, run alongside the prior published R284DX checker. Its finite no-go certificate is a direct exact integer proof and does not rely on numerical MILP feasibility. It performs full-universe `T//P` / `T%P` equality and original SHA checks. The theorem is limited to the unchanged frozen auxiliary Port observer; it makes no physical calibration, native six-axis transfer, general algorithmic speedup, universal information compression or independent Review claim.

Next seek a compact Boolean/integer condition for the exceptional 446 states that does not require re-evaluating `T` when the determinant is unavailable. Compare full input-construction, integer-bit precision, core feature reuse, exception comparison, R284DS labeled event-envelope preprocessing/queries and output recovery before claiming a runtime gain. A different nonlinear feature language could admit a smaller shift; its exact criterion remains open.

## Reproduce

Run `python R284DZ_sharp_seven_bit_affine_quotient_checker.py` next to `R284DX_six_bit_full_quotient_checker.py`. It emits `R284DZ_sharp_seven_bit_affine_quotient_certificate.json` with precise coefficient, 64-cell margin, full-universe equality, inverse matrix, bound ranges and 2,574-case no-go check. Current scientific status is author-proved, exact finite certified, **NOT_REVIEWED**; formal Source Activity and Task/Result status remain independent.
