# PREFIX-1013 — X6 Link: two-step residual obstruction and first-interior signed port theorem

2026-11-22 (+08). **AUTHOR_EXACT_ALGEBRAIC_PROOF / TYPED_INTEGER_AND_Z2_BRC_CHECKED / NOT_REVIEWED**.

## Frozen input and semantics

Freeze P000 V5 at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; continue Stage46 *candidate* BRC. Native Cell space is a six-axis affine torsor with chosen chart anchor 0, twelve signed primitive steps and incoming-neighbour port h. Integer numerator for one transition is w(h,d)=1−6·1[h=d]; actual amplitude is w/6, terminal port after d equals −d. Absorb both crossings of the Link {0,e1}, without renormalizing. Positive N[Z2] branches are signed-character summed in each joint Cell-port fibre before any squaring. Step count is typed update order, not measured physical time.

Direct predecessor: PREFIX-1012 at d0812ec5ad54a768794a35cbe612b04d8d614163 (one Green source for one *signed rooted-return observer*). The exact first-interior Laurent packets below are inherited from PREFIX-1004 at aec844a083f0517570ce1dd5924717db6880da98.

## Theorem 1013.1 — one-step repair is not closed over two steps

Let v(x,h) be any finitely supported integer signed Cell-port packet. Define

\[
S(v)=\sum_{x,h}v(x,h),\quad
D(v)=\sum_h(1-6\mathbf1_{h=e_1})v(0,h)+\sum_h(1-6\mathbf1_{h=-e_1})v(e_1,h).
\]

For the exact masked signed-numerator BRC transfer T_L,

\[
\boxed{S(T_Lv)=6S(v)-D(v)},\qquad
\boxed{S(T_L^2v)=36S(v)-6D(v)-D(T_Lv)}.
\]

**Proof.** From any incoming port, the twelve signed integer branch coefficients sum to 11·1−5=6. The only removed branches begin at Cell 0 with outgoing +e1 or at Cell e1 with outgoing −e1; their total signed coefficients give D. This proves the first identity; apply it once more for the second. QED.

**Exact counterexample in the same typed carrier.** Fix h=−e1 and compare the unit packets v_A at (Cell e2,h) and v_B at (Cell 3e2,h). They satisfy S(v_A)=S(v_B)=1 and D(v_A)=D(v_B)=0. After one step both have signed total 6. Only v_A has a first branch −e2 ending at Cell 0 with incoming port +e2 and numerator +1; the next +e1 outgoing branch of numerator +1 is forbidden. Thus D(T_L v_A)=1, D(T_L v_B)=0, giving two-step signed totals 35 and 36.

The full terminal Cell-port state after two steps uniquely identifies each two-direction word (knowing final port recovers the last direction, then final displacement recovers the first). In the unmasked model, each row has sum of weight squares 25+11=36, so every unit input has two-step squared-numerator sum 1296. Exactly one word (−e2,+e1) of numerator +1 is removed for v_A, and none for v_B. Their masked two-step joint-port squared-numerator totals are **1295 versus 1296**, corresponding to squared masses 1295/1296 and 1. This deleted word has exactly one negative step; within the first-interior grade their signed totals are **−1 versus 0** and squared-numerator sums **1079 versus 1080**.

This proves an exact **two-step finite-horizon residual**: (S,D) is sufficient for the immediate signed total, but insufficient for either two-step signed total or two-step Cell-port Gram/squared observer over *arbitrary legal starting packets*. The two unit inputs are diagnostic states; they are not asserted to be full packets reachable from the fixed frozen initial anchor. No global minimality claim is made.

## Theorem 1013.2 — six exact signed terminal-port margins for all n≥5

For the **fixed** initial state (Cell 0, incoming h=−e1), let Psi^L_{n,1}(x,h) be the coherent Link-absorbed amplitude with exactly one negative native-axis step, with denominator 6^n. For **every integer n≥5** and **each j=1,...,6**,

