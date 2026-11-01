# BRC N=4 BU: rho is the genuine global minimax root-to-E0 phase boundary

2026-10-29. **AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.**

## Frozen scope and definitions

This is solely an external strictly positive sixteen-leaf dual P/Q stopping model, under the terminal observer (T, Decision, Z_BU), including the BU source identity, and the instantaneous behavioral causal S2/S23 policy classes. It does not prove an embedding into P000 native X6 Cell geometry, a three-dimensional slice, independent time dynamics, or physical observations. Reuse the full sixteen-leaf causal reduction at Enterprise Math immutable source 1a4898a57e952245eeacb38be7adf109faa49f49 and the previous optimal one-splice certificate at 9bf7867bb34ae3737630a145286dc80a73b46e1a. Their independent scientific review remains open.

For 0<a<=1 and 0<b<=1 the target is F=(a,b,1,0). All real lawful behavioral competitors have A,B,u,U,V satisfying 0<=A,B,u<=1; 0<=U<=A and 0<=V<=B. The target-minus-competitor signed four-observation-atom vectors are

    s=(A-a+B-b)/2,
    t=(A-a+3(B-b))/4,
    H=B*u/4,
    rQ=a/6-A*u/6-U/3-V/4,
    rP=a/6-A*u/6-U/12-V/2,
    DeltaQ=(s,H-s-rQ,rQ,-H),
    DeltaP=(t,H-t-rP,rP,-H).

The objective e=max(||DeltaQ||_1,||DeltaP||_1)/2 equals the minimax objective for the original S2 and S23 stopped-process policy classes via the cited observer-preserving pathwise reduction.

## Theorem: complete upper cone for every a

Let rho=(sqrt(5889)-25)/329, approximately 0.15726389109969204, and w=(2a-7b)/(2a+4b).

For every real 0<a<=1 and rho*a <= b <= 1, optimizing over **all** legal real causal randomized competitors gives the exact common value

    d2(a,b)=d23(a,b)=
        b(2a-7b)/[8(a+2b)]     for rho*a <= b <= 2a/7,
        0                       for 2a/7 <= b <= 1.

In particular the upper-cone claim requires no A=a+3h<=1 capacity hypothesis. Both endpoints are included.

For 0<b/a<2/7, let C be the unique root in (0,1) of

    (a+3b)C^2+(3a+8b)C+14b-4a=0

and h=bC/(4+C). The inherited low-cone proof gives d2=d23=h for b/a<=rho whenever a+3h<=1. On b/a=rho, the present upper-cone theorem gives d2=d23=h even if that root-attaining strategy is inadmissible. For every rho<b/a<2/7, the upper-cone optimum is **strictly smaller** than h. Therefore rho is the *true* global departure point of the root-valued minimax phase, not just the sharpness threshold for the old single-splice L0/L3/K proof.

The only unsolved small-r sector relevant to this statement is b/a<rho with a+3h>1, where the root-attaining construction exceeds first-layer capacity. This theorem does not claim a full phase diagram there.

## Three legal observable-event TV certificates

The prior four-atom event-mixture identities, independently symbolically checked again, give the following universal lower bounds e>=L0(u) on 0<=u<=3/7 and e>=L3(u),K(u) on 0<=u<=1:

    L0(u)=[4a-14b-3au-(a+3b)u^2]/[2(23-2u)],
    L3(u)=u[a-(a+3b)u]/[2(7-2u)],
    K(u)=bu/(4+u).

These are nonnegative convex combinations of **actual terminal observable event differences** with a nonpositive correction proportional to V-B. The event weights sum to the positive denominators 23-2u, 7-2u, 4+u, respectively; the nonnegative coefficient intervals are exactly the stated domains. No source bit is silently discarded.

L0 is strictly decreasing on [0,3/7], because its derivative numerator is

    a(2u^2-46u-61)+b(6u^2-138u-28)<0.

The derivative numerator of L3 is

    7a-14(a+3b)u+2(a+3b)u^2,

which strictly decreases on [0,1], so L3 has at most one interior critical point, a maximum; its minimum on each subinterval occurs at an endpoint. K is increasing.

## New variable three-piece stitching proves the global high-cone lower bound

Fix rho<=r=b/a<2/7. Define w=(2-7r)/(2+4r) and E0=bw/4. Let C and h be as above.

Since rho>3/20>8/61, we have 0<w<=3/7. Solving the C-root equation for the ratio yields

    r(C)=(1-C)(4+C)/(3C^2+8C+14),
    w(r(C))=C(13C+37)/[2(C^2+2C+22)],
    C-w(r(C))=C(1-C)(7-2C)/[2(C^2+2C+22)]>0.

Thus 0<w<C<1. Substitution gives the exact anchor identities

    L0(w)=L3(w)=E0,
    L3(C)=K(C)=h.

