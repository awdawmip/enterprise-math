# Weighted odd-part structure: a real fast path and its limits

Status: **AUTHOR_SYMBOLIC_RESULT / SHARED_CONTEXT / NOT_ADMITTED**.
This unit contains proofs and an implementation specification, not new
scientific execution. It preserves the actual finite native phase words,
their original order, the initial carrier vector and every residual entry.
The parent supplied a current shipped-helper PASS under canonical GK
`06788df022dbd11720132b4ed0882ce8e41b3b8a`; no new external query or remote
write was made. Previous packages remain immutable.

The useful result is an exact contraction when an actual history has a
long leading zero block. Its cost depends on the remaining history length,
not on the number of odd-order residues, after paying to discover and
certify the period and target address. An actual-family full-rank example
and an actual finite-word noncommutation calculation delimit two broader
compression claims. Neither is a lower bound against all algorithms.

## 1. Consumed sources and exact observable

The prior `sep27-qft-carry-execution/aggregation_theory/` sources are:

* `PERIOD_AGGREGATION.md`, SHA256
  `be20eb9409b1b250edfe9e0bc83fda9701253a71add4f98e3ccea8325d2302be`;
* `period_aggregator.py`, SHA256
  `6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c`.

The existing two-carry executor has SHA256
`f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810`.
Its coefficient contraction is reused, not reproved as a new algorithm.
The actual-family facts below were checked against the frozen general
direct constructor, SHA256
`830b2f0c0c206a53e2b349fe377976d369ebfb76d4dfc5aad494db88ab6e0c63`,
its note, SHA256
`d1876c86c1a2c5c940bdfa7ce3e4f9d8377c46f46b1bc4a2bfdfbe58ff8e34ba`,
the saved `M3_DELTA_EIGHTH.summary.json`, and the source `FixedRotor` and
`QuarterTurn` definitions. The full61-to-six-coordinate word-boundary
codec note has SHA256
`833f04c7eb953f4c0a2b3f6486c2aabb4ff867bf1f67c216d87b5eb61555708a`.
That codec is an exact reachable-subspace encoding. It is not permission
to erase arbitrary residuals or truncate inside a native word.

Fix a real execution history h of length i, let L=2^i, and let
b=a^(2^(t-i)) mod N be the corresponding actual unit shift. At time j,
write O_j=(-1)^(h_j) T_j, with T_j the full actual feedback word. For the
binary expansion n=sum_j n_j 2^(i-1-j), set

    U_h(n) = O_(i-1)^n_(i-1) ... O_0^n_0 e0,
    v_h(w) = 2^-i sum_(b^n=w, 0<=n<L) U_h(n),
    C_h(d) = 4^-i sum_(0<=n,n+d<L) U_h(n) U_h(n+d)^T.

These are vectors, not full operator columns averaged over a mixed seed.
The seed is e0 e0^T. At a target unit z, the relative Gram matrix is

    Gamma_h(z) = sum_w v_h(w) v_h(zw)^T.                       (1)

If a certified exact order R=ord_N(b) and address 0<=r<R with b^r=z have
been obtained, then

    Gamma_h(b^r)
      = 4^-i sum_(0<=n,m<L, m-n=r mod R) U_h(n) U_h(m)^T.       (2)

The address orientation is m-n=r, not its negative. This is the complete
matrix observer used below, so a later trace or branch-mass observer can
use all signed carrier correlations. R and r are analysis parameters
until an actual discovery and verification procedure supplies them.

## 2. Generating functions preserve chronology but do not remove q states

Define the formal vector polynomial

    F_h(x) = sum_(n=0)^(L-1) U_h(n) x^n
           = (I+x O_(i-1))(I+x^2 O_(i-2)) ...
             (I+x^(2^(i-1)) O_0) e0.                         (3)

The scalar indeterminate commutes with the matrices; the matrices have
not been reordered. For an odd certified period q, (2) is exactly

    Gamma_h(b^r) = 4^-i [x^r]_(mod x^q-1)
                         F_h(x^-1) F_h(x)^T.                 (4)

A q-point roots-of-unity transform is a change of basis of the same q
cyclic residues. By itself it requires q evaluations, not poly(log q)
work. The short expression (3) is a polynomial circuit of exponentially
large degree; extracting a specified remainder coefficient is the
unsolved operation, not a free consequence of that short description.
Maintaining the q folded coefficient vectors is ordinary q-address
propagation in new coordinates. Neither device is claimed as a new
large-odd-part compression. Roots of unity here are a proof notation;
no new spectral evaluator or numerical ideal reference is introduced.

## 3. Leading-zero contraction, including a general even period

