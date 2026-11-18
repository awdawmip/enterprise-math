# EC49FFK — H9 exact BRC signed-prefix classification and a wider constructive key family
Date: 2026-11-09. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Scope: **one observation window H9, one complete BRC key, four distinct low signatures 1,2,4,8**, with four original six-operation words and their ordered **signed native X6** microstep expansions. Parent target remains <=5 complete BRC keys and <=93 distinct nonempty native signed-prefix edges.

## Exact finite theorem: H9 costs 52 edges

The frozen original kernel and nine-state observer are in sibling [EC49FFJ/BRC_ORIGINAL_MODEL_EC49FFJ.py](../EC49FFJ_NATIVE_PREFIX_TRIE_20261109/BRC_ORIGINAL_MODEL_EC49FFJ.py); the exact 16-mask directed trie solver and its recurrence/proof are in [EC49FFJ/VERIFY_EC49FFJ_TRIE.py](../EC49FFJ_NATIVE_PREFIX_TRIE_20261109/VERIFY_EC49FFJ_TRIE.py) and its README. For h=9 and K=(x,y,z), word counts are
`#a=z-1, #e=z, #c+#d=x+y-10, #f=10-y-2z, #g=10-x`,
all >=0. Exhaust this finite integer domain: 36 keys with z=1, 21 with z=2, 10 with z=3 and 3 with z=4, total 70. For each key generate all operation orders, retain the four required terminal DFA signatures, form their exact native signed-prefix trie, then solve the four-colour rooted-subtree minimum by the recurrence in EC49FFJ. Every minimum is witnessed by a reconstructed four-word tuple and independently recounting its ordered signed-X6 prefix union.

**Result:** minimum 52 edges, attained at exactly six complete keys,
`(x,y,z)=(x,11-x,1)` with `x=4,5,6,7,8,9`.
The full exact 70-key minimum-cost table is in `EXACT_REPORT_EC49FFK.json`. The run processed 625050 retained operation words and 5320558 prefix trie nodes. A *separately coded* secondary trie-cover dynamic program plus a multinomial/full-key/endpoint/witness audit agreed on all 70 optimal values and counts; its executed source and stdout are in the accompanying author evidence archive, separate from formal independent Driver review. The primary complete per-key witnesses are likewise retained in the author evidence archive.

## Analytic theorem: h-3 constructive key variants for every h>=4

For any integer `h>=4` and any `4<=x<=h`, put
`K=(x,h+2-x,1)`, `r=x-3>=1`, `s=h+1-x>=1`. Take
`w4=f^r e g^s c`, `w2=f^r e g^s d`,
`w8=g f^r e g^(s-1) c`, `w1=g f^r e g^(s-1) d`.
Every word has exactly h operations and matches the original full-key counts. In the original DFA, an initial f keeps the intermediate observer in state 4 under any subsequent f,e,g; an initial g keeps it in state 5 under these operations. Their final c,d transitions produce signatures 4,2 and 8,1 respectively. By the native signed microstep kernel, each word has length `L=2h+4` and endpoint `(2,0,0,0,0,0)`; the two c/d pairs share their first `L-4` microsteps but diverge at the first native microstep of c versus d. The pairs' first steps differ (+axis1 versus +axis2), hence no nonempty prefixes cross pairs. Their total union is exactly `2(L+4)=4h+16` edges. There are `h-3` different complete keys in this constructive family.

Combining this all-h upper construction with the present exact H9 lower certificate and prior EC49FFJ classification proves `C_min(h)=4h+16` for every integer `4<=h<=9`, and each of the `h-3` constructed keys is a minimizer in that finite range. Equality for h>=10 is a live conjecture, not an assertion.

## How to reproduce and validation scope

Run in this directory after checking out the project branch:
```
python3 ../EC49FFJ_NATIVE_PREFIX_TRIE_20261109/VERIFY_EC49FFJ_TRIE.py --hmin 9 --hmax 9 --out /tmp/ec49ffk_h9_complete.json
python3 VERIFY_EC49FFK.py EXACT_REPORT_EC49FFK.json
```
Pure integer BRC operation/DFA computation; no classical pi/trigonometric fallback. This is an author-side mathematical proof via exact exhaustive finite coverage for the declared model, with the 16-state recurrence proved in EC49FFJ. The standalone new script repeats every H9 key calculation and audits the constructible infinite family on h=4..19. Independent project Driver review and formal shared Result admission remain pending.

**Next EC49FFL:** derive a key-independent analytic lower bound `C_min(h)>=4h+16` in a meaningful infinite subfamily, or check H10 exactly using the same signed-prefix trie. For the mother question, take multiwindow/five-key quota patterns not already excluded by exact 22–24 path certificates, keeping each observer and future path operation distinct. P000/ACTIVE worldview unchanged.
