# PFSSV finite-window null contract and identifiability — researcher report

Researcher: `EM-PFN-D67A51`  
Task: `RS-PFSSV-FINITE-WINDOW-NULL-IDENTIFIABILITY`  
Publication: `TP2-38717785C4ADF3A12A49`  
Claim: `claim-PFN-autoB-20260917-043700-88c8edc7`  
Activity: `RA-20260917-AUTOB-PFN-D67A51-88C8EDC7`

## 1. Result in one sentence

The frozen finite geometry determines a coherent **support carrier**, but it does not identify a probability law. A shared-q address surrogate can be made capacity-coherent, yet even after conditioning on the exact unique occupied-address total in every `q mod 30` residue class there are two full-support laws with different distributions for the same shared-address target. Therefore the scientifically relevant null is not identified without an extra exchangeability/invariance/weighting premise. A uniform finite-window law is usable only as a stipulated synthetic surrogate, not as a theorem about deterministic primes.

Disposition proposed by the researcher: `NEGATIVE_BOUNDARY / EXACT_IDENTIFIABILITY_OBSTRUCTION_WITH_STIPULATED_SURROGATE_AVAILABLE`. The parent semiprime residual hard target remains open.

## 2. Frozen evidence used

No new scientific sampling was performed. The research consumes the already accepted generation-2 finite observation/support package:

- taskbook `research_tasks/PFSSV_FINITE_WINDOW_NULL_IDENTIFIABILITY_20260908.md`, blob `sha1:7a96af089d96b37a559fa5c564f7ce5d3a5444ef`;
- accepted parent Result `RR-BDA72F26E3786AD69EA5`, source commit `24d314560a35cefe14d240deb3b44ed7cc24fa38`, owner head `a82ced7bb227471c1b16fecb5a5e3d7ff72a5536`;
- parent exact observation/capacity return and Driver acceptance;
- Driver-reviewed external prior-art memo `driver_reviews/PFSSV_GENERATION2_STAGE2_EXTERNAL_PRIOR_ART_20260908.md`;
- parent BRC/native receipt with lossless trace SHA256 `efc2bedcda8da81f9948098943815011024c2c6d2e7711f209151ed983192fa4`.

The old accepted boundary is retained unchanged: in the `X=100000`, width `1/100` cell, the original scalar Null A can move a residue-11 count from row `p=193` to row `p=163` with positive probability, but the target integer window `[614,619]` has no residue-11 slot. This refutes the universal factor-window occupancy interpretation of that scalar permutation, not every finite conditional randomization model.

## 3. BRC / observer applicability audit

BRC is applicable here as a **typed finite carrier and observer audit**, not as a source of stochastic probabilities.

| BRC audit item | Frozen interpretation in this task |
|---|---|
| Population | The 21 already exposed finite cells; the exact witness below uses only `(X,width)=(100000,1/100)`. |
| Branch identity | `cell -> p-row -> integer q-address -> residue channel`; one q-address retains one identity wherever windows overlap. |
| Composition | Row/channel counts are incidence sums over shared q-address indicators. Duplicating one q separately per row is forbidden when the integer address is shared. |
| Observables | Row total, residue-channel count, zero-row status, diagonal, overflow, raw/rank/derived profiles. |
| Future operations | Exact conditioning, finite weighting, exact support checks and deterministic verification only. No random scientific screen in this task. |
| Scale | Fixed finite windows only; no all-scale or asymptotic conclusion. |
| Observer firewall | Actual primality is deterministic observed data. A random address indicator is an additional surrogate model and must be labelled as such. Branch multiplicity or BRC structure does not itself create probability. |

This is the narrowest adequate carrier for the present question. The native address `D(pq)=(p,q,0)` is preserved; S3/rank/density-flat outputs remain derived observations. Nothing below promotes a probability model to P000, Working Truth, a prime-process theorem or a physical interpretation.

## 4. Typed semantic matrix

