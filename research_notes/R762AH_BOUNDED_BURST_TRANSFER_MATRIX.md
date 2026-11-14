# R762AH — Exact three-slot chronological BRC and a quartic transfer theorem

**Status:** AUTHOR-SIDE CONDITIONAL PROOF / EXACT FINITE VALIDATION / NOT_REVIEWED / NOT_NATIVE_ADMITTED. Date: 2026-11-14.

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. **Frozen scientific input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Continuity:** R762AC/AE/AF/AG; researcher EM-X6-3050F6 and RA-6068F717D991DF54FBBDDEED are historical source provenance, not a current authenticated CLAIM or Result. This research advances the star-model observer, not native admission of TRIADIC_CLOSURE_E.

## Exact scope and the new question

An auxiliary star has m occupied unit-capacity outer ports, distinguished source tokens s_0,...,s_(m-1), and a hub of capacity B>=2, initially and finally empty. In a shortest complete exchange each source enters once (I_i) and exits to a different port j (O_j), never back to i. The observer retains the complete order and port labels of all I/O steps, but erases the source identity of each egress. A_B(tau) is the **number of distinct compatible named source-to-port bijections**; it counts positive source-provenance BRC branches, not signed amplitudes. As established by R762AE, for a physically feasible log the source maps are precisely the perfect matchings with I_i before the paired O_j and i != j. Hub occupancy is the observed ingress-minus-egress prefix count, independent of the matching.

For m>=B define the *sliding-burst* complete log tau_(m,B) algorithmically:

1. Perform I_0,I_1,...,I_(B-1).
2. For j=0,...,m-B, perform O_j, then perform I_(B+j) **if B+j<m**.
3. Perform O_(m-B+1),...,O_(m-1).

All outputs are ordered increasingly; the occupancy never exceeds B. In particular tau_(m,3)=I_0 I_1 I_2 O_0 I_3 O_1 I_4 O_2 ... I_(m-1) O_(m-3) O_(m-2) O_(m-1), with the interleaving understood by the algorithm above.

Let f_(m,B)=A_B(tau_(m,B)). Its source/destination matrix is the restricted 0/1 matrix

M_(m,B)(i,j)=1 if and only if i != j and i <= j+B-1.

## Theorem AH1: a finite transfer carrier for every fixed buffer B

For B>=2, m>=B, there are a fixed nonnegative integral matrix T_B of size 2^(B-1) and a fixed terminal vector t_B, depending only on B, such that

f_(m,B) = e_full^T T_B^(m-B+1) t_B,

where e_full is the state in which all initial B-1 sources of the active window remain unused. Consequently the sliding-fiber sequence at each fixed B obeys some homogeneous integral recurrence of order at most 2^(B-1), and has a rational ordinary generating function.

**Proof.** Before the new ingress preceding output O_j, precisely j source identities have been assigned to outputs 0,...,j-1, while j+B-1 source identities 0,...,j+B-2 have ingressed. Hence exactly B-1 sources remain unused. Track the subset S of the window source indices j,...,j+B-2 that remain unused; there are at most 2^(B-1) possible subsets. The number of unused older sources i<j is c=B-1-|S|. These older identities are distinct, but no later output can have their ID as its own port label; they are therefore equivalent **only for future diagonal exclusions** and contribute multiplicity c.

Ingress the new source j+B-1. Output O_j must choose either one of c older unused sources, one of the remaining window sources j+r (r>0), or the new source j+B-1. It may never choose source j. Shift the window forward; the new highest-window bit is set except when the newly ingressed source was selected. These transitions, with the explicit old-source multiplicity, define the fixed integral matrix T_B. After the final ingress, exactly B-1 outputs remain. Their distinct older/window source matchings, excluding identical source/port labels, depend only on the last subset S, giving a fixed terminal vector t_B. Each compatible source bijection corresponds to exactly one such weighted state path and vice versa. Thus the formula is exact. Cayley–Hamilton and the resolvent of T_B give the recurrence and rational generating function. QED.

This is a *special-form source-provenance algorithm*. State-space complexity is fixed in m when B is fixed, but integer bit lengths grow with m; it does **not** solve a general permanent in polynomial time.

## Theorem AH2: explicit quartic recurrence for B=3

