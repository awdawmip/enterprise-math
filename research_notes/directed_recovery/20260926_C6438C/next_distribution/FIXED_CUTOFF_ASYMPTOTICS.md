# Fixed K33 cutoff: a symbolic obstruction to uniform small Shor TV

Activity: RA-CAAAC604CB513AEA8BBC1DFC  
Researcher: EM-DIRECT-C6438C  
Status: AUTHOR_SYMBOLIC_DERIVATION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED

This is a new proof unit. It does not modify `next_cf_only/`, `support/`, the
phase bank, the original continued-fraction (CF) policy, or any frozen delivery.
There is no new ideal-reference numerical run, ordinary floating-point matrix
propagation, trigonometric evaluation, phase-grid increase, spectral numerical
fit, or empirical TV claim. The comparison distribution below is a symbolic
mathematical object. All statements about the actual instrument refer to the
already certified complete BRC gate columns and their exact composition.

## 1. Result and exact scope

Fix a legal coprime base a modulo N and its actual modular order

    r = 2^s d,  d odd.

Let P_t be the terminal k distribution of the pinned 61-mode, fixed 32/64-grid
K33 streaming instrument at width t. Let I_t be the ideal Shor order-finding
distribution with the same N, a and Q=2^t. Total variation uses

    TV(P,I) = (1/2) sum_k |P(k)-I(k)|.

Along even widths t tending to infinity, if d>3, we prove

    liminf TV(P_t,I_t) >= 1 - gcd(d,3)/d.                  (1)

In particular, a uniformly tiny approximation error is impossible even for a
single fixed order with odd part greater than three. The bound is at least 2/3
over all such odd d. This is a lower bound, independently proved below; it is
not inferred by reversing the existing linearly growing error upper bound.

For every fixed finite r and every admitted width, we also have

    TV(P_t,I_t) <= 1 - gcd(r,2)/r.                       (2)

Thus we do **not** claim TV tends to one for fixed N,a. For odd r>3 with
gcd(r,3)=1, (1) and (2) give the exact symbolic limit

    TV(P_t,I_t) -> 1 - 1/r.                              (3)

There is also an explicit family of odd composite, non-perfect-power inputs
with good bases and default widths t=2 ceil(log2 N) for which, at any fixed odd
prime p>=5,

    TV(P_t,I_t) -> 1 - 1/p.                              (4)

Because odd primes are unbounded, (4) rules out a single all-input TV guarantee
epsilon<1 for this fixed K33 implementation. It neither rules out other phase
policies nor contradicts the proved original-CF positive-success theorem.
These claims concern raw readouts conditional on the specified base. They do
not automatically extend to a random-base average or to the distribution of
CF/gcd factor-or-failure outputs: averaging and postprocessing can reduce TV.

## 2. Certified actual source and branch identity

The original fixed-word source is
`0852cad130c1d877174d235687cf60c19f318c58`. The current activity registration
Source is `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`. The actual full-bank
certificate `phases/bank_t34.json.gz` has decompressed payload SHA256
`feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c`.
It contains the full 61-mode columns, retained residual coordinates and inverse
checks. Its construction and provenance are in `../phases/PHASE_BANK_PROOF.md`
(SHA256 `1f59a1cb3e67f90f02242bb04c2ba9024857c62b8df546f96adfb9577eafce37`).

The exact branch derivation inherited by the streaming implementation is, on
one work-permutation eigencomponent lambda,

    K_(i,h,b) = (I + (-1)^b mu_i T_(i,h))/2,
    mu_i = lambda^(2^(t-1-i)),     b in {0,1}.             (5)

This is an operator on the entire D=61 internal carrier, not a projection to
the first two coordinates. The shared H4 spectator is factored out by its
proved even-round invariant. T_(i,h) is the real rational orthogonal phase
product determined by the actual previous bits h, in actual execution order.
The K33 policy retains m=2,...,32 and makes every m>=33 gate the full-carrier
identity. Each retained m occurs at most once per round. Hence T belongs to a
fixed family of at most 2^31 ordered subset products. No commutation of actual
phase gates is assumed. The history dependence uses at most 31 previous bits.

For any such T and any unit complex mu, direct multiplication gives

    K_0^* K_0 + K_1^* K_1 = I.                           (6)

In particular both branches are contractions. Complexification in (5) is a
proof decomposition of the real actual instrument, not a different runtime
propagator. Signed coordinates and all residual modes remain present.

