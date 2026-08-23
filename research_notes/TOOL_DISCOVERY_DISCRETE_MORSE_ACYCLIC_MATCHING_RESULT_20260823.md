# Tool Discovery Result — Discrete Morse / Acyclic Matching Collapse Calculus

Researcher-ID: `EM-TDDM-FF0986`

Task-ID: `RS-TD-DM-DISCRETE-MORSE-ACYCLIC-MATCHING-COLLAPSE-CALCULUS`

Hard target: `ENTERPRISE_DISCRETE_MORSE_COLLAPSE_TOOL_CLASSIFIED`

## 1. Frozen terminal classification

**Terminal verdict: `NEW_ENTERPRISE_TOOL_INTERFACE`.**

The retained capability is a reusable, exact, finite **algebraic Morse / acyclic-matching reduction interface** for explicitly graded free chain complexes over `Z` or `Q`.  The mathematics is classical: this report does **not** claim new Forman discrete Morse theory, a new algebraic cancellation theorem, or a new homology theorem.  The Enterprise-level novelty is the exact input contract, obstruction boundary, deterministic reduction/certificate interface, and demonstrated cross-family reuse.

The result is intentionally **not** called arbitrary graph simplification.  A graph appears only as a derived dependency structure after an explicit grading and boundary operator have already been supplied and verified.

No toolbox-registry registration or successor stage is opened here.  This taskbook authorizes classification and freeze; any later registration decision belongs to the Driver.

## 2. Exact source baseline and provenance

Taskbook source:

- `research_tasks/TOOL_DISCOVERY_DISCRETE_MORSE_ACYCLIC_MATCHING_COLLAPSE_CALCULUS_20260823.md@0eda7eb9c7a0bdca1edf5d62d487015df6d6bd00`
- source tree: `5118c605b4918853445bf53a81c9c9aaa58362aa`
- taskbook branch: `driver/tool-discovery-aplus-batch-20260823`
- owner branch: `research/tool-discrete-morse-acyclic-matching-collapse`

Frozen comparison inputs authorized by the taskbook:

- `enterprise_toolbox_registry.json@f83f349d1521185ac3e99db574959d0b797cacf2`
- `research_method_inventory.json@f83f349d1521185ac3e99db574959d0b797cacf2`
- `tool_invocation_policy.json@f83f349d1521185ac3e99db574959d0b797cacf2`
- `docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md@f83f349d1521185ac3e99db574959d0b797cacf2`
- `src/enterprise_math/alexander_descent.py@e48d51a062faa94dfdb6b9dce64ea7d76c7ea95e`

Bounded repository search for a current generic `chain complex / boundary / incidence / homology` helper produced no reusable generic Morse owner, so the implementation does not alias an undiscovered current helper.

## 3. Input semantic contract

Accepted object:

1. a **finite free graded chain complex** with a named basis in each integer degree;
2. an explicit boundary `d` lowering degree by exactly one;
3. exact coefficients in a declared ring, currently only `Z` or `Q`;
4. exact verification of `d^2 = 0` before matching or cancellation.

A supplied matching pair is `(a,b)` with `deg(b)=deg(a)+1` and nonzero incidence coefficient `u=[a]d(b)`.  Each generator may occur in at most one pair.

Coefficient law:

- over `Z`, cancellation is legal only for `u=+1` or `u=-1`;
- over `Q`, every nonzero `u` is invertible;
- a rational cancellation with pivot not equal to the integral units `±1` is explicitly marked `field_only=True`;
- no rational/field result is promoted to an integral result.

Rejected at the semantic boundary:

- arbitrary directed state graphs with no independently declared grading/incidence chain semantics;
- inferred “cells”, “faces”, topology, metric, manifold structure, or dimension from implementation geometry;
- non-free or unsupported coefficient modules without a separately implemented coefficient semantics.

## 4. Acyclic matching and obstruction law

For matched pairs `P_i=(a_i,b_i)`, form the exact dependency digraph on matched pairs:

`P_i -> P_j` iff `a_j != a_i` occurs with nonzero coefficient in `d(b_i)`.

Because every upward step is a matched adjacent-grade incidence and every downward step is an unmatched boundary incidence, a directed cycle in this dependency graph is exactly a closed algebraic `V`-path obstruction at the supported level.

The checker returns an explicit alternating witness, e.g.

`v1 -> e1 -> v2 -> e2 -> v1`.

Locally legal pairs are therefore not accepted merely because their pivots are units: the global cycle gate is mandatory.

## 5. Exact elementary cancellation and composition certificate

For a legal pair `(a,b)` with

`d(b) = u a + r`, `u` invertible in the declared coefficient domain,

