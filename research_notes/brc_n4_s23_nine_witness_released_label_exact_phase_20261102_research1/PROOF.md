# BRC N=4 / S23: exact nine-witness radii after releasing one of eight frozen decoders

2026-11-02 · author-side exact mathematical certificate · **UNREVIEWED / NOT_ADMITTED**.
Scientific input: enterprise-math `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (frozen). Parent eight-witness proof: PR #1765 commit `d60079f51d79b14d43d6d2bcd301a5a0ad275807`.

## Claim

Retain the six labeled positive sources AU0, AU1, AV, BU0, BU1, BV, the precise prepared mixing matrix `M20` and their shared causal parameter `b_U` as defined in the predecessor proof and reproduced in `VERIFY.py`. Let `S8={W,J,A,B,C,X,Y,Z}` be its eight lawful eleven-parameter strategies. For h=1,...,8 add `T_h` in the table below; its entries are the original eleven causal coordinates in order `(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)`.

| h | T_h (11 binary digits) | exact radius R_h |
|---|---|---|
| 1 | `00000000000` | 1/2 |
| 2 | `00000001000` | 1/2 |
| 3 | `00000000001` | 1/2 |
| 4 | `00101000000` | 1/2 |
| 5 | `00110000000` | **11/21** |
| 6 | `00101001000` | 1/2 |
| 7 | `00100000001` | 1/2 |
| 8 | `00100000000` | 1/2 |

For each h, keep exactly the seven original pair decoders `{D_1,...,D_8}\{D_h}` fixed. Allow three additional arbitrary real-valued row-stochastic common four-group/four-stop kernels. Define the worst six-preparation total-variation risk for decoder D and lawful policy z by `L_D(z)=max_{1<=i<=6} TV(P_i(z),Q_i(D))`. Then the **exact** finite-set minimax is

```
R_h = inf_{D_alpha,D_beta,D_gamma} max_{z in S8 union {T_h}}
      min_{D in ({D_1,...,D_8} minus {D_h}) union {D_alpha,D_beta,D_gamma}} L_D(z).
```

This result uses all six actual source/mixing rows and one stochastic kernel shared across all prepared inputs. It holds for arbitrary real decoder probabilities.

## Upper bound: eight explicit rational constructions

`VERIFY.py` stores three 4x4 rational row-stochastic kernels for every h, `KERNELS[h]` (row order AU,AV,BU,BV; column order four stopping atoms). Every entry is an exact rational. Direct substitution in the original causal map `F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`, source mapping, and the six-row `M20` gives for **every one of the nine witnesses** a minimum risk equal to `R_h`. Thus all eight upper bounds hold. All 72 per-case witness minimizations and kernels' row-normalization are rechecked with `Fraction`, without numerical tolerances. The seven retained frozen kernels can only improve these upper bounds.

## Lower bounds: 1/2 in seven cases, and a sharp 11/21 obstruction for h=5

The eight-point subset S8 has an analytic three-decoder lower bound 1/2 (predecessor's seven mutual-singularity pairs and three disjoint events). Each original frozen pair decoder has risk >=4/7 or greater on the relevant obstruction policies; the original lower bound therefore remains valid for every released-label case. Alternatively, the exact checker confirms that for each h all nine policies have retained-fixed-decoder minimum risk greater than 1/2; the three free kernels must serve the five obstruction policies, and the established triangle/partition proof applies.

For h=5, a stronger argument gives 11/21. The exact retained-fixed risks on `W,J,A,B,C,X,Y,Z,T5` respectively are `(1,2/3,4/7,1,4/7,1,1,1,1)`, all **strictly greater** than 11/21. Suppose a full ten-decoder bank covers all nine at some radius `r<11/21`. Each witness must therefore be assigned to one of its three free kernels.

For any three witnesses U,V,T assigned to the same common kernel, consider one of the six prepared rows i and allocate each of the four stopping atoms to the target among U,V,T with maximal mass on that atom (ties broken arbitrarily). These events are disjoint. The TV event inequalities imply

```
3r >= [sum_{atom=1}^4 max(P_i(U)[atom], P_i(V)[atom], P_i(T)[atom])] - 1.
```

This is an exact lower-bound certificate for **every** real stochastic decoder. Evaluate all `C(9,3)=84` triples and all six prepared rows in exact rationals. Precisely **70** triples have a row giving a lower bound >=11/21. In particular `(A,Z,T5)` at prepared row 1 attains exactly 11/21. Finally, every one of the **3^9=19,683** possible assignments of nine witnesses to the three free kernels contains a monochromatic triple among those 70 certified triples. `VERIFY.py` enumerates and checks every assignment; it also independently canonicalizes all 3,281 unlabeled partitions. Thus `r<11/21` is impossible, and the exact upper kernels make the bound sharp.

## Interpretation / verification status

The new precise exception is **the fifth released frozen decoder**, for which the ninth off-bank witness raises the exact nine-witness radius from 1/2 to 11/21, a gain of 1/42. The other seven released-label finite problems remain exactly at 1/2. All input strategies are legal points of the original shared eleven-parameter model. Three-decoder lower bounds use analytic TV inequalities and an exhaustive *finite* combinatorial certificate; numerical optimization was used only to discover the rational kernels, and is absent from the final checker.

Full unrestricted eleven-real-parameter ten-label BRC minimax retains its existing `[1/2,2/3]` bracket (k=4,6). No native CLAIM/Result, independent mathematical review, or admission is asserted by this source publication. The Enterprise X6 spatial world and independently typed time remain the project native setting; the S23 observation is a declared restricted mathematical readout, not a quotient of the native state.

Run `python3 VERIFY.py` and compare `RUN_EVIDENCE.json`. Next scientific question: `NEXT_TASK.md`.
