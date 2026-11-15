# BRC N=4 / S23 — sharp 11/18 four-witness obstruction and simultaneous two-face certificate

Date: 2026-11-01. AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. Independent finite statistical S23 theorem, not P000 native spatial dynamics, and not the unrestricted ten-label minimax.

## Scope, sources and observer

Six positive-rational BRC latent sources (AU0, AU1, AV, BU0, BU1, BV) retain separate provenance. The preparation matrix is M=M20/20, with

~~~text
M20 = [[10,10, 0, 0, 0, 0], [ 9,11, 0, 0, 0, 0], [0,0,20,0,0,0],
       [ 0, 0, 0,10,10, 0], [ 0, 0, 0, 2,18, 0], [0,0,0,0,0,20]].
~~~

A legal behavior theta has 11 parameters (a_A,a_B,b_U,b_AV,b_BV; c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV) in [0,1]^11. Each latent source x has distribution F_x=(a_g,(1-a_g)b_h,(1-a_g)(1-b_h)c_x,(1-a_g)(1-b_h)(1-c_x)), with second-stage information set U shared by AU and BU. The prepared stopping law on each of six inputs is p_i=sum_x M_ix F_x.

Fix the deterministic common k=4 encoder E by grouping AU0/AU1 into AU, preserving AV, grouping BU0/BU1 into BU and preserving BV. Fix the FIRST NINE decoders with rows AU,AV,BU,BV; each pair ij has mass 1/2 at stop times i and j:

~~~text
1: 34 24 34 24   2: 34 23 34 34   3: 34 34 34 23
4: 24 24 12 12   5: 12 12 24 34   6: 12 13 23 24
7: 23 34 12 13   8: 24 34 12 14   9: 13 12 13 13
~~~

Let D be ANY REAL row-stochastic four-group-to-four-stop tenth decoder, q_D=M E D, and total variation TV(u,v)=1/2 sum_j |u_j-v_j|. Set L_D(theta)=max_{i=1..6} TV(p_i(theta),q_D,i) and G_D(theta)=min(L_1(theta),...,L_9(theta),L_D(theta)); a label is selected after theta but before observing stop times.

## New exact theorem, quantifiers and witnesses

Define three existing lawful policies and two lawful real two-dimensional faces:

~~~text
W        = (1,   0,   0,0,1 ; 0,0,0,0,0,0)
H        = (1/3, 1,   0,0,0 ; 1,0,1,0,0,0)
J        = (1,   1/3, 0,0,0 ; 0,0,0,0,1,0)
O(s,t)   = (s,   t,   0,0,0 ; 0,1,1,1,0,1)
N(s,t)   = (s,   t,   0,0,0 ; 1,0,0,0,0,0)
P        = O(1,2/9).
~~~

Let S={W,H,J} union {O(s,t):s,t in [0,1]} union {N(s,t):s,t in [0,1]}. Then

   inf_{D in (Delta_4)^4} sup_{theta in S} G_D(theta) = 11/18.

Exactly the same sharp value holds with S replaced by the four-element set {W,H,J,P}. In particular ANY tenth decoder added to these particular fixed nine with this fixed encoder has global lawful S23 worst-case loss >=11/18, an improvement of 1/18 over the previous 5/9 fixed-nine obstruction. This DOES NOT constrain a bank that can change its first nine decoders, nor all k=4 encoders.

### Analytic lower bound for every real stochastic tenth kernel

Direct exact evaluation of the fixed nine gives:

| theta | min of L_1,...,L_9 | prepared BV row (i=6) |
|---|---:|---|
| W | 1 | (0,1,0,0) |
| H | 2/3 | (1,0,0,0) |
| J | 2/3 | (1/3,0,0,2/3) |
| P | 11/18 | (2/9,0,7/9,0) |

