# EC49FNK — exact native BRC radius-three seven-key cases 28500–30499

**2026-11-13 · author-side finite mathematics.** Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This continues the previous verified interval 27500–28499 (PR #2272). The exact task RS-EC49AS has not been shown by the current native control as an immutable published task; this branch is scientific evidence, not a formal CLAIM/Result or independent Driver acceptance.

## Domain and result

Keep the *original* nine-state BRC, 178,850 original lawful operation words, 94 complete raw cache keys, 24 observation labels, and the full ordered, signed six-axis native microstep prefixes. For each of the 38,169 radius-three seven-key configurations K_i, C(K_i) is the minimum number of **distinct nonempty native prefixes** in a set of original lawful words covering all 24 labels while using only the seven keys in K_i. No endpoint or unsigned-path quotient is used.

We exactly computed every index `28500 <= i <= 30499` using integer rooted-trie / demand-subset dynamic programming. There are **2,000** consecutive configurations, with the following exact finite minimum:

```text
min C(K_i) = 86
argmin = {30266, 30393, 30396}
max C(K_i) = 222 (at 29146)
```

The three minimizing full key-index lists are respectively:

```text
30266: [0,4,5,11,32,34,49]
30393: [0,4,5,11,32,46,49]
30396: [0,4,5,11,32,46,61]
```

Thus the one-key substitutions `34->46` followed by `49->61` preserve the optimum in this three-configuration chain. For each case, a reconstructed set of 24 *lawful original BRC operation words* covers all 24 labels and has exactly **43 + 43 = 86** distinct prefixes under first microsteps 05 and 06. Original frozen-input SHA256 = `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Frozen case listing SHA256 = `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`. Complete 2,000-row native output SHA256 = `119a5f2cd4e62f93f3308b50d3064784e1e14aef1e0a6592feace9666e382fd3`.

## Exact lower-bound method

Group lawful operation words by their first signed native microstep r and build their ordered-prefix tries. At each trie node retain the exact available demand masks and minimum prefix-node cost. Combine disjoint child subtries by OR-convolution of masks, counting a nonroot prefix iff a nonempty selected descendant is used. Superset closure yields exact integer `f_r(S)`, the minimum number of native prefixes needed for requested root-r labels S (incidental label coverage allowed). Every demand is assigned to one legal root; minimize `sum_r f_r(S_r)`. Distinct first-microstep roots have disjoint nonempty prefix sets, so the result is exact for each fixed K_i.

The original C++17 solver produced a `FINISHED` receipt for **one 500-index block and fifteen 100-index blocks**, exactly 2,000 ordered consecutive rows in total. The Python independent prefix-trie optimizer separately agreed on indices 28500=138, 28833=98, 28890=98, 29421=98. The longer independent Python pass was interrupted at 30266, and is not claimed as complete. All three 86-cost configurations were separately rerun by the native exact solver, their root-cost tables emitted and their full 24-word witnesses reconstructed and checked against the frozen 178,850-word catalogue.

## New finite structure: sharp third-root exclusion

For each of the three 86-cost configurations, legal first microstep roots are 05, 06 and 07. Roots 05 and 06 contain the baseline partition L05 and L06 of the 24 labels, 12 each; root 07 may accept precisely eight eligible labels Q. For each T subset Q define

`F_K(T) = f05(L05 \ T) + f06(L06 \ T) + f07(T)`

and `G_K(T) = F_K(T) - 86`. Exhaustive exact integer root-function evaluation over **all 256 T** gives, for *each* of the three configurations,

```text
G_K(empty) = 0
min_{T nonempty} G_K(T) = 8
sharp masks (Q's ascending bit order) = [85,170,255]
```

Therefore the baseline 05/06 allocation is the **unique globally optimal first-root assignment**, and every nonempty third-root assignment costs at least 94. The sharp eight-prefix gap survives both one-key replacements.

A reusable *cardinality envelope* is `a_k=min_|T|=k f07(T)`, `b_k=max_|T|=k [f05(L05)-f05(L05\T)+f06(L06)-f06(L06\T)]`; then `G_K(T)>=a_k-b_k` whenever `|T|=k`. Exact envelopes for k=1,...,8 are:

| case | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 30266 | 9 | 9 | 8 | 6 | 8 | 9 | 9 | 8 |
| 30393 | 9 | 10 | 9 | 8 | 9 | 10 | 9 | 8 |
| 30396 | 9 | 10 | 10 | 8 | 9 | 10 | 10 | 8 |

For 30393 and 30396, the eight separate-envelope inequalities *alone* prove the bound 8. For 30266, they prove it for seven cardinalities, with the 70 subsets of cardinality four checked jointly. All attain the exact bound 8.

The 256 exact gap values are not identical across the three cases. For A vs B, counts in order (A cost greater / equal / B cost greater):

| comparison | A greater | equal | B greater |
| --- | ---: | ---: | ---: |
| 30266 vs 30393 | 16 | 104 | 136 |
| 30266 vs 30396 | 4 | 64 | 188 |
| 30393 vs 30396 | 4 | 152 | 100 |

This explicitly separates identical global optimum, identical strict exclusion margin, and identical sharp masks from identical *internal root-cost functions*.

## Validation and durable frontier

The full evidence bundle preserves the original frozen 9.6 MB input, case listing, original C++17 solver, all 2,000 raw records and sixteen full native completion logs, independent Python source and available outputs, three lawful 24-word signed-native certificates, exact root tables, a 256-mask checker, and a SHA256 manifest. Complete bundle SHA256: `c51caea85cf3813588109c194b70aa6e5b76399e17023913a95bc97f3e8f3ac4`. An additional repository certificate carries the lossless 2,000-cost vector and original lawful witnesses.

The covered contiguous radius-three frontier is now **30500/38169 = 79.9%**, with index **30500** next and 7,669 indices remaining. This finite family attains the earlier 86 record, while the separate unrestricted seven-key mother problem retains a known feasible 84-prefix construction. A further scientific question is whether the stable 8-gap and three sharp masks can be predicted by an exact invariant of the key-substitution's root trie before enumerating all 256 allocations.
