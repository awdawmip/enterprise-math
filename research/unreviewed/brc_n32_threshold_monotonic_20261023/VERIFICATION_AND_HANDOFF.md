# N32 verification and research handoff

Date: 2026-10-23. Status: unreviewed author-side theorem; non-canonical branch; native Owner/CLAIM not verified.

## Scientific increment
For all integers n>=4 the unique positive roots of N31's four-label auxiliary
single-pulse growth polynomials obey theta_n < theta_(n+1). Stronger exact
estimate: Z_(n+1)(theta_n) < -2/5. Uniform rational localization:
1-2/3^(n-2) < theta_n < 1-1/(2*3^(n-2)).
Any z<1 has a finite positive post-pulse gain horizon certified by
(1-z)*3^(n-2)>=2. After a post-pulse nonpositive gain there can be no
later post-pulse positive rebound for this single-pulse family.

## Exact author verification
Executed Python-stdlib Fraction checker, output counts:
- exact rational endpoint checks: 47 (n=4..50).
- exact rational recurrence checks: 376 (47 n x 8 rational z).
- rational dyadic unique-root brackets: 13 cases, 92-bit denominators.
- finite-horizon sign examples: 4 fixed rational z.
- all assertions passed; no floating point used for proof decisions.

All 13 intervals use denominator D=4951760157141521099596496896 = 2^92.
Each record is (n, lower numerator), with upper numerator lower+1:
4 4459162553834274028683353508
5 4790859127044322464915738897
6 4897590260597840661039643263
7 4933422440204357714208640494
8 4945544480534331850490572626
9 4949654181590197526577350059
10 4951047666611438416019216821
15 4951757094561814122856782876
20 4951760144394663095672799296
25 4951760157088947510441446952
30 4951760157141304662675929768
31 4951760157141448952263288542
32 4951760157141497050093509247

Concrete exact numerator/denominator witnesses:
- z=99/100: Z_6 = 16990619/100000000 > 0;
  Z_7 = -1675504250899/500000000000 < 0.
- z=999/1000: Z_8 = 405937625969781029/1000000000000000000 > 0;
  Z_9 = -1348307568823350342511999/500000000000000000000000 < 0.
The witnesses illustrate single-transition sign behavior; the all-round
no-rebound theorem follows from the algebraic proof, not finite samples.

The proof is in PROOF.md. Running verify_threshold_monotonicity.py reproduces
the exact tests and creates EXACT_CHECKS.json in the same directory.

Local full manuscript SHA-256:
b3cdb254723e13d312d29b357108e27af5f9e43a1a1d9680abb439b4e78d1435
Local verifier SHA-256:
43540a5838e14c2a1897bced7fca28fc20de80cf20f595375337705d5cc19b3a
Local output JSON SHA-256:
89a952385275083f6de129c9d2f7876abc4af895fe77171495195b98d6270d37
These hashes identify the local files, which are not byte-identical to
this GitHub markdown and companion source; they are not remote proof receipts.

## Frozen authority and limitations
GLOBAL_KNOWLEDGE_V1 main 7a56e3a5a31c6af97f47a09befb54ae4443c9b41.
EM main f768a9f34aa7b0a9521325c52e0638dc7fba0a27.
N31 source: b70c8cf71b9557569da66eddf44ebdd4057d082c.
P000 remains locked. Auxiliary four-label model is not the native X6
observer; the needed embedding, readout and preserved transitions are
not available. No formal Researcher-ID or CLAIM, independent review,
Result, Working Truth or Foundation admission is claimed.
Control: em_control_tasks=CONTROL_QUOTA;
em_session_start=STATIC_READONLY_SCOPE_DENIED, operation_sent=false.

## Next smallest unit
Study exact two-pulse words 0^a 2 0^b 2 0^c, a>=3,b>=1,c>=1,
retaining the two pulse locations and the 16 occupancy states. Search for
an exact post-second-pulse negative-to-positive revival or prove an
appropriate monotonic invariant. A proof of all-strategy L_min is still
open. Do not infer this auxiliary result for P000 X6 before a faithful
bridge exists.
