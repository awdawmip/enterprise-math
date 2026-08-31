# P021 Focusing / Direction-Transport Continuation — Direction-Identity Matching Correction

Status: `RESEARCH RETURN / BOUNDED P021-LOCAL CORRECTION FROZEN`  
Task: `RS-P021-FOCUSING-DIRECTION`  
Researcher-ID: `EM-P021-03162B`  
Claim: `chatgpt-p021-20260828-2334`  
Execution branch: `research/p021-focusing-direction-em-p021-03162b`  
Execution base: `c884ff0d83ac6e6455665bfd6e9366dd8107f2c1`  
Owner: `program/p021-causal-focusing-v3`

## 1. Executive verdict

The historical P021 direction-transport statement

> one-to-one direction identity is canonical from composability support iff the
> support matrix is a permutation matrix

is **too strong under the natural global support-compatible identity semantics**.

The exact correction is a typed fork.

1. **Edge-complete / locally deterministic identity.**  
   If every positive composability edge itself must be the graph of the identity
   transport, then the historical criterion is correct: the support must be a
   permutation matrix.

2. **Global support-compatible identity.**  
   If the declared future observable asks only for a bijection between current and
   next direction classes that is compatible with positive composability, then
   support determines a canonical identity exactly when the support bipartite graph
   has a **unique perfect matching**. This is strictly weaker than permutation
   support.

The two notions must not be conflated.

This correction is P021-local: it classifies what the direction-composability
observable itself can determine. It does **not** re-own generic future quotient
theory from A2/P023 or generic relation/witness algebra from A4.

## 2. Frozen input semantics

Let the current direction classes be

\[
L=\{D^t_1,\ldots,D^t_n\}
\]

and the next direction classes be

\[
R=\{D^{t+1}_1,\ldots,D^{t+1}_n\}.
\]

Retain the historical P021 composability count

\[
T_{ij}
=
\#\{((u,v),(v,w)):
(u,v)\in D^t_i,\ (v,w)\in D^{t+1}_j\}.
\]

Define the Boolean support

\[
S_{ij}=\mathbf 1[T_{ij}>0].
\]

Equivalently, let \(G_S=(L\sqcup R,E_S)\) be the bipartite graph with

\[
(D_i^t,D_j^{t+1})\in E_S
\quad\Longleftrightarrow\quad
S_{ij}=1.
\]

No weights, metric, physical interpretation, or hidden continuum structure are
used below.

## 3. Declare the future observable before collapsing detail

The bounded future observable studied here is:

\[
\mathcal I(S)=
\begin{cases}
\texttt{IMPOSSIBLE}, & G_S\text{ has no perfect matching},\\
\texttt{UNIQUE}(M), & G_S\text{ has exactly one perfect matching }M,\\
\texttt{AMBIGUOUS}, & G_S\text{ has at least two perfect matchings}.
\end{cases}
\]

This observable asks only:

- can all current direction classes be continued injectively and exhaustively to
  next classes?
- if yes, is the continuation forced by support alone?
- if forced, what is the forced pairing?

It does **not** ask:

- whether every positive support edge itself is an identity edge;
- exact multi-step chain counts;
- exact middle-incidence witness joins;
- physical focusing, curvature, shear, Ricci terms, or any GR interpretation.

That scope distinction is theorem-critical.

## 4. P021-DIM-T01 — Typed direction-identity criterion

### 4.1 Strong local / edge-complete semantics

Suppose the intended identity relation must equal the entire positive support
relation.

Then a one-to-one identity exists iff:

1. the support is square;
2. every row contains exactly one `1`;
3. every column contains exactly one `1`.

Equivalently, \(S\) is a permutation matrix.

So the historical P021 criterion remains valid for this **strong** semantics.

### 4.2 Global support-compatible semantics

Suppose instead that a full direction identity is a bijection

\[
\pi:L\to R
\]

such that

\[
S_{i,\pi(i)}=1
\qquad\text{for every }i.
\]

Then such bijections are exactly the perfect matchings of \(G_S\).

Therefore:

\[
\boxed{
\text{support canonically determines the global full identity}
\iff
G_S\text{ has a unique perfect matching}.
}
\]

This is a direct equivalence by definition of perfect matching.

The historical permutation-support condition is sufficient, but not necessary.

## 5. P021-DIM-C01 — Minimal exact counterexample to historical necessity

Take

\[
S=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]

This support is not a permutation matrix:

- row 1 has two positive supports;
- column 2 has two positive supports.

Nevertheless there is exactly one perfect matching.

The second current class has only one available next class, so it must map

