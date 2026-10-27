# N=3 predecessor-kernel rank and bounded convexification of seedless LR policies

2026-10-27, AUTHOR-LEVEL algebraic result. External strictly-positive finite P/Q stopping tree with BRC ordered rational branch mass; NOT native P000/X6/Heartbeat dynamics or independent review. Fixed input GLOBAL_KNOWLEDGE_V1 main@8efb0525822c9a4fa5218bf244e3953d0068fd60; EM main@1d68591d765430a087c45772d0ff47c4944a3196. Native control has no verified CLAIM; the activity/publishing action is not a Source-native Result.

## Model and notation
Depth N=3, P,Q both strictly positive on each finite edge. Time t is an observation-count index separately typed from P000 native six-dimensional space. Root, t=1 and t=2 permit a local distribution on continue, decide Q and decide P; at t=3 only a decision is allowed. A seedless quotient policy uses only (t,L), L(h)=P(h)/Q(h), with no persistent random seed. Observer vector is O=(eP,eQ,EP[tau],EQ[tau]), where eP=P(decide Q), eQ=Q(decide P).

For a time-1 LR class i and time-2 LR value r, let nu_ir(y) be the **uncontrolled** Q mass of terminal histories with time-1 LR i, time-2 LR r, terminal LR y, summed over their ordered histories. Put eta_ir=sum_y nu_ir(y). For eta_ir>0 define K_ir(y)=nu_ir(y)/eta_ir. Values with eta=0 are excluded. Differences between ordered histories sharing i are averaged with their fixed Q weights, because a seedless policy takes the same time-1 action on their LR fiber.

## Theorem 1: finite exact rank/minor criterion
If c0 is root-continue probability and c_i is time-1 continuation at i, then conditional on reaching time-2 LR r the time-3 LR distribution after continuing is

K_r^(c)(y) = [sum_i c0 c_i nu_ir(y)]/[sum_i c0 c_i eta_ir].

It is independent of every permitted upstream seedless action vector (with positive denominator) **iff**

eta_ir nu_jr(y) - eta_jr nu_ir(y) = 0

for all y and all predecessor classes i,j having positive eta. Equivalently all normalized rows K_ir coincide, or the nonzero row matrix nu_ir(y) has rank one. Proof: equality makes the displayed mixture constant; conversely set all time-1 continuation probabilities zero except for one class, then choose another. These choices independently realize each K_ir. Root continuation can be positive. QED.

More strongly, the complete set of conditional kernels at r is conv{K_ir:eta_ir>0}: any simplex weights lambda_i are realized by c_i=t lambda_i/eta_ir with t>0 sufficiently small. Its affine dimension is rank of the normalized-row differences. Its total-variation diameter is

Delta_r=max_{i,j} (1/2) sum_y |K_ir(y)-K_jr(y)|.

All these quantities have finite exact rational certificates. Delta_r>0 witnesses policy-dependent conditional *terminal law*, not by itself nonconvexity of O, a signed support gap, or minimal residual bits.

## Theorem 2: constructive quantitative convexification
Consider ANY finite convex mixture of seedless quotient policies pi_s with weights lambda_s. There is a single seedless policy pi_bar, built without a persistent lottery seed, such that EP[tau] and EQ[tau] match the weighted mixture **exactly**. Let b_r be its Q arrival mass at time-2 LR r, M=max terminal LR, and B=(1/4) sum_r b_r Delta_r. Its error probabilities obey

|eQ(pi_bar)-sum_s lambda_s eQ(pi_s)| <= B,
|eP(pi_bar)-sum_s lambda_s eP(pi_s)| <= M B,
B <= (1/4) max_r Delta_r.

Construction and proof. At root and every time-1 LR fiber, average each Q action-flow mass of the input policies and recover each local action probability by dividing by the averaged incoming Q mass (arbitrary valid action at zero mass). The resulting time-2 Q arrivals b_r are exactly the weighted averages. At each r also average its Q action masses and normalize. All root/time-1/time-2 stop/decide flow contributions and BOTH expected sampling times match exactly: on LR l, P action mass=l*(Q action mass).

For b_r>0 define alpha_sr=lambda_s b_sr/b_r, z_sr=pi_s's continuation probability at r, and K_sr the terminal kernel produced at r by pi_s's upstream actions. The constructed policy has conditional terminal kernel E_alpha K_sr and continuation E_alpha z_sr. Its time-3 Q-arrival measure from r is U_bar,r=b_r (E z)(E K), compared with the desired mixture U_mix,r=b_r E[zK]. Their signed difference D_r (zero total mass) equals, up to sign,

