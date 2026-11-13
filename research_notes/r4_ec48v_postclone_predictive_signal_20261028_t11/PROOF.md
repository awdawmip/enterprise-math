# EC48V — A transient source-neutral clone can alter the raw stopping region after one informative future observation

2026-10-28. AUTHOR_PROVED / EXACT_FINITE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED.
Auxiliary finite strictly positive two-source Weighted-BRC; NOT native X6 dynamics or a Source Result.
Parent: EC48U Draft PR #1600, immutable commit 43ffcd55c493067257a09ff73f01c64f336942ec, U1 and NEXT_TASK.md.

## Exact model and observation interface

Let H be a complete historical label with P(H=h)=Q(H=h)=w_h>0 and sum w=1. A one-state compressed controller does not retain H. Its only current fine-history likelihood-ratio readout at time 1 is L(H)=1. The old time-1 signal is constant. In the refined experiment the controller instead observes an additional transient J with P(J=j|H=h)=Q(J=j|H=h)=r_h(j)>0; J has no effect on the future physical signal Z. The controller at time 1 chooses stop+reject, stop+accept, or continue. If continuing, Z is drawn at time 2 from positive source kernels p_h(z),q_h(z), and the terminal acceptance rule sees the current Z and exact *full controlled-history* LR L(H,J,Z)=p_h(z)/q_h(z). J may either disappear or remain visible at time 2. All trajectories end by time 2. Private randomization is independent of source and not a hidden persistent memory channel.

The four-vector region is S=(alpha=P(accept),beta=Q(accept),E_PT,E_QT). Compare old and refined ONE-STATE controller regions and the full-history H-visible controller, not an extra hidden-history future reward. Define the support functional F_c=alpha-beta-c(E_PT+E_QT), c>=0. Every policy pays base time penalty 2c; a continuation to time 2 adds 2c times its common P/Q occurrence probability. Stopping at time 1 can contribute no positive alpha-beta because P(H,J)=Q(H,J).

## Theorem V1: exact predictive stopping option value

Write
  W_j = sum_h w_h r_h(j) >0,
  G_j = sum_{h,z} w_h r_h(j) [p_h(z)-q_h(z)]_+ >=0,
where [u]_+=max(u,0). Then among ALL admissible stochastic one-state controllers:
  V_old(c) = -2c + [sum_j G_j -2c]_+;
  V_refined(c) = -2c + sum_j [G_j -2c W_j]_+.                    (V1)
The refined value is identical whether the transient J persists at the terminal.

Proof: Conditional on continuing through a fixed j, the terminal rule 1{L>1} is legal, since the sign of p_h(z)-q_h(z) is exactly the sign of L-1. It attains total accepted P-Q mass G_j. Any other accept rule cannot exceed this leafwise signed positive part; equal-LR collisions do not obstruct it because identical LR has identical sign. The extra sum of stopping-time expectations after continuing j is 2W_j. Time-1 acceptance has P-Q contrast zero and never increases F_c. Thus each j can be optimized independently, yielding [G_j-2cW_j]_+; old observation offers only one pooled time-1 decision, with pooled G=sum_j G_j and pooled W=1. The expectation under stochastic behavioural decisions is affine in each local rule, and the finite policy maximum occurs at deterministic extreme points. Arbitrary ex ante mixtures also cannot exceed the maximum. QED.

Define v_j=G_j/W_j, vbar=sum_jW_jv_j. Exactly:
  V_refined(c)-V_old(c)
     =sum_j W_j[v_j-2c]_+ -[vbar-2c]_+ >=0.                   (V2)
For this single support family, equality for EVERY c>=0 holds iff all v_j agree. If v_j differ, choosing 2c strictly between min(v_j) and max(v_j) yields mixed positive/negative branch net benefits, hence a strictly positive gap. For a FIXED c, positivity is equivalent to having both positive and negative entries among G_j-2cW_j (zero entries do not matter). This criterion is not a sufficient statistic theorem for arbitrary four-vector regions, other support directions, or longer dynamic horizons.

