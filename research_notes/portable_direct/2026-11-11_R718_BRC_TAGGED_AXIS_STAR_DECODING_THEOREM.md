# R718 — Tagged-axis star-local BRC pair-degree recovery

**Scope/status:** author mathematical proof and finite exact computation; native X6 event correspondence and independent Driver review pending. Parent Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Frozen science is `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` (unchanged). This follows R714–R716's Boolean triple-source ledger. R717's independent X6/S3 holonomy research (Draft PR #2078) is contemporaneous, not a dependency.

## Exact question and carrier

Let `V` be a set of `n>=3` distinct labeled **native axis identities**, `T=binom(V,3)`, and `E=binom(V,2)`. At one typed Cell/time observation, each candidate triple `t∈T` carries a Boolean presence bit `h_t∈{0,1}`. Its exact integer pair ledger is

```
D_{jk}(h) = sum_{t ⊇ {j,k}} h_t.                   (1)
S(a) = {t∈T: a∈t},       |S(a)|=C(n−1,2).         (2)
```

The complete labeled triple identities are the uncompressed BRC source population. Here, unlike the final native physical model, the 20 six-axis Boolean triples are *candidate* source identities; signs, time, Cell/Link/Port, V29 PASS/TRANSFER and V39 `j` are not asserted to have been represented by those 20 bits. P000 still fixes primitive stable nonzero balance as a genuine triadic closure, with the native six-axis geometry/120° relation and independently typed time.

Fix a previously fully verified state `h0`, a later ledger `D1`, and one **known** typed event-axis tag `a`. The conditional *axis-star locality* hypothesis is that `h1_t=h0_t` for every `t` not containing `a`. No upper bound on the number of changed star bits is required.

## Theorem R718.1 (exact unlimited-radius axis-star decoding)

For any finite `n>=3`, if all changed triple memberships lie in `S(a)`, `h1` is uniquely determined by `(h0,D1,a)`, with a **direct decoder**:

```
For each distinct j,k ≠ a:
  ΔD_{jk} = D1_{jk} − D(h0)_{jk}
  h1_{a,j,k} = h0_{a,j,k} + ΔD_{jk};
For every t not containing a: h1_t = h0_t.       (3)
```

**Proof.** In the pair count `D_{jk}` for `j,k ≠ a`, all triples avoiding `a` are unchanged. The only contributing triple that contains `a` is `{a,j,k}`. Subtracting the two pair counts cancels all frozen contributions and yields exactly `h1_{ajk}-h0_{ajk}`. Every possible changed source has a unique unordered pair `{j,k}` disjoint from `a`, so the reconstruction is unique. The restricted pair/triple incidence matrix contains an identity block with `C(n−1,2)` columns and therefore has full column rank. QED.

For X6, a known-axis star contains 10 of the 20 triple identities. The 10 pair-degree coordinates disjoint from `a` reconstruct **all 10** star bits even when all 10 change. This exceeds the 3-change universal recovery radius of R716 by exploiting a typed locality assumption; it does not silently extend that radius to arbitrary updates.

## Theorem R718.2 (necessary and sufficient ledger certificate)

Put `δ_{jk}=D1_{jk}-D0_{jk}` for `j,k ≠ a`, where `D0=D(h0)`. An integer candidate ledger `D1` is realizable by a Boolean update supported on `S(a)` **if and only if**:

```
(B1) For all j,k≠a: h0_{a,j,k}+δ_{jk} ∈ {0,1}.
(B2) For all j≠a:   D1_{a,j}−D0_{a,j}
                         = sum_{k≠a,j} δ_{j,k}.       (4)
```

Proof of necessity: each changed `ajk` contributes the same signed bit increment to pair rows `aj` and `ak`, and only one increment to row `jk`. Proof of sufficiency: build `h1` from equation (3). B1 makes each new bit Boolean; rows disjoint from `a` match by construction and all other rows match by B2. Theorem R718.1 proves uniqueness. QED.

The five X6 equations (B2) are independent extra consistency rows once the 10 identity rows are selected. This is an exact observer-safety certificate for the declared event class and one before/after time interval, not evidence that the native scheduler permits the event.

## Theorem R718.3 (explicit axis-tag loss witness)

On `V={0,1,2,3,4,5}`, let the strings denote unordered candidate triples:

```
H0 = {024,035,124,135}
H1 = {025,034,124,135}   (four changed triples, all contain axis 0)
H2 = {024,035,125,134}   (four changed triples, all contain axis 1).
```

The endpoints are distinct, but every one of their 15 pair counts agrees:

```
D(H1) = D(H2)
      = [0,1,1,1,1,1,1,1,1,0,1,1,1,1,0]
         # lexical pair order 01,02,...,45
```

Indeed `H0△H1={024,025,034,035} ⊆ S(0)`, `H0△H2={124,125,134,135} ⊆ S(1)`. Their equal ledgers follow by direct inspection, or by recognizing their complementary Pasch 4↔4 source trade. Both are at Hamming distance four from the same `H0`. Thus `(H0,D_after,` “one unspecified axis-star update occurred”`)` **does not uniquely recover the source identity**. With a correct tag `a=0` or `a=1`, formula (3) returns the respective unique endpoint. This gives an exact BRC provenance-loss witness for erasing the axis address.

## Theorem R718.4 (complete six-axis support census)

There are six tags and `2^10` possible changed-membership supports per tag, hence `6×1024=6144` tagged possibilities. After deduplicating identical support masks (which may have multiple valid tags), the number of distinct supports is

```
6×2^10 − C(6,2)×2^4 + C(6,3)×2 − C(6,4) + C(6,5) − C(6,6)
= 5934.                                                     (5)
```

This follows by inclusion–exclusion. Two different axis stars intersect in four triple identities, three intersect in one, and the intersection of four or more contains no triple (but still includes the empty update subset). Among the 5934 distinct supports, **5748** have exactly one possible tag, **165** have two, **20** have three and the empty subset has all **six** tags; the weighted total is `5748+2×165+3×20+6=6144`. The proof relies solely on six labeled axes, not on untested physical reachability.

Equations (1)–(4) are covariant under simultaneous axis relabeling `σ∈S6`; every source `t`, tag `a`, pair entry and state is transported by `σ`. This verifies the existing S6 permutation-rotation skeleton. No full native rotation claim is made.

## Computation, reproduction and frontier

The included Python-standard-library verifier `R718_BRC_AXIS_STAR_LEDGER_VERIFY.py` exhausts all **6144** tagged supports, verifies the **5934** distinct-support census/tag multiplicities, tests **49,152** exact tagged transitions on eight fixed baseline masks (each with a full 15-row ledger comparison), checks **720** relabelings of the Pasch witness and rejects an invalid ledger violating (B2). Exact JSON evidence is in `R718_BRC_AXIS_STAR_LEDGER_RESULTS.json`. Actual local execution:

```
R718_BRC_TAGGED_AXIS_STAR_LEDGER_EXACT_PASS supports=5934 cases=49152 S6=720
```

The all-`n` claim rests on the direct algebraic proof; the finite exhaustive computation confirms the stated six-axis implementation.

**Next discriminating native work:** under the unchanged frozen scientific input, extract one exact legal X6 `Cell/Link/Port` event, signed axis/time tag, V29 PASS/TRANSFER result, V39 loop current `j`, and the before/after *lawful* sourced triple membership states. Compute `ΔH`. If all changed memberships contain the event-axis, apply (3), verify (B1)/(B2), and retain signed branch/provenance outside the Boolean observer. If `ΔH` escapes that star, save the exact event as a counterexample to the proposed event-locality hypothesis and characterize the smaller valid class or a richer source residual. If native observers omit the tag, test realizability of the explicit R718.3 collision. Formal ownership, Source semantic checkpoint, review and acceptance remain governed by current native receipts.
