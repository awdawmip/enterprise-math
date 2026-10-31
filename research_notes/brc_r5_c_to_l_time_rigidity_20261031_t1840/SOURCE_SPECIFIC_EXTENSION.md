# R5 source-specific C→L compensation — exact ALL-SIGNED two-time hull classification

Date: 2026-10-31. Status **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. This is an exact auxiliary finite positive Q/P model, not an accepted native X6 theorem. Input pins and complete baseline model are in sibling RESEARCH.md, frozen at GLOBAL_KNOWLEDGE_V1 `main@e848bbb6de55e7e9c21057a9ce92f7a66f70d503`, Enterprise Math `main@6c20d83d79d260c09b24824cadbf65dedeaf8e5e`.

## Model and universal theorem

Retain the origin-labelled two-law stopping model A→(D,C,Y)→L defined in sibling RESEARCH.md, with `alpha_i∈(0,1/2)`. Replace the origin-independent natural C absorbing/pass split with **source-specific** Q/P natural probabilities `(1−kappa_i,kappa_i)`, `kappa_i∈(0,1)`. Both origins have prior 1/2 under Q/P; at C and common L the likelihood ratio remains 1. C has no agent action; FULL can condition A,D,Y,L behaviour on hidden origin and path, whereas seedless LR shares behaviour at each (time,LR) key. All positive natural P/Q paths are normalized by the likelihood-moment identity. Errors are arbitrary admissible terminal response probabilities and do not alter the time observer.

Define the positive **source compensation parameter**
```
theta_i = [1 + kappa_i*(1−2*alpha_i)] / alpha_i
        = (1+kappa_i)/alpha_i − 2*kappa_i.
```

**For all real alpha_0,alpha_1∈(0,1/2), kappa_0,kappa_1∈(0,1):**
```
conv{(T_P,T_Q) of all FULL real behavioural policies}
  = conv{(T_P,T_Q) of all seedless-LR real behavioural policies}
iff theta_0 = theta_1.
```
Moreover if theta_0=theta_1, the two **actual real behavioural two-time observation sets coincide**, and their common set is a compact convex flow polytope. For theta_0≠theta_1, take `t=(theta_0+theta_1)/2` and
```
H_t = 2*(t+1)*T_P − (2*t+3)*T_Q.
Delta_Ht = min(alpha_0,alpha_1)*abs(theta_0−theta_1)/4 >0.
```
A FULL deterministic witness is at L-infinity distance at least `Delta_Ht/(4*t+5)` from the entire LR **time** hull, and therefore from the entire four-observer LR hull by time projection. This is a complete all-signed time classification, not a four-coordinate mother-theorem claim.

## Exact Bellman proof in EVERY signed time direction

For arbitrary `H=u*T_P+v*T_Q`, let `w_lambda=u*lambda+v`, `w=w_1`. The optimized reward per unit entering L is `ell=max(3*w,4*w)`. Source-independent D and Y conditional optimal rewards are
```
d = max( 2*w_(1/2), 2*w_(1/4)+ell/3 ),
y = max( 2*w_(3/2), (3/2)*w_2+ell/2 ).
```
Source i's C natural reward is `c_i=2*w+kappa_i*(ell−2*w)`; A STOP reward is w. The source-conditional optimal advantage of A CONTINUE is
```
D_i = alpha_i*d+(1−2*alpha_i)*c_i+alpha_i*y−w
    = w + alpha_i*(d+y−4*w)
      + kappa_i*(1−2*alpha_i)*(ell−2*w).
```
The lower optimal D,Y,L actions are source-independent and can be shared by LR without losing support. Only A has different source-conditional advantages. Hence
```
sup_FULL H = w+(max(0,D_0)+max(0,D_1))/2,
sup_LR H   = w+max(0,(D_0+D_1)/2),
Delta_H    = (|D_0|+|D_1|−|D_0+D_1|)/4.
```
All extrema for real behavioural policies occur at deterministic controls because policy key decisions are never revisited along a path. The gap is positive precisely when D_0 and D_1 have opposite strict signs.

If `w<0`, L STOP is optimal, so `ell=3w`, `ell−2w=w`, giving the exact factorization
```
D_i=alpha_i * [ (d+y−4*w)+theta_i*w ].
```
Thus theta_0=theta_1 forces D_0,D_1 to share sign in *every* such direction.

