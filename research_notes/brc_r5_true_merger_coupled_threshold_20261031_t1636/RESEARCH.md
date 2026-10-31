# R5 — Exact coupled terminal-error threshold in the original positive two-merger model

**Date:** 2026-10-31 (Asia/Shanghai). **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is a finite two-measure stopping-process result, not an accepted Source Result or native X6 theorem.

## Frozen provenance

GLOBAL_KNOWLEDGE_V1 main@407f466c44025bb91299a1635ab12d609a4fee1f; global P000 canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (verified against same-snapshot P000_STARTUP.json). Enterprise Math main@5a19591c6841efd21acd1bba1b123d2d90ab66ff. The original path construction and executed code are at immutable Enterprise Math commit e7916482f44a925e11ece98e406309f4655fb1f1, research_notes/brc_r5_positive_two_merger_rigidity_20261031_t1340/EM_R5_20261031_1340_evidence.tar.gz. The previous policy-coupled minimax method is at eb2bfcc9d29a80f2a7396914e9ac6ffc9d3ad8ae, research_notes/brc_r5_policy_coupled_gauge_20261031_t1540/README.md. This note applies that exact method to the **actual original double-merger paths**, not the previous auxiliary two-cylinder example.

P000, ACTIVE worldview, BRC provenance and the separate time type remain unchanged. Real behavioural probabilities here describe a declared auxiliary finite model; no X6 embedding or external physics claim is made.

## Exact natural flows and controls

There are hidden origins i=0,1 of initial Q and P mass 1/2 and LR=1. A=(t=1,LR=1) STOP has (error,time)=(0,1); CONTINUE reaches D,C,Y at t=2 with respective likelihood ratios (1/2,1,3/2), Q probabilities (alpha_i,1-2alpha_i,alpha_i), and P probabilities (alpha_i/2,1-2alpha_i,3alpha_i/2). Fix alpha_0=1/4, alpha_1=1/8. C must stop at t=2 with error 0. D STOP has error 1 at t=2; D CONTINUE leads with Q conditional probabilities (1/3,2/3) to the common LR=1 node L and residual LR=1/4 error 0 at t=3. Y STOP has error 0 at t=2; Y CONTINUE leads with Q conditional probabilities (1/2,1/2) to L and residual LR=2 error 1 at t=3. All corresponding P transitions obey P(child|parent)=(LR_child/LR_parent)Q(child|parent). At the genuine shared stage-3 L key, STOP ends at t=3; CONTINUE ends at t=4. Every natural branch is strictly positive and P,Q total masses are 1.

FULL decisions may depend on origin and complete D/Y history. Seedless LR uses only four shared (stage,LR) decision keys A,D,Y,L with no persistent random seed. The full observation is O=(error_P,error_Q,T_P,T_Q). The signed direction J(O)=41 error_Q - 12 T_Q is evaluated only after positive source-labelled P/Q path propagation.

For every full L history h=(i,j,a), with i in {0,1}, j in {D,Y}, action a in {STOP=0,CONTINUE=1}, introduce a **common** perturbed terminal error label r_h. Both FULL and LR policies use this same set of eight error probabilities. For real 0<=epsilon<=1:
- STOP labels: r_(i,j,0) in [0,epsilon].
- CONTINUE labels: r_(i,j,1) in [1-epsilon,1].
Other errors, stopping times, route transitions, information keys and P/Q path measures remain unchanged.

## Exact all-real theorem (fixed FULL witness)

Choose the deterministic FULL witness f: A CONTINUE only for origin 0, A STOP for origin 1, D STOP, Y CONTINUE, L CONTINUE wherever reached. Its baseline observation is (1/4,1/4,7/4,27/16), with J=-10; baseline LR maximum is -12. For each legal common terminal-error vector r define S_LR(r) as the maximum of J over **all real seedless LR behavioural policies**. Then the exact all-real robust margin for this **fixed witness** is

    M(epsilon)=min_r [ J(O_f(r)) - S_LR(r) ]
              =min(2-41*epsilon/16, (151-205*epsilon)/32)
              =2-41*epsilon/16                for 0<=epsilon<=29/41;
              =(151-205*epsilon)/32            for 29/41<=epsilon<=1.

Therefore, for EVERY admissible shared error vector and every real 0<=epsilon<151/205, FULL and seedless-LR four-observer convex hulls are strictly different. Specifically the witness is at L-infinity distance at least M(epsilon)/53 from the entire LR convex hull. At epsilon=1/16 the exact universal support lower bound is 471/256 and the hull-distance bound is 471/13568; the previous conditional coarse support bound at this epsilon was 5/64. The new claim is independently derived from the original path table, not from the predecessor Bellman bound.

