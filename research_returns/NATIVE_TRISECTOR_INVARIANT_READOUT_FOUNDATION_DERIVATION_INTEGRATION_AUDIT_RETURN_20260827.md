# Native Tri-sector Invariant-Readout Foundation Derivation Integration Audit — Research Return

Status: `FINAL_FROZEN / FOUNDATION_DERIVED_WITH_EXACT_SCOPE_NARROWING / FOUNDATION_UNCHANGED`
Date: `2026-08-27`
Researcher-ID: `EM-NTIRF-4E5B74`
Task: `RS-NATIVE-TRISECTOR-INVARIANT-READOUT-FOUNDATION-DERIVATION-INTEGRATION-AUDIT`
Publication: `TP2-40E602603558313A7D41`
Claim: `chatgpt-ntirf-20260827-1940`

## 1. Primary verdict

`PRIMARY_VERDICT = FOUNDATION_DERIVED_WITH_EXACT_SCOPE_NARROWING`.

The allocation-torsor result does more than remove a presentation nuisance. At the exact semantic strength allowed by the current native-admissibility rules, it permits a frame-free **scalar reconstruction** of the native central quadratic readout. From that reconstructed scalar law one can derive, without adding a breaker primitive or selecting a physical lane:

- the nonsingular odd breaker characteristic `q_b=5`;
- its exact breaker-coprime capacity `k_*=9`;
- the unordered native transverse saturation characteristic set `{5,7}`;
- the unordered longitudinal sharp boundary pair `{5,7}` at `k_*=9`;
- and hence the native scalar closure `3 -> (5,7) -> 9 -> 35 -> 105 -> 53`.

What does **not** become Foundation-generated is the full controlled arbitrary-odd-`s` comparator family, its uniqueness theorem over `s>=3`, or named physical longitudinal/transverse/rail ontology. Those remain research-layer semantics.

Accordingly:

- the whole admitted `NATIVE_TRISECTOR_COUPLED_CLOSURE_THEOREM` is **not** reclassified wholesale;
- its native `s=3` invariant-readout consequence is derivable at N2 scalar/set/relation strength;
- current P0/P1 primitives remain unchanged.

This is the exact scope narrowing required by NSA-13: quotient/scalar invariance is used only to derive quotient/scalar/set-valued consequences, never a distinguished physical representative.

## 2. New bridge: balanced-orbit barycenter readout

Let the accepted native shell be

`A_r={(a,b,c) in N_0^3 : min(a,b,c)=0, a+b+c=r}`

with `|A_r|=3r`, and let the accepted six-frame allocation torsor be `lambda_f` with shell start

`C_r=1+3r(r-1)/2`.

For every `r>=2`, define the intrinsic most-balanced shell orbit

`O_r = Sym_3 · (ceil(r/2), floor(r/2), 0)`,

where repeated permutations are removed, so `O_r` is a set of distinct native states.

`O_r` is `S_3`-invariant. Therefore the accepted orbit-readout descent theorem gives a frame-independent label multiset

`L_r = {lambda_f(x) : x in O_r}`.

No pointwise label is being promoted. We use only a symmetric scalar of the descended multiset:

`Z(r)=ceil(mean(L_r))`.

### Even shell

Put `r=2m`. In any one frame the three balanced states occur at positions

`m, 3m, 5m`.

Hence their mean position is

`3m=3r/2`.

Thus

`mean(L_r)=C_r+3r/2`

and, since the quantity is integral,

`Z(r)=C_r+3r/2=1+3r^2/2`.

### Odd shell

Put `r=2m+1>=3`. The six balanced states occur at positions

`m, m+1, 3m+1, 3m+2, 5m+2, 5m+3`.

Their mean is

`3m+3/2=3r/2`.

Therefore again

`mean(L_r)=C_r+3r/2`,

and now

`Z(r)=C_r+ceil(3r/2)=1+(3r^2+1)/2`.

Combining parities,

`Z(r)=1+(3r^2+epsilon(r))/2`,

where `epsilon(r)=r mod 2`, for every `r>=2`.

This is exactly the previously model-side `H=1` central quadratic filament formula, but now reconstructed as a symmetric scalar of a native `S_3` orbit rather than by choosing a sector, start ray, orientation, or center lane.

