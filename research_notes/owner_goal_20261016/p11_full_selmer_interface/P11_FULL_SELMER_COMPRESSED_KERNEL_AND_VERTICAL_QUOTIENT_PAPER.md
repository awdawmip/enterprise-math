# The full Selmer kernel and the precise obstruction to vertical completeness

Status: UNREVIEWED NEW AUTHOR PAPER, tenth separate object. EM-DVR-F73673. This addresses the remaining full-Selmer versus vertical-subspace gap; no earlier pairing PASS reviews this paper. No scientific program, matrix-rank consumer, factorization, point search or parameter enumeration ran. No new Task, registered Tool, Native Result or truth promotion is created, and the fixed-(233,119) certificate's actual inputs, witnesses and budget are unchanged.

## 1. Primitive parameters and the exact new question

Let r>s>0 be coprime and of opposite parity. Set
A=r²−s², B=2rs, P=A+B, Q=|A−B|, D=P²−Q²=4AB,
and E:y²=x(x−P²)(x−Q²), ordered roots (0,P²,Q²).
Let e be the even member of {r,s}, and epsilon=1 if 4|e, otherwise epsilon=0. Thus v2(D)≥5 in the first branch and v2(D)=4 in the second.

The first/eighth complete local tables give the full all-place Selmer criterion. The fourth/fifth/ninth papers compute a finite Cassels pairing on its vertical subspace V. That restriction cannot by itself certify that V is the entire Selmer group. The precise missing question is: which first-coordinate-nontrivial Selmer directions exist, and when can they be proved absent without silently dropping them?

This paper derives an exact compressed kernel and an exact quotient criterion from those local tables. The alternating matrices introduced below are Legendre **compatibility** forms on auxiliary coefficient spaces, not the Cassels pairing on Selmer classes. Their radicals do not carry a rank-E or Sha interpretation by themselves.

All curves and local fields retain external classical types. The argument is static arithmetic, not a native low-dimensional spatial model. Heartbeat X6's six discrete spatial Cell axes, absence of a native plane and time-as-needed separate typing are retained, with no WT/Foundation change.

## 2. Joint norm identities and forced coefficients

The primitive identities
P=(r+s)²−2s²,   A−B=(r−s)²−2s²
show that 2 is a square modulo every odd prime of PQ: a divisor of s would also divide r, so division by s modulo that prime is legitimate. Hence every such prime is 1 or 7 modulo 8. Partition their 1 modulo 8 prime support, with P/Q labels retained, as

J_P={p|P : p≡1 mod8},   J_Q={q|Q : q≡1 mod8}.

These are disjoint because gcd(P,Q)=1. Let J=J_P disjoint-union J_Q, m=|J|, and let T be the distinct odd prime support of D, d=|T|. All three supports are disjoint. Complete certified factorizations are required if these definitions are consumed as an actual finite interface.

Represent a full Selmer class by its first two signed rational S-unit squareclasses (a,b), with S the prime support of 2PQD and third coordinate ab. The good-prime image proves this support restriction. At an odd prime of D the first coordinate is square, killing its local valuation bit. At a prime of PQ congruent to 7 modulo 8, the unit-pair image kills the first and second valuation bits. At 2, both complete images require the first valuation to be even. Infinity makes the first sign positive. Therefore necessarily

a=alpha_P alpha_Q,

where alpha_P and alpha_Q are positive products of distinct primes in J_P and J_Q. No sign, 2, D-prime or 7-modulo-8 PQ bit remains in a.

At p∈J_P, the local image is diagonal, forcing the p-exponents of a and b to coincide. At q∈J_Q the second local coordinate is square, forcing its q-exponent to be zero. The preceding 7-modulo-8 conditions remove every other PQ bit from b. At 2, b may have a 2-bit only if epsilon=1; at valuation four that bit is forbidden by the eighth theorem. Thus necessarily and uniquely

b=alpha_P c,
c=(−1)^u 2^(epsilon v) product_(ell∈T) ell^(z_ell).

Here u and the z_ell are F2 bits; v is a bit only when epsilon=1, and is absent when epsilon=0. The sign and optional 2 bit are retained, not projected away.

Conversely every pair in this displayed carrier has exactly the forced valuation and real-sign properties. It also meets the dyadic requirement: each prime in J is 1 modulo 8, so a is a square in Q2. For epsilon=1 the local image is vertical with arbitrary second coordinate. For epsilon=0 it permits that first square and every odd-unit second coordinate, exactly as imposed on c. Thus there is no remaining dyadic character equation after these forced coefficients are eliminated.

In particular the local first-coordinate class 5 from the eighth theorem is genuine locally, but never the Q2 restriction of a global Selmer first coordinate for a primitive core: the latter is a positive product of J primes. This does not make the global first coordinate rationally square; distinct J products can still be nontrivial rational squareclasses whose restriction at 2 is square.

