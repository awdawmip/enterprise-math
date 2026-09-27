# General two-bit scalar sums via bounded lattice counting

Status: symbolic reduction by the root author; no new scientific execution and
no implementation of a lattice-counting primitive. This note advances the
complexity assessment of the scalar subproblem. It does not claim a new
general lattice-counting theorem, a practical speedup, or Shor dequantization.

## 1. Exact interface inherited from the two-bit proof

The frozen `TWO_BIT_PERIOD_NESTING.md`, SHA-256
`9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26`,
reduces one oriented displacement sum to a fixed linear combination of moments

    G = sum_(j=0)^(n-1) j^u
        floor((Rj+b+epsilon U)/P)^alpha
        floor((Rj+b+zeta V)/p)^beta,

where n,b are nonnegative integers, R,P,p are positive, U,V are nonnegative,
epsilon,zeta belong to {0,1}, u belongs to {0,1}, alpha,beta are at most three,
and u+alpha+beta<=5. In the application P=2U, p=2V and p divides P.
No divisibility of R by V is needed for the following reduction. In fact the
reduction only uses the nonnegativity and the fixed degree bounds, not p|P.

The former note correctly identifies a missing *implemented* mixed-floor
interface. It does not prove an impossibility statement. We can supply an
external-theorem-based polynomial bit-complexity route without constructing
the missing Euclidean recurrence. The distinction matters: existence of this
route does not make the present typed evaluator support it.

## 2. A three-coordinate floor graph

If n=0, G=0. Otherwise define the bounded rational polytope Q in real
coordinates (j,a,c) by the following six closed inequalities:

    0 <= j <= n-1,
    P*a <= R*j+b+epsilon*U <= P*a+P-1,
    p*c <= R*j+b+zeta*V <= p*c+p-1.

The integer points have exactly one (a,c) for each integer j in [0,n-1].
This is because for integer arguments, the interval [P*a,P*a+P-1] specifies
floor division by P, and similarly for p. The right endpoints must be P-1
and p-1; replacing them by P and p double-counts boundary values.

Thus G equals sum j^u*a^alpha*c^beta over Q intersected with Z^3. Each integer
a,c is nonnegative. The polytope is bounded even before integrality: j lies in
a finite interval and each remaining coordinate lies in an affine interval
of finite width. Lower-dimensional and empty polytopes cause no change to the
integer-point statement.

## 3. Remove weights by a finite-dimensional box lift

Introduce u auxiliary coordinates s_i, alpha coordinates t_i, and beta
coordinates v_i. For each existing coordinate impose respectively

    0 <= s_i <= j-1,
    0 <= t_i <= a-1,
    0 <= v_i <= c-1.

Call the resulting polytope Q_hat. For a fixed integer (j,a,c), the number of
auxiliary integer choices is exactly j^u*a^alpha*c^beta. A positive exponent
at a zero base gives an empty interval and therefore zero choices. An exponent
of zero introduces no coordinate and contributes one, including at base zero.
These are Cartesian products, so multiplicities multiply rather than add.

Consequently

    G = #(Q_hat intersect Z^(3+u+alpha+beta)).             (A)

Its ambient dimension is at most eight; it has at most sixteen inequalities.
All dimensions and inequality counts here are fixed independently of n, R,
g and the bit positions. Auxiliary coordinates are bounded by the bounded
base coordinates, so Q_hat is bounded. Formula (A) introduces no loop over
j, residues, the ratio P/p, or a large interval of lattice points.

This is an unweighted counting reduction. It requires neither a numerical
derivative nor a root-of-unity or floating-point evaluation from our code.
It is not a newly admitted BRC primitive.

## 4. Precise external theorem and complexity consequence

