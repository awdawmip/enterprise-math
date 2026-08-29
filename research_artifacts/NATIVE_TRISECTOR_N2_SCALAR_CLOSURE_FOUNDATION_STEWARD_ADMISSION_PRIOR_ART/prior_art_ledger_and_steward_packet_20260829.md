# Native Tri-sector N2 — External Prior-art Ledger and Steward-facing Packet

Status: `PRIOR_ART_GATE_RESOLVED / STEWARD_DISPOSITION_PENDING_EXPLICIT_AUTHORITY / TASK_NOT_TERMINAL`

Date: 2026-08-29
Researcher-ID: `EM-NTN2STW-1ECE8E`
Task: `RS-NATIVE-TRISECTOR-N2-SCALAR-CLOSURE-FOUNDATION-STEWARD-ADMISSION-PRIOR-ART`
Publication: `TP2-CB300EE2F5761F32C048`
Claim: `chatgpt-ntn2stw-20260829-1014-7c4d2a`
Execution branch base: `a13e0b93850552769e1fe8eb4953ea1baab38742`

## 1. Scope and non-overclaim rule

This packet freezes only the external duplication/lineage boundary for the Driver-accepted native `s=3` N2 scalar/set/relation consequence. It does not re-prove or widen that accepted theorem, does not change P0/P1 primitives, does not import physical rail/lane ontology, does not generalize to arbitrary odd `s`, does not reverse-derive native three-ness, and does not identify the two unrelated typed objects whose numerical value is `9`.

The maintained candidate consequence remains exactly

`native s=3 -> {5,7} -> 9 -> 35 -> 105 -> 53`

at N2 scalar/set/relation strength.

Prior-art absence is **not** a novelty theorem. The classifications below distinguish `EXACT_DUPLICATE`, `PARTIAL_ANTECEDENT`, `ADJACENT_METHOD`, and `NO_MATERIAL_MATCH`. A `NO_MATERIAL_MATCH` label means only that the targeted search used for this gate did not locate a materially identical external result.

## 2. Ledger summary

| ID | Accepted ingredient | External boundary | Classification | Consequence for this project |
|---|---|---|---|---|
| PA-01 | translated-square intersection `|Q0 ∩ (Q0+δ)|=(q+1+χ(δ)+χ(-δ))/4` and the resulting `q_b=5` case split | Paley quadratic-residue difference-set / partial-difference-set parameters give the intersection multiplicities directly after adjoining `0` | `EXACT_DUPLICATE` for the character/intersection identity; `PARTIAL_ANTECEDENT / DIRECT_APPLICATION` for the project-specific `δ=1/3`, coverage predicate, and `q_b=5` corollary | Do not claim novelty for the finite-field intersection mechanism. Preserve the native N2 predicate/type as an application-local consequence. |
| PA-02 | `a(r)=(3r^2+ε(r))/2 mod 5` has exact period `10`; across additive phases the sharp maximum consecutive nonzero run is `9` | Generic polynomial/congruence periodicity is elementary; targeted exact-pattern and formula searches located no materially identical theorem/package | `ADJACENT_METHOD` for modular periodicity; `NO_MATERIAL_MATCH` for the exact period-10 / five-phase / run-9 statement | Record as an application-local finite congruence lemma, with no novelty assertion. |
| PA-03 | three native quadratics can cover all nonzero residues only if `q-1<=6`, followed by exact `q=5,7` root tables | Standard field theorem: a nonzero degree-`d` polynomial has at most `d` roots; union bound gives at most six roots for three quadratics | `EXACT_DUPLICATE` for the degree/root-count mechanism; `PARTIAL_ANTECEDENT / APPLICATION_LOCAL` for the exact native triple and `{5,7}` saturation table | Do not claim novelty for the root-count obstruction. The exact three-polynomial packet remains a typed local instance. |
| PA-04 | for odd `k>=5`, same-parity distinct `u,v` and opposite-parity `w` in `{0,...,k-1}` maximize `|w-u||w-v|` at `(k-4)(k-2)`, with unique unordered distance pair `{k-4,k-2}` | Targeted searches for the exact one-dimensional parity-constrained product lemma located no material match; broad fixed-diameter product-of-distances literature is structurally different | `NO_MATERIAL_MATCH` for the exact lemma; `ADJACENT_METHOD / KEYWORD_NEIGHBOR` only for broad product-distance extremal literature | Keep the elementary endpoint/parity proof local; do not convert search absence into novelty. |

## 3. PA-01 derivation from classical Paley parameters

Let `D` be the nonzero quadratic residues of `F_q` and `Q0=D∪{0}`. For nonzero `δ`,

