# EC49FPS — Exact source-weighted native BRC mixed-observation optimum and low-root-price interval

Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Independent portable research, 2026-11-15. Formal Task CLAIM, Result and independent mathematical Review are not asserted.

## 1. Immutable scientific population and measurement semantics

The scientific input is frozen at commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Original master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; original native BRC rooted-Trie cost table SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Use the *complete original legal-root domain* whose first source configuration is 16995: 242 exact original configurations, 112 distinct rooted cost profiles. Each rooted profile retains its original-configuration multiplicity `w_i >= 1` with `sum_i w_i=242`. This is a discrete native-BRC-derived cost *observation design problem*, not an assertion of a new physical evolution law. The names/roots, all 24 demand labels, complete allocation, exact demand-subset and rooted cost inputs retain the frozen representation and provenance.

There are 324 legal complete-allocation terminal scalar queries (T), and 96 named-root/optional-demand-subset scalar queries (R): 420 distinct original action keys. Each observation produces its exact integer response from the frozen rooted Trie cost table. These 420 queries induce 395 different full-population response partitions. A policy chooses each next action depending only on its previous exact scalar responses, stopping when it uniquely identifies the rooted profile. We minimize expected *total paid query price* without restricting tree depth.

Two declared priors are distinct: (a) uniform on the **242 source configurations**, assigning rooted profile `i` probability `w_i/242`, and (b) uniform on the **112 rooted profiles**. Terminal price is `t>0` and named-root scalar price is `r>0`.

## 2. Theorem (global optimum for configuration-uniform prior)

For `r=t/2`, the exact global optimum among all adaptive policies using **all 420 original action keys** is

`E_config[C] = (841/484)*t`.

There are two minimizing first original action indices: `346` (R/root 5/optional-demand subset mask 557056) and `354` (R/root 6/subset mask 2228224). An exact witness beginning at index 346 uses **only named-root scalar queries**, has 41 internal decision nodes, distinguishes all 112 rooted profiles, and accumulates across all 242 source configurations the following histogram of the number of root queries:

| Root-query count | Original configurations |
|---:|---:|
| 1 | 3 |
| 2 | 65 |
| 3 | 62 |
| 4 | 38 |
| 5 | 74 |

Therefore the total number of root queries summed over all source configurations is `3+2*65+3*62+4*38+5*74=841`, and the expectation is `(841/242)*r` when this witness is run with root price `r`. At `r=t/2`, this gives `841t/484`.

The prior feasible policy obtained in EC49FPR cost `425t/242=850t/484` under the configuration-uniform prior, so optimizing that actual prior strictly reduces the expected price by `9t/484`. Neither result requires new or modified native BRC input.

## 3. Global optimality and exhaustive proof kernel

Let `H` be the set of 112 rooted profiles and `W(S)=sum_{i in S} w_i`. Scale prices by `2/t` at `r=t/2`, so a root readout costs 1 and a terminal readout costs 2. For each action `a` and candidate subset `S`, let `P_a(S)` be the partition of `S` into fibers having equal integer response. For singleton `S`, let `C(S)=0`. For `|S|>=2` define the **exact** Bellman value

`C(S) = min_{a: |P_a(S)|>1} { c_a*W(S) + sum_{F in P_a(S), |F|>=2} C(F) }`, `c_R=1`, `c_T=2`.

Every informative action produces only proper nonsingleton subfibers, so finite induction over `|S|` proves this equation gives the unrestricted-depth global minimum, not merely a greedy, bounded-depth or local solution. Every action leaving a candidate subset unchanged is pointless at strictly positive price. Full-population partitions with identical fibers have identical restricted partitions on every `S`; keeping their cheapest action is therefore a valid **scope-limited observer equivalence certificate** for the stated static scalar-query decision task. This quotient does not erase source configurations, joint provenance, root identities from the scientific input, or any declared other future operation. All original keys are retained to report their minimizing indices.

The exhaustive exact-integer implementation evaluates every potentially improving quotient action. It begins with an explicit feasible `850`-scaled-sum policy and uses only admissible pruning: for each candidate action `a`,

