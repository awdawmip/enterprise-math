# BRC N=4 / S23: exact eight-witness radius 1/2 with three common decoders

2026-11-02 | AUTHOR_ANALYTIC_PROOF + EXACT_FRACTION_EXECUTED | UNREVIEWED / NOT_ADMITTED.

Scientific input pin: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Immediate seven-witness predecessor: eca8150ec1426e5f9c4cddae0a773df2e9a81531; Z counterexample: a604ba64f2afff98345f0d94555570a24a136380.

## Model and exact theorem

Retain all six distinct positive-weight sources AU0,AU1,AV,BU0,BU1,BV; the six prepared mixing rows are

~~~text
M20 = [[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
       [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]] / 20.
~~~

At source s the four stopping-time probabilities are F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)). The 11 shared causal parameters are in order z=(a_A,a_B,b_U,b_AV,b_BV; c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV). Their source selectors (zero-based) are AA=(0,0,0,1,1,1), BB=(2,2,3,2,2,4), CC=(5,6,7,8,9,10). A decoder has four common stochastic rows AU,AV,BU,BV; the six source labels select these via (AU,AU,AV,BU,BU,BV). Each of six predictions Q_i(D) uses exactly the same row M20 as its target P_i(z). Define L_D(z)=max_(i=1..6) TV(P_i(z),Q_i(D)) and G_B(z)=min_(D in B) L_D(z).

The eight lawful witnesses are S={W,J,A,B,C,X,Y,Z}, in the displayed causal parameter order:

~~~text
W = (1,0,0,0,1; 0,0,0,0,0,0)
J = (1,1/3,0,0,0; 0,0,0,0,1,0)
A = O(1/7,1);  B = O(1,1/7);  C = N(1/7,1);  X = O(1,1/15)
Y = (1,0,0,0,0; 0,0,0,1,1,1)
Z = (0,1,0,1,0; 1,1,0,0,0,0)
O(s,t) = (s,t,0,0,0; 0,1,1,1,0,1)
N(s,t) = (s,t,0,0,0; 1,0,0,0,0,0)
~~~

THEOREM. For three arbitrary real, row-stochastic four-group/four-stop COMMON kernels,

  inf_(Dα,Dβ,Dγ) max_(z in S) min_(D in {Dα,Dβ,Dγ}) L_D(z) = 1/2.

COROLLARY. For every h=1,...,8, keep the seven original frozen pair-kernels D1..D8 except Dh, and optimize three further kernels. The resulting exact minimax on S is also 1/2. Indeed the three free kernels alone attain 1/2.

## Lower bound for every real stochastic kernel

Use only the five policies W,J,A,C,Y. Their prepared targets are mutually singular (TV exactly 1) for seven pairs: W--J on row 6; W--A, W--C, W--Y on row 4; Y--J on row 6; Y--A, Y--C on row 4. Suppose three kernels obtained loss r<1/2 on all five. If two mutually singular policies used the same kernel, the triangle inequality would give 1 <= 2r < 1, impossible. Hence W and Y use different labels, neither label can serve J,A,C, and these three must use the remaining third label.

On prepared row 3, J targets mass 1 on E_J={1,2}; A targets 6/7 on E_A={3}; C targets 6/7 on E_C={4}. The three events are disjoint, so a common predicted distribution Q obeys

  3r >= 1+6/7+6/7-Q({1,2,3,4}) = 19/7-1 = 12/7.

This forces r>=4/7, contradicting r<1/2. Thus the optimum is at least 1/2. The checker also verifies all seven TV=1 pair identities and all 3^5=243 assignments of the five witnesses to three labels.

## Attaining kernels and exact risks

The following are FOUR source-group rows by FOUR stop atoms (1,2,3,4), with nonnegative entries summing to 1 per row:

~~~text
D_WA   = [[9/14,0,5/14,0], [9/14,0,5/14,0], [1/2,0,0,1/2], [1/2,1/2,0,0]]
D_JBXY = [[1,0,0,0], [1,0,0,0], [0,0,1/2,1/2], [0,0,1/2,1/2]]
D_CZ   = [[1/2,0,1/2,0], [0,1/2,0,1/2], [1,0,0,0], [1,0,0,0]]
~~~

The exact common-six-source risks are 1/2 on W,A for D_WA; on J,B,X,Y for D_JBXY; and on C,Z for D_CZ. The attached exact Fraction program recomputes all 24 risks and the minimum for each witness; all eight minima equal 1/2. The upper and lower certificates close.

## Eight specific full-domain counterexamples

Consider the trial ten-label bank containing the three new kernels and the original eight frozen pair-kernels with ONE original Dh removed. For each removed h, the following legal deterministic policy z_h causes every one of the remaining ten kernels to have loss exactly 1, even though that bank has exact eight-witness risk 1/2:

| Removed Dh | z_h (eleven 0/1 causal coordinates) | risk under Dh (omitted) | all ten retained risks |
|---|---|---:|---:|
| 1 | 00000000000 | 1/2 | 1 |
| 2 | 00000001000 | 1/2 | 1 |
| 3 | 00000000001 | 1/2 | 1 |
| 4 | 00101000000 | 1/2 | 1 |
| 5 | 00110000000 | 1/2 | 1 |
| 6 | 00101001000 | 1/2 | 1 |
| 7 | 00100000001 | 1/2 | 1 |
| 8 | 00100000000 | 1/2 | 1 |

For each of these 8 x 10 = 80 retained decoder/policy pairs, the exact checker exhibits a prepared row whose target support E has mass P_i(E)=1 and whose decoded probability Q_i(E)=0. Consequently L_D(z_h)=1 exactly. Probability normalization gives the reverse bound 1, so the full lawful domain worst risk of each of these particular banks is exactly 1. These eight exact witnesses identify how to extend the finite optimization.

## Validation and interpretation

Run python VERIFY.py (stdlib Fraction, no numerical tolerance). RUN_EVIDENCE.json contains actual stdout, including all 24 rational finite-witness losses, seven singular-event pairs, 243 labelings, eight deterministic off-witness inputs, and 80 exact disjoint-support checks. The lower certificate is analytic for all real kernels. The off-witness result concerns the explicitly listed bank families, and the full-domain inference follows from each lawful exact 0/1 policy. Exploratory LP and binary-vertex scans only proposed the rational inputs; the claims above use the explicit certificates.

This finite BRC observation retains six labeled sources, positive M20 mixing, and shared b_U. It is not a quotient of P000 X6 native space; Heartbeat World native six-axis spatial geometry and separately typed time remain the project's assumptions. The unrestricted ten-label, full 11-real-parameter mother's known bracket remains [1/2,2/3] for k=4,6.
