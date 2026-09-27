# Aligned displacement progressions for one signed bit

Status: SYMBOLIC_DESIGN / SHARED_CONTEXT_AUTHOR_CHECK / NOT_EXECUTED.
This note proves a restricted arithmetic shortcut. It changes no frozen source,
performs no scientific or metadata timing experiment, and asserts neither a new
general complexity class nor formal admission.

The starting identity is the local `DIFFERENCE_AUTOCORRELATION.md`, SHA-256
`c0c3765fce7d07f383f1ebfcb514dd8483485944bfeb202d024dd21e69205cbf`.
Its scalar query is unchanged: integers `g >= 1`, `0 <= k < g`, `R >= 1`,
`0 <= r < R`, physical stride one, and

    L = 2^g, U = 2^k, P = 2U, H = L/P,
    w(x) = (-1)^bit_k(x),  0 <= x < L,
    K(g,k,R,r) = sum_{0 <= x,y < L; y-x = r (mod R)} w(x)w(y).

Here R is a supplied counting modulus, not a free multiplicative-order oracle.
If a later application needs an actual work order or target address, its existing
discovery and verification obligations remain. The coefficient is signed and its
raw Gram normalization, when that external contract applies, remains `4^(-g)`.

## 1. One progression whose step is a multiple of P

For `0 <= d < L`, write `d = qP+s`, `0 <= s < P`, and define

    C(s) = P-4s,       e(s) = s,          0 <= s <= U;
    C(s) = 4s-3P,      e(s) = -3s+2P,    U <= s < P.

The two branches agree at `s=U`. The previously proved finite-interval
autocorrelation is

    A(d) = sum_{0 <= x < L-d} w(x)w(x+d)
         = (H-q) C(s) + e(s).                           (1)

Let `a > 0`, `P | a`, and consider `d_j=b+ja`, `0 <= j < n`, all in
`[0,L)`. Write `b=q0 P+s` and `m=a/P`. Since s is constant along this
progression, `q_j=q0+jm`, so summing (1) gives

    S(b,a,n) = n[(H-q0) C(s)+e(s)]
               - m C(s) n(n-1)/2.                     (2)

This is a linear progression sum, not an approximation or an extension of (1)
outside its finite displacement domain. The exact division by two is valid
because `n(n-1)` is even. In a future typed implementation, the empty case
returns zero before constructing `n-1`; for `n=1` the last term is zero.
Both C(s) and the answer may be negative.

For a nonnegative head b and positive step a, the canonical full progression
inside the domain has length

    n(b,a) = 0,                              b >= L;
             1 + floor((L-1-b)/a),          0 <= b < L. (3)

The empty branch requires neither a floor-moment table nor an artificial
evaluation of A outside its domain. In every nonempty branch, (3) guarantees
`0 <= q_j < H`. Formula (2) uses no recursive floor-moment table at all.

## 2. The half-aligned case U | R but P does not divide R

Then `R/U` is odd and `P | 2R`. Split a canonical progression
`b+jR`, `0 <= j < n`, into its even and odd indices:

    even: head b,     step 2R, count n0 = floor((n+1)/2);
    odd:  head b+R,   step 2R, count n1 = floor(n/2).

The exact sum is

    S_half(b,R,n) = S(b,2R,n0) + S(b+R,2R,n1),        (4)

where a zero-count branch is omitted before any coefficient evaluation.
Each surviving branch satisfies the domain of (2). Computing its length
independently with (3) gives the same result; the parity-count formulas explain
why no original displacement is lost or counted twice. The divisibility is
**P divides 2R**, not the reverse.

Thus, when `U | R`, one orientation uses at most two constant-size scalar
progression evaluations. In the fully aligned subcase `P | R`, it uses one.
One may more generally split into `P/gcd(P,R)` residue classes of j, but that
number is not uniformly small: for odd R it is P. That general splitting is
not a polynomial-in-k shortcut. No such enumeration is proposed here.

## 3. Both displacement orientations and the endpoints

For a canonical residue r, positive and negative displacements give

    K(g,k,R,r) = Sum(head r, step R)
                  + Sum(head R-r, step R),             (5)

with lengths from (3). `Sum` uses (2) if `P | R`, or (4) if only `U | R`.
Consequently there are at most two fully aligned scalar evaluations or four
half-aligned scalar evaluations for the entire modular query. The two terms in
(5) are oriented contributions, not a set of distinct magnitudes.