### Boundary guard

At `r=1` the balanced orbit degenerates to the three axis states and this particular barycenter-ceiling construction does not reproduce the same formula. The derivation is therefore stated exactly for `r>=2`.

This causes no breaker/capacity loss: every parity/residue class used in the periodic argument has representatives at arbitrarily large `r`, so deleting finitely many initial shell indices does not alter the finite-field covering predicates or sharp periodic run calculation.

Freeze:

`BALANCED_ORBIT_LABEL_MULTISET -> SYMMETRIC_BARYCENTER_READOUT -> NATIVE_QUADRATIC_SCALAR_LAW`.

No distinguished pointwise lane is used.

## 3. Universal breaker reconstructed as a scalar readout predicate

The parity branches of the reconstructed native scalar law have quadratic value sets. For an odd prime `q` with `q∤6`, normalize the two translated branch images as

`I_0(q)={-3x^2/2 : x in F_q}`,

`I_1(q)={-3x^2/2-1/2 : x in F_q}`.

Define the **readout breaker predicate**

`Break(q) iff I_0(q) union I_1(q)=F_q`.

This definition uses only the reconstructed scalar law and finite-field reduction. It does not add `breaker` as an N0 primitive.

The already audited split-hyperbola/Klein-four support theorem proves that, for the nonsingular odd carrier, a universal cover has one quotient class and hence

`q-1<=4`,

so

`q<=5`.

Under `q` odd and `q∤6`, the only possibility is `q=5`.

Directly modulo 5,

`I_0(5)={0,1,4}`,

`I_1(5)={1,2,3}`,

so their union is all of `F_5`.

Therefore

`q_b=5`

is derived as the unique nonsingular odd breaker characteristic of the native reconstructed scalar readout.

Semantic status:

`q_b=5 = DERIVED_NATIVE_INVARIANT at N2 scalar/readout strength`.

It is not a newly declared Foundation breaker object.

## 4. Breaker-coprime capacity reconstructed

For the translated scalar family

`Z_H(r)=H+(3r^2+epsilon(r))/2`,

the already audited quadratic-ramification theorem gives the exact sharp breaker-coprime capacity

`k_*(q)=2q-1`

in a breaker phase: each full `2q` period contains a zero, while a branch critical class outside the overlap gives a period with exactly one zero.

Substituting the derived native breaker `q_b=5` gives

`k_*=2*5-1=9`.

Hence the capacity no longer needs to be supplied as an independent semantic premise at scalar-readout strength.

Guard:

`k_*=9` here is the exact breaker-coprime/divisibility capacity. It remains logically distinct from the separate native typed-Cell theorem asserting an actual prime-incidence island cap of `9`.

## 5. Transverse `5/7` without lane names

For even shell `r=2m`, the accepted allocation-torsor audit already gives the frame-independent unordered balance packet

`P_m={6m^2-2m+1, 6m^2+1, 6m^2+2m+1}`.

Define, for odd nonsingular prime `q` with `q∤6`,

`Sat(q)` iff the union of the root sets modulo `q` of the three members of the **unordered** packet is exactly `F_q^*`.

This is invariant under all permutations of the packet; no lower/middle/upper physical lane is required.

Each packet member is a quadratic polynomial in `m`, so the union has at most six roots. Complete nonzero saturation therefore implies

`q-1<=6`, hence `q<=7`.

The nonsingular odd candidates are `5` and `7`, and direct exact root partitions are:

- modulo 5: `{1} | {2,3} | {4}`;
- modulo 7: `{2,3} | {1,6} | {4,5}`.

In both cases the union is all nonzero residues.

Therefore

`{q : Sat(q)}={5,7}`

among nonsingular odd characteristics.

This is the native invariant-readout content behind T-A's two extremal characteristics. The further statement that **among every controlled odd comparator parameter `s>=3` only `s=3` has both extremal saturations** remains research-layer, because the arbitrary-odd-`s` comparator family is not generated by current P0/P1.

## 6. Longitudinal boundary without physical rail ontology

