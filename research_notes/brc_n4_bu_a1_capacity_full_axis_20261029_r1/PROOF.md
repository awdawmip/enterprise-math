# BRC N=4 BU observer: exact full a=1 minimax boundary-axis theorem

2026-10-29 Asia/Shanghai. **AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Frozen model and statement

This theorem is about the external, strictly positive, sixteen-leaf P/Q causal stopping model, NOT a native P000 X6 or physical theorem. The terminal observer is (T,Decision,Z_BU), retaining the BU source bit. The instantaneous conditional behavioral classes S2 and S23 are precisely those in the full causal reduction at immutable Enterprise Math commit `1a4898a57e952245eeacb38be7adf109faa49f49`. The target is F=(a,b,1,0), with a=1 and real 0<b<=1.

**Theorem** (continuum, all admissible randomized causal strategies): 

```
d2(1,b)=d23(1,b)=b(2-7b)/(8(1+2b))  when 0<b<=2/7;
                 =0                    when 2/7<=b<=1.
```

This determines the entire a=1 boundary, including the formerly unsolved low-rho capacity-infeasible sector 0<b<rho, rho=(sqrt(5889)-25)/329. It is conditional on the exact observer-preserving 16-leaf reduction, which is author-proved and awaits independent review.

## Reduction and actual observable events

The reduced feasible variables satisfy 0<=A,B,u<=1, 0<=U<=A, 0<=V<=B. Define

```
s=(A-1+B-b)/2; t=(A-1+3(B-b))/4; H=Bu/4;
rQ=1/6-Au/6-U/3-V/4;  rP=1/6-Au/6-U/12-V/2;
DeltaQ=(s,H-s-rQ,rQ,-H);
DeltaP=(t,H-t-rP,rP,-H);
e=max(||DeltaQ||_1,||DeltaP||_1)/2.
```

Components refer to the four terminal observable atoms [(1,Q,0),(2,Q,0),(3,P,0),(3,Q,1)]. For either P or Q law, e bounds the absolute signed probability difference for every subset/event of these atoms.

## NEW universal capacity/event certificate: e>=bu/4

For law P, the event consisting of atoms 1–3 (zero-based indices 0,1,2) has signed difference H; the event of the middle two atoms (indices 1,2) has signed difference H-t. Thus e>=H and e>=H-t. Since a=1, A<=1 gives t=(A-1+3(B-b))/4 <= 3(B-b)/4. If B>=b, e>=Bu/4>=bu/4. If B<b,

```
e >= Bu/4 - t >= Bu/4+3(b-B)/4
  >= Bu/4+(b-B)u/4 = bu/4       (0<=u<=1).
```

This certificate applies to every lawful real tuple, without assuming any candidate strategy or optimized B. It retains actual BU provenance and uses only measurable terminal events and first-layer capacity A<=1.

## Full continuum lower bound by exact stitching

The previous sharp-rho proof at immutable `55d5a6f9ed278a01b36f89952b76e3fe7641a9c3` derived the following valid convex event TV certificates:

```
e>=L0(u)=[4-14b-3u-(1+3b)u^2]/[2(23-2u)]  (0<=u<=3/7)
e>=L3(u)=u[1-(1+3b)u]/[2(7-2u)]            (0<=u<=1).
```

L0 is strictly decreasing on [0,3/7]: the numerator of its derivative (positive denominator suppressed) equals 2u^2-46u-61+b(6u^2-138u-28)<0 throughout that interval. The derivative numerator of L3 is 7-14(1+3b)u+2(1+3b)u^2, strictly decreasing on [0,1], hence L3 has no interior strict minimum on any subinterval.

For 0<b<=2/7 put w=(2-7b)/(2+4b) and E=bw/4. Symbolic identities L0(w)=L3(w)=E hold. We have w>=3/7 iff b<=8/61.

**Case I: 0<b<=8/61**. Exact factorizations:

