# Exact full-history witness and independent execution

Read-input global commit 67ddeba77aec9bff05039175463bda1af1397f73; EM  e8992339dbbb511df56bf9a22f5095fd6ea1e123.

For the safe-region example in PROOF.md, use:
root (stop P,stop Q,continue)=(1/15,2/15,4/5).
At time 1: h=a (1/4,1/8,5/8); h=b (1/6,1/3,1/2).
At time 2 action triples:
a,r=1/2 (1/2,1/4,1/4);
a,r=1 (1/3,1/6,1/2);
a,r=3/2 (1/4,1/4,1/2);
b,r=1/2 (1/5,2/5,2/5);
b,r=1 (1/4,1/2,1/4);
b,r=3/2 (1/3,1/3,1/3).
At time 3, probability of declaring Q by r order (1/2,1,3/2), terminal Y order (1/4,1,2):
h=a: (1/3,1/2,2/3), (1/4,1/3,1/2), (1/5,2/5,3/5).
h=b: (2/3,1/3,1/4), (3/4,1/2,1/3), (4/5,3/5,2/5).

Original ordered-history Q mass: root.continue * 1/2 * action1(h).continue * q_h(r) * action2(h,r).continue * mu_r(y).
The corresponding P mass at each terminal history equals y times its Q mass. Stopped errors at each earlier state use Q mass and the current LR multiplier. Sum these to obtain exactly:
O_raw=(429887/806400,378989/806400,13733/9600,20519/14400).

Actual executed author script: a separate Python Fraction ordered-history loop and 21-variable rational feasibility system, with scipy linprog used only to select a sparse support and sympy rational elimination to recover exact masses. All original constraints and a separate induced-policy stage-by-stage computation were then checked with Fraction. Local author stdout reports EXACT_PASS; this note preserves the input policy and the full 12-mass exact certificate; the portable certificate verifier requires no scipy/sympy. Remote GitHub storage by itself is not remote code execution. 
