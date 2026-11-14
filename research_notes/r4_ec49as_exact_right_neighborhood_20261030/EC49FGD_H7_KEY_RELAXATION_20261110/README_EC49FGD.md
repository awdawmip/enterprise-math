# EC49FGD — Exact H7-low key-relaxation crossover: 95 single-key edges versus 93 multi-key edges

Date: 2026-11-10 (Asia/Shanghai). Researcher: **EM-DIRECT-E7770A**; native research activity: **RA-118B1A402E7E8240CC10EF43**. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: **AUTHOR_EXACT_FINITE_COMPUTATION / WITNESS_VERIFIED / NOT_ADMITTED**. No current immutable publication or CLAIM exists for the historical EC49AS task; do not treat this author-side note as a formal Source Result.

## Exact model

Reuse the original six ordered signed X6 operation words
`a=(-1,-1),c=(1,2,-1,-2),d=(2,1,-2,-1),e=(3,1,1,-3),f=(1,-1),g=(2,-2)`,
the frozen 9-state DFA (from `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py`, Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`), original rational nine-history rank observer, terminal labels, and literal signed-native microstep-prefix cost.

Keep the following **20 operation words** fixed, a 20/24-label background of the **actual original mother signature pattern** (H2/H3 high, H7 low):

```text
H2: 16=fe          32=ge
H3: 16=feg         32=gef
H4:  1=gefd         2=fegd       4=cefg        8=gefc
H5: 16=feggf       32=geffg
H6:  1=gefdfg       2=fegdgf     4=feggfc      8=geffgc
H8:  1=geffgfgd     2=feggffgd   4=feggfcfg    8=geffgcgf
H9: 16=feggffggf   32=geffgfggf
```

Their union B contains **89 distinct nonempty literal native signed-six-axis prefixes**. At H7 supply exactly four low terminal labels 1,2,4,8, with any admissible length-7 operation word, legal original DFA state, endpoint (+2,0,0,0,0,0), `#e=#a+1`, and positive full key `K=(x,y,z)`. The exact multiplicity equations are

```
a=z-1, e=z, r=c+d=x+y-8, f=8-y-2z, g=8-x.
```

All counts are nonnegative. Since `h=7`, every possible **strictly positive** key is covered by `1<=z<=3,1<=x<=8,1<=y<=8-2z,x+y>=8`. Split `r=c+d` over every `c=0..r`, enumerate all legal orderings, and run the original DFA.

## Theorem A — H7 four labels constrained to ONE positive full key

Exactly **34** positive keys can individually realize all four low H7 labels. The exact global minimum for the fixed background B among all these key choices is

```
min_{positive K; four H7 labels use K} |B union Prefix(H7 paths)| = 95.
```

The unique optimal key values are `(5,4,1)` and `(6,3,1)`; each adds exactly **6** edges. Prior EC49FGC treated only `K=(6,4,1)` and found **104** (15 new edges). Thus changing the key within the same H7 single-key model saves **9** exact native-prefix edges.

An explicit 95-edge H7 witness at `K=(6,3,1)`: `1=gefdfgf; 2=fegdgff; 4=feggfcf; 8=geffgcf` (the last label can also take `geffgcg` under the distinct key `(5,4,1)` for Theorem B).

**Finite exhaustive proof:** For each of the 34 feasible keys, generate every length-7 word of the prescribed multiset, drop DFA-dead transitions, retain the exact four labels, and insert their **full literal signed-native microstep strings** into a Trie. Let `D_v[S]` be the minimum number of prefix edges outside B used to meet exactly subset S of the four labels inside subtree v. At a terminal allow the empty mask and its own terminal label; merge children with disjoint masks A,B at cost `D_old[A]+D_child[B]+[B nonempty and prefix(child) notin B_background]`. The root full mask is exact because all paths are enumerated and each prefix edge is charged once. The independently computed table of 34 minima is listed below.

## Theorem B — H7 paths may have DIFFERENT positive full keys

Across **all** 25,060 admissible H7 low-signature operation words, with no within-H7 key sharing requirement,

```
min |B union Prefix(H7 paths)| = 93 = 89 + 4.
```

One exact achieving 24-label witness is obtained by adding:

```text
H7: 1=gefdfgf    K=(6,3,1)
    2=fegdgff    K=(6,3,1)
    4=feggfcf    K=(6,3,1)
    8=geffgcg    K=(5,4,1)
```

Literal signed-X6 expansion gives exactly **93** edges. At every H2..H9 the required labels produce exact rational nine-history rank **9**, each word has its correct terminal nine-state label and endpoint (+2,0,0,0,0,0). The 93-edge witness uses **8 distinct raw full-key triples**, or **7 strictly positive triples** (H2 `fe` has `(3,0,1)`); it therefore **does not meet the mother target of at most five full keys**.

The **lower bound 4** can be checked without trusting an MILP solver. Complete H7 enumeration gives at least **two** prefixes outside B for any H7 word of signature 1, and at least **two** for signature 2. Signature-1 paths can begin only with `d` or `g` (first signed native step +2); signature-2 paths begin only with `a,e,f` (first signed native step -1,+3,+1). Thus the two fresh-prefix sets are disjoint, forcing at least 2+2=4. The displayed witness attains the bound. An independent complete all-key 16-mask Trie DP, using 125,245 trie nodes, also reports exactly four new edges.

## Complete same-key optimum table

For every feasible positive H7 key, columns are K, total legal low-signature operation words, extra native-prefix edges relative to B, and resulting total:

| K | words | extra | total |
|---|---:|---:|---:|
| (3,6,1) | 84 | 44 | 133 |
| (4,5,1) | 420 | 22 | 111 |
| (4,6,1) | 210 | 53 | 142 |
| (5,4,1) | 840 | **6** | **95** |
| (5,5,1) | 840 | 30 | 119 |
| (5,6,1) | 280 | 63 | 152 |
| (6,3,1) | 840 | **6** | **95** |
| (6,4,1) | 1260 | 15 | 104 |
| (6,5,1) | 840 | 38 | 127 |
| (6,6,1) | 210 | 73 | 162 |
| (7,2,1) | 420 | 22 | 111 |
| (7,3,1) | 840 | 28 | 117 |
| (7,4,1) | 840 | 36 | 125 |
| (7,5,1) | 420 | 47 | 136 |
| (7,6,1) | 84 | 82 | 171 |
| (8,1,1) | 84 | 47 | 136 |
| (8,2,1) | 210 | 57 | 146 |
| (8,3,1) | 280 | 67 | 156 |
| (8,4,1) | 210 | 77 | 166 |
| (8,5,1) | 84 | 86 | 175 |
| (8,6,1) | 14 | 98 | 187 |
| (5,4,2) | 840 | 50 | 139 |
| (6,3,2) | 2520 | 29 | 118 |
| (6,4,2) | 1260 | 59 | 148 |
| (7,2,2) | 2520 | 30 | 119 |
| (7,3,2) | 2520 | 39 | 128 |
| (7,4,2) | 840 | 69 | 158 |
| (8,1,2) | 840 | 53 | 142 |
| (8,2,2) | 1260 | 63 | 152 |
| (8,3,2) | 840 | 73 | 162 |
| (8,4,2) | 210 | 84 | 173 |
| (7,2,3) | 840 | 56 | 145 |
| (8,1,3) | 840 | 59 | 148 |
| (8,2,3) | 420 | 70 | 159 |

## Verification and next discriminating question

Actual exact-integer computations (2026-11-10): 34 finite same-key Trie optimizations; unrestricted all-key 25,060-word 125,245-node Trie optimization; separate complete-witness signed-X6/DFA/endpoint/rational-rank check. Attached code `VERIFY_EC49FGD.py`, `SCAN_MULTIKEY_EC49FGD.py`, `CHECK_WITNESS_EC49FGD.py` and JSON summaries preserve the steps. No floating-point solver was used to derive these integer minima.

**Next:** jointly alter the 20 background words/key assignments to reduce *distinct full keys* while retaining all 24 original labels and at most 93 literal native prefixes; count both the zero-coordinate H2 seed and strictly positive keys explicitly. The present sharp 93-edge result isolates the key-sharing difficulty for this fixed-word background. Any restriction to a particular background is part of the precise theorem, not a general mother-target no-go. P000 and ACTIVE worldview remain unchanged.
