# X6 Weighted-BRC C6: exact nonidentifiability of the entire one-turn boundary transfer

Status: DRIVER_MATHEMATICAL_AUDIT / EXACT_SCOPED_THEOREM / NOT_NATIVE_RESULT_ADMISSION
Date: 2026-11-12 (+08)
Scope: phase-weighted, non-immediate-backtracking (NB) INNER/OUTER branches of the candidate C6 Path-formal / Weighted-BRC model; not a physical native rotation law.
Parent: RS-X6-NATIVE-ROTATION-DYNAMICS; PO-X6-UPPER-STRUCTURE-20260906.
Contribution: scoped new Driver derivation in a **shared, not clean-blind, X6 scientific context**. Original signed Cell C6/C12 microtrace and underlying X6 definitions retain their recorded source authorship (including EM-FREE-7D3C9A). No new native Task CLAIM, Result acceptance, review independence or objective closure is asserted.

## 1. Exact statement

Retain the six ordered phases and two microbranches per macrostep from the published C6 branch-weight note. Let each OUTER branch have normalized activity 1, and INNER at phase j have a positive rational activity t_j; adjacent INNER branches are forbidden. The legal weighted transition for one phase is

    T(t) = [[1,t],[1,0]],

with previous branch (O,I) indexing rows and current branch indexing columns. One complete C6 turn has boundary transfer

    P(t_1,...,t_6) = T(t_1)...T(t_6).

**Theorem (noninjectivity even for the full labelled endpoint transfer).** Two positive-rational six-phase laws not related by any phase relabelling can have *exactly the same complete 2-by-2 boundary transfer P*. Consequently, for every integer m >= 1 and every pair of boundary vectors u,v, the totals u P^m v agree. In particular all repeated full-turn closed masses tr(P^m), every fixed-boundary open mass and all four O/I entrywise endpoint masses are identical. Even the entire endpoint transfer at all whole-turn counts fails to identify the internal phase activity law.

## 2. Exact constructive proof

Direct multiplication gives the four-phase identity

    T(1/2) T(1/2) T(2) T(2)
        = [[5,4],[7/2,3]]
        = T(1) T(2) T(1/2) T(1).

Prepend the same two factors T(1/2) T(1/2) on both sides. The two six-phase laws are therefore

    U = (1/2,1/2,1/2,1/2,2,2)
    V = (1/2,1/2,1,2,1/2,1),

and both give

    P_U = P_V = [[37/4,15/2],[27/4,11/2]].

All entries are rational and both laws have strictly positive activities. The multisets themselves differ: U contains four 1/2 and two 2, whereas V contains three 1/2, two 1 and one 2. Thus they are inequivalent under *every* permutation, in particular under cyclic rotations and reflections of C6.

Matrix equality entails P_U^m=P_V^m for every positive m, which proves equality for all endpoint conditions and open/closed full-turn statistics. For orientation, one-turn open activity e_O P (1,1)^T is 67/4 for both and one-turn closed activity tr(P) is 59/4 for both; trace/determinant are tau=59/4, delta=1/4. The per-turn fixed primitive-letter multiplicative factor W_S, inherited from the existing C6 microtrace scope, is common to every branch word; multiplying by W_S^m does not separate the two laws. This concludes the proof.

This strengthens the previous trace/determinant collision: it is not merely that two scalar closed-loop invariants omit phase information; here the complete 2-by-2 one-turn transfer omits it.

## 3. A phase-resolved observation that distinguishes the collision

The prefix of three macrosteps gives

    T(U_1)T(U_2)T(U_3)
        = [[2,3/4],[3/2,1/2]],
    T(V_1)T(V_2)T(V_3)
        = [[2,3/2],[3/2,1]].

The open NB masses e_O P_prefix (1,1)^T are **11/4** for U and **7/2** for V. Thus an intermediate phase-three checkpoint, retaining the phase registration, separates this explicit collision even though *no* whole-turn endpoint observation can do so.