The orbit of work label 1 has length r. Its cyclic Fourier eigenvectors have
eigenvalues lambda_j, j=0,...,r-1, and the initial work vector has squared
weight 1/r in each. Actual modular powers and all internal gates preserve
these work eigenspaces. Thus terminal probabilities are the orthogonal sum of
their conditional squared norms with weights 1/r; there are no cross terms
between distinct work eigenvectors.

## 3. Existing phase-product exclusion and uniform contraction

`../next_cf_only/PHASE_PRODUCT_STRUCTURE.md`, SHA256
`65a16d2aa2cad9427318be5e0bb56c83ed4b6684636c19f5745c9eb041a75baa`, proves
for every actual T in (5) that it is within

    eta = 177/2^32 < 1/2

of a planar rotation direct-sum the identity. The integer cyclotomic-norm
argument there then excludes every root-of-unity eigenvalue of T except
orders 1,2,3,4,6. This bound concerns the retained product; this proof has no
need to compare the complete ideal feedback or use its separate 185/2^32
bound. No multiword Phi3/Phi6 exclusion is assumed.

Call a work eigenvalue high-odd when its order has odd part greater than three.
Raising to any power of two preserves that odd part. Therefore, for any
high-odd lambda, every mu_i in (5) has odd part greater than three. Singularity
of K_(i,h,b) would require T to have eigenvalue -(-1)^b mu_i^(-1), whose order
has that same odd part. The phase-product theorem excludes it. Consequently
both branches are invertible, for every round and every possible history.

For fixed r there are finitely many relevant mu values and finitely many T.
Define the positive number

    c_r = min_(high-odd mu, actual T, b) sigma_min(K_(mu,T,b))^2 > 0.

Every selected branch obeys K_b^* K_b >= c_r I. Applying this lower bound to
the *other* branch and using (6) gives

    K_b^* K_b <= (1-c_r) I.                              (7)

This is the critical strict upper contraction bound. Invertibility of only
one branch would not suffice. Iterating (7) along any specified t-bit history
k, starting with a unit internal vector, gives

    conditional_mass_j(k) <= (1-c_r)^t                  (8)

for every high-odd work eigencomponent. This holds for all histories at once,
including histories near ideal peaks; no periodic-bit assumption is needed.

### Optional explicit constant, without enumerating the finite family

One may replace the finite minimum by the conservative explicit bound

    c_r = 2^(-468602 r) = 2^(-2 D (3840+1) r), D=61.      (9)

To prove (9), each retained nonexact complete gate has denominator dividing
2^128. There are at most 30 such gates in T, while the m=2 quarter turn is
integral. Thus entries of T have common denominator dividing 2^3840. Let
A=2^3841 and K=(I+sigma mu T)/2. Then A K has entries in the algebraic-integer
ring Z[mu]. For f=[Q(mu):Q]<=r, the nonzero element

    alpha = A^D det K

is an algebraic integer. Its field norm is a nonzero integer, so

    product_embeddings |det K_embedding| >= A^(-Df).

Each embedding sends mu to another unit root and leaves T unchanged. Each
embedded K is a contraction, hence its determinant has modulus at most one.
The selected |det K| is therefore at least A^(-Df). Every singular value of K
is at most one, so sigma_min(K)>=|det K|>=A^(-Dr). Squaring proves (9).
This proof uses no numerical determinant and no new arithmetic executor.

The constant is extremely conservative. It proves an asymptotic statement,
not a practical onset width, an observed exponential rate, or a small-N TV
estimate. The explicit value depends on r and the pinned bank, not on orbit
labels, the embedding into the W-label work array, N itself, or a particular
history.

## 4. Low-odd spectral weight and arbitrary small output sets

Set g=gcd(d,3), so g is 1 or 3. Among all r-th roots, exactly 2^s g have order
with odd part dividing three: they are exactly the roots of unity of order
dividing 2^s g. Their total initial spectral weight is

    w_low = (2^s g)/r = g/d.                             (10)

The remaining weight 1-g/d consists of high-odd components. Combining their
bound (8) with the trivial total-mass bound on the low-odd components, every
set S of terminal bins satisfies

    P_t(S) <= g/d + (1-g/d) |S| (1-c_r)^t.               (11)

In particular the high-odd portion cannot retain a positive limiting mass in
any set whose number of bins is polynomial in t, or more generally whose
cardinality times (1-c_r)^t tends to zero. This is a statement about absolute
unnormalized history masses, not a claim that every normalized conditional
transition has the same probability.

