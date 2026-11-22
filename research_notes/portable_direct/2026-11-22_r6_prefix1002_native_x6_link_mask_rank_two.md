# PREFIX-1002 — X6 BRC 单 Link 占用门控的精确保真、秩二修复与外边界定律

Date: 2026-11-22 (+08). Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED. This is independent portable mathematical research; no shared Task CLAIM, formal PROGRESS, independent review, or P000 promotion is asserted.

## 1. Frozen inputs, type, and new question

Retain P000 V5 at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json`, native X6 affine Cell torsor, signed primitive-axis neighbours, and joint-relation observer preservation. Continue the Stage46 typed, coherent BRC *candidate* in `research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md` and PREFIX-995–1001. The signed local scattering rule at every Cell is `C[h,j]=1/6-1[h=j]` for the twelve neighbour-relative incoming/outgoing ports. An incoming neighbour label is the **opposite** of the last travelled direction. Start at chosen Cell anchor 0 with incoming neighbour `h=-e1`, corresponding to directed preparation `-e1 -> 0`. Initial norm is one.

New test: close the single geometric undirected Link `L={0,e1}` to traversal in either direction **by absorbing the attempted outgoing amplitude**, while leaving the local twelve-port Stage46 scattering coefficients unchanged. The two forbidden directed transitions are `(0,+e1)` and `(e1,-e1)`; all other transitions remain unchanged. This is an explicit diagnostic occupancy mask on an actual native X6 Link, not an assertion that a degree-renormalized local scatterer, a self-adjoint reflecting boundary, a material interaction, or the full admitted triadic feedback already uses this law.

The observer first adds **signed** amplitudes only inside a common (raw Cell displacement, final incoming-neighbour port) fibre, then sums their squares. Denote its outer positive grade mass at step n by `M_n^L`; the unmasked mass is `M_n` from PREFIX-996. The grade is the integer sum of the six raw relative displacements, not a final encoded Cell address or an extra spatial coordinate.

## 2. Theorem 1002.1 — Exact all-length one-Link outer law

Let
```
A6(m) = sum_{a in N^6, |a|=m} (m!/(a1!...a6!))^2,    A6(0)=1.
```
For every integer n>=2, the absorbing mask has exact **full signed twelve-direction** outer-grade probability

```
               4 A6(n-1) + 6 A6(n-2)
M_n^L =        --------------------- .                     (1)
                         36^n
```

At n=1, `M_1^L=5/36`, while `M_1=1/6`. Hence, for n>=2,

```
M_n^L / M_n = 2/3 + A6(n-2)/A6(n-1).                    (2)
```

**Proof.** Every length-n path ending on grade n consists entirely of positive primitive steps; a negative step would reduce the grade by two. Such positive-only paths never traverse the reverse blocked arc `e1 -> 0` and never revisit the chosen anchor after the first step. The gate therefore removes exactly the paths whose *first* positive letter is 1.

At endpoint vector k and final positive letter j, let `N_j(k)` be the ordinary path multiplicity from PREFIX-995, and `B_j(k)` the deleted first-letter-1 paths. For n>=2, where m=n-2, their exact combinatorial values are

```
N_j(k) = (n-1)! / product_i (k_i - [i=j])!,
B_j(k) = (n-2)! / product_i (k_i - [i=1] - [i=j])!,
```

with every negative factorial argument interpreted as zero multiplicity. All surviving paths retain the common positive amplitude `6^{-n}`. The correct coherent mass is `36^{-n} sum_{k,j}(N_j(k)-B_j(k))^2`, **not** the sum of the individual path squares.

First, `sum_{k,j}N_j(k)^2=6 A6(n-1)`. Second, for every fixed last j, deleting both fixed endpoint letters leaves an arbitrary length-(n-2) word, giving `sum_{k,j}B_j(k)^2=6 A6(n-2)`.

For the cross term fix the last letter j, set the free middle count vector to a with `|a|=m`, and write `N(a)=m!/a!`. The fixed-j cross sum is
`sum_a N(a) N(a+e1)`.
By multinomial recursion `N(b)=sum_i N(b-e_i)` and permutation symmetry of the six labels,

```
sum_a N(a)N(a+e1)
  = (1/6) sum_{|b|=m+1} N(b) sum_i N(b-e_i)
  = A6(m+1)/6.
```

Summing over six final j gives `sum_{k,j}N_j(k)B_j(k)=A6(n-1)`. Consequently
`sum(N-B)^2 = 6 A6(n-1)-2 A6(n-1)+6 A6(n-2)`, proving (1). Division by PREFIX-996 `M_n=6 A6(n-1)/36^n` proves (2). For n=1 five positive exits remain, each with amplitude 1/6. QED.

## 3. Corollary 1002.2 — Exact asymptotic loss with unchanged power

PREFIX-1001 proved `Q_m=A6(m)/36^m = [27/(4 pi^{5/2})] m^{-5/2}(1-5/(8m)+O(m^{-2}))`. Substitute into (1), and use the proved unmasked outer asymptotic:

```
lim_{n->infty} M_n^L/M_n = 25/36,
M_n^L ~ [25/(32 pi^{5/2})] n^{-5/2},                 (3)
M_n^L = [25/(32 pi^{5/2})] n^{-5/2}
         * (1 + 79/(40n) + O(n^{-2})).               (4)