Fix one finite cell with lower endpoint `X` and exact upper endpoint `U`. For every prime `p <= floor(sqrt(U))` with nonempty factor window define

`W_p = [max(p, floor(X/p)+1), floor(U/p)] ∩ Z`.

Let `Q = union_p W_p` be the finite set of **integer q-addresses**, and let

`B[p,q] = 1(q in W_p)`.

The following types must not be conflated:

| Object | Type | Frozen/random status | Contract role |
|---|---|---|---|
| `W_p` and `B[p,q]` | integer geometry/incidence | deterministic | defines legal slots and overlap |
| `a_q = 1{q is prime}` | actual primality | deterministic exposed observation | not randomized or proved stochastic |
| `Z_q in {0,1}` | shared occupied-address surrogate | random only after a law is stipulated | one variable per integer q; shared across every incident row |
| `N_p(Z)=sum_q B[p,q] Z_q` | row count | derived random observable | cannot exceed row slot capacity |
| `N_{p,r}(Z)=sum_{q≡r mod30} B[p,q] Z_q` | row/residue-channel count | derived random observable | cannot exceed integer residue capacity |
| `K_r(Z)=sum_{q∈Q,q≡r mod30} Z_q` | unique-address residue margin | selected conditioning statistic | fixed in the bounded surrogate below |
| zero observed row | statement `N_p(a)=0` | observed deterministic fact | retained; forcing `N_p(Z)=0` would be an additional conditioning choice |
| overflow | existing row/view flag (`p^2>X`) | deterministic label | retained separately; never clipped into another bin |
| probability measure on `Z` | statistical assumption | **not** supplied by geometry | must be explicitly chosen and normalized |
| inferential target | declared statistic `T(Z)` | model-dependent distribution | deterministic observed value `T(a)` is calibrated only conditional on the chosen law |

Integer capacity is therefore a support property. It is necessary for an occupancy interpretation but is not a probability law and cannot prove exchangeability.

## 5. A coherent finite shared-address surrogate

For a fixed cell, compute from the exposed actual prime vector the unique-address residue totals

`K_r* = sum_{q∈Q, q≡r mod30} a_q`.

Define the finite fiber

`Omega_K = {z∈{0,1}^Q : sum_{q≡r mod30} z_q = K_r* for every residue r}`.

Every `z∈Omega_K` uses one shared variable per q-address, so overlaps are automatically consistent. Every row/channel count is an incidence sum of binary slots and therefore satisfies integer slot capacity. Residues with `K_r*=0` become exact structural zeros at the address level. Zero **rows** are not silently discarded: their geometry stays in `B`; whether a zero observed row is itself conditioned to remain zero is a separate modelling decision. Overflow rows are likewise retained and labelled rather than clipped.

Two example laws on the exact same fiber are:

**Contract U (uniform address-residue surrogate).**

`P_U(z) = 1/|Omega_K|` for all `z∈Omega_K`.

This is mathematically coherent, but its uniformity is a stipulated exchangeability premise within each residue class. It is not proved from primality or the Enterprise Math carrier.

**Contract W (positive weighted address-residue surrogate).**

Choose positive address weights and define

`P_W(z) ∝ product_q w_q^{z_q}` on `Omega_K`.

The bounded witness below uses `w_419=2` and `w_q=1` for every other address. This law has exactly the same support, the same residue totals and the same shared-address consistency as Contract U, but a different target distribution.

The statistical object that either contract can calibrate is only a declared statistic of this surrogate, for example `T(BZ)`. A tail probability such as `P_U(T(BZ)>=T(Ba))` is a **surrogate-conditional calibration statement**. It is not evidence that actual deterministic prime data were generated by `P_U` unless an additional premise connects primality to that law.

## 6. Exact constructive nonidentifiability witness

The bounded checker `research_checks/PFSSV_FINITE_WINDOW_NULL_IDENTIFIABILITY_D67A51.py` uses only exact integer arithmetic, a finite Eratosthenes sieve and rational identities. It performs zero random draws.

