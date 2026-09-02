# BRC Weighted CWM — Local Bisimulation Boundary — 2026-09-02

Status: `RESEARCH CANDIDATE / EXACT COUNTEREXAMPLE / QUOTIENT BOUNDARY`

Researcher-ID: `EM-BRCWLOG-6F42A1`  
Parent: `research_notes/BRC_WEIGHTED_CWM_SAFE_QUOTIENT_20260902.md`

## 0. Result

The all-prefix safe CWM quotient is defined by equality of complete future transfer signatures. A tempting implementation shortcut is to require a stronger one-step condition:

> two states have the same aggregate lifted edge carrier into every current future-equivalence class.

That local weighted-bisimulation condition is **sufficient but not necessary** for equality of future CWM semantics.

The obstruction is exact factor relocation between an edge and the downstream transfer value. Two different local transition decompositions can produce the same complete path family statistics `(C,W,M)`.

Therefore:

```text
LOCAL_WEIGHTED_BISIMULATION
    -> FUTURE_CWM_EQUIVALENCE

but, in general,

FUTURE_CWM_EQUIVALENCE
    -/-> LOCAL_WEIGHTED_BISIMULATION.
```

A quotient algorithm that insists on raw one-step block transition equality can be strictly finer than the coarsest semantic CWM-safe quotient.

## 1. Sufficient local condition

Let `P` be a partition of successor states. For a state `x` and a block `B`, define the aggregate lifted one-step carrier

```text
A_P(x,B)
 = boxplus_{e:x->y, y in B} (1,a_e,a_e).
```

Suppose `x` and `y` have the same terminal observation and

```text
A_P(x,B)=A_P(y,B)
```

for every block `B`, while members of each block already have one common future transfer vector.

Then substituting the common block future values and using distributivity shows that `x` and `y` have equal future CWM transfer vectors.

So local block-aggregate equality is a valid sufficient refinement rule.

## 2. Exact counterexample to necessity

Use one terminal sink `t`.

Create three downstream state types:

```text
A1 -> t with weight 1
A2 -> t with weight 1
B  -> t with weight 2.
```

`A1` and `A2` are future-equivalent:

```text
F(A1)=F(A2)=(1,1,1).
```

`B` has

```text
F(B)=(1,2,2).
```

Now define two upstream states.

State `x`:

```text
x -> A1 with weight 1
x -> B  with weight 1.
```

Its terminal path masses are `(1,2)`, hence

```text
F(x)=(2,3,2).
```

State `y`:

```text
y -> A1 with weight 1
y -> A2 with weight 2.
```

Its terminal path masses are again `(1,2)`, hence

```text
F(y)=(2,3,2).
```

Therefore `x` and `y` belong to the same coarsest semantic CWM future class.

But relative to downstream future classes `[A]={A1,A2}` and `[B]={B}`:

```text
A_P(x,[A])=(1,1,1)
A_P(x,[B])=(1,1,1)

A_P(y,[A])=(2,3,2)
A_P(y,[B])=(0,0,0).
```

The local transition summaries differ sharply.

Thus one-step weighted bisimulation fails to merge `x,y` even though the exact all-future CWM quotient must merge them.

## 3. Factor-relocation interpretation

The reason is that a path mass factors as

```text
edge mass * downstream path mass.
```

For the second path:

```text
x route: 1 * 2 = 2
y route: 2 * 1 = 2.
```

The factor `2` moved from downstream state `B` onto the incoming edge to `A2` without changing the complete path mass.

In logarithmic coordinates this is simply

```text
0 + ln(2) = ln(2) + 0.
```

Hence local edge weight and downstream log potential have a factor-splitting freedom. A semantic quotient should depend on complete transfer values, not on one arbitrary location of multiplicative factors.

This resembles a gauge freedom, but no gauge-theory theorem is claimed here; the statement is only the exact invariance of path products under factor relocation.

## 4. Consequence for quotient construction

There are now two distinct compression levels:

### Level A — local bisimulation refinement

- easy to compute from local block transitions;
- sufficient for CWM future preservation;
- may retain more states than necessary.

### Level B — semantic future kernel

- identifies states exactly when their declared complete future transfer vectors agree;
- is coarsest under the all-prefix safety contract;
- can merge states whose local transition decompositions differ.

Do not claim Level A is canonical/minimal without an additional hypothesis that makes downstream transfer classes separating for local transition coefficients.

## 5. Potential completeness hypotheses

Local bisimulation could become necessary under stronger assumptions that prevent distinct block contributions from representing the same total future vector. Candidate hypotheses include:

1. algebraic independence/separation of block future signatures;
2. a declared canonical normalization that removes edge/downstream factor relocation;
3. unique decomposition in a free semimodule over future classes;
4. provenance-preserving rather than result-only weighted semantics.

None is assumed by the current CWM result layer.

## 6. Next question

The precise next target is to characterize when future transfer vectors admit a **canonical factor-normalized representative** for which local bisimulation becomes complete.

If such a normalization exists on a useful BRC subclass, it could compress the all-terminal transfer-vector kernel without sacrificing exactness. If not, semantic transfer hashing remains the correct minimal construction for finite DAGs.
