# R5: Two-upstream scalar-price blind spot and exact signed-time separator

Date: 2026-10-28 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. This is a finite double-measure statistical observation model, **not** a native X6 physics model or an admitted theorem.

Frozen verified inputs: GLOBAL_KNOWLEDGE_V1 main@4702e94662284d0c9d0abd0815240faafe7352ee; Enterprise Math main@6339855b75c3d633f207edfd0d305972c811a9ba. Read project AGENTS, P000, Heartbeat X6/time, ACTIVE worldview, residual/observer preservation, portable and autonomous protocols and R5 predecessor research_notes/brc_r5_discriminant_usc_20261028_t11/RESEARCH.md. The previous single-upstream masking result is in research_notes/brc_r5_optional_upstream_masking_threshold_20261028_t11/PROOF.md. Active native owner query returned CONTROL_QUOTA; session creation was denied STATIC_READONLY_SCOPE_DENIED before transmission (operation_sent=false). These are local-author mathematical materials, not an official CLAIM or Result.

## Finite model, exact types and carrier

Two time-1 histories U,V have Q mass 1/2 each, different P/Q likelihood ratios r_U,r_V, and can independently stop declaring P/Q or continue. Conditional on continuing to time 2, a C edge has Q probability theta and an O edge 1-theta. The O histories terminate and have LR 1+d (U.O), 1-d (V.O), for 0<theta<1 and 0<d<1; the C histories U.C and V.C have the SAME LR 1 and hence share a seedless LR action at t2. The root ratios are r_U=1+(1-theta)d and r_V=1-(1-theta)d. On C the source-dependent time-3 Q prediction kernels for terminal LR Y in (1/2,1,3/2) are K_U=(a,1-2a,a), K_V=(b,1-2b,b), 0<b<=a<1/2. Each K has mean Y equal to 1, making P leaf masses P_leaf=Y*Q_leaf compatible with P(C)=Q(C). All leaves have positive P/Q masses and each measure normalizes to 1. The time-3 decisions are only P/Q declarations; different U/V terminal histories with the same Y again share an LR terminal-declaration action.

Complete-history rules condition on full history; seedless LR behavioral rules condition only on (sample time t, current P/Q ratio R), with arbitrary real local randomization but no persistent common random seed. The exact declared observer is O=(e_P,e_Q,T_P,T_Q)=(P[declare Q],Q[declare P],E_P tau,E_Q tau). Discrete X6 is the locked P000 native physical research frame; U/V labels are merely typed external observer branches. The BRC carrier actually applied here is labeled positive rational branch P/Q mass, keeping source and ordered path, not a signed or complex primitive.

## Theorem A: exact two-upstream Bellman envelope for every signed direction

For any real lambda=(alpha,beta,gamma,delta), minimize lambda·O. For a Q unit at LR r, define f(r)=min(alpha*r,beta) and period-price c(r)=gamma*r+delta. The function f is concave for all signed alpha,beta, because it is a minimum of two affine functions. Define D=2*f(1)-f(1/2)-f(3/2)>=0, g_U=a*D, g_V=b*D, and C=c(1)=gamma+delta.

For i=U,V, with r_i^O=1+d or 1-d respectively, set
S_i=[f(r_i)+c(r_i)]/2,
B_i=[2*c(r_i)+theta*f(1)+(1-theta)*f(r_i^O)]/2.

S_i is the weighted t1 stop cost, B_i the weighted cost if t1 continues and C stops at t2. The complete-history and LR minimum linear scores are EXACTLY:

V_full(lambda)=SUM_i min{S_i, B_i-(theta/2)*max(g_i-C,0)}.

V_LR(lambda)=MIN_{y in {0,1}} SUM_i min{S_i, B_i-(theta/2)*y*(g_i-C)}.

Here y=1 means the COMMON time-2 C action continues, y=0 stops. Both expressions cover every real behavioral randomization, not a parameter grid: a path visits any fixed time-indexed information set at most once, so its linear expected score is multi-affine in local action probabilities, and a vertex (deterministic table) attains its minimum. At t3, a shared declaration at any common final Y is optimal for both hidden sources because both have the same LR there. Therefore optimizing root choices given a fixed common C action yields the second formula. This proves the exact scope of both Bellman envelopes.

## Theorem B: a uniform scalar-Q-time price cone misses every compression loss

If b >= theta*a/(1+theta), then for ALL signed alpha,beta in R and ALL s>=0:

min_full [alpha*e_P+beta*e_Q+s*T_Q]
 =
min_LR   [alpha*e_P+beta*e_Q+s*T_Q].

This is a sufficient gate, not an asserted necessary condition for arbitrary parameters, and it concerns the three-parameter subfamily lambda=(alpha,beta,0,s), NOT all R^4 signed directions.

