# BRC N=4 S23: monotone Chernoff exponent and certified band surrogate

Date: 2026-11-04. Classification: AUTHOR_ANALYTIC_PROOF / LOCAL_SYMBOLIC_AND_NUMERICAL_AUDIT_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen input and precise scope

Scientific input stays at awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Retain the already specified two-state S23 source-label model, with v=2h, 0<v<=1/21, 0<s<=1, k=s/(2-s), source-trial T and scalar-Bernoulli B, and costs 2-s and 1. The full ten-label minimax problem is separate. All results below are internal to the two-state Chernoff experiment; no native X6 spatial-transfer assertion is made.

Put alpha=atanh(v), gamma=atanh(kv), X=s*sqrt(1-v^2)/2, Y=(2-s)*sqrt(1-k^2 v^2)/2. At t=(1+delta)/2, the scalar Chernoff coefficient is

    Z_s(delta)=X*exp(alpha*delta)+Y*exp(-gamma*delta).

Let C_B(s,v)=-log(min_{-1<=delta<=1} Z_s(delta)). Define
    psi(x)=log(sqrt(1-x^2)*atanh(x)/x), psi(0)=0,
    q(x)=[atanh(x)-x]/[x(1-x^2)atanh(x)] for x>0, q(0)=0.

The earlier author result in the same PR proved the exact interior optimizer

    delta_*(s,v)=[psi(kv)-psi(v)]/[alpha+gamma]

and the uniform bounds

    (1-k)v(1-v^2)/6 <= delta_* <= (1-k)v/[6(1-v^2)^2] < 1/125

for 0<s<=1. This note makes additional deductions from that verified *author-side* frontier.

## Theorem 1: monotonicity and rational global sensitivity

For every fixed real 0<v<=1/21, delta_*(s,v) extends continuously to [0,1], is analytic on (0,1), strictly decreasing, and satisfies

    delta_*(0+,v)=-psi(v)/alpha >0,      delta_*(1,v)=0.

