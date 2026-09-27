# Period concatenation for non-top two-bit correlations

Status: SYMBOLIC / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.
This note uses only source reading and algebra. There is no numerical example,
host scientific evaluation, scientific import, native run, query or remote write.
All previously executed sources and evidence remain unchanged.

## 1. Contract and exact source pins

Let 0<=ell<k<g, V=2^ell, U=2^k, P=2U, L=2^g=HP, and

    w(x)=(-1)^(bit_ell(x)+bit_k(x)).

The sequence has period P. For length L define the scalar overlap

    A_L(d)=sum_(0<=x<L-d) w(x)w(x+d),  0<=d<L.

Let A_P be the same overlap on one period, explicitly extended by A_P(P)=0
for the empty overlap. No evaluator for a nonempty interval is called at P.
The supplied-modulus query uses two displacement heads r and R-r (head R
for the second orientation when r=0), each truncated by d<L. Coincident
half-modulus heads retain multiplicity. The original normalization is 4^-g.
Neither R nor a modular target address is obtained for free by these formulas.

Read completely for this derivation:

- `../sep27-qft-two-bit-top-general/TOP_BIT_GENERAL_MODULUS.md`,
  `880fb9d90f9258e0b96f6f47281bd711b11bd2ec515bddb6a6212cf45266ee89`.
- Its `guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md`,
  `e5f31e9619a3233c65af23b642d262e98996d6ca9ee538910e38c21ba412aaab`.
- `../sep27-qft-two-bit/TWO_BIT_PERIOD_NESTING.md`,
  `9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26`.

The available scalar arithmetic backend remains the frozen degree-three
single-floor implementation `typed_floor_moments.py`,
`633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`.
Reading its prior exact contract is not a claim of executing this new reduction.

## 2. The concatenation identity is exact

For d=qP+s, 0<=s<P and d<L, the proposed identity is

    A_L(d)=(H-q)A_P(s)+(H-q-1)A_P(P-s).                  (1)

Proof: the integrand w(x)w(x+d)=w(x)w(x+s) has period P. Its full-period
sum is A_P(s)+A_P(P-s): the nonwrapped range 0<=x<P-s contributes A_P(s),
while x=P-s,...,P-1 gives A_P(P-s) after exchanging the two scalar factors.
There are H-q-1 complete periods followed by a prefix of length P-s, since

    L-d=(H-q-1)P+(P-s).

The prefix is exactly A_P(s). Adding the complete periods proves (1).
This proof is not a noncommutative matrix identity: the wrapped scalar term
was reversed. A matrix-valued analogue would require an explicit orientation
or transpose contract and is not asserted here.

At s=0 the second overlap is A_P(P)=0, and (1) counts H-q complete periods.
At the last period q=H-1 its second coefficient is zero, leaving only the
actual partial overlap. At s=U the two equal half-period overlaps retain
their two coefficients. At d=L the algebra gives zero if A_L(L) is explicitly
defined as an empty sum; this does not extend a nonempty evaluator's domain.
No d>L value is required or asserted.

Thus period concatenation removes enumeration of the H copies **pointwise**.
It does not immediately make a progression of wrapped residues into the
unwrapped progression accepted by the top-bit evaluator.

## 3. A ten-value sufficient progression contract

The concatenation formula can be collected more tightly than the previous
fourteen-value sufficient interface. This is a smaller sufficient list, not
a claim that its entries are linearly independent or algebraically minimal.

Put M=P/V, an even integer. For a displacement d define

    q=floor(d/P), delta=floor((d+U)/P)-q in {0,1},
    Z=floor(d/V), t=d-VZ, E=(-1)^Z,
    J0=E(V-2t), J1=Z J0-E t.                            (2)

Here Z is the global compressed displacement. Its within-period value is
z=Z-Mq. The parity is unchanged because M is even.

To derive the new formula, first consider the compressed *single*-high-bit
overlap B on length HM. Apply (1) to its period M. If C=H-q, its within-period
affine pieces are

    B(Mq+z)=CM+(1-4C)z,                    0<=z<=M/2,
    B(Mq+z)=M(2-3C)+(4C-3)z,              M/2<=z<=M.     (3)

Both pieces agree at M/2. The upper extension at z=M is (C-1)M, exactly the
next period's value at zero; at the last period it is the empty endpoint zero.
Consequently B(Z) and B(Z+1) can use the same reached affine piece, including
an endpoint, when applying the stretch formula. Writing that piece as beta+alpha*z,

    A_L(d)=beta J0+alpha(z J0-Et)
          =(beta-alpha Mq)J0+alpha J1.

Substitute the two choices in (3), selected by delta. The result is

    A_L(d)=M[H+(4H-2)q-4q^2
                +delta(2-4H+(8-8H)q+8q^2)]J0
             +[1-4H+4q+delta(8H-4-8q)]J1.               (4)

For example, this derivation handles a stretch crossing z=M-1 to z=M by the
proved endpoint continuation in (3), not by wrapping and resetting the overlap
length. No cancellation of a residual matrix coordinate is involved.

For any one canonical progression d_j=b+Rj, 0<=j<n and d_j<L, it suffices to
return these ten integer sums:

    X_(a,e)=sum q^a delta^e J0,  a=0,1,2; e=0,1,
    Y_(a,e)=sum q^a delta^e J1,  a=0,1;   e=0,1.         (5)

