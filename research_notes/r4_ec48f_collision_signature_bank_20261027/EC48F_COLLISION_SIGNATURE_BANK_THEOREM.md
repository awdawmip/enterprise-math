# EC48F — Collision-signature bank compression for seedless BRC observation

**Date:** 2026-10-27 (Asia/Shanghai). **Status:** author-side mathematical derivation + exact finite verification; not a native Result, independent Driver review, Working Truth, Foundation theorem, or native-X6 dynamics.

**Frozen source inputs:** GLOBAL_KNOWLEDGE_V1 main@f105f4be6d05e87fb4b8c3e1737db6426a21a23d (bootstrap, manual, P000 V4, ACTIVE worldview and project/mathematics/BRC policies); Enterprise Math control main@5049d1b964e14be0ab2b2294977ef372144a6828 (P000 native-X6 companion and PORTABLE_RESEARCH_PROTOCOL); previous EC48E proof at immutable commit 629ff0645c1c43285cd9fa0dcdb44403117a23c1. Activity RA-EMR4-20261027-0730-EC48F-COLLISION, locally assigned researcher EM-R004-EC48F-20261027-R11. Researcher identity is not a native CLAIM.

## Precise model and problem

H is a finite set of distinct source histories, Y a finite set of later observable labels. Joint source laws p(h,y), q(h,y) are strictly positive and separately normalized. First stage: observe h and privately select one of K memory labels m according to the history-dependent stochastic encoder pi_h(m). Second stage: observe y, then declare hypothesis P with probability u_m(y), a value in [0,1]. There is no persistent common/public random seed. With w(h,y)=sum_m pi_h(m)*u_m(y), define alpha=sum p*w, beta=sum q*w, S_K={(alpha,beta):K-state policies}, and full-history zonotope Z=sum_(h,y) [0,(p(h,y),q(h,y))]. Define K_hull as the minimum K with conv(S_K)=Z and K_seed as the minimum K with S_K=Z. Decisions all terminate at the same second-stage depth; this is not a variable-stopping-time theorem.

For each distinct critical likelihood ratio r=p(h,y)/q(h,y)>0, let H_r be the histories having at least one cell with ratio r. For non-tied h outside H_r, their unique strict-optimal binary row is c_r(h)_y=1{p(h,y)>r*q(h,y)}; let C_r be the set of **distinct** such words. For each tied h define ordered binary endpoint words a_r(h)_y=1{p(h,y)>=r*q(h,y)}, b_r(h)_y=1{p(h,y)>r*q(h,y)}. The ordered *transition signature* is (a_r(h),b_r(h)).

Let D_r be the set of **distinct** transition signatures at r for which a_r(h) or b_r(h) is not already in C_r. Tied histories whose two endpoints are both in C_r are called C-absorbed. Write B_r=|C_r|+|D_r|, d=max_r |D_r|, and m=max_r |H_r|. In EC48A/E notation, K_hull equals the maximum number of distinct binary history-row profiles at a threshold strictly between consecutive critical ratios.

## Theorem EC48F.1: Exact tied-signature decoder bank

**For each critical r and each real s in [0,1], there exists a seedless policy with at most B_r memory states that realizes the complete-history optimal support alpha-r*beta and gives decision probability exactly s on every cell satisfying p=r*q.**

Consequently,

K_hull <= K_seed <= min(|H|, max(K_hull,max_r B_r), K_hull+max(0,d-1), K_hull+max(0,m-1), 2*K_hull).

The 2*K_hull bound is the already-established EC48D alternative and is **not** claimed as a new proof here. The other bounds follow from the following construction.

**Corollary EC48F.2 (synchronized collision equality):** If |D_r| <= 1 for every critical ratio r, then K_seed=K_hull, even if arbitrarily many distinct histories share one exact critical likelihood ratio. This strictly extends EC48E's sufficient condition |H_r|<=1.

### Complete construction and proof

Fix r,s. Create one decoder row equal to each word c in C_r. For each different pair (a,b) in D_r create exactly one further decoder row d_(a,b),s(y)=s*a(y)+(1-s)*b(y). Rows are indexed by private memory labels.

For a non-tied history h, encode deterministically to c_r(h). For a tied history h with pair (a,b) in D_r, encode deterministically to the one dedicated row d_(a,b),s; **all tied histories sharing the ordered pair reuse the same row**, irrespective of their different positive source weights. For a tied history h whose endpoints both belong to C_r, encode privately to existing word a with probability s and existing word b with probability 1-s. These are admissible conditional encoders and decoders with only B_r memory labels.

On a cell where p>r*q, both endpoint bits are 1, so w=1. Where p<r*q both endpoint bits are 0, so w=0. On a tied cell p=r*q, a=1 and b=0, hence w=s. Therefore alpha-r*beta = sum_(h,y) max(p(h,y)-r*q(h,y),0), which is exactly full-history optimal support. With Q_r=sum_(p=r*q) q(h,y), tied q-mass equals s*Q_r, ranging over the entire interval [0,Q_r]. As all tied generators of Z are parallel with slope r, this parametrizes the entire corresponding exposed face. The parameter s indexes separate strategies, not a persistent random seed. Private encoder randomization is used only in histories with both endpoint words in the bank.

