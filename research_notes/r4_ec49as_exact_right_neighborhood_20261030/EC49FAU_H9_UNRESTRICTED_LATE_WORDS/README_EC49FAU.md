# EC49FAU — Exact unrestricted H8/H9 native-X6 BRC optimum for four fixed early schedules

Date: 2026-11-05 (Asia/Shanghai). Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Parent: EC49FAT `e00990837957c7022e57b44e8c9fa8ab386b9b21`. Scope: author-side exact finite proof, not canonical Result/Driver admission.

## Theorem (four separate fixed-H2–H7 families)

Fix one of the four early schedules numbered **1512, 1513, 2200, 2203**, reconstructed verbatim in `VERIFY_EC49FAU.js` from the pinned parent. Each of H2,…,H7 retains the original nine-history rational observer rank 9; in total they use exactly **72 distinct nonempty ordered signed-native-X6 primitive prefixes**, four full six-coordinate positive BRC cache keys and six observation signatures.

Now allow H8 and H9 **arbitrary ordered seven-operation words** of their respective lengths, without any earlier-root requirement, with the original signed native-X6 endpoint displacement `(2,0,0,0,0,0)`, exactly five full six-axis positive BRC keys across all eight horizons, at most the six original observation signatures and rational observer rank 9 at every horizon. Count the union of all nonempty *native signed-primitive* prefixes as the edge cost E.

**For each fixed early schedule independently, the exact optimum is E*=94.**

This proves optimality over *all* late words for those four early schedules, including late words branching outside any previously selected H2–H6 word. The unrestricted H2–H9 mother problem remains at the author-side bounds `80<=E*_H9<=94`.

## Complete native generator (no root assumptions)

The pinned primitive operations, represented by ordered signed X6 axis moves, are

```text
a=(-1,-1) b=(-2,-2)
c=(+1,+2,-1,-2) d=(+2,+1,-2,-1)
e=(+3,+1,+1,-3)
f=(+1,-1) g=(+2,-2)
```

Let a length-h legal word have complete positive BRC key `K=(x,y,z,0,0,0)`. The signed endpoint `+2 E_1` forces **#b=0 and #e=#a+1**. Write `z=#e>=1`, `m=#c+#d`, and `u=#f`, `v=#g`. Positive-axis counts and total operation length give

```text
h = (z-1)+z+m+u+v = 2z-1+m+u+v,
x = 2z+m+u,
y = m+v.
```

Consequently, every possible word at exact h,K, and only such a word, is a distinct permutation of the multiset

```text
a^(z-1) e^z (c|d)^m f^u g^v
m=x+y-h-1,  u=h+1-y-2z,  v=h+1-x
z>=1,  m,u,v>=0.
```

Here `(c|d)^m` means **each individual occurrence independently chooses c or d**, preserving its original ordered signed primitive steps. The enumerator visits all such ordered words, computes their complete six-axis positive BRC key, the exact signed endpoint and all nine original observation histories; only the original six signatures are retained. Thus this finite generator covers all late candidates, without ancestry/branching assumptions.

The original signatures are `D=de, E=ed, C=ce, J=ec, F=feg, G=gef`; the exact rational nine-history rank criterion already proved in EC49FAR and independently Fraction-checked in EC49FAT is

```text
rank9(mask) iff (E or F) and (C or F) and (D or G) and (J or G).
```

## Exact lower bound (all 200 exhaustive classes)

Let `P0` be the set of the 72 early native primitive prefixes, `W8(K)`, `W9(K)` the complete eligible candidate-word sets for full key K. All four early positive keys are infeasible at H8 and H9 in this full-length enumeration: they do not even meet the key-length arithmetic. Thus the five-key budget requires **the same new fifth key** at both late horizons. The complete length/key arithmetic gives 70 raw keys at H8, 95 raw keys at H9 and precisely **50 shared raw keys**. Every one of those 50 has rank-nine-capable full late candidate pools. Hence each of the four schedules has exactly 50 complete fifth-key classes to check.

Define `Pref(A)` as the distinct nonempty ordered signed-primitive prefixes of word set A:

