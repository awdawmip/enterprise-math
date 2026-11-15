# BRC N=4 / S23 — exact S18 three-kernel minimax = 4/7

2026-11-02 · **AUTHOR-SIDE ANALYTIC PROOF WITH EXACT CHECKER / UNREVIEWED / NOT_ADMITTED**.
Scientific input frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct predecessors are PR #1765: S16 shelter lemma `17b9d8a75bd6e58b383ccfefdb61cf736fa65857`; sharp S17 result `c25cfc8b15df4498574b06524482419862f1c1ae`.

## Precise statement

Let `S8={W,J,A,B,C,X,Y,Z}` be the eight legal original eleven-parameter strategies. Let `T1,...,T8` be the eight deterministic off-bank strategies, and `U=00110000001` from the previous S17 result. Add a new legal deterministic eleven-coordinate strategy
```
V = 10000000000
```
where the exact coordinate order is `(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)`. Define `S18 = S8 ∪ {T1,...,T8,U,V}`. Preserve six prepared inputs `AU0,AU1,AV,BU0,BU1,BV`, positive `M20` source mixture, the original four-stop causal kernel `F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))` and shared causal `b_U`.

Fix the original source-aware decoders `D1,D2,D3,D4,D6,D7,D8`; allow three *arbitrary real* 4×4 row-stochastic common kernels `K1,K2,K3`. As usual `L_D(z)=max_{i=1}^6 TV(P_i(z),Q_i(D))`. Then the sharp finite-witness optimization is

```
inf_{K1,K2,K3} max_{z in S18} min(
  L_D1(z),L_D2(z),L_D3(z),L_D4(z),
  L_D6(z),L_D7(z),L_D8(z),
  L_K1(z),L_K2(z),L_K3(z)
) = 4/7.
```

This raises the preceding S17 exact value `5/9` by `1/63`, and the S16 D5 value `11/21` by `1/21`, within this same fixed-seven/free-three model.

## Constructive counterexample to the previous S17 upper bank

For `V=10000000000`, direct exact six-preparation total-variation evaluation against **each** of the old S17 ten-kernel bank (the retained original seven and the previous three explicit rational free kernels) gives `L_D(V)=1`. Thus that particular bank is decisively uncovered by V. This observation motivates the fresh optimization; it does not itself prove the 4/7 lower bound against *all* possible new banks.

## Universal lower bound by source-event hypergraph

Select the eleven-policy subset `S11={W,J,A,B,C,X,Y,Z,T5,U,V}`. Their minimum risks over the retained seven original decoders are exactly

```
(1,2/3,4/7,1,4/7,1,1,1,1,1,1).
```

At any proposed radius `r<4/7`, each S11 policy must therefore use one of the **three new** common stochastic kernels. This induces a 3-coloring of eleven policies.

Given any three policies `x,y,z` assigned to the same kernel, and one fixed prepared row i, allocate the four stopping atoms by a deterministic maximizing target among `x,y,z`. The disjoint allocated events `E_x,E_y,E_z` obey
```
  3r >= [sum_{atom=1}^4 max(P_i(x)[atom],P_i(y)[atom],P_i(z)[atom])] - 1.
```
Indeed `P_i(w)(E_w) ≤ Q_i(K)(E_w)+TV(P_i(w),Q_i(K))` for each w, and the Q event probabilities sum to one. This inequality holds for arbitrary real-valued shared stochastic kernels.

Enumerate all `C(11,3)=165` unordered triples, computing the maximum right-hand side over the original six prepared rows in *exact integer arithmetic*. Exactly **111** triples have some row whose disjoint-event bound is at least `4/7`; the other **54** cannot be certified by this particular triple rule. Enumerate all `3^11=177147` assignments of S11 to three labeled free kernels; **each has a monochromatic triple among the 111 certified triples**. Thus a radius strictly below `4/7` is impossible, and `R_5(S18)≥4/7`.

The finite enumeration establishes complete coverage of the stated 3-label assignments, not an extension of the witness set to an infinite parameter domain; the event inequality is the universally quantified real-kernel part.

## Sharp rational upper construction

Three explicit normalized row-stochastic 4×4 kernels, group-row order `AU,AV,BU,BV`, atom-column order 1..4:

```
K1:
5/7 0 2/7 0;
3/7 0 2/7 2/7;
3/7 0 1/35 19/35;
3/7 10/21 0 2/21

K2:
11/21 10/21 0 0;
10/21 11/21 0 0;
1/21 10/21 0 10/21;
0 0 11/21 10/21

K3:
1/2 0 1/2 0;
1/2 1/2 0 0;
1/2 0 1/2 0;
1/2 0 1/2 0
```

With these three and the original seven retained D_i, the exact minimum total-variation risks for the full 18 points (ordered `W,J,A,B,C,X,Y,Z,T1,T2,T3,T4,T5,T6,T7,T8,U,V`) are:

```
(4/7,4/7,4/7,11/21,4/7,11/21,1/2,1/2,
 1/2,1/2,1/2,1/2,11/21,1/2,1/2,1/2,11/21,11/21).
```

The maximum is **exactly 4/7**, closing the proof. All six prepared source mixtures use the same kernel, and the old `T_i` for `i ≠ 5` are separately covered by retained `D_i` at `1/2`.

## Reproducible exact validation, scope and authority

The actual executed `VERIFY.js` checker (V8 / Node) stores prepared probabilities as safe integers scaled by 12600, checks divisibility for every mixing/causal operation, and evaluates TV numerators with denominator 25200. It verifies all 18 legal policies, 10 stochastic decoder kernels, six prepared rows, old-bank counterexample V, 111 triple certificates and all 177147 labeled colorings. Its JSON output is `RUN_EVIDENCE.json`. The checker covers the **complete finite enumerated event/assignment family**; the analytic disjoint-event proof supplies validity for *arbitrary real* decoder probabilities.

This is a sharp finite-observer-witness result in the original typed S23 auxiliary readout. The separate global mother problem optimizing all ten decoders across the entire eleven-real-parameter lawful domain retains the previous best known interval `[1/2,2/3]` for k=4,6. P000's six-dimensional native discrete Cell space, three-dimensional slice, and independent time are preserved and no native-space theorem transfer is asserted. Native owner, formal CLAIM/Result, independent review and promotion remain unconfirmed/ungranted.
