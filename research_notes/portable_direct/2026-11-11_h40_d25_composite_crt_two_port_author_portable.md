# D25/LIFT: composite-modulus CRT fragmentation of the finite Clausen ports

Date: 2026-11-11. Status: AUTHOR_EXACT_CRT_PROOF / 2001_CASE_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7. Frozen scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3.
Current exact Source continuation read: h40-20261111-1338-current-d25-source-read, SUCCEEDED as-of 26d62234ebcd7315d918cf047763b09bc0997597, execution_authorized=false. Only portable author-side arithmetic is reported.

## Integral two-port carrier

For integers m>=0, epsilon in {0,1}, N=6m+1+4epsilon>=5, put

    c_k = 2^(m-k) * binom(m,k) * binom(2m+epsilon,k),   0<=k<=m
    U = sum_k c_k
    V = sum_k (1-6epsilon+12k)*c_k.

These are exactly U=2^m A and V=2^m B where A=K_m^(epsilon)(1/2), B=(1-6epsilon)A+6K_m^(epsilon)'(1/2) are the previously studied finite Clausen observation ports. N is odd, so 2^m is invertible modulo N.

## Proved all-integer CRT theorem

For any N=product_i(q_i^a_i), and integers U,V, the product UV is zero mod N if and only if, for every i,

    min(v_qi(U), a_i) + min(v_qi(V), a_i) >= a_i.

A global zero at port U requires v_qi(U)>=a_i for all prime-power components, and likewise for V. This is an exact theorem by prime-power divisibility and CRT. In a composite modulus the product may be zero while both named ports remain nonzero.

Exact constructive examples, all obtained from the original integer sums:

| epsilon | m | N | U mod N | V mod N | local explanation |
|---:|---:|---:|---:|---:|---|
| 1 | 10 | 65 | 26 | 5 | N=5*13; V=0 mod5, U=0 mod13 |
| 0 | 14 | 85 | 68 | 15 | N=5*17; V=0 mod5, U=0 mod17 |
| 0 | 28 | 169 | 39 | 117 | N=13^2; both U,V have exactly one factor 13 |

Indeed 26*5=2*65, 68*15=12*85 and 39*117=27*169. These are counterexamples to the stronger global inference 'UV=0 mod composite N implies U=0 or V=0 mod N'. The third example shows prime-power valuation splitting, not merely CRT splitting across different primes.

## New finite observation; all-index conjecture remains open

Candidate: for all m>=0 and epsilon in {0,1} with N>=5, N divides U*V.

Two independent exact integer algorithms (direct math.comb and binomial-factor recurrence) agree on all 2001 tested cases, 0<=m<=1000 in both branches except (m,epsilon)=(0,0). No product-divisibility failure was found.

| epsilon | cases | prime N | composite N | U zero | V zero | neither port zero but product zero |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1000 | 384 | 616 | 329 | 384 | 287 |
| 1 | 1001 | 397 | 604 | 329 | 385 | 287 |
| total | 2001 | 781 | 1220 | 658 | 769 | 574 |

No case has both ports zero mod N. All 781 prime-indexed cases obey the previously observed m-mod-4 zero-port classification. These are complete finite-range statements, not universal proofs. The CRT theorem above is universal, but it does not prove the all-index candidate.

The exact reproducibility program is d25_composite_crt_two_port_verify_20261111.py in this directory; its output comprises 2001 records of m, epsilon, N, two labeled residues, and product. The local full certificate is d25_composite_crt_two_port_cert_20261111.json, preserved in the portable ZIP alongside this report.

## BRC observation and scientific boundary

Retain each prime-power valuation pair (v_q(U),v_q(V)) along with the scalar UV mod N. Scalar-product observation alone is not a valid quotient for the future operation of determining a named zero port. BRC method: COMPOSE_APPLIED (existing dual-port observer + exact composite CRT/valuation coordinates). The population is the above N-indexed auxiliary arithmetic, not a newly claimed native Heartbeat cell coordinate.

Earlier prime-indexed W_p = 2^(-epsilon)*A*B (mod p) does not automatically extend to composite N; this result makes no original weighted W_N, native H0/B0, semilinear Frobenius or Delta_p-R_p claim. Original P000 and frozen science remain unchanged.

Next: seek an integral creative-telescoping or holonomic proof of the candidate N|UV, or a genuine counterexample beyond m=1000; maintain the exact q-adic branch-valuation observer. For the parent native Task, first obtain actual H0/B0 and Frobenius module and the missing session/CLAIM binding. The UR V2 94687-byte source bundle (SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76) remains unrecovered; its mathematics is not recomputed.

Provenance: same H40 author context; no independent mathematical review, no Source-native Task checkpoint or Result. Existing Source-completed predecessors and prior author proofs retain original contribution histories.
