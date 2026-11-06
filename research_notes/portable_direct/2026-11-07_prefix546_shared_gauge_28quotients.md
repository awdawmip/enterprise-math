# PREFIX-546 — One 28-class BRC–gate quotient, three exact root-sign gauges

Date: 2026-11-07 (Asia/Shanghai). Independent author research for RS-X6-NATIVE-ROTATION-DYNAMICS.
Frozen scientific input: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-545 at dd9f068d02cddf62783e553de974ab4d682df9e8.
Status: AUTHOR_PROVED / FINITE_EXHAUSTIVE_CERTIFICATE / EXACT_POLYNOMIAL_CHECKED / EXPERIMENTALLY_BENCHMARKED / UNREVIEWED / NOT_ADMITTED.

## Object and notation

The frozen four-STAR candidate uses A=(1,3,6), B=(1,4,5), C=(2,3,5), D=(2,4,6), 48 oriented phase states, 144 phase edges and 96 phase–prior-bit ports. Each transition selects one of three native successor slots and one INNER/OUTER bit. The gate target is T=(A,+L1,-L3); gate increment g is one precisely when the prior and new branch bits are both INNER and the new phase is T.

Let sigma(i) in {-1,0,+1} indicate the sign of the current first-axis direction (zero for the other directions), epsilon(i)=|sigma(i)|, and r in {-1,0,+1} be the original root sign. On legal phase edges define

tau_r(i,j) = [epsilon(i)+epsilon(j)-|sigma(j)-r|+|sigma(i)-r|]/2.

PREFIX-539 establishes that tau is 0 or 1 on every edge and sums to the path's first-axis BRC cancellation count. Define the 96-port transfer M_r with edge weights q^(tau_r) z^g. Its scalar future observer at port v is F_v^r(d)=e_v^T M_r^d 1. PREFIX-545 gave 28 full-length scalar observational classes for each r separately, with a finite weighted-row certificate and depth-5 separation.

## Theorem 1 — common partition and Laurent diagonal gauge

For all three r, the 96 original ports induce the SAME partition into 28 exact scalar future-observation classes. Each common class C has a constant phase sign sigma_C. Their sign counts are two classes at -1, twenty-one at 0 and five at +1.

Put ell_r(s)=(|s-r|-|s|-|r|)/2, and D_r=diag(q^(ell_r(sigma_C))). Then the 28-by-28 weighted quotient transfers satisfy the exact identity

**Q_r = D_r Q_0 D_r^(-1)** over Z[q,q^(-1),z], for r=-1,0,+1.

Specifically ell_0=0; ell_(+1)(s)=-1 only at s=+1; ell_(-1)(s)=-1 only at s=-1. All actual Q_r entries have nonnegative q-exponents and lie in N[q,z]. For every integer d>=0,

Q_r^d = D_r Q_0^d D_r^(-1),

and rooted readouts can be recovered as
F_C^r(d)=q^(ell_r(sigma_C)) e_C^T Q_0^d (q^(-ell_r(sigma_D)))_D.

Thus a single neutral-root 28-class transfer and class-sign vector generate every original-root scalar joint BRC–gate distribution, including all 48 roots with the appropriate initial branch bit.

### Proof

Subtract tau_0 from tau_r on any original phase edge i->j. The epsilon terms cancel, leaving exactly ell_r(sigma(i))-ell_r(sigma(j)); the constant normalization -|r| cancels between endpoints. The gate weight is unchanged. Hence M_r is diagonal-gauge-conjugate to M_0 on all 96 ports.

The r=0 28-class weighted-row quotient is exact by the exhaustive PREFIX-545 row-congruence proof. The current finite certificate enumerates all 96 memberships and verifies sigma is constant within every quotient class. The 96-port diagonal gauge thus descends to a well-defined diagonal gauge on the 28 classes. It produces valid weighted-row quotient matrices Q_r with equal scalar futures for all ports identified at r=0. This proves at most 28 classes for each r. The direct depth-0-through-5 polynomial fingerprints distinguish 28 classes for both other signs, and the certificate checks equality of all three original-port equivalence relations. Consequently the common 28 classes are exactly the all-length scalar observational classes for all three signs. The all-length part is by the finite row-congruence and induction; the 28-class lower bound is witnessed by finite exact polynomial fingerprints. QED.

