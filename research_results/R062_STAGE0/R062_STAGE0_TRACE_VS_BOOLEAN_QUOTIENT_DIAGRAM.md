# R062 Stage 0 — Trace Quotient versus Boolean Quotient

Researcher-ID: `EM-R062-7C4A91`  
Status: `TRACE_AND_BOOLEAN_ARE_DISTINCT_QUOTIENTS_CLASSIFIED`

## 1. Common richer source

Let `M` be the family of typed native path witnesses carrying:

`(P, sector, generator word, full prefix trajectory, terminal typed cell)`.

Two different forgetful constructions leave this same source.

```text
                         q_trace
PATH / MULTIPATH  ---------------------->  TRANSLATED COMPONENT TRACE
      |                                        (P, sector, a,b)
      |
      | q_support
      v
BOOLEAN BRC SUPPORT
(typed start/terminal reachability)
```

## 2. Trace quotient

`q_trace` quotients a word by adjacent component-preserving commutations:

`X_i X_j ~ X_j X_i`.

For a fixed translated sector it retains start vertex `P`, sector/component family `(ij)`, component counts `(a,b)`, and therefore the frozen native line identity and typed terminal.

It destroys path order inside the commutation class, individual witness provenance, prefix geometry, and multiplicity unless the fiber cardinality is stored separately.

For `(3,4)`, 35 path witnesses map to one trace identity.

## 3. Boolean/support quotient

`q_support` forgets witness identity and multiplicity and retains only nonempty reachability/support in the declared relation execution.

It destroys witness order, multiplicity, provenance and prefix geometry.

It retains component labels and translated placement **only if those are retained in the state/generator typing outside the Boolean coefficient**. Bare Boolean adjacency does not recreate them.

For `(3,4)`, terminal multiplicity 35 maps to support 1.

## 4. Why the quotients are different

The equivalence relations are not the same.

- Trace equivalence is controlled by native component content and commutation.
- Boolean support equivalence is controlled by reachability/nonemptiness.

The reverse-third `(1,1)` shortcut is the separating witness: it can have the same terminal support as the `ij` trace while belonging to a different native component trace.

Thus the Boolean quotient can identify objects that trace semantics must keep apart when labels/context are erased.

On one already-fixed trace fiber, Boolean terminal support trivially factors through the trace because that trace determines its typed terminal. This restricted factorization does **not** make the two quotient notions identical globally.

## 5. Information-loss table

| Information | Path-BRC | N-BRC | Boolean-BRC | Trace |
|---|---:|---:|---:|---:|
| concrete witness identity | yes | no | no | no |
| multiplicity | yes | yes | no | no (unless separately attached) |
| word order | yes | no | no | no |
| prefix geometry | yes | no | no | no |
| native component content | yes | via typed skeleton | only via typed skeleton/context | yes |
| start placement `P` | yes | via typed state | via typed state | yes |
| terminal support | yes | yes | yes | determined by typed trace |

Machine census: `R062_STAGE0_INFORMATION_LOSS_CENSUS.json`.
