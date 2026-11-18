# EC49FGN — exact joint H7/H8 prefix-coherent lower bound

Date: 2026-11-10. Status: **AUTHOR_EXACT_FINITE_CERTIFICATE / LOCAL_EXECUTED / NOT_INDEPENDENTLY_REVIEWED**.

Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The literal nine-state BRC observer and signed native-X6 operation expansion are in `../EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, immutable Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. The two independently checked 24-path witnesses A and B are in `../EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json`. The prior fixed-20 H8-only result is EC49FGM.

## Theorem (joint H7/H8 with prefix coherence)

Take either profile `A` or `B` from EC49FGJ and hold its **16 words outside H7 and H8** fixed, together with their ordered signed-X6 microsteps. The union of their nonempty native microstep prefixes is a set `F` with exactly 78 elements.

For each signature `s in {1,2,4,8}`, choose a legal H7 operation word `u_s` and legal H8 word `v_s` such that (i) both yield signature `s` under the original nine-state BRC observer, (ii) both end at displacement `(2,0,0,0,0,0)`, and (iii) **`u_s = v_s[:7]`** (prefix-coherent extension by exactly one original operation). Allow **any number of complete raw cache keys**. Then the minimum number of distinct nonempty ordered signed-X6 microstep prefixes among all 24 words is exactly

```
               min C_native = 94  (profile A and profile B).
```

The original EC49FGJ A/B witnesses attain 94 using seven raw keys and satisfy all four prefix-coherence relations. This theorem optimizes the eight H7/H8 words **jointly**, unlike EC49FGM's H8-only replacement with 20 fixed words.

## Exact exhaustive argument

Write the complete raw cache key of an H8 path as `(x,y,z)`. Since the original operations have positive-axis multiplicities at most 2 for axis 1, at most 1 for axes 2 and 3, all legal length-8 keys satisfy `0<=x<=16`, `0<=y<=8`, `1<=z<=8`. Native endpoint `(2,0,0,0,0,0)` forces the operation multiplicities

```
       a=z-1;  c+d=x+y-9;  f=9-y-2z;  g=9-x.
```

Loop over this entire bounded key box, each nonnegative split of `c+d`, and each order of the resulting multiset accepted by the frozen nine-state BRC transition table. The 125,680 legal H8 words split by required signature as `{1:28063,2:34777,4:28063,8:34777}` and use 50 raw keys. The H7 prefix is legal at the required endpoint exactly when the appended final original operation has zero net displacement, i.e. it lies in `{c,d,f,g}`; retain only those candidates whose first seven operations also have the same signature `s`. The coherent candidate counts are `{1:17172,2:20418,4:17172,8:20418}`.

For each coherent H8 word `v`, let `D_F(v) = Prefixes_X6(v) \\ F` (set difference), retaining the **entire ordered signed** microstep prefix. A 93-edge counterexample would use at most 15 new edges beyond the fixed 78. Thus it suffices to retain only `|D_F(v)|<=15`; this discards no 93-edge solution. Encode these exact finite sets as arbitrary-precision integer masks, which is an exact one-to-one encoding of the relevant signed paths.

Build the family `L` of all distinct unions `D(v_1) union D(v_2)` of cost <=15, and `R` of unions `D(v_4) union D(v_8)` of cost <=15. For each profile, the minimum size of a mask in `L` and `R` is 8. Consequently, a 93-edge solution could exist only when a mask in `L` and a mask in `R` **share at least one exact microstep prefix**: disjoint masks already cost at least 16. Inverted-index enumeration checks **every overlapping pair** by exact bitwise union. Every union has size >15. This proves the lower bound of 94 without assuming any cap on raw keys.

| Exhaustive count | Profile A | Profile B |
|---|---:|---:|
| Fixed prefix edges | 78 | 78 |
| Retained masks for 1,2,4,8 | 427 / 604 / 427 / 604 | 428 / 604 / 426 / 603 |
| Distinct candidate microstep prefixes indexed | 8,180 | 8,177 |
| `L` masks, `R` masks | 3,578 / 3,332 | 3,484 / 3,445 |
| Cross pairs with nonempty overlap checked | 47,552 | 48,448 |
| Feasible four-signature unions costing <=15 | **0** | **0** |
| Verified 24-word seven-key upper witness | **94** | **94** |

The filter is complete for **this exact prefix-coherent subproblem**. An H7/H8 joint improvement with these same 16 background words must change at least one H7/H8 same-signature prefix relation. Alternatively, another route can modify background words; both are available for subsequent research.

## Reproduction and evidence

Run `python3 VERIFY_EC49FGN.py > EXACT_REPORT_EC49FGN.json` from an accessible checkout of this PR branch. The checker imports the immutable frozen BRC model, reads the exact prior witness file, exhaustively generates length-eight accepted words, and computes signed-six-axis prefix unions using only Python standard-library integers. It asserts the complete H8 candidate count, key count, retained pair minima, two independent 94-edge witnesses, and absence of a <=93 completion.

The attached `EXACT_REPORT_EC49FGN.json` records the actual local execution results. The auxiliary local full standalone checker and stdout are preserved separately as an execution evidence bundle. This is an author-side finite computational proof; independent Driver review and formal Result admission remain separate.

### Scientific continuation

Test a **single non-coherent H7/H8 signature** while keeping the other three signatures prefix-coherent and the same 16-word background. Preserve raw-key <=7 as a separate filter. If no <=93 completion is found, expand to two non-coherent signatures; otherwise extract a complete 24-word signed-X6 path certificate and independently validate the original observer and exact cache-key count. The original seven-key global question `C_min(7) ?= 94` remains open.
