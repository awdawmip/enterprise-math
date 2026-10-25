# C311 — Five-point composite evaluation and coefficient certificates close the 19-path content gap
Date: 2026-10-26. Research status: AUTHOR_EXACT, NOT_ADMITTED. This is integer-polynomial auxiliary-scalar algebra, not a native X6 / BRC heartbeat evolution theorem.

## Frozen authority and mathematical scope
GLOBAL_KNOWLEDGE_V1 main@71ccd50fc2ff4bc40339d3c033b4d34f7af10ff1; 00_BOOTSTRAP, OPERATING_MANUAL, P000_STARTUP and its matching canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview. Enterprise Math source initially main@658e1f3e8d592d635dfae1751b42d0d6ccbca598, publication branch based on latest source main@7f1913a4940bb97898f1c9c4e4cf542db3221eee. Research transport conforms to docs/PORTABLE_RESEARCH_PROTOCOL.md and research_persistence_policy.json.

Researcher uses frozen C293 path records (SHA256 03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89) and C305/C310 source code contained in the prior portable handoff. The C300 cancellation and C305 model factorization remain upstream **author-level assumptions**, not independently audited in this run. No original 79-branch input provenance, signed phase, port, or future-operation residual is erased by scalar projection.

## The exact target
Take integers s>=1, integral polynomials P,C,J_1,...,J_m with primitive C and exact identity C(t)P(t)=sum_a J_a(t). Define L=gcd(s,content(J_1),...,content(J_m)), M=s/L, and R=sum_a J_a/L. By Gauss content multiplicativity, P/L and R are integral polynomials and gcd(s,content(P))=L*gcd(M,content(R)). Here "content" is the nonnegative gcd of all coefficients, including content(0)=0.

C310 showed 19 exceptional instances where the common source terms cancel identically modulo p (p=2 in 15 cases and p=3 in 4), and R has some nonzero coefficient modulo p^2. It did **not** independently exclude other primes from the final gcd.

## C311-A — sampled composite modulus shrinks the prime-support obligation
For any R in Z[t], M>=1 and integer nodes t_0,...,t_h, define H=gcd(M,R(t_0),...,R(t_h)). Then D=gcd(M,content(R)) divides H. Proof: content(R) divides R(t) at every integer t, and consequently D divides every argument defining H. QED.

The converse is false. For R=t(t-1), M=2, every integer R(t) is even but content(R)=1. Thus sampling alone never certifies coefficient content.

## C311-B — complete prime-support coefficient certificate
Suppose H has a **complete verified prime factorization**, p is one of its primes, and:
(1) all coefficients of R vanish modulo p;
(2) at least one coefficient of R is nonzero modulo p^2;
(3) for every other prime q|H, at least one coefficient of R is nonzero modulo q.
Then gcd(M,content(R))=p. Proof: D divides H by C311-A. Conditions (1) and p|H|M give p|D. Condition (2) forces v_p(D)=1. Condition (3) removes every other prime divisor of H. QED. In the setting above gcd(s,content(P))=L*p.

No factorization of the much larger M is necessary; only H is factored. This is an elementary algorithmic certificate, not an originality claim about classical integer polynomial content.

## Reproducible 19-path exhaustive certificate
Input: the 19 exceptional C293 paths [3,6,7,8,11,12,17,26,27,29,30,33,34,38,56,75,76,97,108] with 79 labeled branches. Build the 79 integer numerator term products from frozen C305 and divide each scalar coefficient exactly by the prior structural bound L. For each t in {0,1,2,3,4}, evaluate every factor by integer Horner and multiply modulo M, summing branch terms to yield R(t) mod M. Taking gcd with M gives exactly H, because gcd(M,n)=gcd(M,n mod M). Fully factor H by exact trial division. For each q|H, use the C310 full factorized polynomial convolution to test R coefficientwise modulo q; for p also test R modulo p^2. Keep a concrete nonzero coefficient (degree,residue) witness for every successful exclusion. The main run executed all 19, all 5 samples, every identified prime and p^2, and a separate standard-library truncated-convolution program verified 22 selected coefficient witnesses (19 low-degree, 3 high-degree).

