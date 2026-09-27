# Full-history carry contraction: existing coverage and a missing dispatcher

Status: **SYMBOLIC_AUTHOR_ASSESSMENT / SHARED_CONTEXT / NOT_ADMITTED**.
This assessment reads frozen proofs and source. It performs no scientific execution, ideal propagation, new professional query, or remote write. It changes no predecessor file. All matrices below retain the actual full carrier, or a separately certified exact common embedding; none of the arguments drops residual coordinates.

The principal answer is that a fixed integer displacement already has an O(i)-layer, two-carry contraction for arbitrary chronological native words. Neither few active windows nor commuting words are needed. The whole-period small-odd-part contraction also already exists with full matrices. The useful implementation gap is a **paid-address few-alias dispatcher** in the current paid aggregator. A further symbolic combination below compresses each certified scalar gap to a 2-by-2 scalar transfer, without enumerating window displacements.

## 1. Read sources and what they already establish

All paths are relative to `D:/em/TEMP/` in this reading record.

| Source | SHA-256 | Actual scope read |
|---|---|---|
| `sep27-qft-signed/DYADIC_CARRY_CORRELATION.md` | `70b35a57ee0ffe628b2090f0ddeb0a7bce7eb076a03b627ca10ba8e1f815f3d1` | Fixed-d coefficient, alias decomposition and paid discovery boundary |
| `sep27-qft-carry-execution/carry_executor.py` | `f017b1fb1516e8faa97afd39d663e4eda6d21cad95f65bb2ccf5a79d7ff3b810` | Complete source, including coefficient and coherent sum |
| `sep27-qft-carry-execution/aggregation_theory/PERIOD_AGGREGATION.md` | `be20eb9409b1b250edfe9e0bc83fda9701253a71add4f98e3ccea8325d2302be` | Full odd-part proof, discovery/address costs and mask-rank limitation |
| `sep27-qft-carry-execution/aggregation_theory/period_aggregator.py` | `6f2c855bec09f7cf7fc4853b55ea41f94a195ba3d3b783d18921e9a3b6465f0c` | Complete source; original full-cycle replay and full-matrix contraction |
| `sep27-qft-oddpart/aggregation/paid_aggregator.py` | `ff7cf4c32d5cd86c68a2602c4991972004762343ecff4de72e735441b1a68768` | Complete source; current paid replay and dispatch |
| `sep27-qft-oddpart/aggregation/leading_zero_aggregator.py` | `f6597bcd54c4e9525ef142e3a661a0f30a14bc184169cf8d053005a8149cb7cb` | Complete source; counted leading zeros and suffix-displacement enumeration |
| `sep27-qft-boundary/gram_structure/FINITE_FEEDBACK_AND_MULTIWINDOW.md` | `00cf4dd1de1a0c019a0c2b19f8504992269b4f0bfd4cd1a480eb20edb2af7b0e` | Full note, especially arbitrary-seed maps and their negative-d rule |
| `sep27-qft-boundary/gram_structure/SIGNED_GAPS_REFINEMENT.md` | `1a84d09ed1fecdf7a42de9c1b1e48da881c820e544214011703c79a688938776` | Full note, signed scalar gaps, few aliases and one-negative-bit family |

The later `sep27-qft-oddpart/target_address/TARGET_ADDRESS_NOTE.md` was also read to distinguish the paid implemented address interface from the older proof's proposed interface. In particular, complete two-projection matching already proves membership by Bezout in the ambient abelian unit group; its final modular-power check is a useful redundant executable check, not a necessity caused by noncyclicity.

`CarryExecutor.coefficient` starts at line 77; its current seed is the physical E=e0 e0^T. `sum_coefficients` at line 123 explicitly does **not** certify completeness of its caller-supplied displacement list. The boundary multiwindow note already defines arbitrary-matrix maps at line 123 and explicitly describes the linear seed extension at line 152. This assessment does not relabel those facts as a new theorem or implemented general-seed API.

## 2. Fixed d has no active-window exponential

Fix a committed history h of length i, L=2^i, and its actual ordered operators O_j=(-1)^(h_j) T_j. Let W(n)=O_(i-1)^(n_(i-1)) ... O_0^(n_0), with address bits in chronological MSB-first order. For any full matrix X define

    C_d[X] = 4^-i sum_(0 <= n,n+d < L) W(n) X W(n+d)^T.      (1)

The physical coefficient is C_d[E]. For 0<=d<L initialize two matrices M_0=X, M_1=0. At chronological digit j let a be the corresponding bit of d and replace them with fresh accumulators

    M'_c = (1/4) sum_(e,x,y in {0,1}; x+a+c=y+2e)
                        O_j^x M_e (O_j^y)^T.              (2)

