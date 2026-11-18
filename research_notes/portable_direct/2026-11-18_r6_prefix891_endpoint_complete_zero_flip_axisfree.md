# PREFIX-891 — Zero/flip collision endpoint characterization and axis-disjoint exact census

Date: 2026-11-18 (Asia/Shanghai). Researcher: EM-DIRECT-53C174; research session MCP-58ecc35bbe7c440d9169f344aa8eff28. This is an independent BRC observation auxiliary unit, not a native X6 time-dynamics claim. Frozen scientific-input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. PREVIOUS: PREFIX-889 (zero/flip modular-inverse counts) and PREFIX-890 (disjoint type-resolved collision spectrum). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Exact model and question

Let p >= 1, N=2^p, q1 and q2 odd positive integers greater than 1. Named legal trajectories are Z_x=(x,x), 0<=x<N; and F^i_u=(u,u xor 2^i), 0<=u<N, 0<=i<p. Observe Phi(a,b)=(a mod q1,b mod q2). Let ZF_p(q1,q2) denote the total number of different unordered (Z,F) pairs with identical observations, as in PREFIX-889. We characterize **existence** using at most 2p explicit endpoint candidates, without counting every legal state.

## Theorem 891-A: endpoint-complete collision criterion

If gcd(q1,q2)>1 then ZF_p=0. Otherwise let

K=floor((N-1)/q1), r_i = (2^i * inv(q1 mod q2)) mod q2, with 1<=r_i<q2.

Then ZF_p(q1,q2)>0 if and only if at least one i in {0,...,p-1} satisfies

(A) r_i<=K, or (B) (q2-r_i)*q1 + 2^i <= N-1.

If (A) holds, choose k=r_i, u=N-1, x=N-1-kq1. Then Z_x and F^i_u are different legal trajectories with the same observation (the named bit is toggled downward).

If (B) holds, choose k=q2-r_i, u=N-1-2^i, x=N-1-2^i-kq1. Then Z_x and F^i_u have equal observations (the named bit is toggled upward).

**Proof.** A collision implies u-x=kq1 with nonzero integer k, since q1 divides the first-coordinate difference. The second-coordinate condition is q2 | (kq1+s2^i), where s=+1 if bit_i(u)=0, otherwise s=-1. Since gcd(q1,q2) divides 2^i and is odd, gcd must equal 1. The complementation involution J(y)=N-1-y maps any negative k witness to a positive k witness, preserving equal modular observations, while switching the toggling sign. For positive k, downward toggling requires k congruent r_i (mod q2), and the maximal possible u with bit_i(u)=1 is N-1. Thus some downward witness exists iff its smallest positive congruent k=r_i obeys r_i*q1<=N-1, equivalently (A). For upward toggling, k congruent -r_i (mod q2); the maximal u with bit_i(u)=0 is N-1-2^i, so existence is equivalent to the smallest positive k=q2-r_i satisfying (B). The displayed endpoint witnesses establish the converse, with x in [0,N). Distinct trajectory types exclude identity. QED.

This is a necessary-and-sufficient theorem for **ZF existence**, not for all two-flip collisions. For the specified 19-bit domain, K<q2/2, so (A) and (B) cannot hold simultaneously at a given i. A modular inverse plus p modular residue updates and integer comparisons decides the family without evaluating PREFIX-889's multiplicity sums. The BRC carrier retains transition type Z/F, named source i, directed time ports, and exact nonnegative integer witness counts; endpoint compression is valid for Boolean existence only.

## Theorem 891-B: exact axis-disjoint panel census

Set p=32, Q={262145,262147,...,524287} (131072 odd moduli). Define the PREFIX-887 single-axis collision set A_32={q>1 odd : some 1<=h<32 has q | (2^h-1) or q | (2^h+1)}. Q contains exactly 24 members of A_32. Choose the sixteen first-port values

262147, 280001, 300001, 320003, 340007, 360007, 380003, 400009, 420001, 440003, 460001, 480007, 500383, 510007, 520001, 524285.

All sixteen are outside A_32. Exact full scanning of each row against all q2 in Q yields 2,097,152 ordered pairs, of which 1,308,292 have a constructive zero/flip collision. Exactly 207 of those have q2 in A_32. Therefore **1,308,085 ordered pairs** admit explicit ZF collision certificates and are outside *both* PREFIX-887 axis-aligned families. The sixteen rows are disjoint by first-port identity; no duplicate pair is counted. This is new coverage relative specifically to the single-axis criterion, and no claim is made about deduplication against all other PREFIX-874..890 methods.

The exact per-row counts and a direct witness for each row are in PREFIX891_R6_ENDPOINT_RESULTS.json. For instance, q1=262147, q2=262149 has witness x=4294705146, u=4294967293, i=1: the trajectories (x,x) and (u,u xor 2) have the same residue observation. Both moduli are outside A_32.

## Reproduction, checked scope, and frontiers

Run: python3 research_notes/portable_direct/PREFIX891_R6_ENDPOINT_CERT.py > PREFIX891_R6_ENDPOINT_RESULTS.json. It uses Python exact integers and no third-party packages, checks 648 direct brute-force parameter triples p=1..8, q1,q2 odd in [3,19], scans all 16 rows of Q, validates first witness in each successful row, and asserts five full independent Python-row counts (q1=262147,300001,400009,500383,524285) against a separately implemented power-modulo formula. An independent C++17 implementation also scanned all 16 rows with the same totals and separately performed 567 small triples. The complete 16-row main scan is deterministic finite enumeration, not a statistical sample. Neither program is a formal proof checker; the theorem above supplies the general argument.

Scientific next question: apply this endpoint existence shortcut to the remaining axis-free and ZF-free 19-bit pairs; then test the PREFIX-882/883 two-flip modular-inverse criterion on those pairs and deduplicate its exclusions. The wider target remains B_fix,odd(32) in {19,20} under the frozen scientific model. No X6 shared CLAIM, Result promotion or Working Truth status is asserted.
