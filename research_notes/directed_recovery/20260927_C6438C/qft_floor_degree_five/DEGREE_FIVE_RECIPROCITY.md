# Closing the single-floor moment family through degree five

Status: SYMBOLIC / SHARED_CONTEXT / NOT_EXECUTED / NOT_ADMITTED.
This note generalizes the exact recurrence implemented by the frozen
degree-three source typed_floor_moments.py,
633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2.
It supplies a prospective single-floor backend for the degree-five terms in
PERIOD_EXTENSION.md, 97d2011a41a2f0a8416151955daa4b08f448ab38336b9214e29d8a5208bbd3b6.
It does not eliminate the remaining mixed-floor products.

## Contract

For strict integers n>=0,m>=1 and signed a,b, return all

    F[p,e](n,m,a,b) = sum_(0<=j<n) j^p floor((a*j+b)/m)^e,
    p,e>=0, p+e<=D, D<=5.

Use the usual polynomial convention x^0=1, including at x=0. There are at
most 21 returned moments. The family is finite in degree, not in input size.
No host pow/mod/gcd, floating arithmetic or ordinary numerical reference is
needed by a future actual typed implementation. All parameter divisions,
coefficient evaluations, powers and exact polynomial divisions remain paid.

Let S_p(t)=sum_(0<=j<t) j^p. The required exact polynomials are

    S0(t) = t,
    2 S1(t) = t^2-t,
    6 S2(t) = 2t^3-3t^2+t,
    4 S3(t) = t^4-2t^3+t^2,
    30 S4(t) = 6t^5-15t^4+10t^3-t,
    12 S5(t) = 2t^6-6t^5+5t^4-t^2.                    (1)

Each polynomial vanishes at zero and its forward difference at t equals
t^p, as follows by binomial expansion, so (1) is an identity for every
nonnegative integer t. Use its combined integer numerator and exact division;
do not divide individual monomials by the displayed denominator. Degree-six
typed powers are needed only to construct S5, not as a returned floor exponent.

## Signed normalization

Use Euclidean division a=A*m+a0 and b=B*m+b0, with 0<=a0,b0<m.
Put f_j=floor((a0*j+b0)/m). Then floor((a*j+b)/m)=A*j+B+f_j.
For each p+e<=D,

    F[p,e](n,m,a,b)
      = sum_(k=0)^e sum_(l=0)^(e-k)
          binom(e,k) binom(e-k,l) A^l B^(e-k-l)
          F[p+l,k](n,m,a0,b0).                        (2)

Every child index obeys p+l+k<=p+e<=D. Formula (2) holds for signed A,B.
Skip a coefficient term only when its zero follows from an observed zero
A or B with a positive corresponding exponent; 0^0 remains one. Such a
skip is an omission justified by a source-bound observed value, not a fake
executed multiplication. The unoptimized full formula is correct as well.

If n=0 every sum is zero. If a0=0 and b0<m, every positive-e normalized
moment is zero. The e=0 moments are always S_p(n).

## Transposition with preserved degree

Assume 0<a<m and 0<=b<m, n>0. Let

    Y = floor((a*(n-1)+b)/m).

If Y=0 all positive-e moments are zero. Otherwise for y=0,...,Y-1 define

    T_y = ceil((m*(y+1)-b)/a)
        = floor((m*y + m-b+a-1)/a).

For each input j, write f_j^e as the telescoping sum of
(y+1)^e-y^e over 0<=y<f_j. The condition y<f_j is exactly j>=T_y.
Interchanging these finite sums gives

    F[p,e](n,m,a,b)
      = Y^e S_p(n)
        - sum_(0<=y<Y) ((y+1)^e-y^e) S_p(T_y), e>=1. (3)

The child is the same floor-moment family at parameters

    (Y, a, m, m-b+a-1).                               (4)

If d_p S_p(t)=sum_h c[p,h] t^h is the corresponding numerator from (1),
binomial expansion makes (3) an explicit integer recurrence:

    d_p F[p,e]
      = d_p Y^e S_p(n)
        - sum_(v=0)^(e-1) binom(e,v)
            sum_(h=1)^(p+1) c[p,h] F[v,h](child).      (5)

The output is the exact quotient of the combined right side by d_p.
Every required child satisfies v+h <= (e-1)+(p+1)=p+e<=D.
The highest needed S_p in a positive-e transposition has p<=D-1, so
its child floor exponent h never exceeds D. There is no hidden degree growth.

This recovers the existing degree-three recurrence and extends it to five
without a new scientific assumption. Negative offsets/slopes are handled by
(2) before the normalized transposition, not by an unsupported signed-height
argument in (3).

## Termination and cost statement

A normalization step retains denominator m but makes a,b canonical. It does
not recurse into another unchanged normalization: the normalized child next
uses a base case or transposition. A nontrivial transposition changes the
denominator from m to a, where 0<a<m. The following normalization reduces
the old m modulo a. Thus alternating nontrivial steps follow the Euclidean
remainder sequence and have logarithmic depth in the original integer scale.
There is only one distinct recursive parameter child per node; all at most
21 moments are reconstructed together. Fixed-degree coefficient arrays and
the finitely many terms in (2)/(5) do not branch into independent recursion
trees. Cache reuse may reduce work but is not needed for this bound.

Integer magnitudes retain polynomial bit length: the input affine floor has
bit length bounded by the input lengths of n,m,a,b, and fixed powers/products
increase it only by a degree-dependent constant factor. Euclidean child
parameters and their affine offsets likewise have polynomial bit length.
Therefore a standard actual typed integer implementation of these finite
recurrences has polynomial bit cost in the input description for fixed D<=5.
Constructing scales, rational numerators, exact divisions, validation and
failure/replay evidence is still paid. The current degree-three API has not
magically gained the extra moments just because the recurrence is proved.

## Continuation and limits

A future separately versioned runner can retain the existing signed
arithmetic and native source binding while replacing only the moment family
and recurrence. It must record degree, normalized/transposed child, complete
integer traces, exact divisions and all returned moments; fresh verification
must bind these to the source. Use declared new degree-four/five examples
with actual typed finite sums and preserve all rejected/failed work. Do not
rerun historical degree-three experiments merely for publication.

This closes one finite-degree *single-floor* tool requirement. Products of
distinct coarse/fine floors remain outside its contract; a mixed transposition
that returns to its original parameter state still needs a descending
argument. No mixed closure, measured speedup, literature-first claim, unknown
order discovery, matrix correlation or full Shor dequantization is asserted.

Global-Knowledge-Sync: main@106dd75 / GLOBAL_KNOWLEDGE_V1
