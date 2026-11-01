# PREFIX-425 — The full-source no-early-corner theorem for 0.002 ≤ η ≤ 0.0195

Date: 2026-11-02. Scientific classification: author-side analytic proof with exact outward-integer interval certificate; UNREVIEWED / NOT_ADMITTED.

## Source provenance

Scientific input frozen at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Continuation: PREFIX-423/424; scientific formulas are not re-pinned to the changing control main. Current behavioral read: GLOBAL_KNOWLEDGE_V1 main@6b5d2c73ada20c88f781d4566dedc66d8fff3286, Enterprise Math control main@f405a1a6a4e402219fb01f60014bc0db6e935585. Existing exact interval engine and model: research_notes/PREFIX423_CODE_EVIDENCE.tar.br at commit 9a1ea3ab71469ff6a4f645852d1be9f33b09fdc9, member prefix423_exact_certificate.py. Its predecessor assertions and this extension were actually executed.

## Exact theorem and quantifiers

For every β=10^(-6), 0≤ε≤β and 1/500≤η≤39/2000, minimize κ=||z4|²−41| over all complex coherent (u,v), with

z4=(5+9i)/2+(3+7i)u/2+4iv,
z5=(22+15i)(1+u)/8+(5+9i)v/4,

subject to ||u|²−1|≤ε, ||1+u|²−2|≤ε, |v|²≤β, ||1+v|²−1|≤η and ||z5|²−709/32|≤η. The unique global minimizing source satisfies

u*=−i sqrt(1+ε);
r*=|u*|²=1+ε; s*=|1+u*|²=2+ε;
v*=x*+iy*, x*=(KP+SQ)/N, y*=(KQ−SP)/N

with the negative-source coefficients defined below. In particular, |v*|²=β, |z5|²−709/32=−η and −η<|1+v*|²−1<η. Its objective is κ*=V(r*,s*,η)−41.

## All-source algebra and support identity

Set r=|u|², s=|1+u|², a=(s−r−1)/2, b=−sqrt(r−a²) on the negative phase, v=x+iy and t=x²+y². Exact expansion of the original 5×3 complex matrix yields

I4=|z4|²=J+Ax+By+16t;
k=|z5|²−709/32=c+Px+Qy+Et,

J=(53+29r)/2+39a−4b, A=36+28a+12b, B=−20−12a+28b,
P=[245(1+a)+123b]/16, Q=[−123(1+a)+245b]/16,
c=709(s−2)/64, E=53/8.

Define N=P²+Q², K=−η−c−Eβ, S=sqrt(Nβ−K²),
L=(AP+BQ)/N, M=(AQ−BP)/N,
x*=(KP+SQ)/N, y*=(KQ−SP)/N,
V=J+LK+MS+16β,
μ=L−KM/S, D=−NM/(2S), τ=D−16+Eμ.

For EVERY real x,y the following is an exact polynomial identity after S²=Nβ−K²:

I4−V = μ(k+η)+τ(β−t)+D[(x−x*)²+(y−y*)²].

The stationarity equalities μP−2Dx*=A and μQ−2Dy*=B, together with Px*+Qy*=K, x*²+y*²=β, prove it by coefficient comparison. Whenever S>0 and μ,D,τ>0, all constraints k≥−η, t≤β imply I4≥V, with equality only at the displayed v*. The candidate is feasible since its h=2x*+β lies strictly in (−η,η).

## Certified uniform parameter bounds

A reproducible Python Fraction/integer-isqrt fixed grid of 10^36 covers r∈[0.999999,1.000001] and s∈[1.999999,2.000001] WITHOUT SAMPLING ε. It adaptively bisects the closed rational η-interval [1/500,39/2000] into 42 adjacent closed subintervals (max bisection depth 7), verifying eleven strict inequalities on EVERY subinterval; 463 new exact tests, all passing.

Conservative strict consequences over the entire continuous three-parameter box:

Nβ−K² > 0.0002; μ > 1.63; D > 3756; τ > 3754;
η+h* > 0.00005; η−h* > 0.0039;
V_r < −3; V_(sη) > 146; V−41 > 3.95.

At the endpoint η=39/2000, the entire r,s box satisfies V_s<−0.0127. Since V_(sη)>146 throughout the lower η strip, V_s stays negative at EVERY smaller η. Thus V decreases strictly with both r and s throughout this strip; the unique negative-phase optimum is r=1+ε, s=2+ε. Hence a=0, b=−sqrt(1+ε) and the claimed u* follows.

For the complete positive-phase source population take one fixed rational λ=39/20. As λ≥0 and 16−Eλ>0, k≤η, t≤β and Cauchy–Schwarz give

I4 ≤ F = J+λ(η−c)+(16−Eλ)β+sqrt(β)*sqrt((A−λP)²+(B−λQ)²)

where b=+sqrt(r−a²). Uniform exact interval checks give F<41 and 82−V−F>1/40000 over the entire r,s,η box. The actual minimum lower certificate for 82−V−F exceeds 2.976450144196826×10^(−5). Therefore every positive-phase feasible source has

|I4−41| ≥41−F > V(1+ε,2+ε,η)−41,

which establishes unique FULL-source minimization, including all coherent complex phases.

## New information and limits

This closes the entire previously missing η strip [0.002,0.0195] in the original static five-Port model. Its endpoint joins PREFIX-424's [0.0195,0.01956] full-source transition theorem: for ε>0 the upper s-corner remains globally optimal until η_A(ε), then the unique interior optimizer slides to the lower s-corner at η_B(ε). For ε=0 the two bounds s=2±ε coincide. “Corner failure” concerns the two u-baseline observations; earlier v-Port active-set changes were separately analyzed in PREFIX-420.

Proof-certificate provenance: the exact predecessor checker's 1448 assertions were rerun; PREFIX-425 delta passed 463 additional assertions across 42 closed rational cells. An independent SymPy check reconstructed the raw 5×3 complex observers, the complete-square identity, and checked the derivative formulas at a specified algebraic point. Both are author-side checks, not native Result/Review/Admission. The full self-contained checker, independent checker and unedited run logs are also in the local PREFIX425_COMPLETE_RESEARCH_EVIDENCE.tar.gz evidence package.

BRC reuse: COMPOSE_APPLIED on signed complex source branches, joint observer constraints and provenance; the proof certifies the optimization-specific fibre reduction rather than assuming a total-only collapse. This external static model is not yet mapped to native P000 X6/three-dimensional-slice dynamics or executed as typed BRC.

Next PREFIX-426: extend η beyond η_B, and locate a certified first failure of either k=−η / |v|²=β activity or global negative-phase dominance, with exact coherent witness and preserved joint observations. 

Ownership boundary as actually observed: GitHub user awdawmip has repository push permission; native control listing returned CONTROL_QUOTA and native researcher session creation returned STATIC_READONLY_SCOPE_DENIED. No verified current native owner, CLAIM, Result, Review or Admission is asserted.