The progression result then equals

    M[H X00+(4H-2)X10-4X20
         +(2-4H)X01+(8-8H)X11+8X21]
       +(1-4H)Y00+4Y10+(8H-4)Y01-8Y11.                 (6)

The coefficients and exact integer sums remain signed. The second index in
(5)-(6) denotes indicator exponent, not a second displacement index.

## 4. Which part is covered by the current single-floor API?

Let p=2V and introduce the fine quotients and power differences

    Q=floor(d/p), Qplus=floor((d+V)/p),
    Delta_m=Qplus^m-Q^m.

Then the two lower kernels in (2) have the single-floor identities

    J0=V-2d+2pQ+4d Delta_1-2p Delta_2,                  (7)

    3J1=-3d-12dQ+12pQ^2+6pQ
                    +12d Delta_2-8p Delta_3+2p Delta_1. (8)

For verification, write eta=Qplus-Q, Z=2Q+eta and
t=d-pQ-Veta. Use eta^2=eta and the exact identities

    Q eta=(Delta_2-Delta_1)/2,
    Q^2 eta=(2Delta_3-3Delta_2+Delta_1)/6.

Substitution in J0 and J1 gives (7)-(8). Their terms have total fine degree
at most two and three respectively, and are at most linear in d. The factor
three in (8) is to be divided only after combining the exact integer numerator.
There is no assumption that isolated thirds are integers.

Thus X00 and Y00 in (5) are available from two existing fine-floor tables on
the progression, using offsets b and b+V. But (6) also multiplies these lower
kernels by q, q^2 and the coarse indicator delta. Replacing q^a delta by
neighboring coarse-floor power differences removes a same-scale product; it
does not remove products of a coarse floor with a fine floor.

One sufficient remaining contract is the other eight combinations in (5):
X10, X20, X01, X11, X21, Y10, Y01 and Y11. After expansion a uniform sufficient
interface is a subset of the mixed moments

    sum_(j=0)^(n-1) j^u
        floor((Rj+b+epsilon U)/P)^a
        floor((Rj+b+zeta V)/p)^c,

    epsilon,zeta in {0,1}, u<=1, a<=3, c<=3,
    u+a+c<=5.                                          (9)

For X terms the coarse degree is at most three and fine total degree at most
two; for Y terms the corresponding bounds are two and three. Individual terms
such as a coarse quotient times a fine squared quotient expose the missing
joint information. Their presence in this expansion is not a proof that no
other cancellation can eliminate them, or that they must be evaluated separately.

The current API returns moments of *one* floor of an affine argument. Separate
coarse and fine marginal tables do not by themselves return (9). Although
q=floor(Q/(P/p)), expressing this dependence as a nested floor does not supply
a costed recurrence for the required products. Some nested floors can flatten;
this note does not declare nesting irreducible.

Therefore (1) and (4) have not established a fixed number of existing
degree-three single-floor calls for arbitrary R and non-top k. They give an
exact smaller sufficient interface and a precise unresolved step. A proof of
such an evaluator would need a descending recurrence, bounded state count and
coefficient growth, or an explicit algebraic elimination. No impossibility or
literature-priority claim is made.

## 5. A closed special case without period enumeration

If P divides R, let a=R/P. For a nonempty progression write b=q0 P+s. Then s
is fixed and q=q0+aj. With canonical count

    n=1+floor((L-1-b)/R),

formula (1) sums directly to

    [n(H-q0)-a n(n-1)/2] A_P(s)
      +[n(H-q0-1)-a n(n-1)/2] A_P(P-s).                (10)

The half-product is exact. At s=0 the second overlap is an explicit empty
zero, and a head b>=L is handled as an empty orientation before using (10).
The two period overlaps have constant-size point formulas from the top-bit
source. This requires no floor-moment table, scan of H, or scan of P/p.
In a future executable version P|R and all quotients, lengths, coefficients
and exact halves would be paid typed work. This family is already a subset
of V|R, so (10) is an alternative constructive simplification, not a new
general input-family breakthrough or an executed speedup.

For unrestricted R, splitting the j progression until its period residues
repeat can require P/gcd(P,R) branches. Splitting low remainders can require
V/gcd(V,R) branches. Those can be exponential in explicit bit indices; neither
is hidden inside a polynomial complexity assertion here. The ten-value list
is constant in size but its generic mixed evaluator is still unproved.

## 6. Bounded outcome and continuation

The candidate concatenation formula is proved with all overlap endpoints.
The stronger point collection (4) reduces the previous sufficient interface
from fourteen sums to ten and identifies eight residual mixed combinations
beyond two directly available fine-floor sums. It does not eliminate the
coarse/fine product requirement. Formula (10) closes a concrete period-aligned
special case with constant-size typed arithmetic in a future implementation.

The next mathematical question is whether the particular linear combination
(6), rather than an unnecessarily universal mixed-moment backend, has a
single-floor reduction or a polynomial-size simultaneous recurrence. All
claims remain scalar and conditional on supplied R/address data. This does
not settle growing Walsh masks, chronological matrix products, or Shor sampling.

Global-Knowledge-Sync: main@604893e / GLOBAL_KNOWLEDGE_V1