## 3. Every remaining condition is a unit Legendre row

Write chi_p(t)=0 if the p-adic unit t is a square modulo the odd prime p, and 1 otherwise. It is an additive F2 character on unit squareclasses. After the forced coefficients above, the complete all-place criterion is precisely

chi_ell(alpha_P alpha_Q)=0 for every ell∈T,
chi_p(alpha_Q c)=0 for every p∈J_P,
chi_q(alpha_P c)=0 for every q∈J_Q.

The first line is the remaining first-coordinate square condition at D primes. At p∈J_P, a/b=alpha_Q/c is a unit because the common alpha_P factor cancels exactly. Its square condition is therefore the second line, since a unit and its inverse have the same quadratic character. At q∈J_Q, b=alpha_P c is already a unit, and its square condition is the third line. This cancellation is why P/Q labels and the joint first/second-coordinate relation must be preserved.

No other place contributes a condition: all PQ primes were partitioned; 2 and infinity were checked; and the uniform good-prime theorem covers every remaining prime. Stoll's full all-place Selmer criterion proves both directions, not just an injection into a larger matrix kernel. No rational point is produced by solving these equations.

At every j∈J, chi_j(−1)=chi_j(2)=0 because j≡1 mod8. Hence the retained sign bit and optional 2 bit of c are free in these character equations. All nonfree equations involve only z=(z_ell), alpha_P and alpha_Q.

## 4. A symmetric zero-diagonal compatibility matrix

Define the m-by-d matrix L with rows j∈J and columns ell∈T by

L_(j,ell)=chi_j(ell).

Define B with rows p∈J_P, columns q∈J_Q by B_(p,q)=chi_p(q), and define the m-by-m matrix

K = [ 0  B ; B^T  0 ]

in the J_P/J_Q order. All characters are at coprime units. Quadratic reciprocity gives chi_ell(j)=chi_j(ell), even when ell is 3 modulo 4, because j is 1 modulo 4. It also gives chi_q(p)=chi_p(q). Consequently the three families of conditions in Section 3 become exactly

L^T alpha=0,
L z + K alpha=0,

where alpha concatenates the J_P and J_Q exponent vectors. Equivalently the nonfree full Selmer coordinates form the kernel of

M = [ 0  L^T ; L  K ]

on the ordered carrier (z,alpha). The full Selmer group is isomorphic to F2^(1+epsilon) times ker M, through the explicit reconstruction a=alpha_P alpha_Q, b=alpha_P c. This is a faithful coordinate reduction: it eliminates forced zero/equal coefficients, and reconstructs every remaining global Kummer class uniquely. It is not an information-losing observer which independently forgets a and b.

The matrix M is symmetric with zero diagonal. In the finer T/J_P/J_Q partition its three diagonal blocks are zero. Therefore it represents an alternating bilinear compatibility form over F2, and has even rank. One elementary proof is to select a nonzero off-diagonal entry, split off its nondegenerate two-by-two alternating block by a change of basis, and continue on the alternating orthogonal complement. The zero matrix is the base case.

This alternating property concerns the local compatibility matrix. It is **not** an equality with the elliptic Cassels form, a claimed Sha pairing or a reason to assign any curve rank.

## 5. The exact nonvertical quotient is another compatibility radical

Let C=ker L^T in F2^m and restrict the bilinear form alpha^T K beta to C. Denote its radical by A0. Then

0 → V → Sel²(E/Q) → A0 → 0

is an exact sequence of F2 vector spaces, where the last map remembers alpha. There is no preferred splitting and no rational-point assertion.

Proof. A prescribed alpha has a lift precisely when alpha∈C and K alpha lies in im L, by the two exact matrix equations. For the standard nondegenerate dot product, im L=C^perp. Thus the lift condition is equivalent to beta^T K alpha=0 for every beta∈C, exactly alpha∈A0. Every such alpha has some z solving Lz=Kalpha, and the reconstruction then gives a genuine full Selmer class by the already proved all-place equivalence. Fibres differ by ker L and the retained free sign/2 bits. The kernel alpha=0 is precisely the vertical space V. This proves exactness.

Put rho=rank L and sigma=rank(K restricted to C). Since the restricted K form is alternating, sigma is even. The exact dimension formulas are

dim V=1+epsilon+d−rho,
dim C=m−rho,
dim A0=m−rho−sigma,
nu:=dim Sel²(E/Q)=1+epsilon+d+m−2rho−sigma.

Equivalently rank M=2rho+sigma. These are identities in the actual finite character matrices, not executed rank computations. In particular

nu ≡ 1+epsilon+d+m mod2.

