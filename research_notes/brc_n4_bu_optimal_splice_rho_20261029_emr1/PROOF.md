# BRC N=4 BU: optimal one-splice L0/L3/K certificate and expanded exact root phase

2026-10-29 Asia/Shanghai. AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. This is an external strictly-positive 16-leaf dual-law stopping model with terminal observer (T,Decision,Z_BU), not a P000/X6 native-dynamics result.

## Input, authorship, and exact scope

Reuse the author-side observer-preserving S2/S23-to-four-atom causal reduction at Enterprise Math commit 1a4898a57e952245eeacb38be7adf109faa49f49, research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md, and the certificate definitions from 04e1f2d40fcb5debdd17d75a67c376e407bf9dfa, research_notes/brc_n4_bu_global_small_b_cone_20261029_t11/PROOF.md. Their independent review is outstanding; conclusions here depend on the correctness of the declared external four-atom reduction.

The target policy is F=(a,b,1,0), with 0<a<1 and 0<b. A competitor has A,B,u,U,V real, 0<=A,B,u<=1, 0<=U<=A, 0<=V<=B. Define

    s=(A-a+B-b)/2; t=(A-a+3(B-b))/4; H=B*u/4,
    r_Q=a/6-A*u/6-U/3-V/4,
    r_P=a/6-A*u/6-U/12-V/2,
    Delta_Q=(s,H-s-r_Q,r_Q,-H),
    Delta_P=(t,H-t-r_P,r_P,-H),
    e=max(||Delta_Q||_1,||Delta_P||_1)/2.

The event-mixture certificates established by the cited author-side representation are

    L0(u)=[4a-14b-3au-(a+3b)u^2]/[2(23-2u)],  0<=u<=3/7,
    L3(u)=u[a-(a+3b)u]/[2(7-2u)],              0<=u<=1,
    K(u)=bu/(4+u),                               0<=u<=1,

all <= e at their stated ranges. The actual witness combinations are rechecked symbolically in VERIFY.py.

## The improved continuous-real theorem

Define the exact algebraic constants

    rho=(sqrt(5889)-25)/329  = 0.157263891099692...,
    c0=(sqrt(5889)-73)/10   = 0.373982017179868...,
    k0=(87-sqrt(5889))/30   = 0.342005994273377... .

For every real 0<a<1 and 0<b<=rho*a, let c* be the unique root in (0,1) of

    f(c)=(a+3b)c^2+(3a+8b)c+14b-4a=0,

and put h=b*c*/(4+c*). If the exact capacity condition

    a+3h<=1

holds, then for every legal real causal randomized competitor,

    d2(a,b)=d23(a,b)=h.

The simpler sufficient condition a+3b/5<=1 may replace the exact capacity condition. The new slope rho exceeds the predecessor 60/737 by approximately a factor 1.93. It is **the exact limit of the explicitly specified L0/L3/K one-splice certificate family**, NOT a proved global minimax phase-switch boundary.

## Algebraic backbone and lower bound

Let r=b/a and D(c)=3c^2+8c+14. Since rho<2/7, f(0)=14b-4a<0, f(1)=25b>0, and f'(c)>0 on [0,1], the root is unique. Solving f(c*)=0 gives

    r(c)=(1-c)(4+c)/D(c),
    h/a=c(1-c)/D(c),
    r'(c)=(c^2-52c-74)/D(c)^2<0 for 0<c<1.

The constants satisfy 329rho^2+50rho-16=0, 5c0^2+73c0-28=0, 15k0^2-87k0+28=0, r(c0)=rho and k0=14(1-c0)/(26-c0). Thus r<=rho implies c*>=c0>k0, while 0<k0<3/7.

For arbitrary 0<k<3/7, substituting r(c)=b/a into the event gaps yields exact identities (L/a means the same L evaluated with a=1,b=r(c)):

    [L0(k)-h]/a =
      [13c^2 k-72c^2-c k^2+20c k-28c+26k^2+42k]
      /[2(2k-23)D(c)],

    [L3(k)-h]/a =
      [(c-k)(c k-14c-26k+14)]/[2(2k-7)D(c)].