the implementation uses the exact elementary contraction

- `h(a)=u^{-1}b`, `h(x)=0` otherwise;
- `p(a)=-u^{-1}r`, `p(b)=0`, and `p(x)=x` on surviving generators;
- `i(x)=x-u^{-1}[a]d(x)b` for surviving generators in `deg(b)`, and `i(x)=x` otherwise;
- reduced boundary `d' = p d i`.

For successive cancellations, with accumulated maps `(P,I,H)` and current elementary maps `(p,i,h)`, the exact composition is

- `P' = p P`;
- `I' = I i`;
- `H' = H + I h P`.

The frozen certificate verifier checks, with exact `Fraction`/integer arithmetic:

1. original and reduced `d^2=0`;
2. matching legality and global acyclicity;
3. the deterministic sink-order cancellation trace;
4. the critical basis and exact reduced/Morse boundary;
5. `P d_C = d_M P`;
6. `d_C I = I d_M`;
7. `P I = id_M`;
8. `I P + d_C H + H d_C = id_C`;
9. independent exact replay of every elementary cancellation, rejecting forged maps/boundaries/traces.

This is a strong deformation retract certificate at the supported coefficient layer, hence an exact chain-homotopy/homology-preservation witness.  No floating rank is involved.

## 6. Critical-generator interpretation

The unmatched basis elements are the critical generators of the supplied matching, and the reduced basis is exactly that critical set.

What is certified:

- exact generator compression for that supplied legal acyclic matching;
- an exact reduced differential on the critical generators;
- exact chain-homotopy equivalence at the declared coefficient layer.

What is **not** certified:

- minimum possible number of critical generators;
- optimality of the supplied matching;
- canonicality of a greedy matching;
- equality between critical counts and Betti numbers in general.

Over a field, ordinary Morse inequalities/lower bounds may be applied classically when their hypotheses are separately met; this implementation does not claim a new bound.

## 7. Tool coverage / dedup table

| Existing family/source | Existing role at frozen baseline | Exact overlap | Retained separation |
|---|---|---|---|
| T2 | bounded finite incompatibility/certificate machinery | finite exact certificates | T2 does not cancel adjacent graded generators or construct a Morse differential/SDR |
| T3 | typed/signed incidence cycle/cut/path-defect diagnostics | cycle detection can serve as an acyclicity subroutine | T3 does not perform unit-incidence chain cancellation or return critical complex plus `P/I/H` |
| T6 | operation/observation-safe quotient | both reduce a finite object | homology equivalence is not operation-safe quotient semantics; a Morse reduction may be invalid for a declared observer |
| T7 | finite symmetry/orbit reduction | can reduce matching search and analyze relabeling | does not perform chain cancellation; supplied-matching reduction is equivariant, greedy selection need not be canonical |
| T9 | gluing/holonomy obstruction | both may consume incidence-like data | holonomy/gluing obstruction is not chain-homotopy equivalence and is not replaced by homology |
| `alexander_descent.py` | specialized threshold/Alexander-duality machinery with exact combinatorics/operator witness | Application A can live on a threshold complex | it exposes no general acyclic matching + unit-cancellation + critical-boundary engine; the present tool compresses before/alongside such specialized calculations rather than reproducing the Alexander formula |

**Dedup conclusion:** the new capability is not “signed incidence skeleton plus node deletion”.  T3-like cycle checking is only an internal obstruction test.  The material new interface is exact algebraic cancellation plus the reduced chain complex and SDR certificate.

## 8. Application A — genuine threshold/support complex

Define weights

- `w(a)=w(b)=1`;
- `w(c)=w(d)=2`;
- threshold `T=3`;
- a nonempty support face is admitted iff its weight sum is `<=3`.

The resulting 1-dimensional threshold complex has:

- vertices `a,b,c,d`;
- edges `ab, ac, ad, bc, bd`;
- edge `cd` excluded;
- all triangles excluded.

Chain generators: `9` total (`4` in degree 0 and `5` in degree 1).

Legal supplied matching:

- `(vb,eab)`;
- `(vc,eac)`;
- `(vd,ead)`.

All three pivots are `+1`; the matching is acyclic.  Exact reduction leaves critical generators

- degree 0: `va`;
- degree 1: `ebc, ebd`;

with zero reduced boundary.

Statistics:

- raw generators: `9`;
- critical/reduced generators: `3`;
- removed generators: `6`;
- compression: `66.7%` by generator count.

Exact integer normal-form check:

- determinantal-divisor/Smith computation of the original incidence matrix gives one free `H0` generator and no `H0` torsion;
- exact kernel rank gives `H1 = Z^2`;
- the reduced complex has one degree-0 and two zero-boundary degree-1 generators, giving the same `H0=Z`, `H1=Z^2`;
- the SDR certificate independently proves the chain-homotopy equivalence.

