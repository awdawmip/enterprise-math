# R762EH — Exact finite integral null-lattice quotient at q=9 and q=27

Date: 2026-11-18 (Asia/Shanghai). Same frozen positive six-branch BRC terminal model and researcher lineage as R762EG. Mathematical status: exact finite integer/modular computation; independent review NOT_REVIEWED.

## Result

With R=Z[(Z/q)^3], P=1+X+Z+XY+YZ+XYZ, K=ker_Z(m_P), and I=K_A R+K_B R+K_C R+K_D R for the four integer annihilators of R762EF, the following finite groups are determined exactly (conditionally on the earlier R762ED rational-kernel dimension identity):

| q | rank(K) | unit Smith factors of I->R | Smith factors divisible by 3 but not 9 | quotient K/I |
|---|---:|---:|---:|---|
| 3 | 12 | 8 | 4 | (Z/3)^4 |
| 9 | 60 | 32 | 28 | **(Z/3)^28** |
| 27 | 204 | 104 | 100 | **(Z/3)^100** |

The new q=9,27 computations strengthen R762EG's all-q exact 3-rank theorem by determining the entire finite group in these instances. The pattern suggests the all-q hypothesis K/I congruent to (Z/3)^(4q-8); a proof for q>=81 remains open.

## Exact computational certificate and reduction

Each integer generator has the form K_J=T(U_J)D(V_J), where T(U) has coefficients with period 3 and D(V) is a full cyclic sum. Therefore K_J is invariant under U_J^3 and V_J. Those independent periods generate a subgroup H'_J of size q^2/3, and exactly 3q distinct translates per family suffice to generate I as a Z-lattice. This reduces the exhaustive integer generating matrix from q^3 x (4q^3) to q^3 x (12q), without losing any generator.

The companion standard-Python verifier explicitly constructs these 12q columns, reduces them modulo 9, extracts unit pivots over Z/9, and then extracts independent 3-divisible residuals by division by 3 followed by F3 elimination. All operations are exact and finite. In Smith normal form of the integer image, a diagonal factor prime to 3 contributes a free order-9 direction mod9; one with exact 3-valuation 1 contributes an order-3 direction; one divisible by 9 contributes nothing mod9. The algorithm computes these first two counts, independent of primes other than 3.

At q=3,9,27 the counts add up exactly to rank(K)=8q-12, supplied by R762ED. Since I has full rational rank in K from R762EF, there are no remaining nonzero Smith factors divisible by 9. Moreover q^4(K/I)=0 from R762EF rules out prime-to-3 torsion. Thus the exact finite quotients are elementary 3-groups with 4q-8 cyclic factors, as stated.

This uses exact modular row and column elimination in the indicated finite matrices; it does not rely on approximate eigenvalues. A separate exact HNF/SNF at q=3 in R762EG agrees. The verifier outputs JSON evidence for q=3,9,27.

## Domain boundary and next work

These classifications are **finite q=3,9,27 results**; the all-q statement currently established is the exact 3-rank 4q-8 from R762EG, not the all-q exponent-3 conclusion. A symbolic integrality argument for 3K subset I would resolve the conjectured universal elementary structure. A potential approach is a uniform integer decomposition of the four coset-fiber modules, distinguishing their triple-root patterns and shared character intersections.

The result concerns only the positive six-branch BRC terminal observer. It neither alters frozen P000 nor assigns a signed Cell/Link/Port TRIADIC_CLOSURE_E licence or future-safe native quotient.
