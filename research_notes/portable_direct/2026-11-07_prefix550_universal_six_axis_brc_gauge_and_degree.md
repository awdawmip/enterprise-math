# PREFIX-550 — Universal six-axis BRC gauge, shared 49-coordinate core, and total-degree conservation

**Date:** 2026-11-07 (Asia/Shanghai). **Line:** RS-X6-NATIVE-ROTATION-DYNAMICS; independent author scientific continuation of PREFIX-549. **Frozen science pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Inherited certified frontier:** PREFIX-549 at `7a5002e6a05f11d1b8aaaf5eb489d94529af5603`, where the six-axis BRC/gate future-histogram observer has 51 positive classes and exact field-linear minimal rank 49. **Evidence status:** AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## 1. Frozen model and observable

Use the four STARs A=(1,3,6), B=(1,4,5), C=(2,3,5), D=(2,4,6), their 48 typed phases and 144 legal directed phase edges, with two INNER/OUTER labels per step and 96 phase/previous-bit ports. The gate records two consecutive INNER bits on arrival at (A,+L1,-L3). Every phase i carries precisely one signed native direction `sigma(i)∈{±e1,...,±e6}`. Physical root signatures are the twelve `r=±e_a`, and the root of a complete native path is its initial phase direction `r=sigma(i_0)`. Seven variables `(q1,...,q6,z)` retain the six joint BRC cancellation counts and gate count, including path multiplicity.

With `sigma_a(i)` the signed indicator of axis a, the established local first-to-last BRC formula is

`tau_(a,r)(i,j)=[|sigma_a(i)|+|sigma_a(j)|-|sigma_a(j)-r_a|+|sigma_a(i)-r_a|]/2`.

We use `r=0` **only as an auxiliary algebraic transfer parameter**, not as another physical root.

## 2. Theorem A: all twelve rooted systems are Laurent-gauge conjugate

For each physical signed root r and phase i, define the integer potential

`h_(r,a)(i)=[|sigma_a(i)-r_a|-|sigma_a(i)|-|r_a|]/2`.

Each potential belongs to `{0,-1}`; it equals -1 exactly when `sigma_a(i)=r_a≠0`. Direct algebra gives, for every legal edge i→j,

`tau_(a,0)(i,j)=|sigma_a(i)|`,
`tau_(a,r)(i,j)=tau_(a,0)(i,j)+h_(r,a)(i)-h_(r,a)(j)`.

**Proof.** Subtract the formulas and collect the start- and end-phase terms. Their constants `-|r_a|` cancel. The gate factor is independent of r. This is a coefficientwise identity on each native bit-labelled transition, hence extends by multiplication to arbitrary paths. ∎

Let `Q_r` be the canonical 51×51 positive polynomial quotient of PREFIX-549, with the same classes for all twelve r. Every class consists of one fixed native phase and one/two previous-bit ports, so its potential is unambiguous. Let

`D_r=diag(∏_a q_a^{h_(r,a)(C)})`.

The same 51-class partition is congruent for the auxiliary 0-root transition `Q_0`. Therefore, over the Laurent polynomial ring,

**`Q_r=D_r Q_0 D_r^{-1}`, for every physical signed root r.**

Every nonzero monomial of `Q_0` contains exactly the single source-axis factor `q_axis(source)` and its gate factor; all twelve rooted matrices are recovered by the endpoint correction. Their actual weights remain ordinary nonnegative-exponent polynomials.

Set `v_r=D_r^{-1} 1_51`. Each component of v_r is `q_axis(r)` on a class whose current signed direction equals r, and 1 otherwise. For every physical start port p of root direction r, with class C(p), the full seven-variable generating polynomial satisfies

**`P_p^(r)(d)=q_axis(r)^{-1} (Q_0^d v_r)_(C(p))`, for every d≥0.**

The displayed Laurent expression simplifies exactly to the original polynomial. Thus a **single universal 51-coordinate transition matrix** plus twelve endpoint readout vectors computes every physically rooted joint histogram, without altering native paths or labels.

## 3. Theorem B: the 49-dimensional realization is also universal

PREFIX-549 establishes the following independent, all-length row identities in the canonical class numbering:

`F3-F4-F15+F16=0`, and `F3-F4-F17+F18=0`.

In the frozen model they also annihilate the complete rows of `Q_0`. The six involved classes 3,4,15,16,17,18 all carry the **same signed native direction +e1** (the two previous-bit variants of each of three particular native phases).

Retain class coordinates `I={0,...,50}\{16,18}`, and define the 51×49 reconstruction `E` with

`F16=-F3+F4+F15`; `F18=-F3+F4+F17`.

Define `T_0=(Q_0 E)[I,*]`. The two row relations imply the exact intertwiner

`Q_0 E=E T_0`, hence `Q_0^d E=E T_0^d` for every d. Since each v_r has equal values on the paired previous-bit classes, it lies in the image of E. Put `u_r=v_r[I]`; then `v_r=E u_r`. Consequently,

