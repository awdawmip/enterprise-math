# EC48U — History-dependent terminal cloning: exact LR-fiber theorem and causal obstruction

Date: 2026-10-28. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASS / UNREVIEWED / NOT_ADMITTED. Auxiliary finite strictly-positive two-source BRC stopping/acceptance observer model only. Not an X6 physical-dynamics theorem, formal Source Result, or independently reviewed result.

## Exact prior frontier / evidence status
Parent EC48T Draft PR #1595, immutable parent commit 4cad523163f2698cd24d961c260e2ed0d7cf8125, PROOF.md and NEXT_TASK.md read. Canonical global knowledge main frozen at e8edf6c73fd946a9239541d811134ba887c737f6; Enterprise Math main at 8c37266a7eed9f91bf90e0dcec8421aba1ad398c. P000 native six-axis X6 space, separate time, ACTIVE worldview, and joint-future-observer rules unchanged. Native owner inventory: CONTROL_QUOTA; native session registration: STATIC_READONLY_SCOPE_DENIED / operation_sent=false. This is author-side portable material with pending formal activity/CLAIM/Result/Driver adjudication.

EC48T proved raw four-coordinate invariance under terminal source-neutral cloning where r(j|i) did not depend on lost history. We replace that restriction with a more general exact observer-specific theorem, and separately distinguish causal equivalence and coarse LR.

## Definitions

Fix a finite tree with two probability sources P,Q, and strictly positive masses at all permitted events. Freeze one finite-state (m states) randomized stop/accept controller's entire preterminal policy. Let Ω be the set of positive-mass fine atoms reaching its last accepting decision. It may include realized source-neutral control randomization. Each ω has masses p_ω>0 and q_ω>0. Its old visible terminal interface is x(ω)=(memory state m_ω, old signal i_ω, L_ω), where **L_ω=p_ω/q_ω is the exact joint P/Q likelihood ratio of its whole fine controlled history**. This is read out exactly even when ω itself is not recoverable; controller memory is otherwise bounded by the given m. A source-neutral earlier control coin multiplies both masses by its same conditional probability and cancels from L.

Refine old terminal ω into (ω,j), j in finite alphabet J, with strictly positive conditional probabilities r_ω(j), sum_j r_ω(j)=1. The kernel r_ω may depend arbitrarily on hidden ω and control memory, but is identical under P and Q given ω. Newly visible j changes no previous action, no stop time and no later operation; the terminal controller may accept with probability a(x,j)∈[0,1]. Private source-neutral randomized accepting coins are legal. Let S_m be the **raw** set of (P(accept),Q(accept),E_P T,E_Q T) for m-state controllers, and S_full the corresponding full-history set.

## Theorem U1 — exact raw-region invariance for arbitrary hidden-history-dependent terminal clones

For every such finite tree and every m≥1,

    S_m(refined)=S_m(original),      S_full(refined)=S_full(original).

Proof. The inclusion original⊆refined follows by ignoring j. Conversely fix an arbitrary refined m-controller and copy every preterminal stop/accept, randomization, and memory-update rule into the original tree; stop-time means and earlier accepting masses under both sources therefore match. Integrate the terminal clone at every fine atom,

    A_ω := ∑_j r_ω(j)a(x(ω),j) ∈ [0,1].

Partition reached atoms into fibers F_x={ω:x(ω)=x}. On each nonempty fiber construct the old legal terminal randomized accepting rule

    a*(x) := [∑_{ω∈F_x} q_ω A_ω] / [∑_{ω∈F_x} q_ω].               (1)

It requires only current m,i,L, no additional persistent state, and can be sampled by one terminal private coin. This exactly preserves the accepting Q mass fiber by fiber. Since p_ω=L_x q_ω on F_x, it also preserves accepting P mass:

    ∑_{ω∈F_x}p_ω a*(x) = L_x ∑_{ω∈F_x}q_ω A_ω = ∑_{ω∈F_x}p_ω A_ω. (2)

Earlier accepting contributions and both stopping-time means already coincide. Thus every refined raw four-vector is attainable in the old experiment, proving refined⊆original. For full history simply use accepting probability A_ω at ω. QED.

The Q-fiber average (1) is computed offline from the fixed experiment and policy, not by accessing ω online. It is a **distributional observer-specific** simulator, NOT a sampler reproducing the conditional law J|ω. The theorem is not limited to support functions/convex hulls. For each m raw-region equality holds; hence the least memory budget preserving the raw region relative to full history (if defined) is invariant under terminal-only history-dependent neutral cloning.

## Proposition U2 — exact criterion for strong causal cloning

