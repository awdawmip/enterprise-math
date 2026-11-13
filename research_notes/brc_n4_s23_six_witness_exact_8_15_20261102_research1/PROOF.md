# BRC N=4/S23: exact six-witness, two-free-decoder minimax 8/15

2026-11-02. Status: AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_FRACTION / UNREVIEWED / NOT_ADMITTED. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor is the five-witness 32/63 theorem at `5e58af1f8c251fbe729ebc7772e3d95c73502e76`.

## Precise setting and theorem

Retain the exact original six provenance-labeled positive sources AU0, AU1, AV, BU0, BU1, BV, four stopping atoms, shared causal parameter b_U, the common deterministic four-group encoder AU,AU,AV,BU,BU,BV, and mixing matrix `M20/20` with rows
`(10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)`.
The legal 11-vector is `(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)` in `[0,1]^11`. Each latent row is `F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`; each prepared row is the positive M20 mixture of its six latent rows. For any common four-group stochastic decoder D, `L_D(theta)=max_{i=1..6} TV(p_i(theta),q_i(D))`; bank loss is `G(theta)=min_{d=1..10} L_d(theta)`.

Freeze the original first eight decoder rows from predecessor (group order AU,AV,BU,BV; pair `ij` gives half weight on atoms `i,j`):
```
1:34 24 34 24     2:34 23 34 34
3:34 34 34 23     4:24 24 12 12
5:12 12 24 34     6:12 13 23 24
7:23 34 12 13     8:24 34 12 14
```
Let D9,D10 be arbitrary *real* stochastic four-group-by-four-stop kernels. Set
`O(s,t)=(s,t,0,0,0;0,1,1,1,0,1)`, `N(s,t)=(s,t,0,0,0;1,0,0,0,0,0)`. The six lawful witnesses are `W=(1,0,0,0,1;0,0,0,0,0,0)`, `J=(1,1/3,0,0,0;0,0,0,0,1,0)`, `A=O(1/7,1)`, `B=O(1,1/7)`, `C=N(1/7,1)`, and the **new witness `X=O(1,1/15)`**.

**Theorem (exact, all real decoders).**
```
inf_{D9,D10 stochastic} max_{theta in {W,J,A,B,C,X}} G(theta) = 8/15.
```
As all six points belong to `S={W,H,J} union O([0,1]^2) union N([0,1]^2)`, the previously established full-real-two-face interval improves from `[32/63,4/7]` to **`[8/15,4/7]`**, a lower-bound gain `8/315`. No claim is made that this bank covers the full eleven-dimensional control cube.

## Source-disjoint-event lower certificates

If the same stochastic decoder covers three witnesses `u,v,w` at radius `r` on an original prepared row `i`, and `E_u,E_v,E_w` are disjoint sets of stop atoms, then `3r >= p_i(u)(E_u)+p_i(v)(E_v)+p_i(w)(E_w)-1`: each summand follows from TV's event inequality, and the common decoded probabilities on disjoint events sum to at most one.

Here is an explicit sufficient forbidden-triple core. The three event strings have the same order as the triple letters; e.g. `23/4/1` assigns {2,3}, {4}, {1} to the first, second, third witness. All rows are the ORIGINAL six prepared mixture rows (1-based).

| triple | input row | events | target probability sum | forced radius |
|---|---:|---|---:|---:|
| WJA | 6 | 23/4/1 | 8/3 | 5/9 |
| WJB | 6 | 2/14/3 | 20/7 | 13/21 |
| WJC | 6 | 23/4/1 | 8/3 | 5/9 |
| WJX | 6 | 2/14/3 | 44/15 | 29/45 |
| WAB | 6 | 24/1/3 | 20/7 | 13/21 |
| WAC | 3 | 12/3/4 | 19/7 | 4/7 |
| WAX | 6 | 24/1/3 | 44/15 | 29/45 |
| WBC | 6 | 24/3/1 | 20/7 | 13/21 |
| WCX | 6 | 24/1/3 | 44/15 | 29/45 |
| JAC | 3 | 12/3/4 | 19/7 | 4/7 |
| ACX | 3 | 23/4/1 | 19/7 | 4/7 |
| JCX | 6 | 24/1/3 | 13/5 | 8/15 |
| JAX | 6 | 24/1/3 | 13/5 | 8/15 |

Every forced radius is at least 8/15. All 20 possible triples are also checked by the exact executable, which greedily assigns each atom to one of three policies attaining its largest probability on that atom.

The minimum risk under the first EIGHT fixed decoders, using all six prepared rows, is exactly `W:1, J:2/3, A:4/7, B:4/7, C:4/7, X:8/15`. Thus if `r<8/15`, none of these six may use an old label: two new labels must two-color all six. Consider the label/color containing W:

* If it contains none of J,A,C, the other color contains J,A,C, which is forbidden by JAC.
* If it contains at least two of J,A,C, one W-containing forbidden triple appears.
* If it contains precisely J (respectively A, or C) from J,A,C, it can contain no B, X or further witness: WJ*, WA*, or WC* is forbidden. The opposite color therefore contains ACX (respectively JCX, or JAX), each forbidden.

All possible two-colorings contradict one of the listed disjoint-event certificates, giving `r>=8/15` for *arbitrary real stochastic D9,D10*. The executable independently enumerates 32 two-colorings after fixing X's color and verifies an explicit forbidden triple in each.

## Matching constructive upper certificate

Use the predecessor's actual rational common kernels:
```
D9 (AU,AV,BU,BV):
(9/14,0,5/14,0), (9/14,0,0,5/14),
(1/2,0,0,1/2),  (1/2,1/2,0,0).

D10:
(41/63,0,22/63,0), (41/63,0,22/63,0),
(29/45,0,29/315,83/315), (31/63,0,22/63,10/63).
```
They cover `W,C` at radius `1/2`, and `J,A,B` at radius `32/63`. The new X's six original prepared distributions are exactly:
```
row 1 = row 2 = row 3 = (1,0,0,0)
row 4 = (1/15,0,7/15,7/15)
row 5 = (1/15,0,7/75,21/25)
row 6 = (1/15,0,14/15,0).
```
Frozen decoder 5 gives the six TV losses `(1/2,1/2,1/2,8/15,1/2,1/2)`; hence `G(X)<=8/15`. The fixed-eight minimum on X is exactly `8/15`, as checked. The same single ten-decoder bank thus has six-witness maximum exactly `8/15`, proving the upper bound and equality.

## Validation, scope and next question

`VERIFY.py` is the Python-stdlib `Fraction` source actually executed on this six-source/11-control model. `RUN_EVIDENCE.json` captures its full output: all 20 triple certificates, 32 two-colorings, original six-row center risks, stochastic-row normalization, and 8/15 equality. The analytic event/finite-coloring argument proves the theorem for **all real decoders**, with exact rational arithmetic handling only its finite certificate. Initial selection of X used a rational grid scan; the theorem and certificate do not depend on that search.

This BRC source-labeled finite statistics model is an auxiliary observer, not P000 native X6 Cell/time or the six-dimensional spatial system. The full 11-control, 10-label minimax remains `[1/2,2/3]` for k=4,6; this theorem concerns a frozen k=4 common encoder and fixed first eight decoders. Native CLAIM/Result/review and independent mathematical acceptance are pending.

Next: find a seventh lawful witness or a valid exact dual hypergraph tightening the `8/15` lower bound, or construct two real-face-covering kernels strictly improving `4/7`. Preserve all six prepared rows and shared `b_U`.