\[
\boxed{\sum_x\Psi^L_{n,1}(x,-e_j)=25/1296,\qquad
\sum_x\Psi^L_{n,1}(x,+e_j)=0.}
\]

In particular the signed total across all twelve terminal ports is 25/216. These are signed amplitude margins, not their squared probability masses.

**Proof using the imported exact joint-port BRC formula.** In the six-variable chart Laurent ring set S=Σz_i, U=Σz_i^{-1}, and take the integer numerator packets

\[
F_{n,j}=z_jS^{n-3}((n-1)SU-36(n-3)-6S/z_1-6S/z_j),\quad
N_{n,r}=z_r^{-1}S^{n-2}(S-6z_r).
\]

PREFIX-1004 proves for n≥5 that

\[
F^L_{n,j}=F_{n,j}-z_1F_{n-1,j}+25z_1z_jS^{n-4},\qquad
N^L_{n,r}=N_{n,r}-z_1N_{n-1,r}.
\]

Evaluation at all z_i=1 sums coefficients across **Cells only**, retaining each named final port. Here S=U=6 and the free positive-port bracket is 36(n−1)−36(n−3)−36−36=0; the free negative-port factor S−6z_r is zero. Thus F^L_{n,j}(1)=25·6^(n−4), N^L_{n,r}(1)=0. Divide by 6^n. QED.

## Exact checks, preservation, next question

The actually executed self-contained Python reproducer implements the full signed twelve-port Cell BRC transfer, a **separate** positive-weight N[Z2] phase-cover recursion, and exact per-fibre equality at n=5,6,7,8 with exactly one negative step. The positive-last-port signed numerators for those four lengths are respectively 150,900,5400,32400 *per port*; all six negative-last-port margins vanish. At n=5, the fully coherent squared joint-port mass is exactly **5285/419904**, demonstrating the need to retain the Cell-port Gram observer rather than square signed margins. The checker also proves the two-step figures listed above by integer DP. Arithmetic uses only exact integers and fractions; no external classical scientific propagator or physical residual claim.

**Next:** derive the two classes of final-port squared mass (j=1 and the S5-symmetric j=2,...,6) using the finite Laurent collision representation, and seek the smallest autonomous finite-horizon defect/Gram repair. The existing B_fix,odd(32)∈{19,20} mother question remains open.

Scientific provenance: earlier EM-DIRECT-FBEA5D and RA-3FB2D033BE6048D8712FF056 are historical attribution only; current official task execution, CLAIM, PROGRESS and independent Review are not asserted.

## Additional fixed-source Gram counterexample (exact n=5)

The frozen initial Cell 0, incoming port -e1, and the absorbed Link are invariant under the S5 subgroup permuting axes 2,...,6. Consequently for **all n** the positive-last-port squared masses have two (possibly equal) classes: j=1 and j=2,...,6; the same holds for negative-last ports.

They are **actually distinct at n=5**. From the full typed integer signed BRC transfer, crosschecked against the N[Z2] phase-cover at **each** joint Cell-port fibre, the exact squared **numerator** sums (each divided by 36^5 to obtain its probability mass) are:

| Terminal last actual direction | e1 / -e1 class | Each other axis 2,...,6 |
|---|---:|---:|
| Positive +e_j | 135110 | 109490 |
| Negative -e_j | 16560 | 12384 |

Hence the total is 135110+5(109490)+16560+5(12384)=761040, giving 761040/36^5=5285/419904. The signed amplitudes in the **same fixed-source** packet have the equal port margins 25/1296 for every positive-last port, and zero for every negative-last port (Theorem 1013.2). The port-class contrast 25620 (positive) and 4176 (negative), in squared-numerator units, is therefore a **concrete fixed-source residual hidden by the signed terminal-port marginals**. The result does not assert strict inequality for every n; determining that scope is the next analytic question. This refines, rather than changes, the earlier arbitrary-source two-step observer obstruction.