Benefit: the exact invariant computation can be carried on `3` generators instead of `9`.  This does not reproduce or replace the specialized Alexander-descent formula.

## 9. Application B — relation/syzygy collapse complex

This second family is not a renamed threshold complex.  It is an exact graded relation/syzygy object:

- degree 0: `x,y`;
- degree 1: `r1,r2`;
- degree 2: `s`;
- `d(r1)=x`;
- `d(r2)=x`;
- `d(s)=r1-r2`.

Thus `d^2(s)=x-x=0` exactly.

Legal supplied matching:

- `(r1,s)`;
- `(x,r2)`.

Reduction statistics:

- raw generators: `5`;
- critical/reduced generators: `1` (`y`);
- removed generators: `4`;
- compression: `80%`.

Exact normal-form/presentation check:

- `d1=[1 1; 0 0]` has exact Smith rank `1`, no torsion in the cokernel, and `H0=Z`;
- `ker(d1)=Z(r1-r2)` and `d2(s)=r1-r2`; in the exact kernel basis the induced matrix is `[1]`, whose Smith form gives trivial `H1` and no torsion;
- `d2` is injective, so `H2=0`;
- the reduced complex is exactly `Z*y` in degree 0, agreeing with these groups;
- the exact SDR certificate again verifies the preservation independently.

This establishes reuse on two genuinely different Enterprise problem families: support/threshold topology and relation/syzygy collapse semantics.

## 10. Hard boundaries and counterexamples

### 10.1 Arbitrary state graph

Payload containing only `nodes/edges` is rejected.  The tool requires `ring`, `basis_by_degree`, and exact `boundary`, followed by `d^2=0` verification.  No state graph is silently promoted to a cell complex.

### 10.2 Closed gradient path / cyclic matching

For

- `d(e1)=v1+v2`;
- `d(e2)=v1+v2`;
- matching `(v1,e1),(v2,e2)`,

each pair is locally unit-cancellable but the combined matching has the exact cycle

`v1 -> e1 -> v2 -> e2 -> v1`.

The global matching is rejected.

### 10.3 Bad greedy local choices

The same example proves that “accept each locally legal pair greedily” is unsound: both singleton matchings pass, while their union fails the global acyclicity gate.

### 10.4 Nonunit incidence over `Z`

For `Z --2--> Z`, the incidence pivot is `2`, not a unit.  Integer cancellation is rejected.

The same explicit complex over `Q` is cancellable and reduces to zero, but its certificate is marked `field_only=True`.

### 10.5 Torsion / field-information loss

For `Z --2--> Z`, exact determinantal-divisor/Smith normal form gives

- `H0 = Z/2Z`;
- `H1 = 0`.

After tensoring with `Q`, multiplication by `2` is invertible and rational homology vanishes.  Therefore a field/rational rank check would erase the integral torsion and cannot certify the `Z` statement.

### 10.6 Homology preservation is not T6 operation safety

For an interval `e` with `d(e)=v1-v0`, matching `(v1,e)` reduces to the critical vertex `v0` and preserves homology exactly.  A separately declared operation `OBSERVE_V1`, however, cannot be recovered as the identity of the removed generator `v1` through the reduced basis.  Such a caller needs a T6-style operation-safe quotient condition in addition to, or instead of, Morse reduction.

### 10.7 Presentation-dependent greedy matching is not canonical

The interval permits legal cancellation against either endpoint.  Choosing `(v0,e)` leaves `v1`; choosing `(v1,e)` leaves `v0`.  Both reductions are exact SDRs.  A presentation/order-based greedy constructor is therefore not advertised as canonical.

By contrast, if a supplied matching and the entire complex are relabeled by an isomorphism, the theorem-level reduction/certificate relabels equivariantly; the checker verifies this.

### 10.8 Malformed certificate

Mutating a projection entry in a valid certificate causes verification failure through `PI=id`, chain-homotopy, or exact replay checks.  Certificates are not trusted merely because they deserialize.

### 10.9 Geometry is not native topology

The relation/syzygy example is accepted solely because grading and `d` are explicitly declared.  No geometric embedding, smooth Morse function, manifold structure, continuum topology, or native geometric dimension is inferred.

## 11. Theorem / status ledger

