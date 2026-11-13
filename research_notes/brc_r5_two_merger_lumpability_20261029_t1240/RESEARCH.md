# R5 | Simultaneous P/Q Markovization for interacting LR mergers

2026-10-29, 12:41-12:55 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is author-side portable mathematical research, not an authenticated Source CLAIM, formal Result, independent Driver review, or native Heartbeat-X6 theorem.

## Frozen source pins

- GLOBAL_KNOWLEDGE_V1, `awdawmip/chatgpt-global-knowledge`, verified main `fb864596df6963efc37330cf3781eb0f15baf2c8`: read global bootstrap/manual, EM TASK route, P000 exact original and matching P000_STARTUP projection, ACTIVE worldview, applicable BRC/math/code/research activity rules.
- Enterprise Math `awdawmip/enterprise-math`, verified main `c7c8b0ea6797e9a549073d0babe7ec67e78cb893`: AGENTS, P000, ACTIVE Heartbeat-X6 and observer preservation, current control authority, portable research/autonomous operations.
- Previous R5 Draft PR #1663 at `f5374e55f265113acb0c784b696778d0e6c1996d`: tagged-parallel no-cancellation certificate. Here we study a *different* class of serially interacting LR mergers.
- Native service 0.6.11 read-only snapshot: `research_authority_granted=false`, source control `CODE_REVIEW_REQUIRED`, job quota 5/5. Current Source Owner/CLAIM was not authenticated. Neutral GitHub author storage grants none.

## Exact scope and hypothesis

Fix finite observable histories h, clock t=1,...,H, strictly positive normalized laws P and Q, and current likelihood ratio r(h)=P(h)/Q(h)>0. The controller can stop and declare P, stop and declare Q, or continue; time H forces a declaration. Every local behavioral randomization is fresh (NO persistent correlated random seed). FULL policies see h; LR policies see only key k=(t,r). The information key cannot be visited twice on one trajectory, as the clock increases. Observers are

O=(eP,eQ,TP,TQ)=(P(declare Q),Q(declare P),E_P[t_stop],E_Q[t_stop]).

