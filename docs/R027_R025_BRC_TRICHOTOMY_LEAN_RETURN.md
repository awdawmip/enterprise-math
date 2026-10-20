# R027 — R025 Constant-(p,r) BRC Trichotomy Lean Return

Researcher-ID: `EM-R027-C6194D`  
Task: `RS-R027-R025-BRC-PR-TRICHOTOMY-LEAN-FORMALIZATION`  
Taskbook source: `55a3ff09b9307ac05c0d03f02da3ce8939e9362c`  
Owner PR: `#507`  
Frozen semantic validation head: `bc5cd4bfbc7e19cbb10a2005a0d37fe4f6afd6bb`  
Status: `R025_BRC_TRICHOTOMY_CORE_PROVED / QUANTITATIVE_GROWTH_SCOPE_NARROWED / ROOT_BUILD_PASS / NOT_CANONICAL`

## 1. Scope preserved

This return formalizes only the arithmetic/precision specialization discovered by R025 for constant exponent `p`, constant integer refinement `r`, identity inter-layer operation, and p-th-power endpoint BRC. It does not modify the canonical R023/R023I Boolean/result-support semantics and does not add multiplicity, provenance, probability/weights, signed/amplitude cancellation, or path-count semantics.

Formal payload:

- `EnterpriseMath/Precision/PowerBRCTrichotomy.lean`
- root import in `EnterpriseMath.lean`
- synchronized machine/en/zh exact root-import indexes
- `experiments/r027_power_brc_trichotomy_oracle.py` as bounded mutation/debug evidence only

## 2. Exact objects

For `p r k : Nat`:

- `refinedPowerInput p r k = r * k^p`;
- `rootIndex p r k = EnterpriseMath.IntegerRoot.root p (r*k^p)`;
- exact child-root support is a singleton when the refined input is an exact p-th power and otherwise is the adjacent pair `{m,m+1}`;
- actual endpoint support is the injective positive-power image of the root-index support.

The formalization is theorem-critical exact integer arithmetic only; no floating root is used.

## 3. Return matrix