`|Q0 ∩ (Q0+δ)| = |D ∩ (D+δ)| + 1_D(δ) + 1_D(-δ)`.

Classical Paley residue sets supply the required difference multiplicities.

- If `q ≡ 3 (mod 4)`, the nonzero squares form a skew-Hadamard difference set with `λ=(q-3)/4`; exactly one of `δ,-δ` is a square. Hence the intersection is `(q+1)/4`.
- If `q ≡ 1 (mod 4)`, the nonzero squares form a Paley partial difference set with parameters `(q,(q-1)/2,(q-5)/4,(q-1)/4)`. If `δ` is a square, the intersection is `(q-5)/4+2=(q+3)/4`; if `δ` is a nonsquare, it is `(q-1)/4`.

These three cases combine to

`|Q0 ∩ (Q0+δ)|=(q+1+χ(δ)+χ(-δ))/4`.

For the accepted project instance `δ=1/3` and nonsingular odd primes `q∤6`, full two-set coverage is equivalent to intersection size `1`. Therefore:

- `q≡3 mod4` gives `(q+1)/4=1`, forcing `q=3`, excluded;
- `q≡1 mod4` with square `δ` gives `(q+3)/4>1`;
- `q≡1 mod4` with nonsquare `δ` gives `(q-1)/4=1`, forcing `q=5`.

Modulo `5`, `δ=1/3=2` is nonsquare, so the project-specific conclusion is `q_b=5`.

**Boundary:** the intersection identity is classical residue/difference-set mathematics. The native translated sets, typed `Break(q)` predicate, `δ=1/3`, and use inside the N2 consequence chain are application-local packaging, not evidence of external novelty.

## 4. PA-02 exact finite-period/run computation

For

`a(r)=(3r^2+ε(r))/2 mod 5`, `ε(r)=r mod 2`,

the exact values for `r=0,...,9` are

`[0,2,1,4,4,3,4,4,1,2]`.

The parity component repeats modulo `2` and the quadratic residue component repeats under `r -> r+10`, so period `10` follows; direct comparison against all proper positive divisors/candidates `<10` shows the minimal period is exactly `10` (in particular `a(0)=0` but `a(5)=3`).

For additive phase `H mod5`, the zero classes in one period are:

- `H=0`: `{0}`
- `H=1`: `{3,4,6,7}`
- `H=2`: `{5}`
- `H=3`: `{1,9}`
- `H=4`: `{2,8}`

Thus every phase has a zero each period, while `H=0` and `H=2` have a single zero per period, giving sharp cyclic/nonzero gap length `9`.

Targeted searches used the exact ten-term pattern, the formula `3r^2+parity` modulo `5`, and the phrase-level run-length structure. No materially identical external theorem/package was located. This is recorded only as `NO_MATERIAL_MATCH`; elementary modular periodicity itself is standard adjacent method.

## 5. PA-03 root-count obstruction and native saturation instance

For even shell `r=2m`, the accepted native packet is

`f_-(m)=6m^2-2m+1`,
`f_0(m)=6m^2+1`,
`f_+(m)=6m^2+2m+1`.

For nonsingular odd prime `q`, each is a nonzero polynomial of degree at most `2`, hence has at most two roots in `F_q`. Therefore the union of all three root sets has size at most `6`. Covering every nonzero residue requires

`q-1 <= 6`, hence `q<=7`.

The exact native root tables are:

- `q=5`: `{1} | {2,3} | {4}`;
- `q=7`: `{2,3} | {1,6} | {4,5}`.

Therefore the accepted saturation characteristic set is exactly `{5,7}`.

The polynomial root bound is standard algebra. The exact native triple and its two small-prime tables are an application of that standard theorem plus finite checking, not an externally established identity located in this search.

## 6. PA-04 mixed-parity extremal lemma

Let odd `k>=5`, `W_k={0,...,k-1}`; let `u,v` be distinct of the same parity and `w` have the opposite parity. Then `|w-u|` and `|w-v|` are positive odd integers at most `k-2`.

If the larger distance is at most `k-4`, the product is at most `(k-4)^2 < (k-4)(k-2)`. If one distance equals `k-2`, the second same-parity endpoint cannot be at that same location and its distance is at most `k-4`. Endpoint choices realize the pair `{k-4,k-2}`. Hence

`max |w-u||w-v|=(k-4)(k-2)`,

and every maximizing unordered distance pair is exactly `{k-4,k-2}`.

At `k=9` this yields `{5,7}`.