**`P_p^(r)(d)=q_axis(r)^{-1}(E T_0^d u_r)_(C(p))` for every physical start and every d≥0.**

The diagonal gauge maps commute with this particular reconstruction, because all six involved classes have the same signed direction. Writing `H_r=D_r[I,I]`, we also obtain

**`T_r=H_r T_0 H_r^{-1}` for all twelve physical roots.**

This supplies one **shared 49×49 exact symbolic transition core** and only root-dependent initial and final readout vectors. The previously independently certified 49-rank lower bound continues to characterize the declared simultaneous scalar-series observer; no new minimality premise is required. These representations retain all six-axis BRC/gate *joint histograms* under the stated readout.

## 4. Theorem C: exact total-six-axis BRC conservation law

For any legal path `i_0→...→i_d` rooted physically at `r=sigma(i_0)`, define six cumulative BRC counts `p_a=∑_{t=0}^{d-1} tau_(a,r)(i_t,i_(t+1))`. Summing Theorem A along the path yields

`p_a=∑_{t=0}^{d-1}|sigma_a(i_t)|+h_(r,a)(i_0)-h_(r,a)(i_d)`.

Exactly one native signed axis is occupied at each departure phase, so the sum over axes of the first terms equals d. The initial total potential is -1, and the terminal total potential is -1 if and only if the terminal signed direction equals the initial signed root. Therefore

**`∑_{a=1}^6 p_a=d-1+1_{sigma(i_d)=r}` for every d≥0.**

The identity includes d=0. Every monomial of a length-d six-axis BRC/gate histogram thus has total BRC degree d-1 or d (only degree 0 for d=0), and the degree equals d exactly when the terminal signed direction returns to r. For d≥1, on setting every q_a=t,

`P_p(d;t,...,t,z)=t^{d-1}[A_p(d,z)+t B_p(d,z)]`,

where A counts paths ending at a different signed direction and B counts paths ending at r, retaining the exact gate coefficients. This is a certified reduction for the declared endpoint-root-match observable. Terminal phase, native Cell identity and branch history are still retained when demanded by subsequent composition operations. ∎

## 5. Executed evidence and performance

The reproducible `PREFIX550_shared_gauge_compact_certificate.py` was constructed from the published PREFIX-549 exact native STAR code and actually executed. Output: `ALL_CHECKS_PASS`. It independently reassembles 48 phases, 144 edges and 96 ports; verifies **6,912** native bit-labelled gauge transitions, **612** 51-coordinate quotient gauge rows, **588** reduced 49-coordinate gauge rows, the full two row identities, and **864** coefficientwise seven-variable joint histogram equalities covering 48 physical starts × 2 initial bits × all lengths d=0,...,8.

A separate expanded Python implementation was also actually executed. It checks **672** complete joint histograms using independent original native axis-visit counts, endpoint BRC correction, gate count and branch labels, over all 48 starts × two bits × depths 0,...,6; its original native DP traversed **140,982** nonzero states. The expanded implementation and complete trial evidence are in the supplementary downloadable evidence archive.

**Exploratory end-to-end batch comparison** on CPython 3.13.5/Linux x86_64, three repetitions with `tracemalloc`: all 48 starts × two bits × all lengths d=0,...,7 = **768** complete polynomials / **29,498** nonzero coefficient positions. Timings include polynomial evolution, 49-basis setup when needed and full output recovery; already constructed Q_0 and Q_r are shared preprocessing. Median time / traced peak bytes:

| Method | Time (seconds) | Peak (MB) |
| --- | ---: | ---: |
| Twelve positive 51×51 Q_r matrices | 1.394061 | 5.64 |
| Twelve signed 49×49 T_r matrices | 1.428987 | 5.40 |
| Shared positive 51×51 Q_0, root seeds | 1.404419 | 6.87 |
| Shared signed 49×49 T_0, root seeds | 1.450494 | 6.85 |

All four approaches yield identical outputs. The shared gauge is a structural theorem; these particular Python implementations show similar short-horizon runtime, with additional seed and recovery overhead for universal versions. Results are exact for the frozen combinatorial candidate; benchmarks measure these implementations only.

## 6. Next discriminating research unit

**PREFIX-551:** exploit the further factorization `Q_0=diag(q_axis(C)) G(z)` to eliminate repeated seven-tuple monomial additions and batch all twelve endpoint-root vectors. Benchmark full initialization, all 48 starts and both bits, recovery and peak memory at increasing exact horizons. Then test which endpoint-root-match distinctions are already encoded by total BRC degree under the histogram observer, while retaining terminal phase and branch state for declared future-composition operations.

**Control state:** direct native Enterprise Math status and exact-task continuation returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, with `operation_sent=false`. No currently authenticated Researcher-ID or Owner was obtained; this report is independent-author mathematical material and creates no formal CLAIM, Result, Review or Foundation promotion.
