# Auxiliary N=14 iid sequential testing: exact stage88 affine segment

**2026-10-25. Author-side exact finite-model proof, not native BRC/X6/Heartbeat, Lean, a frozen Result, or independent Driver acceptance.**

## Theorem and inherited inputs

A randomized stopping rule observes at most 14 iid symbols {0,1,2} drawn from P=(1/8,1/24,5/6) or Q=(1/12,1/12,5/6), with arbitrary dependence on the **full ordered history**. Write eP=P(decide Q), eQ=Q(decide P), tP=E_P(T), tQ=E_Q(T), and V14(alpha)=min max(tP,tQ) subject to both errors <=alpha. All finite-horizon randomized rules, not merely count rules, are in the optimization class.

Inherit the stage87 endpoint
alpha87=5172378789334355543/14900301753911083008,
V87=24313783684225133729/1862537719238885376,
S87=29597133147954427/41779200000000000,
with randomized immediate-Q probability S87 at B=(12,0,1), stage87 A87=(13,7,3) now fixed immediate P, and the remaining stage87 frozen action table in `derive88.py`.

**Exact statement (every real parameter):** If
eta88=30744093875/34491439245164544, then for 0<=delta<=eta88,
`V14(alpha87+delta)=V87-(930557219040/245952751)*delta`.

The sharp right endpoint of this *supporting line* and its value are
alpha88=5172392070782909543/14900301753911083008,
V88=24307502422996613729/1862537719238885376.
No absence-of-later-segments theorem is asserted.

## Bellman global lower bound

Let (n,a,b) count draws in total, zeros, and ones. For every ordered prefix of this state Q(prefix)/P(prefix)=2^(a+b)/3^a; all share the same conditional iid suffix law. There are exactly 680 count states with n<=14. At
K88=lambdaQ=483272799336/245952751,
lambdaP=72+(8/9)K88=447284419704/245952751,
Gamma=lambdaP+lambdaQ=930557219040/245952751,
use P-normalized Bellman actions

- immediate P: lambdaQ*2^(a+b)/3^a;
- immediate Q: lambdaP;
- continue: 1+sum_i P_i D(child_i), n<14; at n=14 continuing is forbidden.

Exact rational backwards minimum recursion over all 680 states certifies the frozen stage87 policy with A88=(6,4,0) and B=(12,0,1) set to continue: 1240 nonselected comparisons, 1238 strictly positive gaps, zero negative gaps, and *exactly two* action ties, A88 (continue/P) and B (continue/Q). The least positive gap is 819780607/53125794216. The root is
D0=35742902631612445605710387107/26946839758121734376521728
=V87+Gamma*alpha87.

Conditioning on each full history and Bellman induction yield for **every** ordered-history randomized rule
`D0<=tP+lambdaP*eP+lambdaQ*eQ<=max(tP,tQ)+Gamma*alpha`.
Thus V14(alpha)>=D0-Gamma*alpha universally.

## Branch/probability audit

Exactly 15 of 15 nominal ordered prefixes first reach A88, carrying
pA=125/49152 and qA=125/248832.
The frozen stage87 continuation suffix from A88 has exact tuple
(P-error,Q-error,extra-P-time,extra-Q-time)
RA=(40458953/36691771392,142135663/143327232,1867400093/1528823808,5894645/3981312).
Its explicit suffix tree has 753 terminal **words** in 37 terminal state/action classes; immediate stopping cuts 15*753=11295 complete previously terminating words.

At B, 12 first-hit ordered prefixes carry
pB=48828125/725594112, qB=48828125/362797056;
the continuation tuple is RB=(63/64,1/144,9/8,13/12), with five suffix terminal words.
The two randomization cones are disjoint: after A88 the zero-symbol count is already 4 and can never become the B value 0, while B occurs at a larger time index. Consequently **no u*s cross term** occurs. Branch counts remain distinguished from P/Q probability masses; this is a provenance-preserving, auxiliary BRC-style audit rather than native residual attribution.

