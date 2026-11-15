# R191 — Dyadic recency affine lift and optimal fixed-bit codec

Date: 2026-11-16 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Independent portable science, not a formal CLAIM, Result, Review or Foundation promotion.

Frozen science input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Sources: R182 at 83824bda8cb4ca4d9db71d660165f00fd92326ef; R183 at 5557fb3748bbe9e831e2f35716607dacffc0c6d4; R190 at b4d2eda1f09edec71e6788e3d98d7ced2cf4f44c. Native BRC affine semantics inspected in src/enterprise_math/brc_transport.py at enterprise-math main a16fac51585f41d4b27dd6e8fdb989cc9bb4153b.

## 1. Exact population and observer

Fix k >= 1 distinguished source IDs T={0,...,k-1}. Histories are finite ordered words of complete BRC/X6 atoms, each with source in T or an unselected source symbol *. The underlying carrier retains original signed X6 paths, branch identities, provenance, positive-rational weights and multiplicities. The *only* observer considered here is q_U(w): the most recently occurring target in nonempty U subset of T, or NONE if no target from U occurs.

Let lambda(w) be the partial permutation of selected sources ordered by their last occurrence, from oldest to newest. The R182 exact quotient S_k has product a star b = (entries of a absent from support(b), in their old order) followed by b. It has N_k = sum_{r=0}^k k!/(k-r)! = floor(e*k!) distinct elements. The quotient preserves q_U and every finite future left/right whole-history concatenation. None of these assertions licenses erasing native X6 paths, joint relations, ports, labels outside T, weights or branch data for richer observers.

## 2. Theorem R191A — k-dimensional exact dyadic chronology

For a target source a define a rational affine map D_a on Q^k by (D_a(z))_a=1 and (D_a(z))_j=z_j/2 for j != a. For an unselected source use D_*(z)=z/2. For w=c_1...c_m, let D_w=D_{c_m} o ... o D_{c_1}, with empty-word map the identity. Evaluate the *auxiliary provenance register* from z=0; this zero is not an X6 native origin.

For each selected j, let t_j be its final 1-based position in w if it appears. Then

- D_w(0)_j = 2^{-(m-t_j)} if j appears;
- D_w(0)_j = 0 if j does not appear.

In particular the positive coordinates are exactly the present sources, and strictly increasing positive coordinate values correspond exactly to increasing last-occurrence positions. Every q_U is recovered by the positive maximum of these coordinates (NONE if all zero). This remains true for arbitrary finite prefix/suffix continuations from the same initial zero register.

Proof: induction on the complete-atom word length. On encountering a, the a-coordinate resets to 1, so its age is zero. Every other coordinate is halved, increasing the last-occurrence age by one; zero stays zero. An unselected event halves all coordinates. Last-occurrence positions are distinct for distinct source IDs, so positive values are pairwise distinct. Chronological composition is exact function composition. QED.

Each D_w is represented by a diagonal affine map (alpha_w,beta_w), z_j -> alpha_j*z_j+beta_j. Given earlier map A and later map B, A.then(B) has

alpha = alpha_B elementwise-times alpha_A,
beta = alpha_B elementwise-times beta_A + beta_B.

This provides a sparse O(k)-entry action with O(k) *rational operations* for serial composition. It agrees algebraically with the retrieved brc_transport.Affine.then convention; the actual installed Python module has NOT been executed. The metadata coordinates do not add native spatial dimensions.

## 3. Theorem R191B — why the k-dimensional lift does NOT solve minimal finite-quotient affine dimension

The map w -> D_w is a representation of the entire free word monoid with its chronological product; it is NOT an affine representation of the finite quotient S_k. The quotient identifies aa and a because lambda(aa)=lambda(a)=(a). But for distinct targets a,b,

D_a^2(z)_b=z_b/4 while D_a(z)_b=z_b/2.

Thus D_a^2 != D_a, even though [a] is idempotent in S_k. Inserting an unselected event likewise leaves lambda unchanged but changes the affine map. Therefore R183's k(k+1)/2-coordinate faithful RESET-CLASS quotient representation has NOT been replaced by a k-coordinate faithful quotient representation. Equality by last-occurrence state is not equality by full dyadic affine action.

A native EffectHistogram may carry (positive Fraction weight, D_w action, positive integer multiplicity) and compose these effects exactly. It may coalesce only identical full (weight, action) pairs under its own semantics. When future operations and observation are restricted precisely to R182's q_U/whole-history operations, one may separately evaluate the dyadic register at zero, decode lambda and aggregate through the finite quotient; a richer hidden-state or provenance observer invalidates that compression unless independently certified.

Precision caveat: for w=b a^m with distinct selected a,b, D_w(0)_b=2^{-m}. The denominator needs m+1 bits, so exact dyadic bit length is unbounded with history length. Small affine *dimension* is not a fixed-memory bound. Any finite-precision truncation requires a separate finite-horizon preservation theorem.

