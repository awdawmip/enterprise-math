# BRC N=4 BU: exact sub-rho capacity-limited minimax pocket

**2026-10-29/30 | AUTHOR_SIDE / CONDITIONAL_ANALYTIC_PROOF / UNREVIEWED / NOT_ADMITTED.** This is an external strictly positive 16-leaf P/Q causal-stopping problem observed through the full BU-labelled terminal joint observer (T,Decision,Z_BU), not a P000 native X6 / three-dimensional slice / physical time theorem. The exact observer-preserving 16-leaf-to-four-atom reduction and universal L0/L3 terminal-event-TV certificates are inherited **author-side** dependencies, not independently admitted.

## New continuum theorem and exact nonoverlap

For *all real parameters* a,b in the closed positive-area rectangle

    49/50 <= a <= 1,          151/1000 <= b <= 77/500,

the source-defined S2 and S23 lawful real randomized behavioral minimax objectives coincide, conditionally on the exact original observer reduction, and equal

    d2(a,b)=d23(a,b)=H(a,b)=b(2a-7b)/[8(a+2b)].

The existing source theorem at `research_notes/brc_n4_bu_sharp_rho_global_phase_20261029_emr1/PROOF.md` already proves this same H for the **different** high-ratio region b/a >= rho, with rho=(sqrt(5889)-25)/329. Our rectangle has b/a <= 11/70 < rho, strictly outside it. Existing E-optimal curved-capacity theorems now extend through b<=3/20, from `research_notes/brc_n4_bu_linear_splice_b3_20_20261030_r11/PROOF.md`; our rectangle has b>=151/1000>3/20 and is outside that source theorem. The already-known a=1 axis is not claimed as new: the new open territory is 49/50<=a<1. The root-attaining construction is capacity-infeasible throughout the rectangle (see G sign below).

## Source-defined finite model and lawful event certificates

The target is F=(a,b,1,0). Every lawful source-reduced S2/S23 competitor is represented by 0<=A,B,u<=1, 0<=U<=A, 0<=V<=B, with full BU-labelled signed four-terminal-atom differences

    s=(A-a+B-b)/2,           t=(A-a+3(B-b))/4,
    J=Bu/4,                  rQ=a/6-Au/6-U/3-V/4,
    rP=a/6-Au/6-U/12-V/2,
    DeltaQ=(s,J-s-rQ,rQ,-J), DeltaP=(t,J-t-rP,rP,-J).

Thus e=max(||DeltaQ||_1,||DeltaP||_1)/2. The inherited **actual terminal observable event** dual mixtures give for every lawful competitor:

    e>=L0(u)=[4a-14b-3au-(a+3b)u²]/[2(23-2u)]  for 0<=u<=3/7,
    e>=L3(u)=u[a-(a+3b)u]/[2(7-2u)]            for 0<=u<=1.

Their positive mixing weights and event domains remain a source-dependent independent-review obligation; they are not asserted as new hidden primitives. Write

    delta=(1-a)/3, Bstar=b-delta, w=(2a-7b)/(2a+4b),
    H=bw/4, T(a,b)=a²+38ab-7a+105b²-14b, v=bw/Bstar.

Direct exact symbolic identities hold for all admissible a,b:

    L0(w)=L3(w)=H.

L0 decreases strictly for 0<=u<=3/7, since its derivative numerator is a(2u²−46u−61)+b(6u²−138u−28)<0. L3 has no interior minimum on any subinterval of [0,1], since its derivative numerator 7a−14(a+3b)u+2(a+3b)u² strictly decreases, so any stationary point is a maximum.

**Capacity-plus-event certificate**: the first-three-atom P-observable event has difference J, and its middle-two-atom event has difference J−t, hence e>=J and e>=J−t. Since A<=1, t <= [1-a+3(B-b)]/4 = 3(B-Bstar)/4. For B>=Bstar, e>=Bu/4>=Bstar*u/4. For B<Bstar, e>=Bu/4+3(Bstar-B)/4>=Bstar*u/4 because u<=1<=3. Thus for every lawful competitor and any u in [0,1],

    e>=Bstar*u/4                        (CAP)

provided Bstar>0; this preserves source identity.

## New dual splice and proof over *all real continuations*

For the parameter domain defined above, 0<w<=3/7, Bstar>b/2>0 and w<=v<6/7<1. Exact factorization gives

    L3(v)-H =
      -b(a-1)(2a-7b)T(a,b)
      / [8(a+2b)(a+3b-1)(7a²+29ab-7a+63b²-14b)].

Every denominator factor is positive. Indeed a+3b−1=3Bstar>0 and the final factor equals (a+2b)(a+3b−1)(7−2v)>0. Consequently T>=0 and a<=1 imply L3(v)>=H. In the *full continuum* of lawful competitor continuations u:

    0<=u<=w: e>=L0(u)>=L0(w)=H;
    w<=u<=v: e>=L3(u)>=min(L3(w),L3(v))>=H;
    v<=u<=1: e>=Bstar*u/4>=Bstar*v/4=H.

