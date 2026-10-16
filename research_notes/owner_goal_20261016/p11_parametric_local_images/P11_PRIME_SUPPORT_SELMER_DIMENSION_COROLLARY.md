# A closed-form Selmer-dimension corollary under a checkable prime-support condition

Status: UNREVIEWED AUTHOR PAPER ADDENDUM. EM-DVR-F73673. This is a separately frozen third object; neither of the first two frozen papers is changed. No new Task, accepted Tool, Native Result or scientific invocation is created.

Assume the model and hypotheses of P11_PARAMETRIC_LOCAL_IMAGE_AND_DYADIC_OBSTRUCTION_PAPER.md: P,Q are distinct coprime positive odd integers and32|(P²−Q²). Add the finite checkable hypothesis:

Every odd prime dividing PQ is congruent to3 modulo4.

Let T be the distinct odd prime support of D=P²−Q² and d=|T|. Then the author-derived complete Selmer formula is
Sel²(E/Q)={(1,b,b): b∈〈−1,2,p:p∈T〉},
dim Sel²(E/Q)=d+2,
and consequently
rank E(Q)+dim Sha(E/Q)[2]=d.

Proof. Since gcd(P,Q)=1, the odd prime supports of P,Q,D are disjoint. Use signed squareclasses supported on2PQD. Infinity kills the first-coordinate sign; the complete dyadic vertical image kills its2 coefficient; every p|D kills its p coefficient; every p|PQ has unramified-pair image and kills both p valuation coefficients. Therefore the first class is1. The second class has exactly the free coordinates −1,2 and the primes of T. All remaining local unit-character conditions are automatically satisfied for first class1 and the allowed second units. Conversely each displayed second class satisfies every complete image, so this is equality. Distinct signed rational prime classes are independent. The usual exact Kummer sequence and dim E(Q)/2E(Q)=rank+2 give the last identity without any Sha finiteness assumption.

In particular rank≤d. If an actual full2-descent Cassels pairing certificate on this Selmer space has matrix rank 2t, then
rank E(Q)≤d−2t,
because the rational Kummer image lies in its radical. This bound is conditional on the actual proved matrix entries and complete local-image hypotheses; local solubility alone never supplies those entries. If d=2 and one pairing is nonzero, the bound is rank0, and the same radical argument as in the separately frozen core(5,4) paper identifies Sha[2∞]=(Z/2)². No such conclusion is made when the pairing has not been established.

For the new Euclidean core(5,4), P=49=7² and Q=31 meet the prime-support hypothesis, T={3,5}, d=2. Thus the new rank-zero paper is an instance of a checkable parameter criterion, not a claim of constant rank across all cores. The old fixed(11,8) input P=233,Q=119 does not meet this added hypothesis (233 and17 are1 mod4), so its rank1 proof is a different branch and is not contradicted.

For Euclidean cores r>s>0 of opposite parity the earlier condition32|D is exactly divisibility of the even member by4. If instead that member is2 mod4, U2 fails at2 and this corollary is unavailable. Primes of PQ congruent1 mod4 also require retaining the more general coupled unit-character matrix rather than this closed formula. Noncoprime/even P,Q, repeated roots, incomplete factorization or any missing local theorem kill use of the corollary.

Source dependencies: Stoll’s split Kummer/local-index and Proposition4.2 full2-Selmer framework, with the exact edition/hash cited in the parameter paper; its new valuation proofs are essential. Alternating full2-descent/Cassels–Tate compatibility is only needed for the optional pairing-rank consequences and is cited with the exact FSS/Shukla–Stoll versions in the rank-zero paper. No historical novelty claim is made.

Unknowns retained: rational-generator saturation for positive-rank cases, odd-primary Sha, full Sha finiteness, existence of infinitely many Euclidean cores satisfying this factorization condition, actual rank or pairing values for any unexamined core, and all-core classification. No finite computation or enumeration was run.