## 5. Symbolic ideal-peak concentration and the TV lower bound

For Q=2^t define circular bin distance modulo Q and the set

    S_t = {k: dist_mod_Q(k,Q j/r)<=t for some 0<=j<r}.

There are at most r(2t+1) bins in S_t. For an ideal phase theta=j/r, the standard
geometric sum gives the conditional bin law

    p_Q(k|theta) = |Q^(-1) sum_(x=0)^(Q-1)
                         exp(2 pi i x(theta-k/Q))|^2.

This formula is used symbolically only. If x=dist_mod_Q(k,Q theta)>0, the
numerator bound two and the sine chord bound on [0,pi/2] imply

    p_Q(k|theta) <= 1/(4 x^2).

At most two bins have distances in each interval (m,m+1]. Thus, for integer
t>=2, summing outside radius t gives

    sum_(dist>t) p_Q(k|theta)
        <= (1/2) sum_(m=t)^infinity m^(-2)
        <= 1/[2(t-1)].                                  (12)

The ideal realification has two orthogonal planar phase directions. Conditional
on a work eigenvalue, they give the positive and negative Fourier-phase laws
with weights one half. The uniform j mixture is invariant under j -> r-j, so
their total marginal is exactly the usual ideal Shor law. In particular there
is no extra factor two in (10), (11), or the comparison distribution. The set
S_t already includes both signs of all ideal peaks. The symbolic mixture of
(12) yields

    I_t(S_t) >= 1 - 1/[2(t-1)].                           (13)

Since TV is at least the difference on any event, (11) and (13) give the
explicit finite-width inequality

    TV(P_t,I_t) >= 1 - g/d - 1/[2(t-1)]
                  - (1-g/d) r(2t+1)(1-c_r)^t.           (14)

A negative right side simply gives no positive finite-width information.
For fixed r, polynomial growth of r(2t+1) is dominated by the exponential in
(14), proving (1) along the admitted even widths. The proof does not execute
the ideal law, enumerate the actual leaves, estimate an unknown order, or
provide hidden ideal readouts to the simulator.

## 6. Shared atoms prevent TV tending to one at fixed r

The lambda=1 work eigencomponent has weight 1/r. Along the all-zero history,
all controlled phase factors are inactive, so T=I and mu=1 every round.
Equation (5) gives K_0=I and K_1=0. This component therefore puts its entire
weight at k=0 in the actual law. The ideal zero-phase component also puts
weight 1/r at k=0. Thus both laws have at least the common atom 1/r at zero.

If r is even there is also a lambda=-1 work eigencomponent. In the first t-1
rounds, mu_i=1 and the all-zero history has T=I, so all those bits are forced
zero. In the final round mu=-1 and T=I, so the final bit is forced one. In the
actual little-endian output convention this is k=Q/2. The ideal phase-one-half
component is also deterministic at Q/2. Thus even r provides another common
atom of weight 1/r at Q/2, disjoint from zero.

The identity TV(P,I)=1-sum_k min(P(k),I(k)) now proves (2). When r is odd and
gcd(r,3)=1, g/d=1/r, so the matching liminf and uniform upper bound prove (3).
When r=2d and gcd(d,3)=1, the same argument gives the exact limit 1-1/d; in
particular r=2p has limit 1-1/p. No matching formula for all other r is
asserted. The positive-support result for d=3 says nothing by itself about a
limiting TV value.

## 7. Default-width counterexample family with genuine good bases

Fix an odd prime p>=5. For any integer m>=0 set

    a_m = 18m+4,
    q_m = (a_m^p+1)/(a_m+1) = Phi_(2p)(a_m),
    N_m = (a_m-1) q_m.

The quotient is the integer alternating polynomial

    q = a^(p-1)-a^(p-2)+...+a^2-a+1
      = (a-1)(a^(p-2)+a^(p-4)+...+a)+1.

For a>=4 and p>=5, q>=a^(p-2)(a-1)+1>a^2-1. Also q is odd, q=1 mod a,
and q=1 mod (a-1). Therefore gcd(a,q)=1, gcd(a-1,q)=1, and N is odd.

