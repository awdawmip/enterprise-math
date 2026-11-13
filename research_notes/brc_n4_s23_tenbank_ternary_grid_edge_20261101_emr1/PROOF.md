# BRC N4 / S23: a complete ternary-grid false certificate and exact interior adversarial edge

Date: 2026-11-01. Author-side **analytic proof** (one full behavioral-policy edge) and **exact finite exhaustive certificate** (one entire 11-parameter grid). Status: UNREVIEWED / NOT_ADMITTED. Neither native P000 dynamics nor the unrestricted ten-label minimax is claimed.

## Frozen experimental information structure

Latent BRC cells in order AU0, AU1, AV, BU0, BU1, BV; the six positive prepared P/Q mixtures are rows of

```
M=(1/20)*[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],
          [0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].
```

A lawful S23 behavioral strategy has two first-stage stop probabilities a_A,a_B, three second-stage stop probabilities b_U,b_AV,b_BV (the U information set is shared between AU and BU), and six terminal source-stop probabilities c_x. All belong to [0,1]. For source x, with g(x)=A or B and h(x)=U,AV,BV, its **four-time** law is exactly

```
F_x(theta) = (a_g, (1-a_g)*b_h, (1-a_g)*(1-b_h)*c_x,
                         (1-a_g)*(1-b_h)*(1-c_x)).
```

For each of the six prepared rows p_i(theta)=(M F(theta))_i. Fix the deterministic **four-group encoder** E encoding AU/AV/BU/BV. Fix the previous certified **ten uniform-pair decoders**, one label for each box (coordinate order AU AV BU BV):

```
1: 34 24 34 24      2: 34 23 34 34      3: 34 34 34 23
4: 24 24 12 12      5: 12 12 24 34      6: 12 13 23 24
7: 23 34 12 13      8: 24 34 12 14      9: 13 12 13 13
10:12 12 14 12
```

A group outputs probability 1/2 on each of its two listed times. Let

```
L_l(theta)=max_(i=1,...,6) TV(p_i(theta),(M E D_l)_i),
G(theta)=min_(l=1,...,10) L_l(theta).
```

Labels depend on the full policy theta, but the **decoder kernels do not**. This is a fixed-bank statement, not an optimization over alternative banks.

## Theorem A: the entire ternary 11-cube passes the 1/2 test

For every one of the **3^11 = 177147** lawful S23 behavioral strategies with all eleven stop parameters in {0,1/2,1},

```
G(theta) <= 1/2.
```

Exactly **169441** of these strategies have G(theta)=1/2 and **7706** have G(theta)<1/2. The grid maximum is exactly 1/2.

**Certificate semantics:** VERIFY.js evaluates every base-3 policy index 0,...,177146 with integer arithmetic only. The exact latent law has denominator 8, the prepared mixture denominator 160, and the uniform-pair decoder denominator 160. Each of all ten six-row total-variation losses is exactly an integer sum of absolute differences divided by 320. The script checks every policy, the maximum and both multiplicities; no sampling or floating-point tolerance is used. VERIFY_INDEPENDENT.py independently checks the same complete grid using NumPy signed integers and batched matrix multiplication rather than the JS per-row recurrence. The observed output of both actual executions is included in RUN_EVIDENCE.txt. The claim is **finite exhaustive**, not a statement about all real-valued strategies.

## Theorem B: an analytically exact full-continuum edge invalidates the grid certificate

Consider the following admissible, one-parameter behavioral family H(t), for every real t in [0,1]:

```
a_A=t, a_B=1, (b_U,b_AV,b_BV)=(0,0,0);
(c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)=(1,0,1,0,0,0).
```

B always stops at time 1. The A source laws are AU0=AV=(t,0,1-t,0) and AU1=(t,0,0,1-t). Accordingly the six prepared laws are

```
AU Q = (t,0,(1-t)/2,(1-t)/2)
AU P = (t,0,9(1-t)/20,11(1-t)/20)
AV   = (t,0,1-t,0)
BU Q = BU P = BV = (1,0,0,0).
```

For the above **same fixed ten kernels**, exact total-variation losses on H(t) are

