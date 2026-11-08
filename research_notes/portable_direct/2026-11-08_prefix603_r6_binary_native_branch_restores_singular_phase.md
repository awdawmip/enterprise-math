# PREFIX-603-R6 — Exact repair of singular native BRC phase observers using one action-origin bit

Date: 2026-11-08 (Asia/Shanghai).
Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_PROVED / EXACT_NATIVE_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Dependencies: original PREFIX565 typed native BRC graph (Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41), PREFIX600 native star-incidence theorem, PREFIX601 six-factor weighted discriminant, PREFIX602 sharp 2k-dimensional phase repair.

## Exact question and native observer

The original primitive has 48 signed phases, 96 phase/bit ports, six original labeled actions (slot,newbit) with slot in {0,1,2}, and nine allowed reward roots. In PREFIX601's explicitly parameterized native-action-graph deformation, a phase p at incidence e(p) has one within-star native successor NEXT[p][0] of unnormalized weight 1 and two cross-star successors NEXT[p][1], NEXT[p][2] of weight t_e >= 0, each. The normalization is s_p=1+2t_e. The original frozen kernel is exactly the all-t=1 section.

The observer is the NEXT-PHASE distribution, not the seven-reward/branch-bit history. The new retained bit of native action provenance is I=1 if slot=0, otherwise 0. It is observed *jointly with* the next signed phase: z_int(j)=Pr(I=1, X_1=j). A single scalar Pr(I=1), without endpoint linkage, is a different weaker observer.

## Theorem 1: a universal explicit left inverse

The 48-phase native map sigma(p)=NEXT[p][0] is a permutation. The original within-star component consists of eight 3-cycles on each 24-phase sign sheet, with sign sheet exchange on each step. For every finite nonnegative real 12-vector t and every initial phase probability distribution pi,

    z_int(sigma(p)) = pi(p) / s_p,
    pi(p) = s_p z_int(sigma(p)).

Hence the binary-tagged joint observer is injective even when the *untagged* phase kernel P(t) has rank 48-2k, k=1,...,6. Equivalently C=diag(1/s_p) W_native, with W_native the 48-phase permutation, is invertible for all t >= 0.

PROOF. The internally tagged transition from phase p has exactly one terminal phase sigma(p), with normalized probability 1/s_p; two newbit copies of this action have total probability 1/s_p. Distinct p have distinct sigma(p) by the native permutation. No other p can contribute to the tagged outcome (I=1,sigma(p)). Multiply by the strictly positive s_p to invert. This is an exact finite transition statement, uniform over all nine native reward roots. At the original t=1 section, s_p=3 and pi(p)=3 z_int(sigma(p)). QED.

## Theorem 2: sharp 2k sparse scalar repairs extracted from the binary tag

For k critical reciprocal incidence pairs {e,f} satisfying 4t_e t_f=1, PREFIX601 established rank P(t)=48-2k. PREFIX602 constructed an exact basis ell_1,...,ell_(2k) of the LEFT nullspace of P(t) from the original native incidence data. Each ell is supported on exactly four source phases (a reciprocal pair and one sign sheet).

Given any such ell, define an endpoint coefficient f_ell by

    f_ell(sigma(p)) = s_p ell(p).

The tagged joint histogram determines the scalar linear statistic

    r_ell(pi) = sum_j z_int(j) f_ell(j) = sum_p pi(p) ell(p).

Each f_ell has exactly four nonzero entries. The augmented observer consisting of untagged pi P(t) and these 2k scalar tagged projections is injective: if pi-pi' lies in the left nullspace and has vanishing inner products with every basis ell, the positive-definite Gram matrix forces pi=pi'.

Conversely, fewer than 2k additional real linear scalar measurements cannot restore injectivity on the strictly positive 48-phase probability simplex. Indeed a nonzero left-null direction would also annihilate all added measurements; because P(t) is stochastic the direction sums to zero. Opposite sufficiently small perturbations about a strictly positive law are distinct normalized laws with the same measured outputs. Thus 2k is the SHARP minimum extra number of linear scalar coordinates for repairing the untagged phase observer.

Resource distinction: ONE extra bit is the native tag alphabet per observed step; its JOINT terminal-phase histogram has up to 48 real entries. The minimal 2k scalar repairs are sparse signed projections extracted from that histogram, not 2k native bits. Algebraic recovery is exact; the internal event probability 1/(1+2t_e) can be very small at high weights, so no uniform sampling error guarantee is claimed for unbounded t.

## Executed exact evidence

The executable Python-stdlib checker uses actual pinned PREFIX565 NEXT/PHASES, ROOTS, and original incidence construction from PREFIX600/601/602. It independently enumerates all 48 native slot-0 edges, verifies bijectivity, constructs the 48x48 tagged C and untagged P for each rational case, checks exact ranks and 48 basis-law inversions, constructs every critical-pair left-null vector, proves 4-support tagged projections and rank restoration, and exhibits distinct strictly positive initial laws with identical untagged phase distributions but different tagged laws.

Table of performed checks:

| Weights | critical k | untagged rank | tagged rank | extra scalar measurements | tagged projection support |
| --- | ---: | ---: | ---: | ---: | --- |
| Frozen all t_e=1 | 0 | 48 | 48 | 0 | n/a |
| All t_e=0 | 0 | 48 | 48 | 0 | n/a |
| t_e=(i+1)/(i+3) for i=0,...,11 | 0 | 48 | 48 | 0 | n/a |
| First reciprocal pair (1/2,1/2), rest 1 | 1 | 46 | 48 | 2 | 4 each |
| First two reciprocal pairs (1/2,1/2), rest 1 | 2 | 44 | 48 | 4 | 4 each |
| All t_e=1/2 | 6 | 36 | 48 | 12 | 4 each |

Actual new checker return: ALL_CHECKS_PASS. Rational test operations are exact Fraction; the universal nonnegative REAL theorem follows from the algebraic permutation and prior complete rank/kernel proof, not from finite sampling of parameter vectors. All computations preserve the original typed BRC source and do not invoke classical pi, trigonometry, matrix exponentials or non-BRC physical substitutes.

## Scope and next discriminating question

This result concerns the 48-phase marginal of the declared weighted native-action-graph family; it does not reconstruct hidden initial bit distribution, and does not assert that the gate or six-axis reward alone identifies the lost phase directions. The action-origin tag must actually be retained; it cannot be inferred after it has already been discarded by an untagged observer. No Foundation/Working Truth admission, independent review or physics transfer is claimed.

NEXT: Using the same original PREFIX565 edge(port,action,root) interface, form the 96-port typed reward/gate-labelled one-step observer for each singular weight stratum. Determine exactly which 2k lost phase directions are visible using rewards alone, which require action-slot provenance, and the minimum extra tagged readings. Quantify sampling/precision cost for large max(t_e) separately from algebraic identifiability.