The T-B equations use the pair `k_*-4, k_*-2`. Their invariant content can be reconstructed from native grade/parity alone.

For odd `k>=5`, consider the grade window

`W_k={0,1,...,k-1}`.

Choose distinct `u,v,w` with `u≡v (mod 2)` and `w` of the opposite parity. The mixed-parity tangent obstruction uses the distance product

`D=|w-u| |w-v|`.

### Extremal lemma

The exact maximum is

`max D=(k-2)(k-4)`,

and at every maximum the **unordered** distance pair is

`{k-4,k-2}`.

Proof: in a maximizing configuration `w` may be taken outside the interval spanned by the same-parity pair; otherwise moving the opposite-parity point toward the farther boundary increases both available distances until an exterior configuration is reached. Once `w` is on one side, the same-parity pair maximizing the product is the two nearest admissible indices at the opposite boundary, separated by two because of parity. With `k` odd, the furthest admissible opposite-parity endpoint then gives distances `k-2` and `k-4`. Any inward move of the outer point or either same-parity endpoint strictly decreases at least one factor while not increasing the other enough to exceed the boundary product. Reflection gives the only symmetric alternatives. Thus the maximizing distance **multiset** is canonical even though no oriented rail is selected.

At the derived capacity `k_*=9`, the longitudinal boundary readout is therefore

`{k_*-4,k_*-2}={5,7}`.

Comparing with Section 5 gives the invariant equality

`LONGITUDINAL_BOUNDARY_SET = TRANSVERSE_SATURATION_SET = {5,7}`.

At native `s=3`, this is exactly the scalar content of

`k_*-4=2s-1=5`,

`k_*-2=2s+1=7`,

without claiming that named longitudinal/transverse physical rails are N0 primitives.

## 7. T-A / T-B / T-C classification

### T-A — exact scope narrowing

Classification:

`FOUNDATION_DERIVED_WITH_EXACT_SCOPE_NARROWING`.

Foundation-derived native part:

> For the current native `s=3` shell, the frame-independent unordered balance packet has exactly the two nonsingular complete-saturation characteristics `{5,7}`.

Research-only residue:

> Uniqueness of `s=3` among the full arbitrary odd comparator family `s>=3` remains a controlled research-model theorem. Current P0/P1 does not generate the `s!=3` comparator geometries.

### T-B — exact scope narrowing

Classification:

`FOUNDATION_DERIVED_WITH_EXACT_SCOPE_NARROWING`.

Foundation-derived native part:

- scalar breaker characteristic `q_b=5`;
- exact breaker-coprime capacity `k_*=9`;
- invariant longitudinal boundary pair `{5,7}`;
- equality with the native transverse saturation set `{5,7}`.

Research-only residue:

- the general uniqueness theorem over arbitrary odd `s`;
- named physical longitudinal/transverse/rail ontology as intrinsic Foundation objects.

### T-C — native invariant-readout consequence

Classification:

`FOUNDATION_DERIVED_AT_INVARIANT_READOUT_STRENGTH`.

Here `s=3` is consumed from current Foundation; it is **not** derived by the closure theorem.

With the derived `k_*=9`, the exact scalar consequences are

`M_9=(9-4)(9-2)=35`,

`3M_9=105`,

`3M_9+1=106=2*53`.

Thus the native scalar chain

`3 -> (5,7) -> 9 -> 35 -> 105 -> 53`

is now reconstructible from current P0/P1 through invariant N2 readouts and exact arithmetic, without a preferred frame or breaker primitive.

This does not reverse the dependency to prove Foundation three-ness.

## 8. Semantic-strength dependency ledger

The machine-readable ledger is frozen at

`research_artifacts/NATIVE_TRISECTOR_INVARIANT_READOUT_FOUNDATION_DERIVATION_INTEGRATION_AUDIT/dependency_ledger_20260827.json`.

Its decisive classifications are:

