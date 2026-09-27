# Exact active-window contraction for nonzero histories

Status: **AUTHOR_SYMBOLIC_RESULT / SHARED_CONTEXT / NOT_ADMITTED**.
No scientific execution, new professional query, or remote write is part
of this unit. The current parent supplied the canonical `06788df...` helper
PASS. This directory is new; previous source, evidence and notes remain
frozen. The result is a sufficient-condition algorithm, not a general
polynomial-time Shor simulation theorem.

The new step beyond leading-zero counting is to eliminate a long *trailing*
identity interval as well. The remaining modular weights are evaluated by
a fixed-degree Euclidean floor-moment recursion, rather than enumerating
that interval, the long prefix, or all odd-period residues. Nonzero and
noncommuting native words inside the active window remain exact.

## 1. Source boundary and actual sufficient condition

This note consumes the previous
`sep27-qft-oddpart/weighted_structure/WEIGHTED_ODD_PART_STRUCTURE.md`, SHA256
`c37976fc412d60af9fd29244205446cbcc0d830d4cbfc9fa6fdaa1f01f645187`.
Its relative-Gram orientation, complete pure seed, raw scaling and paid
order/address premises are retained. It does not consume an ideal-QFT
propagator or replace native residuals by ideal phases.

For an actual history h of length i, let O_j=(-1)^(h_j)T_j in the original
chronological order and

    U(n)=O_(i-1)^n_(i-1) ... O_0^n_0 e0,
    n=sum_j n_j 2^(i-1-j).

Assume i=K+ell+B and the actual full-carrier identities

    O_j=I for j<K and for j>=K+ell.                         (1)

These identities require a structural full-word proof or complete native
column certificate. A small ideal target angle, a small residual norm,
or zero readout bits alone after an earlier one is insufficient. A weaker
reachable-subspace identity would need a separately proved invariant
subspace; this note uses the simple full-carrier premise (1).

All matrices use the complete original carrier D, or its previously
verified exact word-boundary codec. Nothing is truncated inside a word.
The ell active operators need not commute, repeat, or have a common root.

Let P=2^ell, H=2^K and V=2^B. Every preparation address has a unique form

    n=VP A+V x+y,  0<=A<H, 0<=x<P, 0<=y<V.

Premise (1) gives the exact vector identity

    U(VP A+Vx+y)=W(x),
    W(x)=O_(K+ell-1)^x_(ell-1) ... O_K^x_0 e0.              (2)

Define the existing signed coefficient observable on this window,

    C_win(d)=4^-ell sum_(0<=x,x+d<P) W(x) W(x+d)^T.         (3)

Its chronological operators must be the original ones. In the concrete
leading-zero plus finite-feedback-window application below, the existing
shortened-history carry executor supplies exactly (3). A generic operator
window may instead need an explicit gate-list adapter; blindly resetting
history indices is not part of this theorem.

## 2. Exact weighted contraction

Suppose an actual discovery/verifier has supplied R=ord_N(b) and
0<=r<R with b^r=z, where b=a^(2^(t-i)) mod N is the original depth-i
unit shift. As before,

    Gamma_h(z)=4^-i sum_(m-n=r mod R) U(n)U(m)^T.           (4)

For d in (-P,P), put t_d=r-Vd, S=VP, and define

    J_d = sum_(Delta=1-H)^(H-1) (H-|Delta|)
                      Count(V,R,(t_d-S Delta) mod R),      (5)

where Count is the previous exact interval-pair count. Namely, if
V=vR+u with 0<=u<R and 0<=rho<R,

    Count(V,R,rho)=Rv^2+2vu
                  +max(0,u-rho)+max(0,u-(R-rho)).           (6)

Then

    Gamma_h(z)=4^-(K+B) sum_(|d|<P) J_d C_win(d).           (7)

