# X6 — PR #1257 historical quotient: first positive N-BRC fibre failures at n=3 and n=6

- Research mother: `RS-X6-LEGACY-PLANE-RECONCILIATION` / immutable publication `TP2-B4A441B23DA3159232C2`.
- Own provenance: `EM-X6-FB6990`; SID `MCP-082892eb480e45dea6d4b9fcc0491034`; existing CLAIM `MCP-30a8f5fd123215e08bd4a7cf`; RUN `RUN-3356cbe3c2b4916d79399941`. These are identifiers, not a current authorization receipt.
- Current mathematical baseline: P000 V5 / signed native X6 Cell torsor, `G6=Z^6`; native positive endpoint vector is an integer displacement, with six individually labeled axes.
- Historical comparison only: withdrawn/superseded PR #1257, pinned `awdawmip/enterprise-math@472ebb9fd09b83035ecd66ebcb3ee491ff89fcfc`, `experiments/x6_native_universal_completion_v2_20260905/x6_cell.py` (Git blob `face40b6834477b3ed1761780ecda34d340ec8fb`), `brc_kernel.py` (Git blob `bd569e030b3c0406bb04dbdb7df536b3b20ce89b`), and correction `research_notes/X6_ENDPOINT_QUOTIENT_TYPE_AUDIT_CORRECTION_V6_20260905.md` (Git blob `6f590af388c9fb4b5ff5c6c384e614042fd8e133`).
- Status: **AUTHOR-PROVED, NEW EXACT FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED**. No legacy PR executable or R063 native benchmark was rerun. This is a new comparison of the original pinned observer with the current typed positive native N-BRC interface, not a rehabilitation of the superseded quotient as X6 Cell ontology.

## 1. Explicit operator and preserved types

Label six **positive** native axes in the PR's order as `AB,AC,AD,BC,BD,CD`, corresponding to the six independent current native signed-X6 coordinate directions `e_0,...,e_5` when used as *input*, without identifying their Cell endpoints. For `z=(z_0,...,z_5) in N^6` define the historical additional-quotient observer

```
q(z) = sum_i z_i g_i in Z^2 x Z/2,
g0=( 1, 0,0), g1=( 0, 1,0), g2=(-1,-1,0),
g3=(-1,-1,1), g4=( 0, 1,1), g5=( 1, 0,1).
```

The third coordinate is reduced modulo 2. Retain current native independent quantities `n(z)=sum z_i`, `Q(z)=sum z_i^2` and positive shortest primitive word multiplicity

```
B(z) = n(z)! / product_i z_i!    (a nonnegative integer).
```

Here `q` is a *historical derived observer*, `n` is primitive path length, `Q` is the squared native six-axis component norm and `B` counts exact positive-axis permutations at each *native* endpoint. A sum of `B` over several endpoints is a different quotient-aggregated mass. A signed C2 character difference is yet another derived channel.

## 2. Two exact earliest-loss thresholds

**Theorem A — observer plus length.** There is no function `f(q,n)` equal to `B(z)` on all positive native six-axis endpoint vectors. The **first** failure is at `n=3`.

At `n=2`, although 21 native positive endpoint vectors occupy only 12 `q`-fibres (nine fibres with two endpoints; three with one), every individual fibre has constant `B`. At `n=1`, all six images are distinct. At `n=3`, 56 native endpoints occupy 20 quotient images; precisely 18 of these 20 fibres contain two different values of `B`. The two other fibres have the constant value `B=6`. A witness is

```
z=(3,0,0,0,0,0), z'=(1,0,0,0,0,2)
q(z)=q(z')=(3,0,0), n(z)=n(z')=3,
B(z)=1, B(z')=3.
```

The exact six-generator image and the finite enumeration below certify minimality without treating quotient states as native Cell identities.

**Theorem B — even retaining the native quadratic norm.** There is no function `F(q,n,Q)` equal to `B(z)` on all positive native six-axis endpoint vectors. The **first** failure is at `n=6`.

