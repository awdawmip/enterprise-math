# C312 — Complete zero-extra-content certificates for 106 remaining frozen paths

Classification: author-level hand proof plus two exact arithmetic implementations; C300/C305 upstream factorized numerator identity still requires independent source audit. Not a Source Result, independent Driver admission, Working Truth, Foundation theorem or BRC/X6 native-transfer claim.

Frozen canonical reads: GLOBAL_KNOWLEDGE_V1 main@0640165130b1a9268805f3ee02e8fb88ecfe368e; enterprise-math scientific main@56f75ca89dc8a07824e0c02200dcc41fff6a9133; C311 immutable predecessor d6f60a8ebf6a9b9fac7f50e6a881ad1eba211ab2. Exact frozen 125-path C293 records SHA256 03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89.

## Theorem A: zero-extra-content certificate with unfactored composite cofactor

Suppose s>0 and C,P,J_a are integer polynomials satisfying C P = sum_a J_a, with content(C)=1. Put

L = gcd(s, content(J_1),...,content(J_m)); S=s/L; R=(sum_a J_a)/L.

Assume the exact factorization S=H product_{q in Q} q^{e_q}, in which H>=1 is an arbitrary positive integer, Q is a set of distinct verified primes and e_q>=1. For every q in Q, provide a degree k_q such that coefficient [t^{k_q}]R is nonzero modulo q. Additionally exhibit T with gcd(H,R(T))=1; vacuous when H=1. Then:

gcd(s,content(P))=L.

Proof: L divides every J_a coefficient, hence L divides content(CP)=content(P), by the primitive C hypothesis and Gauss's lemma. Consequently P/L belongs to Z[t], R=C(P/L), and content(R)=content(P)/L. Each coefficient witness rules out its prime q from content(R). Since content(R) divides every integer value of R, gcd(H,R(T))=1 rules out every prime factor of the entire, possibly unfactored, H. Thus gcd(S,content(R))=1, and gcd(s,content(P))=L. QED. No factorization of H is required.

## Theorem B: a finite-field reason integer-only samples can never suffice

For prime p and integer F(t), F(n)=0 (mod p) for ALL integers n iff the reduction of F modulo p is divisible by t^p-t in F_p[t]. The latter equals the product over all a in F_p of (t-a); its distinct linear factors divide F iff every residue is a root. QED.

In particular F=t(t-1) has content 1 but every integer sample is even; integer point-gcd methods cannot exclude 2 from content(F). The exact coefficient witnesses in Theorem A are therefore essential when a path polynomial is a nonzero F_p polynomial that represents the zero function.

## Certified finite-family result

Frozen model: C195/H168 scalar auxiliary with 79 separately labelled rational branches; 125 C293 paths, 19 exceptional indices independently treated as author-level certificates in C311. C312 enumerates exactly the complement of 106 indices (105 of reduced degree 352 and one path index 28 of degree 265). It independently constructs L via primitive-factor term contents, exactly trial-divides S by every prime below 10000, records the residual H, extracts a nonzero polynomial coefficient of R modulo EVERY listed small prime, and verifies gcd(H,R(1))=1 using a modular Bézout inverse.

Primary exact calculation: 106/106 paths PASS; 881 small-prime polynomial coefficient witnesses PASS; 106 cofactor modular inverse certificates PASS. H is 250 bits on 105 paths and 186 bits on index 28. Optional posthoc comparison against the historical C306 content oracle matches on all 106 but is not a proof premise.

Independent implementation: Python BigInt Kronecker-packed exact truncated polynomial multiplication, rather than the primary NumPy integer coefficient convolution, verifies all 881 witnesses; a distinct direct summed-numerator/division circuit rechecks all 106 H modular residues and inverses. In addition, 391 complete small-prime residue-class sweeps pass. These two implementations SHARE the C300/C305 frozen factorized source input and are not an independent audit of that input.

Exact observed zero-function obstruction counts (nonzero R polynomial mod p, but R(n)=0 mod p for every integer n):

| p | paths containing p in S | zero-function paths |
|---|---:|---:|
| 2 | 106 | 94 |
| 3 | 38 | 38 |
| 5 | 106 | 97 |
| 7 | 106 | 106 |
| 11 | 35 | 34 |

The remainders in F_p[t] modulo (t^p-t) were also checked and agreed with all residue-class evaluations. Thus all 106 frozen paths have the p=7 fixed-divisor/evaluation obstruction; that is a finite-family conclusion in this auxiliary scalar model, NOT a theorem about all integer polynomials.

Together with the 19 preexisting C311 exceptional-path certificates (15 exact extra factors 2, four extra factors 3), this yields all 125 author-level coefficient-content gcd certificates WITHOUT using the old C306 full Newton scan as a proof assumption. Earlier C311 evidence is consumed rather than relabelled as freshly re-executed here.

Source code and independent verifier reside alongside this note. Frozen source input and previous C311 data are carried in the earlier replay capsule; C312 complete replay includes the exact 106-path per-prime coefficient positions/residues, 106 H residues/inverses and local run logs. The validation scope and complete data hashes are in the C312 audit summary. Individual proof records are not promoted without verifying their actual bytes.

## Authority and remaining obligations

GitHub authenticated login awdawmip has repository push/admin permission. Native em_control_tasks returned CONTROL_QUOTA; em_session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. The active native owner is therefore UNKNOWN and no CLAIM, native Result, clean-blind Driver review, or formal mathematical admission is asserted. A GitHub branch is author-side storage, not canonical main integration.

The scalar polynomial quotient does not erase original BRC branch identity, phase, port, sign, provenance or future-operation residual. No native GF(2)-BRC/X6 transfer is claimed; the six-dimensional native Cell space and P000 remain locked and unchanged.

Next C313: independently reconstruct and compare the original C300 exact numerator identity C P=sum J_a for all 125 frozen paths, with independent source definitions, focusing on path 28 and the 19 exceptional pairwise cancellations, prior to any mathematical promotion.