| Claim | R025 research form | Lean exact statement / asset | Status | Required hypotheses | Frozen counterexample / boundary |
|---|---|---|---|---|---|
| refinement/root basin | `m^p <= r*k^p < (m+1)^p` | `rootIndex_basin` | `LEAN_CHECKED_WIP` | `p != 0` | none |
| aligned freeze | `r=a^p -> m=ak`, singleton forever | `refinedPowerInput_aligned`, `rootIndex_aligned`, `childRootFinset_aligned`, `aligned_iterate_singleton` | `LEAN_CHECKED_WIP` | `p != 0` for root recovery | includes `r=1`, `r=2^p`, and super-threshold islands |
| nonalignment ambiguity | positive `k` cannot hide non-pth-power `r` | `positive_nonaligned_input_not_power`, `positive_nonaligned_root_not_exact` | `LEAN_CHECKED_WIP` | `p>=2`, `k>0`, nonaligned `r` | `k=0` is exact for every `r` |
| sub-threshold bounds | `k <= m_k < 2k` | `subthreshold_root_bounds` | `LEAN_CHECKED_WIP` | `p>=2`, `k>0`, `1<r<2^p` | no float-root argument |
| funnel spacing | `m_k+1 <= m_(k+1) <= m_k+2` | `funnel_spacing` | `LEAN_CHECKED_WIP` | `p>=2`, `1<r<2^p` | does not imply a duplicate every layer |
| interval support invariant | interval parents map to exact no-hole interval | `funnel_interval_finset` | `LEAN_CHECKED_WIP` | `p>=2`, `1<r<2^p`, `A<=B` | zero endpoint handled by exact-child convention |
| repeated funnel invariant | every finite iterate remains an integer interval | `repeated_funnel_interval` | `LEAN_CHECKED_WIP` | same funnel hypotheses | no path-multiplicity/probability claim |
| one-step funnel cardinal bound | no more than two children per parent | `childRootFinsetOf_card_le_two_mul`, `funnel_interval_card_le_two_mul` | `LEAN_CHECKED_WIP` | finite support; funnel specialization for interval theorem | this is not an exact `c^t` asymptotic theorem |
| super-threshold separation | `m_k+2 <= m_(k+1)` | `superthreshold_spacing` | `LEAN_CHECKED_WIP` | `p>=2`, `k>0`, `r>2^p` | nonalignment not needed for spacing itself |
| binary child injection/disjointness | two child pairs from distinct positive parents do not collide | `binary_child_disjoint_of_lt`, `binary_childRootFinset_card_two` | `LEAN_CHECKED_WIP` | `p>=2`, positive parents, `r>2^p`, nonaligned | aligned islands have singleton children |
| finite-support doubling | `card Child(S)=2 card(S)` | `binary_childRootFinsetOf_card` | `LEAN_CHECKED_WIP` | arbitrary finite **positive** support, `p>=2`, `r>2^p`, nonaligned | blanket theorem including `0` is false |
| repeated `2^t` growth | `card S_t=2^t card S_0` | `superthreshold_iterate_positive`, `binary_iterate_card` | `LEAN_CHECKED_WIP` | initial finite support all positive; binary regime | positivity is proved invariant |
| regime exhaustion | ALIGNED / FUNNEL / BINARY are pairwise exclusive and exhaustive | `regimes_mutually_exclusive`, `regimes_exhaustive`, `funnel_one_lt` | `LEAN_CHECKED_WIP` | `p>=2`, `r>=1` | equality `r=2^p` is ALIGNED |
| actual p-th-power support bridge | root labels determine exact endpoint states and preserve cardinality | `powerSupport_card`, aligned/funnel/binary actual-support theorems | `LEAN_CHECKED_WIP` | `p>0` for powering injectivity | root index is not identified literally with endpoint state |
| canonical R023 specialization | generic Boolean direct image equals finite arithmetic child-support image | `brc_rootSupport_relImage_bridge`, `brc_powerEndpoint_relImage_bridge` | `LEAN_CHECKED_WIP` | `p>0` for actual-state inverse identification | no change to R023 carrier or theorem statements |

## 4. Exact phase classifier

On the domain `p>=2`, `r>=1`:

1. **ALIGNED**: `exists a, r=a^p`.
   - Every refined p-power parent remains an exact p-power.
   - Child support is singleton.
   - This includes `r=1`, the threshold `r=2^p`, and all super-threshold perfect-pth-power islands.

2. **FUNNEL**: nonaligned and `r<2^p`.
   - Since `r>=1` and `r=1` is aligned, this sharpens to `1<r<2^p`.
   - Adjacent root indices advance by exactly one or two.
   - The union of endpoint children from an integer interval is an exact integer interval with no holes, and this interval representation is invariant under repeated layers.

3. **BINARY**: nonaligned and `2^p<r`.
   - Every positive parent is genuinely nonexact and therefore has two adjacent children.
   - Consecutive positive parents are separated by at least two root indices, so their child pairs are disjoint.
   - Any finite positive support doubles exactly at each layer and therefore has cardinality `2^t * card(S0)` after `t` layers.

## 5. Mandatory kill matrix

| False version | Frozen result |
|---|---|
| `r >= 2^p -> binary` | KILLED: `r=2^p` is exactly `2^p` and hence ALIGNED; `p=2,r=9` is a super-threshold aligned island. |
| doubling remains exact when `0` is present | KILLED: `zero_support_not_doubling`; `0` always maps exactly to singleton `{0}`. |
| every funnel layer has a duplicate collision | KILLED: `funnel_no_duplicate_witness` gives `p=2,r=3`, parent interval `{1,2}`, child interval `{1,2,3,4}`, exactly binary-sized for that layer. |
| nonaligned `r` can become exact after multiplying a positive `k^p` | KILLED by `positive_nonaligned_input_not_power`, using exact power divisibility/cancellation. |
| interval funnel implies multiplicity/probability law | KILLED BY SCOPE: only Boolean/result support is represented. |
| variable `(p_t,r_t)` words automatically inherit the constant classifier | KILLED BY SCOPE: no such inheritance theorem is stated. |
| R025 bounded Python attacks are proof | KILLED BY EVIDENCE DISCIPLINE: the Python oracle is explicitly regression/debug support only. |