The primary source read for this note is Barvinok and Woods,
*Short rational generating functions for lattice point problems*,
[arXiv:math/0211146v1](https://arxiv.org/pdf/math/0211146v1).
Theorem 3.1 gives polynomial-time short generating functions in fixed
dimension. Theorem 2.6 and its following remark permit evaluation at all ones
for a finite set, including cancellation of poles in individual terms.
Together they give exact lattice-point counts for a bounded rational polytope
in fixed dimension. Theorem 3.1 cites the earlier Barvinok-Pommersheim theorem;
that earlier proof has not been separately retrieved here.

The rest of this section is our application of those results. Let B be the
binary encoding length of n,R,b,P,p,U,V, with fixed exponents/offset flags.
The inequalities above have O(B) total encoding length: forming b+epsilon U,
b+zeta V and subtracting one increases bit length by at most a constant over
the maximum participating input length. There are only finitely many allowed
triples (u,alpha,beta) and two offset flags. Applying fixed-dimension counting
to (A) therefore evaluates every needed G in time polynomial in B. The
polynomial's degree and constants are not asserted to be practically small.

The output length is also controlled. For n>=1 set

    Amax = floor((R*(n-1)+b+epsilon*U)/P),
    Cmax = floor((R*(n-1)+b+zeta*V)/p).

Then 0<=G<=n*max(1,n-1)^u*max(1,Amax)^alpha*max(1,Cmax)^beta.
With fixed degree, the logarithm of this bound is O(B). This is a symbolic
bound, not a host computation or a recorded typed arithmetic execution.

Combining these finitely many moments using the frozen two-bit identities
gives a classical polynomial-bit algorithm, based on the cited theorem, for
the *single supplied-modulus scalar coefficient* at arbitrary R. Both oriented
progressions must still be assembled with their exact multiplicity; r=0
includes displacement zero only once and a half-modulus residue may have two
equal nonzero heads. Empty orientations have zero contribution. The original
raw factor stays 4^-g. For binary R and L=2^g the relevant input length is
O(g+log(R+1)); coefficient construction and output bit length are polynomial
in that quantity.

This closes an abstract complexity route for this scalar family. It does not
close the implementation or certificate gap in the current typed code. The
former note's missing recurrence remains missing; this note bypasses it by a
different established algorithm, with a larger fixed dimension.

## 5. An independent fixed-sparsity reduction

There is also a direct counting formulation that avoids the moment expansion.
Let S be a set of h bit positions in [0,g), L=2^g, and

    w_S(x)=(-1)^(sum_(k in S) bit_k(x)),
    K_S=sum_(0<=x,y<L; x-y congruent r mod R) w_S(x)*w_S(y).

The earlier observer writes y-x congruent r instead. Exchanging x and y is a
bijection with the same symmetric product w_S(x)*w_S(y), so these definitions
give the same scalar K_S. This does not assert such symmetry for arbitrary
outside matrix factors.

Fix one assignment e_x,k,e_y,k in {0,1} for all k in S. There are 4^h
assignments. Use integer variables x,z and a_x,k,a_y,k, substituting

    y = x-r-R*z.

Impose 0<=x<=L-1, 0<=x-r-R*z<=L-1 and, for every k in S, with T_k=2^k,

    e_x,k*T_k <= x-2*T_k*a_x,k <= (e_x,k+1)*T_k-1,
    e_y,k*T_k <= x-r-R*z-2*T_k*a_y,k <= (e_y,k+1)*T_k-1.

Every permitted integer pair (x,y) in this assignment has exactly one z and
one quotient for each bit constraint. Conversely each integer point yields
one permitted pair with precisely those bits. No quotient parity ambiguity
or pair multiplicity remains. All real coordinates are bounded: x,y are
bounded, R>0 bounds z, and each quotient is in a finite-width interval.

Let C_e denote this polytope's integer-point count. Then

    K_S = sum_e (-1)^(sum_k(e_x,k+e_y,k)) C_e.           (B)

Its dimension is 2+2h. For each *fixed* h, (B) is a constant number of
fixed-dimension counts with polynomial-size coefficients. Hence it supplies
another polynomial-bit existence result for every fixed sparse Walsh mask.
For h=2 it uses sixteen counts in dimension six, with no alignment condition.
This may be a preferable backend interface to the degree-five box lift, but
no practical comparison has been run.

If h grows with g, neither 4^h nor the fixed-dimension theorem is a uniform
polynomial bound. We do not infer a lower bound or an impossibility result
from that failure. The direct construction makes the relevant unresolved
parameter explicit: supporting arbitrary masks with growing h needs an
additional compression argument.

## 6. What this does and does not deliver to the research program

The exact, newly recorded content is the reduction (A), its input/output-size
argument, and the alternative explicit pair bijection (B). The algorithmic
counting theorem is established literature, and novelty of these applications
has not been searched or claimed. The source was read as a specific primary
paper; it is not a new paid professional-query result or provider cache hit.
No existing query ID/budget/status is changed by this reading.

Current executable work remains the separately versioned V|R two-bit adapter.
The general case requires a source-versioned backend that constructs and
certifies the count, with all scientific integer operations on the approved
actual typed route. A call to a host polytope package would not constitute
the authorized BRC experiment. To execute this route, design the exact
certificate, map its primitive operations, bound retained output, and review
the source before any new run. Merely producing inequalities is not an
evaluated certificate.

Neither (A) nor (B) finds R or a target address; those are supplied parameters.
Neither treats a history-dependent matrix product as a scalar Walsh weight.
Neither bounds the number of full Gram queries or preserves a complete
quantum sampling distribution by itself. They are therefore concrete scalar
complexity progress, not a full Shor/QFT dequantization claim.

Global-Knowledge-Sync: main@a3609ca / GLOBAL_KNOWLEDGE_V1
