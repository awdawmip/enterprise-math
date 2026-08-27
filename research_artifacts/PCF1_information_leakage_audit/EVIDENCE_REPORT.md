# PCF1 Prime-Coordinate Factor Information-Leakage Audit — Evidence Report

Status: `FROZEN RESEARCH RETURN CANDIDATE / AUDIT_COMPLETE_WITH_ADMISSIBLE_SET`  
Task-ID: `RS-PRIME-COORD-FACTOR-INFORMATION-LEAKAGE-AUDIT`  
Publication: `TP2-FFE7E8757053C4F4030A`  
Researcher-ID: `EM-PCF1-FC7357`  
Execution branch: `research/prime-coord-factor-information-leakage-audit-em-pcf1-fc7357`  
Execution base: `c7a5a1c148f48f3c9d57cafe79536030541ed2d5`  
Whitelisted source pin: `8e8ec2fde8adeb4c75580075d63ac76adc562536`

## 1. Executive verdict

Primary verdict:

`AUDIT_COMPLETE_WITH_ADMISSIBLE_SET`

The audit finds a sharp distinction between **decoding a factor split once asymmetric local data are already present** and **constructing that asymmetry from an unfactored integer**.

The current Enterprise corpus contains several exact gcd decoders, most strongly Prime Fusion T5/T6/T11. Those decoders are mathematically genuine. However, the source-guaranteed residues, channel idempotents and oriented mixed phases are built from a cell/channel description that already determines the factors. They therefore do not satisfy the frozen algorithmic interface `(N,s) -> observable` for arbitrary unfactored `N`.

At the same time, the fixed Prime Fusion polynomials can be evaluated at a public seed `x=s mod N` without a factor oracle. This produces legitimate factor-blind gcd probes. They are retained as benchmark baselines, not promoted to a speedup: the exact CRT support count is fixed-degree root support, so uniform-seed amplification is square-root-scale on balanced semiprimes.

The missing object is therefore precise:

`N_ONLY_ASYMMETRY_GENERATOR`

namely a constructor from `(N,s)` alone whose hidden CRT projections desynchronize with proved non-negligible frequency or on an explicit infinite family, and whose difference can be integerized into a nontrivial gcd.

## 2. Sources audited

All 15 whitelisted entries from the immutable PCF1 taskbook were audited at `8e8ec2fde8adeb4c75580075d63ac76adc562536`:

1. `ENTERPRISE_BRC_HALF_COUPLING_BLIND_PADIC_FINGERPRINT_20260826.md`;
2. `ENTERPRISE_BRC_HALF_COUPLING_PADIC_ALL_PRIME_PROOF_20260827.md`;
3. `ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_20260827.md`;
4. `PERFECT_PRIME_TABLE_CRITICAL_COFACTOR_ALL_M_PROOF_20260826.md`;
5. `HIGHDIM_PRIME_WALL_FILTER_ALGEBRA_EQUIVALENCE_AUDIT_20260823.md`;
6. `PRIME_NATIVE_FILAMENT_SHARP_BOUND_INDEPENDENT_REPLICATION_20260823.md`;
7. `NATIVE_SHELL_GRADE_MONOTONE_INTEGER_ALLOCATION_FOUNDATION_AUDIT_20260827.md`;
8. `NATIVE_TRISECTOR_P0P1_ARITHMETIC_BRIDGE_FOUNDATION_GENERATIVITY_20260826.md`;
9. `PRIME_FUSION_T4_T7_T8_FINAL_EXACT_CLOSURE_20260823.md`;
10. `PRIME_FUSION_PHASE_EXTENSION_TARGETED_INDEPENDENT_VERIFICATION_20260823.md`;
11. `PRIME_FUSION_FINAL_SOURCE_REPAIR_AND_PACKAGE_FREEZE_20260824.md`;
12. `PRIME_FUSION_F1_LEAN_FINITE_ALGEBRA_FORMALIZATION_20260824.md`;
13. `PACKET_PATH_FOUNDATION.md`;
14. `RELATIONAL_AXIS_CONVENTION.md`;
15. `THREE_DIMENSIONAL_RELATIONAL_AXIS_CONVENTION.md`.

One exact dependency was opened because it is load-bearing for the input-model decision: the frozen Prime Fusion theorem package blob `055bdaaca81c5ac7ab350a71acf3b69fe5e564a9`. It states explicitly that an interior cell `(a,b)` defines `N(a,b)=a^2+b^2`, `C(a,b)=a^2-ab+b^2`, `H=N*C`, the pointed residue `r=-a*b^(-1) mod H`, and the T5/T6/T11 gcd decoders.

## 3. Exact audit lemmas

### Lemma A — coordinate witness leakage

Suppose a target integer is represented as

`H=(a^2+b^2)(a^2-ab+b^2)`,

with both factors nontrivial.

