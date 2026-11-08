# PREFIX-606-R6 — Exact total-variation efficiency of all three native binary BRC slot tags

Date: 2026-11-08 Asia/Shanghai. Frozen pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`; original native BRC blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. Dependencies PREFIX-600/601/602/605. Status: AUTHOR_PROVED / EXACT_ALGEBRA_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem

Retain the exact 48 native BRC phases, slots 0/1/2, and the already declared nonnegative twelve-incidence weighted extension. Write P for the untagged next-phase matrix and C_j for the joint probability kernel of native slot j and terminal phase. Let `D={δ∈R^48: δP=0}` be the untagged observationally invisible signed source-phase directions. The three nonconstant binary tags record `1{slot=j}` jointly with the terminal phase.

**For every finite nonnegative incidence-weight vector t and every δ∈D, the following exact identities hold:**

```text
 ||δ C_0||_1 = (1/2) ||δ||_1
 ||δ C_1||_1 = (1/4) ||δ||_1
 ||δ C_2||_1 = (1/4) ||δ||_1.
```

For any pair of different initial phase laws π,π' satisfying `πP=π'P`, let `B_j(π)` be the full binary-tag/terminal-phase joint law. Their **total-variation distances** satisfy

```text
 TV(B_0(π),B_0(π')) = TV(π,π')
 TV(B_1(π),B_1(π')) = (1/2) TV(π,π')
 TV(B_2(π),B_2(π')) = (1/2) TV(π,π').
```

Thus the internal-slot tag **preserves all total-variation separation** on the directions invisible to the untagged endpoint, whereas either cross-slot tag retains exactly half. All three remain algebraically sufficient by PREFIX-605. These are sharp operator identities on the untagged nullspace, valid at every critical stratum (and vacuously at k=0).

## Proof

The six paired native incidences partition twelve source-incidence classes, two states in each signed 24-phase block. For each critical pair `{e,f}`, let `x=t_e>0` and `t_f=1/(4x)`. By the PREFIX-602 left-null formula and the 36 exact original-graph Laurent identities established in PREFIX-605, the basis left-null vector has the form `ell=s*w`, with source coordinates exactly `+(x+1/2),+(x+1/2),-(x+1/2),-(x+1/2)` on four distinct phases. Divide by `x+1/2` to obtain `h` with two +1, two -1, and `||h||_1=4`.

For slot 0, the four terminal-phase coefficients of `ell C_0` are `+1/2,+1/2,-x,-x`; dividing by `x+1/2` gives a vector with L1 norm 2. For slots 1 and 2, the two coefficients are `-1/2,+x`, giving L1 norm 1. The finite original BRC graph verifies that the source supports of all twelve possible h are disjoint and, for a fixed j, the terminal supports of all twelve `h C_j` are disjoint. Every δ in the exact left nullspace has a unique expansion `δ=Σ_a c_a h_a` over the active 2k critical signed-block generators. Therefore `||δ||_1=4Σ|c_a|`, `||δ C_0||_1=2Σ|c_a|` and `||δ C_1||_1=||δ C_2||_1=Σ|c_a|`. This proves the first three identities.

Since `δP=0`, the complementary binary-bit histogram is `δ(P-C_j)=-δ C_j`. Hence the full joint tagged output difference has L1 norm `2||δ C_j||_1`. Total variation is one half L1 difference, establishing the displayed TV identities. QED.

## Verification and interpretation

The executable standard-library exact certificate `PREFIX606_R6_exact_total_variation_tag_certificate.py` reuses the already checked 36 symbolic graph identities and independently rechecks signed input null vectors, every tagged kernel and all three L1 ratios for five asymmetric critical parameter choices `x∈{1/8,1/4,1/2,1,8}`, all six critical pairs active. Execution returned `ALL_CHECKS_PASS`; saved `PREFIX606_R6_RESULTS.json` records the exact checks. The all-weights claim is derived from the exact symbolic source graph and disjoint-support proof; five numerical rational cases are supplemental verification.

This result measures **statistical distinguishability** of initial distributions that had identical original untagged one-step endpoint laws. It does not assert full 96-port-bit recovery, full inverse conditioning for arbitrary differences, or a finite-N minimax risk bound. The original frozen t_e=1 model has k=0; the informative cases are the explicit weighted singular strata. Native root choices do not change phase/slot kernels.

**Next:** quantify finite-sample estimators and conditioning of the recovered initial phase law, including perturbations *near* the singular surfaces rather than exactly on them, and study the cost/benefit of using the more informative slot-0 bit.
