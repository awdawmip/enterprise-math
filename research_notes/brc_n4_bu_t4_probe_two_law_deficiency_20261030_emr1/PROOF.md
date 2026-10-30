# BRC N=4: sharp two-law information-loss witness for a genuinely fourth-leaf probe

Date: 2026-10-30. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. This concerns the external 16-leaf finite two-law BRC source used in PR #1738, commit ab8754904f4f82ecde486dd060a2620ec319371b. It does not change that PR's old-observer minimax theorem. A post-terminal time-four readout is an explicitly **new experimental operation** and not a P000 native-dynamics claim.

## Complete finite source and legal behavioral policy

At stage two the four Q source masses are AU=1/6, AV=1/3, BU=1/4, BV=1/4. Each source has two equal stage-three children j in {0,1}, each of which has two equal stage-four children k in {0,1}. The stage-three P/Q likelihood ratios are AU=(9/10,11/10), AV=(1/4,1/4), BU=(1/5,9/5), BV=(2,2). Thus the probability of each full leaf (origin,j,k) is Q=q_origin/4 and P=Q*r_origin,j, all strictly positive and each law summing to 1.

Use the legitimate instantaneous S23 policy G0 with A=B=c=1, U=V=0: AU and BU continue to T3; AV and BV stop at T2. AU stops at T3 with decision P, BU with Q. This T3 decision is current-LR measurable, because the AU child LR set {9/10,11/10} and BU set {1/5,9/5} are disjoint.

The original O'=(T,Decision,Z_BU,Z_AU) is exactly the same under P and Q:

| O' atom | P | Q |
| --- | ---: | ---: |
| (2,Q,0,0) | 7/12 | 7/12 |
| (3,P,0,1) | 1/6 | 1/6 |
| (3,Q,1,0) | 1/4 | 1/4 |

Therefore TV(P_O',Q_O')=0. The original target-fixing K' and its minimax conclusion were scoped to this terminal observer and its original stopping rules.

## New delayed external operation

Define Probe4, performed at time four even after T3 stopping, to inspect the actual exogenous fourth leaf and reveal H4=1 exactly if origin=BU, j=1 and k=1. This readout genuinely depends on the fourth leaf k. The operation requires exogenous leaf outcomes to remain accessible after stopping; that extra assumption is part of the new experiment and requires independent temporal-semantics review.

On the single BU coarse atom, H4 splits the masses:

| BU, H4 | P | Q |
| --- | ---: | ---: |
| 1 | 9/80 | 1/16 |
| 0 | 11/80 | 3/16 |

Every non-BU coarse atom has H4=0. Hence TV(P_(O',H4),Q_(O',H4))=1/20 while TV(P_O',Q_O')=0. This is an exact BRC provenance contrast: positive branch mass has not been signed-cancelled; the difference is in the measurable signed probability comparison.

## Sharp law-independent decoder obstruction

Any common stochastic decoder D, required to retain O' as a component, can choose only one parameter theta=Pr_D(H4=1|O'=BU). The P and Q conditional BU probabilities are p=9/20 and q=1/4, and the coarse BU mass m=1/4 under both laws. Its BU reconstruction TV errors are m*abs(theta-p) and m*abs(theta-q). The triangle inequality yields max error >= m*abs(p-q)/2=1/40. The midpoint theta=7/20 attains equality. Set H4=0 on all non-BU atoms; those are reconstructed exactly. Thus

**inf over all law-independent stochastic decoders D preserving O' of max(TV_P reconstruction, TV_Q reconstruction) = 1/40.**

This proves that the old K' coarse state is not sufficient for arbitrary permitted Probe4 operations in the declared extended model. It does NOT prove that no operation-aware compression can exist, or that the S2/S23 minimax value for the new observer differs from 71691/2414000.

For any similarly collapsed S23 policy with BU second-stage conditional continuation c and first-stage continuation B, independent of future child (j,k), its BU event has mass m=Bc/4 under each law; the same binary probe has sharp **BU-local** decoder radius Bc/40. For the old-observer attaining policy B=69/500, c=1039/1207, this gives BU mass 71691/2414000 and local lower bound 71691/24140000.

## Evidence, assumptions and status

VERIFY.py was executed using Python Fraction. It enumerates all 16 leaves, checks positivity, P and Q normalization, the exact three-atom coarse equality, both refined BU masses, TV=0 vs 1/20, and exact decoder optimum 1/40. VERIFY_EVIDENCE.txt contains actual console output. The optimality across all real theta is analytical via the triangle inequality, not a finite sample argument.

Original exact source: PR #1738, ab8754904f4f82ecde486dd060a2620ec319371b (five-atom minimax); PR #1735, 6d9bc93c9d110418d22daf344ed83d883a4a1a23 (16-leaf source and source-bit observer). Frozen GLOBAL_KNOWLEDGE_V1 main@c4901dbacb7d324d144197e88ca8a8d3a1c140ef; initial Enterprise Math main@ae26ceec541fc54102253d70ee80cefbb0fd3bbf. P000 and ACTIVE residual-fidelity worldview read without modification. GitHub actor awdawmip. Native Sites reports research_authority_granted=false; owner inventory returned CONTROL_QUOTA, so native Owner, CLAIM, formal Result and Driver review remain unverified.

**Next:** Give an operation-aware, two-law Markov/Blackwell sufficiency criterion for all chosen time-four operations. Determine the minimal BU repair coordinate for the singleton query and for all Boolean BU-leaf queries. Independently validate the delayed post-terminal readout as a lawful extension of the original model and specify any P000 native X6/time embedding separately.
