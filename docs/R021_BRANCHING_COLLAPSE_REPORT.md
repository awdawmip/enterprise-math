# R021 Branching-Collapse Tool Calculus — Research Report

- **Task:** `RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS`
- **Researcher-ID:** `EM-R021-9832F2`
- **Taskbook base:** `15e9dcb67ce1f78b320099f2078c733bcba39ebb`
- **Priority:** `P0 / FOUNDATIONAL_CRITICAL`
- **Research mode:** discovery / adversarial kill-test / not canonical
- **CI:** `CI_NOT_REQUIRED_FOR_RESEARCH`
- **Final return class:** `BRANCHING_COLLAPSE_TOOL_CORE_FOUND / EXACT_REGIME_CLASSIFIED / ON_DEMAND_COMPILER_CHECKED / PARETO_ADVANTAGE_DEMONSTRATED / ROOTING_SUCCESS / ENTERPRISE_SPECIALIZATION_SURVIVES / NOT_CANONICAL`

## 0. Executive verdict

The branching-collapse hypothesis **survives**, but only after a major narrowing.

Runtime branching is **not** a universally stronger semantic collapse than deterministic refinement. In the declared Boolean **final result-support** regime, it is best understood as a second implementation family for the same exact future semantics:

1. deterministic refinement stores one residual/future-signature state;
2. branching stores a Boolean set of branch atoms whose union realizes the same residual behavior;
3. on-demand splitting materializes only distinctions demanded by the remaining future language;
4. recoalescence is safe only when the replacement retains the same remaining result-support signature, unless the literal union denotation itself is retained exactly.

A genuine Pareto advantage exists. The executable finite witness in this report has four pairwise future-distinct deterministic residual states but an exact two-atom Boolean branching presentation. After charging **all** atom labels, transition incidences, output incidences, and fine-to-branch encoder incidences, the explicit-table storage score is `10` versus `18`. The price is maximum live branch width `2` rather than deterministic width `1`; word depth is unchanged. This is therefore a real storage/work Pareto point, not hidden-state cheating.

The positive result is sharply scoped. It requires a future semantics whose transformers are join/union preserving (relational direct image / Boolean reachability), and a residual behavior that admits a sparse Boolean/NFA-like factorization or a query-local reachable fragment substantially smaller than the global residual quotient. The advantage can disappear completely when:

- multiplicity, provenance, weights, probability, cancellation, or branch identity are observed;
- the future language is rich enough to reconstruct the fine phase/state;
- exact branch denotations are stored as full fine-state bitsets;
- a symbolic deterministic representation factors the same structure just as cheaply;
- many repeated queries amortize deterministic global precomputation;
- minimum branching synthesis itself is too expensive to justify.

The strongest project-side conclusion is therefore:

> **Branching-collapse is a reusable exact compiler pattern for support-valued future languages, not a new universal precision order.**

The tool should be routed after semantic precision has been fixed, inside the R014 representation-resource layer.

---

## 1. T01 — strict carrier type system and exactness hierarchy

### 1.1 Fine system

Let

\[
\mathcal F=(X,A,\{R_a\}_{a\in A},q,O)
\]

where `X` is the fine state set, `A` the generator alphabet, `R_a subset X x X` a fine relation, `q:X->Q` the declared coarse collapse, and `O:X->Y` the final observable.

For a fine support `S subset X`, define relational direct image `Phi_a(S)=R_a[S]`; for a word `w=a_1...a_h`, `Phi_w=Phi_{a_h} o ... o Phi_{a_1}`. The exact declared result support is

\[
E_w(S)=O[\Phi_w(S)]\subseteq Y.
\]

This is the R015 Boolean/result-support semantic fibre. It intentionally discards path count, path identity, weights, probabilities, and provenance.

### 1.2 Objects that must remain type-distinct

