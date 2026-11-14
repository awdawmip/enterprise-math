# R156B — Exhaustive exact alias-fiber bound through length 20

Date: 2026-11-15 Asia/Shanghai. **Exact finite theorem by exhaustive integer enumeration;** any all-length extension is **OPEN**. Independent review: **NOT_REVIEWED**. External scalar tied-phase S23 finite Sturmian observer, fixed scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Finite theorem

For every binary word `w` of every length `1<=m<=20`, compute its genuine Sturmian open slope support `(alpha,beta)`; discard a word exactly when this interval is empty. For each admitted word form the absolute R146 prefix cuts `U,V`. Then each exact observer signature `(alpha,beta,U,V)` has at most **two** distinct word preimages.

At length 20, there are exactly **944 admissible words**, **868 different observer signatures**, and **76 two-word fibers**. Across all 20 lengths, no fiber of size 3 or greater occurs in the exact computation. This is a finite theorem, not a proof of the conjectured universal two-to-one bound.

## Complete verification argument

The program `R156B_check.py` enumerates the integers `n=0,...,2^m-1` for each m; the m-bit binary expansion is a bijection to all length-m binary words. Let `p_j` be prefix sums and `q=p_j-p_i` the ones count in the contiguous factor `w[i:j]` of length `k=j-i`. The exact support is

```text
alpha = max(0, all (q-1)/k),
beta  = min(1, all (q+1)/k).
```

All comparisons use integer cross multiplication, without floating point. If `alpha>=beta` the word is excluded; otherwise reduce `alpha=a/b` and `beta=c/d` using gcd, and compute

```text
U = b + min_j(b*p_j-a*j),
V = max_j(d*p_j-c*j).
```

The dictionary key `(a,b,c,d,U,V)` is exactly the tuple `(alpha,beta,U,V)` in canonical reduced form, so dictionary sizes are the desired mathematical fiber cardinalities. At every length the program checks that no key occurs three or more times and that the valid-word count is consistent with its singleton/two-word partition.

**Independent arithmetic cross-check:** for all 2,046 candidate binary words of lengths 1..10, a separately implemented `fractions.Fraction` algorithm independently computes support, cuts and admissibility and is asserted equal to the integer-only result. This verifies not just the counted collisions but the actual interpretation of every dictionary key in that full lower window. The enumeration itself includes every one of **2,097,150** binary candidates of lengths 1..20, under the exact program and standard Python arbitrary integers.

Selected counts (all outputs are in the JSON record):

| m | Admissible words | Distinct signatures | Two-word fibers | Fiber size >=3 |
|--:|--:|--:|--:|--:|
| 7 | 54 | 50 | 4 | 0 |
| 10 | 136 | 122 | 14 | 0 |
| 14 | 346 | 320 | 26 | 0 |
| 17 | 594 | 546 | 48 | 0 |
| 18 | 696 | 632 | 64 | 0 |
| 19 | 816 | 748 | 68 | 0 |
| 20 | 944 | 868 | 76 | 0 |

Exact checker outcome: `R156B_EXHAUSTIVE_M20_NO_TRIPLE_ALIAS_PASS`. The JSON `R156B_verification.json` contains counts for **each** m=1..20, not just selected rows.

## Relation to R156

R156 establishes a genuinely infinite **two-word non-reversal alias family**, with an exact positive appearance-threshold shift. R156B adds finite evidence that these aliases have at most one companion in the tested length range. The all-length claim

```text
for each m>=1, every fiber of w -> (alpha,beta,U,V) has cardinality <=2
```

remains an **open conjecture**; a length >20 counterexample would be fully compatible with this finite theorem.

## Next scientific questions

1. Seek an injection from each observer fiber into a two-point orientation invariant, or construct a first triple collision at larger m, using Sturmian return-word/Christoffel structure. A direct all-length proof must preserve actual absolute prefix cuts.
2. Use the exact two-sided padding identities of R156 to generate known collision subclasses and isolate any fiber not accounted for by them.
3. Test the full-m global permanent-presence threshold separately; word-fiber multiplicity and last-absence bounds are different questions.

**Source/control:** author-side portable research. Current main lookup of `research_task_records/RS-S23-AV` returned 404; no formal task CLAIM, imported researcher identity or activity checkpoint asserted. R156B is held as a durable research note, not an independently reviewed theorem promotion.
