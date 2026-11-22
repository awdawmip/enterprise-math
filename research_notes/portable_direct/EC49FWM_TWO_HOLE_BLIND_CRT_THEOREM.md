# EC49FWM — Two-hole CRT blind inverse theorem

Date: 2026-11-22 (Asia/Shanghai).
Frozen scientific lineage: BRC16943; EC49FWL exact one-hole inverse at commit 0bbbbffa615824d0f02aa40c2225dc29f8c2ecf9. Independent portable auxiliary research; status AUTHOR_PROVED / EXACT_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED. No claim to native Farey dynamics, authenticated Activity or formal Task execution.

## Problem and theorem

Let n,q be coprime positive integers, q odd and q >= 5. Let U be a nonempty subset of Z/n with w=|U|. Let Z={z1,z2} be an unknown two-point subset of Z/q, and V=(Z/q)\Z. Under CRT put W=U x V in Z/(nq). For a cyclic subset S, define the *indexed* reflection defect Delta_S(c)=|S triangle (c-S)|. The complete indexed nq-entry spectrum of W is observed; the two missing positions and w are not known in advance, but the exactly-two-hole model and the moduli are known.

Define kappa(b)=|Z intersect (b-Z)| and R(b)=sum over a modulo n of Delta_W(a,b).
The two diagonal centers 2z1,2z2 have kappa=1, the single cross-sum center b*=z1+z2 has kappa=2, and all q-3 remaining centers have kappa=0. They are distinct because q is odd and z1 != z2.

**Exact pointwise factorization:**

Delta_W(a,b) = (q-4+kappa(b)) Delta_U(a) + 2w(2-kappa(b)).    (1)

**Exact row-sum identity:**

R(b) = 2[n(q-2)w - (q-4+kappa(b))w^2].                        (2)

Consequently R has three and only three levels:
- Rmax (q-3 occurrences), at kappa=0;
- Rmid=Rmax-2w^2 (two occurrences), at kappa=1;
- Rmin=Rmax-4w^2 (one occurrence), at kappa=2.

In particular the *unknown* two holes and support weight are uniquely recovered by

w = sqrt((Rmax-Rmin)/4),
Z = { 2^{-1}b mod q : R(b)=Rmid },
b* = the unique index with R(b*)=Rmin.

The full indexed shorter spectrum is then recovered by

Delta_U(a) = Delta_W(a,b*)/(q-2).

All formulas use exact integers. Neither individual membership probes nor an a priori factor-position lookup are needed.

## Proof

Let K_U(a)=|U intersect (a-U)|. The complement identity gives |V intersect (b-V)|=q-4+kappa(b), and the CRT intersection law gives |W intersect ((a,b)-W)|=K_U(a)(q-4+kappa(b)). Since |W|=(q-2)w and Delta_U=2(w-K_U), equation (1) follows by substitution.

Each ordered pair (u,v) in U^2 contributes to exactly one center a=u+v, so sum_a K_U(a)=w^2. Summation of the intersection identity proves (2). The three special centers are distinct in odd characteristic and q>=5 leaves q-3 positive-number baseline rows. Since w>0, the three levels are strictly separated, giving the recovery of w,Z,b*. Setting kappa(b*)=2 in (1) yields Delta_W(a,b*)=(q-2)Delta_U(a). QED.

## Sharp observer boundary and explicit witness

The unknown factor is identified, but the underlying signed support need not be. The frozen prior pair U_A={0,2,3,4,7} and U_B={0,1,3,4,6} in Z/10 has the same support size 5 and same full indexed Delta_U, yet different membership. Formula (1) implies the two different 110-word supports have the same entire indexed CRT defect spectrum for every common two-hole factor V. This is an exact fiber-constancy result for the specific observer {Z,w,Delta_U}, not for future native operations.

For q=11 and Z={2,7}, the minimum row occurs at b*=9, intermediate rows at b=3,4, and all others are maxima. For w=5 the row sums are respectively 450,500,550. The two-hole factor does not erase the signed-position residual.

For empty U, all defects vanish and holes cannot be inferred. This statement assumes exactly two holes and odd q>=5 and makes no identification claim for unknown hole count or arbitrary noisy or partial spectra.

## Verification

Standalone Python standard-library program: EC49FWM_TWO_HOLE_CRT_VERIFY.py. Actual output: EC49FWM_TWO_HOLE_CRT_OUTPUT.json.

At n=10,q=11 it checks all 1024 possible U and 55 two-hole choices, giving 56,320 exact inverse instances; 770 are also checked against direct cyclic Z/110 computations. At n=4,q=5, it checks 160 inverse instances and 20 direct Z/20 computations. All assertions PASS, including the inherited same-spectrum support collision.

The analytical proof establishes the stated general result independently of these finite sample sizes. Scientific dependencies BRC16943 and the frozen predecessor remain parent-dependent and independently unreviewed. The computation does not execute the actual moving Farey F_native/Y_native, prove an X6 model embedding, or alter P000.

## Next scientific issue

Classify three-hole autocorrelation center collisions: the middle point of an arithmetic progression can make one diagonal center coincide with an off-diagonal pair sum, creating a new exceptional row pattern. Test exactly which hole triples remain identifiable from indexed row sums. Separately locate the *frozen native* moving Farey update and observation, and test whether the inherited same-spectrum support pair separates at the successor observer before attempting any future-state compression.