If `w>=0`, the admissible continuation policy STOP at D,Y and CONTINUE at L has source-conditional A continuation value `2w+2kappa_i(1−2alpha_i)w` because `w_(1/2)+w_(3/2)=2w`. Thus even its advantage over A STOP equals `w[1+2kappa_i(1−2alpha_i)]>=0`. Both optimal D_i are nonnegative, irrespective of theta. Therefore theta equality forces zero support gap in every signed direction, and equality of both compact two-time convex hulls.

Conversely if theta_0≠theta_1, choose `t=(theta_0+theta_1)/2>0`, `u=2(t+1)`, `v=−(2t+3)`. Then `w_1=−1`, `w_(1/2)=−(t+2)<0`, `w_(3/2)=t>0`. Consequently L and D STOP, Y CONTINUES, and `d+y−4w=t`. Therefore `D_i=alpha_i*(t−theta_i)`; the two signs are opposite. Direct substitution into the exact absolute-value gap yields
`Delta_Ht=min(alpha_0,alpha_1)*|theta_0−theta_1|/4`.
Finally `|u|+|v|=4t+5`; dual Hölder gives the stated L-infinity distance bound. This proves the complete all-real convex-hull classification.

## Why the ACTUAL real two-time images coincide on the compensation surface

For a seedless LR policy, A's continuation probability is common to both origins. The aggregated Q key-time process is exactly a finite single-source effective model with
```
s=(alpha_0+alpha_1)/2,
m=[(1−2alpha_0)*kappa_0+(1−2alpha_1)*kappa_1]/2,
kappa_eff=m/(1−2s) ∈ (0,1).
```
D/Y conditional routes and the shared L future are identical across source. Every observed key has `P-key-occupancy=LR*Q-key-occupancy`. Hence every LR real behavioural time observation comes from a finite nonnegative **linear occupancy-flow polytope**, and every feasible flow is realized by choosing its Q stop/continue fraction at the corresponding observed key. Its (T_P,T_Q) image is a compact convex polytope. When theta values agree, the above all-signed theorem gives inclusion of all FULL deterministic vectors in this LR convex image. Every FULL real behavioural observation belongs to the convex hull of its finite deterministic images (expand the multi-affine policy map into deterministic product mixtures), so the FULL actual time image is contained in the LR actual time image. The reverse follows because any LR policy is an admissible FULL policy. Thus their **actual time sets**, not merely hulls, are equal. This argument makes NO claim about actual four-coordinate error images under path-dependent terminal errors.

## Two exact positive SOURCE-COMPENSATED examples

`(alpha_0,kappa_0)=(1/4,3/4)` and `(alpha_1,kappa_1)=(1/5,1/6)` give `theta_0=theta_1=11/2`. Different origins have different stage-2 and C transition kernels, yet their FULL/LR actual two-time images coincide. Another compensated pair: `(1/4,9/10)` and `(1/5,4/15)`, with theta `29/5`. These models preserve a genuine source-history BRC residual despite exact equality of the time readout; they are candidate inputs for full four-observer screening, not yet solutions.

## Exact rational regression and boundaries

`VERIFY_SOURCE_SPECIFIC.py` runs alongside sibling `VERIFY.py` and uses its exact hull routine. For six rational parameter triples/quads it enumerates **4096 FULL and 16 LR deterministic policies each**, checks both Q/P terminal normalizations and the all-signed hull equality by testing every FULL time point against the exact rational LR convex polygon for three theta-equal examples. Three theta-unequal examples give exact H_t support gaps and multiple outlying FULL vertices. Literal executed stdout: `EXACT_SOURCE_SPECIFIC_OUTPUT.txt`, marker `PASS_EXACT_R5_SOURCE_SPECIFIC_C_DETOUR_TIME_HULL_COMPENSATION`. The all-real claim is the algebraic theorem above; finite enumeration supplements it.

BRC: source and path identity, positive Q cylinder weights and LR P transport are maintained until the signed time readout; theta is a derived observer-specific repair coordinate, not a replacement for full source provenance. Native X6 transfer, four-hull equality, actual real four-image nonmembership, formal CLAIM/Result and independent Driver review remain separate.