## Theorem 2 — not permutation-equivalent, but diagonally similar

The three quotient matrices are pairwise NOT related just by row/column permutation over Z[q,z]. Under simultaneous class permutation the all-entry weight sum remains unchanged. Exact complete weighted-row enumeration gives:

- sum of all entries of Q_(-1) = 128 + 38q + 2qz;
- sum of all entries of Q_0 = 126 + 40q + 2qz;
- sum of all entries of Q_(+1) = 142 + 24q + 2z.

These polynomials differ pairwise. Nevertheless Theorem 1 supplies an exact diagonal Laurent similarity, a stronger and useful structure than label identity. QED.

## Exact execution

The Python standard-library certificate PREFIX546_shared_gauge_certificate.py, using the pinned predecessor module PREFIX545_compact_exact_certificate.py (Git blob 376476947ad4035decb31ff1f28b2fbb97481ce0), checks the full original port class relations, all three direct quotient rows against the neutral quotient with integer exponent shifts, and exact symbolic future readouts.

Actual results: ALL_CHECKS_PASS; 28 common classes, class signs (-1:2, 0:21, +1:5); 504 rooted labeled weighted edge contributions (three signs times 168); 7,200 exact full polynomial comparisons (3 signs times 96 ports times 25 lengths, 0..24). Infinite-length equality is justified by the weighted-row congruence plus the algebraic gauge identity, not inferred from the finite readout window. The original native endpoint checks (48 roots x 2 bits x 8 lengths) are preserved in PREFIX-545.

An additional local standalone certificate evaluated the 28-state scalar Krylov matrices at q=2,z=3 modulo 1,000,000,007, finding rank 23 for each sign. The specialized nonzero minor is a generic rank lower bound of 23 over Q(q,z); determining exact generic minimum linear rank remains open.

## Full-batch implementation and measured costs

PREFIX546_batch_benchmark.py compares the common 28-class realization to the exact 49-coordinate baseline PREFIX542_exact_certificate.py (Git blob 4ae63c3635fe549702e63a7c285de9a1ba460888). All 48 root polynomials (initial OUTER) and every length 0..D are recovered and compared by exact dictionary equality. Measurements: one CPython 3.13/Linux x86_64 process, gc before each run, tracemalloc enabled, five-run medians. The 49-coordinate module precomputes its static BACK table on import; the 28-class quotient+gauge setup is measured and added separately.

Setup of Q_0 and both gauge transforms: median 0.016818 seconds, peak 242,040 bytes.

| D | Exact output polynomials | 28-core seconds | 28-core + setup seconds | 49-core seconds | 28-core peak bytes | 49-core peak bytes |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 432 | 0.009698 | 0.026516 | 0.026701 | 175,592 | 314,648 |
| 16 | 816 | 0.044537 | 0.061356 | 0.099984 | 612,864 | 1,126,032 |
| 24 | 1,200 | 0.111464 | 0.128282 | 0.247357 | 1,522,636 | 2,810,000 |

At D=24 this implementation is about 1.93 times faster counting 28-class construction and complete readout, and uses less memory in the measured core stage. Runtime values are exploratory; complete peak including all imports/preprocessing and generalized input scaling were not measured here.

## Model boundary and next unit

These theorems apply to the declared scalar all-continuation joint BRC–gate readout in the frozen four-STAR X6 candidate. The controlled chosen-action language still has 51 exact classes; native Cell identity, phase/bit provenance, original six spatial axes, future path operations and joint relations are retained in their typed original state. This quotient is a valid observer-specific compression, not a global change to P000 or the Heartbeat World ontology.

Next PREFIX-547: establish the generic Krylov rank over Q(q,z), study a constructive linear realization for all rooted outputs, and test multi-axis BRC joint observation while retaining explicit original-port and Cell relations.

Native control em_status and em_control_continuation returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false. No verified native Researcher-ID, current owner, formal CLAIM, Result, Review or admission was established. Publishing source-bound mathematics is not formal task acceptance.