Targeted searches for same/opposite parity interval triples, maximum products of two distances, and the exact `{k-4,k-2}` signature found no materially identical result. A recent geometric paper on maximum products of distances for fixed-diameter point sets is only a broad keyword/method neighbor: it is not the same one-dimensional parity-constrained three-point statement and is not used as proof authority here.

## 7. Independent finite verification performed for this gate

These checks are regression evidence only, not theorem proofs.

1. For every prime `5<=q<1000` (166 primes), with `δ=1/3`, the direct set intersection `Q0∩(Q0+δ)` matched `(q+1+χ(δ)+χ(-δ))/4` exactly; direct two-set coverage occurred only at `q=5`.
2. For all nonsingular odd primes `q<1000`, direct roots of the three native quadratics saturated `F_q^*` exactly for `q in {5,7}`.
3. The ten-term scalar table above was reproduced exactly and the minimal positive period was verified to be `10`.
4. For every odd `k=5,7,...,101`, exhaustive enumeration of all admissible triples `(u,v,w)` (1,646,449 triples total) matched maximum `(k-4)(k-2)` and the only maximizing unordered distance pair was `{k-4,k-2}`.

## 8. Authoritative / relevant external sources

### Classical exact antecedent

- R. E. A. C. Paley, **On Orthogonal Matrices**, *Journal of Mathematics and Physics* 12 (1933), 311–320. DOI: `10.1002/sapm1933121311`.
- Vitor Araujo Garcia, **On group codes arising from Paley-type partial difference sets and skew–Hadamard difference sets**, *Designs, Codes and Cryptography* 94, article 92 (2026). DOI: `10.1007/s10623-026-01846-6`. This modern source explicitly records the Paley-type PDS parameters `(q,(q-1)/2,(q-5)/4,(q-1)/4)` and identifies Paley residue constructions as classical.

### Standard algebra antecedent

- MIT 18.310 lecture notes, **Polynomial Codes and some lore about Polynomials**, section proving that a degree-`k` polynomial over a field has at most `k` roots. Used only for the standard root-count obstruction.

### Negative-control adjacent literature

- Cambie, Decadt, Dong, Hu, Tang, **On the maximum product of distances of diameter 2 point sets**, arXiv:2603.07088 (2026). This is a geometrically different fixed-diameter product-distance problem and is recorded only to prevent a false keyword-level equivalence with PA-04.

## 9. Steward-facing semantic ceiling and recommendation

`RECOMMENDED_STEWARD_ACTION = ADMIT_NARROW_NATIVE_S3_N2_CONSEQUENCE_WITH_PRIOR_ART_ANNOTATIONS`

This is a **research recommendation only**, not a Foundation disposition.

If an explicitly active Foundation Steward accepts the packet, the maintained consequence should be no stronger than:

1. native sector count `s=3` is an upstream input;
2. the exact native N2 saturation characteristic set is `{5,7}`;
3. the project-specific translated-square breaker characteristic is `q_b=5`, with its core intersection identity annotated as classical Paley/difference-set mathematics;
4. the exact mod-5 capacity readout is `k_*=9`, as an application-local periodic congruence lemma;
5. the mixed-parity N2 grade-gap readout at `k=9` is `{5,7}`, with no physical rail interpretation;
6. `35`, `105`, and `53` are scalar consequences only after the preceding native N2 inputs are fixed.

Must remain excluded:

- P0/P1 primitive mutation;
- pointwise intrinsic allocation labels;
- N0 breaker primitives;
- named physical longitudinal/transverse rails;
- arbitrary odd-`s` comparator theorems;
- reverse derivation of native `s=3`;
- identification of breaker-coprime capacity `9` with the separate prime-incidence island-cap `9`;
- any claim that the four mathematical ingredients or their native composition are externally novel merely because targeted searches did not locate a duplicate.

## 10. Authority gate and next action

`PRIOR_ART_GATE = RESOLVED`.

`FOUNDATION_STEWARD_DISPOSITION = NOT_PERFORMED`.

Reason: current execution is a Researcher TASK_RESEARCH claim. The taskbook explicitly requires an active `FOUNDATION_STEWARD` role for maintained-surface admission/narrowing/rejection. Driver acceptance and this Researcher-ID do not grant that authority.

Next authorized action: an explicitly activated Foundation Steward consumes this packet together with `DR-9F0EF13296934CCAD8BD` and `RR-20AF98E870D82802D679`, then issues exactly one maintained-surface disposition among exact admission, narrower admission, or rejection, preserving the semantic ceiling above.

Current blocking authority condition: `FOUNDATION_STEWARD_AUTHORITY_NOT_ACTIVE_IN_CURRENT_CONVERSATION`.