## 4. Theorem R191C — an optimal fixed-length quotient state code

R182 established the lower bound ceil(log2 N_k) bits, but the ordered-list storage uses O(k log k) bits. The following gives an exact constructive fixed-bit code attaining its lower bound.

For 0<=r<=k put P(k,r)=k!/(k-r)!, O_r=sum_{j=0}^{r-1}P(k,j), with O_0=0. For a partial permutation s=(s_0,...,s_{r-1}), define d_i as the 0-based rank of s_i among indices not used in s_0,...,s_{i-1} (ordered numerically). Put

R_k(s) = O_r + sum_{i=0}^{r-1} d_i * P(k-i-1,r-i-1).

The empty state has code zero. For each fixed r, the final sum is the lexicographic rank of an r-permutation: after choosing digit d_i there are exactly P(k-i-1,r-i-1) completions. The interval for r has size P(k,r) and consecutive r-intervals are disjoint. Euclidean division by successive completion counts uniquely recovers digits, so R_k bijects S_k with integers [0,N_k-1].

Define B_k=ceil(log2 N_k)=(N_k-1).bit_length(). Every state can therefore be stored in exactly B_k binary bits (some bit patterns unused). To update on a selected source a, decode, delete a if present, append a, and encode; an unselected event leaves the code unchanged. To concatenate encoded histories, decode both, apply the R182 star law and re-encode. To answer q_U, decode and select the final member lying in U (or NONE). The R182 exact quotient theorem gives correctness for *all* future source-only operations and arbitrary finite history lengths.

No deterministic exact fixed-length memory for this observer, supporting the declared continuations, can use fewer than B_k bits: singleton queries determine the support, and two-source queries determine every relative order, so all N_k states are distinguishable with empty continuation. Any deterministic memory must have >=N_k internal states. QED.

This attains the bit bound but is not an O(1)-time update claim; simple rank/unrank and remove/append have polynomial index work and nonconstant arbitrary-precision integer cost. The ordered-list implementation of R182 remains a time/space alternative. No end-to-end native BRC speedup is established.

| k | N_k | exact B_k bits | R183 reset-affine coordinates | R191 dyadic-affine coordinates |
|---:|---:|---:|---:|---:|
|1|2|1|1|1|
|2|5|3|3|2|
|3|16|4|6|3|
|4|65|7|10|4|
|5|326|9|15|5|
|6|1957|11|21|6|
|7|13700|14|28|7|

The columns are different resource types: R183 action genuinely factors through finite S_k, R191 dyadic actions use unbounded exact dyadic precision, and R191's bit-optimal code uses nonlinear decode/re-encode of the finite semigroup.

## 5. Exact local validation

Companion R191_dyadic_recency_and_rank_check.py uses Python arbitrary integers and fractions.Fraction without numerical approximation. The attached R191_verification.json records PASS for the following finite domains:

- All 16,071 partial-permutation states over k=1..7 round-trip uniquely by rank/unrank; all 125,663 single-atom append updates, including one unselected atom.
- All 110,786 ordered pairs of quotient states for k<=5 under coded star product; all 1,104 nonempty subset queries for k<=4.
- All 1,365 words of length <=5 on three selected and one unselected source; 51,150 specified ordered word pairs under exact diagonal affine composition; 19 dyadic denominator bit-growth witnesses.
- Explicit k=2 failure of the false quotient identities D_a^2=D_a and D_*D_a=D_a, while lambda(aa)=lambda(a) and lambda(*a)=lambda(a).

Universal theorems are established by the symbolic proofs above, not by extrapolating finite enumeration. The computations are author-side independent reference tests, NOT an independent mathematical review, formal checker result, installed brc_transport integration or native multi-port benchmark.

## 6. Status and next discriminating problem

Frozen scientific pin remains unchanged. The precise new contribution is a history-sensitive exact k-coordinate source chronology with an explicit NON-DESCENT witness, plus an exact bit-optimal codec for the previously counted finite source-last-occurrence quotient. The earlier R182 count and R183 reset representation remain intact.

Next: attempt the genuinely open minimal faithful rational affine dimension of finite S_k (do not conflate with the above free-word lift); execute a pinned brc_transport.Affine / EffectHistogram integration test with exact positive fractions, and compare diagonal sparse actions with finite-bit quotient updates and real bit-operation costs; independently continue intermediate-aperture C_b(k) minimax work if an unowned task is available.

Control: portable independent research only; no current formal CLAIM, no Task Result, no independent review and no P000 change. Historical provenance EM-DIRECT-BF4AD7 / SID MCP-46f202db13e64ad6b4c8860e06908245 / RA-7A118452894D2600AE7DE5A2 does not supply new execution authority.