`L_a(S)=c_a*W(S) + sum_{F in P_a(S), |F|>=2} W(F)`;

since every nonsingleton child requires at least one further positive-price query, `L_a(S)` is a rigorous lower bound on that action's total scaled cost. An action with bound not below the current achieved incumbent, or with already accumulated **exact** child costs not below the incumbent, cannot lower the optimum. Action ordering only affects runtime. Integer recursion, all-first-action comparison and complete response-tree construction returned `C(H)=841`. The final scan of 395 canonical action partitions found only original action keys 346 and 354 at that minimum.

The witness is checked against the original action's exact integer values for each of 112 rooted profiles. A separate independently written verifier reparses the frozen original master and rooted cost table, reconstructs **all 242 configurations and 112 profiles**, replays the witness on each original configuration, checks the leaf's correct profile identity and the 841-scaled-cost histogram. Thus the executable proof supplies an exhaustive lower bound **and** independently replayed upper bound for this finite native BRC observation task. Recorded search: 18,717 memoized nontrivial candidate subsets at the full-state optimum; 21,951 after evaluating the initial-action table. Python integers and bitmasks are exact; there is no statistical confidence interval, floating-point discretization, numerical BRC approximation or classical trigonometric propagation.

## 4. Theorem (entire low-root-price interval)

For every `t>0` and `0<r<=t/2`, **the exact unrestricted-depth global optimum** for the same configuration-uniform original BRC domain is

`E_config[C] = (841/242)*r`.

For the *uniform prior on the 112 distinct rooted profiles*, EC49FPR's checked half-price optimum is `37t/28` and its optimum witness also consists exclusively of named-root readouts (41 internal nodes). Consequently, in the same interval the global optimum for that different prior is

`E_profile[C] = (37/14)*r`.

**Proof (price monotonicity):** Fix either prior and denote `r0=t/2`. The finite half-price theorem establishes a globally optimal root-only policy `pi0` costing `r0*L`, where `L` is its expected count of root queries. For any alternative mixed adaptive policy `pi` with expected root and terminal counts `R_pi,T_pi>=0`, its cost at any `r<=r0` obeys

`r R_pi + t T_pi >= (r/r0) [r0 R_pi + t T_pi] >= (r/r0)*r0*L = r*L`.

The original root-only `pi0` attains `r*L`, proving the full interval exactly. This uses only positive costs and the previously proved finite optimum at the endpoint. The same argument also proves that, for `r<r0`, any policy involving a positive-probability terminal readout is strictly worse than `pi0`. Endpoints: `r=t/2` is included; `r=0` is excluded from the positive-price Bellman termination argument but gives a formal zero-price infimum by evaluating the root-only policy.

## 5. Verification, provenance and next useful mathematical problems

Run (from the evidence directory):

`python3 VERIFY_EC49FPS.py EC49FPR_EVIDENCE_20261115`

`python3 VERIFY_EC49FPS_WITNESS_INDEPENDENT.py EC49FPR_EVIDENCE_20261115 EC49FPS_CONFIG_WEIGHTED_HALF_PRICE_CERT.json`

The first program checks the two frozen original SHA256 hashes, recreates legal root-domain classes and complete terminal/root measurements, validates weights against the earlier EC49FPN certificate, proves the exact Bellman optimum and writes the complete witness plus every first-action cost. The second independently parses the raw source, checks all 242 original responses and the weighted histogram. Both were run successfully. The earlier EC49FPR `37/28` half-price endpoint was already verified on the same science pin, and its machine certificate was inspected to confirm the witness uses only root readouts.

Open mathematical questions: identify exact first policy-change price ratio **above** `r/t=1/2` under each prior; determine whether there is an interval with a mixed root-and-terminal optimal tree; study the observer-preserving repair for the class 16943 terminal-invisible named-root residual. The previously reported complete-class classification coverage remains 565/625; the present work optimizes an already classified class and adds no new classified domain.