This is a Selmer-dimension parity statement only; it assigns no rational rank, root number, analytic rank or Sha parity from an uncomputed compatibility form.

The exact stopping/coverage criterion is

V=Sel²(E/Q) if and only if K restricted to C is nondegenerate.

If dim C is odd, an alternating form on C has nonzero radical, so A0 is nonzero and V is necessarily a proper subspace. In that branch any attempt to use dim V as the full nu, or to certify the full Cassels radical from a vertical matrix alone, is invalid. This provides a finite provable nonvertical-obstruction test, not a guessed limitation or a failed search.

Even when A0=0, no curve rank follows without an actual Cassels pairing and, where required, rational Kummer information. If A0 is nonzero, a full-Selmer dimension still comes from the formula, but the vertical Cassels restriction leaves those new directions' pairings unresolved. Its actual rank still gives only the legitimate bound rank(E(Q))≤nu−2−rank(restricted pairing).

## 6. Exact special branches and reuse

If J is empty, then C and A0 are zero. The full Selmer group is vertical and nu=1+epsilon+d. This recovers the old all-PQ-primes-7-modulo-8 branch in both dyadic regimes: d+2 when 4|e, and d+1 when e is 2 modulo 4. No new curve dimension is computed. The earlier core-(5,4), core-(9,8) and core-(6,1) papers keep their own independent inputs and scopes.

If one of J_P,J_Q is empty, K is zero, so A0=C. In that branch vertical completeness holds exactly when L has full row rank. This is an exact matrix criterion, not a claim that the rank condition holds for all cores. If both sides are nonempty, the cross-character block B can remove nonvertical directions through its restriction to C; it must not be dropped merely because the local first coordinate is square at 2.

The compatibility interface needs distinct prime supports for these character equations, but a future reconstruction or pairing consumer must still retain actual P,Q, root order, factor multiplicities and the Euclidean core. In particular D's squareclass and the PQ multiplicities in the ninth Cassels formula cannot be recovered by treating every support exponent as one. The reduction here preserves exactly the full Kummer class and declared membership/quotient readout; it does not authorize erasing data needed by other observers.

## 7. Dependencies and strict boundary

Only the first and eighth complete local-image theorems, Stoll's full split Kummer/all-place criterion, elementary unit Legendre characters and quadratic reciprocity are required for the new kernel/quotient proof. The first is exact Source270c9c6470db2cb14885f82d1021754f2bf19b23, research_notes/owner_goal_20261016/p11_parametric_local_images/P11_PARAMETRIC_LOCAL_IMAGE_AND_DYADIC_OBSTRUCTION_PAPER.md,11894B SHA25613e6d431795353340280c2f9b14c148e117139c85bbd797bf73336e891d453c6. The eighth is exact Sourcefe6eb52b197ab7c3f1791fcf9e4a75decc16bc78, research_notes/owner_goal_20261016/p11_complete_dyadic_local_images/P11_MISSING_DYADIC_VALUATION_FOUR_COMPLETE_IMAGE_PAPER.md,9596B SHA2567bef7c3940ba9b2aeb63d1663bf0976c67bca1d4032e150e5ae042d949ba9934.

The classical primary is the previously inspected Stoll2001 DOI10.4064/aa98-3-4, exact PDF SHA256b4854a404601da748a687c64a3d72a36033590a4ba911b7021db53340c5aa9d1, with the same split cubic root order, homomorphism/kernel, zero coordinates, local index and Proposition4.2 already bound in the prior Source62f22f7432923ac4c04d9a89944957654920a481 archive. No pairing theorem is required for the new compatibility radical. The optional last rank inequality separately uses the already explicit genuine Cassels/rational-radical interface; it is not inferred from M or K. The ninth pairing application remains a different independently reviewed paper and is not this new object's review.

This composes the same method family at a recorded full-Selmer/vertical scope gap. It does not claim a new shared Tool, an executed implementation, historical novelty or comprehensive registry/literature absence. Old accepted fixed-core seeds, F5, H, multiples and five closed Tasks are not repeated. Original source/author/Driver planning contributions remain in their immutable archives, and the current author cannot give a decisive Native vote on these own claims.

Fail/kill conditions include a nonprimitive or same-parity core, incomplete/wrong factorization, lost P/Q labels, a mistaken root/zero convention, importing general odd P,Q primes that do not obey the joint norm-two identities, replacing signed rational squareclasses by an insufficient local residue, or a failed Stoll/local-image binding. They prevent invoking the corresponding compressed theorem. No actual compatibility or Cassels rank is computed, no point is found, and no exact global rank, saturation, odd-primary Sha, whole-Sha finiteness, infinite family or all-core classification is supplied. No new Task, program authorization, budget extension, parent closure, WT or Foundation change follows. A separate genuine nonauthor paper review is required.
