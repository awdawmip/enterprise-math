# EC48L — One stochastic bit preserves the entire original four-observable region at horizon two

**Date:** 2026-10-27 (Asia/Shanghai). **Role:** author-side portable TASK_RESEARCH. **Research status:** UNREVIEWED / NOT_ADMITTED; no native CLAIM or independent Driver review.

**Frozen sources:** GLOBAL_KNOWLEDGE_V1 main edbbe204c4417149655022554f50f0d0004eb179; current Enterprise Math main 7d0f1ba8f62243d01c65b630a1333e60b9f0a9c4. Read P000, the ACTIVE residual-faithful worldview, joint-relation-preservation guard, role startup, and portable research protocol. Predecessor: EC48K proof and NEXT_TASK at immutable 1fc87563493f5dc928c2a30b2992b7f21c2fad0f. This is an auxiliary two-source positive-weight BRC experiment: neither the native X6 model nor a longer-horizon conservation claim.

## Typed problem

A finite two-stage sequential experiment has first-stage histories h in H with strictly positive masses P_h,Q_h, and terminal leaves x in X_h with positive masses P_x,Q_x summing to P_h,Q_h. Both probability laws sum to 1. At time 1 an observer may stop/reject, stop/accept or continue; after continuation at time 2 it may accept/reject. Private randomization is permitted. The full-history observer F sees h,x. The B1 observer may stochastically write one policy-dependent bit b from the observed h before the first action; subsequent decisions only see (time, current joint likelihood ratio, b) and use fresh private coins. Current likelihood ratio is r_h=P_h/Q_h at time 1 and rho_x=P_x/Q_x at time 2. No persistent public seed. The target observation is O=(alpha,beta,tau_P,tau_Q), where alpha=P(accept), beta=Q(accept), tau_s=E_s[T], T in {1,2}. Denote the original attainable sets by S_F,S_B1.

## Theorem EC48L (global exact original-set equality)

**For every finite strictly positive two-source horizon-two experiment just specified, with arbitrarily many stage-one histories and likelihood-ratio collisions,**

```
S_B1 = S_F.
```

This answers EC48K's open original-region question affirmatively, not just its previously proved convex-hull support equality. The stochastic encoder may be separately chosen for each target policy.

### Constructive proof

Fix any randomized full-history policy and set t_h=Pr(continue|h), a_h=Pr(stop AND accept|h), and z_x=Pr(accept|reached x). Then 0<=a_h<=1-t_h and 0<=z_x<=1. The full readout is

```
alpha_F = sum_h P_h a_h + sum_x P_x t_{h(x)} z_x
beta_F  = sum_h Q_h a_h + sum_x Q_x t_{h(x)} z_x
tauP_F  = 1 + sum_h P_h t_h
tauQ_F  = 1 + sum_h Q_h t_h.
```

For every stage-one ratio r define the fiber H_r={h:P_h/Q_h=r} and

```
D_r=sum_{h in H_r} Q_h (1-t_h); A_r=sum_{h in H_r} Q_h a_h;
eta_r = (A_r/D_r if D_r>0 else 0).
```

For every terminal ratio rho define X_rho={x:P_x/Q_x=rho} and

```
E_rho=sum_{x in X_rho} Q_x t_{h(x)};
B_rho=sum_{x in X_rho} Q_x t_{h(x)} z_x;
theta_rho = (B_rho/E_rho if E_rho>0 else 0).
```

Both eta and theta belong to [0,1] by the action probability bounds. Write b=1 with probability t_h conditioned on the real history h, and b=0 otherwise. At time one, b=1 means continue; b=0 means stop and accept with probability eta_{r_h}. At time two the only reachable bit is b=1: accept with probability theta_{rho_x}. This is a valid B1 policy using fresh private randomness.

For each r the Q-mass of time-one acceptance equals eta_r D_r=A_r, and the P-mass equals r A_r, since P_h=r Q_h throughout H_r. For each rho the Q-mass of terminal acceptance equals theta_rho E_rho=B_rho, and the P-mass equals rho B_rho. These are exactly the two full-history accepted masses in each ratio fiber. Continuation probability t_h is unchanged for every history, so both expected stopping times also match. Hence S_F is contained in S_B1. The reverse inclusion follows because the complete observer simulates the one-bit encoder and its decoders. QED.

The calculation preserves both source laws and first-stage continuation mass before quotienting. It certifies this compression ONLY for four declared readouts and horizon two; it does not preserve all path labels or unspecified future operations. The crucial assumptions are stochastic history-dependent encoding, policy dependence, source-independent coins, and a terminal decoder allowed to see the **joint** terminal likelihood ratio.

### Worst-case sharpness: one bit is necessary in general

Take the three-terminal-leaf tree A+,A-,B with source masses
```
            A+    A-     B
P           3/8   1/8    1/2
Q           1/8   3/8    1/2
```
The two first-stage histories A,B both have ratio 1. The leaf B is a single deterministic terminal successor if continued. For J=alpha-beta-(tauP+tauQ)/8, full-history F continues only A, stops/rejects B, and accepts only A+, yielding O=(3/8,1/8,3/2,3/2), J=-1/8. This is optimal: continuing A gains P-Q acceptance contrast 1/4 and costs extra time 1/8, while continuing B gains zero contrast and costs extra time 1/8. The zero-bit current-LR-only policy must use the same continuation probability t at A and B. Its maximal terminal contrast t/4 exactly cancels time cost t/4, leaving max J_zero=-1/4. Strict gap max J_F-max J_zero=1/8. Therefore the worst-case additional memory cardinality, measured in binary bits, is exactly one for this model class.

## Exact calculation and verification

The executable verifier EC48L_VERIFY.py performs these two rational-fiber reductions and compares all four coordinates using fractions.Fraction, with no floating point or tolerance. Its actual run on 2026-10-27 checked **2401** positive models: one six-leaf collision fixture plus 2400 seeded trees (1..8 first-stage histories, 300 models per history count, 1..4 leaves each, positive integer raw P,Q weights 1..9, randomized rational actions), random seed 4848127. **0 assertion failures**. The collision fixture has

```
t=(1/4,2/3,1/2) for A,B,C;
a=(1/8,1/9,1/4);
terminal z=(0,1/2,1,1/4,1/3,2/3);
eta_1=35/114; theta_3=2/11, theta_(1/3)=19/22, theta_1=1/2;
O_F=O_B1=(305/864,395/864,53/36,53/36).
```

The universal theorem is proved by the algebra above; this finite check validates the implementation. No formal proof assistant or external independent mathematical review was run.

## Next scientific boundary

The horizon-two original-set question is closed at author-proof level. EC48M will test horizon THREE with at least one interior stage-two decision, retaining typed P/Q branch mass and two expected stopping times, and will derive a universal repair construction or a strict rational nonrealizability certificate. Separate work is needed to map any of this auxiliary observer model to native X6 heartbeat dynamics and preserve declared future operations under that map. Project canonical Result/Driver acceptance remains pending.
