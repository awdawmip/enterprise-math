# Stage149 — external N14 ternary iid: full-real optimal affine segment

**Evidence:** exact author computation-assisted proof; mathematical Driver review, native CLAИM/Result, and P000/native-X6 transfer remain unverified. This is a positive-rational *external iid observer* model. It preserves individual ordered histories in the independent checker. The count-state dual is valid only for the four stated observers.

## Model and theorem

For independent ternary observations with P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6), allow arbitrary complete-ordered-history randomized stop/decision policies, forced to stop by depth N=14. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau). The value V14(alpha) is min max(tP,tQ) subject to both errors <=alpha.

The prior immutable Stage148 author result has alpha148=6124245463802993075/17602807464179269632 and V148=35426720708566621357/2933801244029878272.

**Theorem.** For every REAL 0 <= delta <= 73294925/4400701866044817408,

V14(alpha148+delta) = V148 - (198980368/266527)*delta.

The right endpoint is

- alpha149 = 6124245464096172775/17602807464179269632
- V149 = 106280162016260661671/8801403732089634816.

For every alpha > alpha149 the *same* affine supporting lower bound is strictly below the optimal value. This is right-sharp support, not a prediction about the next optimal curve.

## Universal Bellman lower bound

For any ordered prefix with state s=(n,a,b), where a,b count symbols 0,1, its likelihood ratio is r(s)=Q(prefix)/P(prefix)=2^(a+b)/3^a. Set

K=100164600/266527, L=98815768/266527.

The finite backwards rational Bellman recursion on all 680 count states is

H(s)=min{K*r(s) [decide P], L [decide Q], 1+sum_i P_i H(next_i(s)) [continue]},

with continuation omitted at n=14. Exact Fraction evaluation yields H(root)=2645762825003325844206337/9733658641089851031552, just two ties:

- B=(11,0,1), Q-stop versus continue;
- G=(11,7,3), P-stop versus continue.

Across all states/actions there are 1238 strictly positive alternative gaps (minimum 2016649859/176854523904) and zero negative ones.

By backward induction, for **every** randomized complete-history policy (without assuming that its decisions depend only on counts), the conditional P-weighted continuation cost is at least H(s). The iid suffix law and current likelihood ratio depend on the count state, which suffices only for this particular lower bound. Consequently

H(root) <= tP+L*eP+K*eQ <= max(tP,tQ)+(K+L)*alpha,

hence V14(alpha)>=H(root)-(K+L)*alpha universally.

## Ordered branch provenance and four exact observers

At each strict state take its unique Bellman-minimal action. At B take Q-stop with probability b, otherwise continue; at G take P-stop with probability g, otherwise continue. Both states have depth 11 and distinct first-two-symbol counts, so their real ordered-history cones are disjoint. The exact first-hit inventories, computed separately using literal integer-weight ordered-prefix DFS, are:

- B: 11 histories, P mass 107421875/1451188224 and Q mass 107421875/725594112.
- G: 330 histories, P mass 275/28991029248 and Q mass 275/61917364224.

The DFS propagates separate P integers (3,1,20) at denominator 24^n and Q integers (1,1,10) at denominator 12^n. A separate backward Fraction recurrence computes (eP,eQ,tP,tQ) for all four coin corners. All 16 componentwise identities agree, including exactly zero four-vector mixed corner difference. Actual DFS visited nodes at (b,g)=(0,0),(1,0),(0,1),(1,1) are 567934, 567802, 563974, 563842.

Writing M=(eP,eQ,tP,tQ), the exact affine map is M(b,g)=M00+b*dB+g*dG, with

M00=(
 1212667745125447135/3505953353861431296,
 224474522518415/641959232274432,
 5331415436276024017/438244169232678912,
 630124894429211/53496602689536)

dB=(
 4619140625/2229025112064,
 -751953125/417942208512,
 -25673828125/278628139008,
 -17939453125/104485552128)

dG=(
 -12925/400771988324352,
 6325/106993205379072,
 -171325/16698832846848,
 -45925/8916100448256).

These are signed **differences of observers** over positive P,Q branch measures; negative increments do not turn the primitive weights into signed BRC mass.

## Full-real interval and exact sharpness

The error equality eP=eQ is equivalent to

g=(2467840000000/58241)*(b-b_star),

where b_star=7957468313073991/8143872000000000 is exactly the Stage148 terminal B coin (with G=0).

The feasible balanced segment continuing Stage148 is

b_star <= b <= b_end=7957468505269291/8143872000000000,  0<=g<=1.

At b=b_end, g=1 while b_end<1: **G's P-stop coin saturates first**. At the left endpoint, eP=eQ=alpha148 and tP=V148; at the right, eP=eQ=alpha149 and tP=V149. The times are dominated by tP at both endpoints with strictly positive exact gaps:

- tP-tQ at left = 36781979533221897065/79212633588806713344;
- tP-tQ at right = 36781979277243213665/79212633588806713344.

The common error strictly increases with b. At both endpoints the complementary-slackness identity

tP + L*eP + K*eQ = H(root)

holds exactly, and V148-V149=(K+L)(alpha149-alpha148). All observer coordinates, error balance, and time gap are affine in b. Therefore these constraints and equality hold for **every real** b in the segment. This proves attainment throughout the full real interval, not just for four corners or a finite rational grid.

For right sharpness: the finite full-ordered-history randomized policy space and its observer image are compact (all symbol weights positive), so minima are attained. If any alpha>alpha149 attained the same Bellman lower support, positivity of K and L would force eP=eQ=alpha, tP>=tQ and the minimizing Bellman action at every reached history; strict gaps prohibit every other action. At a tied count state all first-hit prefixes have the same Q/P likelihood ratio, and the iid suffix law is identical; hence any history-dependent tie randomization can be replaced by one P-mass-weighted effective coin without changing the four observables. B and G have disjoint cones at the same depth, so every policy attaining this support has some M(b,g) in [0,1]^2. Balance restricts it to the displayed b segment, where alpha cannot exceed alpha149. Contradiction. Thus the supporting line is strictly below the true value to its right.

## Evidence, scope, and next unit

The portable local checker performs exact 680-state Fraction Bellman evaluation; separately structured backward-recursion and ordered-DFS four-corner checks; first-hit masses; mixed term; exact rational balance, saturation, time dominance and slope identities. The parent Stage148 result supplies only the left endpoint; all Stage149 corner data are recomputed at its new dual.

Source pins: GLOBAL_KNOWLEDGE_V1 main@f43f0160e56ef99ea5daa8bbfe8c44516e7661b9; Enterprise Math main@51e594f6642b88f8ab6d852f575fff4911d3e081; Stage148 proof and candidate EM@aafcfc3ca6e2f8325311848ccc2a5193a074209f. Method: existing rational Bellman plus positive-rational ordered-prefix BRC-style provenance reuse. Native control listing returned CONTROL_QUOTA and session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The active owner, Source CLAIM, Result and independent Driver acceptance are not verified.

This auxiliary iid theorem neither changes P000 (6 native spatial axes, 3D research slice, separate time) nor supplies an embedding of branch labels, phase, ports, or allowed future operations into native GF(2)-BRC/Heartbeat X6. Such a transfer must be proved separately.

**Next Stage150:** Hold B's Q/C tie at Stage149 dual weights, scan every one of the 680 states for the next strict action-gap closure after G has saturated P-stop; independently recompute new first-hit cones and four-observer feasibility. Do not repeat the finished Stage149 segment, and do not infer mathematical acceptance from GitHub storage.