## Continuum-achieving primal family

Let u be the immediate-P probability at A88, s the immediate-Q probability at B. Against baseline (u=0,s=S87), define positive rationals

X=pA*RA[P-error]=5057369125/1803473947459584,
Y=qA*(1-RA[Q-error])=148946125/35664401793024,
E=pB*(1-RB[P-error])=48828125/46438023168,
H=qB*RB[Q-error]=48828125/52242776064.

Disjoint ordered cones give exactly:
`eP-alpha87=-X*u+E*(s-S87)`,
`eQ-alpha87= Y*u-H*(s-S87)`.
Choose
`s=S87+h88*u`,
`h88=(X+Y)/(E+H)=24473525451/6963200000000`.
Then the two errors are *identical*:
`eP=eQ=alpha87+eta88*u`,
where `eta88=-X+E*h88=Y-H*h88=30744093875/34491439245164544>0`.
At u=1, `S88=29743974300660427/41779200000000000<1`; also 0<S87<S88, so this defines a feasible randomized rule for **every real** u in [0,1].

Its time difference is affine in u. The two exact endpoint values are
`tP-tQ=2174599878250146305/3725075438477770752` at u=0, and
`tP-tQ=2166716868242604305/3725075438477770752` at u=1; both are strictly positive. Thus max(tP,tQ)=tP for every u. Every positively taken action is Bellman-minimal (the randomized choices are exactly the two action ties), hence
`tP+lambdaP*eP+lambdaQ*eQ=D0`.
It follows that `max(tP,tQ)=D0-Gamma*(alpha87+eta88*u)`, proving the displayed affine optimum for the entire real interval, not just rational test points.

## Right-end sharpness

An attaining randomized finite-horizon policy exists by compactness of its finite product of stochastic decision simplexes. If alpha>alpha88 attained the same supporting line, equality of both inequalities would force eP=eQ=alpha (both Lagrange multipliers positive) and all positive-reach chosen actions to be Bellman-minimal. The certified strict gaps leave only A88 and B free. At a fixed count state, P and Q path weights are proportional and the conditional suffix law is the same, so even an ordered-history-dependent policy reduces for these objectives to an effective randomization probability on each state. Since the cones are disjoint, equal errors again enforce `s=S87+h88*u`, hence `alpha=alpha87+eta88*u<=alpha88` for 0<=u<=1: contradiction. Therefore this supporting line is right-sharp.

## Evidence and limits

The author executed Python Fraction scripts `derive88.py`, `crosscheck88_compatible.py`, and an additional `crosscheck88.py` with full unconstrained Bellman minimum evaluation. The first computes all rationals and 680 action states; the second uses explicit ordered prefix/suffix DFS and eight interpolation checks; the third recomputes the true per-state minimum. These checks share the stage87 inherited selected-action map. They do *not* constitute independent Driver review, a formalized Lean theorem, a native CLAIM, an actual native BRC carrier or a verified X6/Heartbeat transfer. GitHub user identity was observed as `awdawmip`; native task inventory returned `CONTROL_QUOTA` and `session_start` returned `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`), so live owner/CLAIM remains unverified.

**Unproved next candidate:** K89=419904/217, A89=(11,5,4), continue versus immediate Q. With A88 fixed immediate P, compute exact first-hit and suffix evidence, Bellman gaps, possible overlap with B, and compensation or a genuine obstruction. See `NEXT_TASK_PACKET_89.md`.

Predecessor: `awdawmip/enterprise-math@37573fb052c58a0357da3d3489392422badeb250:research_notes/n14_aux_iid_affine_87_20261025/PROOF.en.md`. Global knowledge pin `5ddaf5f3d8bd1ce9934486e7ab80b3627ddaec6c`; EM initial project read pin `a7a070b59f7a2fdc0cbdd447f1cdaeff6f0c1bdf`.