Return M_0 after i layers. Here e is the high/outgoing carry and c the low/incoming carry. Equation (2) contracts the ordinary addition constraint in reverse carry direction while appending actual words in their forward chronological direction. Each legal pair (n,n+d) has a unique carry path with both external carries zero. The products therefore retain their exact order even when every O_j is noncommuting and non-scalar. There are four allowed local bit/carry tuples per layer, two full boundary matrices and a constant number of fresh full-matrix temporaries. No D^4 superoperator tensor is required to apply this map to one X.

The recurrence is linear in X; it is valid symbolically for any real matrix. A future native adapter can restrict to the already admitted dyadic matrix representation. It must not claim that the frozen executor currently validates arbitrary new seeds. For d<0 the identity is

    C_(-d)[X] = (C_d[X^T])^T,                              (3)

so transposing only the result is safe for E, but not for an arbitrary asymmetric intermediate seed. At i=0, C_0[X]=X; at |d|>=L it is zero. No normalization by a history mass is involved.

The existing execution uses actual signed observer combinations and complete word actions. O(i) here counts matrix-transition layers, **not** constant-time arithmetic: native word lengths, D, integer widths, entry observers, binding checks, admission, retained receipts and serialization remain charged.

## 3. Paid few-alias dispatch: exact interval and concrete omission

Suppose actual replay has supplied exact R=ord_N(b) and MEMBER r with 0<=r<R and b^r=z. Every allowed alias, and no other integer, is

    d_k = r+kR,
    k_min = ceil((1-L-r)/R),
    k_max = floor((L-1-r)/R),
    J = max(0, k_max-k_min+1).                             (4)

Thus

    Gamma_h(z) = sum_(k_min <= k <= k_max) C_(d_k)[E].       (5)

Equation (4) follows by solving 1-L<=r+kR<=L-1. It gives completeness, uniqueness and the strict endpoints; no duplicate zero or missing negative displacement is possible. Each alias sum is coherent and signed. It is not a mixture or a sum of individual masses.

The bound J<=floor((2L-2)/R)+1 gives a useful condition independent of active windows. In particular R>=L implies J<=2, and R>=2L-1 implies J<=1. For R>=L the only possible aliases are r when r<L and r-R when r-R> -L; both may occur when R=L and r is nonzero. r=0 is counted once. A MEMBER target can still have J=0 and hence zero correlation at this finite depth.

The current paid implementation does not select this general route:

- `paid_aggregator.py:61-77` obtains and freshly replays the paid target/order and the inherited permutation.
- `_contract_verified_period` starts at line 90. Line 100 tests only `s > depth`, where R=2^s q. That sufficient condition implies R>=2L but misses large odd periods and many mixed periods.
- Otherwise line 113 constructs q full matrices, line 119 constructs q routing entries, and line 132 allocates q contribution lists per high layer. An odd R>=L therefore enters a q-state contraction even though (5) has at most two terms.

This is a resource-dispatch omission, not a wrong value in the existing algorithm. The fixed-d theorem is already published; the few-alias observation is also explicitly present in the signed-gap note. A separately versioned dispatcher can use the completed fresh replay, evaluate (4) through admitted signed integer arithmetic, and choose (5) before any q-sized allocation. It must retain the interval calculation and aliases as the completeness receipt. Calling `sum_coefficients` alone does not supply that receipt.

Conditional contraction work is O(iJ) matrix layers, O(D^2) live matrix workspace if aliases are streamed, plus signed addition of J results and all evidence storage. The generic odd-part route, when s<=i, costs O(q(i-s)+s) matrix layers and O(qD^2) live matrices. A declared cost model can choose between these routes; neither dominates uniformly. q=1 handles exponentially many aliases in O(i), so unconditional alias enumeration would be a regression. A useful conservative envelope is

    min{ O(iJ), O(q(i-s)+s) }                              (6)

for the two admitted routes, with the exceptional large-two-part case handled before allocation. This envelope omits neither paid arithmetic nor certificate work; it describes only the subsequent matrix contraction.

The new *application condition* is J polynomially bounded, equivalently a sufficiently large R relative to the chosen prefix length, not a sparse public history. For default t=2 ceil(log2 N), R<N, so R>=2^i is chiefly an early-prefix condition; it cannot cover all late prefixes. More importantly, the current exact order/address implementation can itself use O(q) actions and replays that work per Gamma query. Thus even a two-alias matrix contraction with exponentially large odd q is **not** an end-to-end polynomial algorithm through the present discovery interface. A known target exponent r and an arbitrary modular target label z are different inputs. Giving r/R to the contraction does not make their acquisition free. The same paid information must be given to the classical comparator.

## 4. Further combination: contract scalar gaps inside the fixed-d stream

The following explicit transfer is not written in the read multiwindow sources. It is a direct composition of the already established two-carry recurrence, rather than a replacement theorem for arbitrary matrix coefficients. It saves matrix work in the few-alias route without expanding window-displacement tuples.

Suppose a consecutive block of g>=1 chronological positions has certified complete operators O_j=sigma_j I, sigma_j in {+1,-1}. For one target digit a, (2) becomes a scalar matrix acting on the column of two full matrices:

    L_0(sigma) = [[2,0], [sigma,sigma]],
    L_1(sigma) = [[sigma,sigma], [0,2]].                    (7)