Define Ccrit=(sqrt(5889)-73)/10. It is the unique positive root of 5C^2+73C-28=0, and r(Ccrit)=rho. Since r(C) strictly decreases for 0<C<1, r>=rho means C<=Ccrit. The exact factorization

    (h-E0)/a =
      C(C-1)(5C^2+73C-28)
      /[8(C^2+2C+22)(3C^2+8C+14)]

therefore yields h>=E0, with equality exactly at rho, and strict inequality when r>rho.

For **every** legal competitor with any real continuation u∈[0,1], divide into:

    0<=u<=w: e>=L0(u)>=L0(w)=E0;
    w<=u<=C: e>=L3(u)>=min(L3(w),L3(C))=E0;
    C<=u<=1: e>=K(u)>=K(C)=h>=E0.

No finite-grid extrapolation is involved. This covers all possible causal competitors under the exact four-atom reduction.

## Matching lawful S23 strategy and zero branch

For rho<=b/a<=2/7 choose

    A=a, B=b, u=w=(2a-7b)/(2a+4b),
    U=b(1+w), V=b.

Because 0<=w<1 and b<=2a/7, the first-layer rates are <=1, V=B, and U<=2b<=4a/7<a=A. The same AU/BU time-two kernel is used; AV continues at U/A and BV at V/B=1. This is a legal real behavioral S23 strategy. Direct substitution gives the full signed observer differences

    DeltaQ=(0,E0,0,-E0),
    DeltaP=(0,0,E0,-E0).

Hence TV_Q=TV_P=E0, attaining the analytic universal lower bound.

When b>=2a/7 choose A=a, B=b, u=0, U=V=2a/7. Both signed four-atom differences vanish exactly and all conditional rates are legal; the minimax is zero. This includes b=2a/7 by continuity and direct substitution.

## Exact lawful rational counterexample to the old root formula beyond rho

The previous theorem's c*=9/25, b/a=1744/10793 example was only known as a failure of its **certificate family**. The following explicitly lawful competitor turns it into a strict, genuine minimax root-formula counterexample:

    a=1/2, b=872/10793, C=9/25,
    root candidate h=72/10793,
    u=w=4689/14281,
    A=1/2, B=872/10793,
    U=16541840/154134833, V=872/10793,
    true TV_Q=true TV_P=E0=1022202/154134833,
    h-E0=6030/154134833>0.

The root-attaining candidate also satisfies its capacity constraint at this point, so the strict improvement is not a feasibility artifact. The full 16 strictly positive Q/P leaf masses, normalized law distributions and terminal observer TV values were recomputed using exact Fraction arithmetic.

## Verification, provenance, and limits

The complete local author-side verifier ran 32 exact symbolic identities (including the L0/L3/K mixture identities and coefficient sums, factorization, both strategies' observed atoms, and the zero policy) and exact sixteen-leaf P/Q reconstructions for four rational high-cone examples, the exact rational root competitor, and a zero-loss witness. The full executable verifier and stdout are included in the companion user-facing research evidence archive. The concise published verification source and evidence are provided beside this proof; its checked scope must be read from that exact file rather than assumed identical to any longer local verifier. Continuous-real optimality comes from the preceding analytic argument, not from finite test counts.

Frozen source snapshots: GLOBAL_KNOWLEDGE_V1 main@0d4f6f9957a0e636c207d4c6fc4585463e72a96c and Enterprise Math initial scientific input main@054560e20268196aa73885c4f2eb5c05c7e21ab0. P000 current startup projection blob matched its original global canonical blob; project P000 V5, active worldview, joint-observer preservation rule, and current portable research protocol were read. Actual authenticated GitHub user: awdawmip. Native Site authorization reported research_authority_granted=false and a fresh bounded owner query returned CONTROL_QUOTA. No formal owner/CLAIM/native Research-Activity/Result/independent Driver review is asserted; this is **author-side portable research**, stored for independent mathematical review, not admitted Foundation or Working Truth.

Observer fidelity: 16-leaf-to-four-atom collapse is established only under the exact terminal (T,Decision,Z_BU) readout for P/Q law TV. Future operations, time-four information, extra AU source bits, a native six-dimensional X6 Cell or three-dimensional slice embedding, and an independent time-dynamics transfer still require separate proofs. The P000 worldview is not modified.

## Next discriminating question

For 0<r=b/a<rho, let C=C(r), h=arC/(4+C); investigate the true minimax in the first-layer **capacity-infeasible** sector a+3h>1. Begin with a rational C and exact r(C), test A=1 strategies against all-event TV dual inequalities, and produce an analytic optimum or a lawful rational falsifier. A separate observer-fidelity track should test added Z_AU/time-four readout and any downstream operation before claiming a stronger compression.