| Object | Type | Meaning | Silent identification allowed? |
|---|---|---|---|
| coarse label | `q(x) in Q` | one quotient label | no |
| coarse fibre | `q^{-1}(c) subset X` | all fine states compatible with a label | no |
| fine support | `S subset X` | actual set-valued fine state | no |
| coarse-support alternatives | `C subset Q` | possible quotient labels | no |
| denotational branch | `b`, with `gamma(b) subset X` | one named fine subset/cell | no |
| live branch set | `Z subset B` | Boolean set of branch atoms | no |
| branch token | identifier in `B` | runtime correlation/residual atom | no; token identity is storage |
| result support | subset of `Y` | declared final observable | no |
| multiplicity carrier | multiset / `N`-semimodule | path counts | no |
| provenance carrier | set/multiset of histories | path identity | no |

A branch token is not free syntax. Its identifier, transition table, output row, encoder incidence, and any correlation payload are all representation cost.

### 1.3 Branching carrier

Use a Boolean branching presentation

\[
\mathcal B=(B,\eta,\{\Delta_a\}_{a\in A},\lambda),
\]

with `eta:X->P(B)`, `Delta_a:B->P(B)`, `lambda:B->P(Y)`, extended by union to subsets of `B`. The presentation is exact for a declared language `U` iff

\[
\lambda^\cup(\Delta_w^\cup(\eta(x)))=E_w(\{x\})
\]

for every `x` and `w in U`.

A denotational branch carrier `gamma:B->P(X)` is a useful special case, but an NFA-like behavioral atom may instead be a residual behavioral component.

### 1.4 Branching taxonomy

1. **Literal alternative branching** — final alternatives only; generally not compositional.
2. **Cell/fibre branching** — branch atoms denote explicit subsets of a coarse fibre.
3. **Fine-support branching** — retain an exact `S subseteq X`; exact but potentially full fine-state cost.
4. **Branch-token refinement** — reusable Boolean atoms retain correlation/residual behavior.
5. **Branch-on-demand refinement** — instantiate distinctions only when the next demanded generator/suffix needs them.
6. **Coalesced branching** — merge duplicate/behaviorally equivalent live branches under the declared suffix language.

### 1.5 Exactness levels and implications

```text
provenance exact
      |
      v
multiplicity / path-count exact
      |
      v
finite-word Boolean result-support exact
      |
      v
one-step Boolean result-support exact
```

A second compositional axis is:

```text
strong generatorwise saturation completeness
      |
      v
repeated collapse/re-expansion support exactness
      |
      v
one-step existential quotient support exactness
```

The lower implication does not reverse. R018 proves one-step existential quotient lifting from a saturated fibre, while R021 finds a two-state repeated-saturation failure.

Separations: support exact does not imply multiplicity exact; multiplicity exact does not imply provenance exact; one-step existential quotient exact does not imply composition exact; current coarse-output equality does not imply safe recoalescence.

---

## 2. T02 — repairing unsafe deterministic collapse

### 2.1 Unique coarsest one-step deterministic repair

Fix one generator `R` and quotient `q`. Define

\[
\sigma_R(x)=q[R(\{x\})]\subseteq Q.
\]

Then `rho_R(x)=(q(x),sigma_R(x))` induces the **unique coarsest refinement of `q`** on which coarse successor support is constant inside every refined fibre. Any exact refinement must split every pair with different successor-support signatures; this kernel does exactly that and nothing more.

The oracle exhaustively enumerates all `q`-refining set partitions of a four-state sample and confirms the coarsest property.

### 2.2 Unique coarsest finite-language deterministic repair

For finite `U`, define

\[
\Sigma_U(x)=\big(E_w(\{x\})\big)_{w\in U}.
\]

Then `rho_U(x)=(q(x),Sigma_U(x))` is the **unique coarsest deterministic `q`-refinement exact for all point-state final supports in `U`**.

### 2.3 What branching changes

Branching does not change `Sigma_U`; it changes how the family of signatures is represented:

\[
X \xrightarrow{\eta} \mathcal P(B)
\xrightarrow{\Delta_w}\mathcal P(B)
\xrightarrow{\lambda}\mathcal P(Y).
\]

Distinct deterministic residual signatures can be unions of a smaller collection of atom behaviors. This is the exact source of possible state/table compression.

### 2.4 Lower bound and no-free-metadata rule

A `k`-atom Boolean branch carrier with no hidden state has at most `2^k` live subsets. Hence `m` pairwise future-distinct deterministic residual states require