* At `r=0`, the first head is zero and the second is R. The zero displacement
  occurs once; each strictly positive multiple of R has both orientations.
* If R is even and `r=R/2`, the heads coincide. Both terms remain: the two
  orientations are disjoint pair sets. Deduplicating the heads would be wrong.
* If `R >= L`, each original orientation contains at most one displacement.
  It is still possible that **both** orientations are nonempty, including
  `R=L` and `0<r<L`. Their sum is `A(r)` if `r<L`, plus `A(R-r)` if
  `R-r<L`. At `r=0` this reduces to `A(0)=L`. Only when
  `R >= 2L-1` can the two nonzero orientations never both be nonempty.
* The split in (4) also handles these empty or singleton progressions; it must
  not invent the odd-index branch when n is one.
* For the smallest domain `g=1, k=0`, `L=P=2`, `U=H=1` and
  `A(0)=2`, `A(1)=-1`. Symbolically this gives K=0 for R=1; values
  `(2,-2)` for R=2; and, for `R>=3`, value 2 at r=0, value -1 at
  each of the distinct residues 1 and R-1, and zero elsewhere. These are
  consequences of the two possible displacements, not a new executed test.

Although R>=L needs no alignment for singleton evaluation of (1), this
observation does not authorize silently changing an existing implementation's
dispatch or evidence schema. Such a route would be separately versioned.

## 4. The existing cancellation case R | U

Define the signed residue histogram

    h(c) = sum_{0 <= x < L; x = c (mod R)} w(x).

If `R | U`, each positive U-block and the following negative U-block contain
exactly `U/R` representatives of every residue. There are H such pairs of
blocks, so `h(c)=0` for every c. Equivalently, pairing x with the position
obtained by toggling bit k stays inside [0,L), preserves x modulo R, and
reverses the sign. Therefore

    K(g,k,R,r) = sum_{c mod R} h(c) h(c+r) = 0          (6)

for every residue r. This proves the cancellation without constructing an
R-entry histogram. It is the already available one-window cancellation
special case, not a new discovery. The existing one-window identity
`K=4 J0-T_L` agrees: each sign class has uniform residue count `L/(2R)`,
so `4 J0=T_L=L^2/R`. That identity's pinned note is
`sep27-qft-signedgap/ONE_WINDOW_REDUCTION.md`, SHA-256
`ee13a8d8bc03dd8359f3a3a3d80ac7cfdc9a0094f19deeb2af91189d75a42095`.

The predicates `R | U` and `U | R` have different meanings. The former
is a zero shortcut; the latter supports (2)-(5). At their overlap `R=U`,
the half-aligned formula must also yield zero, because both proofs evaluate
the same finite signed pair sum. Otherwise, neither predicate may be assumed.

## 5. Cost, continuation, and the unchanged boundary

For these special cases, proof of the routing predicate, progression lengths,
Euclidean quotients/remainders, signed coefficients, products, and exact division
by two needs a constant number of scalar integer operations per surviving
progression. No floor-moment tables, internal D-by-D matrices, full label
histograms, or pair enumeration are required by the formula. This is an
arithmetic-operation statement, not a count of primitive BRC digit replays.
Magnitudes and intermediates have `O(g+log(R+1))` bits; even a cancelled
expanded product remains of that bit-size order. Constructing powers of two,
serialization, source checks and retained receipts are also paid work. Existing
fixed-degree moment evaluation was already polynomial in these bit lengths;
this restricted route removes those recursive tables, not an exponential
general-Shor bottleneck.

A prospective implementation must use the actual signed TypedFloorMoments
arithmetic runner for all scientific integer operations and exact divisions,
record branch predicates and every scalar receipt, keep strict canonical
inputs/source binding and replay, and retain signed answers. The old observer
and its successful evidence remain unchanged. A useful bounded comparison would
cover aligned and half-aligned interior bits, `R=U`, an empty orientation,
`r=0`, `r=R/2`, `R>=L`, and `g=1`, with one independently typed pair
comparator only where a fresh answer is needed. It must report actual digit
cost rather than infer speed from the absence of moment tables. No such
implementation or execution has been performed for this note.

This is a one-negative-bit, stride-one scalar coefficient only. It does not
reorder any native word, erase residual coordinates, change an actual feedback
history, establish a common root, solve arbitrary sign masks/multiple-gap
convolution, or make order/address discovery free. In particular it is not a
full QFT or Shor dequantization result.

Global-Knowledge-Sync: main@f8aa9c8 / GLOBAL_KNOWLEDGE_V1
