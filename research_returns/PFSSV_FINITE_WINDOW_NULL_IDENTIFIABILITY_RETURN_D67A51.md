# PFSSV finite-window null identifiability return

Status: `RESEARCH_RETURN_FROZEN_CANDIDATE / AWAITING_DRIVER_REVIEW`

Task: `RS-PFSSV-FINITE-WINDOW-NULL-IDENTIFIABILITY`  
Publication: `TP2-38717785C4ADF3A12A49`  
Execution: `ER-99877B70D038535256A3`  
Claim: `claim-PFN-autoB-20260917-043700-88c8edc7`  
Researcher: `EM-PFN-D67A51`

## Disposition

Researcher verdict: `NEGATIVE_BOUNDARY`.

Hard-target disposition: `FINITE_WINDOW_NULL_CONTRACT_EXACTLY_NONIDENTIFIED_WITH_STIPULATED_SURROGATE_AVAILABLE`.

The finite geometry and shared-q address constraints determine a support carrier but do not identify a probability law. A coherent address-level surrogate can be specified, but its calibration is conditional on an additional exchangeability/weighting premise that is not supplied by primality, capacity, BRC, or the frozen observations.

## Exact bounded result

For the accepted frozen cell `X=100000`, width `1/100`, `U=101000`, the exact checker reproduces 66 geometric rows, 15 zero-total rows, 237 raw prime-pair incidences, one diagonal incidence and one overflow incidence.

Let `Q` be the union of all integer q-addresses in the fixed p-row windows. The checker finds:

- `|Q|=2016`;
- 236 unique actual prime q-addresses;
- shared integer q-addresses `322, 356, 372, 419, 441`;
- the only shared address that is actually prime is `q=419`, incident to `p=239` and `p=241`.

The shared-address model uses one binary surrogate variable `Z_q` per integer q-address. Row/channel counts are incidence sums of the same `Z_q` wherever q is shared. This automatically satisfies integer slot capacity and shared-address consistency.

Condition on the exact unique occupied-address total `K_r` in every residue class `q mod 30`. In residue 29 there are 69 integer q-addresses and the actual vector occupies 29.

Two laws on the same finite fiber are then:

1. `U`: uniform on all configurations with the fixed residue totals;
2. `W`: the same support and residue totals, but assign address weight 2 to `q=419` and weight 1 to every other address (other residue fibers remain uniform).

For target `T(Z)=Z_419`,

`P_U(T=1)=29/69`,

while

`P_W(T=1)=2*C(68,28)/(C(68,29)+2*C(68,28))=29/49`.

Thus `P_U(T=1) != P_W(T=1)` although both laws preserve the same fixed geometry, capacities, shared-q identity and exact residue totals. The null law is not identified by those structural constraints.

More generally, for any finite constraint fiber `Omega_c`: if it is empty the contract is inconsistent; if the target is constant the target law is degenerate; otherwise positive exponential tilts on the same fiber give different target distributions. Adding row/channel margins can shrink the fiber but cannot by itself select a unique probability law unless it makes the target degenerate.

## Stipulated finite surrogate that is actually coherent

A usable synthetic contract is:

- random object: shared binary q-address occupancy `Z`;
- sample space: exact finite fixed-window address configurations;
- conditioning: declared `K_r` residue totals (or another explicitly declared deterministic fiber);
- law: uniform or a separately declared positive weighting;
- observable: row/channel counts obtained through the fixed incidence map;
- inferential target: only a declared statistic under that surrogate.

Uniformity means conditional exchangeability within the declared fiber. It is an assumption, not a proved prime-process invariance. Therefore a p-value or quantile from this contract is a `STIPULATED_SYNTHETIC_SURROGATE` calibration and does not by itself establish a frequentist law for deterministic primes.

Zero observed rows remain part of the geometry; forcing them to remain zero is an additional conditioning decision. Overflow remains separately labelled and is not clipped. The native address `D(pq)=(p,q,0)` is preserved; rank/S3/density-flat coordinates remain derived observations.

## Validation and provenance

No scientific random draw was performed.

Exact checker:
`research_checks/PFSSV_FINITE_WINDOW_NULL_IDENTIFIABILITY_D67A51.py`

Receipt:
`research_notes/pfn_null_identifiability_d67a51/verification_receipt.json`

Detailed BRC/observer audit and proof:
`research_notes/pfn_null_identifiability_d67a51/REPORT.md`

The checker passed locally with status:
`PASS_EXACT_BOUNDED_NONIDENTIFIABILITY_WITNESS`.

It also reproduces the accepted old capacity witness `p=193 -> p=163`, residue 11, where the target integer residue capacity is zero.

The parent accepted BRC/native trace is reused as frozen provenance; it is not rerun or promoted. Prior-art reuse is restricted to the Driver-reviewed memo: permutation validity requires stated invariance; bounded-table/finite-window methods supply antecedents but do not provide this prime law; nonuniform conditional weights are an explicit mechanism rather than a geometric consequence.

## What remains unproved

This return does not prove or refute deterministic semiprime residual structure. It does not justify prime-process exchangeability, recover historical blindness, complete a family-wise residual screen, establish a new joint prime null, register a global tool, or extrapolate from the finite witness to all scales.

## Control-plane recommendation

Freeze this researcher return for independent Driver review. Treat the finite statistical-contract question as resolved by an exact identifiability obstruction plus a clearly labelled synthetic surrogate. Do not start the suspended 512/4096 scientific screen from this return. A future experiment is legitimate only if a separate scientifically justified random mechanism/invariance premise is supplied and its post-exposure status is honestly declared.

Researcher-ID: EM-PFN-D67A51 / RS-PFSSV-FINITE-WINDOW-NULL-IDENTIFIABILITY