Proof. For two addresses let Delta=A'-A, d=x'-x and e=y'-y.
Their difference is S Delta+Vd+e. For fixed Delta there are H-|Delta|
choices of A,A'. The remaining modular condition on y,y' is exactly
e=t_d-S Delta mod R, counted by (6). This scalar count depends on d,
not on the individual x,x'. Their full native outer-product sum is
4^ell C_win(d). Multiplying by 4^-i proves (7). This groups whole
identical-vector contributions; it neither changes word order nor drops
cross terms or signed residual entries.

The apparent long sum (5) is the new issue. It is not necessary to
enumerate its 2H-1 terms: Sections 3--4 evaluate it in O(log(R+1))
fixed-degree arithmetic stages. No factorization of R is needed for
that scalar evaluation, so even and odd periods are treated uniformly.

## 3. The modular triangle is a difference of floor polynomials

For any signed integer x, let

    k=floor(x/R),  k_-=floor((x-u)/R),  k_+=floor((x+u)/R).

Set rho=x-Rk, so 0<=rho<R. Since 0<=u<R, both k-k_- and k_+-k are
zero or one. Direct expansion gives

    max(0,u-rho)
      =(u-x)(k-k_-)
        +(R/2)[(k^2+k)-(k_-^2+k_-)],                      (8)

    max(0,rho+u-R)
      =(x+u-R)(k_+-k)
        -(R/2)[(k_+^2-k_+)-(k^2-k)].                      (9)

If the corresponding floor difference is zero, the expression is zero.
If it is one, (8) reduces to u-rho and (9) to rho+u-R. The equality
boundaries have value zero, so no endpoint convention is missing. These
identities also hold at u=0, when both expressions vanish, and for
negative x with genuine floor division rather than truncation toward zero.

For an affine x=aj+b, (8)--(9), multiplied by a linear weight in j,
need only the moments

    F_(p,e)(n;m,a,b)=sum_(j=0)^(n-1) j^p floor((aj+b)/m)^e,
    p,e>=0,  p+e<=3.                                     (10)

There are ten such moments, including the four elementary e=0 sums.
Rational halves in (8)--(9) cancel to exact integers. An implementation
can double the expressions and perform an exact final division, while
retaining every signed intermediate through admitted integer arithmetic.

Finally split the symmetric sum in (5) as

    J_d = sum_(j=0)^(H-1)(H-j)
              [Count(V,R,(t_d-Sj) mod R)
               +Count(V,R,(t_d+Sj) mod R)]
          -H Count(V,R,t_d mod R).                       (11)

This uses two affine moment problems with slopes -S and S, and one
ordinary Count evaluation. The subtraction removes the twice-counted
Delta=0. It does not subtract a physical probability or approximate an
amplitude. The constant part of Count contributes exactly
H^2(Rv^2+2vu), providing a normalization check.

## 4. Self-contained Euclidean moment recursion

The moment family (10) is closed under an elementary lattice-count
recursion. This section supplies the algorithm rather than appealing
to an unimplemented generic floor-sum oracle.

Let n>=0,m>=1 and a,b be signed integers. Write their Euclidean divisions

    a=A m+a0,  b=B0 m+b0,  0<=a0,b0<m.

Then floor((aj+b)/m)=Aj+B0+floor((a0j+b0)/m). Expand the e-th power
by the binomial theorem. Multiplication by j^p produces only moments
whose total degree remains at most p+e. Thus a,b can first be normalized
using signed exact integer arithmetic. The case e=0 is a power sum;
the case n=0 is zero. If a0=0, all remaining positive-e normalized
moments are zero.

For the remaining normalized problem 0<a<m, 0<=b<m, put

    Y=floor((a(n-1)+b)/m).

If Y=0 the positive-e moments are zero. Otherwise let

    P_p(x)=sum_(j=0)^(x-1)j^p,
    J_y=ceil((my-b)/a)=floor((my-b+a-1)/a).

