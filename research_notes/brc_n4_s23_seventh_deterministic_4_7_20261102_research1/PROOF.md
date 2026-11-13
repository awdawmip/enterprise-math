# BRC N=4 / S23 — seventh off-face witness gives exact minimax 4/7

Date: 2026-11-02. Evidence state: AUTHOR_ANALYTIC_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Parent: six-witness single-line exact profile at `d60c0b6427c363657879b198ac3834c0cd376dbb`.

## Model and theorem
Retain original six **labeled** positive sources `AU0,AU1,AV,BU0,BU1,BV`, common shared `b_U`, and original six prepared mixing rows `M20 = [10,10,0,0,0,0; 9,11,0,0,0,0; 0,0,20,0,0,0; 0,0,0,10,10,0; 0,0,0,2,18,0; 0,0,0,0,0,20]`, divided by 20. Latent source law is `F(a,b,c)=(a,(1−a)b,(1−a)(1−b)c,(1−a)(1−b)(1−c))`. Legal controls `z=(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)∈[0,1]^11`. Index maps are `AA=[0,0,0,1,1,1]`, `BB=[2,2,3,2,2,4]`, `CC=[5,6,7,8,9,10]`.

Decoder `D` has four common stochastic group rows `AU,AV,BU,BV`; expand with source group map `[AU,AU,AV,BU,BU,BV]` and the same M20. Define `L_D(z)=max_i TV(P_i(z),Q_i(D))` on the four stopping atoms and `G(z)=min_{j≤10} L_{D_j}(z)`. Fixed decoders D1..D8 are the original pair kernels (exactly specified in VERIFY.js); D9,D10 range over **all real stochastic 4×4 kernels**.

Existing points:
- `W=(1,0,0,0,1;0,0,0,0,0,0)`, `J=(1,1/3,0,0,0;0,0,0,0,1,0)`.
- `O(s,t)=(s,t,0,0,0;0,1,1,1,0,1)`, `N(s,t)=(s,t,0,0,0;1,0,0,0,0,0)`.
- `A=O(1/7,1)`, `B=O(1,1/7)`, `C=N(1/7,1)`, `X=O(1,1/15)`.

**New seventh witness:** `Y=(1,0,0,0,0;0,0,0,1,1,1)`. Its six prepared rows are **exactly** `(e1,e1,e1,e3,e3,e3)`. It is lawful and off both O/N subfaces.

**Theorem:** for `S={W,J,A,B,C,X,Y}`,
`inf_{D9,D10∈Stoch(4,4)} max_{z∈S} G(z) = 4/7`.
In particular, the full eleven-real-parameter minimax with **these eight fixed decoders** has lower bound 4/7.

## Lower certificate for arbitrary real free decoders
If three witnesses U,V,T use the same decoded prepared row Q_i with TV risks ≤r, then for pairwise disjoint stop events E_U,E_V,E_T:
`3r ≥ P_i(U)(E_U)+P_i(V)(E_V)+P_i(T)(E_T)-1`.
Reason: each individual event discrepancy is bounded by TV, and `Q_i(E_U)+Q_i(E_V)+Q_i(E_T)≤1`. This applies uniformly to all real decoder probabilities.

The original fixed-eight minimum risks on `W,J,A,B,C,Y` are `1,2/3,4/7,4/7,4/7,1` (the additional X has fixed minimum 8/15). For `r<4/7` each of these six must therefore use free decoder D9 or D10. This creates a two-coloring of six vertices; fix W color 0 and enumerate 32 remaining color assignments.

Every coloring has a monochromatic triple among the twelve exact event certificates below. Notation `WJB: 6: 2/14/3: 20/7` means prepared row 6, disjoint atom sets `{2},{1,4},{3}`, target mass 20/7, and the triple event lower bound `(20/7−1)/3`.

| Triple | Row | Disjoint events | Mass | TV lower bound |
|---|---:|---|---:|---:|
| WJB | 6 | 2/14/3 | 20/7 | 13/21 |
| WJY | 6 | 2/14/3 | 3 | 2/3 |
| WAB | 6 | 24/1/3 | 20/7 | 13/21 |
| WAC | 3 | 12/3/4 | 19/7 | 4/7 |
| WAY | 6 | 24/1/3 | 3 | 2/3 |
| WBC | 6 | 24/3/1 | 20/7 | 13/21 |
| WCY | 6 | 24/1/3 | 3 | 2/3 |
| JAC | 3 | 12/3/4 | 19/7 | 4/7 |
| ABC | 3 | 23/1/4 | 19/7 | 4/7 |
| ABY | 5 | 12/4/3 | 97/35 | 62/105 |
| ACY | 3 | 23/4/1 | 19/7 | 4/7 |
| BCY | 5 | 24/1/3 | 97/35 | 62/105 |

All lower bounds are ≥4/7. Complete two-coloring witness list (mask bits in order J,A,B,C,Y):
```
00 WJB  01 WAB  02 WJB  03 WBC  04 WJY  05 WAC  06 WJY  07 WCY
08 WJB  09 WAB  10 WJB  11 JAC  12 WJY  13 WAY  14 WJY  15 JAC
16 WJB  17 WAB  18 WJB  19 WBC  20 WAC  21 WAC  22 ABY  23 ABY
24 WJB  25 WAB  26 WJB  27 JAC  28 BCY  29 BCY  30 ABC  31 JAC
```
Thus any hypothetical risk r<4/7 yields a monochromatic triple forcing r≥4/7, a contradiction.

## Upper certificate (explicit shared stochastic kernels)
Group-row order AU,AV,BU,BV; atom columns 1,2,3,4. Keep fixed D1..D8 and choose
```
D9 = [1,0,0,0]; [1,0,0,0]; [0,0,1/2,1/2]; [0,1/2,1/2,0].
D10= [1,0,0,0]; [1,0,0,0]; [1/3,0,1/3,1/3]; [1/3,0,0,2/3].
```
Each is nonnegative row-stochastic. All seven **full original six-preparation** risks (minimum over all ten common decoders) are: W=1/2 (D9), J=4/15 (D10), A=4/7 (D7), B=1/2 (D9), C=4/7 (D4), X=1/2 (D9), Y=1/2 (D9). Hence max =4/7.

## Verification, scope, frontier
`node VERIFY.js` uses exact BigInt rationals, validates six prepared rows, all relevant fixed decoder risks, the twelve disjoint-event masses, **all 32 two-colorings**, stochasticity and attained seven-witness risks. `RUN_EVIDENCE.json` is the actual returned result from the exact same verification function published in this source file. The real-decoder lower bound is analytic; finite exhaustive colorings are a complete finite proof obligation rather than a sampling claim.

Relative to the previous six-witness peak 8/15 this seventh lawful off-face witness raises the fixed-eight finite-witness optimum by **4/105**. The resulting full-[0,1]^11 **restricted-design lower bound** is 4/7. General jointly optimized ten-label minimax remains in the earlier [1/2,2/3] bracket (k=4,6). P000 native X6, three-dimensional slice and independent-time transfer is a distinct unproved interface; this result is exact within the positive-source statistical observer.

Next: vary one or more of the eight frozen decoders, keeping all six source rows and common random-kernel constraints, to determine if the 4/7 obstruction persists; find a lower certificate for jointly redesigned ten decoders or a sharper universal upper construction. Native owner/CLAIM/Result, independent review and mathematical admission remain pending.