(b_r/2) sum_{s,t} alpha_sr alpha_tr (z_sr-z_tr)(K_sr-K_tr).

Since every K_sr is a convex mixture of the fixed predecessor kernels K_ir, TV(K_sr,K_tr)<=Delta_r, where TV(D)=(1/2)sum_y|D(y)| for zero-mass signed D. Then
TV(D_r) <= (b_r/2) Delta_r E|z-z'| <= b_r Delta_r/4.
For the second step, |x-y|<=x(1-y)+y(1-x) on [0,1], so E|z-z'|<=2(Ez)(1-Ez)<=1/2. Summing r gives TV(U_bar-U_mix)<=B.

At each terminal LR y set the constructed decide-Q probability to [desired mixture Q-arrival mass that decides Q at y]/U_mix(y) when U_mix(y)>0, arbitrary otherwise. These fractions lie in [0,1]. Errors versus the desired mixture are integrals of 1-d_y (range <=1) and y*d_y (range <=M) against the zero-total-mass signed difference U_bar-U_mix. Hence absolute errors <=B and <=MB. Time results remain exact. Rational model, mixture weights and action probabilities give rational constructed probabilities. QED.

Delta=0 recovers the earlier controlled-Markov linear-flow convexity lemma. This theorem is a *quantitative* statement when Delta>0; it does not claim these upper bounds are optimal among all quotient policies or resolve the equal-support/unequal-image conjecture.

## Exactly verified ten-leaf rational witness
Root: Q(a,b)=(1/3,2/3), P(a,b)=(2/3,1/3); L1(a,b)=(2,1/2).
From a: Q(x,y)=(1/2,1/2), P(x,y)=(1/4,3/4).
From b: Q(x,y)=(2/3,1/3), P(x,y)=(1/3,2/3).
Thus L2(ax,ay,bx,by)=(1,3,1/4,1). At ax terminal LR values (1/2,1,3/2) have Q kernel Ka=(1/4,1/2,1/4), P kernel (1/8,1/2,3/8). At by same terminal LR support with Q kernel Kb=(1/3,1/3,1/3), P kernel (1/6,1/3,1/2). At ay and bx use two P=Q=(1/2,1/2) terminal outcomes, retaining respectively LR 3 and 1/4. All ten leaves are strictly positive; conditional P/Q normalize; LR transport exact.

At collision r=1, eta_a=Q(ax)=1/6, eta_b=Q(by)=2/9. A rank minor at terminal LR y=1/2 is eta_a nu_b(y)-eta_b nu_a(y)=1/324, so rank-one fails. Delta_1=TV(Ka,Kb)=1/6; other Delta values are zero.

Policy A: continue root,a and time-2 r=1, stop/decide P at all other reachable nonterminal nodes, terminal decide Q iff terminal LR is 1/2 or 3/2. Policy B: continue root, stop/decide P at a, continue b with probability 3/4 (otherwise decide P), and stop/decide P at time 2. Their 1/2-flow-averaged seedless C continues root; at a with probability 1/2; at b with probability 3/8; at time-2 r=1 with probability 1/2; elsewhere stop/decide P; terminal decide Q iff y is 1/2 or 3/2.

Exact Fraction calculations:
O(A)=(1/12,11/12,11/6,3/2);
O(B)=(0,1,5/4,3/2);
[O(A)+O(B)]/2=(1/24,23/24,37/24,3/2);
O(C)=(7/144,137/144,37/24,3/2);
difference=(1/144,-1/144,0,0).

For C, b_1=1/6. The desired terminal Q-arrival law at r=1 is (1/12)Ka; actual is (1/24)(Ka+Kb). The TV error is exactly (1/24)TV(Ka,Kb)=1/144=b_1 Delta_1/4. Thus the per-fiber total-variation estimate and this construction's eQ bound are attained by the example. This is NOT a best-possible distance from the midpoint to the entire seedless image.

Verification: attached VERIFY.py, executed output EXACT_OUTPUT.txt. Only the ten-leaf instance is computationally checked; the all-real theorem is the algebraic derivation above. No native Source CLAIM/Result/independent Driver review. Next task in NEXT_TASK.md.