For 1<=y<=Y, the condition floor((aj+b)/m)>=y is equivalent to
j>=J_y. Using f^e=sum_(y=1)^f [y^e-(y-1)^e], interchange two finite
sums to obtain

    F_(p,e)(n;m,a,b)
      = P_p(n) Y^e
        -sum_(z=0)^(Y-1) [(z+1)^e-z^e]
            P_p(floor((m z+m-b+a-1)/a)).                  (12)

For p+e<=3 and e>=1, P_p has degree p+1 and the first bracket has
degree e-1. Expanding their product therefore asks only for moments
of total degree <=(p+1)+(e-1)<=3, now with parameters

    (n',m',a',b')=(Y,a,m,m-b+a-1).                        (13)

All ten moments use the same next geometry (13); they can be evaluated
together. After the next coefficient normalization, the modulus pair
follows the ordinary Euclidean descent m -> a -> m mod a. Consequently
there are O(log(m+1)) recursion levels, each with a constant number of
fixed-degree integer/rational operations. One must not independently
expand an uncached recursion tree for each moment and then claim the
simultaneous bound.

For explicit implementation, the only required power-sum polynomials
inside (12) are

    P_0(x)=x,
    P_1(x)=x(x-1)/2,
    P_2(x)=x(x-1)(2x-1)/6.

The e=0 base cases also use P_3(x)=[x(x-1)/2]^2. Their integer-valued
denominators are fixed constants; no growing-degree interpolation or
spectral arithmetic is hidden in the recurrence. The convention 0^0=1
is used only for the p=0 summand in (10).

### Bit lengths and actual arithmetic boundary

In this application n=H, |a|=S and |b|=|r-Vd| or a shift by u.
Every original affine value has O(i+log(R+1)) bits. The Euclidean
recursion reduces its modulus and finite summation range. Fixed-degree
power sums, moments and coefficient products consequently have
polynomial bit length in i+log(R+1); the recursion never materializes
R residues or an integer with 2^i bits. A conservative polynomial
bit-cost claim is sufficient here; counting log R arithmetic stages
alone is not substituted for bit complexity.

No actual new floor-moment executor has been run in this unit. A native
implementation must derive Euclidean quotients/remainders, signed
normalization, fixed polynomial products, and exact divisions from the
admitted arithmetic and retain its receipts. Ordinary Python floor
division in a future numerical checker would not by itself establish
that source correspondence.

## 5. Complete contraction cost and raw representation

At most P nonnegative coefficient contractions plus transposes supply
all 2P-1 signed C_win(d). The latter's weights must still be evaluated
separately because J_d and J_-d need not coincide for a fixed r.
Each coefficient uses ell chronological two-carry layers. Thus, after
paid order/target acquisition, the costs are

    O(2^ell ell) actual full-matrix carry layers,
    O(2^ell log(R+1)) fixed-degree integer moment stages.   (14)

Actual gate actions, D^2 matrix entries, observer calls, exact rational
word denominators and integer lengths multiply these stage counts.
The scalar weights satisfy 0<=J_d<=H^2 V^2, since they count ordered
pairs of the free coordinates. Their bit lengths are at most 2(K+B)+1.

If C_win(d)=B_d/2^(e_d), E=max e_d, the final raw representation is

    sum_d J_d 2^(E-e_d) B_d / 2^(E+2K+2B).                (15)

This is not a normalized branch state. No H,V or their squares should
be divided out again. Weighted summation can stream one coefficient
at a time; retaining all coefficients uses O(2^ell D^2) storage. Native
temporaries, proof traces and output receipts remain additional costs.

Discovery remains separate. The current paid odd-part method can use
Theta(q) modular steps before any contraction, and target address work
must also be charged. A short coefficient computation after receiving
that information is not a solution to discovering a general large q.
The same order information is available to the classical order/factor
baseline; the possible benefit is native full-distribution/correlation
evaluation after that common cost.

## 6. Actual nonzero histories that satisfy the premise