M_n^L/M_n = 25/36 + 5/[72(n-1)] + O(n^{-2}).         (5)
```

Thus one fixed blocked Link changes the leading coherent boundary coefficient exactly, while retaining the outer-grade exponent 5/2 for this preparation and absorbing-mask rule. This is a genuine all-length comparison, not a numerical extrapolation. It uses the unchanged frozen Stage46 candidate, not a new dynamical axiom.

## 4. Theorem 1002.3 — Rank-two *joint-port* restoration of every signed grade

Write the full directed-port state as `|x,h>`, and let `T` be the unrestricted Stage46 linear propagation on finitely supported signed amplitudes. Let

```
u1=|e1,-e1>,   (v1 a)=sum_h C[h,+e1] a(0,h);
u2=|0,+e1>,    (v2 a)=sum_h C[h,-e1] a(e1,h).
U=[u1,u2], V=[v1;v2].
```

The masked operator is exactly `T_L=T-UV`. For the **formal power series in step-count z**, put `G(z)=(I-zT)^{-1}`. Then

```
G_L(z)=(I-zT_L)^{-1}
      =G(z)-z G(z)U [I_2+z V G(z)U]^{-1} V G(z).    (6)
```

**Proof.** The two rank-one terms `u_a v_a` are exactly the two forbidden directed Link transitions; hence their sum deletes all and only those amplitudes. The formal inverse is well-defined coefficientwise because `I+z V G U` has constant term `I_2`. Multiply the right-hand side of (6) by `I-zT+zUV`: the Woodbury cancellation leaves identity in every coefficient. At each fixed step n, the original X6 transfer has finite propagation from any finite-support input, so each coefficient is a finite exact rational expression. QED.

This is an exact **two-channel Schur/renewal correction** for the full signed, endpoint-and-port-resolved amplitude, preserving interference and the possibility of arbitrarily many later attempted passages. The compact 2x2 *feedback matrix* does not license deleting the unmasked source/endpoint Green functions needed by the declared observer. Equation (6) is a preservation interface, not a complexity-speedup claim.

## 5. Exact computation, contrasting first interior, and boundary

Independent integer methods: (i) twelve-direction signed-port dynamic programming, with all coefficients represented as integers over `6^n`; (ii) a direct independent enumeration of all signed words at n=1..3; and (iii) the exact `A6` collision recurrence used to check (1) up to n=300. The DP and closed-form outer mass agree for n=1..6, preserving the terminal incoming port throughout. Selected exact outputs:

| n | unmasked outer | masked outer | masked first interior (grade n-2) | masked total mass |
|---:|---:|---:|---:|---:|
| 1 | 1/6 | 5/36 | 5/6 | 35/36 |
| 2 | 1/36 | 5/216 | 175/216 | 35/36 |
| 3 | 11/1296 | 25/3888 | 2555/46656 | 44735/46656 |
| 4 | 83/23328 | 365/139968 | 1945/93312 | 201295/209952 |
| 5 | 113/62208 | 275/209952 | 5285/419904 | 1606135/1679616 |
| 6 | 3557/3359232 | 15245/20155392 | 9715/1259712 | 7226095/7558272 |

The original PREFIX-997 n=2 first interior is `5/6`; the masked value is `175/216`. Thus a single native Link modification already changes the next signed grade and global norm. Reusing PREFIX-1000's **unmasked** three-collision identity directly would be false for the masked model, whereas (6) remains valid for all signed grades. `n=300` exact collision arithmetic gives an outer mass ratio displayed as `0.694677871169`, approaching `25/36`.

Reproducibility files: `PREFIX1002_R6_PORT_OCCUPANCY_CERT.py` and `PREFIX1002_R6_CERTIFICATE.json` in this directory. The Python checker uses no floating point in equality assertions; printed ratio decimals are displays of exact Fractions. Script SHA256 of the locally executed source: `734883c6a502e965161df30f4aefc2785a3d16905be02978df9d3ac92415165e` (compare remote bytes if needed).

## 6. Scientific scope and next unresolved question

Stage46 is a same-author BRC constitutive candidate; this note supplies an analytic consequence and exact checks, not independent mathematical admission. The mask is *absorbing without local degree renormalization*. Reflection/re-emission, material-occupancy evolution, triadic field feedback, or multiple dependent Link gates have different transfer operators and require their own observer-safe tests.

**Next discriminating unit:** use (6) to eliminate endpoint/port state for the first-interior grade *under the single-Link gate*, and determine whether the resulting exact scalar can be expressed using a bounded number of six-label collision numbers or requires a genuinely new marked-return collision family. Compare an absorbing gate with a local reflection-preserving (norm-preserving) gate on the same two directed Link ports. Keep Source P000/ACTIVE and the shared owner boundary unchanged.

Historical provenance: `EM-DIRECT-FBEA5D`, `RA-3FB2D033BE6048D8712FF056` are prior contribution/Activity identifiers only. Actual current-session role, Activity CAS, CLAIM, and control inventory are to be determined by their original native receipts; the paper claims none of them. Mother objective `B_fix,odd(32) in {19,20}` remains open.
