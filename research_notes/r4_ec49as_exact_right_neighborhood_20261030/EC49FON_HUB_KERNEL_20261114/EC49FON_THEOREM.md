# EC49FON — Hub-root cancellation kernel and frozen native injectivity

Date 2026-11-14. **Author-proved exact algebraic theorem; exact finite author check; NOT_REVIEWED.** Continues [EC49FOM PR #2400](https://github.com/awdawmip/enterprise-math/pull/2400) at immutable commit `32380d1f974d87198fb67d7b0ba6a769a646a7df`. Frozen scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` is unchanged. Historical researcher provenance: `EM-DIRECT-204C14` / `RA-6893088D0A7347CE7F4D8720`. This is independent mathematical work outside a published `RS-EC49AS` task, not a CLAIM, Result or independent review.

## Exact algebraic theorem

Let R be a finite set of named roots, h in R the hub, and L a finite set of optional named demands independently assigned to roots. Assume for each l in L: h in E(l) and |E(l)| >= 2. Set A_l=E(l)\{h}, V_r={l:r in E(l)}, B_r={l:E(l)={h,r}} for r != h. Let g_r:2^{V_r}->Z be **arbitrary integer differences of reachable rooted costs**, after incorporating mandatory forced labels. For a complete legal assignment rho define S_r(rho)={l:rho(l)=r} and F(rho)=sum_r g_r(S_r(rho)).

**Theorem (complete integral kernel).** F(rho)=0 for *every* legal rho if and only if (g_r) is an integer linear combination of the following linearly independent generators:

* Constants: for each r!=h, g_r(S)=+1 and g_h(S)=-1, other components 0.
* Unary demand l: g_h(S)=1[l not in S] and g_r(S)=-1[l in S] for every alternative r in A_l; other components 0.
* Higher interactions: for each r!=h and each Q subset B_r of size at least two, g_h(S)=1[Q intersect S is empty] and g_r(S)=-1[Q subset S]; other components 0.

Therefore the kernel is a **free abelian group** of rank

`(|R|-1)+|L|+sum_{r!=h}(2^{|B_r|}-1-|B_r|)`.

In particular, every nonlinear globally cancelling interaction is supported inside a **binary spoke** B_r: a collection of labels whose only legal roots are the same pair {h,r}.

**Proof.** Write U(A)=g_h(L\A), where A is the set of labels not assigned to h. Let nu(Q), Q subset L, be its Boolean Möbius coefficients, and mu_r(Q), Q subset V_r, the Möbius coefficients of g_r for each r!=h. Put z_(l,r)=1[rho(l)=r] for r in A_l. Since 1[rho(l)!=h]=sum_{r in A_l}z_(l,r),

`F = sum_{Q subset L} nu(Q) prod_{l in Q}(sum_{r in A_l}z_(l,r)) + sum_{r!=h}sum_{Q subset V_r} mu_r(Q) prod_{l in Q}z_(l,r).`

The monomials indexed by compatible partial assignments tau:Q->R\{h} are an integral basis of functions on the full legal-assignment set. To see this, evaluate on the all-hub baseline and each assignment in which exactly the labels of a chosen partial tau take their alternative roots. The evaluation matrix is the inclusion zeta matrix on compatible partial assignments, triangular with 1 on the diagonal; integer Möbius inversion supplies its inverse.

For Q empty, its coefficient is nu(empty)+sum_{r!=h}mu_r(empty); zero gives precisely the constant generators. For Q={l}, each alternative r yields nu({l})+mu_r({l})=0, giving the unary generators.

For |Q|>=2, a partial assignment tau to different nonhub roots ("mixed") has coefficient nu(Q), while one sending all labels of Q to root r has coefficient nu(Q)+mu_r(Q). If the sets A_l (l in Q) are not all the same singleton, a mixed assignment exists by independent choice of alternatives. It forces nu(Q)=0; every available monochromatic assignment then forces mu_r(Q)=0. Otherwise every A_l={r}; equivalently Q subset B_r, and one unconstrained integer nu(Q) remains together with mu_r(Q)=-nu(Q). These are exactly the displayed higher generators. The free integral coefficients prove spanning and Z-linear independence. QED.

A genuine nonlinear abstract rooted-cost example uses Q={7,13} when both labels have roots {06,07}: g_07(S)=1[Q intersect S=empty], g_06(S)=-1[Q subset S]. Both components can be nonzero, yet the full cost delta is zero for every assignment because both labels leave 07 exactly when both enter 06. If desired, set baseline costs D^A_r(S)=10+2|S| and D^B_r(S)=D^A_r(S)+g_r(S); both families remain nonnegative and monotone. This construction does not assert a native signed-prefix swap.

## Exact specialization to the frozen BRC domains

EC49FOM's immutable named domains are:
`5:{05,07}; 7:{06,07}; 13:{06,07}; 15:{03,05,07}; 17:{03,06,07}; 19:{03,05,07}; 21:{03,06,07}`.
For h=07, the spokes are B_03=empty, B_05={5}, B_06={7,13}. There are exactly 648 named complete assignments and 16+8+16+128=168 reachable rooted-cost coordinates. The theorem gives kernel rank **3+7+1=11**, including exactly one nonlinear quadratic generator.

An independent exact matrix check constructs all 648 incidence rows (four 1s per row) against the 168 rooted-cost coordinates. GF(2) bitset Gaussian elimination yields rank 157. The eleven displayed integer kernel generators annihilate all 648 rows and have rational rank 11. Consequently the matrix has rank **exactly 157 over Q** and kernel dimension 11, matching the theorem.

## New finite native result: all 1000 same-domain pairs

The existing EC49FOM source archive's exact rooted-cover profile export has **8,744 entries** and SHA256 `e2b9c419fdd2614eeea37de54437dd776ed7024e06ceacce3941aab192b393af` (`EC49FOM_PROFILES.csv`); the 84-edge list has SHA256 `04b8ab0a0b2e51262ac92d40073062a30bc8c0dcd7a0be997cbd89e3aacdbe54` (`EC49FOM_MOBIUS_84.csv`). Underlying frozen signed-prefix raw file SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; original 84-edge input SHA256 `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`.

First, the 84 directed single-key edges contain 82 common-domain edges. **All 32 edges with identical complete-assignment total cost maps also have identical reachable rooted-cost profiles.** The remaining 50 change both observations; across the 82 edges there are 790 changed rooted-cost entries (sum over edges).

Second, partition all 51 saved cache configurations by their four (mandatory-root mask, optional-root mask) pairs. Exactly three domain classes exist:

| Cache configurations | Complete assignments per config | Unordered pairs | Equal terminal cost maps | Distinct terminal signatures |
|---:|---:|---:|---:|---:|
| 45 | 648 | 990 | 360 | 12 |
| 5 | 648 | 10 | 4 | 2 |
| 1 | 1944 | 0 | 0 | 1 |
| **51** | — | **1000** | **364** | **15 across three different domains** |

On each of the **1000** domain-comparable pairs, the complete integer cost-map signatures coincide **if and only if** the entire reachable per-root cost profile signatures coincide. Thus the terminal observer is injective *on the distinct rooted profiles represented by this frozen finite cache family*, despite the algebraically available nontrivial kernel. This does not erase the four **single-assignment** cancellations identified in EC49FOL; that is a different quantifier.

## Reproduction and frontier

Use `VERIFY_EC49FON_KERNEL.py` (pure Python standard library, exact integer arithmetic, GF2 rank and eleven-vector rational elimination) with the **unchanged** input files `EC49FOM_PROFILES.csv` and `EC49FOM_MOBIUS_84.csv` from the EC49FOM evidence archive. It emits a full 1000-pair classification `EC49FON_ALL_PAIRS.csv`, exact `EC49FON_RESULT.json`, and the two successful rank/native assertions. No floating point arithmetic or new native trie computation is used in this continuation.

Next: search a newly justified class of frozen signed-prefix cache changes *outside* the 51 configurations for a nonzero delta lying in the binary-spoke kernel, or derive a signed-prefix-specific structural obstruction. Any result must distinguish abstract set-function realizability from realizability by the exact native rooted prefix-cover cost operator. The algebraic theorem is author-proved; finite inputs checked exactly; independent mathematical review/admission remains **NOT_REVIEWED**.