\[
|B|\ge \lceil\log_2 m\rceil.
\]

Transition closure may require more. Any extra discriminator that increases the number of representable live configurations is charged as representation state. One apparent token plus an uncharged exact-state ID is the fine state in disguise and is rejected.

---

## 3. T03 — branch width and resource invariants

For a fixed presentation record at least:

- `N_B=|B|`: branch atom labels;
- `E_B=sum_{b,a}|Delta_a(b)|`: transition incidences;
- `E_O=sum_b|lambda(b)|`: output incidences;
- `E_eta=sum_x|eta(x)|`: explicit encoder incidences;
- `W_max=max_{x,w}|Delta_w(eta(x))|`: maximum live branch width;
- cumulative branch creations;
- refinement depth;
- maximum compatible fine fibre per branch;
- coalescence ratio;
- all exact denotation/correlation metadata bits/incidences.

The comparison vector is

\[
\mathsf{Res}=(\text{labels},\text{bits/incidences},\text{precompute work},\text{runtime work},W_{max},\text{word depth},\text{materialization},\text{amortization}).
\]

### 3.1 Minimal branch width is not a standalone objective

If the representation family is unconstrained, deterministic future-signature refinement is itself a branching presentation with singleton live sets, so unconstrained minimum width is trivially `1`. A meaningful width optimization must fix a carrier/refinement family or budget, for example

\[
W^*(K)=\min_{P:C(P)\le K,\ P\ exact}\max_{x,w}|\Delta_w(\eta(x))|.
\]

This is why storage/work/depth must be treated as a Pareto vector.

---

## 4. T04 — branch-on-demand split / execute / coalesce calculus

### 4.1 Exact denotational invariant

Let live denotational branches after prefix `w_{<=i}` be `C_{i,1},...,C_{i,k}` and maintain

\[
\boxed{\bigcup_j C_{i,j}=\Phi_{w_{\le i}}(S_0).}
\]

Split preserves union; execute maps each branch by relational direct image; literal-set-union coalescence preserves union. Since relational direct image preserves arbitrary unions, the invariant is inductive and final result support remains exact.

### 4.2 Metadata catch

This exact-set implementation is safe even under aggressive merge **only because the exact union denotation remains stored**. An exact subset of an `n`-state universe costs up to `n` bits as a bitset. The oracle reports exact-denotation metadata cost explicitly; it is never treated as free compression.

### 4.3 Safe reusable-token recoalescence

If live branches are replaced by a reusable token/subset `Z'`, forgetting the exact union, define for remaining suffix language `V`

\[
\operatorname{Sig}_V(Z)=\big(\lambda^\cup(\Delta_v^\cup(Z))\big)_{v\in V}.
\]

The replacement is exact for the declared result-support semantics iff