| i | p | bits(M) | bits(H) | support primes checked | complete H factorization |
|---:|---:|---:|---:|---:|---|
| 3 | 3 | 5019 | 87 | 8 | 2^56 *3 *5 *7 *17^2 *23 *31 *53 |
| 6 | 2 | 4954 | 62 | 8 | 2^13 *3 *5^8 *7 *17 *31 *41^2 *53 |
| 7 | 2 | 4881 | 43 | 7 | 2^8 *5^6 *7 *13 *17 *23 *53 |
| 8 | 3 | 5030 | 65 | 10 | 2^16 *3 *5 *7 *17 *23 *31 *43^3 *53 *61 |
| 11 | 2 | 4699 | 45 | 9 | 2^8 *3 *5 *7 *11^2 *13^2 *17 *37 *61 |
| 12 | 2 | 4923 | 53 | 9 | 2^8 *7^4 *11 *13 *17 *37 *41 *53 *61 |
| 17 | 2 | 4878 | 43 | 8 | 2^8 *5 *7 *11^2 *13^2 *17 *37 *61 |
| 26 | 2 | 4961 | 56 | 10 | 2^16 *3 *5 *7 *11 *17 *41 *53 *61 *239 |
| 27 | 2 | 5001 | 56 | 10 | 2^13 *5 *7 *11 *17 *23 *41 *53 *61 *239 |
| 29 | 2 | 4948 | 58 | 8 | 2^14 *5^6 *7^2 *11 *17 *37 *53 *61 |
| 30 | 2 | 4964 | 83 | 10 | 2^18 *3^9 *5^8 *7 *11 *17 *23 *37 *53 *61 |
| 33 | 2 | 4946 | 57 | 8 | 2^13 *5^7 *7 *11 *17 *37 *53 *61 |
| 34 | 2 | 4957 | 62 | 8 | 2^13 *5^7 *7 *11^2 *13^2 *17 *37 *61 |
| 38 | 3 | 5043 | 45 | 8 | 2^14 *3 *5 *7^2 *17 *41 *53 *61 |
| 56 | 3 | 5012 | 80 | 8 | 2^51 *3 *7 *11 *17 *37 *53 *61 |
| 75 | 2 | 4979 | 41 | 8 | 2^13 *3^3 *5 *7 *11 *17 *23 *61 |
| 76 | 2 | 4980 | 42 | 8 | 2^13 *5 *7 *11 *17 *23 *53 *61 |
| 97 | 2 | 4703 | 54 | 9 | 2^8 *5 *7 *11^2 *13^2 *17 *37 *41^2 *61 |
| 108 | 2 | 4955 | 65 | 8 | 2^14 *3 *5^6 *7^2 *17^2 *29 *37^2 *61 |

19/19 complete candidates satisfied theorem C311-B. Totals: 95 exact modular integer evaluations and 162 complete mod-q polynomial coefficient checks. H is 41–87 bits even though M is 4699–5043 bits. The resulting gcd(s,content(P))=L*p independently matches the historical C309/C306 oracle, but the oracle did not choose the answer in this certificate. The full 19-path JSON contains the five decimal residues, H, every factor exponent and all coefficient witness degrees/residues; it is included in the portable handoff ZIP.

Local replay: C311_COMPOSITE_EVAL_PRIME_FILTER.py prints C311_ALL_19_EXACT_PROOFS_PASS; NUMBER_OF_PRIME_CHECKS 162; C311_INDEPENDENT_COEFFICIENT_CROSSCHECK.py prints C311_INDEPENDENT_22_WITNESSES_PASS. C311_COMPOSITE_FILTER_REFERENCE.py is the smaller core recomputation; it prints C311_ALL_19_PASS / 95_SAMPLES / 162_COEFFICIENT_CHECKS when placed beside the frozen C305/C310 inputs. No floating point, finite sampling inference or C306 target oracle is used.

## BRC, provenance, independent review and next problem
Reuse state COMPOSE_APPLIED/REUSE_EXECUTED: C305/C310 79-branch factorized kernels under the coefficient-content observer. This arithmetic concerns projected signed integer coefficients, not positive BRC mass or native phase-aware transport. It does not assert a native X6 theorem, physical heartbeat dynamics, independent source verification of C300, or accepted formal result.

The connected GitHub login was awdawmip and repository write was allowed. Direct native EM gateway returned em_control_tasks=CONTROL_QUOTA and em_session_start=STATIC_READONLY_SCOPE_DENIED with operation_sent=false; native active owner was not confirmed, so no TASK CLAIM, Source Result, Driver review or Foundation promotion is asserted. Private GitHub control bridge request status succeeded but its new dispatch request timed out; that is not NO_DISPATCH. This author artifact is a research-branch checkpoint, not a canonical task publication.

Next C312: independently audit C300's two exactly cancelled linear factors and C305's 79-branch construction directly against the frozen original rational expression; then study minimal sample-node optimization and deterministic bounds for composite evaluation filters without inferring universality from 19 observed successes.