```
L_1(t)=...=L_6(t)=1,
L_7(t)=(11+9t)/20,
L_8(t)=(1+t)/2,
L_9(t)=L_10(t)=max(1-t,1/2).
```

**Proof of these identities.** Labels 1-6 have a prepared row with disjoint support from its decoder: for 1-3 and 5-6 one B row has a pair excluding time 1; for label 4 the AV decoder pair 24 excludes AV's whole {1,3} support. For label 7, AU P's only overlapping atom is time 3, of mass 9(1-t)/20, so TV=1-9(1-t)/20=(11+9t)/20; all its remaining rows have no larger loss. For label 8, AU Q's only overlapping atom is time 4, of mass (1-t)/2, so TV=(1+t)/2; all remaining rows have no larger loss. For labels 9 and 10, AV's only overlapping atom is time 1, whose overlap is min(t,1/2), so TV=1-min(t,1/2)=max(1-t,1/2); all other rows have no larger loss. These comparisons are exact for every real t between 0 and 1.

Since L_7(t)-L_8(t)=(1-t)/20>=0, taking the minimum proves the **exact edge envelope**

```
G(H(t)) = min{(1+t)/2, max{1-t,1/2}}
        = { (1+t)/2, 0<=t<=1/3;
            1-t,     1/3<=t<=1/2;
            1/2,     1/2<=t<=1 }.
```

It has a unique maximum **2/3**, achieved at **t=1/3**. But at the three values t=0,1/2,1 tested by the entire ternary grid the risk is exactly 1/2. For t=1/3 the ten label risks are (1,1,1,1,1,1,7/10,2/3,2/3,2/3). The rational witness was known from the predecessor as a failure of these particular kernels; the **new facts** proved here are its entire analytic risk profile and the surprising simultaneous passing of all 177147 binary/half-step grid policies.

## Why this matters for m=10

A complete `{0,1/2,1}^{11}` grid test can falsely suggest a fixed ten-label decoder bank covers the full behavioral strategy family at radius 1/2. The failure occurs at an interior point where the **min over fixed labels** switches between distinct active affine loss functions. Corner convexification valid for full-policy-visible decoders does not apply to a fixed finite bank. Any proposed full-m10 upper bound therefore needs continuous validity (analytic inequalities, an exact adversarial separation oracle, or error-certified discretization), not just corners or a half-step grid.

This result neither proves nor disproves the unrestricted optimal ten-label error `R_beh(k,10)` (still bounded by 1/2 and 2/3 for k>=4). It proves a **bank-specific, exact countercertificate and adversarial diagnostic**. The six latent statistical cells are not native P000 X6 axes, and four abstract stopping times are not a calibrated native time coordinate. S2 causal transfer and native X6 relation/time fidelity are separate obligations. BRC use preserves positive source provenance and the joint observer; differences are only external TV-comparison differences.

## Provenance and validation scope

Frozen account normative snapshot GLOBAL_KNOWLEDGE_V1 `main@75711f73714b2cebf8a177ec4ec53912e23acffc`; project `main@ac48238d40c28c9ad139faa5b0e11cb7defdd8f9`. Read 00_BOOTSTRAP.md, OPERATING_MANUAL.md, P000 V5, ACTIVE worldview, joint-relation preservation and portable research protocol. Inputs: preceding ten boxes and six-source M at [PR #1757](https://github.com/awdawmip/enterprise-math/pull/1757), immutable proofs `6a78eef5487058815d600ae2b53c3f52d957c1aa` and `063c8e1f35c95a1644c55f28ca42b35b67a1b9da`; initial m=1..3 plateau at [PR #1763](https://github.com/awdawmip/enterprise-math/pull/1763), `0fd66ceeb7db5ede45232876951e3842da3c077b`.

The independent JS integer exhaustive run and the Python NumPy integer matrix run both passed the 177147-grid criterion. JS additionally checked the **ten individual analytic edge formulas** for 121 rational points t=n/120 and the t=1/3 sharp witness; the continuum theorem follows from the exact formulas above, **not** from those 121 finite points. Author-side / UNREVIEWED / NOT_ADMITTED; project-native Owner/CLAIM/Result or independent review not inferred from GitHub storage.

