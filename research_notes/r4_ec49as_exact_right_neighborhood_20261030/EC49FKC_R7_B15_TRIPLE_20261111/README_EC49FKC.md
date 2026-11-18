# EC49FKC — 801 additional exact triple-label B=15 retained-key radius-seven optima (2026-11-11)

**Status:** AUTHOR_FINITE_EXACT / TWO_EXECUTED_ALGORITHMS_PASS / DRAFT / INDEPENDENT_DRIVER_REVIEW_PENDING.  
**Frozen pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.  
**Immediate precursor:** EC49FKB double-H9 exact pair certificate (3524 seven-path contexts), same PR and frozen BRC/X6 model.

## Finite theorem and proof

For each original 94-native-prefix, seven-complete-cache-key witness A or B, choose seven of 24 labeled paths to replace, keep the other 17 original operation words, and let `F(Q)` be the distinct literal signed, ordered native-X6 prefixes of those fixed words. In the retained-key `|F(Q)|=78` class the hypothetical 93-prefix bound allows only `B=15` new prefixes.

The 4336 retained-key B15 choices in each profile partition into 67 exact background classes. For thirteen distinct classes (five for A, eight for B), `EXACT_TRIPLE_CERTS_EC49FKC.json` specifies three observation labels `S` that are omitted by **every** Q belonging to that class.

For a fixed class, let `D_F(w)=P(w)\\F`, where `P(w)` retains all ordered/signed native-X6 prefixes and `k(w)` retains all three integer components of the raw complete cache key. The 17 fixed words already require seven exact keys. Enumerate all frozen legal words `w` (178850 total), restrict to the seven keys, the three labels and `|D_F(w)|<=15`. Beginning with `{empty set}`, for each label of `S` replace the state family by all distinct set unions `U union D_F(w)` having cardinality at most 15.

The final family is empty for each of the thirteen certified classes. This is a complete finite proof of the triple-label lower bound: every legal completion would have to realize those three labels, yet no such completion can use <=15 new literal prefixes. The original witness supplies a 94-prefix upper bound. Therefore every Q in these classes has **exact minimum 94**.

| Verified new triple-only class | A | B |
| --- | ---: | ---: |
| Backgrounds with three-label obstruction | 5 | 8 |
| Labeled seven-path contexts covered | 303 | 498 |
| Exact total cost for each | 94 | 94 |
| **Additional distinct contexts** | **303** | **498** |

The thirteen groups are disjoint from each other and from EC49FKB's two-label class (which has its own unique 1762-context background per profile). Hence EC49FKB + EC49FKC jointly prove **4325** exact 94-prefix local contexts: **2065 A + 2260 B**. The remaining retained-key B15 set is **2271 A + 2076 B = 4347** contexts, potentially addressable by four-label or full seven-label optimization.

## Actual executable evidence

The author-side antichain verifier `EC49FKB_R7_B15_ARITY3.py` was executed against the frozen generator and original FGJ witnesses; it enumerated all 346104 possible seven-position subsets per profile and exactly checked pair/triple obstructions. It returned `A: pair 1762, triple 303, unresolved 2271` and `B: pair 1762, triple 498, unresolved 2076` (elapsed 32.91 seconds on the observed local run). This separates the new 801 triple-certified positions from the existing 3524 pair-certified ones.

`VERIFY_EC49FKC.py` is the **separately executed, duplicate-only direct set-union checker**, with independent signed-prefix and raw-key parsing rather than the first verifier's antichain domination. It reconstructed each of the 67 backgrounds, all thirteen saved group indices and three-label omissions; every final <=15-prefix union family was empty. Actual executed sentinel:

```text
EC49FKC_DIRECT_801_PASS {'A': 303, 'B': 498}
```

The checker and compact thirteen-certificate JSON are directly in this directory. From this directory run `python VERIFY_EC49FKC.py`. It reads frozen `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` already preserved under the sibling `EC49FJD_RELEASE_B11_COMPLETE_20261111/` folder in the same PR. Python 3.10+ standard library suffices. The optional `EC49FKB_INPUT_DIR` can point to that exact directory in another checkout. All count arithmetic and set tests are exact integers/finite sets. The 13-group certificate JSON is complete and executable, not merely a proof outline.

**Next discriminating unit:** inspect the remaining 54/10/65-context B15 classes where no pair/triple bound was found. Compute exact four-label native prefix-union obstructions or full seven-label trie minima. Keep released-key R7 positions and unrestricted global 93-prefix search as separate questions.

**Authority:** independent author result on the existing Draft PR. The native EC49AS task query returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`; this record grants no CLAIM, formal Result, independent Driver acceptance, P000 or ACTIVE changes.
