# R5 — Exact positive central-history information freedom at every interior stopping-time pair

Date: 2026-11-06 Asia/Shanghai. Claim: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Scope, mathematical parent, source freeze
The R5 mother question seeks a finite **strictly positive rational** P/Q stopping model with equal four-observer FULL_HIST / seedless LR convex hulls but unequal **actual** four-observer images. The present lemma studies the exact delta=1/4 four-stage auxiliary P/Q/BRC likelihood-ratio model, with unrestricted P/Q declarations at stopped keys. It is **not a theorem about native six-axis Heartbeat dynamics**. Frozen science: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Exact scalar gate: EM `57f7d654e5dd002567e0b0d333937e6e38f3b4cb`; exact time-octagon boundary theorem: EM `46c13622fb3ce59025c31ae5cb90d70d57066fbf`.

At time 3, `q3[0]=(13/20,1/5,3/20)`, `q3[1]=(1/40,9/20,21/40)`. Set `x=(g,u0,u1,X0,X1,X2)`, `0<=u_i<=g<=1`, and
`0<=X_j<=V_j=(q3[0,j]u0+q3[1,j]u1)/2`.
The stopping-time projection is
`T_Q=1+g+(u0+u1)/2+X0+X1+X2`,
`T_P=1+g+(3u0+5u1)/8+X0/2+X1+3X2/2`.
Write `A=u0/10`, `B=9u1/40`, `S=A+B=V1`, `X=X1`,
`alpha=47/180`, `beta=67/162`, `d=beta-alpha=247/1620>0`.
All legitimate FULL_HIST central coefficients are precisely
`J_lo=max(alpha X,beta X-d A) <= J <= J_hi=min(beta X,alpha X+d B)`.
The seedless LR coefficient at the same flow is
`J_LR=X(alpha A+beta B)/(A+B)` for S>0, zero for S=0.
The time image H_T is the eight-sided rational polygon in the exact prior boundary theorem, with facet slacks `s_i(t)=a_i t_P+b_i t_Q-c_i>=0`:
`(-282,323,41),(-160,160,-41),(-216,188,-139),(-2,1,-4),(2,-3,-4),(236,-274,-179),(80,-80,-23),(146,-123,23)`.

## Theorem — exact J-thickness and radial lower bound

For each fixed feasible six-flow x, its FULL_HIST central coefficient interval has **exact** length
`J_hi-J_lo=d*min(A,B,X,S-X)`.
If `A>0,B>0,0<X<S`, the interval has positive length and its fixed-flow seedless LR value lies strictly between its endpoints.

Let `c=(1/2,1/4,1/4,27/640,13/320,27/640)`, whose stopping-time image is `t_c=(15/8,15/8)`. This c is a strict interior point of the six-flow polytope. Its eight facet slacks in the specified order are
`(287/8,41,173/2,17/8,17/8,431/4,23,161/8)`.

For any stopping-time pair `t=(t_P,t_Q)` **strictly inside H_T**, define the dimensionless rational/polyhedral radial gauge
`lambda(t)=min_{i=1..8} s_i(t)/s_i(t_c)`.
Then `0<lambda(t)<=1` and there is an **explicit** feasible six-flow x with timing t for which
`J_hi(x)-J_lo(x) >= (247/64800)*lambda(t) > 0`.
Both endpoints and every intermediate J are realized by legitimate FULL_HIST histories. The same flow x also admits one seedless LR history profile whose J lies strictly between the FULL endpoints.

Combining with the previous exact boundary-fiber theorem: the existence of a flow of time t with nonzero central-history J freedom is **equivalent** to `t` being in the strict interior of H_T (for this fixed four-stage tree). This is an information-carrier/fiber claim; it neither assumes nor asserts a four-observer actual-image separation.

## Proof

**(1) Interval width.** Subtract `alpha X` from both endpoints. Then
`J_lo-alpha X=d*max(0,X-A)`,
`J_hi-alpha X=d*min(X,B)`, using `0<=X<=A+B`. Hence
`J_hi-J_lo=d*(min(X,B)-max(0,X-A))=d*min(A,B,X,A+B-X)`, by splitting at X=A and X=B. The four terms are nonnegative. Every J in this interval corresponds to
`x_{01}=(beta X-J)/d, x_{11}=X-x_{01}`, satisfying `0<=x_{01}<=A,0<=x_{11}<=B`; the j=0,2 histories are recovered using common `X_j/V_j` at positive V_j, arbitrarily at zero mass. This proves full all-real attainability, including boundaries.

**(2) Strict seedless interior.** If `A,B>0,0<X<S`, then `J_LR-alpha X=d*B X/S`. The inequalities
`max(0,X-A) < B X/S < min(X,B)`
follow from `A,B>0,0<X<S`. Thus `J_lo<J_LR<J_hi`.

**(3) Explicit interior center.** For the stated c, capacities are `(27/320,13/160,27/320)`, so `X_j=V_j/2`. Direct substitution yields timing `t_c=(15/8,15/8)`. The strictly positive facet slacks are displayed above. At this center, `A=1/40`, `B=9/160`, `X=13/320`, and `S-X=13/320`, whence its J-width is exactly `d/40=247/64800` and `J_lo=3367/259200<J_LR=143/9600<J_hi=871/51840`.

**(4) Radial constructive lift.** Boundedness of the octagon and strict interiority of t_c imply `lambda(t)<=1`, and `lambda(t)>0` for interior t. If `lambda=1`, then t=t_c. Otherwise set
`b=(t-lambda*t_c)/(1-lambda)`. Every `s_i(b)=(s_i(t)-lambda*s_i(t_c))/(1-lambda)>=0`, and one is zero, so b is on the octagon boundary. The prior exact time-boundary theorem gives a feasible unique six-flow x_b (explicitly interpolate its adjacent vertex flows). Define
`x=lambda*c+(1-lambda)*x_b`.
Feasibility is preserved by linear flow constraints, and its timing equals t. The four nonnegative affine functionals `A,B,X,S-X` are each at least `lambda` times their value at c. Thus
`min(A,B,X,S-X)>=lambda*min(1/40,9/160,13/320,13/320)=lambda/40`.
Multiply by `d=247/1620` to obtain the announced lower bound. Since each of the four functionals is positive, the strict LR-interior result applies. QED.

**(5) Boundary converse.** The preceding time-boundary theorem establishes unique flow at every boundary time pair and `X=0`, `A=0`, `X=A+B` or `B=0` on its respective edge; the exact width formula then gives zero. Thus the interior criterion holds in both directions.

## Verification and status
`VERIFY.py` uses `fractions.Fraction` and enumerates all 64 deterministic timing policies, 26 distinct time images, the eight facet/vertex incidences, exact widths at the center and boundary, 864 rational radial edge-to-center pairs, and 240 fixed-seed convex-combination interior targets (1104 exact interior tests). See `EXACT_OUTPUT.txt`. The proof is the analytic argument above; sampling exercises the construction but is not used for all-real quantification.

This adds a quantitative **lower bound on latent central-history information freedom conditional on time**. The mother R5 actual-image separation remains to be decided globally over all admissible six-flows for a fixed full four-observer W.