Then input `(a,b)` already yields the factorization in polynomial time by evaluating

`N(a,b)=a^2+b^2`,  
`C(a,b)=a^2-ab+b^2`.

Therefore the source Prime Fusion cell witness is not an admissible algorithmic input for an arbitrary target `H`. T4/T5 may decode the same split in richer algebraic language, but they do not remove this information dependency.

### Lemma B — a nontrivial idempotent is equivalent to a coprime factor split

Let `H>=2` and let `e^2=e mod H`. Define

`A=gcd(e,H)`,  
`B=gcd(e-1,H)`.

For each prime power `l^k || H`, idempotence gives `l^k | e(e-1)`. Since `gcd(e,e-1)=1`, the entire prime power divides exactly one of `e` and `e-1`. Hence

`gcd(A,B)=1`,  
`A*B=H`.

Thus a nontrivial idempotent (`1<A<H`) immediately factors `H`.

Conversely, for every coprime split `H=AB`, CRT gives a unique idempotent satisfying

`e=0 mod A`,  
`e=1 mod B`.

Therefore producing a nontrivial idempotent and producing a nontrivial coprime factor split are polynomial-time interreducible. The T6 Boolean collapse is an exact **factor certificate/decoder**. It becomes an extractor only after an N-blind mechanism generates the idempotent.

### Lemma C — exact support of a public-seed polynomial gcd probe

Let `H=pq` with distinct primes. Let `P` be a polynomial and let `r_p`, `r_q` be its numbers of roots modulo `p`, `q`.

For uniform `x mod H`, the gcd `gcd(H,P(x))` is nontrivial exactly when `P(x)` vanishes modulo one hidden factor and not the other. CRT gives the exact number of successful residues:

`r_p(q-r_q)+r_q(p-r_p)`.

Therefore

`Pr(success)=r_p/p+r_q/q-2*r_p*r_q/(pq)`.

If `P` is nonzero modulo both factors and has degree `d`, then

`Pr(success) <= d/p+d/q`.

This applies directly to the public-seed audit probes derived from the Prime Fusion fixed polynomials:

- `P_1(x)=x^2+1`;
- `P_2(x)=x^2+x+1`;
- `P_+(x)=x^6+1`;
- `P_-(x)=x^6-1`.

### Lemma D — balanced-semiprime cost boundary

If `p,q >= alpha*sqrt(H)` for a balanced semiprime family, a fixed-degree public-seed polynomial probe has

`Pr(success)=O(H^(-1/2))`.

Consequently independent uniform-seed amplification needs

`Omega(sqrt(H)) = 2^Omega(n)`

expected trials, where `n=ceil(log2 H)`, unless a new N-native mechanism provably biases the seed/state distribution toward factor-asymmetric local behavior.

This is the exact boundary between the existing gcd formula and the missing factorization breakthrough.

## 4. Route classification

| Route | Algorithmic classification | Main reason |
|---|---|---|
| BRC blind p-adic fingerprint | `FACTOR-CONDITIONAL / ENUMERATIVE / DESCRIPTIVE` | the input index is prime `p`; for factoring `N`, that is hidden factor data |
| BRC all-prime proof | `FACTOR-CONDITIONAL / ENUMERATIVE / DESCRIPTIVE` | exact prime-local theorem, no N-native constructor |
| inert finite Clausen bridge | `FACTOR-CONDITIONAL / ENUMERATIVE / DESCRIPTIVE` | prime and prime class are part of the input |
| Perfect Prime Table critical cofactor | `N-BLIND / DESCRIPTIVE` | public `m` object, but no `N -> support` or divisor-coverage map |
| high-dimensional prime wall/filter | `N-BLIND / ENUMERATIVE / DESCRIPTIVE` | exact counts are factor-blind from definitions but can be value-scale |
| native prime filament | `N-BLIND / DESCRIPTIVE` | local primality/neighbor structure has no gcd bridge |
| native shell allocation | `N-BLIND / DESCRIPTIVE` at invariant level | pointwise serialization remains a semantic/gauge dependency |
| native tri-sector P0/P1 bridge | `N-BLIND / DESCRIPTIVE` | semantic bridge, factor-neutral |
| Prime Fusion T4/T7/T8 | `FACTOR-CONDITIONAL / DESCRIPTIVE` | cell/channel witness already reveals factors |
| Prime Fusion phase extension | `FACTOR-CONDITIONAL / DESCRIPTIVE` | mixed phases are defined on factor-labelled local components |
| Prime Fusion T1-T15 final package | `FACTOR-CONDITIONAL / DESCRIPTIVE` for source guarantees | one-gcd decoders are exact but source witnesses are factor-resolved |
| Prime Fusion F1 Lean | same input-model classification | formalization verifies decoder theorems, not an N-only generator |
| Packet/Path Foundation | `N-BLIND / DESCRIPTIVE` | factor-neutral counting substrate |
| Relational Axis Convention | `N-BLIND / DESCRIPTIVE` | public relational chart; axis signs are gauge |
| 3D Relational Axis Convention | `N-BLIND / DESCRIPTIVE` | factor-neutral compatibility carrier |

