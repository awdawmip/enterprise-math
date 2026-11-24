# R5 — three scalar budget readings are necessary and sufficient

Date: 2026-11-14. Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Scientific input frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Derived radius-two, integer-coordinate, event-index center observer on exactly 954 events; closure mask B ranges over all 28 original length-three gaps, and the allowed center budgets are **all integers 214≤K≤954**.

Let `N_B(K)` denote the number of complete optimal center-index K-subsets for closure mask B. Define the full-budget optimizer-family trajectory `F(B)=(Opt_B(K))_{K=214}^{954}`. A scalar count sampling design is a list of center budgets `K_1,...,K_m` with the observation vector `(N_B(K_1),...,N_B(K_m))`. It *identifies* the full trajectory if equality of observed integer vectors for two 28-bit masks B and B' holds if and only if `F(B)=F(B')`. The design budgets may be any integers in the stated range, and may repeat.

**Theorem.** The minimum m for which such a scalar observation design identifies F(B) for every 28-bit B is **exactly three**. One optimal design is `(214,223,294)`.

## Necessity (uniform over all choices of two budgets)

The exact complete-family essential-cut support for each admissible K belongs to precisely one of three pairwise-disjoint coordinate blocks:

- `A={3,8,9,10,27}` for K214..222 (at K222 the smaller subset {27});
- `C={25,27}` for K223..291;
- `D={15,17}` for K293..314;

At K292 and all K315..954 the support is empty.

**Important correction to the naive disjoint-block argument:** A and C are not disjoint: both contain cut 27. Nevertheless, the private coordinates `A_private={3,8,9,10}`, `C_private={25}` and `D_private={15,17}` are pairwise disjoint and each occurs only in its corresponding budget band. Each nonempty band has at least one essential private coordinate that no other band can observe. Any two budget choices occupy at most two of these three bands. Choose a private coordinate from the missing band; flipping it while keeping every other cut fixed cannot change either sampled integer count (the complete optimizer family at both sampled budgets does not depend on that coordinate). However, the complete trajectory changes because that coordinate is essential at a budget in its band: the all-closed vs all-except-that-cut endpoints have distinct complete optimizer families. Thus no two scalar samples distinguish all trajectories.

Equivalently, identifying all distinct full trajectories requires observing each of the three disjoint **private-information** bands at least once. This argument applies even to arbitrary nonlinear decoding of the two observed exact integers, not only a linear or polynomial decoder. A single reading is a special case.

## Sufficiency (exact integer injectivity)

The independently executed verification `VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py` enumerated exact minimum-cost tie counts at each of the 2^5=32 masks on A at K214, each of the 2^2=4 masks on C at K223, and each of the 2^2=4 masks on D at K294. The count maps were each injective: respectively **32/32**, **4/4**, **4/4** distinct exact integers.

All 28-bit masks have the same full trajectory precisely when they agree on the union `U=A∪C∪D={3,8,9,10,15,17,25,27}` (size 8). The observation at K214 determines all of A, including common bit 27. The K223 reading determines the C pair (including 27), and K294 determines the D pair. Because each band count is injective on its own support, equality of all three observed integers implies the two masks agree on U and therefore have identical full trajectories. The reverse implication is immediate.

The original 28-bit masks have 2^8=256 possible complete-family trajectories and 2^20=1,048,576 masks per trajectory. This information-theoretic classification pertains to the declared observer and all admissible budgets, not native X6 state. The theorem is a purely discrete finite exact statement based on the previously established principal-mask filtering theorem, verified exact path spectra and high-budget invariance, with no independence or external physical validity asserted.

## Sources and reproducibility

- [Main optimizer-family tomography result](RESEARCH.md) and [exact integer program](VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py), branch `research/r5-global-optimizer-tomography-20261114`, published through Draft PR #2427.
- Frozen R5 input commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Historical full-prerequisite-mask results, Draft PR #2412, immutable commit `a242de1dbb59cd6df8cfced61f1405e8c09d3f7c`.

Remaining scientific question: compute **max_S min_T** center-replacement distance for low budgets K214–291; this minimal-three-count classification settles the pending scalar-tomography sample-number question.
