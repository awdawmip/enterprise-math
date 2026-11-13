# R762J — Exact source-state residual and bounded co-presence BRC enumeration

Date: 2026-11-13 (Asia/Shanghai). Status: **AUTHOR-SIDE EXACT PROOF + REPRODUCIBLE INTEGER VERIFICATION / NOT_REVIEWED**. Parent Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; publication: `TP2-8B7E13C5904A2D6F1142`; frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.

Predecessor R762I Draft PR #2292 supplies the persistent three-source port-carrier model. Here we keep three sources for P000's primitive triadic question, and use general `n` **only as a combinatorial theorem**, not as a proposal for higher-arity primitive equilibrium. The three source-labeled ports remain at distinct signed X6 primitive adjacent Cells; no new spatial dimension or Euclidean angle is introduced. A source `i` starts `U` (unopened), its outbound `O_i` changes `U→A` (active at its assigned port), and its return `I_i` changes `A→C` (completed at the root). Every source is processed exactly once. Serial order is an abstract event index, not physical heartbeat time.

## Theorem 1 — minimal sufficient *named future-feasibility* state

For the language of all legal **source-named** continuations of a prefix, the exact minimal deterministic residual state is the ternary vector `s=(s_1,...,s_n)∈{U,A,C}^n`. Every one of the `3^n` states is reachable. Two prefixes have exactly the same legal future event words if and only if their ternary vectors are identical. The minimal fixed-width code is `ceil(log2(3^n))` bits, hence **27 states and 5 bits** for n=3.

**Proof.** In state `s`, `O_i` is legal precisely if `s_i=U`, and `I_i` precisely if `s_i=A`. It follows inductively that equal vectors admit exactly the same legal suffix words. Conversely, different vectors differ at some named source i. The sets of legal one-letter continuations for `U,A,C` are respectively `{O_i}`, `{I_i}`, and the empty set, which distinguishes that coordinate. All `3^n` vectors are reached by performing `O_i,I_i` for each source declared `C`, only `O_i` for each source declared `A`, and no event for each `U`. Thus no quotient with fewer than `3^n` states preserves all named future legality. The observed **joint occupancy** `A(s)` alone has only `2^n` possible values, but fails to distinguish unopened from completed sources; the Boolean "all active" has only two values. This exactly identifies the additional retained residual required by the stated observer.

The theorem concerns named future legalities, not future full V29/V39 observations or recovery of earlier event order. Those require any relevant ledger/source history as separately typed fields. It also does not assert that `O_i/I_i` are actual admitted physical force events.

## Theorem 2 — exact N-BRC branch multiplicity of every ternary prefix state

Fix a labeled state with `a` active sources, `c` completed sources and `u=n-a-c` unopened sources. Every source-specific legal history reaching that state has exactly `t=a+2c` events. The number of distinct ordered source-named prefixes is

```text
B(s) = (a+2c)! / 2^c.
```

**Proof.** The event set consists of both `O_i` and `I_i` for each of the `c` completed sources, and only `O_i` for the `a` active sources. Among the `t!` permutations, the `c` disjoint precedence conditions `O_i<I_i` each halve the count. They act freely and independently, giving precisely `t!/2^c`. The identity counts **positive, source-labeled finite branches**; it is an exact integer N-BRC/multiplicity carrier and no signed amplitude cancellation is used. In particular, the full terminal state has `(2n)!/2^n` histories, matching R762I, but every intermediate `3^n` source state now has a closed-form branch count.

For n=3, sum `B(s)` over all prefix states of each length t gives the length-specific schedule counts

```text
t=0,1,2,3,4,5,6:  1, 3, 9, 24, 54, 90, 90.
```

These counts are a typed branch multiplicity, not a claim that time advances by one heartbeat per event.

## Theorem 3 — bounded simultaneous-port capacity (all n)

Let `M` be the maximum number of active named sources in a complete schedule. Let `N_{n,≤k}` count the schedules with `M≤k`. For a Dyck word `D` of n opening and n closing brackets, write `h(d)` for the number of active sources immediately before each closing bracket. Then:

```text
N_{n,≤k} = n! * sum_{D: length 2n, max-height ≤k} product_{downstep d in D} h(d).
```

**Proof.** Forget the named source but retain `O` and `I`. The resulting legal sequence is a Dyck path. For any fixed Dyck path, assign distinct source identities to the n opening steps in n! ways; for each closing step at height h, choose one of the h currently active sources to return. This gives exactly `n!∏h(d)` named histories, preserving identity multiplicity. Bounding the number of active ports is precisely bounding the Dyck height.

Define formal ordinary generating series `F_k^{(h)}(z)` for Dyck excursions based at height h and confined to height ≤k, with each descent from level j weighted by j and a pair weighted by z. First-return decomposition proves

```text
F_k^(k)(z)=1;
F_k^(h)(z) = 1 / (1-(h+1) z F_k^(h+1)(z)), 0≤h<k.
N_(n,≤k) = n! [z^n] F_k^(0)(z).
```

Thus the exact positive-branch count is the coefficient of the finite Stieltjes continued fraction `1/(1-z/(1-2z/(.../(1-kz))))`. All series identities are **formal** and use integer branch weights, not analytic approximation or a physical BRC propagator.

For capacity 1, every opening must be immediately followed by its matching return, so `N_{n,≤1}=n!`. At capacity 2, the formal fraction simplifies:

```text
F_2^(0)(z)=(1-2z)/(1-3z).
N_(n,≤2)=n! 3^(n-1) for every n≥1.
N_(n,M=2)=n! (3^(n-1)-1).
```

Consequently the exact **three-source** split is

```text
M=1 : 6 ; M=2 : 48 ; M=3 : 36 ; total : 90.
```

For four independently named carriers, the new computed split is `24,624,1296,576` for M=1,2,3,4 (total 2520). The general formula establishes a reusable capacity-law for arbitrary finite n within this combinatorial model.

## Reproduction, scope, and what remains unresolved

`research_notes/R762J_VERIFY.js` implements the exact source-labeled 3-status N-BRC transition (one branch per distinct allowable named event, integer weights), retains the peak co-presence, and checks the derived state multiplicities. Independently, a Dyck-word recursion with downstep height weights verifies the capacity histogram. All n=1..8 pass; the n=8 terminal count is 81,729,648,000 and exactly 6,561 distinct ternary states are checked over all prefix lengths. `research_notes/R762J_EVIDENCE.json` is the verbatim machine output.

Provenance: R762I PR #2292; P000 signed Cell/triadic foundation at scientific pin above; source current `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context` and heartbeat/BRC-only constraints. This result uses the exact source-named positive-branch multiplicity domain of N-BRC, without π, trigonometric functions, matrix exponentials or physical residual attribution. It neither equates coincident port occupancy to `TRIADIC_CLOSURE_E` nor computes V29 PASS/TRANSFER or V39 transport.

**Next discriminating experiment:** obtain the source-legal three-force quantum and true `TRIADIC_CLOSURE_E` same-state admission predicate. Test whether the same ternary source state, with different ordering histories, yields identical (i) event permission, (ii) V29 ledger increment and (iii) V39 loop transport. The **first** difference supplies the minimal concrete repair state for that target; if the typed transition depends only on ternary status, this theorem supplies a 27-state legal-suffix core. Retain full provenance until that observer-specific safe quotient is established.

Control: author-side independent research under a currently unresolved native continuation read; no active CLAIM, authenticated new execution run, Source Result or Driver review is asserted by this document. Frozen source and ACTIVE/P000 remain unchanged.
