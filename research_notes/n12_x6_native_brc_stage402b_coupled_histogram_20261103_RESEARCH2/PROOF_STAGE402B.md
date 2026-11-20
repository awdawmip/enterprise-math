# Stage402-B: exact joint BRC histogram transfer; nonzero-K C=2 compression

Date: 2026-11-03. Classification: AUTHOR_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED. Parent: Stage401-B at dcbf958c5d6702244acff34bb6ca4558011e4c91, Draft PR #1736.
Frozen scientific pins unchanged: EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; Global bf84bd7c61a2444b59b1da96be57df0e9ae47e53; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavioral rules read separately. Native execution identity and current Task owner unconfirmed: STATIC_READONLY_SCOPE_DENIED / CONTROL_QUOTA.

## Domain and observations

The six-axis P000 primitive alphabet A={+E1,-E1,...,+E6,-E6} has 12 letters; a synchronized pair letter is in B=A×A (144). Two source-tagged aligned paths W=((p1,q1),...,(pm,qm)) retain their separate six-coordinate endpoints zP,zQ, 12×12 directed adjacency histograms JP,JQ, all 20 triple-coordinate readouts, and live coincidence K(W)=sum_i [pi=qi]. Endpoint-only unweighted and positive BRC masses are functions of m and z. A fixed nonzero multiplicative signed path trace is separately determined by per-letter multiplicities; it is not a positive mass.

Stage401-B future language: common paired APPEND(a,b), at most C synchronized CANCEL actions, latter enabled iff the two last paired letters are inverse **in both sources**. Each intermediate observer includes both marginals, live K, and enabledness. G_C(W) is Stage401's recursively defined exact joint future signature. This study is a Path-formal combinatorial observer, not a physical heartbeat model or a final native Cell address conversion.

## Theorem 402.1: exact coupled histogram distribution

For fixed m>=1, nonnegative directed integer JP,JQ each with total m-1, endpoints zP,zQ, coincidence r and budget C, a residual-edge integer DP computes

D_C(r,g) = # {W: (m,zP,zQ,JP,JQ,K(W)) is the prescribed observation, G_C(W)=g}

without enumerating entire paired histories. State after t>=1 positions is (a,b,RP,RQ,k,u), recording last paired label, *remaining* two directed edge multisets, matches seen, and last at most L=2C+1 paired labels. F_t(state) is the exact prefix count. Initialize with each initial (a,b) with residual JP,JQ, k=[a=b], and u=((a,b)), but only when the endpoints match the starting-letter indegree identity: the multiplicity of v in P is [v=a]+sum_x JP(x,v), similarly for Q. Multiply these exact counts by the appropriate signed native unit vectors to obtain zP,zQ.

If RP(a,a')>0 and RQ(b,b')>0, make one transition
F_(t+1)(a',b', RP-e_(a,a'),RQ-e_(b,b'), k+[a'=b'],tail_L(u||(a',b'))) += F_t(state).
At t=m with both remaining edge matrices zero and k=r, aggregate counts by G_C(u). The empty case m=0 contains exactly the empty history if all specified observations are zero.

**Proof:** Every paired history has a unique first letter and unique subsequent pair of directed transitions. Conversely each valid transition chain creates exactly one paired history. Inductively F_t counts every realizing prefix exactly once; merging state-identical prefixes preserves both future transition options and the count. Never multiply a transition by RP(a,a')*RQ(b,b'): duplicate directed edges are **unlabeled**, and that factor counts artificial labeled-edge permutations. The source endpoints are fixed by initial letter plus the incoming degree of each direction. K updates by exactly the equality indicator of each newly appended paired letter. By induction on C, G_0 depends on the final paired letter (or EMPTY), and G_C uses lower-order signatures for W,pred(W), and—if enabled—pred²(W); therefore it inspects at most 2C+1 final paired letters. If |W|<=L, the stored suffix is W and preserves EMPTY; if |W|>L the recursion never reaches the start boundary. Thus G_C(u)=G_C(W), so terminal grouping gives exactly D_C. Under Stage401-B future-equivalence, q_C=#{g:D_C(r,g)>0} is the exact minimal number of deterministic states, with ceil(log2 q_C) fixed bits. QED.