For this controller and interface x, a source-independent simulator seeing only x and using fresh private randomness reproduces the *conditional distribution of J for every actual fine atom ω* (therefore the entire joint law of (ω,J) under both P,Q) if and only if, for every j, r_ω(j) is constant on every nonempty F_x.

Necessity: two fine atoms with the same x feed the same sampler; its conditional j-distribution cannot take two values. Sufficiency: sample the common r_x(j). This stronger condition allows arbitrary future observers of the joint (ω,J) to be preserved, provided the simulation and further update interfaces actually retain needed j. If j is required by later stages but cannot be re-read, its storage/future control memory must be separately accounted for. U1 does NOT imply this strong property.

## Certificate U3 — four-leaf strict coarse-LR obstruction

Let two hidden histories A,B have P=(3/4,1/4), Q=(1/4,3/4). The old observable has one terminal symbol i and **only the coarsened LR** P(i)/Q(i)=1; no persistent memory. An old accepted pair is (u,u), hence sup(α−β)=0. Introduce a strictly positive, source-neutral conditional clone j∈{0,1} with r(j=1|A)=3/4 and r(j=1|B)=1/4. Under P the four terminal (h,j) masses in order A1,A0,B1,B0 are (9,3,1,3)/16; under Q they are (3,1,3,9)/16. Accepting iff j=1 produces (α,β)=(5/8,3/8), giving a **strict exact support defect at least 1/4** compared to the old coarse-LR controller. With fixed last stop T=2, both time means are 2 and the same gap applies to the four-coordinate support direction (1,−1,0,0).

This is deliberately NOT a U1 counterexample: the old full fine-history LR is (3,1/3), not 1; if that readout is available, the old controller can distinguish A,B. The precise LR interface and observation chronology matter.

## Certificate U4 — terminal observation safety does not imply future joint-operation safety

Use P=Q=(1/2,1/2) on hidden histories A,B, a single old i and m=1. The **full fine-history LR** is 1 at both histories, so x is identical. Clone r(j=1|A)=3/4 and r(j=1|B)=1/4, source-neutral and strictly positive. Terminal two-source acceptance and stop-time regions remain unchanged by U1. But a later declared relational observable receives real H and J and returns R=1{(H=A,J=1) or (H=B,J=0)}. Its true mean under P and Q is 3/4. Any x-only sampler emits J=1 with fixed probability u, yielding mean [u+(1−u)]/2=1/2, irrespective of u. The future-observer discrepancy is exactly 1/4. The two sources happen to coincide in U4; U3 independently uses distinct strictly positive sources.

Thus a terminal-only observationally sufficient quotient can discard a future-relevant **joint branch residual**. This is not a four-coordinate stopping-region support gap (that would conflict with U1). All stronger future claims require an explicit operation-specific factorization or retention of the joint branch–clone relation.

## Executed evidence and limits

Python fractions.Fraction verifier was executed locally on 750 seeded rational positive two-source trees (seed 48021), including early source-neutral random stop/accept, two-source signal kernels, 1–3 memory states, 1–3 old signals, source-neutral hidden-history-dependent clone kernels and randomized final actions. The exact Q-fiber reconstruction passed on all four coordinates; 68 of the trees had full joint LR collisions. U3 and U4 rational certificates and normalized masses were also checked. These finite tests are not the universal proof; U1/U2 above are analytic and U3/U4 are explicit certificates. No Lean checking, external replication or formal mathematical admission.

BRC interface reused: exact positive-rational weighted branch masses, exact likelihood-ratio fibers and observer/future-operation safety. REUSE_APPLIED (mathematical carrier), no claim of executing native BRC engine. The theorem involves an auxiliary binary-source probability observer, not native Heartbeat World six-dimensional Cell dynamics. P000 and ACTIVE worldview remain unchanged; transfer needs a typed native X6 embedding, separately typed time, complete readout, joint-relation preservation and a proof that later native updates descend through any quotient.

## Literature and next exact unit

Related classical Blackwell/garbling framework: Rauh et al., Coarse-Graining and the Blackwell Order, Entropy 19(10):527 (2017), DOI:10.3390/e19100527; Max Planck preprint https://www.mis.mpg.de/publications/preprint-repository/article/2017/issue-74. Mathematical originality relative to the full literature is unreviewed.

EC48V: add one informative post-clone stage; determine necessary and sufficient finite-memory predictive state or a minimal exact rational support-gap witness. In particular do not equate the U4 joint-future reward with the already fixed four-coordinate stopping objective. Preserve source/memory/LR readout, stopping time and future operation type in the next study.
