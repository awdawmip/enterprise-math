# EC49EXK — H8/M5/S≤6: explicit 80-edge signed-native paired-BRC construction

Research date: 2026-11-03. Parent EC49EXJ `cdb6486c813acd141aba70dd1a6db68e53ae3fcf`, Draft PR #1730. Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 `773d538180bfb49e24cffeb35c3ee75eb0628e2e` and Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Current behavioral inputs separately read from global main `3df0b99cdb0aea8ddd36b487a365fa3972699861` and EM main `eeb6f882aae70ec0a2b37d74ea7b7f988ee1a9c4`. P000 and ACTIVE worldview unchanged.

## Model and resource metrics

The seven operations are ordered signed primitive native-X6 paths: a=(-1,-1), b=(-2,-2), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2), where each integer denotes one *signed native axis index*, not a Euclidean coordinate. At horizons h=2..8 select h-operation words of displacement (2,0,0,0,0,0); within a horizon all words have one identical complete six-axis positive primitive-count key, and their nine seam-history observation rows must span rank 9 over Q. Two independently indexed strictly-positive symbolic BRC channels use factors X_p=product_i x_i^p_i and Y_p=product_i y_i^p_i while preserving complete signed step order/provenance. E counts distinct nonempty ordered *primitive-step prefixes*, M counts distinct full positive BRC keys, S counts distinct nine-history-to-five-bucket transfer signatures.

## Theorem 1: constructive bound for H8/M5/S≤6

The following family has exactly (E,M,S)=(80,5,6):

| h | operation words | full positive six-axis BRC key | cumulative E |
|--:|---|---|--:|
| 2 | ce de ec ed | (3,1,1,0,0,0) | 28 |
| 3 | feg gef | (3,1,1,0,0,0) | 42 |
| 4 | edfg defg gefc fegc | (4,2,1,0,0,0) | 58 |
| 5 | fegfg geffg | (4,2,1,0,0,0) | 64 |
| 6 | fegfff geffff | (6,1,1,0,0,0) | 72 |
| 7 | fegffff gefffff | (7,1,1,0,0,0) | 76 |
| 8 | fegfffff geffffff | (8,1,1,0,0,0) | **80** |

The executed standard-library checker reconstructs all six signed native axis counts, verifies the return vector, exactly computes nine-history transfer matrices by rational row reduction, verifies nine-dimensional rank in all seven horizons, and directly counts the union of signed primitive prefixes. The T4 signatures at h2,h4 are (1836687,1867942,1872656,1873981); other horizons use T2=(1836425,1866380). Together these use exactly 6 distinct signatures. The five keys in the table are pairwise distinct except the explicitly shared h2/h3 and h4/h5 keys.

EC49EXJ proves the four-key/six-signature exact optimum E=90. The five-key witness therefore reduces E by **10**, or 11.11% of 90, at the same H8/S≤6 constraint.

## Theorem 2: exact minimum 80 within a fixed explicit five-key template

Keep h2,h3,h6,h7,h8 words *fixed as above*. At h4 take one word for each of the four T4 signatures and at h5 one for each of the two T2 signatures; both horizons use key (4,2,1,0,0,0). Within this well-defined template the exact minimum is E=80.

**Proof.** The nonempty signed primitive prefix union of the fixed five horizons has exactly 62 edges. Let u,v,w be positive native axis-1,2,3 counts, r=#c+#d, a=#a. Native return requires #b=0,#e=#a+1. The word length and key equations yield r=u+v-h-1, a=w-1, #f=u-r-2w and #g=v-r. For key (4,2,1), h4 has r=1,#f=#g=1, and h5 has r=0,#f=#g=2. Permuting all eligible operation multisets and applying the exact actual nine-history transfer map gives **exactly 12 candidate words in each of the four h4 signature groups and two h5 signature groups**. All choices cover exactly 12^6=2,985,984 possible mandatory one-per-signature word selections.

Associate to each word a Python arbitrary-precision integer bitmask of all ordered signed native primitive-step prefixes *outside* the 62-edge fixed baseline. For any selection the additional cost equals the integer bit_count of the OR of its six masks. The source `VERIFY_EC49EXK.py` enumerates all 12^4=20,736 h4 tuples, constructs all 12^2=144 h5 pairs and evaluates the exact union cost. It prunes an h4 tuple only when its alone-prefix cost is already at least the best joint cost: OR is monotone, so this cannot discard a better solution. Executed counts: 20,555 h4 tuples soundly pruned, 26,064 cross-pair evaluations, exact minimum 18 new edges. The four h4 words `edfg defg gefc fegc` and two h5 words `fegfg geffg` attain it. Hence E=62+18=80 is the exact fixed-template optimum. Adding redundant words cannot lower a union-of-prefix cost, so choosing one word per required signature is sufficient for that template's optimum.

## Global lower-bound improvement and remaining problem

EC49EM proved for all H≥5 the unrestricted-within-h-equal-key bound E≥4H+30, giving E≥62 at H8. At equality E=62, the h8 full-rank fiber must have #c+#d=0 and #a=0, since EC49EM's lower bounds for the other cases are strictly larger. The compulsory 28-edge h2 core and the two required h8 f-first/g-first paths of native length 18 already occupy all 62 edges. Thus every selected h3..h7 word must be an operation-prefix of one of those h8 paths (the native operation codes are prefix-free). Consequently these words also have #a=#c=#d=0. Their horizon-specific full keys satisfy u+v=h+1 and are distinct for h=3,4,5,6,7,8: at least **six** cache keys. Therefore E=62 cannot meet M=5, and the exact global five-key optimum E* is presently bounded by **63≤E*≤80**.

The 80 lower bound applies to the fixed template stated above; the global M5 category remains a live mathematical problem. No physical heartbeat-residual or time-evolution claim is made. No classical pi/trigonometric reference computation was performed.

## Reproduction and status

Run `python VERIFY_EC49EXK.py > EC49EXK_REGENERATED.json` using Python 3.10+ standard library. `EC49EXK_EXECUTED.json` records the actual executed original version's exact counts, resources and per-horizon keys/words; its complete original code is archived in the same folder. Arithmetic is exact integers plus fractions.Fraction rank operations; finite enumeration and monotone mask pruning constitute the proof kernel.

Classification: `AUTHOR_CONSTRUCTIVE_PROOF / EXACT_FINITE_TEMPLATE_OPTIMUM_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. Authenticated GitHub account awdawmip; active Source owner lookup returned `CONTROL_QUOTA`, so native ownership remains unconfirmed and no CLAIM/Result/independent Driver pass is asserted.

Next: EC49EXL investigates alternative h5/h6, h6/h7, h7/h8 key collisions and global five-key schedules, seeking a witness with E<80 or a matching unconditional lower bound.