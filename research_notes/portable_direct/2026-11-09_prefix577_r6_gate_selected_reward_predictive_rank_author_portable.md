# BRC-X6: exact all-port gate-plus-reward predictive dimensions (2026-11-09)

**Status:** AUTHOR_PROVED / EXACT_INTEGER_CLOSURE / TWO_MODULAR_CROSSCHECKS / UNREVIEWED / NOT_ADMITTED. Frozen scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native model: 96 ports, 576 tagged actions, nine frozen roots `0,±e1,...,±e4`; original six spatial rewards `R1..R6` plus a separate gate indicator `K`.

## Statement

For observation subset `O`, a policy choice `u` and output symbol `o`, let
`M_{u,o}[p,q] = #{a: a is a permitted original action under u, next(p,a)=q, output_O(p,a)=o}`.
The all-port predictive space is `V_O = span_Q {M_{u1,o1}...M_{un,on} 1 : n≥0, all legal action/output words}`. Counts convert to the corresponding probabilities by multiplying each step by the known equal-choice normalization.

Policies: **passive** = six equally sampled tags; **newbit** = choose newbit and sample slot uniformly; **slot** = choose slot and sample newbit uniformly; **full** = choose both.

The exact dimensions over Q and the exact number of language-equivalent starting-port classes (rank / classes) are:

| Observed rewards and gate | Passive | Newbit | Slot | Full |
|---|---:|---:|---:|---:|
| `(K,R5)` | **29 / 37** | **29 / 37** | **48 / 51** | **48 / 51** |
| `(K,R6)` | **29 / 37** | **29 / 37** | **46 / 51** | **46 / 51** |
| `(K,R5,R6)` | **35 / 37** | **35 / 37** | **50 / 51** | **50 / 51** |

Each result holds at **every finite ordered observation-word length** for **all 96 initial ports** and each of the nine frozen roots. Exact strong-bisimulation block counts under the same policies are respectively `37,37,51,51` in each row. The already known gate-only regression is `11,11,44,44`, not a new claim.

The predictive spaces for passive and newbit-controlled observations are equal for each observation set. The slot-controlled and fully controlled spaces are likewise equal. The weaker conditioned operators are sums of the corresponding finer operators, so inclusion of spaces plus equality of independently established exact dimensions proves these equalities. Notably `(K,R5)` and `(K,R6)` have equal passive ranks (29) but unequal full-control ranks (48 vs 46), a concrete operation/observer dependence of the BRC residual. This does not contradict the previously established C2 symmetry of the uniform-start distribution: this theorem ranges over all initial ports and controlled choices.

## Exact proof and reproduction

The code uses the unchanged frozen kernel and checks the 576 individual tagged transitions against an independently retained CSV edge snapshot. It also checks that each of the nine roots gives exactly the same `next,K,R5,R6` on all 576 actions.

For each of 12 operator families, start with the all-ones vector in `Z^96`, repeatedly apply every nonzero operator, and maintain a rational basis using exact integer row elimination. At a pivot `p` for row `b`, replace `v` by `b[p]v-v[p]b` and divide by its gcd. This is exact rank computation over `Q`, not a floating-point fit. Once no new independent vector appears, directly verify that **all** basis images under **all** operators reduce exactly to zero. There are **4,467 exact image-closure checks** across the twelve cases. The basis is contained in the original predictive space (all generators are reached from `1` by permitted operators); it contains `1` and is invariant under every permitted operator. Therefore equality of spaces and the stated rank hold by induction for all lengths.

A fully separate CSV-driven implementation checks the ranks and strong partitions. Finite-field ranks over `F_1000000007` and `F_998244353` independently match the exact integer ranks. Grouping native ports by equality on all exact basis columns gives the language class counts. Maximum basis-word depths are 7 for passive/newbit single-axis, 6 for passive/newbit two-axis, and 5 for slot/full cases.

The original seven-file reproducible package generated in the research conversation contains `PREFIX577_R6_GATE_SELECTED_REWARD_PREDICTIVE_RANK_THEOREM_20261109.md`, `frozen_native_kernel_prefix577.py`, `native_edge_snapshot.csv`, `verify_gate_selected_reward_ranks.py`, `independent_csv_modular_crosscheck.py`, `GATE_SELECTED_REWARD_PREDICTIVE_RANK_CERTIFICATE.json`, and `MANIFEST_20261109_SELECTED_REWARD_RANK.json`. An independent extracted execution reproduced all exact and modular checks and every manifest file SHA-256.

- Exact JSON certificate SHA-256: `aaff81c056ae3a7d2c6f245a5f5d91770669ad3a9a34e8f862e33267b41ea9fd`.
- Original ZIP SHA-256: `d3d8cbe1a18835c2562cef8600beb7def4746e55acce787e87319e6344942172` (16,459 bytes).
- Predecessor author gate-policy quotient: `10136cd5654f545d201840234d2a71bd107054a6`.
- Predecessor author gate-only predictive ranks: `85a52df4e277dbb1c7abf81a17d3e736a2d48262`.

## Canonical Source and recovery boundary

The original D25 native continuation request `h40-r11-d25-continuation-20261108t1512-v1` now has `SUCCEEDED` receipt, observed 2026-11-08T16:40:40.741889Z. Its Source route is `REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION`, `owner=taskbook/unassigned`, `dispatch_state=NEEDS_DISPATCH`, `claim_id=null`, `execution_authorized=false`. The present research session still lacks the private execution capability required for native continuation, so **no Source CLAIM, OPEN, Result, task checkpoint or CM experiment was asserted**. The D25 original H0/B0 divided-power, `[X]U mod p^2`, Frobenius/eta, kappa and `Delta_p-R_p` remain open and retain priority under lawful dispatch.

The original four-file UR V2 bundle has not been recovered at the required 94,687 bytes / SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. Accepted D24 records remain sealed. This paper preserves author evidence and full contribution provenance; it is not Source-admitted science or an independent review.

**Optional scientific continuation:** characterize the exact annihilator relations behind the gaps between 37/51 language classes and the corresponding predictive dimensions under each declared control policy, then test adding one of `R1..R4`. Avoid overlapping current independent owners.