For the frozen cell `X=100000`, width `1/100`, `U=101000`, it reproduces the accepted cell totals:

- 66 geometric rows;
- 15 zero-total rows;
- 237 raw prime-pair incidences;
- one diagonal incidence;
- one overflow incidence.

It then forms the union of integer q-addresses and obtains exactly:

- `|Q| = 2016` integer slots;
- 236 **unique** actual prime q-addresses;
- five integer q-addresses shared by two p-rows: `322,356,372,419,441`;
- only one of those shared addresses is actually prime: `q=419`, shared by rows `p=239` and `p=241`.

The corresponding windows are

- `W_239=[419,422]`, whose actual primes are `419,421`;
- `W_241=[415,419]`, whose only actual prime is `419`.

Thus the accepted raw pair count `237` is one larger than the 236 unique prime addresses precisely because the same prime address `q=419` is incident to two rows. This is a concrete reason that a coherent q-address model cannot treat every row's q realization as an independent copied object.

Now restrict attention to residue `29 mod 30`. In `Q` there are 69 such integer addresses and the actual unique prime vector occupies 29 of them. Both Contract U and Contract W condition on the same exact residue total `K_29=29` and have full support on all `29`-subsets of those 69 addresses.

Take the target

`T(z)=z_419`.

Under Contract U, symmetry gives

`P_U(T=1)=29/69`.

Under Contract W with only `w_419=2`,

`P_W(T=1) = 2*C(68,28) / (C(68,29)+2*C(68,28)) = 29/49`.

Therefore

`29/69 != 29/49`.

The two laws have the same finite geometry, the same shared q-address carrier, the same integer capacities, the same exact residue totals, the same zero/nonzero admissible address support, and positive mass on every configuration in the common fiber; nevertheless they assign different distributions to the same shared-address target. The probability law is not identified by those structural constraints.

This is not a Monte Carlo discrepancy. It is an exact finite combinatorial separation.

## 7. General identifiability theorem for any stronger finite conditioning

Let `Omega_c` be any finite set of shared-address configurations obtained by adding declared deterministic constraints such as selected row margins, channel margins, structural zeros or other finite-window conditions. Let `T:Omega_c -> R` be the statistic intended for calibration.

**Proposition (finite-support probability identifiability trichotomy).**

1. If `Omega_c` is empty, the proposed contract is inconsistent.
2. If `T` is constant on `Omega_c` (in particular if `Omega_c` is a singleton), the distribution of `T` is identified but degenerate; that conditioning supplies no nontrivial null variability for `T`.
3. If `T` is nonconstant on `Omega_c`, support/conditioning alone does not identify its distribution. There exist at least two strictly positive probability laws on the same `Omega_c` with different distributions of `T`.

**Proof.** In case 3 choose any strictly positive baseline law `P_0` on the finite set. For real `theta`, define

`P_theta(omega)=exp(theta*T(omega)) P_0(omega) / Z(theta)`.

Every `P_theta` has exactly the same support and obeys every deterministic constraint used to define `Omega_c`. Because `T` is nonconstant, its moment generating normalizer is nontrivial and the law of `T` varies with `theta`; equivalently one may tilt two configurations with different `T` values. Hence the constraints do not identify a unique target distribution. QED.

This proposition resolves the possible objection that more row/channel margins might repair identifiability by themselves. They can make the fiber smaller, empty or degenerate, but if a nontrivial target still varies, a probability/invariance premise is still required.

## 8. What is assumed and what is proved

### Proved or exactly verified in scope

- the old scalar Null A occupancy interpretation has the already accepted capacity obstruction;
- a one-variable-per-q shared-address carrier is capacity coherent by construction;
- the exact `X=100000,1/100` cell has the shared-address facts and counts listed above;
- the two explicit laws U and W share the same finite support and exact residue-total conditioning but give `P(Z_419=1)=29/69` and `29/49` respectively;
- deterministic support constraints alone identify a nonconstant target distribution **only after** an additional probability law/invariance premise is supplied.

