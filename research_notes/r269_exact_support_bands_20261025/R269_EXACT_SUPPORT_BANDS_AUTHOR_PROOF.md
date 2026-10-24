# R269 | Exact support bands of affine BRC and linearly many saturated effect fibers

2026-10-25 | AUTHOR-SIDE MATHEMATICAL PROOF, EXACT FINITE CHECK, NOT NATIVE ADMITTED

Pinned global knowledge: main@a4331e69229a9558cc5d43300abb842a2d65e744, P000 ACTIVE_LOCKED canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Enterprise Math prepublication canonical source: main@7c783f61dce5b4442b1b45cbe70e4ab399a653ce. Frozen R268 predecessor: commit aac6b9ae60761cceab87c8dbe5d20432b3406d07 in research_notes/r268_six_output_support_20261025, exact transition source R268_six_output_support.py (Git blob cc0afa4c68e974b70d9ed35d423406c4485a473b).

## 1. Typed model and question

Reuse the *formal*, unit-positive, two-choice BRC, not a validated native X6 heartbeat operator. Let q in {0,1,2}; ordered selector a in {0,1}. Outgoing edges (q',eta,beta) are

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

Provenance detector r tracks presence of substring 00: r=0 (not seen and last symbol not zero), r=1 (not seen and last zero), r=2 (seen). Under a=0,1: r0 -> (1,0), r1 -> (2,0), r2 -> (2,2). Initial state (q,r,epsilon,k)=(0,0,+1,0). The full affine effect g=(epsilon,k), epsilon in {+1,-1}, acts on six *formal* slots as (epsilon*z1+k,epsilon*z2,z3,z4,z5,z6). Chronological composition: (epsilon,k) THEN (eta,beta)=(eta*epsilon,eta*k+beta). Branch weights are positive integers; no cancellation.

There are seven reachable memories
S=((0,0),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2)).
The six terminal output labels are c=(q,h), where h is the Boolean r==2. The cumulative *step count* n is not physical heartbeat time.

R268 established existence of at least one common full-effect fiber with all six terminal outputs for each n>=7, and a universal six-state lower bound for positive aggregate affine representations with single-valued output D(control,n,full_effect). The residual gap 6<=d_min<=7 remains open. New R269 question: classify *all* effect-support bands and count saturated fibers exactly, rather than just finding one witness.

## 2. Exact-band theorem

For state s=(q,r), orientation epsilon and depth n, let K_n(s,epsilon) be the support of integer translations k reached by at least one positive-weight word with that precise (q,r,epsilon,k). Define the parity interval
I_n(a,b)={integer k: k congruent n (mod 2), -n+a <= k <= n+b}.

**Theorem.** For every integer n>=10, each epsilon in {+1,-1} and each s in S, the exact support is K_n(s,epsilon)=I_n(a_s,b_s), independent of epsilon, with these offsets:

| s | a_s | b_s |
|---|---:|---:|
| (0,0) | 2 | -8 |
| (0,2) | 4 | -4 |
| (1,1) | 2 | -6 |
| (1,2) | 4 | -4 |
| (2,0) | 0 | -6 |
| (2,1) | 8 | -4 |
| (2,2) | 2 | -6 |

The claim is exact for *each n*, not merely eventual density and not a claim of equal multiplicities.

### Proof, base

At n=10, enumerate all 2^10=1024 binary selector words. Apply the displayed deterministic q/r rules and affine composition to each word; group the resulting positive paths by (q,r,epsilon,k). For each s and epsilon, the observed translation set equals exactly the interval in the offset table. The full 1024-word enumeration is independently equal to the R268 exact positive-count recurrence at depth 10. Reproducible Python and independent C++17 programs are provided, so this is a finite exhaustive base certificate rather than a sampled assertion.

### Proof, all-depth induction

Assume the seven intervals hold at some n>=10. Under one edge (eta,beta), translation k maps to eta*k+beta. The source I_n(a,b) maps *exactly*, with parity n+1, to I_(n+1)(a',b'), where

eta=+1: (a',b')=(a+beta+1,b+beta-1);
eta=-1: (a',b')=(-b+beta+1,-a+beta-1).

Every beta is odd, hence the parity flips correctly. Since source supports are identical for each orientation, fixing either target epsilon restricts each incoming edge to exactly one source epsilon and leaves all the same interval images.

The following table lists **all** incoming source-edge images, not a sample. Destinations are the seven (q,r) memories and each offset pair is the resulting (a',b').

| Destination | Source/selector -> resulting offset |
|---|---|
| (0,0) | (1,1)/1 -> (2,-8) |
| (0,2) | (1,1)/0 -> (6,-4); (1,2)/0 -> (4,-6); (1,2)/1 -> (4,-6) |
| (1,1) | (2,0)/0 -> (2,-6) |
| (1,2) | (2,1)/0 -> (10,-4); (2,2)/0 -> (4,-6) |
| (2,0) | (0,0)/1 -> (2,-10); (2,0)/1 -> (0,-8); (2,1)/1 -> (8,-6) |
| (2,1) | (0,0)/0 -> (8,-4) |
| (2,2) | (0,2)/0 -> (4,-6); (0,2)/1 -> (4,-6); (2,2)/1 -> (2,-8) |

