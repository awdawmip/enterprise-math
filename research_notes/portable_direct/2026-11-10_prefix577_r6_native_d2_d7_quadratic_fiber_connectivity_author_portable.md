# BRC-X6: degree 2–7 原生二策略交换纤维全连通（精确有限定理）

2026-11-10 · Frozen scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` · **AUTHOR_PROVED / EXACT_FINITE_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**.

## Native model and result

Reuse the exact 38 lawful deterministic strategies from the frozen nine-root, 81 signed joint-flow conservation model: 96 original action ports, four signed source ports (6,7,28,29) with signs (+,-,-,+), six distinct labeled actions each. Their original-native codes and the associated 24×38 action-incidence matrix `C` are specified in the predecessor [full integer quadratic exchange theorem](https://github.com/awdawmip/enterprise-math/blob/56c9f5207f63a19a8d11ce045f135eae6b47e7a9/research_notes/portable_direct/2026-11-10_prefix577_r6_native_quadratic_exchange_full_Z_kernel_author_portable.md). That earlier result provides the exact 38-column native generation and pair-collision classification; we do not recount its original mathematical discovery.

**Theorem (every degree-2 through degree-7 native fiber is quadratically connected).** For any integer `2 ≤ d ≤ 7` and any `b∈Z^{24}` with nonempty fiber

```
F_d(b) = { n∈Z_{≥0}^{38} : Cn=b and Σ_j n_j=d },
```

the graph on `F_d(b)` with edges `n → n-e_i-e_j+e_k+e_l` for nonnegative legal replacements satisfying `C_i+C_j=C_k+C_l` is **connected**. Repeated indices are permitted. Every intermediate vertex is a nonnegative integer representation of exactly the same original 24 labeled probabilities, and inherits all original signed joint-flow invariants of the legal columns.

## Fully exhaustive exact certificate

The 741 unordered policy pairs form exactly 605 distinct action-sum classes: 472 singletons, 130 doubletons, three tripletons. For each nontrivial class, anchor its first lexicographic pair to every other pair, yielding precisely 136 exchange generators. Every legal two-for-two switch is connected to the anchor within the same fixed complement.

For every d, enumerate **all** `binom(38+d-1,d)` nondecreasing policy multisets. Independently enumerate every degree-(d−2) complement and every one of the 136 anchored exact pair exchanges. Map both exchanged d-multisets bijectively into the integers `0,...,binom(38+d-1,d)-1` by the exact colex rank

```
rank(a_0,...,a_{d-1}) = Σ_{i=0}^{d-1} binom(a_i+i,i+1).
```

Union the corresponding vertices with an integer disjoint-set union (DSU). Then enumerate all d-multisets a second time and compute their full 24-coordinate native action-count signatures, using four separate six-action count rows. All counts are at most seven and are packed exactly in three bits per action. Check the single-root property for every distinct signature (not merely one example).

| d | All multisets | Exact exchange edges | Successful DSU merges | Distinct conserved fibers | Vertices with a mismatched DSU root |
|---:|---:|---:|---:|---:|---:|
| 2 | 741 | 136 | 136 | 605 | 0 |
| 3 | 9,880 | 5,168 | 4,208 | 5,672 | 0 |
| 4 | 101,270 | 100,776 | 64,086 | 37,184 | 0 |
| 5 | 850,668 | 1,343,680 | 662,356 | 188,312 | 0 |
| 6 | 6,096,454 | 13,772,720 | 5,311,918 | 784,536 | 0 |
| 7 | 38,320,568 | 115,690,848 | 35,515,648 | 2,804,920 | 0 |

At every d, `all multisets − successful unions = distinct conserved fibers`. Every edge preserves its conserved signature, hence connected components cannot cross fibers. The equality and the exhaustive zero-root-mismatch test jointly establish exactly one component per fiber. The C++20 checker uses integer arithmetic only; every result above was obtained by running it from d=2 through d=7. An algorithmically separate Python exhaustive per-fiber BFS verified degrees 3 and 4 (all 2,842/26,234 nonsingleton fibers respectively), with no disconnected fiber.

## Useful consequence, scope and next unit

For a fixed legal six-strategy perfect cover `J=(1,...,1)` and a native residual `r=b-J` admitting a degree-`d≤7` exact policy representation, **all decompositions containing that fixed six-cover** and differing only in their residual policy multiset are connected through legal nonnegative quadratic moves that keep the cover unchanged; these are total-degree 6+d≤13 anchored fibers.

This bounded theorem advances the previous integer-kernel-basis result to actual nonnegative connectivity, and is not an all-degree Markov-basis assertion. For the open D16 uniform `minSupport≤12` target, the remaining step is the degree-10 residual/full 38-policy support question. An executable next finite discrimination is to inspect degree 8 for a first connectivity obstruction or establish a structural induction while retaining all native observer coordinates.

## Reproducibility and status

The conversation-local 14-file ZIP `BRC_X6_DEGREE2_TO7_QUADRATIC_FIBER_CONNECTIVITY_20261110.zip`, SHA-256 `6138bb4bd1085334405d6ef67041a12503db8c7870cbebf377212dd4071b5abc`, contains the C++20 complete enumerator, independent Python BFS, all degree 2–7 integer logs, JSON certificate, theorem and manifest. That ZIP is a conversation attachment; this GitHub Markdown is the persistently published author-side result. The actual original UR V2 94,687-byte four-file bundle and native D25 claim/writer/provenance remain separate debts. No authenticated native Source claim, Result, review or mathematical admission is asserted.
