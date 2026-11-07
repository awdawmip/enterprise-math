# R620 | Frozen signed BRC: valuation and complete X6 closed-source spectrum

Date: 2026-11-08. AUTHOR / UNREVIEWED / NOT_ADMITTED.

## Exact scientific input and stated observer

Frozen R462: 18783e01e3646c72b7aab3b16d3f565e83e6446f,
source research_notes/r388_signed_k3_corank16_20261029_emr3/r388_exact.py
(Git blob 7fa7a762f758b30c6090468ac43487daa34abad8), theta=0.
This is the original signed K/J to B to D auxiliary BRC recursion, with
B_0=1+t. For any *single* B_0-terminal ordered K-source word
w=(i_1,...,i_m), 1<=i_a<=12, define
s(w)=sum i_a, m=|w|, W(w)=product K_{i_a}(t), P(w)=(1+t)W(w).
Let nu_t be the least exponent with a nonzero integer coefficient.

We retain the R619 *declared experimental* map from the twelve labels
to P000 X6 pure Cell-torsor coordinate steps:
sigma(2j-1)=+e_j, sigma(2j)=-e_j, j=1,...,6.
Its endpoint is z(w)=sum sigma(i_a). A word with z=0 is termed a
coordinate-closed word under this explicit map. This map is a mathematical
path decoration of native six-axis adjacency, not an established native
weighted joint-field update or heartbeat-time trajectory.
The original signed K weights and ordered provenance are unchanged.

## Theorem A: all twelve signed K-leading coefficients are nonzero

The exact frozen formula is
K_i(t)=t^(i-1) sum_{j=1}^4 [-d_j(i)](1+t)^(i+1-j),
d=(-C(4,i)+C(2,i-1), C(5,i-1)-C(5,i-2),
   C(7,i-2), -C(9,i-3)),
omitting terms with negative exponents, and with out-of-range binomials
set to zero. Evaluation at t=0 after factoring t^(i-1) yields
alpha=(2,-1,-8,-11,6,53,106,119,83,36,9,1).
Each entry is nonzero, hence for EVERY ordered source word:

  nu_t(W(w)) = s(w)-|w|,
  [t^(s-|w|)] W(w) = product alpha_{i_a} != 0,
  nu_t(P(w)) = s(w)-|w|.

Proof: the lowest nonzero coefficient of a product of nonzero integer
polynomials is the product of their nonzero lowest coefficients.
The unit-constant B_0=1+t preserves the valuation. This also proves
[P(w)] mod t^(d+1)=0 iff s-|w|>d for d>=0. If its jet is nonzero,
the first nonzero degree together with s recovers the word length.

At a fixed positive level s, words of length m number
N(s,m)=[x^s](x+...+x^12)^m
=sum_{k>=0}(-1)^k C(m,k)C(s-12k-1,m-1),
where out-of-range binomials are zero. Their possible valuations are
exactly 0,...,s-ceil(s/12), since m ranges from ceil(s/12) to s.
This classification is per word; sums over sources can undergo further
signed cancellation.

## Theorem B: exact closed-source valuation semigroup

If z(w)=0 under the declared sigma, the counts of positive and negative
labels for every axis j are equal. Write this common count r_j>=0.
Define R=sum_j r_j and h=sum_j(j-1)r_j. Then exactly

  s=sum_j (4j-1)r_j = 3R+4h,
  |w|=2R,
  v=nu_t(W)=sum_j(4j-3)r_j = R+4h.

Thus 3v-s=8h is a nonnegative multiple of 8, and s/3<=v<=21s/23.
The following is a NECESSARY AND SUFFICIENT condition for the existence
of a coordinate-closed B_0-terminal source word of level s and valuation v
for any integers s,v>=0:

  R=(s-v)/2 is a nonnegative integer,
  h=(3v-s)/8 is a nonnegative integer,
  0<=h<=5R.

For sufficiency, express h as a sum of R digits in {0,1,2,3,4,5}
(possible for all 0<=h<=5R). Let r_j count the digit j-1 and form any
ordering with r_j copies of each pair (2j-1,2j). Then the endpoint is
zero, the level is 3R+4h=s, and the valuation is R+4h=v.
Necessity follows by collecting the exact source counts. For fixed r,
the number of distinct ordered words is (2R)! / product_j (r_j!)^2,
and their (nonzero) leading signed coefficient is
product_j(alpha_{2j-1}alpha_{2j})^r_j.

COROLLARY: every level-s coordinate-closed word has valuation >=s/3,
so all jet observations of degree d<ceil(s/3) are zero. At s=3n
(n>=1), equality v=n is achieved exactly when r_1=n and all other
r_j=0, giving C(2n,n) distinct ordered words of leading
coefficient (-2)^n. This is an unbounded exact observer blind zone.

## Theorem C: fully classified level-21 closed source fiber

For s=21, the criterion has only v=7 or v=15. All possibilities:

  r=(7,0,0,0,0,0): v=7, 3432 words, signed leader -128
  r=(0,3,0,0,0,0): v=15, 20 words, leader 681472
  r=(1,1,1,0,0,0): v=15, 720 words, leader -55968
  r=(2,0,0,1,0,0): v=15, 180 words, leader 50456

Therefore exactly 4352 ordered coordinate-closed sources exist at level
21. All have zero low-order scalar jets through d=6; at d=7 exactly
3432 first become nonzero, whereas the other 920 first become nonzero
at d=15. Different ordered words within the same branch counts retain
identical commutative scalar W: distinguishability is group-level only.

For all n>=1, w_A=(1,2)^(7n) and w_B=(3,4)^(3n)
have endpoint zero and level 21n but valuations 7n and 15n.
In the exact R619 observer (endpoint,level,W mod t^(d+1)) and under
arbitrary future K-word appends, they are equivalent for d<7n and
first separate at d=7n. Future multiplication cannot lower valuation.

## Verification and next unit

Executable R620_VERIFY.js recomputes the *original* frozen twelve
signed BRC K branches with BigInt, checks all 22621 words of length
0..4 by independent polynomial multiplication, compares the
integer-semigroup criterion against six-pair unbounded recurrence for
all 32761 (s,v) pairs in [0,180]^2, enumerates the exact level-21
source counts and checks n=1..5 of the infinite separating family.
Its result is R620_EVIDENCE.json and passes with marker
R620_EXACT_VALUATION_CLOSED_FIBER_PASS. The unlimited-scope statements
are proved by the algebra above, not inferred from finite tests.

Next: read the actual X6 packet field/joint observer and legal update
interfaces, and test whether any available weighted native evolution
realizes sigma plus the signed K-source semantics. Until this bridge is
proven, use the result as an exact auxiliary BRC / path-decorated
six-axis calculation. Preserve P000, ACTIVE worldview and R462 pin.