For each destination the minimum incoming a' is the stated target a_s and the maximum incoming b' is the stated target b_s. At the smallest target n+1=11, the complete incoming parity intervals have a *gap-free union*: it equals I_11(a_s,b_s). This is checked exactly by the 7-row interval union in both verifiers and can also be read from the displayed finite table. Each constituent interval [-N+a',N+b'] grows by one outward at either endpoint when N increases by one. All intervals for a given N have the same parity, and their start/end distances on the parity lattice remain unchanged as N grows. Hence all overlaps or adjacencies present at N=11 persist at all N>=11, and the union continues to fill the whole target parity interval. No extra k can appear because every available edge was included. Thus for both target epsilon signs the entire exact support at depth n+1 equals I_(n+1)(a_s,b_s). Induction completes the universal theorem.

This induction uses positive support and the genuine affine composition. It makes no inference of signed cancellation, amplitudes or native physical dynamics.

## 3. Exact counting corollaries

For depth n, let E_n be the set of all distinct full effects (epsilon,k) with positive total mass. Let F7_n be the subset of effects carrying **each of the seven** distinct internal states in S, and F6_n the subset carrying **each of the six** distinct terminal labels (q,h). From the table and a direct parity-interval union,

E_n={ (epsilon,k):epsilon=+1 or -1, k congruent n (mod 2), -n<=k<=n-4}, so |E_n|=2(n-1).

Intersect all seven internal-state intervals. The greatest lower offset a_s is 8 (state (2,1)); the least upper offset b_s is -8 (state (0,0)). Hence

F7_n={ (epsilon,k):epsilon=+1 or -1, k congruent n (mod 2), 8-n<=k<=n-8}, so **|F7_n|=2(n-7)**.

For six output channels, the only merged no-00 terminal support is (q=2,h=0), which is the union of r=0 and r=1 bands, namely I_n(0,-4). Taking the intersection across all six output channels yields

F6_n={ (epsilon,k):epsilon=+1 or -1, k congruent n (mod 2), 4-n<=k<=n-8}, so **|F6_n|=2(n-5)**.

All three formulas hold exactly for every n>=10. Their differences are independent of depth: |E_n minus F7_n|=12; |E_n minus F6_n|=8; |F6_n minus F7_n|=4. For each orientation, precisely two boundary translations k=4-n and k=6-n support all six outputs but not all seven internal memories.

| n | distinct effects | all-seven fibers | all-six fibers | six-not-seven |
|---:|---:|---:|---:|---:|
| 10 | 18 | 6 | 10 | 4 |
| 11 | 20 | 8 | 12 | 4 |
| 12 | 22 | 10 | 14 | 4 |
| 18 | 34 | 22 | 26 | 4 |
| 32 | 62 | 50 | 54 | 4 |
| 64 | 126 | 114 | 118 | 4 |
| 80 | 158 | 146 | 150 | 4 |

The proportions of distinct effect keys carrying all seven or all six approach one as n grows. This does **not** imply the same for positive-weight path *mass*; support counts and weighted counts are different observables.

## 4. New necessary condition for any six-state aggregate implementation

Fix exactly R268's general comparison class D(d): genuine chronological affine effects, arbitrary positive rational branch masses and multiplicities, optional time-dependent packets, no required word-by-word homomorphism, exact equality of every (output-channel, full-effect) positive histogram, and a single-valued terminal decoder D(internal_state,n,epsilon,k). A given state at a given (n,epsilon,k) can emit only one terminal label, even when its mass is split over many upstream words.

At **each** of the precisely 2n-10 full-effect keys in F6_n, all six distinct labels must have positive mass. If d=6, each of its six internal states must therefore carry strictly positive mass at that effect, and the decoder must be a bijection from those six states to those six labels. This holds for every n>=10. It is a strong family of coupled occupancy constraints, but **not** a proof of impossibility of d=6. In particular it cannot be turned into the fixed-decoder Hankel-rank 7 lower bound from R265/R262 without a new argument controlling the effect- and depth-dependent decoder. Thus the correctly bounded broad problem remains **6<=d_min<=7**.

## 5. Evidence, limitation and next exact problem

The Python exact verifier reuses the unmodified R268 step/forward interface, checks all 1024 words at the n=10 base, all seven incoming interval unions, and all support/count identities through n=80. The independent C++17 checker independently codes the transitions, checks the 1024-word base, symbolic image unions and all identities through n=30. Both executed PASS in the local controlled environment, with exact integer arithmetic. Infinity is proved by the base-plus-induction argument, not extrapolated from finite replay. Full source, JSON evidence and a cold-start recheck are available in the supplied portable ZIP.

Native control read: em_control_tasks -> CONTROL_QUOTA; em_session_start(RESEARCHER) -> STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The connected GitHub identity is awdawmip, but this did not issue a native Researcher session, verify a live owner, create a CLAIM, run native Enterprise Math packages, or produce a formally reviewed Result. Source author branch storage is evidence persistence, not admission. P000 remains ACTIVE_LOCKED, with no unsupported native X6 or R193 transfer.

Next exact unit R270: use cross-depth positive affine mass transport, together with the linearly many fully six-output-saturated fibers, either to construct an **actual** six-control aggregate positive BRC with correct full joint histograms for *every* depth or derive a **non-homomorphic**, effect/time-decoder-compatible obstruction. R193 native source/path/time-port and ControlPacket/EffectHistogram execution are separate pending native-transfer prerequisites.
