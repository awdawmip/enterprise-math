# PREFIX-549 — Exact six-axis BRC–gate observer: 51 classes, Krylov rank 49

Date: 2026-11-07, Asia/Shanghai. Line: RS-X6-NATIVE-ROTATION-DYNAMICS (independent author). Frozen scientific pin: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continuation: PREFIX-548 at ea082cc8ce65d77ff2402e6cd034990dbdf7340d. Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / NONZERO_MODULAR_MINOR / UNREVIEWED / NOT_ADMITTED.

## 1. Frozen model

Use the original four STARs A=(1,3,6), B=(1,4,5), C=(2,3,5), D=(2,4,6); their typed 48 phases have 144 directed edges, three successors per phase and two branch-bit choices on each step. There are 96 ports (phase,previous-bit), with bits 0=OUTER, 1=INNER. A gate counts when previous/new bits are both 1 and the arrival phase is (A,+L1,-L3).

For each native axis a∈{1,...,6}, σ_a(i) is the signed current-axis indicator in {-1,0,+1}. Given the original root signature r, define on each legal phase edge i→j the BRC increment

  τ_(a,r)(i,j)=[|σ_a(i)|+|σ_a(j)|−|σ_a(j)−r_a|+|σ_a(i)−r_a|]/2.

Exact edge enumeration establishes τ∈{0,1} for the twelve physically realized r=±e_a. Telescoping recovers the native first/last endpoint correction and axis-visit totals of PREFIX-539/548. A labeled edge is weighted by ∏(q_a^τ_a)·z^g; all six axes, gate and multiplicity remain joint. This is a future scalar histogram observer of the frozen X6 candidate, not an identification of native Cell identities.

## 2. Theorem A: exactly 51 positive future-histogram classes

For each of the 12 realized signatures, among the 96 phase–bit ports there are precisely **51** all-length future-polynomial equivalence classes. They consist of 45 doubletons (bit 0 and bit 1 at one phase) and six singletons, from the three bit-sensitive phases

  (A,-L6,+L1), (B,-L4,+L1), (B,-L5,+L1).

All 12 signatures produce the same partition. Distinct class fingerprints through future lengths d=0,1,2 grow as [1,12,51] for nine signatures and [1,13,51] for the three negative roots on axes 4,5,6 (the final 51 is common).

**Proof.** Start with a one-class partition; for every port and every action, group its six weighted transitions by (destination class, complete 7-variable monomial) with integer multiplicities. Refine until stable. Exhaustive frozen-table equality gives 51 stable classes and complete weighted transition-row congruence for every r. Induction on future depth then proves that ports inside each class generate identical polynomials for *every* length. Conversely, exact polynomial expansion at d=0,1,2 gives 51 distinct fingerprints for each r, separating all classes; 51 is therefore exact. The attached standalone certificate constructs every counter from the 144 native phase edges.

## 3. Theorem B: exact field-linear minimal dimension 49

Let Q_r be the 51×51 multivariate polynomial quotient matrix over Z[q1,...,q6,z] in canonical class order obtained by first-encounter refinement at r=(-1,0,0,0,0,0). For all twelve r, two complete weighted row identities hold:

  Q_r[3,*]−Q_r[4,*]−Q_r[15,*]+Q_r[16,*]=0,

  Q_r[3,*]−Q_r[4,*]−Q_r[17,*]+Q_r[18,*]=0.

These relations also annihilate the all-one vector, hence for F_i(d)=(Q_r^d 1)_i they hold for every integer d≥0. The rank of the infinite length-indexed Krylov array K_r=[1,Q_r1,Q_r²1,...] over F=Q(q1,...,q6,z) is at most 49.

To prove sharpness, choose the **same** row indices I={0,...,50}\{16,18} and the **same** depth columns 0,...,48 for all r. Evaluate at (q1,q2,q3,q4,q5,q6,z)=(2,3,5,7,11,13,17), modulo the prime 1000000007. The respective 49×49 determinant residues for r=(-e1,+e1,-e2,+e2,-e3,+e3,-e4,+e4,-e5,+e5,-e6,+e6) are

  772471633, 704956490, 943298894, 282007017, 805462083, 902086238, 120964783, 162451683, 55944770, 843283531, 512296320, 489832900.

Every residue is nonzero: each specialized determinant is the image of an integer-coefficient symbolic determinant, so the corresponding polynomial minor cannot vanish identically. Thus for **all 12 physically realized roots**:

  **rank_F K_r = 49**, at every nonnegative future horizon.

This is the exact minimal field-linear dimension for simultaneously returning all 51 complete scalar joint length-series. Its scope is the declared future histogram readout, rather than individually commanded future actions.

## 4. Constructive realization

Keep the 49 coordinates in I, reconstruct coordinate 16 as -F3+F4+F15, and coordinate 18 as -F3+F4+F17. Let E be this extension, and T_r=(Q_r E)[I,*]. The two full-row identities give Q_r E=E T_r and E1_49=1_51. Hence

  Q_r^d 1_51 = E T_r^d 1_49, for all d≥0.

The 51-state quotient retains positive counting coefficients. The 49-coordinate implementation may use signed intermediate coefficients. Both are exact and preserve the six-axis joint histogram.

## 5. Reproduction, verification and scope

The published standard-library Python certificate was executed with status ALL_CHECKS_PASS. It checks 48 phases/144 edges/96 ports, twelve 51-class stable partitions, 165 distinct weighted transition terms per quotient, exact complete depth-2 polynomial separation, two coefficientwise transition identities at each root and twelve nonzero modular minors.

A longer independent implementation also executed with ALL_CHECKS_PASS. Instead of locally accumulating τ, it retains original six-axis visit totals, terminal phase and previous bit, computes the original BRC endpoint corrections, and directly compares all complete histograms at 48 original roots ×2 initial bits×d=0,...,5 = **576 complete polynomial crosschecks**. Full extended program, both raw JSON outputs and a SHA256 inventory are retained in the companion evidence archive.

PRE-549 and this result use the same frozen four-STAR candidate: PREFIX-548 found a two-axis rank of 27 among 28 positive classes; joint six-axis observation now distinguishes 51 classes and has exactly 49 field-linear directions. This demonstrates which extra joint observer distinctions arise upon retaining axes 3–6.

Next PREFIX-550: benchmark end-to-end 51-positive versus 49-signed batch outputs including construction, recovery and memory; test integral 49-coordinate basis design and introduce selected Cell/ordered-branch future operations to measure observer-safe state enlargement.

For background on weighted finite automata and linear representations: Balle, Panangaden and Precup, *A Canonical Form for Weighted Automata and Applications to Approximate Minimization*, arXiv:1501.06841 (2015). The finite six-axis certificates here are model-specific.

Native control queries returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. Researcher-ID/current owner could not be confirmed; no formal CLAIM, Result or Review was made. No P000/ACTIVE worldview edit is requested.