At k=k0 and c=c0 both gaps vanish. In the L0 expression the quadratic numerator as a function of c has a negative leading and a negative linear coefficient for k=k0, so it strictly decreases for c>0. Its denominator is negative, hence L0(k0)>=h for c>=c0. In the L3 expression, c>k0 and 2k0-7<0; the second factor is zero at c0 and strictly decreases in c, hence L3(k0)>=h for c>=c0.

L0(u) is strictly decreasing on [0,3/7]: its derivative numerator is a(2u^2-46u-61)+b(6u^2-138u-28)<0. L3(u) has no interior minimum on [0,1], since its derivative numerator 7a-14(a+3b)u+2(a+3b)u^2 is strictly decreasing for u<=1. The exact root relation is

    L3(c)-K(c)=-c*f(c)/[2(7-2c)(4+c)],

so L3(c*)=K(c*)=h. As K is increasing, the full continuum of competitor continuations is covered:

    0<=u<=k0:   e>=L0(u)>=L0(k0)>=h;
    k0<=u<=c*:  e>=L3(u)>=min(L3(k0),L3(c*))>=h;
    c*<=u<=1:   e>=K(u)>=K(c*)=h.

This proves a universal lower bound without parameter sampling.

## Matching legal strategy and observability

Set

    A=a+3h, B=4b/(4+c*), u=c*,
    U=B(1+c*), V=B.

The assumption gives A<=1. Also B<=b<=rho*a<1, and U<=2b<=2rho*a<a<=A; V=B. These are genuine legal behavioral S23 rates: shared AU/BU continuation c*, AV rate U/A, BV rate V/B, with BU source identity retained in the terminal readout. Substitution modulo f(c*) gives

    Delta_Q=(h,0,0,-h),  Delta_P=(0,0,h,-h),

therefore both TV distances equal h. The preceding author-side causal reduction transfers the result to d2. The verifier checks the eight symbolic atom equalities and five exact 16-leaf rational witnesses.

## Certificate-family sharpness; not a strategy counterexample

For a root c in (0,1), consider any single split k with 0<=k<=min(c,3/7), requiring simultaneously L0(k)>=h and L3(k)>=h. At k=c, L0(c)<h, so only k<c can qualify. The factorization of L3(k)-h above forces

    k>=k_req(c):=14(1-c)/(26-c).

If k_req(c)>min(c,3/7), the certificate fails. Otherwise L0 decreases, so its best value among admissible k>=k_req is L0(k_req). Exact elimination gives

    [L0(k_req(c))-h]/a =
       [(11c+14)(5c^2+73c-28)]/[5(c+114)D(c)].

This is negative for c<c0. Conversely for c>=c0 the constant k=k0 works. Hence the existence of a valid L0/L3/K *single-splice* certificate is equivalent to c>=c0, or r<=rho, over 0<r<2/7. This does not rule out other observable-event certificates or better causal strategies.

An exact rational witness outside this certificate range is c=9/25, r=b/a=1744/10793, k_req=224/641. At that split, [L0(k_req)-h]/a=-60166/30857187<0. This is **only a failure of this proof scheme**, not a minimax counterexample.

## Executed verification, provenance, and next issue

The locally executed SymPy/Fraction verifier checked 28 symbolic identities (including three event-mixture identities, eight attainable-delta relations, threshold eliminations), reconstructed the same 16 strictly positive P/Q leaf masses, and tested five exact rational strategies. It printed PASS_BRC_N4_BU_OPTIMAL_L0_L3_K_STITCH_20261029. Evidence and source are saved beside this proof. The checks support the stated algebra and concrete strategies; the continuum claim is the analytic argument above. No independent mathematical review or Foundation/Working Truth admission is claimed.

GLOBAL_KNOWLEDGE_V1 pinned snapshot: ba02af17db81592cf9cab0148dbc93f429c5e9c0. Enterprise Math initial scientific input: 3e63f90523a75fc7250c2c603f556578152fc354. Actual GitHub account: awdawmip. Source-native service observed research_authority_granted=false and the owner-inventory request returned CONTROL_QUOTA, so no native CLAIM or active-owner assertion is made.

Next discriminating unit: at r just above rho, search for a genuinely new observable-event TV dual (not the exhausted one-splice L0/L3/K family) or an exact rational lawful competitor with e<h. Resolve whether rho is merely certificate sharpness or a true minimax phase boundary, while separately observing the exact capacity wall a+3h=1.