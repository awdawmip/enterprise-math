# R737 — X6 signed-loop cubic closing-depth recovery theorem

Date 2026-11-12 Asia/Shanghai. Parent task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen scientific Source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior verified coordinate carrier: R735, PR #2132, commit 02b267dee700df3f562b4ccaa21db9de29f09b1f. Parallel R736 PR #2134 studies S3 ledger holonomy rather than this cubic-coordinate observer.

## Object, observer, question

Choose any three distinct native axes of the six-axis X6 Cell torsor, relabeled 0,1,2 only for local computation. W is the 720 ordered permutations of the six signed primitive steps (+0,-0,+1,-1,+2,-2), each used exactly once; NB is the 240 words with no adjacent inverse pair. All six native axes remain in the ambient space. Each word starts and ends at the same selected Cell. This is a finite *coordinate path* N-BRC carrier, not a force equilibrium event.

Write d_t for the signed unit step and x(t)=sum_{r<=t}d_r, x(0)=0. For i<j, R735's integer circulation is J_ij=sum_t x_i(t-1)d_{t,j}; Q_i is the sign of axis i's first step. R735 proved (Q,J) has 192 fibers on NB: 144 singleton and 48 double. We seek an explicit S6-covariant observation of the missing history, rather than an arbitrary fixed-chart one-bit codebook.

Define the strict ordered cubic tensor T_ijk=sum_{r<s<t}d_{r,i}d_{s,j}d_{t,k}. If s_i denotes the index of the second occurrence of axis i, define the *closing cross-depth* K_i=sum_{j in A\{i}}x_j(s_i).

**Lemma 1 (exact tensor identity).** For every w in W and every active axis i,
K_i = sum_{j in A\{i}} T_iij.
Proof: exactly two steps use axis i; they have opposite signs and product -1. Consequently T_iij=-sum_{t>s_i}d_{t,j}=sum_{t<=s_i}d_{t,j}=x_j(s_i), by the zero net j displacement. Sum over j.

**Lemma 2 (X6 covariance).** For a native axis permutation g in S6, Q_{g(i)}(gw)=Q_i(w), K_{g(i)}(gw)=K_i(w), and the two-index circulation J transforms antisymmetrically. These follow by termwise relabeling of the signed path and relative positions. Cell-anchor translation leaves all three objects invariant. The 3D display is a restriction to three selected X6 axes; it is not a separate native world or a native plane.

## Theorem (complete finite census, with exact checker)

For every chosen triple of X6 native axes, (Q,J,K) is injective on NB. The full 27-component ordered cubic T *by itself* is also injective on NB. For a fixed pair of active axes, (Q,J,K_i,K_j) is injective; any single fixed K_i leaves exactly sixteen double fibers. The results over NB are:

| Observation | Classes | Singleton | Double | Maximum fiber |
| --- | ---: | ---: | ---: | ---: |
| (Q,J) | 192 | 144 | 48 | 2 |
| (Q,J,K_i) | 224 | 208 | 16 | 2 |
| (Q,J,K_i,K_j), i≠j | 240 | 240 | 0 | 1 |
| (Q,J,K) | 240 | 240 | 0 | 1 |
| (J,K) | 228 | 216 | 12 | 2 |
| full cubic T | 240 | 240 | 0 | 1 |

**Complete proof for the finite domain.** The attached checker builds *all* permutations of six different signed tokens by recursively removing each remaining token. It checks adjacent inverse pairs to obtain precisely NB; it calculates every observable by exact integer additions/products and groups complete integer tuples, asserting each row above and the equality K_i=sum_{j ne i}T_iij for all 720 words. It checks every choice of one/two K components. Every input in the defined finite population is covered, so the collision and injectivity claims for this finite domain follow. A separate Python itertools.permutations implementation independently obtained the same numbers. Lemma 2 transports this one-triple result to all 20 choices of native X6 triples.

**R735 collision repaired.** wA=(+0,+1,+2,-0,-2,-1), wB=(+0,+2,+1,-0,-1,-2) have equal Q=(+,+,+) and J=(1,1,0), yet K(wA)=(2,0,1) and K(wB)=(2,1,0).

**Further classification.** Over all 720 words, T has 379 values with classes: 240 singletons, 96 doubles, 24 quadruples, 18 eightfolds, and one 48-fold fiber. Every singleton word is in NB, and every NB word is a singleton. The fully alternating cubic contraction Omega=sum_{pi in S3}sgn(pi)T_{pi(0),pi(1),pi(2)} is zero on all 720 words, showing that the repeated-axis third-order interaction contains information unavailable to that alternating scalar.

## BRC and operational scope

Population: 240 signed ordered X6 primitive paths (one N-BRC branch per word). The branch path, signs and order are distinct from positive branch weight and from any signed physical force amplitude. Observation: (Q,J,K); allowed future operation: any deterministic operation that consumes the decoded original word in this declared finite carrier. The observer is injective, so its decoding is exact for that declared scope. K provides a natural S6-covariant three-integer repair, whereas the R735 one-bit chart decoder needs an arbitrary double-fiber index. The simple K update records a coordinate at the closing step of each axis and uses one pass. No general computational complexity improvement for BRC enumeration is claimed.

Checker: node research_notes/R737_X6_CLOSING_DEPTH_VERIFY.js. Evidence: research_notes/R737_X6_CLOSING_DEPTH_RESULTS.json. Assertion: R737_X6_CLOSING_DEPTH_CUBIC_EXACT_PASS. In addition to the complete 720-case census, the verifier uses two independent K evaluations and 3,600 genuine X6 S6-transport tests (five paths × 720 permutations).

Current control continuation observed HANDOFF_READY / NEEDS_DISPATCH, owner taskbook/unassigned, persisted predecessor checkpoint NOT_FOUND, typed continuation route, publication TP2-8B7E13C5904A2D6F1142. This session's native session_start attempt failed with SESSION_ISSUANCE_QUOTA. The work is an author-side mathematical record, not a winning CLAIM, formally frozen Source Result or independent Driver review.

**Next unit:** obtain a Source-backed legal triad Cell/Link/Port event with three signed sources and actual TRIADIC_CLOSURE_E, then exact V29 PASS/V39 j updates. Apply both R735 collision paths to that event, test whether V39 distinguishes them, and isolate the smallest event-level residual. A candidate coordinate J must be connected to real V39 j by a proved event map rather than a naming analogy.