| Claim | Status | Exact evidence |
|---|---|---|
| finite chain input validated before reduction | PASS | adjacent-degree boundary and exact `d^2=0` checks |
| supplied local matching legality | PASS | nonzero incidence, adjacent grades, disjoint pairs |
| `Z` unit/nonunit distinction | PASS | `±1` only; pivot `2` rejection |
| closed gradient path obstruction | PASS | exact dependency-cycle witness |
| exact elementary cancellation | PASS | `d'=pdi` with exact coefficients |
| exact Morse/reduced boundary | PASS | reduced complex replay + `d^2=0` |
| project/lift certificate | PASS | chain-map identities + `PI=id` |
| accumulated chain homotopy | PASS | `IP+dH+Hd=id` after dependent multi-step cancellation |
| malformed certificate rejection | PASS | mutated certificate rejected |
| integral torsion guard | PASS | exact determinantal-divisor/Smith invariants for `[2]` |
| cross-family reuse | PASS | threshold/support `9->3`; relation/syzygy `5->1` |
| relabeling invariance of supplied-matching result | PASS | relabeled complex/matching certificate verified |
| greedy canonicality | REJECTED | two legal interval reductions leave different named critical vertices |
| arbitrary graph simplification | REJECTED | schema/semantic gate |
| operation-safe quotient equivalence | REJECTED | explicit observer counterexample |
| new mathematical theorem | NOT CLAIMED | classical Forman/algebraic Morse prior art acknowledged |

## 12. Deterministic checker

Required executable:

`scripts/tool_discovery_discrete_morse_acyclic_matching_check.py`

Primary replay:

```bash
python scripts/tool_discovery_discrete_morse_acyclic_matching_check.py --self-test
```

Frozen formal regression result:

- checks: `14`;
- mismatches: `0`;
- exact integer/rational arithmetic only;
- Smith invariant factors computed by exact determinantal divisors/minors in the bounded benchmark checker;
- unknown CLI arguments rejected by `argparse` with nonzero exit (`2`).

Additional deterministic demos:

```bash
python scripts/tool_discovery_discrete_morse_acyclic_matching_check.py --demo-unit
python scripts/tool_discovery_discrete_morse_acyclic_matching_check.py --demo-cyclic
python scripts/tool_discovery_discrete_morse_acyclic_matching_check.py --demo-nonunit
```

The no-argument invocation also runs the full regression.

Frozen implementation SHA256 values (local byte-for-byte artifacts used for the branch write):

- `src/enterprise_math/discrete_morse_collapse.py`: `a6b94ccd6c8b8e4ee91d1eaabb0097a7716a52323d2bd200159da76c5f49983b`;
- `scripts/tool_discovery_discrete_morse_acyclic_matching_check.py`: `b97c3133d79583cffb02a6f8a6200f5bac4038e55466678d5fafd49b10961ddd`.

Robustness addendum (not needed for the formal `14`-check gate):

- `280` seeded random acyclic integer unit-pivot cases verified with exact SDR replay;
- `100` seeded random rational nonzero-pivot cases verified;
- mismatches: `0`.

## 13. Reusable source module

Because the positive interface gate is met, the optional reusable implementation is frozen at

`src/enterprise_math/discrete_morse_collapse.py`.

Its public semantic surface consists of:

- `FiniteChainComplex`;
- `MatchingPair`;
- `validate_matching` / closed-gradient obstruction;
- deterministic acyclic cancellation order;
- `morse_reduce`;
- `MorseReductionCertificate`;
- `verify_certificate`;
- exact torsion guard for the rank-one nonunit counterexample;
- relabeling helpers.

The returned certificate contains the critical generators, exact reduced boundary, projection, lift, homotopy, cancellation trace, and field-only marker.

## 14. Residual limits / non-successor handoff

Bounded domain of this result:

- finite free chain complexes;
- exact `Z` and `Q` coefficients only;
- supplied matching correctness/certification, not optimal matching search;
- no automatic semantic quotient guarantee beyond the declared chain invariant;
- no claim about smooth/continuum Morse theory;
- no claim that critical counts are minimal;
- no general-purpose integral homology engine is introduced—the checker uses an exact bounded Smith/determinantal-divisor method for the claimed benchmark comparisons.

Potential future extensions (coefficient localization, PID modules, symmetry-aware matching search, T6 operation-safe composition, optimal matching search) are **not opened here**.

## 15. Final hard-target closure

`ENTERPRISE_DISCRETE_MORSE_COLLAPSE_TOOL_CLASSIFIED = PASS`

Strongest justified terminal classification:

`NEW_ENTERPRISE_TOOL_INTERFACE`

Reason: a generic, exact, cross-domain acyclic-matching/chain-cancellation interface with critical-generator reduction and replayable SDR certificate is absent from T2/T3/T6/T7/T9 and from the Alexander-descent specialization, while all underlying mathematical cancellation facts remain classical prior art.

Freeze complete. Stop after committing the required artifacts and this terminal result; do not open a successor.