The lower bound is global, not inferred from a finite grid.

An attaining genuine causal policy is

    A=a, B=b, u=w, U=b(1+w), V=b.

The entire box has b/a<2/7, 0<w<=3/7, U<2b<=77/250<a, V=B; all conditional behavior rates are lawful. Its full BU-observer signed differences are DeltaQ=(0,H,0,-H), DeltaP=(0,0,H,-H). Thus TV_Q=TV_P=H, which matches the lower bound and proves the stated minimax conditional on the inherited source reduction and dual lemmas.

## Exact rational rectangle verification

b/a <= (77/500)/(49/50)=11/70, and exactly

    5889 - (25+329*(11/70))² = 611/100 >0,

so b/a<rho. Also b/a>=151/1000>8/61, which yields w<=3/7. Because delta<=(1−49/50)/3=1/150 < b/2, we have Bstar>b/2 and v=(b/Bstar)w<2w<=6/7.

For T, derivatives T_a=2a+38b−7>0 and T_b=38a+210b−14>0 on the box. Hence

    T >= T(49/50,151/1000) = 749/200000 >0.

For the prior root-capacity polynomial G=5a²+8ab−21b²−2b−5, G_a=10a+8b>0 and G_b=8a−42b−2<0 on this rectangle, so

    G >= G(49/50,77/500) = 50831/250000 >0.

The inherited exact capacity-boundary criterion G=0 at a=alpha(b) therefore certifies a>alpha(b), where alpha(b)=(sqrt(121b²+10b+25)−4b)/5. This is precisely the previously unresolved **sub-rho capacity-infeasible** territory, not an old feasible-root result.

## Additional strict rational witness outside the rectangle

At a=97/100, b=19/125 (which satisfies the general three-piece splice premises but lies below the rectangle's a-minimum), the same proof gives

    w=219/637, v=16644/45227,
    TV_Q=TV_P=H=4161/318500,
    E=(a+3b−1)(7−a−21b)/[12(4a+12b+2)]=33583/2568000,
    E−H=859/65432640>0,
    L3(v)−H=3574299/256257086540>0.

Its ratio b/a=76/485<rho. Therefore an *unrestricted extrapolation* of the earlier E formula fails beyond the actually proven b<=3/20 domain, even within b/a<rho. No valid earlier E theorem is contradicted.

The algebraic E−H identity is exactly (1−a)T(a,b)/[24(a+2b)(2a+6b+1)]. For interior a<1 the new box has E>H, showing a strict change of attainable optimum relative to an unsupported E extrapolation.

## Executed evidence, source and limits

The companion `VERIFY.py` was locally run with exact SymPy and fractions.Fraction arithmetic: 23 exact symbolic identities and 6 exact rational parameter witnesses with both full 16 strictly positive normalized P/Q leaves and source-labelled terminal TV distributions. Literal stdout is `VERIFY_EVIDENCE.txt`. These tests verify the actual policies and displayed algebra, not the continuum quantifiers or independent reviewer status.

Scientific source pin: Enterprise Math main@84b725104b07628241b4a12be4d77b423ebf6c0f. Inherited reduction from immutable commit 1a4898a57e952245eeacb38be7adf109faa49f49; universal L0/L3 event duals in the high-rho proof cited above and original source d78e2b5729c824918126aec8ffb26ff3e5dc4cb5. Existing b<=3/20 author-side theorem and the earlier b<=37/250 affine theorem are both preserved. GLOBAL_KNOWLEDGE_V1 current main@b5a4c88d7e9d5040ad4ab233b023720ea9b3070a, P000 frozen source pin retained separately, ACTIVE Heartbeat X6+1 typed time and joint-observer provenance constraints apply. No native X6, added AU/time-four, three-dimensional slice or physical time correspondence has been proved.

Native Site is read-only (`research_authority_granted=false`, `write_relay_enabled=false`, no legitimate current Driver DA). This branch is portable **author-side** mathematics, with `REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`. It is not an official Task, frozen Result, independent Review, Reference, Synthesis, Follow-up or Foundation promotion. No old frozen F7 Result or reviews are modified. No `sorry`, `admit` or unsupported custom target axiom is used; inherited duals are explicit review obligations.

**Next discriminating work:** with genuinely independent authority, audit the observer-preserving sixteen-leaf reduction and both L0/L3 positive event dual mixtures. Then determine the sharp two-variable boundary T=0 or v=1 between the newly proved H-optimal pocket and the E-optimal region, without duplicating existing canonical tasks. Formal new tasks still require current Source, legitimate Driver authority and immutable V2 publication admission.
