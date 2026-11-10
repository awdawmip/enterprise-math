# BRC-X6 / D8 exact-two-missing-action fibers: finite quadratic connectivity

**2026-11-10** · **AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. Author-only portable evidence; no native TASK_RESEARCH CLAIM, Result, Driver review or scientific admission is asserted.

**Immutable scientific source:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native four signed source ports `(6,7,28,29)`, signs `(+,-,-,+)`, six *labelled* actions per source, 38 legal lexicographically ordered deterministic policies, nine original frozen roots. The original signed joint-flow condition is verified in the companion executable artifact; `C` below is a faithful 24×38 incidence readout of those original legal policies, not a replacement for admissibility.

## Finite theorem

Let `C∈{0,1}^{24×38}` contain exactly one occupied action row per source in each legal policy column. For **every** nonnegative integer 24-vector `b` with all four six-coordinate source blocks summing to **8**, with `b∈col_Q(C)`, and with **exactly two zero action coordinates**, the integer fiber

`F_8(b)={n∈Z_{≥0}^{38}: Cn=b, sum_j n_j=8}`

is **nonempty and connected** under exact 2-for-2 legal policy exchanges `e_i+e_j ↔ e_k+e_l` satisfying `C_i+C_j=C_k+C_l`.

There are **20,252** distinct target vectors `b` and **5,487,816** eight-policy multiset representations in this complete two-zero domain. Same-source missing pairs: **216 target fibers, 16,800 multisets**. Different-source missing pairs: **20,036 target fibers, 5,471,016 multisets**. Exactly **66 of 276** unordered zero-label pairs admit rational-span degree-eight targets (12 same-source, 54 cross-source).

Together with the previously independently preserved degree-eight all-positive and exactly-one-zero theorems at `0e6c727d8080cf4d7c315be88b52a386167c2ae0` and `fbf2c9f5c3e3408c4d324e7add7dc632c77ce7b4`, this proves degree-eight nonempty quadratic connectivity for **all 23,521** rational-span integer targets with **at least 22 of 24 action coordinates positive**, represented by **6,747,364** policy multisets.

## Exhaustive proof and independent arithmetic checks

1. **Complete state enumeration.** Enumerate weakly increasing eight-tuples of the 38 original policies. At each partial state with `r` picks remaining and `m_s` unseen action labels in source `s`, prune only if `sum_s max(m_s-r,0)>2`. Every completion must leave at least this many zero coordinates, so no eligible two-zero tuple is pruned. Exactly **89,090,191 recursion nodes** visited, **65,825,942** pruned, **5,487,816** two-zero states retained; support patterns are disjoint.
2. **Full exact quadratic graph.** All **741** unordered legal policy pairs fall into **605** pair-incidence classes. For every retained tuple, replace every possible two-position pair by every distinct policy pair in its class; check the resulting tuple is retained. Per zero-label pattern, DSU on combinatorial ranks performs **70,252,832 directed exchange occurrences**, **5,467,564 successful unions**, and yields **20,252 components**. Grouping by all 24 exact action counts finds precisely 20,252 targets with **zero split fibers**.
3. **Independent span census.** Exact rational elimination of the 24×38 matrix yields `rank_Q(C)=13` and 11 exact left-nullspace relations. For each of the 276 pairs of absent labels, enumerate all positive integer compositions of 8 among the other 4, 5 or 6 labels of each source (35, 35 and 21 options respectively). A 2+2 integer signature meet-in-the-middle over the 11 relations finds exactly **20,252 rational-span targets**, broken down as above, without constructing any multiset or graph. Because every rational-span target appears in the exhaustive multiset census, existence follows.
4. **Independent support population.** On all `2^24` label masks `T`, compute `k(T)`, the number of legal deterministic policy supports contained in `T`. Integer zeta/Möbius inversion of `binom(k(T)+7,8)` counts the multiset population with exactly each occupied label set. Exactly-two-zero gives **5,487,816** (16,800 / 5,471,016). The same independent executable recovers predecessor populations **465,292** and **794,256** for zero and one missing label.
5. **Frozen observer provenance.** Independently reconstruct all 38 policies by testing the full signed joint flow on 96 original ports at each of nine frozen roots, preserving action labels and source signs. All nine-root checks pass, and the resulting lexicographic policy table matches the enumeration input.

Exact local reproducible 12-file companion bundle:
`BRC_X6_NATIVE_D8_EXACT_TWOZERO_QUADRATIC_AUTHOR_PORTABLE_20261110.zip` SHA-256 `966a55466485b76d4232ce3bd24141ba84e74e612b9999f11f0f8cf36e37a7a6`.
It contains two standalone C++ checkers, independent SymPy span checker, original frozen kernel and native-flow provenance checker, exact logs, detailed theorem, README and per-file SHA-256 manifest. Source outputs include `CERTIFICATE_STATUS=PASS_DEGREE8_EXACT_TWO_ZERO_FIBER_CONNECTIVITY`. The bundle is **local delivery, not native Source publication**.

**Next scientific unit:** exactly-three-zero degree-eight support strata, or proof of a stronger uniform Markov-basis theorem. The original D25/LIFT/JT2 frozen science, legitimate CLAIM owner and UR V2 94,687-byte/sha256 original-provenance recovery remain unaffected. This author evidence has not been submitted as an original native Task checkpoint or Result.