Order the two-bit window states numerically 0=00, 1=10, 2=01, 3=11, where bit 0 represents source j and bit 1 represents source j+1. The exact row-to-column transfer and tail vector are

\[
T_3=
\begin{pmatrix}
1&0&2&0\\
1&0&1&0\\
0&1&1&1\\
0&1&1&0
\end{pmatrix},
\quad t_3=(2,1,1,1)^\mathsf{T},\quad e_{\rm full}^\mathsf{T}=(0,0,0,1).
\]

The tail coefficient 2 counts two ways to place two distinct old tokens into the final two ports; each other state permits one tail matching. The characteristic polynomial is

\[
\det(\lambda I-T_3)=\lambda^4-2\lambda^3-\lambda^2-\lambda-1.
\]

Therefore with f_m=f_(m,3) for m>=3,

\[
f_3=2,\ f_4=6,\ f_5=15,\ f_6=39,\qquad
\boxed{f_m=2f_{m-1}+f_{m-2}+f_{m-3}+f_{m-4}\ \ (m\ge7).}
\]

Extending f_2=1 for the two-port case (capacity effectively 2), the ordinary generating function is

\[
\boxed{\sum_{m\ge2}f_m x^{m-2}=\frac{1+x^2}{1-2x-x^2-x^3-x^4}}.
\]

These statements follow by direct matrix multiplication and Cayley–Hamilton. The transition graph is irreducible and has a self-loop, so f_m grows at the Perron rate given by the unique largest positive root of the quartic (~2.59205279238617). The root is **only** a combinatorial growth rate, not a native physical or temporal scale.

## Fully finite check (not an unbounded maximum theorem)

Enumerate all physically feasible complete logs with hub capacity 3 for m=2,...,10, normalized by renumbering source labels in their first-ingress order. This renaming preserves each fiber and is exhaustive modulo the simultaneous permutation of port and source labels. Complete exact physical state dynamic programming gives:

| m | normalized realizable logs | max A_3(tau) | sliding f_m |
|---:|---:|---:|---:|
| 2 | 2 | 1 | 1 |
| 3 | 10 | 2 | 2 |
| 4 | 54 | 6 | 6 |
| 5 | 290 | 15 | 15 |
| 6 | 1,558 | 39 | 39 |
| 7 | 8,370 | 101 | 101 |
| 8 | 44,966 | 262 | 262 |
| 9 | 241,570 | 679 | 679 |
| 10 | 1,297,782 | 1,760 | 1,760 |

This is **1,594,602** normalized physical complete logs. For every m<=10, the sliding log attains the observed maximum. **Open conjecture:** whether this is the global maximum for all m>10. No universal maximality is claimed.

The accompanying Python 3 standard-library verifier independently compares (1) a direct subset permanent, (2) the fixed-window transfer recurrence, and (3) named physical-token transitions for B=2,3,4 on every sliding log for m=B,...,18. It also exhaustively constructs the normalized B=3 log population for m=2,...,10 and compares its max with the sliding count. Exact integer source labels, multiple matching branches and the observer are retained; there is no pi, ordinary trigonometry, signed-force cancellation or BRC-Shor propagation.

## P000, native interface, and next discrimination

The three-port capacity-three burst is a concrete auxiliary Cell/Port source-observer candidate; R762AG identified its first three-source ambiguity threshold. The AH2 quartic contrasts with the proven B=2 Fibonacci family (R762AF). But P000 only fixes primitive three-force closure arity and 120-degree Enterprise PERP_E. It does **not** admit the hub occupancy rule, a stable interim one-/two-force balance, internal V29 PASS, V17 frame action, V39 holonomy or repeated force-event legality. For m>3 the source population is not itself a single primitive triad, and m>6 is not a six-axis single-star geometry.

**Next:** obtain a source-typed P000-admissible TRIADIC_CLOSURE_E incidence and transition, then intersect the above perfect matchings with that *actual native event alphabet*, preserving ordered branches, signs, Cell attachments, V29 TRANSFER/PASS distinction, V17/V39 updates and future-operation scope. The conjectured unrestricted B=3 maximum can be studied independently; neither result has been promoted to a native theorem.

**Publication boundary:** author-side Draft PR scientific material only; not native Source PROGRESS, Result, Driver acceptance, or P000 modification.