The integer identity a^p+1=(a+1)q directly gives a^p=-1 mod q. No division
or invertibility of a+1 modulo q is required. Since q>2, the order modulo q
divides 2p and does not divide p. Because p is prime, its only possibilities
are 2 and 2p; q>a^2-1 excludes order two. Hence

    ord_q(a)=2p,    ord_(a-1)(a)=1,    ord_N(a)=2p.

At the half-order p, a^p is +1 on the a-1 component and -1 on the q component.
Both components are odd, coprime and greater than one. Thus a is a legal good
base for N: the half-order residue is neither +1 nor -1 modulo N and both
standard gcd branches give proper factors (a-1 and q).

Furthermore a-1=3(6m+1) has 3-adic valuation exactly one, and q=1 mod(a-1)
implies 3 does not divide q. Therefore v_3(N)=1. In particular N is not any
nontrivial perfect power, not merely not a prime power. This family survives
the even-number and perfect-power preprocessing routes. q need not be prime;
no theorem on primes in arithmetic progressions is used. As a small symbolic
identity, p=5,m=0 gives a=4, q=205 and N=615, with order ten. This is not a new
numerical BRC execution or a measured TV fixture.

As m tends to infinity, N_m tends to infinity and the default even width

    t_m = 2 ceil(log2 N_m)

tends to infinity. All work orbits in the family have the same order r=2p.
The restriction of the actual instrument to each orbit is the same cyclic
permutation representation up to relabeling, with exactly the same internal
gate bank. The contraction c_(2p) is therefore uniform in m. Applying (14)
with d=p gives the lower limit 1-1/p at these default widths. Section 6 gives
the matching upper bound 1-2/r=1-1/p for every m, proving the exact limit (4).

For every fixed 0<=epsilon<1 choose an odd prime p with 1-1/p>epsilon. Equation
(4) then exceeds epsilon for all sufficiently large members of this fixed-p
family. Hence there is no uniform all-input epsilon<1 TV approximation theorem
for the pinned fixed K33 instrument. This quantifier order is essential:
choose p, then let m grow. It does not claim TV tends to one for a single fixed
input, nor that the conservative bound locates a usable finite counterexample.

## 8. Finite-memory transfer condition and the remaining small-odd cases

The finite feedback window alone is not a proof of TV failure. A finite-memory
instrument can have exact deterministic branches and preserve ideal atoms.
Here strict contraction came from a separate complete-carrier root exclusion.

For a fixed periodically repeated branch cycle of length ell, let

    L = K_(ell-1) ... K_0.

Each K_j is a contraction. If the spectral radius rho(L)<1, then repeated
cycle mass decays exponentially (for any rho(L)<kappa<1, a finite constant
C_kappa gives ||L^n||<=C_kappa kappa^n). Conversely, nondecaying mass on a
repeated cycle requires a unit-modulus eigenvalue of L. A corresponding
eigenvector preserves norm at every intermediate branch. By completeness,
the unselected sibling branch must annihilate the transported vector at each
step. This is an exact simultaneous-kernel condition, not a small phase-error
condition.

An equivalent finite-dimensional contraction certificate is positivity of

    G_D = sum_(j=0)^(D-1) (L^*)^j (I-L^*L) L^j.

For a finite-dimensional contraction, G_D positive definite is equivalent to
absence of a unit-circle invariant component: its kernel consists of vectors
with no norm loss through these D steps, and the Cayley-Hamilton relation then
extends zero loss to all steps. This supplies a possible exact observer target
for d=1 or d=3, where the high-odd argument does not apply. No such transfer
matrix or new observer has been numerically executed in this unit.

The main theorem does not need a proof that nearest-peak bit strings become
periodic; it controls all histories and the whole polynomial-size peak event.
It also does not replace the original-CF theorem by a distributional claim.
Positive useful support, a finite retry bound, small TV, and computational
efficiency are distinct properties. This unit disproves one uniform-TV claim
for this fixed implementation while preserving the already proved support.

## 9. Continuation frontier

The new deliverable is a symbolic theorem and a verified algebraic family,
not an empirical benchmark. The original linear TV upper certificate remains
valid and useful within its stated sufficient range; exceeding that range was
never itself a lower-bound argument. The new obstruction comes from (7)-(14).

Possible next work is a sharper explicit contraction bound from a smaller
certified phase family, or a separate small-odd transfer analysis. Neither is
required for the qualitative obstruction proved here. Any numerical execution
must preserve the ACTUAL_TYPED_BRC_ONLY route and declare a new bounded actual
task; this document introduces no new allowed arithmetic or propagation tool.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
