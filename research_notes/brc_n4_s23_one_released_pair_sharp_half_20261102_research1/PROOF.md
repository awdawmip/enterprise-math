# BRC N=4 / S23: one released pair label reduces the seven-witness minimax sharply to 1/2

Date: 2026-11-02. Status: AUTHOR_ANALYTIC_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Scientific input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34; immediate predecessor: seven-witness exact 4/7 at 2abe978bebb87b1940bcccadd51a3448200ba4b5.

## Model and exact theorem
Work with the original six distinct positive sources AU0,AU1,AV,BU0,BU1,BV, six prepared mixing rows M20/20, common stochastic four-group decoder kernels (AU,AV,BU,BV), four stopping atoms, and eleven lawful causal parameters z in [0,1]^11. Source law F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)); the full M20 and shared-parameter index arrays are retained in VERIFY.js.
Let L_D(z)=max_i TV(P_i(z),Q_i(D)), and G(z)=min_j L_{D_j}(z). The seven legal witnesses S={W,J,A,B,C,X,Y} and original eight fixed pair-kernels D1..D8 have the precise definitions in the predecessor proof and in the executable VERIFY.js. In particular A=O(1/7,1), C=N(1/7,1), X=O(1,1/15), Y=(1,0,0,0,0;0,0,0,1,1,1).

For each h in {1,...,8}, keep all original pair-kernels D1..D8 except Dh fixed, and optimize Dh,D9,D10 jointly over arbitrary real row-stochastic 4x4 four-group kernels, with the same common source/mixture geometry. Then

  inf_(Dh,D9,D10) max_(z in S) G(z) = 1/2   (for EVERY h in {1,...,8}).

The exact value with only D9,D10 free was 4/7. Thus freeing any one of the first eight labels produces the exact seven-witness drop 4/7-1/2=1/14.

## Analytic lower bound (all real stochastic decoders)
Five witnesses W,J,A,C,Y have residual minimum risk strictly above 1/2 under the remaining seven fixed pair-kernels, no matter which h is released. Exact minima are independently checked for all eight cases by VERIFY.js. Therefore, if a bank had worst seven-witness risk r<1/2, each of W,J,A,C,Y would have to select one of its three freely optimized kernels.

At the indicated *common prepared row*, the following target pairs are mutually singular, each with exact TV distance 1: W-J at row 6; W-A, W-C, W-Y at row 4; Y-J at row 6; Y-A and Y-C at row 4. A single decoder Q used for such a pair has 2r >= TV(P(U),P(V)) = 1 by the triangle inequality. Hence for r<1/2, W uses a free label distinct from all J,A,C,Y, while Y uses a second free label distinct from J,A,C. With only three free labels, J,A,C must all use the third free label.

For that shared third decoder, on prepared row 3 consider three disjoint events E_J={1,2}, E_A={3}, E_C={4}. Their target masses are respectively 1, 6/7, 6/7; total 19/7. For any common decoded row Q, event discrepancies bounded by TV give

  3r >= P3(J)(E_J)+P3(A)(E_A)+P3(C)(E_C)-1 = 19/7-1 = 12/7.

Thus r>=4/7>1/2, contradiction. This proves the exact 1/2 lower bound using only five of the seven legal witnesses. The argument quantifies over all real stochastic kernels; its small three-label assignment step is combinatorial.

## Constructive upper bound (the same source mixing for every witness)
Use for D9 and D10 the exact rational kernels from the predecessor proof:

  D9:  [1,0,0,0]; [1,0,0,0]; [0,0,1/2,1/2]; [0,1/2,1/2,0].
  D10: [1,0,0,0]; [1,0,0,0]; [1/3,0,1/3,1/3]; [1/3,0,0,2/3].

Replace any selected Dh, h in 1..8, with the same new kernel:

  Dstar: [1/7,0,3/7,3/7]; [1/7,0,3/7,3/7]; [1,0,0,0]; [1,0,0,0].

All three are common, row-stochastic and nonnegative. The minimum risks over D9,D10,Dstar for W,J,A,B,C,X,Y are exactly

  W=1/2, J=4/15, A=3/7, B=1/2, C=3/7, X=1/2, Y=1/2.

Therefore each of the eight allowed choices of h attains seven-witness risk 1/2 regardless of the remaining seven original pair kernels. Combining the analytic lower and explicit upper bounds proves the theorem.

## Evidence and mathematical scope
VERIFY.js extends the pinned predecessor's exact BigInt rational checker, retaining the predecessor's source-mixing, seven-witness target laws and 12 disjoint-event certificates. It additionally checks seven distance-one pair certificates, the row-3 mass 19/7, all 3^5=243 assignments of five compulsory witnesses to three labels, all eight freed-label cases and their full six-preparation risk values. Run with node VERIFY.js. RUN_EVIDENCE.json records the actual V8 exact execution result.

This is a finite-witness sharp optimization under seven frozen pair-kernels and three free common kernels. It identifies which resource relaxation removes the previous 4/7 seven-witness obstruction. The unrestricted eleven-real-parameter, jointly optimized ten-label mother objective retains its earlier global bracket [1/2,2/3] (k=4,6); it requires additional witnesses/continuous certificates. P000 X6 and independent time remain separate typed native interfaces, not inferred from the statistical observer.

## Next scientific question
Determine whether a concrete ten-label bank using seven fixed pair kernels plus the three above can certify a new upper bound below 2/3 on the full [0,1]^11 legal control domain. First check exact ternary controls and identify a worst witness, then bound the continuous eleven-dimensional cells without forgetting shared b_U and six labeled sources. Alternatively seek a bank-independent lower certificate using more than seven witnesses.