```text
d8(K) = min_{A subset W8(K), rank(A)=9} |Pref(A) \ P0|

d9_plus(K) = min_{B subset W9(K), rank(B)=9}
            |Pref(B) \ (P0 union Pref(W8(K)))|.
```

Granting H9 all possible eligible H8 prefixes for free is an optimistic *lower-bound relaxation*. Every legal joint choice A,B therefore satisfies

```text
E >= 72 + d8(K) + d9_plus(K).
```

`VERIFY_EC49FAU.js` implements exact minimal-cost six-bit OR-mask dynamic programming over the full signed-primitive prefix trie. At a node, every child contributes an independently selectable mask/cost; combining children ORs the masks and adds the costs, keeping the least cost per mask. Nonfree nonroot nodes each charge exactly one edge when selected. Induction on subtree height proves exactness of all costs over the finite word set. All signature masks satisfying the stated four-clause rank condition are considered.

The **200** stored class certificates (50 keys × 4 early schedules) all obey `d8>=16`, `d9_plus>=6`, and therefore `72+d8+d9_plus>=94`. Each case has a unique key at which the relaxed lower bound attains 94:

| Early schedule | Attaining full fifth key | d8 | d9_plus | Lower bound |
|---|---|---:|---:|---:|
| 1512 | (5,5,1,0,0,0) | 16 | 6 | 94 |
| 1513 | (7,3,1,0,0,0) | 16 | 6 | 94 |
| 2200 | (5,5,1,0,0,0) | 16 | 6 | 94 |
| 2203 | (7,3,1,0,0,0) | 16 | 6 | 94 |

The pinned EC49FAJ construction is an upper witness in the unrestricted candidate family: for each early H7 path p select `pc,pd` at H8 and `pfg` at H9. The executed program recomputes native-prefix count **94**, five complete BRC keys, six signatures, signed endpoint and rational rank 9 at every horizon. Thus lower and upper bounds match.

## New independent all-late-word census

An independent direct C++ literal enumerator and a separately written Python finite-state dynamic program (carrying the native observation transitions, full-key counts and first-three-operation ancestry, not root-filtered candidates) agree exactly:

| Horizon | All +2E1 operation words | Allowed six-signature words | H2-rooted | H3-rooted excluding H2 | Escaping both |
|---|---:|---:|---:|---:|---:|
| H8 | 340,064 | 131,686 | 15,956 | 2,988 | **112,742** |
| H9 | 1,964,862 | 647,930 | 73,932 | 14,108 | **559,890** |

These escaping words are explicitly included in the new theorem's candidate pools. Independent Python finite-state mask census agrees with the exhaustive generator's per-key six-signature masks for **all 100 pairs (50 shared keys × both late horizons)**. All programs use exact integer combinatorics on native signed-X6 paths; the original rational-rank-to-four-clause reduction is previously crosschecked by exact Fraction elimination. No floating-point approximation or modular-rank heuristic enters the new certificate.

## Actual execution and files

The published `VERIFY_EC49FAU.js` was **actually executed in the current isolated JavaScript V8 runtime** on the entire 200-class domain, with result status `PASS_AUTHOR_SIDE_EXACT_INTEGER` and all four 94-edge outcomes. Its full *actual output* is stored, not a skeleton, as `EXACT_REPORT_EC49FAU.json` (all case/key rows, costs, counts and trie-node counts). The independently executed Python/C++ crosschecks agree on the full candidate census and were retained as separate supporting local files.

Reproduce with `node VERIFY_EC49FAU.js > EXACT_REPORT_EC49FAU.reproduced.json`; it needs Node.js >=18, no third-party dependencies, and should be run with sufficient memory for the full enumeration. The program retains all original ordered primitive steps; it does not use a coarse endpoint-only trie.

**Next EC49FAV:** since all arbitrary late-window words have now been covered for these four early schedules, reconfigure H2–H7 jointly and search an explicit legal **93-edge** nine-window construction, or establish an exact lower bound on a newly specified early-window family. Preserve the frozen scientific input; P000 and ACTIVE worldview are unchanged. The Github author-side artifact is distinct from native Source CLAIM/Result and independent Driver review.