\[
D^t_2\mapsto D^{t+1}_2.
\]

That consumes the second next class and forces

\[
D^t_1\mapsto D^{t+1}_1.
\]

Thus support alone determines the unique global bijection

\[
\pi=(1\mapsto1,\ 2\mapsto2)
\]

without any additional label or witness choice.

Hence the historical implication

\[
\text{non-permutation support}
\Longrightarrow
\text{no canonical one-to-one identity from support}
\]

is false under global support-compatible semantics.

This is minimal: at \(n=1\), a support with a unique perfect matching is already
the \(1\times1\) permutation support.

## 6. P021-DIM-T02 — Infinite strictness family

For every \(n\ge2\), define

\[
U^{(n)}_{ij}=\mathbf1[i\le j].
\]

This is the upper-triangular all-ones-on-and-above-diagonal support.

It is not a permutation matrix for any \(n\ge2\), but it has a unique perfect
matching: the diagonal.

Proof is forced elimination.

- Row \(n\) is adjacent only to column \(n\), so \(n\mapsto n\) is forced.
- Delete that matched row and column.
- The remaining support is \(U^{(n-1)}\).
- Induct.

Therefore the gap between permutation support and canonical global identity is
not an isolated \(2\times2\) accident; it persists for arbitrarily many
direction classes.

## 7. P021-DIM-T03 — Exact ambiguity criterion via alternating cycles

Let \(M\) be any perfect matching of \(G_S\).

Then

\[
\boxed{
M\text{ is the unique perfect matching}
\iff
G_S\text{ contains no }M\text{-alternating cycle}.
}
\]

Proof:

- If an \(M\)-alternating cycle exists, flip matched/unmatched edges along the
  cycle. The result is a distinct perfect matching.