Proof: Here c(r)=s for all r. Set J_U=f(r_U)-theta*f(1)-(1-theta)*f(1+d), J_V=f(r_V)-theta*f(1)-(1-theta)*f(1-d). Jensen concavity gives J_U,J_V>=0. Since f is piecewise affine with at most ONE kink, it is affine on at least one of the intervals [1-d,1] and [1,1+d]. Thus J_U=0 or J_V=0 (possibly both), even for signed alpha,beta. The root continuation advantage in history i, permitting its private optimal C action, is A_i=J_i-s+theta*(g_i-s)_+.

When s<=g_V or s>=g_U the C branches admit one common optimal action, so LR achieves the full optimum. The only potential conflict is g_V<s<g_U. In this interval s>0. If J_V=0 then A_V=-s<0 (g_V<s), so full stops V already at t1; LR can use C continuation for U. If J_U=0 then A_U=theta*g_U-(1+theta)*s < theta*a*D-(1+theta)*b*D <=0, so full stops U already at t1; LR can use C stop for V. In both cases a full optimal strategy uses at most one source at the collision and is reproducible by a shared LR action. Since LR is a subclass, the minima agree. QED.

This theorem explicitly exhibits a source/observer dependency invisible to a whole continuous scalar-cost cone; it is not a physical claim or a general kernel-lumpability theorem.

## Rational eight-leaf signed-time separator

Take theta=3/4, d=1/2, a=1/4, b=1/8. The gate holds because b/a=1/2 > theta/(1+theta)=3/7. Yet the two upstream LR signatures are distinct (r_U=9/8, r_V=7/8); the hidden C histories collide at LR=1; their future kernels differ.

Leaf row | 128P | 128Q | terminal LR
U.C low | 6 | 12 | 1/2
U.C mid | 24 | 24 | 1
U.C high | 18 | 12 | 3/2
U.O | 24 | 16 | 3/2
V.C low | 3 | 6 | 1/2
V.C mid | 36 | 36 | 1
V.C high | 9 | 6 | 3/2
V.O | 8 | 16 | 1/2

All entries are positive and each integer mass column sums to 128. Choose signed lambda=(20,23,10,-9); f(r)=min(20r,23), c(r)=10r-9, C=c(1)=1, D=7, g_U=7/4, g_V=7/8.

The **complete** Bellman decision table, in weighted cost units, is:

Branch | t1 stop | t1 continue, C stops | t1 continue, C continues
U | 99/8 | 101/8 | 395/32
V | 69/8 | 17/2 | 547/64

Full-history can continue at both roots, continue at U.C but stop at V.C: V_full=395/32+17/2=667/32=1334/64.

LR must choose common C action: if C stops, it stops U at t1 and continues V, costing 99/8+17/2=167/8=1336/64; if C continues, both roots continue, costing 395/32+547/64=1337/64. Therefore V_LR=167/8 and the exact signed full-policy gap is **V_LR-V_full=1/32**.

An explicit full policy (continue U and V; continue U.C, stop V.C declaring Q; stop U.O declaring P, V.O declaring Q; at time-3 U.C declare Q for Y=1/2,1 and P for Y=3/2) attains
O*=(43/64,7/32,19/8,19/8),
whose score lambda·O*=667/32.

Every real seedless LR behavioral strategy obeys the rational separation
20*e_P+23*e_Q+10*T_P-9*T_Q >= 167/8,
which O* violates by 1/32. Thus conv(O_LR) is STRICTLY contained in conv(O_full). The input is an **excluded** mother-problem candidate. It also demonstrates why transporting a scalar-price no-loss theorem from the earlier single-upstream topology to a merged two-upstream topology is invalid, even at the same a=1/4,b=1/8 ratio.

## Exact checker scope, provenance and next question

The attached VERIFY.py is a self-contained Python Fraction/integer program actually executed for this author-side result. It tests normalization/positive masses/time-indexed signatures, enumerates all 3^4*2^2*2^6=20736 complete deterministic tables and all 3^3*2^2*2^3=864 LR deterministic tables (380 and 120 distinct O vectors), confirms their exact minima, matches both Bellman envelopes, and checks 9537 finite scalar-cost examples as *supplementary* evidence. EXACT_OUTPUT.txt is the original exact-output text. The universal scalar-cost theorem rests on the symbolic Jensen/kink proof above; the universal over-real-randomization separating bound rests on multi-affine extremality, not the finite price grid. No independent review, Lean check, physical experiment, Source Result or Working Truth promotion occurred.

The task after this checkpoint is to parameterize the signed gamma/delta cone of equality using the general envelope, produce complete rational facet/cone certificates for fixed collision strata, and seek a DIFFERENT positive rational tree that passes **all** signed four-dimensional supports. Only then attempt a real-behavior nonattainment witness; the present tree is known to fail convex-hull equality. Native authorization and owner checks must be reacquired for formal CLAIM/Result.
