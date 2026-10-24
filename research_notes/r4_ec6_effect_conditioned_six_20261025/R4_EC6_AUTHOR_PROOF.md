# R4-EC6 — Exact six observed states with effect-conditioned BRC transfer

2026-10-25 (Asia/Shanghai). Author-side mathematical proof / exact computations. NOT formally admitted or independently reviewed.

## Frozen sources and authority

GLOBAL_KNOWLEDGE_V1 main@74fdc5c633aa854383ed50a76a72ec6c186c793a (00_BOOTSTRAP, OPERATING_MANUAL, P000 startup and ACTIVE worldview). Enterprise Math Source main@75d9a5fe322ca7efe0ee4358a63d7cefcd0d9660 (AGENTS, native X6, observer preservation, docs/PORTABLE_RESEARCH_PROTOCOL.md). R274 support-frontier lemma: research_notes/r274_affine_support_frontier_20261025/R274_BRC_AFFINE_SUPPORT_FRONTIER_20261025.md at c168d92b0e6333e7318331e3c792b35fefdc8ef2. Parallel R275 clean-q2 positive-cone result read at fa8a1dacd1c854b70f4a4a81f09107a919f18a71; different and not subsumed.

Authenticated GitHub identity awdawmip. Native em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false: no native Researcher identity, owner verification, CLAIM, Result or Driver acceptance. This is a research-draft branch only.

This is a declared positive-weight formal BRC model embedded as a restricted formal observer on native X6, NOT an independently established six-dimensional native propagation law. The affine pair acts on (z1,z2,z3,z4,z5,z6) as (eps*z1+k,eps*z2,z3,z4,z5,z6). Six native dimensions remain intact, and formal operation depth n is not calibrated physical time. Native R193 source/time ports remain unchecked. P000 remains ACTIVE_LOCKED.

## Exact source model

