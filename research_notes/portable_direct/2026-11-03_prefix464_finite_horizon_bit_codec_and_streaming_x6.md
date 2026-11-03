# PREFIX-464 — Finite-horizon bit-optimal X6 BRC weight codec and exact streaming closure

2026-11-03 Asia/Shanghai. Research6 author-side theorem and exact arithmetic certificate; UNREVIEWED / NOT_ADMITTED. Successor to PREFIX-463 at cbbbbff41de9a9117869a88e423aac2e750074f8. Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Applicable current behavioral rules, P000 and ACTIVE X6/Heartbeat worldview read separately.

## Input and typed observer

In the native six-axis signed chart use the 11 eligible residual letters +e1, ±e2,...,±e6. For a word of length m, let s be the number of unilateral +e1 letters, y_i=c_i^+-c_i^- (i=1..5), p_i=min(c_i^+,c_i^-), and p=(m-s-Σ|y_i|)/2=Σp_i. Write u=(p2,p3,p4,p5). All letter weights w0,wi+,wi- are fixed strictly positive rational numbers; rho_i=wi+wi-. Let B be the matrix of prime valuations of rho_i/rho_1 for i=2..5, and r=rank_Q(B), 0≤r≤4. PREFIX-463 proved equality of individual word-product weights at fixed (m,s,y) exactly when B u = B u'. Here the observer is the exact histogram of (endpoint, individual positive-rational word-product weight, integer count), with future homogeneous letter-append operations. It is not an occupation/order/provenance-sensitive observer.

## Theorem A: finite-horizon reversible packed integer

Choose r independent rows of B to form an integer r×4 matrix C. For all integer u,u', Cu=Cu' iff Bu=Bu': every row of B lies in the Q-span of C. For fixed p≥0 and row j, set a_j=min(0,C[j,1],...,C[j,4]), b_j=max(0,C[j,1],...,C[j,4]), W_j=p(b_j-a_j)+1. Every u≥0 with Σu≤p obeys pa_j ≤ (Cu)_j ≤ pb_j. Therefore

    E_p(Cu) = Σ_{j=1}^r ((Cu)_j-pa_j) Π_{h<j} W_h

is a scalar in [0, ΠW_j), uniquely decoded by successive mixed-radix divisions; decode first, then restore offsets pa_j. This is an exact codec for the stated weight-histogram equivalence. Its fixed-width bound is ceil(log2 ΠW_j) bits, implemented as (ΠW_j-1).bit_length(); r=0 gives zero bits.

Proof: the coordinate bounds follow from u_i≥0, Σu_i≤p and extrema among each row's coefficients plus zero. Mixed-radix digits are uniquely decoded; row-selection preserves the valuation-matrix kernel over Z4. PREFIX-463's prime valuation equivalence then identifies exactly the product-weight equivalence. QED.

## Theorem B: asymptotically optimal number of bits

For fixed B put n_B(p)=|{Bu:u∈Z4_≥0, Σu≤p}|. For any r≥1,

    (floor(p/r)+1)^r ≤ n_B(p) ≤ Π_{j=1}^r [p(b_j-a_j)+1].

To prove the lower bound select r Q-linearly independent *columns* of B. Independently varying their nonnegative coefficients from 0 to floor(p/r) keeps Σu≤p, and distinct grid points have distinct Bu. The upper bound is Theorem A. Thus log2 n_B(p)=r log2 p+O_B(1), and E_p uses r log2 p+O_B(1) bits: within a constant number of bits of the information-theoretic minimum ceil(log2 n_B(p)) as p→∞. r=0 gives n_B(p)=1. The constant depends on the fixed weight family. This is a worst-case fixed-width *signature-only* result, not a claim of exact finite-p minimum, nor of constant storage for endpoint/count/weights.

There is no conflict with the PREFIX-463 global additive rank lower bound: mixed-radix coefficients and offsets depend on the finite horizon p and must be recomputed as p changes. A globally additive one-coordinate Z4→Z map cannot have the same integer kernel as a rank-r>1 valuation matrix.

