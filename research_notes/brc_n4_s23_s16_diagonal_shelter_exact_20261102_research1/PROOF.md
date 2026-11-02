# BRC N=4 / S23: S16 diagonal shelter theorem (all eight release choices)

2026-11-02. Author-side mathematical result; **UNREVIEWED / NOT_ADMITTED**. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct predecessor: PR #1765, immutable `2b85bbba145e2f102eb4744009eb807a51bb3b0b`, `research_notes/brc_n4_s23_nine_witness_released_label_exact_phase_20261102_research1/{PROOF.md,VERIFY.py}`.

## Exact question and result

Let `S8={W,J,A,B,C,X,Y,Z}` and let `T1,...,T8` be the **eight distinct lawful 11-coordinate binary policies** in the predecessor's `OFF` array, with the original common causal parameter `b_U` and six prepared source rows. Put `S16=S8 union {T1,...,T8}`. Let `D1,...,D8` be the eight original frozen pair decoders `BASE`. For release choice `h`, retain all seven `D_i` with `i != h` and freely optimize three arbitrary real row-stochastic four-group/four-stop kernels `K1,K2,K3`. Let `L_D(z) = max_{u=1..6} TV(P_u(z), Q_u(D))`.

Define

```
R_h(S) = inf_{K1,K2,K3} max_{z in S}
         min( { L_Di(z) : 1 <= i <= 8, i != h }
               union { L_K1(z), L_K2(z), L_K3(z) } ).
```

Then **for all eight choices**,

```
R_h(S16) = R_h(S8 union {T_h}) =
   1/2      if h is 1,2,3,4,6,7,8,
   11/21    if h is 5.
```

The full sixteen-witness pooling therefore creates **no larger radius** than the previous relevant nine-witness problem. This is a new exact reduction of the pooled problem, not an assertion about the unrestricted eleven-real-coordinate continuous domain.

## General protected-witness / diagonal-shelter lemma

Let `D1,...,Dm` be fixed decoders, `W` any base witness set and `z1,...,zm` extra witnesses. Assume `L_Di(zi) <= rho` for each `i`. Fix a released index `h`; retain `Di` for all `i != h` and permit `k` otherwise arbitrary new decoders. If `R_h(W union {zh}) >= rho`, then

```
R_h(W union {z1,...,zm}) = R_h(W union {zh}).
```

**Proof.** The lower bound follows from set inclusion. For the upper bound, choose any free-decoder tuple with risk at most `R_h(W union {zh}) + epsilon` on `W union {zh}` (this exists by definition of infimum). Each additional `zi`, `i != h`, is served by the *retained* `Di` at risk at most `rho <= R_h(W union {zh})`. The same tuple therefore covers all extra witnesses without increasing the worst risk beyond `R_h(W union {zh}) + epsilon`. Send `epsilon` to zero. No attainment, smoothness, independence of source rows, or finite grid assumption is required. QED.

## Exact six-source diagonal calculation

The original source order is `AU0,AU1,AV,BU0,BU1,BV`. Its weight matrix (each row divided by 20) is

```
M = [[10,10, 0, 0, 0, 0],
     [ 9,11, 0, 0, 0, 0],
     [ 0, 0,20, 0, 0, 0],
     [ 0, 0, 0,10,10, 0],
     [ 0, 0, 0, 2,18, 0],
     [ 0, 0, 0, 0, 0,20]].
```

The causal-to-source index vectors are `AA=(0,0,0,1,1,1)`, `BB=(2,2,3,2,2,4)`, `CC=(5,6,7,8,9,10)`, and the common decoder-group map is `G=(0,0,1,2,2,3)`. The original four-stop causal kernel is
`F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c))`.
Prepared targets are `P_u(z)=sum_s M[u,s] F(a_s,b_s,c_s)/20`; prepared decoder rows are `Q_u(D)=sum_s M[u,s] D[G_s]/20`. All six source labels are preserved, including the shared `b_U`.

The exact binary witness list `T1..T8` and original pair-decoder strings are embedded in `VERIFY.js`, copied from the predecessor. A pair string such as `34` represents the row `(0,0,1/2,1/2)`. Every prepared `P_u(Ti)` and `Q_u(Dj)` has denominator dividing 40, so
`L_Dj(Ti)=max_u sum_t |40 P_u(Ti)[t]-40 Q_u(Dj)[t]| / 80`.
The **complete 8x8 exact result**, rows `Ti`, columns `Dj`, is

```
                 D1 D2 D3 D4 D5 D6 D7 D8
 T1               1/2  1  1  1  1  1  1  1
 T2                1  1/2 1  1  1  1  1  1
 T3                1   1  1/2 1  1  1  1  1
 T4                1   1   1  1/2 1  1  1  1
 T5                1   1   1   1  1/2 1  1  1
 T6                1   1   1   1   1  1/2 1  1
 T7                1   1   1   1   1   1  1/2 1
 T8                1   1   1   1   1   1   1  1/2
```

In particular `L_Di(Ti)=rho=1/2`, so the shelter lemma applies. The predecessor's exact nine-witness radii are at least `1/2` and are sharp: `1/2` for seven releases and `11/21` for release 5. Substitution completes the S16 proof. The predecessor's arbitrary-real-kernel lower bounds and explicit rational upper kernels are used unchanged; their proof remains independently reviewable under its own immutable source.

## Verification and scope

`VERIFY.js` uses exact integers (prepared probability denominator 40; TV denominator 80), all 64 original-decoder versus binary-witness risks, and all six prepared rows. It checks all 96 target/decoder row probability normalizations and every diagonal/off-diagonal assertion. The program was actually executed in V8; `RUN_EVIDENCE.json` is the matching observed output. All sixteen strategies are legal in the original eleven-coordinate model. The lemma is valid for arbitrary real stochastic free kernels and infima, not only those found on a rational grid.

The new result is **finite-witness**. There is no new certified improvement to the complete eleven-parameter ten-label minimax interval `[1/2,2/3]` (k=4,6), and no claim of native CLAIM, Result, independent mathematical review, foundation promotion, or P000-native X6 embedding. P000's six-dimensional native discrete Cell geometry, three-dimensional slice semantics and independent time remain unchanged; S23 is a typed auxiliary readout. See `NEXT_TASK.md`.
