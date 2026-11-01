# BRC N4 BU: exact 2D low-b root phase, completing a positive-b strip

2026-10-29 (Asia/Shanghai). AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Domain and result

Freeze the positive 16-leaf P/Q stopping tree with complete terminal observer O=(T,Decision,Z_BU), immediate behavioral S2/S23 causal policies, and the independently re-derived full-causal four-observation reduction in Enterprise Math commit 1a4898a57e952245eeacb38be7adf109faa49f49, research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md. With 0<=A,B,c<=1, 0<=U<=A, 0<=V<=B, this exact reduction has signed atom differences

    s=(A-a+B-b)/2, t=(A-a+3(B-b))/4, H=B*c/4;
    rQ=a/6-A*c/6-U/3-V/4, rP=a/6-A*c/6-U/12-V/2;
    DeltaQ=(s,H-s-rQ,rQ,-H), DeltaP=(t,H-t-rP,rP,-H),
    e=max(||DeltaQ||_1,||DeltaP||_1)/2.

**Theorem.** For ALL real 97/100<=a<=99/100 and 0<b<=1/100, let c* be the unique root in (3/7,1) of f(c)=(a+3b)c²+(3a+8b)c+14b-4a=0. Then, over ALL lawful real S2/S23 randomized causal policies,

    d2(a,b)=d23(a,b)=b*c*/(4+c*).

This settles the previously open entire two-dimensional 0<b<1/100 strip. Composing with the previously published author-side [1/100,307/2100] and [307/2100,1] b-phase proofs produces an author-side exact chart for the full 97/100<=a<=99/100, 0<b<=1 rectangle. Earlier high-b certificates remain subject to independent review.

## Unique root and lawful matching competitor

For c>=0, f'(c)=2(a+3b)c+3a+8b>0. Furthermore f(3/7)=-(124a-881b)/49<0 since 124a-881b>=11147/100, and f(1)=25b>0. Let H=b*c*/(4+c*) with 0<H<b/5<=1/500. Define the ACTUAL S23 strategy

    A=a+3H, B=4b/(4+c*), c=c*, U=B(1+c*), V=B.

It is legal: 0.97<=a<A<0.99+0.006=249/250<1, 0<B<=b<=1/100, U<=2b<=1/50<A and V=B. Its continuation rates on AV,BV are U/A and V/B=1; time-three stops are implemented using the current-likelihood BU versus non-BU decision. The root relation can be rearranged as b=a(1-c)(4+c)/(3c²+8c+14). Direct substitution into the exact P and Q atom differences gives DeltaQ=(H,0,0,-H), DeltaP=(0,0,H,-H), so both TV losses attain H.

## Universal TV lower bound and exact cover of c∈[0,1]

Use only actual observable-event signed differences
Q1=s, Q2=H-s-rQ, Q3=H-rQ, Q7=H, P4=rP, P5=t+rP, P6=H-t.
Each is at most the respective two-law max TV error e. For every lawful A,B,U,V, the following nonnegative event-mixture dual certificates hold:

    L0(c)=[4a-14b-3ac-(a+3b)c²]/[2(23-2c)] <= e, for 0<=c<=3/7;
    L3(c)=c[a-(a+3b)c]/[2(7-2c)] <= e, for 0<=c<=1;
    K(c)=bc/(4+c) <= e, for 0<=c<=1.

Precisely: the L0 mixture uses events (Q2,H-s,P4,P5) with nonnegative weights (c+4,3-7c,2(1+4c-c²),2(c²-2c+7))/(23-2c) summing to 1, plus correction 7(c+4)(V-B)/[4(23-2c)]<=0. The L3 mixture uses (Q3,Q7,P4,P5), weights (c,7(1-c),2c(2-c),2c²)/(7-2c), plus correction 7c(V-B)/[4(7-2c)]<=0. K is exactly the convex combination (c Q1+(4-2c)Q7+2c P6)/(4+c). These symbolic identities are checked in VERIFY.py. In particular the BU-bit provenance is retained.

L0 strictly decreases on [0,3/7], since its derivative numerator is a(2c²-46c-61)+b(6c²-138c-28)<0. The derivative of L3 has sign D(c)=7a-14(a+3b)c+2(a+3b)c² with D'(c)=4(a+3b)(c-7/2)<0 over [0,1]. Hence L3 has NO interior minimum on any closed subinterval: a stationary point, if any, is a maximum.

For fixed c=3/7, L0 and L3 each increase with a and decrease with b. Their exact derivative signs follow from (4-3c-c²)/[2(23-2c)]>0, -(14+3c²)/[2(23-2c)]<0, c(1-c)/[2(7-2c)]>0, -3c²/[2(7-2c)]<0. Exact corner computations give

    L0(3/7) >= L0(3/7;97/100,1/100) = 73/1400 >1/500;
    L3(3/7) >= L3(3/7;97/100,1/100) = 1137/60200 >1/500.

The exact identity L3(c)-K(c)=-c f(c)/[2(7-2c)(4+c)] gives L3(c*)=K(c*)=H. Because K increases with c, ANY real competing c is covered:

    c in [0,3/7]: e>=L0(c)>=73/1400>1/500>=H;
    c in [3/7,c*]: e>=L3(c)>=min(L3(3/7),L3(c*))=H;
    c in [c*,1]: e>=K(c)>=K(c*)=H.

This is a universal analytic lower bound over the entire lawful parameter space, matched by the constructed strategy; no finite sampling extrapolation is used.

## Reproducibility, status and next unit

The executed exact SymPy verifier checks all event-dual identities, f root parametrization, L0/L3 derivatives, endpoint inequalities, signed policy vectors and three exact rational policies:
(a,b,c*,TV_P=TV_Q)=(97/100,3201/324100,19/20,1843/972300); (99/100,3069/381950,24/25,297/190975); (49/50,34993/178471450,999/1000,6993/178471450).
The output PASS_EXACT_BRC_N4_BU_LOW_B_2D_CLOSURE is in VERIFY_EVIDENCE.txt. The whole 16-leaf causal mapping is proved and checked separately in the predecessor commit, not rerun here.

Fixed GLOBAL_KNOWLEDGE_V1 snapshot main@99ce00fffc6ecc6426729ce702d8e787f0d336bd, initial EM input main@2528561531a335c545c1312bf9a1ed16f8d0df3c. Actual GitHub identity awdawmip, no native active research authority/CLAIM/Result, current owner not verified. This is external finite-model author work, UNREVIEWED/NOT_ADMITTED, with no fidelity theorem into P000 X6 space, three-dimensional slices, native rotation or independent physical time.

Next: locate the first a-strip boundary where L0/L3/K/R certificates or causal capacity fail, or refine O by AU lineage or time-four timing and find the minimal observer-safe state/actual rational falsifier.