The frozen `phases/closed_phase_bank.py`, SHA256
`16b2bd768fcd89c50971ab8ddf06c81af562a7f4608373ff497f294d5ce6e6ed`,
contains `IdentityTail`: the empty native word on the entire retained
carrier. Its `truncated_tail_bank` assigns that word to m>=cutoff.
This is an explicit changed phase bank, not equality with the original
untruncated bank. Its word-prefix precision and error certificate must
remain the ones actually associated with it.

More generally suppose a concrete verified bank has W_m=I for every
m>J, and all nonzero readout positions of h lie from f through l.
Then every O_j before f is I. Every j>=l+J also has h_j=0 and each
earlier one c activates only an identity phase: j-c+1>J. Hence (1)
holds with

    K=f,
    ell=min(i,l+J)-f,
    B=i-K-ell.                                           (16)

For example, one isolated nonzero readout can activate only J consecutive
O_j, even if i is much larger. A cluster of width w gives ell<=w+J-1.
Those actual words can be noncommuting and create nonzero residuals;
they are all retained in (3). The old leading-zero contraction would
still enumerate the long suffix of length i-f. The new method instead
depends exponentially only on the active width in (16), and handles
the remaining trailing interval through (11)--(12).

For the existing identity tail starting at m=33, J=32. This is a
concrete exact finite-word application, but does not inherit a uniform
small ideal-Shor TV error for all t. The earlier fixed-cutoff error
and obstruction results still apply. A cutoff growing with t and a
proper error budget is a different bank and must have its own complete
word/error certificate. The symbolic schedule in
`DRIVER_SCHEDULE_COROLLARY.md`, SHA256
`a04de6a209f272009db5504f05c3bf3ceab28d34b2d0df2285294593d4e8cecb`,
explains that distinction; this note implements neither that scheduler
nor any new phase bank.

The general direct-word bank used in the preceding execution package
must not be silently replaced by this fixed-grid tail bank. It does
not come with a finite-feedback-window identity. Even an isolated one
can activate a new nonidentity actual word at every later phase index.
Its small ideal angles do not certify (1). Likewise a newer Stage80
low-precision result cannot be transplanted to the direct-word family
without matching actual source and operator certificates.

Nothing here proves that typical histories contain a short cluster.
Widely separated nonzero readouts can make the single enclosing active
window almost all of h. Multiple active windows might permit a richer
contraction, but replacing them by independent scalar counts would
generally discard their modular and signed correlations; that further
step is not proved here.

## 7. Boundaries, a falsifiable next step, and what remains open

If B=0, V=1 and Count(1,R,rho) is the indicator rho=0. Formula (7)
reduces to the previous leading-zero result. The floor recursion is a
more general evaluator of the same integer counts, not a second source
of normalization. If K=0, H=1 and (11) leaves one Count, giving a
trailing-identity contraction. If R=1, u=0 and Count=V^2, so J_d=H^2V^2
and the free-interval scale in (7) cancels exactly. An empty active
window gives the all-zero history's interval correlation; the general
formula remains valid though its special direct Count is cheaper.

No primality, factorization, oddness, or coprimality of R with V is
required by the moment evaluation. This is a useful difference from
an inverse-based interval reduction. Negative t_d and the distinction
between mathematical floor and truncation toward zero are essential.

The next bounded implementation should first implement simultaneous
moments of total degree <=3 through admitted signed integer observers.
Verify its finite identities with small signed a,b and exact divisions,
then verify (11) against complete typed pair counts. Only then connect
it to complete native C_win(d) and compare full signed Gamma matrices
against the existing paid aggregator on one actual nonzero finite-tail
history, including a noncommuting active word and nonzero residuals.
Also include K=0, B=0, R=1, even R, negative t_d and a failed identity
premise. Bind the actual bank; do not validate using a numerical ideal
phase propagation.

This supplies an explicit new exact compression parameter, the width
of the actual nonidentity window, with an implementable poly-bit scalar
counting algorithm. It does not supply such a short window for general
Shor histories, nor remove the paid large-odd-part/order-discovery gap.
