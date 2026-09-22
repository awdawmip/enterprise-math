# POWER feedback VII: exact sparse-support identifiability and gcd closure

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`
Researcher-ID: `EM-DIRECT-16243626C61A`
Session: `local-power-review-16243626C61A` (existing local continuation key, not server authentication)
Progress-Event-ID: `power-sparse-identifiability-20260922-16243626C61A`
Status: `PROVED_SCOPED_DERIVATIONS_AND_BOUNDED_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`
Control/source read: `awdawmip/enterprise-math@88a7bf00ea111fc05a77a2ee3345101d2a2aad44`.

## 1. Selected question and exact observation lease

Continue the previous sparse-weight residual: when do the retained exponent positions
still identify a period, rather than merely detect some collisions? The previous affine
result assumes a FULL interval; it is not a theorem for monotone weights just on sparse marks.

Fix a finite nonempty support S={s_1<...<s_k} contained in [0,H]. Let a be a modular unit
with unknown order r. All weights w_i>0 are exact integer multiplicities on S; every
unlisted position has weight zero. Define

    K_r(w) = sum_u (sum_{i:a^(s_i)=u} w_i)^2
           = sum_i w_i^2 + 2 sum_{i<j, r | (s_j-s_i)} w_i*w_j.

The observer family is ALL such collision masses for this fixed S, or equivalently the
full labeled equality partition on these positions. It is not arbitrary access to numerical
residue properties, new exponent probes, characters, physical measurements, or noisy masses.
The hypothesis family is every abstract period 1..H plus a single above-H class. Some of
these periods may be inadmissible in a PARTICULAR ambient group; extra verified ambient
information can narrow the prior and is outside the necessity claim below.

This is a finite T0 positive-mass / T4 collision / T6 observer-fiber specialization.
The source `group_ring_affine_character.py` was executed unchanged as the full-interval
reference (blob 61adb8c7ed2d610dbd924871e35c3e315c927c06); the existing bounded compiler
`group_ring_batch_response.py` (82c87f779a07b84de601d54ebd04d3bfb1856f92) was executed
unchanged as the same-output order baseline. The inherited 127 tests remain intact.
This does not claim to have executed a new universal T6 tool or created a new family.

## 2. Necessary and sufficient support criterion

Let D={s_j-s_i : i<j}, and define the visible divisor signature

    E_D(r) = {d in D : r divides d}.

Two periods give exactly the same labeled equality partition on S iff their E_D sets
are equal. They then give the same K_r(w) for EVERY weight assignment. Conversely, if
the signatures differ, some pair monomial w_i*w_j has a different coefficient; hence
K_r-K_s is a nonzero degree-two polynomial. It cannot vanish on every positive integer
weight vector. Section 4 strengthens this to one simultaneous finite separating assignment.

The signature itself has a smaller exact label:

    c_D(r) = gcd E_D(r), with gcd(empty)=0.

For E_D(r) nonempty, r|c_D(r), and

    E_D(r) = {d in D : c_D(r) divides d} = E_D(c_D(r)).

Proof: every selected d is divisible by its gcd; conversely r divides that gcd, so any
d divisible by the gcd is selected by r. Thus

    E_D(r)=E_D(s)  iff  c_D(r)=c_D(s).

Zero labels are exactly empty signatures. With 0 as the divisibility top element,
c_D is extensive, idempotent and monotone in the DIVISIBILITY order, not numeric order.
This is the coarsest label preserving the entire declared reweighting-observer family.

### Exact bounded identifiability theorem

The following are equivalent for the abstract family {1,...,H,above-H}:

1. Labeled equalities on S distinguish all these hypotheses.
2. Some ONE positive integer weight vector gives different K values for all hypotheses.
3. c_D(r)=r for every 1<=r<=H.

(1)<->(3): if c_D(r)>r, the different candidate c_D(r)<=H has the same signature;
if c_D(r)=0, r aliases the above-H class. Conversely distinct fixed-point labels separate.
(2)->(1) is immediate. (1)->(2) is established by the finite polynomial-grid argument below.

For mere detection the weaker condition is only c_D(r)>0. These are different obligations.
No historical-priority claim is made for these elementary divisibility/polynomial arguments.

## 3. Three permanent witnesses

### Detection without ANY possible weighted identification

H=6, S={0,4,5,6}; D={1,2,4,5,6}. Every r=1..6 is detected, but

    E_D(3)=E_D(6)={6},  c_D(3)=c_D(6)=6.

Only the pair of positions 0 and 6 collides in both cases. EVERY positive weighting gives
K_3=K_6. Actual modular witnesses are bases 2 (order3) and 3 (order6) modulo7. The current
GCD value 6 is merely an indistinguishability-class label here, not a proof of order6.

### An incomplete ruler CAN identify all periods

H=9, S={0,1,5,7,9}; D={1,2,4,5,6,7,8,9}, missing lag3. Nevertheless

    gcd(E_D(3))=gcd(6,9)=3,

and every other candidate is also a fixed point. Thus full difference coverage is
sufficient but NOT necessary; supported multiples can retain the missing period exactly.

### Monotone weights on the nonzero support do NOT inherit the dense theorem

H=6, S={0,1,2,3,6}, weights=(1,2,3,4,7) are increasing on S. Yet

    K_2=11^2+6^2=157=12^2+2^2+3^2=K_3.

This support IS identifiable. A checked assignment (47,14,65,1,66) gives codes for
periods1..6,above6 equal to

    37249,31909,17417,19567,12835,17191,10987.

They are all distinct, but NOT numerically monotone. Use the verified decoder, not binary
search inherited from the dense monotone-weight theorem. The sparse zeros break that
full-interval hypothesis; there is no contradiction with the previous result.

## 4. Positive finite reweighting: existence plus executable certification

There are C=H+1 candidate polynomials. For different structural signatures, P=K_r-K_s
is nonzero, multilinear and of total degree2. Select independent weights uniformly in
{1,...,R}. Choose a nonzero w_i*w_j coefficient. After fixing the other variables, the
coefficient of w_i is a nonconstant affine polynomial in w_j, and is zero at at most one
choice. Unless that happens, P vanishes for at most one value of w_i. Hence

    Pr[P=0] <= 2/R.

A union bound over candidate pairs gives failure <= C(C-1)/R. Choosing R=2*C*(C-1)
therefore succeeds with probability at least1/2 per ideal independent trial. For a complete
sparse ruler k=O(sqrt H), both each weight and the scalar K have O(log H) bits; no
superexponential superincreasing weights are being hidden. The entire profile still costs
O(k log H) bits, and the explicit decoder has H+1 entries.

An alternative keeps all weights in {1,2}. After fixing other variables, the nonzero
bilinear coefficient means P cannot vanish at all four corners of the (w_i,w_j) grid.
Each distinct pair is separated with probability at least1/4 per independent channel.
For t channels the failure probability is at most choose(C,2)*(3/4)^t; O(log H) channels
suffice for constant success probability. This is a multi-observer option, not a free
single-scalar replacement.

Implementation uses a seeded PRNG for reproducible search, not as a mathematical assertion
of independent ideal randomness. It computes EVERY finite code and accepts only an exact
injective table. Thus its output correctness is deterministic. Exhaustion returns
SEARCH_EXHAUSTED or BUDGET_EXHAUSTED, never UNIDENTIFIABLE_SUPPORT without a structural witness.
`verify_codebook` recomputes all codes and rejects forged lookup mappings. A local validated
object is not a signed external certificate; a supplied measurement must still be genuine.

The ingredients are standard polynomial identity testing; the short elementary proof above
is complete for this degree-two case. Classical context: Schwartz (1980), DOI
10.1145/322217.322225. The publisher landing page was unavailable in this run; no claim to
have read that full paper is made, and the proof does not depend on inaccessible text.

## 5. Sparse construction and a sharper practical choice: KEEP the gcd provenance

A simple complete sparse ruler is obtained with b=ceil(sqrt H):

    S = {0,...,b-1} union {b,2b,...,floor(H/b)*b} union {H}.

For d<=floor(H/b)*b, use d=ceil(d/b)*b-i, 0<=i<b. For larger d use d=H-(H-d)
with H-d<b. Thus every d=1..H appears and k<=2*ceil(sqrt H)+1. This is a classical
block-ruler construction, not a newly invented combinatorial object.

No support inside [0,H] can identify the whole hypothesis family with o(sqrt H) marks
using this collision-observer family: every integer r>H/2 must itself occur as a difference,
otherwise it is undetectable. Hence choose(k,2)>=ceil(H/2). This is ONLY an observation/support
lower bound with the stated exponent horizon; it is not a lower bound for general factoring,
all order algorithms, adaptive outside-horizon probes, or extra algebraic observations.

The weighted scalar decoder is not usually the best computational interface. If the actual
residues a^s are already generated, retain ONE representative exponent per residue bucket
and a running gcd of differences to that representative. Its value is exactly c_D(r):
all within-bucket pair differences are differences of representative differences and vice
versa. On a certified identifying support it therefore equals r, and on the complete ruler
there is no O(H) offline decoder to build. A zero gcd on the complete ruler proves only r>H.
On arbitrary support it proves only no collision in the chosen support.

`ruler_order` uses successive powers for the low block and successive multiples of a^b for
the high block, plus at most one endpoint exponentiation. It is O(sqrt H) modular products
plus O(log H) endpoint exponentiation, with sorting/gcd/bit costs explicit. This remains a
classical square-root-scale collision route. Preserving provenance is better here than
compressing it into a scalar and then paying to decode it.

## 6. Implementation and actual costs

Source: `src/enterprise_math/group_ring_sparse_identifiability.py`.
Tests: `tests/test_group_ring_sparse_identifiability.py`.

For k marks and horizon H, the general codebook compiler uses O(k^2) pair products plus
sum_{r=1}^H floor(H/r)=O(H log H) multiple visits per trial/channel, plus a structural scan.
It keeps O(H) decoder entries (and t components per entry for t channels). General online
weighted observation computes k modular exponentiations once, then O(t*k) mass operations.
The modular multiplication bit cost, coefficient bit lengths and all decoder storage remain.

Actual local checks, Python3.13.5/Linux x86_64 sparse execution checkout:

- 38 new +127 inherited tests =165 PASS.
- Every nonempty support for H=1..10:4082 support configurations.
- 188192 candidate-pair closure/signature equivalence checks.
- 40895 independent weighted occupancy-vs-lag masses.
- 256 certified codebooks over H=1..128, both weight alphabets.
- 16768 exact codebook period roundtrips.
- 34280 actual modular-unit/horizon cases against direct order enumeration and the
  UNCHANGED bounded BSGS compiler, n=3..150. New tests separately include n=2; the old
  comparator's n>=3 precondition was respected, not bypassed.
- 75 distinct candidate pairs checked on full binary weight grids for three selected supports.

At H=4096 the simple ruler has128 marks. One large-alphabet channel has a4097-entry decoder.
The binary implementation obtained16 channels with only weights1/2; the largest measured
mass in that codebook uses16 bits. These channel counts are checked examples, not optimality.

Seven-call single-host medians in milliseconds (one warmup); all values below compute the
same bounded ORDER answer, not the same internal scalar. Cold includes codebook construction
and observation. Warm reuses the explicitly retained H+1-entry decoder. The direct gcd
method includes its own ruler generation and collision work. Tracing is separate, not RSS.

| n,a,H | marks | cold scalar codebook | warm scalar | labeled ruler gcd | unchanged bounded BSGS |
|---|---:|---:|---:|---:|---:|
|10007,5,4096|128|8.184989|0.064137|0.019158|0.014853|
|10007,5,16384|256|30.280437|0.141473|0.038027|0.021933|
|65537,3,65536|512|147.850686|0.307943|0.070216|0.045869|
|100160063,2,65536|512|152.990224|0.302785|0.073651|0.049334|

The cold codebook peak Python allocation in the third case was11906268 bytes; warm
incremental allocation60164 bytes EXCLUDES the existing decoder, so it is not total RAM.
The direct gcd/classical peaks were74216/41936 bytes. These measurements disprove any
unconditional speed/RAM advantage for the weighted codebook. Retain it for observer-design
or restricted scalar-interface tasks, not as a default faster order solver. The existing
classical comparator remained fastest in these samples.

## 7. Literature, source boundaries and continuation

Read primary arXiv HTML: Lawrence, Li, C. Musco and C. Musco, *Low-Rank Toeplitz Matrix
Estimation via Random Ultra-Sparse Rulers*, arXiv:1911.08015v1, sections1.1 and2 (classical
ruler coverage and block construction); Saarela and Vanhatalo, *A Connection Between
Unbordered Partial Words and Sparse Rulers*, arXiv:2408.16335v2 (definition/context).
Do not transfer their covariance/noise theorems to modular order inference. This return
claims scoped derivations, tests and interfaces, not priority in sparse-ruler or identity-
testing theory. Actual dedicated Scholar request Issue377 produced three related metadata/
snippet records, jobPARTIAL/batchFAILED; no full texts obtained through that channel.

The old no-run activity remains this conversation's direct research persistence surface.
No formal Task-ID, CLAIM, ER, frozen Result, independent Driver review or Foundation/Lean
admission is fabricated. Current ordinary-control guidance has only formal-run, Driver or
maintenance PRE_FINAL bindings, not this legacy no-run research record; an evidence audit
is not a native formal-run final gate. Do not change the activity to maintenance to hide this.
P000 and protected worldview are unchanged. No RSA-270 experiment or full repository suite.

The selected sparse-support identification unit is closed at its stated finite observer
scope. The next mathematical residual is a cheaper certificate/decoder for larger custom
supports or noisy/rounded observations with explicit separation margins. Random weight
existence alone supplies no noise robustness, no efficient preprocessing guarantee, and no
sub-BSGS generic improvement. Preserve the three witnesses and do not repeat earlier engines.