This is an observation-design theorem for this candidate weighted path model, not a theorem identifying the unique physical Cell trajectory, general X6 rotation law, or all possible phase-observer reconstruction schemes. For a future native X6 successor, test which phase clock, incoming branch, orientation and intermediate observations must remain in state rather than relying solely on six-step coarse-grained transfer.

## 3.1. Exact tomography from phase-registered cyclic boundary transfers

The loss above is specific to observing only a **fixed phase origin** at every whole turn. Retain the complete labelled 2-by-2 transfer measured from each cyclic starting phase:

    P_j = T(t_j) T(t_{j+1}) ... T(t_{j+5}),  indices modulo 6.

For strictly positive t_j, all entries of P_j are positive (every six-factor product has positive entries). Define b_j=(P_j)_{1,2} and c_j=(P_j)_{2,1}. The cyclic products satisfy

    P_j T(t_j) = T(t_j) P_{j+1}.

Indeed, the two sides are both T(t_j)...T(t_{j+5})T(t_j). Comparing the (2,2) entry gives

    c_j t_j = b_{j+1},  hence  t_j = b_{j+1}/c_j.

**Tomography theorem.** Knowing all six phase-registered whole-turn endpoint matrices P_1,...,P_6 in their true cyclic order determines all six positive activities *uniquely*, by the above explicit rational quotients. This is a constructive, algebraic inverse, not a numerical fit or a claim of minimal observation cost.

The collision U,V has identical starting-phase transfers P_1,P_2,P_3, but differs already at start phase 4:

    P_4(U) = [[23/2,33/8],[9,13/4]],
    P_4(V) = [[23/2,33/4],[9/2,13/4]].

Thus retaining **cyclic starting-phase registration**, unlike repeating only the same whole-turn measurement, can resolve the ambiguity. This gives two exact and distinct experimental repairs: an intermediate phase-three prefix readout (section 3) or sufficiently rich cyclic boundary tomography. Neither replaces the missing physical native rotation definition.

## 4. Exact reproduction

The proof is the displayed four-factor matrix identity, followed by multiplication and elementary properties of powers. The following independent rational arithmetic check verifies every displayed finite identity (it is not the universal proof):

```python
from fractions import Fraction as F

def mul(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],
             A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0],
             A[1][0]*B[0][1]+A[1][1]*B[1][1]))

def T(t): return ((F(1),t),(F(1),F(0)))
def P(seq):
    out=((F(1),F(0)),(F(0),F(1)))
    for t in seq: out=mul(out,T(t))
    return out

u=(F(1,2),F(1,2),F(1,2),F(1,2),F(2),F(2))
v=(F(1,2),F(1,2),F(1),F(2),F(1,2),F(1))
assert P((F(1,2),F(1,2),F(2),F(2))) == P((F(1),F(2),F(1,2),F(1)))
assert P(u)==P(v)==((F(37,4),F(15,2)),(F(27,4),F(11,2)))
def open_mass(q): return q[0][0]+q[0][1]
assert open_mass(P(u))==open_mass(P(v))==F(67,4)
assert open_mass(P(u[:3]))==F(11,4)
assert open_mass(P(v[:3]))==F(7,2)
assert sorted(u)!=sorted(v)
```

## 5. Source and operational boundaries

Builds on the actual published phase transfer theorem and its explicit NB and phase-activity hypotheses:
- [2026-11-12_x6_phase_weighted_brc_c6_loop_identifiability.md](2026-11-12_x6_phase_weighted_brc_c6_loop_identifiability.md).
- [2026-11-12_x6_weighted_brc_c6_loop_and_star_atlas_invariants.md](2026-11-12_x6_weighted_brc_c6_loop_and_star_atlas_invariants.md).
- Original microtrace source: research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md.
- Native source definition: definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md.

This is a saved, scoped Driver mathematical audit contribution. The historical X6 Result/HRI revisions, F7 Native Review, official task/owner CLAIM and mother Objective closure are separate canonical actions and are not supplied by this GitHub proof.
