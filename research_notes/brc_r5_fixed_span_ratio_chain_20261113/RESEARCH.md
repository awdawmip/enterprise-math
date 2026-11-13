# R5 — Exact multinomial ratio-chain for fixed-span checkpoint gap decoding

Date: 2026-11-13. Status: author-side mathematical proof and executed local exact computation. Frozen science pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551` (unchanged).

## Precise predecessor and scope

This extends the R5 35-byte fixed-span combinatorial-rank codec in [Draft PR #2239](https://github.com/awdawmip/enterprise-math/pull/2239), commit `f4cf24a363e7795b05a9d27c617ee3c4d2ea7abc`. The original 56-byte center source is [Draft PR #2232](https://github.com/awdawmip/enterprise-math/pull/2232), commit `1353a03177bb2c095495ce0de22d9bdedcc5dddb`. Both exact source strings and their source SHA-256 are included in the portable verifier.

For the frozen R5 center list, there are 213 centers indexed by integers `1,...,952`, and 212 adjacent gaps in `{3,4,5}` with sum 951. Their actual frequency vector is (16,77,119). The 35-byte rank codec requires only the gap count n, sum L, alphabet, and initial center; unlike the 33-byte option, the decoder does not require the exact frequency vector.

## Theorem: consecutive-histogram ratio law

Let n>=0 and L be integers, and consider length-n words over ordered gap alphabet `{3,4,5}` with total sum L. Let a, b, c denote the multiplicities of 3, 4, 5. Then the feasible histograms are precisely

`a_min = max(0,4n-L) <= a <= a_max = min(n,floor((5n-L)/2))`,

`b = 5n-L-2a, c = L-4n+a`,

with integral a, and each histogram class has `M(a)=n!/(a! b! c!)` words.

For consecutive feasible histograms,

`M(a+1) = M(a) * b*(b-1) / ((a+1)*(c+1))`,

where `b>=2` at each nonterminal step and the division is exact in integer arithmetic.

**Proof.** The two equations for n and L give the stated b,c. Their nonnegativity yields exactly the a bounds; no other feasible histogram exists. Increasing a by one maps (a,b,c) to (a+1,b-2,c+1), preserving both constraints. Substituting into the factorial quotient gives the ratio. Both M(a) and M(a+1) are integers by their multinomial interpretation, which proves the exact division.

This constructs the complete histogram-block cardinality sequence using one initial multinomial calculation and one rational-ratio step per subsequent class. The blocks retain the exact order used by PR #2239's 35-byte rank. Consequently the unranking algorithm can identify the correct histogram by subtracting successive M(a) values, and then use the previous exact fixed-count multiset unrank. The rank/payload encoding is unchanged, so all previously stored bytes retain their meaning.

The class size remains `T(n,L)=sum_a M(a)`; the previously proved finite-class capacity bound is not changed. For n=212, L=951, there are exactly 55 feasible histograms, `T=43238460278605276751226501913190848199841244337559724275404587140697800213579145152`, bit length 275, requiring 35 bytes for a fixed-width encoding of the **whole class**.

## Verified exact results

An independent local Python standard-library script `VERIFY_FAST_FIXED_SPAN.py` was run in this turn. It checked the exact 56-byte source SHA-256 `bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326` and exact 35-byte rank SHA-256 `9a1baae24527efdcb30a208330500e3e6e460c738facc4d39ad26451d03328fa`. Decoding the 35-byte rank using both the prior factorial-per-histogram enumerator and the new integer ratio chain produced the identical 213 centers of the 56-byte predecessor; re-ranking these gaps recovered exactly the same numeric 35-byte rank.

All 9,841 ternary words of length 0 through 8 were exhaustively tested for rank/unrank equality with both methods and for equality of the entire feasible-histogram sequence. Two out-of-range ranks were correctly rejected. Both implementations computed identical class cardinality and 275-bit size.

The local CPython benchmark used 17 rounds of 150 full decoding calls each, reporting round medians:

| Exact decoder | Median microseconds |
|---|---:|
| Previous factorial-per-histogram enumeration | 137.328 |
| New integer ratio-chain enumeration | 94.381 |

The local decrease was 31.27%, with the identical persistent 35-byte payload. These timings are implementation- and host-dependent. This is a reduction in fixed-span decoding work; the original 2,520-byte scientific seed, wall-rank construction, checkpoint bitmaps, rational query mapping, and full-query correctness remain unchanged upstream/downstream obligations.

## Source, reproducibility and next frontier

This directory includes `VERIFY_FIXED_SPAN_RATIO_CHAIN.py`, a standalone standard-library reproduction of the ratio theorem, predecessor exact byte checks, short exhaustive tests and timing. `EXACT_OUTPUT.json` records the executed original local implementation's output. The local check was equivalent source logic; the committed portable source needs independent execution on the remote blob after publication.

Next discriminating experiment: rebuild the pinned 953 rational walls and complete event counts E(b), apply the original 35-byte (and 33-byte) center decoders, regenerate all nearest-center indices and bitmaps, and compare 2,747,520 boundary-prefix counts to the frozen original oracle. Then measure *complete cold startup* and peak memory with seed decode and output recovery, distinguishing single-lookup and amortized repeated-lookup applications. Keep R5 owner/CLAIM, mathematical proof checking and formal Result/Driver review under their actual independent authorization.
