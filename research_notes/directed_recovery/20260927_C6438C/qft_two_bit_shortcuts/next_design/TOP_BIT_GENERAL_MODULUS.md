# Highest selected bit: arbitrary-modulus two-bit scalar reduction

Status: new symbolic derivation; no code or scientific execution in this unit.
The supplied counting modulus R is arbitrary and positive. This reduction does
not require 2^ell to divide R. It uses only the already implemented family of
single-floor moments of total degree at most three. It is a family extension,
not a complete Shor dequantization or a newly claimed general counting theorem.

## 1. Setup and exact point formula

Let g>=2, 0<=ell<g-1, L=2^g, V=2^ell, M=L/V and k=g-1.
Let w(x)=(-1)^(bit_ell(x)+bit_(g-1)(x)) for 0<=x<L, and

    A(d)=sum_(0<=x<L-d) w(x)*w(x+d),  0<=d<L.

The frozen stretch identity gives, for d=Vz+t, 0<=t<V,

    A(d)=(-1)^z * [(V-t) B(z) - t B(z+1)],             (1)

where B is the highest-bit autocorrelation on length M, with B(M)=0:

    B(z)=M-3z  for 0<=z<=M/2;
    B(z)=z-M   for M/2<=z<=M.

At the shared endpoint M/2 both formulas agree. If d<L/2, then z<M/2
and both z and z+1 are in the lower formula (possibly at its endpoint).
If d>=L/2, then both are in the upper formula (possibly z+1=M).
Substitution of t=d-Vz proves the following polynomial form:

    A(d)=(-1)^z F_low(d,z),  d<L/2,
    A(d)=(-1)^z F_high(d,z), d>=L/2,

    F_low = VM + (3-2M)d + (2VM-6V)z + 6dz - 6Vz^2;
    F_high = -VM + (2M-1)d + (2V-2VM)z - 2dz + 2Vz^2. (2)

No assumption on R has been used. The split at d=L/2 belongs to the upper
formula. Using the low polynomial above that split is not justified when t>0.

## 2. Remove parity using two neighboring floor tables

Write P=2V and, for each displacement d,

    q=floor(d/P), qplus=floor((d+V)/P), e=qplus-q.

Then e is either zero or one, z=floor(d/V)=2q+e, and (-1)^z=1-2e.
For either polynomial in (2), write

    F(d,z)=a0+a1*d+(b0+b1*d)z+c*z^2,
    D(d)=b0+b1*d,
    F0(d,q)=a0+a1*d+2D(d)q+4c*q^2.

Expansion using e^2=e yields

    (1-2e) F(d,2q+e)
      = F0(d,q) + e[-2F0(d,q)-D(d)-4c*q-c].           (3)

Thus the only parity-weighted monomials needed are e, q*e, q^2*e,
d*e and d*q*e. Let Delta_j=qplus^j-q^j. Since qplus=q+e,

    e       = Delta_1,
    q*e     = (Delta_2-Delta_1)/2,
    q^2*e   = Delta_3/3-Delta_2/2+Delta_1/6.           (4)

These are pointwise identities, including e=0 and q=0. Multiplying the first
two by d gives the remaining required monomials. Hence the point sum of (3)
is a rational linear combination of ordinary single-floor moments for q
and qplus. There is no product of two independently varying floor functions.
Denominators divide six; the total is an integer. An implementation can multiply
the whole formula by six and perform one certified exact division at the end,
or retain separately certified exact versions of the identities in (4).

The coefficients for the two pieces are, in order (a0,a1,b0,b1,c):

    low:  (VM, 3-2M, 2VM-6V, 6, -6V);
    high: (-VM, 2M-1, 2V-2VM, -2, 2V).              (5)

## 3. At most eight top-level single-floor tables per residue

For any head b>=0 and step R>0, let n be the number of terms b+Rj<L.
If b>=L then n=0. Otherwise

    n=1+floor((L-1-b)/R).

Let m be the number of those terms below L/2. If b>=L/2 then m=0;
otherwise

    m=min(n, 1+floor((L/2-1-b)/R)).

The low segment has head b and count m. The high segment has head b+Rm
and count n-m. A zero-count segment is omitted without evaluating a nonempty
out-of-domain table. Within either segment, set d=b_segment+Rj and use two
moment tables with denominator P, slope R, and offsets b_segment and
b_segment+V. All required terms have the form

    sum_(0<=j<count) j^u floor((Rj+offset)/P)^v,
    u+v<=3.

For example d*q^2 requires u=1,v=2; the cubic difference needs u=0,v=3.
The tables also supply their v=0 polynomial terms. Four top-level tables
suffice for one orientation, and eight for the two orientations below.
This is a bound on top-level calls, not a bound on recursive work or digit cost.

The signed residue count is

    K(R,r)=sum_(d<L; d congruent r mod R) A(d)
           +sum_(d<L; d congruent -r mod R; d>0) A(d).

For 0<=r<R use heads b=r and b=R-r when r>0; use heads 0 and R when r=0.
Coincident heads at r=R/2 retain multiplicity two. This is the same scalar
pair count whether y-x or x-y is used, by exchanging x and y. Original raw
normalization remains 4^-g. R is supplied; this does not discover an order.

## 4. Complexity, evidence boundary and next action

All parameters above have O(g+log(R+1)) bits. With the existing exact
fixed-degree Euclidean single-floor moment procedure, the reduction gives
a polynomial-bit algorithm for this highest-selected-bit two-sign family
at arbitrary R. It requires neither residue enumeration nor the general
fixed-dimensional lattice-counting backend. This is a symbolic composition
bound; no new implementation cost, elapsed-time gain or executed unaligned
answer is asserted.

The immediate existing aligned shortcut implementation must remain frozen
within its declared admission domain. A subsequent distinct implementation
can admit all R for k=g-1, retain typed segment counts, coefficients, exact
divisions and both orientations, and run a predeclared bounded unaligned
comparison against an actual typed pair comparator. New coverage must include
ell>0, nonalignment, both sides of L/2, nonzero t, empty segments, half-modulus
multiplicity, r=0 and R>L. Its certificate schema and negative controls must
make all new branch choices and paid failures observable.

The source stretch proof is TWO_BIT_PERIOD_NESTING.md, SHA-256
9189f01243aa308f516534337b40e6e2c03a7fcf3f79a7dde179a5689bca1d26,
published in EM 55e8e66b76d062c6c72432f0f5b364c3e9b1bba8 under
research_notes/directed_recovery/20260927_C6438C/qft_gap_hybrid/next_design/.
The endpoint identity is also restated and reviewed in STRUCTURAL_SHORTCUTS.md
(845df9a8a9e67862f197412d2bd8a20fdc10aedf14db73efc59f70ca97cfda7f)
and its review (133d81d27860bc108075a8b995ec42644d37834c3824caaacfc6c22b30f946ab),
now published at EM 20b5ef9e9146039863963bc039d2a163ac99f4a5 under
research_notes/directed_recovery/20260927_C6438C/qft_two_bit_aligned/next_design/.
The reusable floor source is typed_floor_moments.py, SHA-256
633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2,
at EM c0f04346c520fddc8016c86227b3b6cc2e9f30f6 under
research_notes/directed_recovery/20260927_C6438C/qft_adaptive/nonzero_structure/.

This note uses pure symbolic algebra and existing proof/source records. It
makes no new literature-priority claim or professional-query claim. Matrix
weights, order/address discovery, growing masks and full sampling remain open.

Global-Knowledge-Sync: main@9f0e65b / GLOBAL_KNOWLEDGE_V1