An equivalent forward recurrence stores **used** JP,JQ, current native displacements, K, the current last pair and L-letter suffix. It merges prefixes and accumulates exact BigInt counts; this is the implementation in the attached independently executed JS reproducer.

## Theorem 402.2: strict quotient at C=2 and LIVE K=4

Set A=+E1, B=-E1 while retaining the ambient 12-direction domain. Take P=(A,A,A,A,A,A), and Q from:
Q1=(A,A,A,B,A,B);
Q2=(A,A,B,A,A,B);
Q3=(A,B,A,A,A,B).

These form the ENTIRE exact current-observation fiber with m=6, zP=6E1, zQ=2E1, JP(A,A)=5, JQ(A,A)=2, JQ(A,B)=2, JQ(B,A)=1, K=4, all other entries zero. P is forced. Q must start A, end B and has exactly these three Euler walks. All listed BRC endpoint observations, 20 projections and any fixed multiplicative nonzero per-direction signed trace agree.

G_2 partitions this fiber into {Q1} and {Q2,Q3} (q_joint=2): the paired suffixes needed are respectively (B,A,B) and (A,A,B). With P always A, neither original adjacent paired pair admits immediate synchronized inverse cancellation; with two CANCEL allowances an APPEND inverse to the last paired letter followed by CANCEL can expose up to the last three original paired labels. This makes the two groups distinguishable while Q2 and Q3 remain jointly indistinguishable. In contrast, separately retaining the two sources' S_2 signatures distinguishes all Q1,Q2,Q3 (q_separate=3), because single-source Q can have its own inverse pairs even when simultaneous P cannot. Hence on this exact K>0 fiber the deterministic fixed-length representation compresses from 2 to 1 bit without changing any future observation in the declared paired language.

Independently running the native full 12-signed-axis step-count recurrence N_(t+1)(z)=sum_(a in A) N_t(z-step(a)) with N_0(0)=1 gives N_6(6E1)=1 and N_6(2E1)=4665. These count all native axis-step paths to the same endpoints; they are not the three histogram-constrained source histories.

## Complexity, verification, next question

Let sP,sQ be numbers of nonzero directed-edge slots. Residual possibilities <= prod_(e in support JP)(JP(e)+1)*prod_(e in support JQ)(JQ(e)+1) <= (m+1)^(sP+sQ); suffixes <=144^(2C+1), K has m+1 values, and last letters and depth contribute only further polynomial-in-m factors for fixed C. Thus at fixed sparse support and C the algorithm is polynomial in numeric m, **not claimed bit-polynomial** in the input's binary-encoded edge multiplicities. Individual exact output counts can require O(m log 144) bits. Zero slots among the full two-source 288 adjacency counters need not occupy DP state. Dense worst cases remain expensive.

Executed JS BigInt program exhaustively crosschecks all 5,461 paired paths m=0..6 over signed ±E1: 5,101 (fiber,G2) exact count checks. It checks the complete nonzero K=4 fiber and full twelve-direction BRC counts at m=6, return marker STAGE402B_COUPLED_TRANSFER_PASS. Separately executed Python residual-edge DP crosschecked all ±E1 observation fibers m=0..5 for C=0,1,2 (2,763 exact fiber/budget comparisons) and the witness. Generality beyond these finite domains follows from the above mathematical proof. No formal checker or independent Driver admission.

Stage403-B next: precisely define asynchronous single-source POP or a bounded source synchronization offset (including how K is observed after lengths differ), seek a minimal counterexample to G_2 future sufficiency under that enlarged language, then construct the least new alignment/trace residual and a typed exact BRC transfer. Preserve P000 and all scientific source pins.