- Conversely, if \(M'\neq M\) is another perfect matching, the symmetric
  difference \(M\triangle M'\) is a disjoint union of even cycles alternating
  between \(M\) and \(M'\). Hence an \(M\)-alternating cycle exists.

So global direction-identity ambiguity has an exact finite obstruction:
an alternating cycle in the support relation.

This is standard matching theory, not a project novelty claim.

## 8. P021-DIM-T04 — Direction identity-retention defect

The same support gives a useful bounded P021 observable even when no full
bijection exists.

Let

\[
\nu(S)
\]

be the maximum matching size of \(G_S\). Define

\[
\boxed{\delta_{\mathrm{id}}(S)=n-\nu(S).}
\]

Then:

- \(\nu(S)\) is the maximum number of current direction classes that can be
  assigned pairwise distinct support-compatible next identities;
- \(\delta_{\mathrm{id}}(S)\) is the exact minimum number of current classes that
  must fail such one-step injective identity retention.

By the Hall-defect form of the bipartite matching theorem,

\[
\boxed{
\delta_{\mathrm{id}}(S)
=
\max_{A\subseteq L}
\bigl(|A|-|N(A)|\bigr).
}
\]

This is a precise one-step **identity-retention defect**.

It must not be silently renamed a physical focusing scalar. Birth/death,
coalescence, physical expansion, and GR interpretation require separately
declared semantics and, for physics, the P016 validation/falsification boundary.

## 9. Exact collapse boundary for this task

The following distinctions are now frozen.

| Declared future question | Minimum P021-local data used here | Can counts `T_ij` be collapsed to support? | Can exact witness identity `W_ij` be collapsed? |
|---|---|---:|---:|
| Does a support-compatible full bijection exist? | Boolean support `S` | Yes | Yes |
| Is that full bijection canonical from support alone? | Boolean support `S` | Yes | Yes |
| What is the unique pairing, when unique? | Boolean support `S` | Yes | Yes |
| What is the one-step identity-retention defect `n-nu(S)`? | Boolean support `S` | Yes | Yes |
| Does every positive composability edge itself equal an identity edge? | Boolean support `S` | Yes | Yes |
| Exact multi-step chain count/composition | Fine middle-incidence witness joins | No in general | **No** |
| Physical focusing/curvature interpretation | Outside this bounded theorem | N/A | N/A |

Thus the present correction does **not** weaken the historical witness-join
negative result.

In particular, the old two-chain lesson survives:

- cardinality shadows can agree while exact multi-step joins differ;
- the coupling-defect/equitability relay remains the correct downstream
  generalization for count observables;
- support-level unique matching is only a one-step typed identity observable.

## 10. Why the typed fork matters

A support matrix can exhibit local split/merge degrees while still admitting one
globally forced identity pairing.

Therefore three states must be distinguished:

1. **LOCAL_DETERMINISTIC**  
   support itself is a permutation matrix;

2. **GLOBAL_UNIQUE_ONLY**  
   support is not a permutation matrix but has a unique perfect matching;

3. **GLOBAL_AMBIGUOUS_OR_IMPOSSIBLE**  
   support has multiple perfect matchings or none.

The historical code/documentation collapsed states 1 and 2 by returning a
canonical pairing only in state 1.

That collapse is safe only if the declared observable is the strong
edge-complete/local-deterministic identity relation. It over-refines the state
needed for the global support-compatible identity observable.

## 11. Exact finite regression

Task-local checker:

`/scripts/check_p021_direction_identity_matching.py`

uses only Python standard library.

It verifies:

1. the minimal \(2\times2\) non-permutation unique-matching counterexample;
2. every Boolean square support through \(n=4\);
3. the Hall-defect identity on every such support;
4. unique-perfect-matching iff no alternating cycle on every support that has a
   perfect matching;
5. permutation support always implies unique perfect matching;
6. the upper-triangular strictness family through \(2\le n\le8\).

Frozen exhaustive census:

| n | all Boolean supports | no perfect matching | unique perfect matching | multiple perfect matchings | permutation support |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 0 | 1 |
| 2 | 16 | 9 | 6 | 1 | 2 |
| 3 | 512 | 265 | 150 | 97 | 6 |
| 4 | 65,536 | 27,713 | 13,032 | 24,791 | 24 |

The finite census is regression evidence only. The theorem statements above are
proved symbolically and do not depend on an \(n\le4\) cutoff.

Checker output at freeze:

```text
P021 direction-identity matching regression: PASS
n=1: total=2, no_pm=1, unique_pm=1, multiple_pm=0, permutation_support=1
n=2: total=16, no_pm=9, unique_pm=6, multiple_pm=1, permutation_support=2
n=3: total=512, no_pm=265, unique_pm=150, multiple_pm=97, permutation_support=6
n=4: total=65536, no_pm=27713, unique_pm=13032, multiple_pm=24791, permutation_support=24
minimal_nonpermutation_unique_pm=((1,1),(0,1))
upper_triangular_unique_pm_checked=2..8
hall_defect_identity_checked=all_supports_n<=4
alternating_cycle_uniqueness_checked=all_supports_with_pm_n<=4
```

## 12. Prior-art boundary

The mathematical primitives used in this correction are classical:

- bipartite matchings and Hall's condition/deficiency;
- unique perfect matchings;
- alternating-cycle characterization of matching uniqueness.

No novelty is claimed for those graph-theoretic results.

The P021-specific contribution of this return is the semantic placement:

- identifying that the historical P021 `permutation support iff canonical
  identity` statement mixed two distinct direction-identity observables;
- giving the exact weaker support-only criterion for the global observable;
- preserving the stronger permutation criterion for the local edge-complete
  observable;
- locating the exact boundary at which witness identity becomes necessary again
  for multi-step composition.

External prior-art checks used only to police novelty/scope:

- Encyclopedia of Mathematics, “Graph, bipartite”, including the matching
  deficiency formula;
- standard matching literature on the unique-perfect-matching /
  alternating-cycle criterion.

## 13. Owner / downstream routing

### P021 owner

Recommended correction:

- retain historical `permutation support` as the theorem for
  `EDGE_COMPLETE_LOCAL_IDENTITY`;
- add `UNIQUE_PERFECT_MATCHING` as the theorem for
  `GLOBAL_SUPPORT_COMPATIBLE_IDENTITY`;
- keep the two output types explicit in code and docs.

### A2/P023

`INFORM`, not re-own.

This return instantiates the general principle “collapse only relative to a
declared future observable”. Generic quotient/minimum-repair machinery remains
upstream-owned.

### A4

`INFORM`, not re-own.

Perfect matching is applied here to the P021 direction-composability relation.
Generic correspondence/witness composition remains A4-owned.

### P018

`INFORM`.

The distinction shows a concrete typed precision fork: local relation identity,
global matching identity, count composition, and witness identity require
different retained information.

### P016

No physical claim is made. No action is required.

## 14. Terminal task-scope verdict

\[
\boxed{
\texttt{P021\_DIRECTION\_IDENTITY\_CRITERION\_NARROWED}
}
\]

The bounded task slice is complete.

Hard block within this slice: `NONE`.

What remains open is a separate successor question, not a blocker:

- whether a useful **multi-step** canonical direction identity can be defined by
  composing unique one-step matchings while respecting exact witness joins, and
  exactly when that composition remains invariant under refinement.

That successor must preserve the already-proved fact that count/support shadows
are not composition-complete in general.
