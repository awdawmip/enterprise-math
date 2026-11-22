# X6 R117 — A two-parameter exact first-outsider wall with early-Port atlas

Date: 2026-11-23 (Asia/Shanghai). Status: **AUTHOR_PROOF / EXACT_INTEGER_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED**. This is the **conditional** four-positive-weight, all-six-pair BRC observer of R90–R116. It is **not** a native Heartbeat Cell/Link/time-dynamics result and changes no frozen P000 input.

## Result

For nonzero integer a=(x,y,z), retain all six observation pairs and define:

- port(a) = max(sum(max(a_i,0)),sum(max(-a_i,0))).
- heights(a)=(0,x+3y+6z,3x+12y+30z,7x+39y+126z).
- F_w(a) = max_{i<j}|heights_i-heights_j|/(w_i+w_j).
- eta_p(w) = min_{a!=0,port(a)<=p} F_w(a).
- N_p(w) = {unoriented ±a:port(a)<=p,F_w(a)<3 eta_p(w)/2}.

Use integral moment coordinates (tau,m,n), with m congruent to n modulo 2, such that heights=(0,tau,3m,tau+6n) and

a=(10tau-12m+3n,-5tau+7m-2n,tau+(n-3m)/2).

Consider the **two-dimensional positive-weight strip**

w(q,delta) = (1+10q, 11-10q, 35+36q, 143-72q+delta),

where 3/5 <= q <= 7/10 and -1/4 <= delta <= 1/4. Put Y = B+D = 154-82q+delta.

**Theorem.** For *every* real (q,delta) in this closed rectangle and *every* integer Port p>=10,

eta_p(w) = **6/Y**.

Let the following unoriented sign-representatives be listed as (tau,m,n)[minimal Port]:

S7 = {(0,1,-1)[17], (0,1,1)[10], (1,0,0)[11], (1,-1,-1)[21],
      (1,-1,1)[28], (1,1,-1)[6], (1,1,1)[1]}.

Let e=(1,2,0)[16]. The complete strict-near set is exactly

**N_p(w) = [S7]_{Port<=p} union ( {e} if p>=16 AND 151q>100+delta, else empty ).**

Thus the new direction first enters across the exact affine wall
**q=(100+delta)/151**, is excluded at equality, and is available as early
as Port 16. For p>=28 there are exactly seven directions on and below
this wall and eight above it. This gives a genuine transverse thickening
of the R116 straight-segment first-outsider threshold (delta=0), rather
than another sample point on the same one-dimensional path.

The term **outsider** means absent from the initial Type-I twelve-row
template in fixed physical placement (1,2). The direction e has raw
integer coordinates (-14,9,-2), Port 16. The other seven rows are
from that original template. This does not assert a physical X6 outsider
or any new native primitive direction.

## Proof over the unbounded integer lattice

1. The entire rectangle has Y>72, Y>A+C, Y<2(A+C), A>B, and
Y<2(B+C); all inequalities are strict. If tau!=0 the AB observer
is at least 1/12 >6/Y. If tau=0 and n!=0, BD contributes at least
6/Y. If tau=0,n=0, parity forces even nonzero m, and AC contributes
at least 6/(A+C)>=6/Y. Hence **F_w(a)>=6/Y for every nonzero integer
a**, with no Port assumption. The integer witness (tau,m,n)=(0,1,1),
whose Port is 10, has BD score exactly 6/Y; its five other pair scores
do not exceed 6/Y by the displayed rectangle inequalities. Consequently
eta_p=6/Y for all p>=10.

2. Strict-near score means F_w(a)<9/Y. AB gives
|tau|<108/Y<2. After choosing sign, tau=0 or 1.
AC gives |m|<3(A+C)/Y<3 and BD gives |tau+6n|<9.
Thus |m|<=2, n in {-1,0,1}, m congruent to n modulo 2.
For tau=0, remove the zero vector and simultaneous sign:
(0,1,-1),(0,1,1),(0,2,0).
For tau=1, the only possibilities are
(1,-2,0),(1,0,0),(1,2,0),(1,-1,-1),(1,-1,1),
(1,1,-1),(1,1,1). These **ten** are the entire infinite-lattice
candidate bank. No larger Port can introduce an additional candidate.

3. For a candidate with heights h, define the exact pair slack
S_ij=9(w_i+w_j)-|h_i-h_j|Y. The row is strictly near precisely when
all six S_ij>0. Every S_ij is affine in (q,delta), so extrema on the
closed rectangle occur at its four vertices.
All seven S7 rows have every slack at least **59/20>0**.
For (0,2,0) the BC slack is
9(B+C)-6Y=-510+726q-6delta <= **-3/10**.
For (1,-2,0) the BC slack is
9(B+C)-7Y=-664+808q-7delta <= **-1933/20**.
The two rows are therefore never strictly near.

4. The remaining row e=(1,2,0) has
heights=(0,1,6,1). Its five pair slacks other than AC are
strictly positive throughout the rectangle, with minimum
at least **59/20**. Its AC slack is exactly

S_AC=9(A+C)-6Y=**6(151q-100-delta)**.

It therefore enters if and only if 151q>100+delta. Direct inversion
gives the exact Ports printed in S7 and Port(e)=16. Intersecting the
finite bank with Port<=p proves the theorem for all integer p>=10. QED.

## Reproduction and scope

The standalone companion Python checker uses only the standard
library and exact integer cross-multiplication. It independently
enumerates **38,598 nonzero unoriented triples** of Port<=28 per
weight sample, retaining *all six pair gaps* in each comparison.
Thirteen rational samples cover four rectangle corners and the
points just below, exactly at and just above the wall at each
delta=-1/4,0,1/4. It verifies the global finite lower bound, the
actual Port-10 optimal witness, and complete near sets at
p=10,11,15,16,17,21,28. All **501,774** vector/sample checks passed,
including strict exclusion at equality. The complete all-Port and
all-real-parameter statements rest on the analytic finite-bank proof,
not on those thirteen samples. The author has not received an
independent mathematical review.

### Inputs and provenance

- R90 exact Type-I/II 12-row template and first Port, global knowledge
  journal x6-r90-complete-twelve-direction-catalog.md
  (blob c02e1e001d43c334b8433be565886f450ea09c6c).
- R116 first outsider on the unperturbed cross-cone segment,
  x6-r116-first-outsiders-on-cross-cone-segment.md
  (blob c4bf3e2b2a02563ba91098b01c1fe57a9c9650b8).
- R116 original source theorem in
  enterprise-math@06eea6f558dfcc3a7c91102d314a56a1548cedfb.
- P000 V5, HEARTBEAT_WORLD_NATIVE_X6_TIME, joint-relation six-pair
  preservation, ACTIVE account worldview, current portable research
  method and continuation rules were read on this research turn.
- Scientific computation here is exact arithmetic *within the already
  declared conditional six-pair BRC observer*. It does not claim native
  residual attribution, phase cancellation or heartbeats. The
  original X6 native dynamics and frozen science requirements remain separate.

**Next:** optimize the strip width by exact rational wall-margin
inequalities, then classify the first-outsider surface under a general
four-weight transverse perturbation. For p<10 the realizing witness
is not admissible and an independently proved early-Port atlas is open.
