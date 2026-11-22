# T6: eliminate the two extremal 2^7-defect pairs by odd-prime reciprocal moments

Date: 2026-11-23 (Asia/Taipei). Exact arithmetic extension by RESEARCH_DRIVER **EM-DVR-DEBB5E**, original SID `MCP-9b4714dc46b948afa4875a86c89c713c`. Original prior T6 authors and task ownership are unchanged.

## Statement

Let `A,B` be finite multisets of positive integer exponents with `sum(A),sum(B)<=2331` **separately**, and suppose the **full** moments `H_k(X)=sum_{e in X}(e/(e+1))^k` agree for every `k=0,...,6`. By the [2^8 cancellation proof](https://github.com/awdawmip/enterprise-math/blob/3063e3ecc0e1f96262db7cc409c5015287edcd4a/research_notes/driver/2026-11-23_t6_universal_p2_eighth_six_moments.md) and the [complete 2^7 signature classification](https://github.com/awdawmip/enterprise-math/blob/4d0265969514c35a281165a4262dee20532c69d1/research_notes/driver/2026-11-23_t6_p2_seventh_26_collision_classification.md), exact-valuation-seven multiplicity differences must be zero or one of six difference archetypes, represented by 26 possible unordered profile pairs.

**New theorem.** Two of those 26 apparent pairs are impossible under the original full moment identities. The following two `v2(d)=7` profiles cannot occur as the positive and negative sides (in either orientation):

1. `{1152,1152}` against `{128,2176}`, interpreted here as **denominators** `d=e+1`, not exponents; both use exponent mass `2302`.
2. `{896,1408}` against `{384,1920}`; both use exponent mass `2302`.

Therefore, any genuine full-moment equality has either identical exact-valuation-seven profiles or one of **at most 24 remaining congruence-colliding unordered pairs**, whose signed differences lie among just four prior archetypes with multiplicities `10,7,5,2`. The earlier 2^7 aggregate conservation of layer cardinality and exponent mass continues to hold.

## Proof: first extremal pair, prime 17

For either orientation, at `v2(d)=7` one side contains `d=2176=17*128` once and the other contains none. That layer consumes exponent mass `(1152-1)*2 = (128-1)+(2176-1)=2302` on **each** side. Thus all other exponents on either side have total mass at most `2331-2302=29`, and every such extra denominator `d=e+1` satisfies `d<=30`.

Among denominators `d<=30`, the only multiple of 17 is `d=17` (exponent mass `16`), with multiplicity at most 1 on either side. No denominator divisible by `17^2` is budget-feasible; no additional `17`-multiple outside `17` or `2176` can occur. The full first reciprocal moment equality `S_1(A)=S_1(B)`, which follows from `H_0,H_1`, multiplied by 17 and reduced modulo 17, gives, after choosing orientation where the difference at `d=2176` is `-1`,

`delta_m(17) - (128)^(-1) = 0 (mod 17)`.

Since `128 ≡ 9 (mod 17)` and `9^(-1) ≡ 2 (mod 17)`, we require `delta_m(17) ≡ 2 (mod 17)`. But `delta_m(17)∈{-1,0,1}`; contradiction.

## Proof: second extremal pair, prime 11

The only exact-valuation-seven denominator divisible by 11 in this pair is `1408=11*128`; take its signed multiplicity difference to be `+1`. Again each side consumes exponent mass `2302`, leaving at most `29` for every other exponent. Among `d<=30`, the only denominators divisible by 11 are `d=11` (exponent mass 10) and `d=22` (exponent mass 21), so let `a=delta_m(11)` and `b=delta_m(22)`. We have `|b|<=1`, and no `11^2` denominator is possible.

Use the full first two reciprocal moment identities `S_1(A)=S_1(B)` and `S_2(A)=S_2(B)` (from `H_0,H_1,H_2`); multiply the `k`th identity by `11^k` and reduce modulo 11. The only surviving denominators have one factor 11, giving

`a + b*2^(-k) + (128)^(-k) == 0 (mod 11)`, `k=1,2`.

In `F_11`, `2^(-1)=6` and `128^(-1)=7^(-1)=8`, whence

`a+6b≡3 (mod 11)`, `a+3b≡2 (mod 11)`.

Subtracting gives `3b≡1 (mod 11)`, hence `b≡4 (mod 11)`, which contradicts `b∈{-1,0,1}`. Reversing sides merely negates both congruence equations and yields the same impossibility.

## Scope and next test

This second lemma is a **full rational-moment necessary-condition improvement** beyond the six-moment 2-adic signature table; it does not assert that any of the other 24 candidates is attainable. The elimination uses the actual separate exponent-mass budget to bound all external denominators, and directly retains the distinct composite cofactor directions. For the remaining four archetypes, test odd-prime residue constraints against each pair's actual leftover budget, without replacing the full rational observations by isolated prime components.

Increment this Driver's completed **mathematical subunits by one** for this new proof. New Native Review admitted 0; Result admitted 0; formal Task complete 0; mother T6 objective complete 0. Source/Activity semantic linkage remains a separately authorized operation.
