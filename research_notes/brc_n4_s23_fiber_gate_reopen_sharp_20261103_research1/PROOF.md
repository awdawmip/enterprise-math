# BRC N4/S23 — one-step reopening of a four-dimensional observation fiber

Date: 2026-11-03 (Asia/Shanghai). Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Exact prior fiber theorem: 6c2368ce2c205fde60263f1671c694591c7dacb6:research_notes/brc_n4_s23_complete_observer_fiber_stratification_20261103_research1/PROOF.md.

## Exact six-source causal input and future operation

There are six retained labeled preparations and four outcomes, with shared z0,...,z10 in [0,1]. Use arrays A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10), original mixer M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)) and branch row R(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)). The labeled mixed outputs are P_i(z)=sum_j M[i,j]*R(z[A_j],z[B_j],z[C_j])/20.

The predecessor proves that every h=(h5,h6,h8,h9) in [0,1]^4 gives the *same* current observation at z(h)=(1/3,5/6,1,1/2,1/2;h5,h6,1,h8,h9,1/3). Define a **declared algebraic future operation** U_beta that replaces the common gate z2=1 with beta in [0,1] while leaving the remaining parameters and all source labels unchanged. Write P^beta(h)=P(U_beta(z(h))) and d_beta(h,g)=max_i TV(P_i^beta(h),P_i^beta(g)), where TV is half the outcome-wise L1 distance.

## Theorem: sharp exact stability on the entire real four-cube

For all h,g in [0,1]^4 and beta in [0,1], with delta=h-g,

~~~text
d_beta(h,g)=(1-beta) ||T delta||_infinity,

T = [[1/3,1/3,0,0],
     [3/10,11/30,0,0],
     [0,0,1/12,1/12],
     [0,0,1/60,3/20]].

(2/63)(1-beta)||delta||_infinity <= d_beta(h,g)
                                   <= (2/3)(1-beta)||delta||_infinity.
~~~

Both constants are attained by legal parameter pairs, hence sharp. At beta=1 the full four-dimensional fiber is invisible. At every beta<1 the future observer is injective, its four scalar outcome-2 measurements have rank four, and its infinity-operator condition number is 21.

**Proof.** The only raw rows involving h are R0,R1,R3,R4. In R0,R1 the first two outcome probabilities are (1/3,(2/3)beta), and the final pair is (2/3)(1-beta)(h5 or h6,1-h5 or 1-h6). In R3,R4 the first two outcomes are (5/6,(1/6)beta), and the final pair is (1/6)(1-beta)(h8 or h9,1-h8 or 1-h9). The two remaining raw rows are h-independent. Consequently, each mixed-source difference has form (0,0,y_i,-y_i), with

~~~text
y0=(1-beta)(delta5+delta6)/3;
y1=(1-beta)(9 delta5+11 delta6)/30;
y2=0;
y3=(1-beta)(delta8+delta9)/12;
y4=(1-beta)(delta8+9 delta9)/60;
y5=0.
~~~

The TV norm of (0,0,y,-y) is |y|; thus the displayed T identity holds for every real parameter. The exact inverse of T is

~~~text
T^(-1) = [[33/2,-15,0,0],[-27/2,15,0,0],
          [0,0,27/2,-15/2],[0,0,-3/2,15/2]].
~~~

The maximal absolute row sums give ||T||_infinity=2/3, ||T^(-1)||_infinity=63/2. The norm inequalities follow and the matrix has rank four. The upper constant is attained by h=(1,1,0,0), g=(0,0,0,0). The lower constant is attained by h=(1,0,0,0), g=(0,19/21,0,0), whose delta has norm one and T delta=(2/63,-2/63,0,0). All these points belong to the complete allowed real four-cube. QED.

## One-operation future-observer sufficiency and quantitative singularity

The current observation P^1 is constant on this fiber, but one future operation U_beta for any beta<1 distinguishes **every** pair h!=g. Any representation that permits exact reconstruction of both P^1 and P^beta must be injective on this fiber; otherwise it would identify two different h with distinct future readouts. Four outcome-2 source entries (labels 0,1,3,4) provide an invertible affine chart: divide their differences by (1-beta) and apply the displayed inverse. The sharp inverse sensitivity is 63/[2(1-beta)], diverging as beta approaches 1. The original mixing determinant is 1/50, so the four hidden degrees of freedom arise from the closed causal gate, rather than rank loss from source mixing.

This is a precise observer/future-operation-scoped structural residual: risk-only erasure is valid for the present observation and unsafe for this one-step future observer. The operation U_beta is an algebraic parameter replacement in the frozen positive-probability model; no native Heartbeat physical evolution, π/trigonometric computation or BRC-Shor performance is claimed. All original source and branch provenance remains explicit.

## Verification, evidence and open work

The accompanying actually executed Python stdlib Fraction checker reconstructs all six original source-mixed four-outcome distributions; checks 81 rational points in the closed-gate fiber, 81 legal points at each of five gate settings, 1280 exact corner pairs, sharp extremizers, total variation formulas and inverse reconstructions. RUN_EVIDENCE.json records the real execution marker. The all-real theorem is the symbolic derivation above, not finite sampling.

Next: For the predecessor's 32 upstream-degeneration signatures, derive an exact minimal finite menu of allowed gate replacements that distinguishes every hidden coordinate. Calculate observer rank and sharp inverse sensitivity on each stratum, and specify the operations for which a proposed quotient is safe. Continue the separate frozen S18/J/F5/C6 decoding minimax using full source-labeled observations.