**Predictive lumpability hypothesis.** At each alive k, *every* full history h with that k induces the same Q conditional distribution K_Q(k,k') over next LR keys k' after a continue action. Additionally, K_P(k,k')=(r'/r)K_Q(k,k'), with sum K_Q=1 and sum r'K_Q=r. Immediate declaration outcomes and costs depend only on (k,action). For multiple continue actions, impose this condition action-wise. This is a property of the future key *pushforward*, not necessarily of full hidden path kernels.

## Theorem (all real behavioral policies; actual images)

Under predictive lumpability, for every FULL behavioral strategy there exists a **single genuine seedless LR behavioral strategy** matching exactly all Q and P (time,LR,action) occupancies, all terminal (time,LR,declaration) distributions under both laws and the four observers. Consequently

O_FULL = O_LR

as *actual images*, and that common image is a **compact convex polytope**, not merely a set with an equal convex hull. The result permits any finite number of serial interacting LR collisions.

**Complete proof.** At each alive full history h let z_Q(h) be its Q reachability mass. Identical policy action probabilities under P and Q cancel from their path likelihood ratio, so z_P(h)=r(h)z_Q(h). Define the aggregated Q key masses and action flows

m_k = sum_{h:key(h)=k} z_Q(h),   f_(k,a) = sum_{h:key(h)=k} z_Q(h)*pi(a|h).

All f are nonnegative and sum_a f_(k,a)=m_k. Define pi_LR(a|k)=f_(k,a)/m_k if m_k>0, choosing an arbitrary legal distribution for m_k=0. Its current Q action flow equals FULL's f_(k,a), while its P flow equals r f_(k,a), matching FULL simultaneously for both laws. At next time, predictive lumpability gives Q inflow to k':

m_(k') = b_(k') + sum_k f_(k,continue)*K_Q(k,k').

Thus LR has the same next key occupancy, and induction over the finite increasing clock gives identical P and Q action flows at every key. Terminal Q flows are f_(k,declare P/Q) and terminal P flows are r f_(k,declare P/Q); summing those proves the terminal laws and four coordinates equal. Zero-mass information keys contribute no flow, so the arbitrary boundary choice is valid. This is *one* seedless behavior policy, not a persistent mixture of deterministic strategies. LR belongs to FULL, giving both inclusions.

For convexity introduce nonnegative real Q-flow variables m_k, f_(k,a) with the **linear** constraints:

m_k = b_k + sum_j f_(j,continue)*K_Q(j,k), sum_a f_(k,a)=m_k,
f_(k,continue)=0 on terminal keys.

The finite time-acyclic flow system is bounded and nonempty. Every feasible flow conversely is realized by the single LR policy f_(k,a)/m_k at positive mass, with arbitrary legal zero-mass choices. The observer map is the **linear projection**

eP=sum_(t,r) r*f_((t,r),declareQ);
eQ=sum_(t,r) f_((t,r),declareP);
TP=sum_(t,r) t*r*(f_((t,r),declareP)+f_((t,r),declareQ));
TQ=sum_(t,r) t*(f_((t,r),declareP)+f_((t,r),declareQ)).

A bounded linear-flow polytope has a compact convex polyhedral linear image. QED.

**Kill criterion:** the mother target requires equal convex hulls and UNEQUAL actual O sets. This sufficient lumpability class, however many interacting mergers it has, cannot yield such a counterexample. This does not claim all non-lumpable models have unequal images, or that source residual can be erased for arbitrary other observers.

## Fully rational strictly positive serial two-merger example

At t=1 FULL sees origin o=A/B, each with unconditional P=Q=1/2; both share LR r=1. At t=1,2,3 continuing draws independent multiplier s in {1/2,1,3/2} with strict positive conditional Q row K_Q=(1/4,1/2,1/4) and conditional P row K_P=(1/8,1/2,3/8)=s*K_Q. Both rows normalize, and sum_s s*K_Q(s)=1. LR then becomes r'=r*s. At t=4 one must declare.

Two nonterminal LR mergers are (1,1), merging origins A/B, and (3,3/4), merging distinct positive incoming histories (s=1/2,u=3/2) and (s=3/2,u=1/2). The earlier continue choice changes whether the latter is reached: they are serially **interacting**, not tagged-parallel independent components.

FULL witness: at t1 continue only origin A; stop/declare P at B. At t2 stop/declare Q if first multiplier s=1, otherwise continue. At t3 for r=3/4 stop/declare Q if first multiplier s=1/2 but continue if s=3/2; otherwise declare P if r>=1, Q if r<1. At t4 declare P if r>=1, Q otherwise.

Exact full observer:
O_FULL=(335/1024,77/128,227/128,57/32).
At key (3,3/4) Q occupancy=1/16; the two distinct histories supply 1/32 each. Its Q (stopP,stopQ,continue) flows=(0,1/32,1/32), so the seedless LR strategy uses (0,1/2,1/2) at that key. At first merger (1,1) LR uses (1/2,0,1/2). The Markovized policy gives exactly the same four-vector and entire terminal P/Q histogram. It is a constructive demonstration that source/path differences can be erased SAFELY for this particular future observer scope.

## Executed exact verification, scope and literature

The published `VERIFY.py` is the **actually executed** Python standard-library `fractions.Fraction` verifier; its `EXACT_OUTPUT.txt` is its actual stdout. It checks normalization, LR moment, 2 positive incoming sources of the second collision, Q and P occupancy and action flows, all terminal histograms and four errors/time values. It also compares 240 additional independently seeded rational FULL behavioral policies to their exactly constructed seedless LR conversions. Output ends `PASS_EXACT_R5_SERIAL_INTERACTING_MERGER_LR_MARKOVIZATION`. These 240 checks are FINITE regression; the theorem's universal all-real scope follows from the algebraic proof above.

Prior-art mathematical context, not originality claim: R. Laroche and R. Tachet des Combes, *On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs*, ICML 2023, PMLR 202:18548-18562, https://proceedings.mlr.press/v202/laroche23a.html. Classical single-law Markovization motivates the present two-law likelihood-ratio-matched application. No native X6 correspondence, physical result or worldwide novelty is asserted.

BRC state holds origin/path identity, time and strictly positive P/Q mass UNTIL the *declared* next-key kernel, both-law ratio relation, and terminal observer factorization prove this specific quotient safe. Source-sensitive future kernels remain genuine structural residuals; P000 and ACTIVE worldview unchanged.

**Next unit:** construct a non-lumpable interacting two-merger finite rational model; enumerate every FULL and LR deterministic four-vector, certify ALL signed convex hull directions via rational convex combinations of ≤5 LR vertices per FULL vertex or rational Farkas separator. Only for a model that passes the exact hull-equality filter, attempt a complete real semialgebraic four-observer nonmembership proof. Preserve Source owner, independent review and proper admission.