\[
\boxed{\operatorname{Sig}_V(Z')=\operatorname{Sig}_V(\bigcup_i Z_i).}
\]

Hence same current coarse label or same current output is insufficient. Histories become consumable exactly when no declared remaining future distinguishes them.

### 4.4 Local split rule

For the next demanded generator `a`, the minimal deterministic local split of a coarse fibre is by `x -> q[R_a({x})]`. This is one-step sufficient. Repeating local splits is exact only if the carrier preserves later correlation; re-expanding each local label to its entire fibre is unsound.

---

## 5. T05 — deterministic refinement versus branching: real Pareto

### 5.1 Strategy comparison

| Strategy | Exact regime | Storage | Runtime state | Main price/failure |
|---|---|---:|---:|---|
| A naive deterministic coarse | generally inexact | low | 1 | spurious futures |
| B global deterministic future-complete | exact for `U` | residual labels + table | 1 | global precompute |
| C full compatible fine fibre | exact fibre-support | full support/bitset | large | may be fine state itself |
| D naive existential coarse branching | one-step fibre image exact | low | coarse alternatives | composition may invent paths |
| E exact branch-token | exact if verified | atoms + encoder + transitions + outputs | width `W` | work/minimization |
| F branch-on-demand + recoalescence | exact under invariant | reachable/local | dynamic | gains may be only laziness |
| G exact fine state/support | exact | full | point/support | no compression |
| H lazy deterministic control | exact | reached residuals only | deterministic residual(s) | control for laziness confound |

Strategy H is required for fairness: if F beats B only by avoiding unreachable global residuals and H gets the same gain, that is an on-demand benefit, not a branching-specific one.

### 5.2 Strict branching-specific storage witness

The oracle exhaustively searches all two-atom NFAs over a two-symbol alphabet: `4^4=256` transition choices times `3` nonempty accepting sets = `768` presentations. Maximum minimized reachable subset-DFA size is `4`, attained by `70` presentations.

One low-edge witness:

```text
atoms: b0,b1
alphabet: 0,1
accepting: b0

b0 --0--> empty
b0 --1--> {b1}
b1 --0--> empty
b1 --1--> {b0,b1}
```

Four deterministic residual states encode as `{b0}`, `empty`, `{b1}`, `{b0,b1}`. All four have different future signatures. For every fine state and every word of length `0..6`, `508` state-word cases match exactly.

Charged explicit-table cost:

| coordinate | deterministic | branching |
|---|---:|---:|
| labels | 4 | 2 |
| transition incidences | 8 | 3 |
| output incidences | 2 | 1 |
| encoder incidences | 4 | 4 |
| **total** | **18** | **10** |
| max live width | 1 | 2 |
| logical depth | `h` | `h` |

One atom is impossible without extra metadata because only two Boolean subsets are available for four pairwise future-distinct residual signatures. At the two-atom minimum, width `2` is unavoidable. Thus branching strictly improves explicit storage while deterministic execution has lower live width/work: a genuine nondominated Pareto pair.

### 5.3 No universal compression conclusion

A deterministic residual system may itself have a compact symbolic/circuit representation, so exponential explicit state counts are not automatically exponential bit costs. Minimum NFA/branching synthesis is also computationally hard. R021 therefore compares complete compiler packages, not raw state counts.

---

## 6. T06 — executable oracle, exhaustive search, mutations

Artifacts:

- `experiments/r021_branching_collapse_oracle.py`
- `experiments/r021_enumeration_summary.json`
- `experiments/r021_theorem_counterexample_matrix.json`
- `tests/test_r021_branching_collapse_oracle.py`

Focused local tests: **11 passed, 0 failed**.

### 6.1 Coarsest checks

For a four-state sample all `4` partitions refining `q` were checked. The future-signature partition is the unique coarsest finite-language exact refinement; the one-step coarse-successor partition is the unique coarsest one-step refinement.

### 6.2 Minimal repeated-saturation counterexample

The search exhausts `n=1` before entering `n=2` and finds the first failure after 25 enumerated systems. A two-state witness is minimal:

```text
X={0,1}
q(0)=q(1)=Q
R: 0 -> 0
S: 1 -> 0
start support = {0,1}
```

Fine execution: `{0,1} --R--> {0} --S--> empty`.
Naive quotient: `Q --R_bar--> Q --S_bar--> Q`.
The separately existing coarse edges have incompatible middle incidence, so composition fabricates a path.

### 6.3 Mutation suite

The oracle catches: re-expansion to a full coarse fibre; merge by current coarse label alone; and removal of needed branch distinctions.

### 6.4 Arithmetic audit

No floating-point constants and no true-division AST nodes are present. Arithmetic benchmark logic is integer-only.

---

## 7. T07 — arithmetic and structural pressure tests

### 7-A. Floor quotient plus translation

Let `q_r(n)=floor(n/r)`, `n=kr+s`, `0<=s<r`, and translate by `c=ar+d`, `0<=d<r`, with `g=gcd(r,c)=gcd(r,d)`. After `j` translations,

\[
q_r(n+jc)=k+ja+\left\lfloor\frac{s+jd}{r}\right\rfloor.
\]

Writing `jd=ell_j r+t_j`, the state-dependent part is only the threshold bit `1_{s>=r-t_j}` when `t_j!=0`. Nonzero residues `jd mod r` are distinct until period `r/g`. Therefore for translation prefixes `1..h`, one `q_r` fibre has exactly

\[
\boxed{K_h=1\text{ if }r|c;\qquad K_h=\min(h+1,r/g)\text{ otherwise}.}
\]

At full horizon this stabilizes at `r/g` phase classes, contiguous blocks of `g` residues. If `g=1`, sufficiently long future language reconstructs every residue.

Executable rows:

| `r` | `c` | gcd | full classes | early class counts | verdict |
|---:|---:|---:|---:|---|---|
| 8 | 1 | 1 | 8 | 2,3,4,5,6,7,8,8 | all residues reconstructed |
| 12 | 8 | 4 | 3 | 2,3,3,3,... | 3 phase blocks |
| 12 | 6 | 6 | 2 | 2,2,2,... | binary phase split |
| 10 | 20 | 10 | 1 | 1,1,1,1 | deterministic descent safe |

**Kill result:** branching cannot delete information the future distinguishes. In the coprime long-horizon case it must encode all `r` phases somewhere. Benefit is deferral/factorization, not information erasure.

### 7-B. `p`-th-power bracket

R018's nonexact `powerBracket` fibre at root `k` is exactly the integer open gap `(k^p,(k+1)^p)`. Deferred lower/upper endpoint selection followed by result-only relational futures is safe from the joint endpoint observation; arbitrary fine-state translation before bracket observation is not.

For square bracket `(4,9)` with fibre `{5,6,7,8}` under `+1`, future-signature class counts are `2,3,4,4` for horizons `1..4`. Thus the translation language reconstructs the full four-point fibre by horizon 3. Branching is useful only as temporary/on-demand refinement here, not as a permanent coarse carrier for arbitrary translations.

### 7-C. Witness/factor cutoff

Minimal witness:

```text
fine states: 6,10
cutoff 2: both -> {2}
cutoff 5: 6 -> {2,3}; 10 -> {2,5}
```

The low-cutoff witness set cannot determine the later higher-cutoff answer. Deterministic repair has two classes; literal branching also needs two distinguishable tokens/configurations. No storage advantage exists in this minimal instance.

Larger independent witness families may admit a witness-atom bitset representation with fewer explicit table states, but the live subset still carries the information bits and is charged. Nonlinear conjunction, multiplicity, or provenance leaves the Boolean-support contract.

### 7-D. Middle-incidence relation composition

The two-state composition witness is also the minimal middle-incidence example. After `R`, exact middle support is `{0}`. Re-expansion to coarse fibre `{0,1}` creates state `1`, which alone enables `S`. A branch token retaining `{0}` repairs exactness, but here the token is literally the fine identity: necessity of correlation is shown, not compression.

---

## 8. T08 — language-relative theorem package

### R021-T08.1 — deterministic future kernel

For finite `U`, equality of `(q(x),Sigma_U(x))` is the unique coarsest deterministic `q`-refinement exact for all declared point-state result supports.

### R021-T08.2 — Boolean branching exactness

A Boolean presentation is exact for `U` iff `lambda^cup Delta_w^cup eta(x)=E_w({x})` for all `x,w`. Union preservation extends singleton exactness to arbitrary input supports.

### R021-T08.3 — split/execute/coalesce invariant

For denotational branches whose exact union is retained, arbitrary splitting and literal-union coalescence commute with relational future steps and preserve final result support.

### R021-T08.4 — safe token recoalescence

Replacing a live branch union by another reusable representation is exact for remaining language `V` iff the two residual result-support signatures on `V` are equal.

### R021-T08.5 — no canonical minimum branching carrier in general

The deterministic quotient is canonical up to isomorphism because it is a kernel quotient. Branching factorizations are not: incomparable atom/transition graphs can realize the same behavior, and minimum NFA-like synthesis is hard. R021 therefore does not define “the” canonical minimum branching collapse without a fixed representation class and cost/order.

### R021-T08.6 — exact regime for strict branch advantage

A strict branching representation advantage is possible when the deterministic residual behavior admits a smaller union-generating transition-stable factorization whose fully charged package is nondominated. The two-atom/four-residual witness proves existence.

---

## 9. T09 — prior-art/rooting audit

The generic mathematical core is prior art; no novelty claim is made for nondeterminism, determinization, future equivalence, partition refinement, abstract interpretation, or CEGAR.

| Ingredient | Prior-art root / neighbor | Routing |
|---|---|---|
| nondeterministic automata / determinization | M. Rabin & D. Scott, *Finite Automata and Their Decision Problems*, IBM J. R&D 3(2), 1959, DOI `10.1147/rd.32.0114` | `ROOTING_SUCCESS / PRIOR_ART` |
| deterministic residual/future equivalence | A. Nerode, *Linear Automaton Transformations*, Proc. AMS 9(4), 1958, DOI `10.1090/S0002-9939-1958-0135681-9` | `ROOTING_SUCCESS / PRIOR_ART` |
| coarsest partition/refinement | R. Paige & R. Tarjan, *Three Partition Refinement Algorithms*, SIAM J. Comput. 16(6), 1987, DOI `10.1137/0216062` | `ROOTING_SUCCESS / PRIOR_ART` |
| behavioral equivalence/bisimulation | P. Kanellakis & S. Smolka, *CCS Expressions, Finite State Processes, and Three Problems of Equivalence*, Inf. Comput. 86(1), 1990, DOI `10.1016/0890-5401(90)90025-D` | `ROOTING_SUCCESS / PRIOR_ART` |
| abstract execution | P. Cousot & R. Cousot, *Abstract Interpretation: a Unified Lattice Model...*, POPL 1977, DOI `10.1145/512950.512973` | `ROOTING_SUCCESS / PRIOR_ART` |
| on-demand refinement / CEGAR | E. Clarke et al., *Counterexample-Guided Abstraction Refinement*, CAV 2000, DOI `10.1007/10722167_15` | `ROOTING_SUCCESS / PRIOR_ART` |
| symbolic state sets | J. Burch et al., *Symbolic Model Checking: 10^20 States and Beyond*, Inf. Comput. 98(2), 1992, DOI `10.1016/0890-5401(92)90017-A` | `ROOTING_SUCCESS / PRIOR_ART` |
| minimum NFA hardness | T. Jiang & B. Ravikumar, *Minimal NFA Problems are Hard*, SIAM J. Comput. 22(6), 1993, DOI `10.1137/0222067` | `ROOTING_SUCCESS / PRIOR_ART` |
| stochastic aggregation analogue | P. Buchholz, *Exact and Ordinary Lumpability in Finite Markov Chains*, J. Applied Probability 31(1), 1994, DOI `10.2307/3215235` | neighboring prior art; not a proof dependency |
| Boolean relational branch timing | Enterprise Math R015 | internal dependency |
| saturation/composition and power bracket | Enterprise Math R017/R018 | internal dependency |
| semantics vs representation-resource Pareto | Enterprise Math R014/P018 bridge | internal routing |

Enterprise-specific residue is the typed routing:

```text
collapse semantics
-> declared future result-support language
-> deterministic residual kernel
-> optional Boolean branching factorization
-> on-demand materialization/recoalescence
-> fully charged representation-resource Pareto
```

plus arithmetic pressure tests that identify when future operations reconstruct the fine state.

---

## 10. T10 — active kill test

Eight attack routes were applied.

1. **Hidden fine support in metadata.** Exact subset metadata can cost the full fine bitset. Universal compression claim killed.
2. **Long-horizon floor translation.** Coprime translation eventually reconstructs every residue. Branching can only defer/factor.
3. **Power bracket + translation.** `(4,9)` under `+1` reconstructs all interior positions by horizon 3.
4. **Middle incidence.** Minimal exact token can be exact fine identity, yielding zero compression.
5. **Multiplicity/provenance/weights.** Boolean union is the wrong carrier when those observables are declared.
6. **Branch minimization complexity.** A compact exact carrier may be too costly to synthesize.
7. **Laziness confound.** Lazy deterministic refinement must be the control; only NFA-like factorization proves branching-specific static reduction.
8. **Symbolic deterministic representation.** Explicit DFA state count may overstate deterministic bit/compiler cost.

The strongest universal claim is therefore false:

> “runtime branching is always strictly cheaper/stronger than deterministic future-complete refinement.”

The scoped claim is true:

> “within union-preserving final result-support semantics, Boolean branch presentations plus on-demand refinement form an exact alternative implementation class and can occupy Pareto points unavailable to an explicit deterministic residual table.”

---

## 11. Resource-regime classification

### Branching attractive

- Boolean result support only and union-preserving future steps;
- many deterministic residuals are unions of a small transition-stable atom basis;
- short/selective queries materialize only a sparse suffix/reachable fragment;
- encoder/correlation metadata remains sparse after full accounting;
- storage/model-size pressure dominates per-step work;
- remaining signatures quickly become equal and permit recoalescence.

### Deterministic refinement preferable

- many repeated queries amortize global refinement;
- residual machine is already small or symbolically factored;
- serial latency/runtime work is more important than storage;
- branch width approaches residual/fibre size;
- exact branching synthesis is expensive.

### Neither Boolean carrier adequate

Path multiplicity, provenance identity, probabilities/weights, signed cancellation, and support-global nonlinear predicates require a richer algebraic carrier.

---

## 12. Downstream recommendations

### P023

Route after semantic future-safe precision is fixed:

```text
semantic target
-> canonical deterministic future kernel rho_U
-> choose exact representation: deterministic / Boolean branching / symbolic / fine support
-> compare by R014 resource Pareto
```

Do not redefine semantic precision so that “more branches” means “finer”. Suggested explicit states: `FUNCTIONAL_SAFE`, `SUPPORT_SAFE_DETERMINISTIC`, `SUPPORT_SAFE_BRANCHING`, `SUPPORT_UNSAFE`.

### P018

Keep cell label, full cell fibre, set of alternative cells, branch atom, and live branch set type-distinct. For power brackets import only the scoped R018 result: endpoints suffice after endpoint selection, not before arbitrary fine-state futures.

### R014

Add branch atom count, encoder bits/incidences, transition incidences, max/cumulative live width, correlation metadata, split/coalesce work, synthesis cost, and query amortization to the resource vector.

### P021 / witness semantics

Do not project witness/multiplicity semantics to Boolean support unless downstream only asks existential result support. If witness identity remains observable, branch labels are semantic data.

### Shared tool

A reusable finite-state **representation analyzer/compiler** is justified after Driver review. It should accept the fine relation system, collapse `q`, declared future language `U`, and final support observable; return the deterministic future kernel, one-step kernel, exact Boolean branching candidates, on-demand materialization, recoalescence checks, full charged resource vector, and counterexample on failure.

No Lean payload is required yet.

---

## 13. Proposed compact Lean payload (future)

If Driver wants a formal gate, the useful core is:

1. `futureKernel_coarsest`;
2. `branchPresentation_support_exact_of_singleton_exact`;
3. `split_execute_union_invariant`;
4. `recoalesce_iff_remainingSignature_eq`;
5. `floorTranslation_futureClass_count`.

NFA Pareto/minimization evidence should remain executable/prior-art evidence rather than Foundation theorems.

---

## 14. Final Driver answer

**Is branching-collapse a strong reusable tool? Yes, but only as a typed, language-relative exact representation/compiler tool.**

It is strong when the declared future observable is Boolean result support, dynamics are union preserving, and residual behavior has either a sparse Boolean/NFA-like factorization whose full metadata cost remains smaller, or a sparse query-local reachable region where on-demand materialization saves global work (with lazy deterministic refinement as control).

It is **not** a universal semantic improvement over deterministic collapse. It cannot erase information actually distinguished by the future language. Coprime floor translation and translated power brackets eventually reconstruct hidden phase/fine state; middle-incidence and witness-cutoff examples can force exact fine identity; multiplicity/provenance require richer carriers.

The correct routing is

\[
\boxed{\text{semantic exactness first}\;\to\;\text{deterministic residual baseline}\;\to\;\text{branching/symbolic representation Pareto}.}
\]

Branching survives R021 as a reusable **representation calculus**, not as a replacement for the deterministic future-signature theorem and not as a new scalar precision notion.

**Canonical status:** `NOT_CANONICAL`.