For each r, B_r states therefore suffice for that exposed face. All strict-support vertices are attainable with K_hull states by assigning one memory label per distinct strictly optimal row. If D_r is empty, B_r=|C_r|<=K_hull. Otherwise some a or b from D_r lies outside C_r. For the generic threshold immediately below or above r, that outside endpoint occurs together with all C_r strict rows, proving K_hull>=|C_r|+1. Hence B_r<=K_hull+|D_r|-1<=K_hull+max(0,d-1)<=K_hull+max(0,m-1). Full-history deterministic memory always gives K_seed<=|H|; EC48D supplies the independent 2*K_hull bound.

Decoder complementation sends (alpha,beta) to (1-alpha,1-beta). Since every generating vector (p,q) has strictly positive coordinates, each nontrivial edge of the two-dimensional positive-generator zonotope is a support face with normal (1,-r) or its opposite, plus endpoint vertices; the above policies and their complements attain the complete boundary. Finally S_K is star-shaped about (0,0), because multiplying all decoder probabilities by t in [0,1] multiplies both alpha and beta by t. Each point of Z lies on a segment from 0 to a boundary point. Thus complete boundary attainment implies S_K=Z. If every |D_r|<=1, each B_r<=K_hull, so K_seed=K_hull. **QED.**

The theorem is a *sufficient* bank construction. |D_r|>1 is not evidence of a missing ROC interval or strict memory gap. The general implication conv(S_K)=Z => S_K=Z remains unresolved.

## Exact positive rational witness outside EC48E

Take positive raw joint arrays (rows are histories, columns later observations):

P_raw = [[1,3,5],[2,3,7],[2,3,7],[8,4,9]]; total 54.
Q_raw = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]; total 12.

Normalize p=P_raw/54, q=Q_raw/12. The open-interval sign profile maximum is K_hull=3. At the critical ratio r=2/3, the first THREE histories have a tie in their second label, even though the first history's other ratios differ from the next two histories. The fourth history is nontied with C_r={(1,1,1)}. All three tied histories have a=(0,1,1) and b=(0,0,1), so D_r contains exactly one pair. The two rows (1,1,1) and (0,s,1) implement this whole face:

alpha(s)=(40+9s)/54, beta(s)=(6+3s)/12,
alpha(s)-(2/3)*beta(s)=11/27 for all s in [0,1].

The exact scan gives max_r|D_r|=1 and max_r|H_r|=3. Therefore **K_seed=K_hull=3<|H|=4** despite genuine cross-history equal ratios. This is not covered by EC48E's one-tied-history assumption.

## Executed checks and scope

The project verifier EC48F_VERIFY_MIN.py uses standard-library fractions.Fraction. At every exact rational critical ratio it constructs the banks, actual conditional encoder/decoder probabilities, verifies forced strict bits and tied bits for s=0,1/5,1/2,4/5,1, and checks the exact support value and tied q-mass. A reproducible seed 202610270730 generated 900 strictly positive integer law pairs: 350 synchronized-ratio grouped families and 550 collision-rich families. The executed output is stored in EC48F_REPORT.json. This is finite implementation testing; the all-finite-model result is the proof above. It does not establish universal equality when d>=2, nor physical X6 propagation.

**Research ontology and BRC reuse:** This is an auxiliary two-stage positive-weight BRC source/decision observer with history provenance and temporal order retained, NOT native X6 Cell dynamics. The P000 research basis is six-dimensional native discrete Cell space plus one separately typed time dimension; no native-plane assumption is made, and no X6 readout/embedding preservation certificate exists for this auxiliary theorem. Source masses stay positive, while the signed expression p-r*q is a linear support test, not a signed BRC amplitude. EC48A/E sign-profile and exposed-face mathematics and EC48D two-bank bound are REUSE_APPLIED; the Fraction script is an EXTEND_EXISTING_TOOL type of narrow verification.

**Real permissions and admission:** GitHub authenticated actor awdawmip with repository push capability. Native em_control_tasks returned CONTROL_QUOTA. Native em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. The active native owner could not be verified and no CLAIM or native Result was obtained. Independent Driver review, theorem acceptance and native execution remain pending.

## Next EC48G

Investigate ratios with exactly two distinct unabsorbed pairs, |D_r|=2, and preferably two tied histories and K_hull=2 or 3. The bound above allows K_hull+1 but does not prove that one extra state is needed. Construct a continuous K_hull decoder/encoder reconfiguration path or provide exact positive rational P,Q, a critical r, optimal-encoder graph component intervals, and a missing rational open interval. Separately assess whether the additive bound is sharp. Native variable stopping/depth readouts and actual X6 dynamics remain different problems.
