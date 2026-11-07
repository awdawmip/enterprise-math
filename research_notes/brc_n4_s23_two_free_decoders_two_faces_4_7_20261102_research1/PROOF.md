# Jointly free two BRC N4/S23 decoders: exact finite minimax and 4/7 continuum two-face certificate

2026-11-02. Author analytic proof and exact rational execution; UNREVIEWED / NOT_ADMITTED. Scientific input freeze: `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Direct predecessor: `@5272933b590d957eba7046d4f99afffe88b2453a`, which fixes nine decoder rows and proves exact two-face 11/18. This work retains the SAME first eight rows, but makes BOTH rows 9 and 10 free.

## Precise positive-source statistical model

Six distinct positive-rational BRC/S23 latent source labels are AU0, AU1, AV, BU0, BU1, BV (not native spatial X6 axes). With `theta=(a_A,a_B,b_U,b_AV,b_BV,c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV) in [0,1]^11`, source x has four-stop distribution
`F_x=(a_g,(1-a_g)b_h,(1-a_g)(1-b_h)c_x,(1-a_g)(1-b_h)(1-c_x))`.
The SAME b_U controls A-U and B-U. Original whole-source mixing is `M=M20/20` with
```text
M20=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).
```
All six prepared distributions `p_i(theta)=sum_x M[i,x] F_x` are retained separately. The common deterministic k=4 encoder maps the six sources to `(AU,AU,AV,BU,BU,BV)`. A decoder D has four stochastic rows AU,AV,BU,BV; `q_i(D)=sum_x M[i,x] D[group(x),:]`. A single decoder's loss is `L_D(theta)=max_{i=1..6} TV(p_i(theta),q_i(D))`, where `TV(p,q)=sum_{u=1}^4 |p_u-q_u|/2`. A bank of ten losses yields `G(theta)=min_{d=1..10} L_d(theta)`, selecting the label after theta but before observing the stop.

Freeze these first EIGHT decoder tables, where a pair ij means mass 1/2 on each indicated stop, in group order AU AV BU BV:
```text
1:34 24 34 24     2:34 23 34 34
3:34 34 34 23     4:24 24 12 12
5:12 12 24 34     6:12 13 23 24
7:23 34 12 13     8:24 34 12 14
```
Write `R_8+2(S)=inf_{D9,D10 in (Delta_4)^4} sup_{theta in S} G(theta)`, with arbitrary REAL nonnegative stochastic entries.

The lawful witnesses, in exactly the eleven-control order above, are
```text
W=(1,0,0,0,1;0,0,0,0,0,0)
H=(1/3,1,0,0,0;1,0,1,0,0,0)
J=(1,1/3,0,0,0;0,0,0,0,1,0)
P=(1,2/9,0,0,0;0,1,1,1,0,1)
T=(0,0,0,0,0;0,1,1,1,0,1).
```
The entire two legal real faces are
`O(s,t)=(s,t,0,0,0;0,1,1,1,0,1)` and
`N(s,t)=(s,t,0,0,0;1,0,0,0,0,0)`, for all real `s,t in [0,1]`. Thus `P=O(1,2/9)`, `T=O(0,0)`.

## Theorem A: exact four-witness optimum 13/27

For `S4={W,H,J,P}`, **R_8+2(S4)=13/27** over ALL REAL decoder rows. Direct computation of the fixed eight gives minimum risks W=1,H=2/3,J=2/3,P=11/18; their pure BV prepared rows are respectively `e2,e1,(e1+2e4)/3,(2e1+7e3)/9`. For any radius `r<13/27<1/2`, none of these four may use the fixed eight. As BV of W is disjointly supported from BV of H, J, P, a single decoder cannot cover W together with any H/J/P at r<1/2 (BV TV=1). The two free labels must separate W and {H,J,P}. On the latter common BV row `q=(q1,q2,q3,q4)` the three target events give `q1>=1-r`, `q4>=2/3-r`, `q3>=7/9-r`. Hence `1>=q1+q3+q4>=22/9-3r`, so `r>=13/27`, contradiction. This lower bound applies to ANY real stochastic D9,D10.

The upper construction takes D9 group rows `(e1,e1,e4,e2)` and D10 rows `(Q,Q,U,Q)` with `Q=(14/27,0,8/27,5/27)`, `U=(5/9,0,2/9,2/9)`. D9 has loss 0 on W. Direct ORIGINAL six-input prepared-mixture comparisons give six TV coordinates of D10 on H `(5/27,5/27,10/27,4/9,4/9,13/27)`, J `(13/27,13/27,13/27,2/9,17/45,13/27)`, P `(13/27,13/27,13/27,1/3,43/90,13/27)`. Thus the four-witness bank worst loss is 13/27, sharp.

## Theorem B: exact five-witness optimum 1/2

For `S5={W,H,J,P,T}`, **R_8+2(S5)=1/2**. Fixed-eight best loss at T is 1/2 and its BV preparation is e3. For a hypothetical r<1/2 all five must use new labels; W is BV-disjoint from each H,J,P,T, so the other label must cover those four. H,J,T respectively force `q1>=1-r`, `q4>=2/3-r`, `q3>=1-r`; normalization gives `1>=8/3-3r` and hence `r>=5/9>1/2`, contradiction. The SAME bank used in Theorem A covers four witnesses <=13/27, while existing fixed decoder 2 covers T exactly at 1/2. Therefore 1/2 is attained.

## Theorem C: a strict 4/7 upper certificate on BOTH FULL REAL two-dimensional faces

Set `S={W,H,J} union {O(s,t):s,t in [0,1]} union {N(s,t):s,t in [0,1]}`. The whole continuously parametrized restricted minimax satisfies

```text
           1/2 <= R_8+2(S) <= 4/7 < 11/18.