## Theorem C: exact append recursion, no occupation reconstruction needed

Let h_m(s,y,v) count ordered words with endpoint (s,y) and reduced signature v=Cu. Start with h_0(0,0,0)=1. Appending +e1 updates s→s+1 and leaves v unchanged. Appending sign·e_(i+1), i=1..5, updates y_i→y_i+sign. The opposite-pair count p_i rises by one **exactly when sign·y_i<0 using the pre-append y_i**. When i≥2 and that condition holds add the (i−1)st column of C to v, otherwise v is unchanged. Sum old integer counts at equal destination keys. This 11-branch update exactly computes the declared histogram for every m.

Proof: min(c_i+,c_i-) increases precisely if the opposite (previously less numerous) direction is added. Therefore the stated v update equals the signature of the actual extended occupation. Every ordered word has exactly 11 distinct extensions. Given (m,s,y,v), all prime valuations Bu are recovered by Q-linear row combinations of C and are integers on valid states; the baseline endpoint factor times rho_1^p times prime powers reconstructs the unique positive rational word-product weight. Thus all and only words with equal endpoint and product weight are aggregated. QED.

The precomputation factors input rational numbers (cost depends on integer factorization) and performs exact rational rank elimination. Each dynamic transition uses O(r) arbitrary-precision integer additions plus endpoint updates; the full DP cost depends on the actual number and bit lengths of reachable states. External packed keys are decoded/repacked using O(r) big-integer operations when p changes. This is a reproducible reference mathematical codec, not an optimized native BRC runtime benchmark.

## Exact certificate, source and finite scope

The executed stdlib-only Python source prefix464_compact_certificate.py exhaustively enumerates all 11-bin unordered occupation vectors for m=0..7 and computes multinomial exact counts and Fraction letter products. It independently computes the 11-step compressed-signature DP, checks equality of counts for each endpoint/signature, checks weight equality inside every signature fiber, reconstructs and decodes the scalar mixed-radix key for every state, and verifies that total ordered paths equal 11^m. It checks 0/1/2/3/4 valuation-rank families plus a nonintegral positive-rational rank-4 family. ALL_CHECKS_PASS. At m=7 each family represents 19,487,171 ordered words by exact aggregation.

At m=7 the compressed-state counts for ranks 0,1,2,3,4 are 9108, 17820, 18612, 19162, 19448 respectively (all 11-bin unordered occupation states: 19448). At one endpoint with p=16, C(20,4)=4845 possible occupations collapse to 1,65,425,1785,4845 distinct product-weight signatures respectively; worst-case fixed radix bits are 0,7,10,14,17. Rank 2's 425 labels require at least 9 bits, and this radix code uses 10. A second rational rank-4 family requires 20 bits due to larger coefficient ranges. These state/bit figures omit endpoint, multiplicity, and metadata costs.

A separately executed longer independent stdlib Fraction certificate crosschecked reconstruction of every compressed state against direct product-weight dynamic programming for the same m=0..7 and checked rank lower-grid witnesses up to p=64. The second executed code and its detailed output remain available as independent conversation evidence.

## Reuse, status and next

REUSE_APPLIED: P000 native X6, PREFIX-462 toric occupation fiber, PREFIX-463 valuation rank, and frozen positive BRC histogram semantics. Signed six-dimensional chart displacement is not a final Cell address. Explicit order, provenance, nonhomogeneous conditional histories, and other observer-typed operations require their own verified preservation.

Next PREFIX-465: compare an actual HNF/SNF integer image basis against pivot-row and dense bounded codebooks, including preprocessing, input transformation, storage bits, append/decoding and output costs. Then test a genuine conditional-history native BRC future for a concrete additional provenance repair coordinate. The all-degree polynomial evaluation nullity problem remains separately open.

Authority: authenticated GitHub awdawmip (push/admin). Current native Sites gateway reports research_authority_granted=false and control task list returned CONTROL_QUOTA. Owner/Researcher-ID/CLAIM not verified; direct author-side Source publication only, with no independent Review or Admission.
