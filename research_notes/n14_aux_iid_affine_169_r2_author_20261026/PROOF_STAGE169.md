# Stage169 — exact complete-real optimal interval and strict support-line sharpness

**Scope/status:** author-side exact finite computation plus a self-contained argument, not an independent Driver review, native CLAIМ/Result, or native P000 X6 Cell theorem. The model is an **external** horizon-14 three-symbol IID sequential test; its randomized policies may inspect every ordered history, not just a count statistic.

**Immutable science inputs:** GLOBAL_KNOWLEDGE_V1 canonical main@b1c6f9e87fc51617f9b75e37235682850b279b20 (bootstrap, operating manual, locked P000 and ACTIVE worldview from the same pinned snapshot); Enterprise Math main@40ae5bccbce019f594aa9044fb4ed54847cafe3c for portable research/control rules; predecessor Stage168 author result and Stage169 dual candidate from EM@253334e2a08694d8a564338414b5ab73ee08f899 in research_notes/n14_aux_iid_affine_168_r1t11_author_20261026. The Stage168 proof is author-side, not independently admitted.

## Theorem

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), and stop at an observation count τ≤14. Set eP=P(decide Q), eQ=Q(decide P), tP=E_P τ, tQ=E_Q τ and
V14(α)=min{max(tP,tQ):eP≤α,eQ≤α} across all full-ordered-history randomized policies.

Start with the Stage168 exact endpoint
α168=882432475025404219615/2530093150022563528704,
V168=4191390146637112343957/361441878574651932672.

For **every real** δ in
0≤δ≤η169=1973578354315/3904464737689141248,
including irrational δ, we prove

**V14(α168+δ)=V168−[601328993941480/1184147012589] δ.**

The new endpoint is
α169=882433753904177815735/2530093150022563528704,
V169=4191297370163761372757/361441878574651932672.

For every α>α169, this *same* affine Bellman support line lies strictly below the optimum V14(α); this does not assert that the value function terminates there.

## Dual bound covering every policy

At count state s=(n,a,b), count outcomes 0 and 1 by a,b, and define the prefix likelihood ratio ell(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. Put

K=100796326719840/394715670863,
L=298940013781960/1184147012589.

The backward dynamic program at n<14 is H(s)=min{K ell(s), L, 1+Σ_i P_i H(child_i(s))}; omit continuation at n=14. The finite tree induction holds for any arbitrary *ordered-history* randomized strategy because all histories of a given count state share this conditional IID continuation problem. Thus Hroot≤tP+K eQ+L eP≤max(tP,tQ)+(K+L)α on the feasible set.

Fraction-exact exhaustive enumeration of Σ_{n=0}^{14} C(n+2,2)=680 states gives
Hroot=24482517961003925257583517135827/129736380945356220519564705792.
The only two tie states are R=(10,0,1), stop-Q vs continue, and Y=(6,4,1), stop-P vs continue. Exactly 1,238 other permissible action gaps are strictly positive, minimum 199132488595033/18415854339784128. No negative gap. See VERIFY_STAGE169_REFERENCE.py and certificate169.json.

## Full-history primal realization

Choose stop-Q at R with coin r, stop-P at Y with coin y, and elsewhere the unique minimal action. The two first-hit ordered path cones are disjoint: Y already has four symbol-0 observations by n=6, whereas R has zero at n=10; such counts never decrease. A separate unmerged prefix-DFS with integer numerator P weights (3,1,20)/24 and Q weights (1,1,10)/12 finds these **distinct ordered first-hit branches**:

R: 10 paths; P first-hit mass 9765625/120932352; Q first-hit mass 9765625/60466176.
Y: 18 paths; P first-hit mass 5/32768; Q first-hit mass 5/82944.

Because the first-hit cones do not overlap, the four observer coordinates M=(eP,eQ,tP,tQ) have the exact affine form M(r,y)=M00+r dR+y dY. Cached Fraction count-state conditional suffix evaluation and the independent unmerged ordered DFS agree exactly for all four deterministic corners and all 16 coordinates. Their mixed interaction vector M11−M10−M01+M00 is (0,0,0,0), not an approximation. Both terminal P/Q masses equal one. The DFS traverses exactly 365077,352333,364837,352093 ordered nodes at corners 00,01,10,11 (1,434,340 total). All exact rational corners are preserved in certificate169.json and the full local verification package.

The difference D(M)=eP−eQ depends affinely on the coins and the coefficient of r is nonzero. The *unique* balance solution is

**r(y)=8969559568954741/11823616000000000 +(874857538089/1477952000000000)y.**

For every real y∈[0,1], 0<r(y)<1, with r(1)=8976558429259453/11823616000000000. At y=0 this strategy reproduces the exact Stage168 α,V endpoint. At y=1 the two equal errors reach α169; the difference is η169. All intermediate real α values are attained because the error changes linearly and strictly with y.

The time dominance tP−tQ is positive at both endpoints:
at y=0: 939301590775510833895/2530093150022563528704;
at y=1: 939181182760914408775/2530093150022563528704.

Both endpoints satisfy tP+K eQ+L eP=Hroot exactly. By affinity of the observers and balance relation, every real y in [0,1] has eP=eQ=α(y), tP>tQ, and attains the lower bound. Hence V14(α(y))=Hroot−(K+L)α(y), which proves the full-real theorem.

## Strict right support and limits

The feasible full-history randomized realization-plan polytope is compact and finite dimensional; optima exist. If an α>α169 attained the same support line, positivity of K,L would force eP=eQ=α, tP≥tQ, and Bellman-minimal action selection at each positively reached history. All three P/Q symbol probabilities are positive, so the strictly positive nonminimal gaps prohibit any action outside the unique actions and the two tie states R,Y. For any distinct ordered histories sharing R or Y, conditional suffix observers and the Q/P prefix ratio agree. P-first-hit-mass averaging of their possibly different coins gives one effective coin at R and one at Y, preserving *only the declared four observers* (not whole histories). The cones are disjoint, so every equality-attaining observer lies in M([0,1]²). Balance forces r=r(y) and legal y≤1 implies α≤α169, contradiction.

BRC use is explicitly **positive rational labeled path mass and first-hit provenance under two different P/Q observers**, not GF(2) signed/phase cancellation, a native six-dimensional Cell transport, or a reduction of future-relevant structured residuals. Native control task enumeration returned CONTROL_QUOTA, and session creation was denied with STATIC_READONLY_SCOPE_DENIED / operation_sent=false; no live Owner, formal CLAIM, Source Result, or independent review is asserted. GitHub source storage is not native admission. Proof calculations share the stated external model and do not establish physical applicability.

**Next exact unit:** Stage170 is presently DUAL-ONLY. A separate Fraction tangent/gap scan from Stage169 along dK=-1 and dL=-10592/12501 finds first closure at T=(12,5,2) (P/C), K170=4773735/18929, L170=14183320/56787. The primal balanced-policy interval, endpoint and sharpness remain open. See NEXT_TASK_PACKET_170.md and dual170.json.
