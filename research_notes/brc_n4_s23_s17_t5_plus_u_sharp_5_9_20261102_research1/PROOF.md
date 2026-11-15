# BRC N=4 / S23 — sharp 5/9 radius for S17 after releasing D5

**Author-side exact mathematical proof and complete finite verifier, 2026-11-02. UNREVIEWED / NOT_ADMITTED.** Frozen science: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. All source labels and shared `b_U` follow PR #1765 predecessor `2b85bbba145e2f102eb4744009eb807a51bb3b0b`.

## New lawful adversarial witness

The new binary eleven-coordinate strategy (coordinate order `a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV`) is

```
U = 00110000001
```

It differs from the previous `T5=00110000000` in the last coordinate. Under the previous released-D5 bank (seven retained original decoders and the three explicit `KERNELS[5]`), its maximal six-preparation TV loss is **1 for each of all ten decoders**. The exact input and risks are recomputed in `VERIFY.js`; this refutes coverage by that *particular bank*, not by every possible decoder bank.

## Main theorem

Let `S8={W,J,A,B,C,X,Y,Z}`, `Ti` the original eight binary off-bank strategies, and `S17 = S8 union {T1,...,T8,U}`. Retain `D1,D2,D3,D4,D6,D7,D8` as the seven original common source-aware pair decoders; permit three new arbitrary real 4x4 row-stochastic kernels `K1,K2,K3` shared by all six prepared inputs. Each prepared target `P_i(z)` and decoder `Q_i(D)` follows exactly the original six-source positive M20 mixture and shared causal parameter. Write `L_D(z)=max_{i=1..6} TV(P_i(z),Q_i(D))`. Then

```
inf_{K1,K2,K3} max_{z in S17}
 min( min_{j in {1,2,3,4,6,7,8}} L_Dj(z),
      L_K1(z), L_K2(z), L_K3(z) ) = 5/9.
```

This improves the sharp `11/21` bound of the pooled S16 set under the same fifth release by **2/63**. It is an exact finite-witness theorem for arbitrary real random kernels, not a new bound on the globally unrestricted ten-label continuous minimax.

## Upper bound: explicit rational kernels

The following matrices have group-row order `AU,AV,BU,BV`, four stop-atom columns, and rows separated by semicolons. They are all normalized row-stochastic.

```
K1:
10/21 11/21 0 0;
10/21 11/21 0 0;
1/21 10/21 0 10/21;
0 11/21 10/21 0

K2:
44/63 0 19/63 0;
44/63 0 19/63 0;
4/9 1/9 4/9 0;
4/9 0 4/9 1/9

K3:
8/105 97/210 97/210 0;
1/7 113/210 0 67/210;
97/210 113/210 0 0;
97/210 0 0 113/210
```

In the ten-decoder bank formed by the seven retained original decoders plus these three, the exact minimum risks for `(W,J,A,B,C,X,Y,Z,T1,T2,T3,T4,T5,T6,T7,T8,U)` are

```
(11/21,5/9,5/9,11/21,113/210,11/21,5/9,113/210,
 1/2,1/2,1/2,1/2,113/210,1/2,1/2,1/2,11/21).
```

Hence the maximum is exactly `5/9`. The original off-bank T_i with i != 5 are covered by their retained D_i at TV `1/2`, as independently verified by the previous S16 shelter theorem. All original six observation rows are evaluated, with one stochastic kernel shared across them; no source is independently optimized.

## Lower bound: 92 event triples + exhaustive 3-color obstruction

Consider the ten-strategy subset `S10={W,J,A,B,C,X,Y,Z,T5,U}`. Exact computation against the retained fixed seven gives respective minimum risks

```
(1,2/3,4/7,1,4/7,1,1,1,1,1)
```

which are **all strictly greater than 5/9**. If all ten strategies could be covered at a radius `r<5/9`, each would thus have to use one of the three new kernels. Color the ten strategies by their chosen free kernel.

For any three strategies `x,y,z` of one color and any one of the six prepared inputs `i`, allocate each of the four stopping atoms to whichever of `x,y,z` has the largest target mass (break ties deterministically). The three allocated events are disjoint; their total decoder probability is at most one. Since each of the three TV risks is at most `r`, this gives the source-aware exact inequality

```
3 r >= sum_{atom=1}^4 max(P_i(x)[atom],P_i(y)[atom],P_i(z)[atom]) - 1.
```

Exhaustively inspect all `C(10,3)=120` triples and all six original prepared rows using exact integers. **92 triples** admit a row whose right side is at least `5/3`, giving `r>=5/9` whenever that triple is monochromatic. There are **8 critical triples** with bound exactly `5/9`. Exhaustively check all `3^10=59,049` assignments of the ten strategies to three labeled free decoders. Each assignment contains a monochromatic triple among those 92. Thus `r<5/9` is impossible for any real stochastic kernels.

The sharp upper construction proves equality. The finite enumeration is exhaustive because there are exactly 120 triples and 59,049 labeled assignments; the analytic TV inequality gives the universal decoder lower bound. No floating-point approximation enters the certificate.

## Computation and scope

`VERIFY.js` is the actually executed V8 program. It represents all target and decoder prepared probabilities as exact integers scaled by 12,600, checks exact divisibility of source mixing and four-stop causal products, and evaluates total-variation numerators over denominator 25,200. Its standard JSON result is `RUN_EVIDENCE.json`. Independent Python `Fraction` checks of the exact rational bank and the subset event logic also agreed during discovery, but only the reproducible V8 code is published as the primary certificate.

This is an auxiliary S23 finite-witness result; the mother eleven-real-parameter ten-label minimax still has the established interval `[1/2,2/3]` (k=4,6). P000's six original discrete axes, three-dimensional slice and independent time are preserved as the native project ontology, without pretending this finite probability calculation establishes an X6-native transfer. No native CLAIM, Result, Driver review or project mathematical admission is asserted.