## 6. Quantitative-growth scope

The exact Lean core proves the no-hole interval representation and the one-step finite upper bound `card(next) <= 2*card(current)`. It does **not** promote R025's descriptive `c^t`, `c=r^(1/p)`, growth-scale prose into an exact Lean asymptotic theorem in this task.

This narrowing is intentional: finite funnel windows can realize spacing `2` throughout one or more layers, so “strict subbinary at every layer” would be false. A sharper asymptotic/cardinality theorem, if desired, should be a separate descendant with its own exact constants/error bounds.

Therefore the exact return token is:

`R025_BRC_TRICHOTOMY_CORE_PROVED / QUANTITATIVE_GROWTH_SCOPE_NARROWED / ROOT_BUILD_PASS / NOT_CANONICAL`

## 7. R024 deterministic routing bridge

| Formal regime | Runtime implication candidate |
|---|---|
| ALIGNED | fixed-point / exact-power shortcut |
| FUNNEL | symbolic root-index interval / basin cursor |
| BINARY | explicit branch budget or factored binary token; do not pretend recoalescence exists |

This is a deterministic downstream routing interface only. R027 does not benchmark these runtime representations and does not modify R024 benchmark conclusions.

## 8. Validation and proof hygiene

Frozen semantic validation object:

- semantic head: `bc5cd4bfbc7e19cbb10a2005a0d37fe4f6afd6bb`;
- PR merge validation ref: `3f69dee2a22ffbf5922578242721f1b2e3534638`;
- Lean workflow run: `31512045852`;
- Lean build job: `93848024891`.

The job executed exactly:

```text
lake build --wfail -KCI EnterpriseMath
```

Load-bearing root-coverage evidence in the job log:

```text
Built EnterpriseMath.Precision.PowerBRCTrichotomy
Built EnterpriseMath
Build completed successfully (3028 jobs).
```

The same log's `#print axioms` audit reports only standard Lean/mathlib foundational dependencies such as `propext`, `Classical.choice`, and `Quot.sound`; the task module contains no `sorry`, `admit`, task-local `axiom`, or `postulate`.

Repository quality validation on the same semantic head also passed: job `93848309789` ran the repository unittest suite and finished `Ran 1356 tests ... OK`. The shared-surface integrity test passed, covering the synchronized machine/en/zh root-import registration.

Any owner-branch commits made after the frozen semantic validation head for the sole purpose of updating this return document do not modify the Lean module, `EnterpriseMath.lean`, common-surface registration, oracle, or theorem statements. The Driver handoff records the final owner head separately from the frozen semantic validation head, avoiding self-referential document-SHA churn.

## 9. Finite oracle status

The bounded exact oracle covers the taskbook boundary set and broader local attacks. It is deliberately non-authoritative relative to Lean. The owner package records a 724,010-case exact pressure sweep over funnel interval images and selected super-threshold positive-support doubling boxes with no counterexample; this remains regression evidence, not proof.

## 10. Canonicalization boundary

This owner result is `LEAN_CHECKED_WIP`, not `CANONICAL_MAIN` and not `LEAN_CHECKED_MAIN`. Canonical publication must remain a separate Driver/L4 integration decision. That integration must preserve the frozen R023/R023I carrier and theorem statements, replay only the R027 specialization payload, and rerun the applicable current-main admission/final gates.