1. current P0/P1 shell/address + native sector count -> shell and `S_3` action: `DERIVED_NATIVE_INVARIANT`;
2. shell -> accepted allocation torsor: `DERIVED_NATIVE_INVARIANT`;
3. torsor + invariant balanced orbit -> label multiset: `PRESENTATION_ONLY_BUT_DESCENDS`;
4. label multiset -> barycenter-ceiling scalar `Z(r)`: `DERIVED_NATIVE_INVARIANT` at N2 scalar strength;
5. scalar parity law -> breaker covering predicate -> `q_b=5`: `DERIVED_NATIVE_INVARIANT` at N2 predicate/scalar strength;
6. breaker scalar -> `k_*=9`: `DERIVED_NATIVE_INVARIANT` at N2 scalar strength;
7. even balance packet -> saturation set `{5,7}`: `DERIVED_NATIVE_INVARIANT` at N2 set strength;
8. grade/parity window -> sharp distance pair `{5,7}`: `DERIVED_NATIVE_INVARIANT` at N2 set strength;
9. equality of the two `{5,7}` readouts -> native T-B instance: `DERIVED_NATIVE_INVARIANT` at N2 relation strength;
10. native closure -> `35,105,53`: `DERIVED_NATIVE_INVARIANT` scalar consequences;
11. current P0/P1 -> arbitrary odd-`s` comparator family: `EXTRA_SEMANTIC_PREMISE`;
12. current P0/P1 -> named physical rail ontology: `EXTRA_SEMANTIC_PREMISE`, not needed by the narrowed theorem;
13. using desired `3/5/7/9` output to justify native `3` or any upstream predicate: `CIRCULAR_OR_TARGET_LEAK`, rejected.

No edge relies on a preferred physical axis, frame point, target-selected capacity law, or reverse use of the desired closure.

## 9. Regression certificate

Finite checks were used only as regression, not as the general proof.

Exact regression performed:

- shells `r=2..128`;
- all six frames per shell;
- `762` frame/multiset invariance checks;
- `3420` balanced-orbit label evaluations;
- every shell matched `Z(r)=1+(3r^2+epsilon(r))/2`;
- all odd primes `q<=199`, `q∤6`: transverse complete-saturation set exactly `[5,7]`;
- all odd primes `q<=199`, `q∤6`: breaker set exactly `[5]`;
- every odd `k=5..101`: `49` window checks, all with maximum `(k-2)(k-4)` and maximizing unordered pair `{k-4,k-2}`.

The universal statements are proved by the exact orbit-position formulas, root-count bound, existing one-orbit breaker theorem, existing ramification theorem, and parity extremal argument above.

## 10. Method harvest

`METHOD_HARVEST = COMPOSE_EXISTING_TOOLS / NO_NEW_GENERAL_PURPOSE_TOOL`.

The work composes:

- accepted allocation-torsor orbit descent;
- native semantics strength typing;
- existing split-hyperbola/Klein-four breaker support;
- existing quadratic-ramification capacity theorem;
- elementary finite-field root counting;
- elementary grade/parity extremal analysis.

No new global tool family is justified.

## 11. Final freeze

`PRIMARY_VERDICT = FOUNDATION_DERIVED_WITH_EXACT_SCOPE_NARROWING`.

`NATIVE_T_C_SCALAR_CHAIN = FOUNDATION_DERIVED_AT_INVARIANT_READOUT_STRENGTH`.

`T_A_GENERAL_ODD_S_UNIQUENESS = RESEARCH_LAYER`.

`T_B_GENERAL_ODD_S_UNIQUENESS = RESEARCH_LAYER`.

`NAMED_PHYSICAL_RAIL_ONTOLOGY = NOT_PROMOTED`.

`BREAKER_PRIMITIVE = NOT_ADDED`.

`FOUNDATION_MUTATION = NONE`.

`HARD_TARGET = ACHIEVED_WITH_EXACT_SCOPE_NARROWING`.

`UNRESOLVED_RESIDUE = GENERAL_ODD_S_COMPARATOR_UNIQUENESS_AND_NAMED_PHYSICAL_RAIL_ONTOLOGY_REMAIN_RESEARCH_LAYER; NONE_FOR_NATIVE_N2_SCALAR_CLOSURE_CHAIN`.

Recommended Driver action: admit the narrowed native invariant-readout consequence if Foundation policy permits, keep the existing full comparator theorem node at `AUDITED_RESEARCH_THEOREM`, and leave current Foundation primitives unchanged.