A length-n binary word begins at q=0, provenance r=0, effect g=(eps,k)=(+1,0). Each binary edge has integer weight 1. Its table of (q',eta,b) is:

q=0: input0 (2,-1,-1); input1 (2,+1,-1)
q=1: input0 (0,-1,-1); input1 (0,+1,-1)
q=2: input0 (1,+1,+1); input1 (2,+1,-1)

Update g -> (eta*eps, eta*k+b); composition respects the actual chronological order. The monitor r is 0 if "00" absent and last bit is 1 (or start), 1 if "00" absent and last bit is 0, 2 if "00" has appeared. On bit 0, r=(0,1,2) -> (1,2,2); on bit 1 -> (0,0,2). Let P_n(q,r,g) be exact word counts and h=1_{r=2}. The joint observed histogram is C_n(q,h,g)=sum_{r:1_{r=2}=h}P_n(q,r,g). There are precisely six possible observed (q,h) labels.

## Theorem A — six labels suffice when the transfer itself can inspect effect and time

Define theta_n(q,g)=P_n(q,1,g)/[P_n(q,0,g)+P_n(q,1,g)] for an occupied nonhit fiber, and theta=0 otherwise. Consider six aggregate control labels (q,h), with their complete effect grade g. At step n apply the original (q,bit)-specific affine effect and next control q'. On h=1, both bit edges preserve h=1 with weight 1. On h=0, bit 1 keeps h=0 with weight 1. On h=0, bit 0 is replaced by two parallel, identically affine-labelled edges: next h=0 with weight 1-theta_n(q,g), next h=1 with weight theta_n(q,g). Omit zero-weight edges.

From initial mass 1 at (q,h,g)=(0,0,+1,0), this gives EXACTLY C_n(q,h,g) at all finite n, preserving all six joint output channels, all affine grades, positive-rational edge weights, and integer path totals 2^n.

Proof: induction on n. An occupied nonhit grade contains mass N=P_n(q,0,g)+P_n(q,1,g). The bit-0 mass routed to newly hit is N*theta=P_n(q,1,g), exactly those original words whose last bit was zero. The mass routed to remaining nonhit is N*(1-theta)=P_n(q,0,g), exactly those originally r=0. Both receive the same q' and effect because the original edge depends on q and bit, not r. Under bit 1, both nonhit r values go to r=0, so their masses merge exactly. An already-hit r=2 is absorbing and its two original edges are copied. The initial histograms coincide. Thus the entire joint histogram recurs identically. Any surviving rational edge weight is strictly positive. QED.

IMPORTANT: these coefficients require an external time/effect-conditioned schedule derived from the original seven-state distribution. This is an initial-law-specific oracle-conditioned transfer, NOT a uniform finite-state BRC realization, not an online memory-free exact quotient, and not a solution to the effect-blind-transition open problem. A full cost model must charge for generation/storage of the theta schedule.

## Theorem B — minimality 6 in this enlarged conditioned-kernel class

At depth n=7, same complete affine effect g=(+1,-3), the six strictly positive channel counts, ordered by (q,h), are:
(0,0):2; (0,1):2; (1,0):3; (1,1):1; (2,0):1; (2,1):9.

A single internal label at a fixed n,g has only one observed (q,h) under an arbitrary deterministic decoder D(label,n,g). Therefore d labels can support at most d observed channels on that fiber; d>=6. Theorem A attains d=6 if transitions may be effect/time-conditioned using externally supplied rational coefficients. Thus d_min=6 in THIS enlarged class only. QED.

## Theorem C — exact growing family of genuinely mixed transfer grades

R274 proved exact step-two support intervals for every n>=10 and either effect sign. At q=2, the two nonhit provenance states have supports:
r=0: k=-n,-n+2,...,n-6;
r=1: k=8-n,10-n,...,n-4.

Their intersection is k=8-n,10-n,...,n-6, containing exactly n-6 entries per effect sign. Each such entry has both original counts strictly positive, hence 0<theta_n(2,eps,k)<1 at exactly 2(n-6) effect grades at every n>=10. Of the other occupied q2 nonhit grades, theta=0 exactly at k=-n,-n+2,-n+4,-n+6 (each sign; 8 grades total), and theta=1 exactly at k=n-4 (each sign; 2 grades). The union has 2(n-1) occupied grades.

Proof: Positivity and completeness of the two R274 support intervals show the overlap precisely. Its cardinality per sign is [(n-6)-(8-n)]/2+1=n-6. The two difference sets consist of the four lower and one upper boundary sites just listed. No others occur. The R274 interval theorem follows from exhaustive n=10 base and positive incoming-interval induction. QED.

This counts active addresses requiring mixing in the specific quotient; it does NOT imply independent coefficient-bit lower bounds. There may be a compact formula.

## Theorem D — natural six-label quotient cannot be effect-blind even when time dependent

Suppose the same six literal labels (q,h) and same bit-specific q/affine edges are used, but the split coefficient on bit 0 depends only on n,q,h, NOT accumulated g. At n=1, words 0 and 1 both have (q,h)=(2,0), yet their effects are g=(-1,-1) and g=(+1,-1), with last-bit monitors r=1 and r=0 respectively. Appending bit 0 gives word 00 -> (q,h,g)=(1,1,-1,0), while word 10 -> (1,0,+1,0). No other input bit feeds q'=1 at n=2. Since path weights are nonnegative and unwanted masses are exactly zero, the split must equal 1 on g=(-1,-1) and 0 on g=(+1,-1). A grade-blind coefficient is identical across these two fibers, impossible. QED.

This excludes only the literal output-labelled Markov quotient; arbitrary differently encoded six-control models remain OPEN.

At n=7, the still-clean (q=2,g=(-1,+1)) fiber has P(q,r=0)=P(q,r=1)=1, so theta=1/2: this is not just a deterministic effect-based last-bit reconstruction.

## Executed validation and limits

Python exact integer/Fraction reference and constructed six-label transfer match at every n=0..90. Independent exhaustive original-word enumeration through n=11 checks the Python reference. Independent C++17 boost::multiprecision integer recursion checks n=0..40, exhaustive words through n=12, the n=7 six-channel counts, and the exact 2(n-6) mixed-grade count n=10..40. All passed, no floating-point arithmetic. Infinite claims follow the proofs, not finite extrapolation.

Existing typed BRC positive histogram + affine serial law + observer/fiber support: REUSE_APPLIED; native enterprise_math ControlPacket/EffectHistogram: NOT_RUN. No R193 native provenance/time, Lean proof, empirical P000 or independent Driver acceptance.

## Next discriminating research problem

For effect-BLIND positive-rational transitions (possibly n-dependent but not g-dependent) and an arbitrary deterministic terminal decoder D(state,n,g), settle six versus seven internal control states for all finite depths, either via a lawful six-state construction with an exact induction or a no-go covering ALL possible internal encodings. Theorem D handles only the literal output-labelled quotient. Distinguish transition-grade access from decoder-grade access and price any external coefficient oracle. Preserve the separate native R193 and X6 validation residue.