The complete field-by-field matrix is machine-readable in `audit_bundle.json`.

## 5. Admissible N-blind registry

The audit admits the following input-safe classes:

1. packet/path counts on a public N-native carrier;
2. relational transfer data with gauge carried explicitly;
3. frame-invariant native shell grades/counts/orbits;
4. prime-wall/filter counts when computed without factor inputs and with full support cost charged;
5. local filament predicates when the label allocation and neighborhood are public/non-postselected;
6. public-seed Prime Fusion polynomial gcd probes `gcd(N,x^2+1)`, `gcd(N,x^2+x+1)`;
7. public-seed sixth-power probes `gcd(N,x^6-1)`, `gcd(N,x^6+1)`.

Items 6–7 are `EXTRACTIVE` only in the narrow per-seed sense that a nontrivial gcd is a valid factor. Their currently proved uniform-seed search cost is `ENUMERATIVE / square-root-scale`; they are benchmark baselines, not a claimed improvement.

## 6. Conditional/rejected registry

The following may be used only proof-side or as verifier data until separately repaired:

- BRC `R_p(m)`, `S_p` and inert-prime objects when `p` is a hidden divisor of target `N`;
- Prime Fusion target cell `(a,b)` for `H`, because it directly computes the channel factors;
- source pointed residue `r=-a*b^(-1) mod H`;
- nontrivial idempotent `e`;
- factor-labelled oriented mixed locus `M_{p,q}`;
- T11's source-guaranteed `x in M_{p,q}`;
- critical-cofactor candidate support until an N-native support map and divisor-coverage theorem exist;
- distinguished pointwise shell serialization unless its native semantic status is independently resolved.

No quantity is repaired by merely renaming factor labels as coordinates or phases.

## 7. Cross-route information map

The BRC p-adic family and the Prime Fusion family fail the N-only gate for different reasons:

- BRC is **prime-indexed**: the local prime is required before the observable is formed.
- Prime Fusion is **witness/channel-indexed**: after the cell/root/idempotent is supplied, the split is exact and cheap, but the witness already contains the split.

The packet/path, shell and relational-axis families are genuinely factor-blind but currently factor-neutral.

The prime-wall and filament families can carry arithmetic response without a factor oracle, but no current source provides a sub-square-root support theorem or gcd-ready asymmetry.

Thus the program is not missing another decoder. It is missing a constructor that generates local asymmetry before the factorization is known.

## 8. Downstream gate

`downstream_gate.json` freezes the exact allowed/forbidden input surface.

PCF1 is sufficient to release the audit dependency for:

- `RS-PRIME-COORD-FACTOR-BLIND-BENCHMARK-SUITE`;
- `RS-PRIME-COORD-FACTOR-HIDDEN-FACTOR-SEPARATION-SPECTRUM`;
- `RS-PRIME-COORD-FACTOR-BLIND-PADIC-GCD-BRIDGE`;
- `RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION`.

The critical-cofactor support-compression lane still additionally depends on its all-`m` parent result as published.

For every downstream lane, hidden `p,q`, factor-derived phases, coordinate witnesses, nontrivial idempotents and mixed-locus membership are verifier/proof data only.

## 9. Reproducible regression evidence

Checker:

`scripts/check_pcf1_information_leakage_audit.py`

It verifies:

- the 15-row audit schema;
- the H=91 Prime Fusion regression `(a,b)=(2,3)`, `(N,C,H,r)=(13,7,91,60)`;
- T5, T6 and T11 gcd splits on that witness;
- the idempotent factor-split law for every idempotent modulo every `2<=H<=250`;
- the exact public-seed polynomial support formula for four fixed polynomials across all distinct primes `5..43`.

Authoring-time local execution result:

`PCF1_AUDIT_CHECK_PASS routes=15 idempotent_H<=250 probe_primes<=43 H91=PASS`

The finite checks are regression support only; the general statements in Section 3 are proved arithmetically.

## 10. Final classification

`PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_COMPLETE = true`

`PRIMARY_VERDICT = AUDIT_COMPLETE_WITH_ADMISSIBLE_SET`

`CURRENT_SOURCE_LEVEL_N_ONLY_SPEEDUP = NOT_ESTABLISHED`

`CURRENT_EXACT_GCD_DECODER = ESTABLISHED`

`PROGRAM_LEVEL_MISSING_OBJECT = N_ONLY_ASYMMETRY_GENERATOR`

This audit does not prove that such a generator cannot exist. It proves that none of the audited source-guaranteed factor-sensitive objects may be treated as that generator without circularly importing the factor split, and it fixes the factor-blind baseline against which any successor must improve.
