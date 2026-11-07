# S23 conditional AV (n=3): exact full-27-output minimax

2026-11-07. Author-side exact rational/analytic proof. Independent mathematical review and native admission pending.
Frozen scientific source: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: PR #1777@37dd89d9fd81df3be22808e00f44aa917b6b6ebe.

## Theorem (full observer)

For every real a,c in [1/2,7/8], set z=(1-a)c and b=(1-a)(1-c). Conditioned on the SAME unknown pair (a,c), the full three-symbol ordered output law is (a,z,b) to the third tensor power (27 ordered words). The compressed input law is Bernoulli(z) to the third tensor power (8 ordered words). Among all parameter-independent stochastic decoders from the eight input words to the 27 output words, the exact worst-case total-variation minimax error is

**δ₃ = 5211/21952 = 0.23738155976676384…**

This is the original full 27-output conditional AV auxiliary problem, not the three-class coarsening.

## A simple exact optimal 4×10 kernel

The binary input count k is the number of nondistinguished symbols. Group outputs by histogram h=(h0,h1,h2). Column order, followed by number m(h) of ordered words in each histogram:

~~~text
h:     300   210   201   120   111   102   030   021   012   003
m(h):    1     3     3     3     6     3     1     3     3     1
~~~

The rows of K are HISTOGRAM-TOTAL probabilities, not single ordered-word probabilities:

~~~text
k0: 0     0      0         0             0       0     1      0      0      0
k1: 0     3/10   0         7/10          0       0     0      0      0      0
k2: 0     21/100 9/25      157/22050     27/100  7/100 0      3/50   1/50   127/44100
k3: 18/25 6/25   919/37044 14069/926100 0       0     0      0      0      0
~~~

To lift to the actual 8×27 decoder, use the same count-k row for every binary word of that count, then assign probability K[k,h]/m(h) to each ordered ternary word with histogram h. This gives nonnegative row-stochastic probabilities and preserves full-27 total variation exactly. The A-event row masses (at least one output symbol 2) are (0,0,1381/1764,919/37044), matching the prior sharp necessary face at t=t0.

## Exact lower bound

Take (a,c)=(1/2,1/2) and (5/7,7/8). Both give z=1/4 and thus identical compressed input distributions, but different target 27-output laws. Their total-variation distance is exactly 5211/10976=2d for d=5211/21952. Any common reconstructed distribution has at least one error ≥d by the triangle inequality.

## All-real upper bound via two Bernstein rectangles

For each histogram h, the target mass is Q_h=m(h) a^h0 z^h1 b^h2. The predicted mass is
M_h=Σ_{k=0}^3 C(3,k) z^(3-k)(1-z)^k K[k,h].
Set r_h=Q_h−M_h, so Σ_h r_h=0 and TV=Σ_h max(0,r_h). Every r_h is a polynomial of degree at most 3 in each of a and c separately.

Split the full real parameter square into just two rectangles:
L=[1/2,5/7]×[1/2,7/8]; R=[5/7,7/8]×[1/2,7/8].
Represent each r_h on each rectangle in the tensor bicubic Bernstein basis, with coefficients β[h,i,j] for i,j=0,1,2,3. The basis is nonnegative and sums to one, giving the rigorous continuous bound

**TV(a,c) ≤ max_{i,j} Σ_h max(0,β[h,i,j]).**

Here are all 32 exact rational values of the slack d−Σ_h max(0,β[h,i,j]), 4 rows × 4 columns for each rectangle:

~~~text
L:
0                       210573/2195200       3649467/35123200       700041/10035200
3537/76832              6032483/46099200    1052489/9219840        11611/351232
2229971/26891200        3419/21952          2487101/23049600       0
22419301/188238400      681061/3841600      2187/19208             0

R:
22419301/188238400      681061/3841600      2187/19208             0
706619/5378240          1224973/6722800     127279/1229312         0
1756359/12293120        637647/3841600      2972981/28098560      104499/5619712
544743/5619712          12924421/112394240 5781469/56197120      527644501/8991539200
~~~

All entries are ≥0. Thus this K has TV≤d for **every real** a,c in the lawful square. The two lower-bound endpoints attain TV=d; hence δ₃=d.

Certificate production is finite exact rational arithmetic: evaluate each bicubic residual at a_i=c_i=1/2+i/8 for i=0..3; transform the evaluation tensor to Bernstein coefficients using the inverse collocation matrix
U=[[1,0,0,0],[-5/6,3,-3/2,1/3],[1/3,-3/2,3,-5/6],[0,0,0,1]], then split the a axis by the exact de Casteljau construction at t=4/7 (a=5/7). The attached VERIFY.py recomputes all coefficients and inequality checks using Python Fraction only. RUN_EVIDENCE.txt is actual program output. This is an exact all-real certificate, not extrapolation from a numerical grid.

## Scope and next research

This theorem resolves the auxiliary three-observation **full 27-output TV** minimax exactly and retains all 27 ordered words through an exact histogram lift. It leaves the original six-source ten-label S23 mother-protocol transfer to be proved against its pinned source and observation map. Histogram reduction here is scoped to the declared TV observer; native Heartbeat-X6 joint paths or provenance are not declared redundant. P000, ACTIVE worldview and immutable scientific source stay unchanged. Independent mathematical review, formal CLAIM and Result admission remain separate.

Next: compare the original ten-label mother experiment and this conditional AV auxiliary experiment by exact stochastic preprocessing/postprocessing maps, including source labels and three-observation dependence; prove the transferred statement or exhibit a concrete factorization obstruction.