For all 0<s<1, writing D=alpha+gamma and k'=2/(2-s)^2,

    -partial_s delta_* = (v*k'/D) [q(kv)+delta_*/(1-k^2 v^2)] >0.       (1)

There is an explicit global Lipschitz estimate, valid also for endpoint limits,

    0 <= delta_*(a,v)-delta_*(b,v) <= M_v (b-a),
    M_v = v(3-2v^2)/[3(1-v^2)^3],     0<=a<=b<=1.                  (2)

The one-sided endpoint derivatives are

    partial_s delta_*(0+,v)=v*psi(v)/(2*alpha^2)<0,               (3)
    partial_s delta_*(1-,v)=-(alpha-v)/[(1-v^2)*alpha^2]<0.      (4)

**Proof.** For 0<x<1, direct differentiation gives psi'(x)=-q(x). Since atanh(x)>x, q(x)>0. Let A(k)=psi(kv)-psi(v), D(k)=alpha+atanh(kv). For 0<=k<1, A>0 and D>0; A'(k)=-v q(kv), D'(k)=v/(1-k^2 v^2). Differentiating delta_*=A/D and using k'=2/(2-s)^2 proves (1); its sign proves strict monotonicity. Endpoint continuity uses psi(0)=0, and the derivative limits at k=0,1 give (3),(4), noting q(0)=0 and k'(0)=1/2, k'(1)=2.

For the quantitative bound, the positive atanh series gives atanh(x)-x <= x^3/[3(1-x^2)] and atanh(x)>=x. Thus
    0<=q(x)<=x/[3(1-x^2)^2].
Now D>=(1+k)v. Use the previously proved optimizer upper bound:
    v/D*q(kv) <= v/[3(1-v^2)^2],
    v/D*delta_*/(1-k^2 v^2) <= v/[6(1-v^2)^3].
Their sum is <=v(3-2v^2)/[6(1-v^2)^3]. Since k'<=2, (1) yields -delta_s'<=M_v; integrate over [a,b]. QED.

## Theorem 2: quadratic-error Chernoff surrogate for any s-band

Fix v in (0,1/21] and any real 0<=a<=b<=1. Use the endpoint-limit convention above and define

    d_ab = [delta_*(a,v)+delta_*(b,v)]/2,
    W_ab = delta_*(a,v)-delta_*(b,v).

For every s in [a,b] intersect (0,1], define C_ab(s,v)=-log Z_s(d_ab).
The true *optimized* Chernoff information obeys

    0 <= C_B(s,v)-C_ab(s,v)
       <= alpha^2 W_ab^2/8
       <= R_v (b-a)^2,                                        (5)

where the **fully rational-in-v** band-error constant is

    R_v = v^4(3-2v^2)^2/[72(1-v^2)^8].                         (6)

Thus writing C_T=-log[1-s+s sqrt(1-v^2)] and

    F(s,v)=C_T/(2-s)-C_B(s,v),
    F_ab(s,v)=C_T/(2-s)-C_ab(s,v),

the entire band has the certified one-sided enclosure

    F_ab(s,v)-R_v(b-a)^2 <= F(s,v) <= F_ab(s,v).               (7)

In particular, if an outward interval evaluation on a band proves F_ab<0 throughout, then F<0 there. If it proves F_ab>R_v(b-a)^2 throughout, then F>0 there. This yields a certified sign test for the **truly optimized** Bernoulli experiment with only one band-center exponent, avoiding repeated pointwise optimizer solving. To make it machine-rational, enclose the two endpoint exponent values and log/exp/sqrt with directed rational arithmetic; (6) is already an exact rational number at rational v.

**Proof.** For L_s(delta)=log Z_s(delta), the tilted-weight identity gives
    L_s''(delta)=p(delta)(1-p(delta))(alpha+gamma)^2
               <=(alpha+gamma)^2/4<=alpha^2.
L_s'(delta_*)=0 and Taylor's integral remainder yield
    0<=L_s(d_ab)-L_s(delta_*)<=alpha^2 (d_ab-delta_*)^2/2.
By Theorem 1, delta_*(b)<=delta_*(s)<=delta_*(a), so |d_ab-delta_*|<=W_ab/2. Hence the first inequality in (5). By (2), W_ab<=M_v(b-a); by alpha=atanh(v)<=v/(1-v^2), substitute to obtain exactly R_v in (6). The sign enclosure is algebra. QED.

At maximal lawful v=1/21, exact integer arithmetic gives

    M_v = 4077927/85184000 < 1/20,
    R_v = 7333604480242089/11238578900172800000000.

For any s-band of width 1/10000, the rational bound R_v(b-a)^2 is approximately 6.526e-15 (the exact fraction appears in RUN_EVIDENCE.txt). The bound is unconditional in the band's location and does not assert that a sign was classified there.

## Corollary: exact optimizer-free derivative formula for C_B

For 0<s<1 let k'=2/(2-s)^2. Then

    partial_s C_B =
      -gamma/[s(alpha+gamma)]
      +alpha/[alpha+gamma] *
        {1/(2-s) + [(k v^2)+(delta_* v)]k'/(1-k^2 v^2)}.    (8)

**Proof.** At the stationary delta_*, the weights of the two terms in Z_s are gamma/(alpha+gamma) and alpha/(alpha+gamma). Differentiate -log Z_s holding delta fixed (envelope theorem), using X'/X=1/s, Y'/Y=-1/(2-s)-k v^2 k'/(1-k^2 v^2), gamma'=v k'/(1-k^2 v^2). No derivative of delta_* occurs. QED.

Formula (8) and the monotone enclosure (2) are inputs for a rational interval derivative certificate for H(s,h)=F(s,h)/(h^4 s(1-s)); one can either certify H_s>0 on the full lawful h=1/42 slice or isolate additional roots. This note does **not** claim that global uniqueness has been established.

## Validation and observer boundary

VERIFY.py actually executed in Python with SymPy and mpmath. It checks psi'(x)=-q(x) by exact symbolic simplification; exactly checks rational M_v and R_v constants; audits (1) and (8) against independent high-precision numerical differentiation at 99 s samples; checks two nontrivial band examples and the endpoint slopes. RUN_EVIDENCE.txt preserves stdout. The universal real-parameter claims are supported by the explicit analytic proofs above; the sample computations are an implementation audit, not a substitute for proof. In BRC terms, T retains source-label branch information; B is the declared scalar projection. We optimize within the resulting observer-specific two-state channel without asserting any recovery of discarded provenance. The mother ten-label model's known minimax interval [1/2,2/3] remains unchanged.