### Assumed only if a user later chooses Contract U

- conditional exchangeability of q-address occupancy within each declared residue fiber;
- uniform weighting of all compatible address configurations.

### Assumed only if a user later chooses a weighted contract

- the specified positive weights, including their scientific interpretation if any.

### Not proved

- that primes are exchangeable within residue classes or finite windows;
- that any `P_U`/`P_W` surrogate is the data-generating law of primality;
- that a surrogate p-value has a frequentist interpretation for deterministic prime data absent a justified random mechanism;
- that semiprime residual structure exists or does not exist;
- that the original exposed holdouts regain blindness;
- that a finite-cell result extrapolates to all scales.

## 9. Prior-art and tool reuse table

| Antecedent/tool | Reuse in this task | Boundary retained |
|---|---|---|
| Hemerik–Goeman, exact random permutations | Principle that exact permutation inference needs invariance under the stated null | no invariance of prime rows is granted |
| Rapallo–Yoshida, bounded contingency-table fibers | Finite constrained-support viewpoint and structural-zero discipline | shared-q incidence is not automatically a standard fixed-margin table; connectivity does not select probabilities |
| Berrett–Wang–Barber–Samworth, conditional permutation | Nonuniform conditional weights are legitimate model components when the mechanism is specified | their conditional mechanism is not a prime-process theorem |
| Amarasingham et al., finite-window jitter supplement | Example that a uniform finite fiber can be a declared conditional null | neural-window exchangeability does not transfer to factor windows |
| SciPy `random_table` prior-art note | Fixed-margin sampler as adjacent implementation reference | lacks arbitrary shared-address/capacity constraints and is not used here |
| Existing PFSSV BRC DIV/ROOT/LOG traces | Frozen exact geometry and observation provenance | not rerun as a new scientific experiment; BRC supplies no probability law |
| New checker D67A51 | Exact bounded support/shared-address/combinatorial witness | no random draws, no all-scale claim, no global tool registration |

No new external literature search was needed; the task explicitly supplied the Driver-reviewed bounded prior-art memo.

## 10. Decision for the hard target

The hard target is resolved at the declared finite-model scope by an **exact missing-assumption/nonidentifiability boundary**.

A coherent finite contract can be written, for example Contract U, but only with the explicit label `STIPULATED_SYNTHETIC_SURROGATE`. Its inferential target is limited to the distribution of a declared statistic under that surrogate. The frozen geometric/capacity/residue/shared-address constraints do not uniquely select Contract U, because Contract W satisfies the same declared structural constraints and changes the target distribution exactly.

Consequently there is no justified path from the current frozen evidence to a unique scientific prime null without supplying a new premise such as a specified invariance group, an address-specific conditional mechanism, or scientifically justified weights. Choosing such a premise after inspecting exposed outcomes would define a new estimand/model and would not restore the historical blind gate.

The correct return is therefore not a new 512/4096 screen. It is a `NEGATIVE_BOUNDARY` on identifiability, together with an explicit usable-but-stipulated finite surrogate specification.

## 11. Replay / verification

Run:

`python research_checks/PFSSV_FINITE_WINDOW_NULL_IDENTIFIABILITY_D67A51.py`

Expected status:

`PASS_EXACT_BOUNDED_NONIDENTIFIABILITY_WITNESS`

The preserved receipt is `research_notes/pfn_null_identifiability_d67a51/verification_receipt.json`. The local checker execution used zero random draws and passed all assertions before publication.

## 12. Residue and next legitimate action

The following remain open and are not silently converted to failures:

- deterministic semiprime residual structure;
- a scientifically justified stochastic mechanism for primes or a declared external randomization device;
- valid family-wise residual calibration under such a mechanism;
- any future honest holdout, which must be newly designed because the historical holdouts are exposed.

Driver review should decide whether the finite synthetic surrogate has enough scientific value to justify a separately specified future experiment. This researcher does not start that experiment, does not invent a blind reset and does not promote this finite obstruction beyond its scope.
