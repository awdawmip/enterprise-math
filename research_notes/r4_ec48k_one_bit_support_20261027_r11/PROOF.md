# EC48K | One bit preserves every linear support of the horizon-two four-observable BRC region

**Date:** 2026-10-27 (Asia/Shanghai). **Author-side identity:** EM-R004-K7E48K, TASK_RESEARCH, locally allocated for this automation conversation. **Activity:** RA-EMR4-20261027-R11-1727-BIT-HULL. **Status:** UNREVIEWED / NOT_ADMITTED; no Source CLAIM, native Result, or independent Driver review.

**Global rules frozen for this run:** GLOBAL_KNOWLEDGE_V1 main `fdb6b0aff365cc24c392c253031d9b601793889a`; P000_STARTUP projection SHA `c6d4d2d79b09537bdae55253baef9c28583e44dc` validated against original P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. **Enterprise Math reading pin:** main `356319bdfd0839249f6a867e1c7d304dccba3051`. **Direct predecessor:** EC48J author-side proof `bcc78048736a01f6d07850d3adc0b998f47f76a0:research_notes/r4_horizon2_threeleaf_20261027_t11/PROOF.md`.

## 1. Precisely typed experiment and observer

Take two strictly positive probability laws P,Q on the same finite horizon-two rooted tree. At the first observation each history h has positive marginal P_h and Q_h; after continuation it has finitely many terminal leaves x with P_x,Q_x>0 and sum_{x below h} P_x=P_h, likewise Q. The current likelihood ratio P_h/Q_h is available at stage 1; P_x/Q_x is available at stage 2.

The observer may stop at stage 1 and accept/reject, or continue, then accept/reject at stage 2. Private randomization independent of source is allowed. The complete-history observer F uses h at stage 1 and x at stage 2. Observer B1 may write a **policy-dependent** bit b(h) from the full observed h *before* stage-1 stopping, and at each stage acts using only (current stage, current likelihood ratio, b) and local randomness. The bit is retained until the end. A new policy may choose a new encoder b(h). There is no persistent externally shared random seed. The observation is the four-vector O=(alpha=P[accept], beta=Q[accept], tauP=E_P[T], tauQ=E_Q[T]). Let S_F,S_B1 denote their original sets. B1 can be simulated by F.

This is a positive-mass BRC branching-carrier and observer/fiber theorem in an **auxiliary two-source decision model**. P and Q masses are preserved separately; signed linear functionals below act only on output observations, not on primitive positive branch weights. It is not an X6 dynamics, 3D-slice, BRC-Shor or physical theorem. The future-operation horizon is exactly two observations.

## 2. Theorem (universal two-stage one-bit support sufficiency)

**For every such finite positive two-source horizon-two tree with arbitrarily many first-stage histories,**

```
for all w=(a,b,c,d) in R^4:
  sup_{O in S_B1} (a alpha+b beta+c tauP+d tauQ)
    = sup_{O in S_F} (a alpha+b beta+c tauP+d tauQ).
```

Consequently **conv(S_B1)=conv(S_F)**, where conv denotes the usual convex hull in R^4. No number of colliding first-stage histories yields a strict *linear-support* obstruction to one writable policy-dependent bit under the declared model.

**Proof.** Fix w=(a,b,c,d). If terminal leaf x is reached, the best terminal accept/reject contribution is max(0,a P_x+b Q_x). It is achieved by the current-LR test: accept if a (P_x/Q_x)+b>0, reject if negative (ties arbitrary). This terminal decoder is the **same across all first-stage histories and independent of the bit**.

At stage 1 history h, write C_h=c P_h+d Q_h. If stopping, the optimized source-weighted contribution is

```
S_h = C_h + max(0,a P_h+b Q_h).
```

The optimal stop acceptance action is again a current-LR test. If continuing, the optimized contribution is

```
D_h = 2 C_h + sum_{x below h} max(0,a P_x+b Q_x).
```

Bellman separation over the finite first-stage histories gives the full-history linear optimum

```
V_F(w) = sum_h max(S_h,D_h).
```

Construct one B1 policy as follows. Write b(h)=1 exactly when D_h>S_h (choose either bit in a tie). The time-1 decoder continues iff b=1. If b=0 it stops, and accepts iff a (P_h/Q_h)+b>0 (here the symbol b in the formula is the **second component of w**, not the memory bit). At time 2 it uses the terminal likelihood-ratio sign test irrespective of memory. All choices are deterministic, source-independent rules fixed as part of this one policy. The resulting support value is exactly sum_h max(S_h,D_h). Thus V_B1>=V_F; the reverse inequality follows because F simulates B1. Compactness and the supporting-hyperplane characterization of closed convex sets in finite dimension imply equality of the convex hulls. QED.

The construction is valid with unequal stage-1 likelihood ratios, arbitrary collisions, any number of leaves, and either sign of time coefficients c,d. Strict positivity makes the ratio tests defined. Policy dependence of b(h) is essential; the theorem does not say **one universal encoder** works for all w. It also does not prove original nonconvex set equality S_B1=S_F.

## 3. Exact three-history rational witness and controlled search

Let first-stage H={A,B,C}, each with P_h=Q_h=1/3. Every h has two positive terminal leaves, with ordered leaf P,Q masses

```
x          A+   A-   B+   B-   C+   C-
12 P_x      3    1    1    3    2    2
12 Q_x      1    3    3    1    2    2
ratio       3   1/3  1/3   3    1    1
```

For J=alpha-beta-(tauP+tauQ)/16, the full and one-bit optimum is **1/8**. A maximizing B1 policy writes bit 1 at A and B (continue), bit 0 at C (stop/reject); stage 2 accepts exactly leaves with current likelihood ratio 3. It has the exact four-vector O=(1/2,1/6,5/3,5/3). The zero-bit current-LR-only observer must stop or continue all histories at stage 1 because their current ratios coincide; its maximum is **1/12** (continue all). The bit's strict linear-support improvement over zero bit is **1/24**.

The attached self-contained JavaScript checker uses integer masses with common denominator 12 and integer coefficients. It enumerates all 3^3*2^6=1,728 deterministic full policies in this six-leaf tree, evaluates **226** explicitly declared integral four-vectors w, and checks each full brute-force maximum against the constructive B1 Bellman maximum. It verifies the exact witness readout, value and LR-only maximum. Integer evaluation is exact and has no rounding or numerical tolerance. The 226 tests check the code and fixture; the unrestricted finite-tree theorem follows from the proof above.

## 4. Frontier and limits

This answers the **linear separating-support branch** of EC48K: no such separator can exist for one bit in the stated horizon-two model, regardless of the number of first-stage histories. The original-region problem is separate: the existence, or absence, of a genuinely nonconvex full-history point outside S_B1 has not been established here. To test original membership, a fixed four-vector target must be matched by a policy-dependent stochastic encoder and two decoder rows, including stage-1 stop/accept/continue rates and terminal LR-fiber acceptance; matching all linear support values alone is insufficient.

Claims are author-side; no formal proof assistant, independent math review, native X6 transfer or original-set equality is asserted. The existing current project owner/CLAIM is unaffected.