```
L0(3/7)-E = (b-2)(61b-8)/[280(2b+1)] >=0,
L3(3/7)-E = (31b-6)(61b-8)/[2408(2b+1)] >=0.
```

For u in [0,3/7], monotonicity gives e>=L0(u)>=L0(3/7)>=E. For u in [3/7,w], the endpoint-minimum property gives e>=L3(u)>=min(L3(3/7),L3(w))=E. For u in [w,1], the new universal event bound gives e>=bu/4>=E.

**Case II: 8/61<=b<=2/7.** Now 0<=w<=3/7. For u in [0,w], e>=L0(u)>=L0(w)=E. For u in [w,1], e>=bu/4>=E. Thus e>=E for every real u and every admissible causal competitor.

## Matching actual causal strategies

When 0<b<=2/7, choose A=1, B=b, u=w, U=b(1+w), V=b. Legal since 0<=w<=1, U<=2b<=4/7<1=A, V=B. The common time-two AU/BU kernel and BU-dependent time-three decisions realize an S23 behavioral strategy. Exact signed atom differences:

```
DeltaQ=(0,E,0,-E),   DeltaP=(0,0,E,-E).
```

Therefore both law TVs equal E, completing the minimax sandwich. For b>=2/7 choose A=1,B=b,u=0,U=V=2/7. The bounds U<=A and V<=B hold and both signed atom vectors vanish, proving the zero branch.

## Exact capacity collision and falsification of unconstrained-root extension

If C in (0,1) solves the previous low-cone quadratic, write D(C)=3C^2+8C+14, r=b/a=(1-C)(4+C)/D(C), h=bC/(4+C)=aC(1-C)/D(C). Then a+3h=a(11C+14)/D(C). The exact root-strategy feasibility boundary is

```
a_cap(C)=D(C)/(11C+14);
b_cap(C)=(1-C)(4+C)/(11C+14).
```

For C=1/2, r=3/25, a_cap=25/26, b_cap=3/26. At a=1,b=3/25 the unconstrained root loss is h=1/75 but the old root policy requires A=26/25>1 and hence is inadmissible. The present true minimax equals E=87/6200, strictly exceeding h by 13/18600. This exact rational witness distinguishes an infeasible extrapolation from an actual optimum.

## Verification, authority, and limits

Executed local `VERIFY.py` checks 32 exact SymPy identities, builds 16 strictly positive P and Q leaves and normalizes both laws, and validates complete BU-labelled terminal TV losses for nine exact rational b values including 8/61 and 2/7. `VERIFY_EVIDENCE.txt` records literal stdout. Continuum optimality is by analytic universal TV event certificates + matching policies, not finite tests. No native formal CLAIM, Result, independent Driver admission or native P000 transfer is asserted.

Frozen global knowledge `GLOBAL_KNOWLEDGE_V1 main@4b3659222a1886c4643af5bdc6a867c745d65043`; initial Enterprise Math scientific `main@8168b9667b766ce95c681e67628de6af10fdec3b`. Read global bootstrap, manual, BRC/math policy, ACTIVE worldview, project P000 V5 and X6/independent time, joint-observer preservation, portable research and current authority. Authenticated GitHub user awdawmip; Site gateway reported research_authority_granted=false; fresh native control_tasks/dispatch requests returned CONTROL_QUOTA, so current owner remains unverified. This is author-side portable research on a declared external finite P/Q BRC model; future O enhancements (Z_AU or time-four), native X6 Cell, three-dimensional slice, separately typed time dynamics and physical validity require independent transfer proofs.

## Next discriminating problem

Solve the remaining interior wedge 0<a<1, 0<b/a<rho, a+3h>1. The new e>=bu/4 bound used the a=1 equality in t and does not transfer unchanged when a<1; derive the exact first-layer-capacity correction and match a lawful A=1 strategy with an event dual certificate on a nonempty 2D region, or a strict rational counterexample. See NEXT_TASK.md.