```

The lower bound follows from S5 subset S. For the upper construction retain D9=(e1,e1,e4,e2) from Theorem A, and **replace** D10 with the following different COMMON four-row stochastic decoder:

| group | stop 1 | stop 2 | stop 3 | stop 4 |
|---|---:|---:|---:|---:|
| AU | 3/7 | 2/7 | 2/7 | 0 |
| AV | 3/7 | 0 | 2/7 | 2/7 |
| BU | 3/7 | 0 | 1/35 | 19/35 |
| BV | 3/7 | 0 | 2/7 | 2/7 |

Each row is nonnegative and sums to 1; in particular the BU row sum is `3/7+1/35+19/35=1`. Exact six-preparation TV comparisons give `L_D9(W)=0` and `L_D10(H)=L_D10(J)=L_D10(P)=4/7`.

**All-real face certificate.** On either O or N, A prepared rows i=1,2,3 depend affinely ONLY on s, and B rows i=4,5,6 affinely ONLY on t. This is a consequence of the fixed source laws, shared original causal controls and zero A/B cross-block weights in M20. For ANY fixed decoder row bank, `TV(p_i,q_i)<=r` is equivalent to **all 16** signed inequalities

```text
sum_{u=1}^4 sigma_u (p_i(s,t)_u - q_i,u) <= 2r,
       sigma in {-1,+1}^4.
```

For the three A rows they constrain s to one exact closed interval; for the three B rows they constrain t to another. Therefore the full six-row `L_D<=r` region for a given face and label is precisely a Cartesian product of closed intervals, possibly empty. Intersecting all signed halfspaces with r=4/7 gives these **exact** label sublevel rectangles:

| face | label | s range | t range |
|---|---:|---|---|
| O | 2 | [0,4/7] | [0,4/7] |
| O | 7 | [0,1/7] | [3/7,1] |
| O | 5 | [3/7,1] | [0,1/7] |
| O | 10 | [1/7,1] | [1/7,1] |
| N | 1 | [0,4/7] | [0,4/7] |
| N | 4 | [0,1/7] | [3/7,1] |
| N | 5 | [3/7,1] | [0,4/7] |
| N | 10 | [1/7,1] | [1/7,1] |

These four rectangles cover every real pair in [0,1]^2 on EACH face: when s<=1/7, the low-left label plus the left-high label cover all t since [0,4/7] overlaps [3/7,1]. When s>=1/7 and t>=1/7, label 10 applies. In the remaining region s>=1/7 and t<=1/7, the low-left label reaches s=4/7 while label 5 begins at s=3/7. All boundaries are closed. Therefore the entire S is covered at radius 4/7, proving the universal real-face upper bound.

The four rectangles were calculated by **all 16 TV-sign inequalities for each of all six original four-stop prepared rows** in the exact verifier, rather than optimizing each latent source separately. The checker additionally confirms decoder 10's four corners of [1/7,1]^2 on BOTH faces, enumerates each face's full nonempty label rectangles and confirms exact coverage of 20 open partition cells; closure then covers every cut boundary. The analytic affine/rectangle argument is load-bearing for the continuum conclusion. Four- and five-witness exact values are universal in all real stochastic decoder rows because of the BV-event lower certificates.

**Strict improvement with source fidelity.** The predecessor held the first NINE decoder kernels fixed and established sharp 11/18 for the SAME S; freeing precisely decoder 9 as well as decoder 10 gives explicit 4/7 on the TWO complete real faces, a gain `11/18-4/7=5/126`. This is a scoped constructive result: the exact full-face redesigned-two-rows minimax remains in [1/2,4/7]. The unrestricted 11-control ten-label behavior minimax remains bounded [1/2,2/3] for k=4,6; our two-face bank is not asserted to cover all [0,1]^11. Source identifiers are BRC finite statistics, not native P000 six-axis Cell identities or independent time; native/future-operation fidelity remains separate.

**Evidence and next question.** `VERIFY.py` was actually executed with Python standard-library exact Fraction arithmetic on the original six mixed four-stop laws. It validates all witness risks, dual constants, stochastic normalization, 16-sign affine intersections, explicit intervals and full two-face rectangle partitions. `RUN_EVIDENCE.json` is captured stdout. Next optimize the same two free decoders below 4/7, or prove an improved >=1/2 lower bound by new lawful witnesses and a certified dual; a full eleven-dimensional multiaffine partition will be needed for any global upper-bound advance. All mathematical conclusions here are author-verified and await independent review and native admission.