For any r<11/18, none of the first nine decoders covers any of these four at risk <=r. Suppose the tenth decoder covered all of them. The pure BV preparation i=6 is unchanged by mixing, so its decoded distribution is the same stochastic BV row q=(q1,q2,q3,q4) for every policy. From W and H, TV<=r forces q2>=1-r and q1>=1-r. The J target forces q4>=2/3-r. The P target forces q3>=7/9-r. Hence normalization requires

  1=sum_j qj >= 2(1-r)+(2/3-r)+(7/9-r)=31/9-4r,

implying r>=11/18. Contradiction. This is a genuine universal analytical bound in all real decoder probabilities, not a numerical heuristic.

### Explicit matching tenth kernel

The four rows AU,AV,BU,BV of the tenth decoder are:

| group | time 1 | time 2 | time 3 | time 4 |
|---|---:|---:|---:|---:|
| AU | 7/18 | 4/9 | 1/6 | 0 |
| AV | 7/18 | 5/18 | 1/6 | 1/6 |
| BU | 7/18 | 0 | 2/9 | 7/18 |
| BV | 7/18 | 7/18 | 1/6 | 1/18 |

Each row sums to 1. Direct six-input exact mixture gives L_D(W)=L_D(H)=L_D(J)=L_D(P)=11/18, closing the four-witness minimax.

### Exact closed-rectangle continuum certificate on TWO complete real faces

On both O and N, every A prepared stopping distribution depends affinely only on s; every B distribution only on t, because the exact M has zero cross-group entries. For a fixed decoder, a constraint TV(p_i(z),q_i)<=r is EQUIVALENT to all 16 signed linear inequalities

  sum_{u=1}^4 sigma_u (p_i(z)_u-q_i,u) <= 2r,  sigma in {-1,1}^4.

Intersect the resulting affine halfspaces for three A mixed preparations and three B preparations. Every decoder's sublevel set is precisely the Cartesian product of two closed intervals. At r=11/18 the following four exact sublevel rectangles already cover each whole [0,1]^2:

N(s,t):
| label | s interval | t interval |
|---|---|---|
| 1 | [0,11/18] | [0,11/18] |
| 4 | [0,2/9] | [7/18,1] |
| 5 | [7/18,1] | [0,11/18] |
| 10 | [2/9,1] | [1/3,1] |

O(s,t):
| label | s interval | t interval |
|---|---|---|
| 2 | [0,11/18] | [0,11/18] |
| 7 | [0,2/9] | [7/18,1] |
| 5 | [7/18,1] | [0,2/9] |
| 10 | [2/9,1] | [2/9,1] |

To see complete coverage, if s<=2/9 use the first two relevant rectangles, whose t intervals [0,11/18] and [7/18,1] overlap. For s>=2/9 use the tenth rectangle at upper t (>=1/3 on N, >=2/9 on O), and use the lower-t rectangles with s intervals [0,11/18] and [7/18,1], which overlap. All sets are closed, hence boundaries also covered. Therefore sup_{theta in S} G_D(theta)<=11/18 and the four-witness lower bound proves exact equality.

## Executed evidence and model boundaries

VERIFY.py is a stand-alone Python standard-library Fraction program. It constructs every source law, matrix row, encoder, and decoder, verifies the four exact witnesses and their all-six-row errors, intersects every sign inequality to establish the eight exact rectangle intervals, and checks the complete rational rectangle cell partition (16 open cells on each face with closed boundaries). RUN_EVIDENCE.txt contains actual stdout. The universal real-domain statements rest on the analytical lower bound and affine-halfspace/rectangle cover, rather than extrapolation from finite samples.

Compared with the prior frozen ten-label 9/14 one-face exact result, this is a different tenth decoder; it sharpens the FIXED-NINE best attainable risk simultaneously over two entire real faces plus W/H/J to 11/18. The unrestricted 11D minimax for k=4 and k=6,m=10 still has known interval [1/2,2/3]. S2 causal information-set transfer, native P000 X6/independent-time fidelity, and independent mathematical review remain separate obligations. Statistical source labels are not native spatial axes.