The output rows index the low/incoming carry and the input columns the high/outgoing carry. For a=0, the low-zero branch receives two diagonal bit choices from high-zero; low-one receives one off-diagonal choice from each high carry, both with sign sigma. The a=1 case is its complementary constraint. This proves (7), including the public readout signs; no nonnegative-count interpretation is imposed on its entries.

For target digits a_first,...,a_last in chronological order, the block map is

    (M'_0,M'_1)^T = 4^-g
          L_(a_last)(sigma_last) ... L_(a_first)(sigma_first)
          (M_0,M_1)^T.                                    (8)

Only small scalar arithmetic is needed to form the product. It is then applied as two signed linear combinations of the existing full matrices. The incoming matrices may be asymmetric and mutually correlated. The scalar block is not replaced by separately seeded coefficients, and no transpose shortcut is used. Non-scalar words before and after the block remain in their original order.

For an all-positive block there is a closed expression. Put H=2^g and let a in [0,H) be the integer represented by the target block. Its unnormalized transfer is

    L_block = [[H-a,   a  ],
               [H-a-1, a+1]].                             (9)

Indeed a low carry c and high carry e admit exactly those x,y in [0,H) with x+a+c=y+H e. Their counts are H-a-c for e=0 and a+c for e=1. All four values in (9) are nonnegative, including a=H-1. The complete map is still 4^-g L_block, with no missing raw-amplitude factor. For the empty block g=0 use the identity transfer; **do not apply (9)**, which would introduce a spurious carry path at a nonexistent digit.

Equation (9) takes a constant number of arithmetic operations on O(g)-bit integers after digit extraction; this is not O(1) bit cost. An arbitrary signed block takes O(g) small 2-by-2 products, with entries of O(g) bits. Complete scalar-word or common invariant-subspace certification is a separately paid premise. Agreement only on e0 or an apparent zero residual in one trajectory is insufficient.

If a history has A non-scalar positions and B maximal scalar blocks, one fixed coefficient now needs the original native matrix actions only at the A positions, O((A+B)D^2) scalar-entry combination work, and O(i) small scalar operations in the general signed case. All-positive blocks use (9) instead. Denominator widths and receipt sizes remain charged. This is useful even with many separated noncommuting windows, because it never enumerates their local displacements: (4) enumerates only the J **global** aliases.

Thus a concrete conditional family is few global aliases plus long certified scalar gaps; it permits arbitrary chronological operators within every remaining window. The matrix-transition factor can be reduced to J(A+B), rather than the product of all local displacement ranges. When every position is non-scalar this falls back to the existing O(iJ) result. When J is huge this does not solve the modular sum; the small-q or proved floor-count routes can remain preferable.

The single-digit matrices, multiplication direction, all-positive closed expression and g=0 exception received shared-context symbolic cross-check from the completion-audit colleague. No native implementation or numerical fixture of (8)-(9) was run for this assessment.

## 5. What remains expensive, and the bounded next step

The previous whole-period recurrence already computes full matrices for arbitrary history: q residue matrices in the high block, then two carries in the low block. It does not assume commutation, few windows or diagonal Gram entries. Reimplementing it under a new full-history name would duplicate completed work. Its current paid adapter has already replaced the original O(R) complete-cycle replay with explicit odd-part discovery and target recovery; those costs are still real.

No uniform two-state substitute for the arbitrary modular mask follows from the fixed-d lemma. The existing odd-R cut-rank argument applies when both sides of a binary cut have at least R addresses: the congruence mask contains an R-by-R identity submatrix. It rules out a smaller exact local linear representation of that **unweighted mask** at that cut. It does not lower-bound every native weighted contraction, nonlocal method, approximation or simulator. It is consistent with all the few-alias and scalar-gap special cases above.

The smallest useful next implementation is a new paid-J dispatcher, preserving current discovery/replay receipts and adding typed interval-completeness evidence before choosing a contraction. Bounded validation should compare the complete matrix against the existing full-period method on already admitted small cases, cover J=0/1/2 and J>2, both signs of d and d=0, R=L endpoints, arbitrary noncommuting words, and a zero-mass history. This is a proposed check, not an execution claimed here. It should retain failed route candidates and compare setup/replay separately from contraction.

A second independently useful step is an arbitrary-dyadic-seed carry adapter with (3), then a versioned scalar-block implementation of (8)-(9). Its negative controls must include asymmetric input seeds, a scalar certificate valid only on an unproved subspace, reversed block multiplication, a negative public sign, and g=0. Comparing all full coordinates and raw denominators is necessary. No word certificate, ideal-QFT error bound, sampling totalization or source binding is weakened by either proposed optimization.

Global-Knowledge-Sync: main@b98c6e4 / GLOBAL_KNOWLEDGE_V1
