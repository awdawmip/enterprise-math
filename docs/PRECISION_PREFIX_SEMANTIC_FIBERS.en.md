# Exact Literal-Word Fibers under Prefix Semantic Quotients

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

Class counts tell how many semantic states remain after quotienting literal words. They do not tell how much literal syntax each semantic class absorbs.

For the terminal/discovery/timing ladder, those quotient fibers can be computed exactly. The result shows that semantic redundancy is highly nonuniform at the full-timing level.

## 1. Fixed setup

Take k generator labels and exact literal word length H.

Suppose a word uses exactly s distinct generators.

The semantic ladder is

`literal word -> full timing RLE -> discovery order -> terminal set`.

We ask for the cardinality of each fiber at every quotient layer.

## 2. Terminal-set fiber

Fix one particular s-element terminal generator set S.

Literal words in this fiber are exactly length-H words over S in which every symbol appears at least once: surjections from H labelled positions onto s generator labels.

Their number is

`F_terminal(H,s)=s! * S(H,s)`

where `S(H,s)` is a Stirling number of the second kind.

The `s!` assigns the s partition blocks to the s actual generator labels.

## 3. Discovery-order fiber

Now fix one ordered first-appearance list

`(g_1,...,g_s)`.

The literal positions belonging to each generator form a partition of the H positions into s nonempty blocks. Ordering blocks by their least position fixes the generator labels uniquely according to `(g_1,...,g_s)`.

Therefore

`F_discovery(H,s)=S(H,s)`.

This is the standard restricted-growth-string correspondence with set partitions.

## 4. Terminal fiber is factorially larger than discovery fiber

For one terminal set, all `s!` possible first-appearance orders are forgotten.

Hence

`F_terminal(H,s)=s! * F_discovery(H,s)`.

The executable layer verifies the identity together with literal-word grouping on exhaustive bounded instances.

## 5. Full-timing fiber depends on the duration vector

Fix one exact RLE semantic form

`((g_1,r_1),...,(g_s,r_s))`

with all `r_i>=1` and `sum r_i=H`.

In phase i:

- the first action must be the newly introduced generator `g_i`;
- each of the remaining `r_i-1` positions may use **any** of the i generators already discovered, without changing the prefix state.

Therefore the exact number of literal words in this one timing fiber is

`F_timing(r_1,...,r_s)=product_(i=1)^s i^(r_i-1)`.

This fiber formula is verified directly by grouping literal words by their exact RLE normal form.

## 6. Timing fibers are highly nonuniform

For fixed H and s, distribute the `H-s` extra stutter positions among the s phases.

### Minimum fiber

Put every extra stutter in phase1.

Since phase1 has only one already-seen generator:

`F_min=1`.

There are timing classes that correspond to exactly one literal word.

### Maximum fiber

Put every extra stutter in phase s.

All s generators are already available there, giving

`F_max=s^(H-s)`.

Thus timing fibers at the same H and s can differ by an exponential factor in the number of stutter positions.

## 7. Timing fibers sum to the discovery fiber

Fix one discovery order with s generators. Full-timing classes under it correspond to positive compositions

`r_1+...+r_s=H`.

Summing their literal fibers gives

`sum_(r_i>=1, sum H) product_i i^(r_i-1) = S(H,s)`.

This exactly recovers the discovery-order fiber.

The branch verifies the identity over a broad bounded H/s range.

## 8. Discovery fibers sum to the terminal fiber

There are `s!` discovery orders on one fixed s-element terminal set, all with the same fiber size `S(H,s)`.

Therefore their total is

`s! S(H,s)`,

recovering the terminal quotient fiber.

## 9. Terminal fibers reconstruct all literal words

Choose the s-element terminal set in `C(k,s)` ways. Summing over s gives

`sum_s C(k,s) s! S(H,s)=k^H`.

This is the standard decomposition of all k-ary length-H words by the number of distinct symbols used.

The executable compiler reconstructs `k^H` independently through both terminal and discovery fibers.

## 10. Discovery fibers reconstruct all literal words

Choose an ordered s-tuple of distinct generator identities in

`P(k,s)=k!/(k-s)!`

ways. Each order has `S(H,s)` literal words.

Thus

`sum_s P(k,s) S(H,s)=k^H`.

The two reconstructions provide independent checks on the quotient hierarchy.

## 11. Semantic class count is not enough for cache savings

Suppose a literal cache is deduplicated by full prefix timing.

The number of semantic entries is one resource, but the amount of syntax collapsed into each entry depends on its duration pattern.

A class with early long stuttering may have tiny fiber, while a class whose stutters occur after many generators are visible can absorb up to `s^(H-s)` literal words.

Therefore average compression ratios can hide substantial heterogeneity.

## 12. Uniform literal-word distribution induces nonuniform semantic probabilities

If all `k^H` literal words are equally likely, a semantic class has probability proportional to its fiber size.

At terminal and discovery levels, classes are uniform within a fixed s stratum because their fiber sizes depend only on s.

At full timing level, classes with the same s are **not** equiprobable: the duration vector controls fiber size.

This matters for expected cache hit rates, entropy coding and workload-aware representation optimization.

No average-case optimization theorem is claimed here; the exact fibers supply the necessary input distribution.

## 13. Precision interpretation

Moving down the quotient ladder removes different semantic distinctions:

- timing -> discovery forgets duration placement;
- discovery -> terminal forgets first-appearance order;
- terminal -> literal inversion would additionally require recovering all repeated-action provenance.

The fiber formulas measure exactly how much literal syntax becomes semantically indistinguishable at each layer.

## 14. Stage131 consequence

A representation-resource analysis can now distinguish:

- number of semantic cache entries;
- maximum fiber / best-case dedup;
- minimum fiber / worst-case dedup;
- workload-weighted fiber distribution;
- decoder cost from semantic entry to required outputs.

“Semantic class count” alone is therefore not a complete storage/compression descriptor.

## Owner-local assets

- `src/enterprise_math/prefix_semantic_fiber_decomposition.py`;
- `tests/test_prefix_semantic_fiber_decomposition.py`;
- this bilingual theorem note.

## Prior art / status

Stirling numbers, surjections, restricted-growth strings and positive compositions are standard prior combinatorics. P023/A2 retains future-signature/precision ownership. This Draft owns only the exact semantic-fiber accounting specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