The value 151/205 is **sharp only for this witness and this signed observer direction**: at that epsilon a legal terminal-response vector causes the witness to tie one LR deterministic policy in J. It is NOT a certificate of all-signed convex-hull equality or of the vanishing of the moving FULL optimum.

## Proof: exact common-label minimax, not independent policy perturbations

Let q_p(h) be the unconditional Q occupancy of a terminal L cylinder under policy p, before assigning its terminal error. These nonnegative occupancies are determined by the full history and natural transitions, and are independent of error labels. Write delta_h=r_h-a, where a is the baseline action error 0 or 1. For each policy p,

    J(O_p(r)) = J(O_p(0)) + 41 sum_h q_p(h) delta_h.

For witness f, q_f(0,Y,CONTINUE)=1/16; all seven other L-cylinder occupancies vanish. Each LR decision key is visited at most once, so its signed observer objective is multi-affine in its four real behavioural probabilities. It attains its maximum on the 16 deterministic LR vectors b=(A,D,Y,L). This remains true with history-sensitive terminal error marks.

Put m_b=J(O_f(0))-J(O_b(0)) and

    c_b = sum_(h action STOP) max(0,q_b(h)-q_f(h))
        + sum_(h action CONTINUE) max(0,q_f(h)-q_b(h)).

The same response labels are used by both classes. Since r_STOP-0 belongs to [0,epsilon] while r_CONTINUE-1 belongs to [-epsilon,0], minimizing the affine witness-minus-LR difference over the COMMON box selects its actual adverse endpoints. Finite minima commute, giving the exact identity for every real epsilon:

    min_r [J(O_f(r))-max_b J(O_b(r))]
        =min_b min_r [J(O_f(r))-J(O_b(r))]
        =min_b (m_b-41 epsilon c_b).

Exhaustive exact rational reconstruction of the 16 LR path occupancies gives the **entire** table (bits A,D,Y,L):

    0000,0001,0010,0011,0100,0101,0110,0111 : (m,c)=(2,1/16)
    1000,1001                               : (101/16,1/16)
    1010                                    : (151/32,5/32)
    1011                                    : (2,0)
    1100                                    : (65/4,1/8)
    1101                                    : (231/16,1/16)
    1110                                    : (469/32,7/32)
    1111                                    : (81/8,0)

All 16 affine rows are bounded below by the lower envelope of the 0000 and 1010 rows throughout [0,1]: on each piece it is sufficient to compare these linear functions at the three rational breakpoints 0, 29/41, 1. The two active rows intersect at epsilon=29/41. The 1010 row becomes zero at epsilon=151/205, proving the formula and fixed-witness sharpness. An explicit adverse label choice for 1010 raises STOP errors at both origins' Y-to-L histories to epsilon, and lowers the origin-0 Y-to-L CONTINUE error to 1-epsilon; all remaining labels may stay at baseline.

For epsilon<151/205 the exact lower envelope is strictly positive, hence J(O_f(r))>S_LR(r) for every legal shared vector r. The LR real-policy convex hull has the same signed maximum S_LR(r), so J strictly separates the FULL witness. Since the L1 norm of the coefficient vector (0,41,0,-12) is 53, the dual Hölder bound gives distance at least M(epsilon)/53. This finishes the all-real proof.

## Exact executable certificate and its limits

VERIFY.py uses standard-library Fraction only, reconstructs the original complete P/Q natural flows for all 1024 FULL and 16 LR deterministic policies and verifies normalization, the original witness and support extrema, the 16 (m,c) entries, the entire piecewise linear envelope via exact endpoint inequalities, and the two rational thresholds. It additionally enumerates all 256 COMMON error-box corners at each of five epsilon choices 0, 1/16, 29/41, 151/205, 1, independently checking the fixed-witness versus the maximum over the full 16-policy LR set. EXACT_OUTPUT.txt is the literal executed output and ends with PASS_EXACT_R5_COUPLED_MERGER_FIXED_WITNESS_THRESHOLD. Finite epsilon tests are regressions; the real continuum follows from the proved finite affine minimax and endpoint certificate.

This author-side result preserves the BRC origin/route/action cylinder carrier, positive likelihood-transported Q/P mass and source-sensitive residual. Formal independent Driver review, native task owner, CLAIM, Result, and any X6 readout bridge still require their own genuine permissions and evidence.

**Next mathematical unit:** replace the fixed witness by the moving FULL optimum. For each of 16 LR deterministic policies solve an exact rational LP in the eight COMMON error labels and epigraph variable, constrained by all 1024 FULL deterministic J payoffs; then minimize over LR policies to compute min_r[max_FULL J(r)-max_LR J(r)]. Only if the complete J gap can vanish should one test full four-dimensional all-signed convex-hull equality by exact <=5 LR-vertex convex certificates or Farkas separators, and only after that actual real LR-image nonmembership.