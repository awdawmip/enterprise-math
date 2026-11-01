# BRC N=4 / S23: exact three-policy obstruction to a single tenth-decoder repair

Date: 2026-11-01. Author-side mathematical proof and exact Fraction computation; **UNREVIEWED / NOT_ADMITTED**. This is a finite statistical S23 model, not a native P000 dynamical theorem.

## Frozen model and quantifiers

Reuse the six latent positive BRC sources (AU0,AU1,AV,BU0,BU1,BV), prepared input mixing matrix M=M20/20,

```text
M20 = [[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
       [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]]
```

and the full six-preparation/four-stopping-time total-variation observer. A legal S23 behavior is described by (a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV) in [0,1]^11. For latent source x in first-stage group g and second-stage information set h, its stopping distribution is

F_x=(a_g,(1-a_g)b_h,(1-a_g)(1-b_h)c_x,(1-a_g)(1-b_h)(1-c_x)).

The U second-stage decision is shared by AU and BU. The prepared laws are p_i=sum_x M_ix F_x. The common deterministic k=4 encoder preserves exactly the four AU/AV/BU/BV groups. A fixed four-group stochastic decoder D induces six prepared decoded rows q_i=D_group(i). The label is chosen after the strategy, but before any stopping observation:

G_D(theta) = min_{l=1,...,10} max_{i=1,...,6} TV(p_i(theta),q_{l,i}).

Keep the **original nine** group decoders from predecessor PR #1765 unchanged, specified by uniform pairs of stopping times, in AU AV BU BV order:

```text
1=34 24 34 24    2=34 23 34 34    3=34 34 34 23
4=24 24 12 12    5=12 12 24 34    6=12 13 23 24
7=23 34 12 13    8=24 34 12 14    9=13 12 13 13
```

The tenth decoder D is now **arbitrary**, with each of its four group rows any probability vector on four times. Define three legal strategies:

* W: a_A=1, a_B=0, b_U=b_AV=0, b_BV=1, and all six c_x=0. The six prepared laws are (delta_1,delta_1,delta_1,delta_4,delta_4,delta_2).
* H: H(1/3) of PR #1765: a_A=1/3, a_B=1, all b=0, (c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)=(1,0,1,0,0,0).
* J: J(1/3) of PR #1765: a_A=1, a_B=1/3, all b=0, c_BU1=1 and all other c=0.

Direct exact evaluation of the unchanged nine decoders yields min_{l<=9} loss(W)=1 and min_{l<=9} loss(H)=min_{l<=9} loss(J)=2/3. Their BV prepared laws are, respectively, delta_2, delta_1, (delta_1+2 delta_4)/3.

## Theorem 1 — sharp three-witness obstruction

For the fixed encoder and the original nine decoders,

**inf_{arbitrary stochastic tenth D} max_{theta in {W,H,J}} G_D(theta) = 5/9.**

Proof. Let r=max_theta G_D(theta). For r>=5/9 there is nothing to show. Suppose r<5/9. The first nine decoders all have loss >=2/3 on each of W,H,J, so tenth D must achieve radius <=r on each. Write its BV row q=(q1,q2,q3,q4). Because W has BV=delta_2 and H has BV=delta_1,

q2>=1-r, q1>=1-r, and q4<=1-q1-q2<=2r-1.

Since J has BV=(1/3,0,0,2/3), the overlap identity TV(u,q)=1-sum_t min(u_t,q_t) gives

r >= TV(J_BV,q) = 1-min(1/3,q1)-min(2/3,q4)
  >= 2/3-q4 >= 5/3-2r.

Thus 3r>=5/3, or r>=5/9, contradiction. This argument covers **all real stochastic tenth decoders** without an optimization oracle.

For the matching upper bound use the explicit tenth decoder D* (AU/AV/BU/BV rows):

```text
AU = (1/2, 0,   1/4, 1/4)
AV = (1/2, 0,   1/2, 0)
BU = (4/9, 0,   1/9, 4/9)
BV = (4/9, 4/9, 0,   1/9)
```

The six rowwise TV values against D* are
W: (1/2,1/2,1/2,5/9,5/9,5/9);
H: (1/6,1/6,1/6,5/9,5/9,5/9);
J: (1/2,1/2,1/2,2/9,22/45,5/9).
Therefore each G_D*(theta)<=5/9, proving equality.

**Rigidity at the optimum.** If one tenth decoder achieves max_theta G_D(theta)<=5/9, each of W,H,J must use that tenth label (since 5/9<2/3). The first two BV constraints imply q1,q2>=4/9 and q4<=1/9. The J constraint implies q4>=1/9. Hence necessarily

**D_BV=(4/9,4/9,0,1/9)**.

Other decoder rows may not be unique.

## Theorem 2 — a forced displacement under exact grid preservation

If the unchanged nine decoders plus a tenth D satisfy both G_D(W)<=1/2 and G_D(H)<=1/2, then **G_D(J)=2/3 exactly**.

Proof. Neither W nor H can use the first nine labels at <=1/2. Their BV rows force q2>=1/2 and q1>=1/2, so nonnegativity and row sum 1 force q=(1/2,1/2,0,0). The J BV target gives TV(J_BV,q)=2/3, so the tenth label's J loss is >=2/3. The unchanged nine-label bank has a J loss exactly 2/3 (labels 6 and 9), whence G_D(J)=2/3.

W is one of the legal deterministic policies in the complete {0,1/2,1}^11 ternary grid. Consequently, **any single tenth replacement that preserves the whole ternary-grid radius <=1/2 and repairs H(1/3) to <=1/2 is forced to have J(1/3) loss exactly 2/3.** This shows that the adversarial displacement seen for the predecessor's specific repair is structurally unavoidable under these precise fixed-nine requirements. The predecessor's repaired tenth row exhibits sharpness and achieved the ternary-grid radius <=1/2 by its separately archived exact verification.

## Verification, scope, and remaining obligations

The executed `VERIFY.py` uses Python Fraction to reconstruct M, all 11 S23 controls, all nine fixed decoders, the three witnesses, and D*. It checks every nine-label risk on each witness, all 18 rowwise TV values, the sharp rational upper construction, and the BV saturation certificate. Its finite computations verify these exact values; the universal statement for arbitrary real D follows from the analytic inequalities above. No full 11D continuum or general ten-decoder optimizer was certified by this result.

BRC reuse is substantive: preserve six source provenance, the exact positive-rational mixture M, all six prepared input rows, the causal S23 branch controls, and the four-stop-time TV observer. The four group labels are statistical group states, not the six P000 native spatial axes. This result changes neither P000 nor the ACTIVE worldview.

The unrestricted optimization R_beh(k,10) for k=4 or k=6 retains the prior [1/2,2/3] interval. The stronger obstruction here applies only when the encoder and **nine existing decoders are frozen**. Independent mathematical review, S2 information-set transfer, and P000 native six-axis/time correspondence remain separate obligations.