For every `n<=5`, the integer partitions of `n` have pairwise distinct sums of squares; hence `(n,Q)` already determines the unordered multiplicity partition, and thus the multinomial `B`. At `n=6`, take

```
A=(3,1,0,0,1,1),     B=(2,2,0,0,0,2).
q(A)=q(B)=(4,2,0);   n(A)=n(B)=6;   Q(A)=Q(B)=12;
B(A)=6!/(3! 1! 1! 1!)=120;
B(B)=6!/(2! 2! 2!)=90.
```

This is an **infinite exact family**, not merely one finite example. For every `t>=0`, set

```
A_t=(3,1,t,0,1,1),   B_t=(2,2,t,0,0,2).
q(A_t)=q(B_t)=(4-t,2-t,0);
n(A_t)=n(B_t)=6+t;   Q(A_t)=Q(B_t)=12+t^2;
B(A_t)=(6+t)!/(6 t!); B(B_t)=(6+t)!/(8 t!);
B(A_t)/B(B_t)=4/3.
```

Thus `q,n,Q` preserve the same observer endpoint, native primitive word length and native squared distance while losing a **persistent positive integer path-multiplicity distinction**. The missing datum is native axis-count/provenance shape, or an equivalent sufficient statistic for the declared future `B` readout. This is an exact observer-descent failure, not negative probability mass or a signed cancellation.

## 3. Executed independent small-shell integer certificate

A newly authored exact Python checker (not the original PR test) enumerates native positive axis-count multisets, computes `q,n,Q,B` using integer arithmetic and independently checks all shell totals `sum B=6^n` for `n=0..6`. It reports:

| n | native positive endpoints `C(n+5,5)` | historical q endpoints |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 6 | 6 |
| 2 | 21 | 12 |
| 3 | 56 | 20 |
| 4 | 126 | 30 |
| 5 | 252 | 42 |
| 6 | 462 | 56 |

Mixed `B` fibres by `(q,n)` at `n=0,1,2,3`: `0,0,0,18`. Mixed `B` fibres by `(q,n,Q)` at `n=0..6`: `0,0,0,0,0,0,6`; at `n=6` there are 166 distinct `(q,Q)` fibres. The executable also checks `t=0..11` of the displayed infinite family; the universal identities follow algebraically for every integer `t>=0`.

Checker: `research_checks/X6_PR1257_OBSERVER_NBRC_NONFACTOR_N6_20261114_1900.py` (executed locally: `PASS_X6_PR1257_OBSERVER_NBRC_NONFACTOR`; commit is separately source-pinned in the own Research Activity).

## 4. Original-call-site classification and next frontier

At original PR #1257 `brc_kernel.py`, `c2_weight_channels` appends `left-right` only to an explicitly **signed derived C2 character** readout; each original branch weight must be strictly positive. The same file's `equal_axis_visible_multiplicity` aggregates positive endpoint multiplicities with `+`, not signed subtraction. These exact original function sites are *not* an LP019 erroneous subtraction of positive natural N-BRC. The historical quotient was already explicitly superseded as a full X6 Cell model; this report certifies an additional minimal BRC information-loss boundary for attempts to reuse its observer.

Outstanding mother work: locate any actually active erroneous LP011 signed-X6 dominant-axis/argmax caller and LP019 positive-natural-BRC subtractive caller in remaining frozen branches/current dynamic consumers, if such callers exist; finish old/current 28-LP dependency ledger and independent Driver `REQUEST_REVISION`. Preserve actual frozen R063 C3/C4 benchmark as **not rerun**.

Do not repeat earlier 11 published semantic units; do not retry the specifically safety-denied 17:00 R063 Stage2 prose report, including rewrapping or alternate transport. The present PR1257 theorem and checker are distinct fresh sources and do not alter that decision.
