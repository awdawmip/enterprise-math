# X6 R105 — Sharp 3/2 cutoff in the actual six-pair BRC family; complete Port spectrum

Date: 2026-11-22 (Asia/Shanghai). Scientific status: AUTHOR_SYMBOLIC_PROOF / EXACT_INTEGER_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.
Frozen input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`.
Predecessor: R104 \`research_notes/portable_direct/2026-11-22_x6_r104_thirteen_class_robust_gap_and_finite_box.md\`.
Scope: the same **conditional auxiliary positive-count BRC six-pair star-gap observer**. It is not a native X6 signed/phase/path/heartbeat observer realization. P000 and ACTIVE worldview remain unchanged.

## Observer and definitions

Let \(a=(x,y,z)\in\mathbb Z^3\setminus\{0\}\), identifying \(a\) with \(-a\). Define

\[
q(a)=\max\bigl(\sum_i\max(a_i,0),\ \sum_i\max(-a_i,0)\bigr),\quad
u=x+3y+6z,\quad v=3x+12y+30z,\quad h=7x+39y+126z.
\]

Take the fixed positive weights \(w=(A,B,C,D)=(9,1,59,41)\). Its exact six-pair norm is

\[
F(a)=\max\left\{\frac{|u|}{10},\frac{|v|}{68},\frac{|h|}{50},
\frac{|v-u|}{60},\frac{|h-u|}{42},\frac{|h-v|}{100}\right\}.
\]

For every integer \(p\ge11\), put
\[
\eta_p=\min_{\substack{a\ne0\\q(a)\le p}}F(a),\qquad
N_p=\{\{\pm a\}:q(a)\le p,\ F(a)<3\eta_p/2\},\qquad
C_p=\{\{\pm a\}:q(a)\le p,\ F(a)\le3\eta_p/2\}.
\]

## Theorem R105 — exact all-Port sublevel spectrum

For every integer \(p\ge11\), one has \(\boxed{\eta_p=1/10}\).
The union of \(C_p\) over **all** such \(p\) consists of exactly the following **14** unoriented directions, with the displayed exact Port threshold and score:

| Direction \(a\) | \(q(a)\) | \(F(a)\) |
|---|---:|---:|
| (1,0,0) | 1 | 1/7 |
| (5,-4,1) | 6 | 1/7 |
| (9,-5,1) | 10 | 1/7 |
| (10,-5,1) | 11 | 1/10 |
| (14,-9,2) | 16 | 1/10 |
| (15,-9,2) | 17 | 1/7 |
| (19,-10,2) | 21 | 1/7 |
| (23,-14,3) | 26 | 1/7 |
| (24,-14,3) | 27 | 1/10 |
| (25,-14,3) | 28 | 1/7 |
| (29,-18,4) | 33 | 1/7 |
| (33,-19,4) | 37 | 3/20 |
| (34,-19,4) | 38 | 7/60 |
| (39,-23,5) | 44 | 3/20 |

With \([P]\) denoting the indicator of a proposition \(P\), the **complete** formulas for all \(p\ge11\) are

\[
|N_p|=4+[p\ge16]+[p\ge17]+[p\ge21]+[p\ge26]+[p\ge27]+[p\ge28]+[p\ge33]+[p\ge38],
\]
\[
|C_p|=|N_p|+[p\ge37]+[p\ge44].
\]

The full set of minimizers contains \(s=(10,-5,1)\) from Port 11; additionally \((14,-9,2)\) from Port 16; additionally \((24,-14,3)\) from Port 27. At every \(p\ge38\), **exactly 12** directions satisfy the *strict* \(3/2\) cutoff. At every \(p\ge44\), **exactly 14** satisfy the *non-strict* cutoff. Both the 13th and 14th best feasible scores for \(p\ge44\) are exactly \(3/20\).

**Sharpness in the concrete BRC class.** The R104 universal theorem bounds the number with \(F<3\eta_p/2\) by 13. Here there are 14 directions with \(F\le3\eta_p/2\) at every \(p\ge44\). Consequently, for every \(\lambda>3/2\), a proposed universal bound of 13 directions satisfying \(F<\lambda\eta_p\) is **false even within the actual positive six-pair BRC family**. The \(3/2\) threshold is optimal. This leaves open whether the *strict* sublevel maximum within this family is 12 or 13.

## Proof — infinite lattice reduced to an exact finite box

First \(s=(10,-5,1)\) has \(q(s)=11\) and \((u,v,h)(s)=(1,0,1)\), so \(F(s)=1/10\). Thus \(\eta_p\le1/10\) for every \(p\ge11\).

Conversely, for any nonzero integer \(a\), if \(u\ne0\) the first term of \(F\) is at least \(1/10\). If \(u=0,h\ne0\), the exact moment congruence \(h-u\equiv0\pmod6\) implies \(|h-u|\ge6\), so \(F(a)\ge6/42>1/10\). If \(u=h=0\), invertibility of the moment matrix implies \(v\ne0\). The exact congruences \(v\equiv0\pmod3\) and \(h-u-6v\equiv0\pmod{12}\) give \(v\in6\mathbb Z\), so \(F(a)\ge|v|/60\ge1/10\). This proves the minimum for the *entire* lattice, independent of Port.

Now \(F(a)\le3/20\) implies three simultaneous necessary integer bounds
\[
|u|\le\lfloor(3/20)10\rfloor=1,\quad
|v|\le\lfloor(3/20)68\rfloor=10,\quad
|h|\le\lfloor(3/20)50\rfloor=7.
\]
Thus every possible vector in the closed sublevel lies among precisely \(3\cdot21\cdot15=945\) integer moment triples, independently of \(p\). The exact inverse is
\[
x=(h+19u-8v)/2,\quad y=(-h-14u+7v)/3,\quad z=(h+11u-6v)/12.
\]
The necessary and sufficient integrality conditions are
\[
v\equiv0\pmod3,\quad h-u\equiv0\pmod6,\quad h-u-6v\equiv0\pmod{12}.
\]
Enumerating this finite integer box gives 32 nonzero *oriented* integral vectors; exact evaluation of the other three pair terms removes four, leaving exactly 28 oriented or **14 unoriented** admissible vectors. Their exact scores and Port costs are the table above. The companion \`x6_r105_sharp_threshold_verify.js\` reproduces the full finite calculation with integer arithmetic, common denominator 35700, integer score threshold 5355, and exact row assertions.

Finally, the infinite-lattice minimum \(\eta_p=1/10\) is constant, the exhaustive closed sublevel table is independent of \(p\), and intersection with the exact cost condition \(q\le p\) gives both indicator formulas. The scores of the two equality-shell directions are exactly \(3/20\), entering at Port 37 and Port 44 respectively. Therefore the 14-direction and sharpness statements hold for **all** \(p\ge44\). QED.

## Verification boundary and next direction

The 945-box coverage follows mathematically from the exact inequalities and covers every integer difference, regardless of Port. The executable finite enumeration checks its stated arithmetic, not independent mathematical review or native X6 fidelity. The next discriminating problem is deciding whether 13 *strictly* near-optimal directions are attainable for some arbitrary positive \(w\), or proving a 12-direction universal bound specific to this six-pair BRC norm. Keep separate the original R063 native benchmark and Cell/Link/Port/time observer-preservation obligations.
