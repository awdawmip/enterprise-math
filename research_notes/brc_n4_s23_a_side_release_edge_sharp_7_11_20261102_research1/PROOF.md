# BRC S23 — exact A-side release edge at 7/11 for the pinned ten-decoder bank

**Date:** 2026-11-02. **Category:** author-side mathematical theorem with exact rational executable evidence; UNREVIEWED / NOT_ADMITTED. **Frozen scientific input:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Concrete decoder-bank source:** `57a6db1d81068504cca2b3a6ea809a63555473d6`. **Direct scientific predecessor:** `c02114d77f9686730566fee07ea7b654acd171c0`. GitHub author is not asserted to hold a native execution session or CLAIM.

## New exact theorem and domain

In the original six-source, shared-causal BRC S23 model, retain the specific seven fixed decoders D1,D2,D3,D4,D6,D7,D8 and three rational kernels K1_old,K2_old,K3_repair from the decoder-bank pin. Write
[
z=(z_0,z_1,z_2,z_3,z_4;z_5,z_6,z_7,z_8,z_9,z_{10}).
]
Define the legal A-side release edge
[
Z(t)=(1/5,1/3,t,0,0;1,1,0,1/5,1,0),quad tin[0,1].
]
For a decoder D, (L_D(z)) is the maximum total variation over six separately labeled observed preparation sources, and (m_{mathcal B}(z)=min_{Dinmathcal B}L_D(z)). Then
[
oxed{max_{0le tle1}m_{mathcal B}(Z(t))=rac7{11}},
qquadoxed{argmax_{tin[0,1]}m_{mathcal B}(Z(t))={5/11}}.
]
The new rational adversary is
[
W_7=(1/5,1/3,5/11,0,0;1,1,0,1/5,1,0).
]
Its ten risks in the bank order are exactly
[
(7/11,1,1,2/3,4/5,2/3,7/11,526/825,7/11,4/5).
]
Every entry is at least 7/11, establishing the lower bound. The previous witness (W_6=Z(9/20)) has bank risk (19/30). The strict increase on this *specific fixed decoder bank* is
[
7/11-19/30=oxed{1/330}.
]

## Six-source law and entire real-parameter proof

The same frozen model uses indexed source parameters
[
A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10),G=(0,0,1,2,2,3)
]
and nonuniform source mixing
[
M=egin{pmatrix}
10&10&0&0&0&0\9&11&0&0&0&0\0&0&20&0&0&0\
0&0&0&10&10&0\0&0&0&2&18&0\0&0&0&0&0&20
end{pmatrix}.
]
For the i-th raw source, with (x=z_{A_i}, b=z_{B_i}, c=z_{C_i}), retain
[
R_i=(x,(1-x)b,(1-x)(1-b)c,(1-x)(1-b)(1-c)).
]
The actual six labeled observation rows are (P(z)=(M/20)R(z)). The observed decoder rows are (Q(D)=(M/20)(D_{G_i,*})_{i=0}^5), and
[
L_D(z)=max_{0le i<6}rac12sum_{j=0}^3|P_{ij}(z)-Q_{ij}(D)|.
]
Throughout the stated edge, each (P_{ij}(Z(t))) is affine in t. Therefore (L_D(Z(t))) is convex for every fixed decoder D.

The exact rational endpoint evaluations are
[
L_{D1}(Z(0))=1/2,quad L_{D1}(Z(5/11))=7/11,
]
[
L_{D8}(Z(5/11))=7/11,quad L_{D8}(Z(1))=1/2.
]
Use the D1 convex chord on ([0,5/11]) and D8 convex chord on ([5/11,1]). For every real t,
[
m_{mathcal B}(Z(t))le
egin{cases}
1/2+3t/10,&0le tle5/11,\
3/4-t/4,&5/11le tle1.
end{cases}
]
Each piece is strictly below 7/11 except at its common endpoint (t=5/11). Combined with the exact witness vector this proves the maximum and its uniqueness for *all real t*. No finite sampling is used as a continuum argument.

## Robustness beyond a single witness

Every causal row is a three-stage probability law, and each global parameter occurs at most once within a given raw source row. Changing one global coordinate (z_j) by (delta) changes that raw probability row by TV at most (|delta|); the nonnegative, row-stochastic (M/20) cannot amplify this TV bound. By replacing coordinates one at a time, for any two valid global policies (z,win[0,1]^{11}),
[
|m_{mathcal B}(z)-m_{mathcal B}(w)|lesum_{j=0}^{10}|z_j-w_j|.
]
Consequently the entire relative open neighborhood
[
sum_{j=0}^{10}|z_j-(W_7)_j|<1/330
]
has (m_{mathcal B}(z)>19/30). In the full eleven-parameter cube this neighborhood has positive Lebesgue volume, even though W7 lies on some boundary faces. This exact robustness bound reuses the labeled source structure.

## Reproducibility and scope

Run `node VERIFY.js > RUN_EVIDENCE.recomputed.json` with Node.js supporting BigInt. The script constructs the seven deterministic half-half kernels and all three rational stochastic kernels, checks row normalization, reconstructs the original source and mixing maps, computes four endpoint risks and the full ten-risk witness vector using reduced exact BigInt fractions, checks the predecessor witness and an exact affine identity at t=1/4, and emits JSON. The endpoint convexity argument above is the complete symbolic continuum proof. The script does not enumerate the full eleven-dimensional problem.

For the larger *reoptimized* union (mathcal S_{18}cup J([0,1])cup F_5([0,1]^5)cupmathcal C_6cup Z([0,1])), the previous author-side universal lower bound 3/5 remains; the pinned bank gives upper bound 7/11. Hence the currently supported author-side interval is ([3/5,7/11]). No claim is made that 7/11 is optimal after redesigning the three free kernels.

**BRC interface:** the full labeled six-row probability carrier is preserved, TV is the declared observer, and arbitrary-rational decoder kernels are readouts on a common shared causal source law. No source identity, branch provenance, or observer row is collapsed.