Suppose h_0=...=h_(K-1)=0, with 0<=K<=i. Put

    ell=i-K,  P=2^ell,  H=2^K.

Every O_j in the first K rounds is exactly I: no earlier nonzero readout
activates feedback and its own sign is positive. Later feedback depends
on h, not on the preparation bits n_j. Consequently, for n=P A+x,

    U_h(P A+x)=V(x),  0<=A<H, 0<=x<P,                       (5)

where V(x) is the original ordered suffix of ell actual O_j acting on
e0. It contains the full residual vectors and all signs after the zero
block. No commutation is used. Define

    C_tail(d) = 4^-ell sum_(0<=x,x+d<P) V(x) V(x+d)^T.

This is exactly the existing coefficient observer on the shortened
history (h_K,...,h_(i-1)), using the same admitted phase bank and carrier.
Indeed an active old control c=K+c' at time K+j uses phase index
(K+j)-(K+c')+1=j-c'+1, in the same temporal control order. Old controls
c<K are zero. Only the coefficient executor may be shortened this way:
the original depth-i modular shift, certified period and target must
remain those of the original program. A new shorter program's modular
power table is not a replacement for them.

Write the actually certified order as R=2^s q, q odd, and set

    g=gcd(P,R)=2^min(ell,s),  M=R/g,  A0=P/g.

For every integer d with |d|<P:

* If g does not divide r-d, let W_d=0.
* Otherwise, when M>1, compute the unique residue

      rho_d = A0^(-1) ((r-d)/g) mod M,  0<=rho_d<M.

  This inverse exists since gcd(A0,M)=1. For M=1 define rho_d=0.

For H=v M+u, 0<=u<M, define the nonnegative integer

    Count(H,M,rho) = M v^2+2vu
                  + max(0,u-rho)+max(0,u-(M-rho)).            (6)

Then the exact contraction is

    Gamma_h(b^r) = 4^-K sum_(|d|<P) W_d C_tail(d),
    W_d = Count(H,M,rho_d) on the divisible cases.            (7)

Proof. Write n=P A+x and m=P B+y. Then d=y-x and the congruence in
(2) is P(B-A)+d=r mod R. Divisibility by g is necessary; after division
by g, the remaining condition is B-A=rho_d mod M. Among A in [0,H),
each residue has v representatives, with one additional representative
in residues [0,u). The inner product of this count vector with its
rho-shift is M v^2+2vu plus the cyclic interval overlap. That overlap
has exactly the two terms in (6). At rho=0 its second term is zero,
so the interval is not double counted. The independent sum over x,y
is 4^ell C_tail(d); combining it with the raw 4^-i gives 4^-K in (7).

This proof uses ordinary integer identities symbolically. An implementation
must still obtain the divisibility, inverse, quotient, residues, products
and signed complete-matrix sums through the actual admitted arithmetic.
The large positive integer weights multiply all entries, including
negative entries; they do not justify replacing signed matrices by norms.

### Raw normalization and boundaries

If a suffix coefficient is stored as an integer matrix B_d divided by
2^(e_d), choose E=max_d e_d over nonzero terms. A raw representation of
(7) is

    numerator = sum_d W_d 2^(E-e_d) B_d,
    denominator = 2^(E+2K).                                (8)

Reduction by common powers of two is optional canonicalization, not
normalization of the branch. The factor 4^-K must not be dropped and
the weights must not be divided by H or H^2 a second time. A matrix sum
helper which already divides by four requires compensating for that
operation explicitly; it is not an unscaled sum helper.

If ell=0, only d=0 remains and C_tail(0)=e0e0^T. If K=0, H=1 and (6)
selects rho=0, so (7) is the old full-length coefficient sum with no
gain. If M=1, v=H,u=0 and Count=H^2; the divisibility condition remains
essential when g>1. In particular q=1 does not permit discarding g.
Negative d uses the existing transpose C_tail(-d)=C_tail(d)^T, while
its own weight is computed from r-d. The two weights need not coincide.
Depth zero, zero matrices, and zero-probability histories are valid raw
identities; conditioning on the last class is not an available sampler.

### Cost and information acquisition

There are at most 2P-1 displacement terms, or P native coefficient
contractions using transposes, each of depth ell. Thus after period and
target discovery the coefficient part costs O(2^ell ell) full-matrix
carry layers instead of O(q i) residue layers or all long aliases.
Each layer still pays the actual feedback word applications, full D
entries, observers and rational bit lengths. Coefficients have weights
at most H^2, adding at most 2K numerator bits before summation. One
inverse and the O(P) integer index/weight operations also have a real
typed cost. This is useful when ell is small; it does not assert that
ell is small for a typical sampled history.

Individual coefficients can in principle be accumulated one at a time.
An implementation that retains all terms instead uses O(2^ell D^2)
matrix slots in addition to native temporaries and receipts. The current
leading-zero implementation does retain its terms; the two-carry
routine's small boundary is not a claim of constant total storage.

The former O(R) complete-cycle discovery remains a valid paid input
source. The new small-odd-part discovery, if actually certified, can
be another source. Neither turns a large unknown q or a target discrete
log into free input. Any obtained period/return information is also
available to a classical order/factor postprocessor on the same input.
The advantage sought here is a complete native correlation query or
reuse across histories, not a factoring advantage from hiding that cost.

## 4. Applicability mass and an actual high-coherence history

For a leading zero block of length K, its work base is b^P and its
order is exactly M=R/g. Its raw probability has no residual cancellation,
since all its O_j are I. With H=vM+u,

    Pr(0^K) = Count(H,M,0)/H^2
            = (M v^2+2vu+u)/H^2
            = 1/M + u(M-u)/(M H^2).                         (9)

If H<M this is exactly 1/H. Only when H is much larger than M is the
usual approximately 1/M description justified. In particular, for
large M and long K this special set has small probability. There is
no rejection/resampling-until-zero step and no claim that a low-mass
fast path makes the entire sampler efficient.

A further actual-family check illustrates why norm-only near-uniform
claims fail on some histories. Let h=0^i, L=2^i, and let the current
order q be odd. Write L=vq+u and gamma_r=Count(L,q,r)/L^2. Then

    Gamma_h(b^r)=gamma_r e0e0^T,
    M_h=gamma_0>=1/q,
    0<=gamma_0-gamma_r<=q/(2L^2).                            (10)

The next feedback is still I. Its actual next modular shift p squares
to b. In an odd-order portion of the original orbit, p=b^((q+1)/2).
For this r the conditional bit's TV distance from a fair bit is
gamma_r/(2 gamma_0), hence at least

    1/2 - q^2/(4L^2).                                      (11)

The nontrivial regime is L much larger than q. This is a single actual
conditional history with probability gamma_0, typically about 1/q.
It is not a lower bound on whole-sampler TV, not an average-time lower
bound, and not a no-go theorem for other samplers. The odd-order
qualification is necessary: near a two-primary suffix the next shift
can be outside the subgroup generated by b and the collision is zero.

## 5. The actual weighted cyclic rank can already be q

Take the same real finite-family history h=0^i and any odd q>1. Consider
the scalar q-by-q cyclic correlation matrix K_(e,f)=gamma_(f-e), with
gamma defined above. Its cyclic eigenvalues are

    4^-i |sum_(n=0)^(L-1) zeta^(k n)|^2,  0<=k<q,           (12)

where zeta is a primitive q-th root in this proof only. The k=0 sum is
L. For k nonzero, zeta^k has an odd order dividing q, and cannot have
its L-th power equal to one because L is a power of two. The geometric
sum is therefore also nonzero. Consequently rank(K)=q exactly.

This uses the actual all-identity feedback history and pure initial
seed e0; it is not a worst-case arbitrary orthogonal gate construction.
Even a one-dimensional weighted vector sequence can induce full cyclic
correlation rank. Thus a uniformly small exact cyclic-rank factorization
cannot be inferred merely from a small carrier or from actual Shor
feedback scheduling.

At the same time, (6) evaluates every individual gamma_r with a short
integer formula. This is an explicit warning against converting rank
q into a general computational lower bound. Structured coefficient
evaluation may be cheap while a full cyclic matrix has maximal rank.
The favorable structure in Section 3 uses precisely that distinction.

## 6. A conditional short-realization criterion and its bit-cost caveat

One possible route beyond a zero block is a certified rational realization

    U_h(n)=B A^n c,   0<=n<L,                               (13)

of dimension k. A concrete sufficient condition, checkable against actual
native actions without enumerating n, is

    Bc=e0,   O_j B = B A^(2^(i-1-j)) for every j.            (14)

Multiplying these identities in the original time order proves (13).
Global commutativity of the O_j is unnecessary, but (14) does force
commuting actions on the invariant image of B. Discovering B,A,c,
checking (14), and controlling their exact rational bit sizes all cost
work; this is not an assumed interface of the current phase bank.

For a certified period q, write L=vq+u and S_m(X)=sum_(j=0)^(m-1) X^j.
The folded coefficient at residue e is

    F_e=B A^e S_(v+1[e<u])(A^q)c,   0<=e<q.                (15)

In sum_e F_e F_(e+r mod q)^T, partition the e interval at the constant
number of endpoints where either multiplicity changes or e+r wraps.
On each subinterval e=l+j, both multiplicities and the wrap flag are
fixed. Its contribution is B times

    sum_(j=0)^(d-1) A^j x y^T (A^j)^T                      (16)

times B^T, for explicitly known x,y. Simultaneous matrix power/sum
doubling computes (15) and (16) in O(poly(k,D) log L) arithmetic
operations without assuming an inverse of I-A or I-A^q. Finally
multiply by 4^-i. Thus a small certified realization with bounded
intermediate bit sizes would yield a genuine short contraction.

Here the displayed logarithmic count assumes q<=L. For a uniform
statement it can be replaced by log(L+q); when q>L, zero-multiplicity
intervals may instead be skipped before constructing unused A^q powers.

The qualification on bits is indispensable. Even a fixed rational A
can give A^q denominator length proportional to q. Logarithmically
many matrix multiplications do not make those products polynomial in
log q. A proposed application must bound every materialized integer
length and the actual native observation cost, or replace the products
by another justified representation. Neither such a general certificate
nor a general construction of (13) is established here.

## 7. A frozen actual word rules out the naive common-root certificate

The exact quarter word Q acts as

    Q e0=-e1,  Q e1=e0,  Q c=c on the residual coordinates.

The frozen direct m=3, tolerance 1/8 word is exactly

    W=D0(2zz^T-I),
    z=alpha e0+beta e1+c,
    (alpha,beta,c)=(15136,6269,3,95,3,166)/16384,
    D0=diag(1,-1,...,-1).                                  (17)

These integers are taken from the previously executed construction,
whose full 61 columns and canonical native word were already checked.
No new commutator experiment or ideal trigonometric reference is used.
Direct symbolic expansion gives

    (QW-WQ)e0 = 2||c||^2 e1 - 2(alpha+beta)c != 0.          (18)

In particular W is not simply a root of Q on a common invariant
carrier containing e0. The scheduled readout pattern (1,0,0) uses
O_0=-I, O_1=Q and O_2=W. It cannot satisfy (14): powers of the same A
would imply QW e0=WQ e0. The contradiction concerns this actual finite
word family, not arbitrary orthogonal matrices. It is unnecessary to
assume this pattern is nonzero for every modular input; the structural
claim that the bank provides a universal common-root identity is
already false.

This does not exclude every higher-dimensional finite realization,
noninvariant encoding, history-specific cancellation, approximate
method or other algorithm. It excludes importing ideal phase powers,
or Stage89/90 power merging, into the new direct-word family without
new exact structural certificates. Full signed chronology is still
required in Sections 3 and 6.

## 8. Clarification of the older two-projection membership check

The frozen prior discussion overstated one reason for retaining a final
target check. Suppose z and b are units modulo N, R=2^s q with q odd,
and the *same* integer r has exact projected equalities

    z^(2^s)=b^(r 2^s),  z^q=b^(r q).                        (19)

In the abelian unit group let x=z b^(-r). Then x^(2^s)=x^q=1.
Bezout coefficients for gcd(2^s,q)=1 give x=1, hence z=b^r. Cyclicity
of the ambient unit group is not needed. Therefore a final exact
b^r=z comparison is logically redundant if both precise equalities
in (19), all unit premises and their common-r binding are already
certified. It remains useful as an executable cross-check against
address reconstruction or certificate-binding errors. This clarification
does not edit the frozen proof or remove the current executed check.

## 9. Exact next bounded step

Implement only the leading-zero observer (7) as an optional route:

1. Bind the original program, complete history, source, target, period
   and carrier admission; strictly verify the first K bits are zero.
2. Pay for fresh typed period/address certification and preserve it in
   the evidence. Compute g,M,A0, divisibility, inverse, weights and all
   matrix-entry products through the existing admitted typed observers.
3. Run the existing coefficient executor on the shortened history with
   the same bank and carrier. Keep the original modular target. Apply
   (8) without conditioning or dropping residual coordinates.
4. Compare complete signed matrices with the previous author-run verified period
   aggregator on a few bounded cases: K=0, ell=0, M=1 with g>1, odd q,
   r=0, a wrap/negative displacement, and an early-one K=0 case with no
   promised acceleration. A dispatcher may choose the old route there;
   the formula itself remains valid.
5. Report coefficient depth/actions, integer lengths, observer receipts,
   discovery/address work, and the exact applicability mass (9).
   Give a classical comparator with the same discovered period data.

This note supplies a proved, parameter-dependent compression of actual
weighted correlations and two precise limits on tempting extensions.
General large-odd-middle simulation remains open; more partition colors,
renaming an FFT, or ignoring period discovery does not close it.