The physical meaning of v_j is E[g_H|J=j] under the common w, where g_h=sum_z[p_h(z)-q_h(z)]_+. The LR currently read out at time 1 is constant, but J predicts whether an *optional future informative test* is worth its cost. A J-kernel constant over hidden histories makes v_j constant, but is not necessary for this particular option-value equality.

## Certificate V2: eight strictly positive rational leaves

Two hidden histories A,B have w_A=w_B=1/2 under P,Q. Independent of source given H:
  r_A(1)=3/4, r_B(1)=1/4; r_A(0)=1/4, r_B(0)=3/4.
Future binary Z:
  p_A(1)=3/4, q_A(1)=1/4;
  p_B(1)=q_B(1)=1/2;
the Z=0 probabilities are complements. All 8 (H,J,Z) leaves have strictly positive P and Q masses, with total P mass=total Q mass=1. At time 1 P(J=j)=Q(J=j)=1/2, and all full H,J LR equal 1. Terminal full-path LR is 3 at A,Z=1, 1/3 at A,Z=0, and 1 at B,Z=0 or 1; the source-neutral r_h cancels from the full LR.

Direct rational aggregation gives W_0=W_1=1/2, G_1=3/16, G_0=1/16; thus v_1=3/8 and v_0=1/8. Strict difference holds for EVERY real 1/16<c<3/16. At c=1/8:
   V_old=-1/4,  V_refined=-3/16,  gap=1/16.                 (V3)

Refined witness: reject and stop at J=0; continue if J=1; accept at time 2 iff L>1. Its actual four-vector is
   O=(9/32, 3/32, 3/2, 3/2)
and F_{1/8}(O)=-3/16. Old one-state strategies all satisfy F_{1/8}<=-1/4; this separates even the convex hulls of the raw four-vector regions. J is NOT needed at the terminal for this separation. Full-history H-visible controller continues only on H=A and has optimum -1/8, so J improves a constrained observer without making it full-history sufficient.

Complete exact gap (c>=0):
   Delta(c)=0 if c<=1/16 or c>=3/16;
   Delta(c)=c-1/16 if 1/16<c<=1/8;
   Delta(c)=3/16-c if 1/8<c<3/16.
No "future branch reward" replaces the declared four coordinates.

## Executed verification and validity boundary

VERIFY.py performs exact Fraction checks on normalization, strict positivity and LR; exhaustively enumerates deterministic time-1 and terminal acceptance rules for the finite explicit model: 48 old-one-state, 144 refined-one-state/J-erased, 2,304 refined-one-state/J-retained and 20,736 full-history policies. All suprema equal the analytical values. A seeded 500-case rational check verifies the option-value identity and mixed-sign criterion; 47 finite cases had a strict gap at the sampled cost. The arbitrary cost interval is proved analytically, not inferred from finite samples. Randomized linear support optimization is covered by the extreme-point proof. No Lean formal verification or independent reviewer.

Reused source-qualified Weighted-BRC positive rational branches, exact source masses, full path likelihood ratio and provenance/observer leases from definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json at project main@5ee39e714b4df6d4e7a87ce66c8eca3c3348c030; reuse resolution REUSE_APPLIED. This is auxiliary positive-rational branching, not native heartbeat BRC–Shor arithmetic. Terminal Q-fiber compression of EC48U is valid for its exact terminal-only observation horizon but fails to authorize removal of a future decision-relevant branch residual. Classical Blackwell sufficiency and costly-information theory are relevant prior art; this note does not claim their general principle as new.

GLOBAL_KNOWLEDGE_V1 fixed snapshot main@cd47c1ecd3ba6262dfa1e96bdd3237251cd942fc. P000_STARTUP.json original canonical blob matched 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. ACTIVE worldview and P000 not modified. GitHub actor awdawmip has repository push permission; native em_status 0.6.11 reported research_authority_granted=false, control quota 5/5, no executor binding; actual owner list query em_control_tasks returned CONTROL_QUOTA. Hence no active Owner or CLAIM assertion, no native Research-Activity/Result, and no independent Driver approval. Author-side portable research only. Continuation in NEXT_TASK.md.