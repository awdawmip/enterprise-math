# BRC prime-cut rank and adaptive observer (AUTHOR DRAFT)

Status: UNREVIEWED / NOT_ADMITTED / NO_FORMAL_CLAIM. Date: 2026-10-11. This is a mathematical author draft, not a canonical Task Result, accepted theorem, or P000/X6 dynamics statement.

## Immutable input
- GLOBAL_KNOWLEDGE_V1 main: cebf09bb2c4efe43f40b8ed60e34e5b1ffd0b580; both 00_BOOTSTRAP.md and OPERATING_MANUAL.md, EM project router, P000 V4 and ACTIVE worldview were read under this pin. P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches P000_STARTUP projection.
- Enterprise Math protocol snapshot: 31d29efd75d5f9ac88e36e5bbd942a55c2b23e6c; AGENTS, PORTABLE_RESEARCH_PROTOCOL, CHATGPT_ORDINARY_CONTROL, BRC and native X6/residual/joint-observer contracts.
- Prior local author frontier: 20261011 Boolean-tree fixed-observer theorem and changed-horizon counterexamples; not a mathematically admitted Result.
- BRC reuse: T0_BRC Boolean support/path-result/provenance typing: REUSE_APPLIED. Composite factors, labelled words and provenance remain explicit. The prime-seed model is an auxiliary scalar observer fiber, NOT an independent native spatial axis, two-dimensional plane, or accepted physical X6 dynamic.

## Population and observations
Let S be a finite set of primes, p0 the first prime exceeding max(S), and r any prime >= p0. Allow M_s(n)=s*n and D_s(n)=n/s only if defined. Legal words of length <=L have every prefix exponent vector nonnegative and terminal factors U_L={prod(s^a_s): all a_s>=0, sum a_s<=L}. For each declared pair (H,u), read ONLY the nonblocking Boolean observation B(H,u;r)=1_{r*u<=H}. All legal labelled words remain identifiable; their branching and reachability are independent of r. A finite nonadaptive protocol P is any finite family of such tests, in particular the union of complete future word trees for finitely many (H,L).

## Theorem A: exact prime-cut rank
For each test set b=floor(H/u). If there is a prime p with p0<=p<=b, define d(H,u)=largest such prime; otherwise drop this constant-false test. Let D(P) be the distinct finite set of such prime cutpoints. Then the EXACT minimum sufficient quotient for all declared Boolean readings and labelled word trees is
 K_P(r)=#{d in D(P): d<r},
 C(P)=1+|D(P)|,
 minimum fixed-length bits=ceil(log2(1+|D(P)|)).
Proof: On the prime population r*u<=H iff r<=d(H,u); every observation is a nested cut of the ordered prime domain. If D={d1<...<dk}, there are k+1 realized intervals, and each adjacent pair is separated by an actually declared observation. Word identities/multiplicity do not add r-dependent information. For d=|S|, m complete trees of depths <=L give C(P)<=1+m*binom(L+d,d).

## Theorem B: EXACT protocol migration criterion
There exists a deterministic lossless decoder from the full Q observer state to all readings of P iff D(P) subset of D(Q).
In particular C(P union Q)-C(Q)=|D(P) minus D(Q)| exactly.
Proof: inclusion gives partition refinement; otherwise pick missing cutoff d in P but not Q and adjacent primes d and nextprime(d). These yield identical Q readings yet differ in P at cutoff d.

## Explicit structural residual / repair
S={2,3}, L=2, U={1,2,3,4,6,9}:
 D(H=27)={5,7,13,23}: C=5, 3 bits.
 D(H=28)={7,13,23}: C=4, 2 bits.
 D(H in {27,28})={5,7,13,23}: C=5, 3 bits.
Prime seeds r=5 and r=7 have F(28,2)=4 both, but F(27,2)=4 and 3 respectively. Therefore H=28 does NOT safely replace H=27, despite its greater numerical threshold. The single repair bit epsilon_5(r)=1_{4*r<=27}=1_{r<=5} alongside F(28,2) is sufficient for both observers, and one additional bit is necessary because joint classes increase from 4 to 5. This is an observer-dependent Boolean loss, NOT a claimed energy/force/X6 physical residual.

## Theorem C: adaptive conditional observation
Let a finite deterministic policy tree choose legal operations and threshold tests based on prior Boolean readouts, and preserve its actual transcript. Feasible prime seeds at every reachable policy node form a contiguous interval in the ordered prime set, by induction under comparisons r<=d. A test cutoff d is EFFECTIVE only if that node's current reachable interval has seeds on both sides. Prune unreachable branches. Every effective comparison splits one reachable interval in two, and a fixed prime cutpoint d cannot be effective in two disjoint feasible intervals. Hence
 C(policy)=1+number_of_distinct_effective_cuts.
All potential tests read as though nonadaptive give an upper bound, not necessarily equality.

Counterexample: test r<=7 at root; if true then multiply by 4 and test 4*r<=92, else stop. Potential raw cutpoints are {7,23}, predicting 3 classes if incorrectly unioned. But the second test runs only on r=5,7 and is always true. Actual transcripts: (true,true) and (false,stop); effective cuts={7}; C=2. Conditional reachability is part of the BRC future-observer safety certificate.

## Exact verification performed locally (not claimed to run in EM native host)
- 505 singleton (H,L) plans, H=0..100, L=0..4.
- 8320 two-threshold plans, H=0..64, L=0..3.
- 97 labelled legal-word tree comparisons.
- 1503 paired plan migration checks independently comparing actual decoding fibers: 222 safe, 1281 unsafe; all match D-inclusion.
- 1200 finite randomized adaptive policy trees, direct prime-domain interpreter vs independent interval-pruning evaluator, 0 mismatches; 851 include unrealizable potential cuts.
- Exact integer arithmetic and no numerical approximation; proof above establishes general validity, not extrapolation from finite tests.
- Full local evidence supplied in conversation artifact EM_R1_BRC_PrimeCut_Rank_20261011.zip, comprising detailed report, two Python verifiers, JSON certificates, logs and SHA256SUMS. This GitHub note is the portable mathematical statement, not a claim that those local files have been independently received in Source.

## Registration/ownership and next unit
The authenticated native MCP identity was read-only: em_session_start actually rejected with STATIC_READONLY_SCOPE_DENIED. Read-only inventory had 395 tasks (one LEASED), but no authorization or winning CLAiM for this self-directed auxiliary line. Do not borrow another owner or infer a Researcher-ID from GitHub login. This branch note is only draft evidence, not formal Source Result/Review.
Next: extend the effective-cut theorem to finite policies whose action legality and future observers depend on hidden composite/joint/path state. Construct a smallest counterexample to scalar prime-cut rank sufficiency; provide an explicit typed BRC repair coordinate and observer/future-operation descent certificate. Any native-X6 claim requires a separate embedding/readout/operation-preservation proof.
