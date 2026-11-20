# R1160A Gaussian norm/orientation generator, exact finite test, 2026-11-20

Task RS-R1160A-GREGORY-MACHIN-RATIONAL-ATOM-GENERATOR. Status: author calculation staged, not yet Source-published, not reviewed. Original immutable references: Gregory-Machin 1160 durable handoff 2026-09-09 and original H1000 exact support-two census.

**Finite theorem.** Every primitive turn atom [b+ai] with 0<a<b<=H and gcd(a,b)=1 can be produced without production scanning coprime coordinate pairs by enumerating integer norms n<=2H^2 and retaining n with no prime q congruent 3 mod 4, and with exponent of 2 at most 1. For n=2^epsilon * product p^e (p congruent 1 mod 4), choose one exact sum-of-two-squares Gaussian factor pi_p and enumerate (1+i)^epsilon * product (pi_p^e or conjugate(pi_p)^e). Filter each product's four unit associates to 0<a<b<=H. The empty split-support case yields no strict atom. This is the generator; a separate pair scan is used only as a finite oracle.

Proof: Gaussian unique factorization; for primitive b+ai inert q would divide both coordinates; (1+i)^2 is an associate of 2, hence ramified exponent <=1; using both factors over a split p makes p divide both coordinates. Thus each primitive input occurs. Distinct orientation lists/norms cannot yield associate duplicates by unique factorization; each unit orbit has at most one strict-octant representative, hence each atom is emitted once.

**Free-direction key.** For surviving factor list, take signed oriented split exponents s_p e_p, divide by their common gcd and identify vectors up to global sign. This ignores independent C8 torsion, preserves the old free-direction equivalence count, and is unaffected by per-prime factor orientation conventions.

**Measured exact results** (one local g++ -O3 -std=c++17 host run; separate oracle scans only for comparison):
- H=30: admitted norms 324; oriented descriptions 854; unique atoms 277, free directions 180, oracle 277.
- H=100: 3144; 9558; 3043, 2018, oracle 3043.
- H=300: 25594; 85950; 27397, 18218, oracle 27397.
- H=1000: 259466; 954918; 304191, 202662, oracle 304191; about 0.53 sec / 46080 KiB.
- H=1100: 311876; 1155408; 368117, 245234, oracle 368117; about 0.66 sec / 55040 KiB.

Each accepted atom occurs once in the generator and is found by the independent oracle; H1000 reproduces the frozen 304191-atom and 202662-free-direction baseline. The older pair-circuit and Pareto totals (102186 and 101706) are NOT rechecked by this implementation.

**Scope/obstruction.** The algorithm does not scan coordinate pairs in production, yet its norm sieve ranges across O(H^2) integers and generates more orientations than surviving atoms: 954918 vs 304191 at H1000. No asymptotic speedup is established. H1100 is the larger bounded finite reproduction, not universal performance. The sum-of-squares factor selector uses a floating square-root estimate corrected and certified by exact 64-bit integer squaring; output and comparisons use exact integers. For much larger H, integer ranges and sieve resources must be rechecked. End-to-end comparison against the original Python baseline and better multiplicative recursion/height pruning remain open.

Reproduction: compile companion C++17 script with g++ -O3 -std=c++17 and run executable with args 1000 and 1100.