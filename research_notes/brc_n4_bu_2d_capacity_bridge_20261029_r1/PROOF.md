# BRC N4 BU: exact capacity-saturated minimax on a two-dimensional corridor

2026-10-29 Asia/Shanghai; AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model and exact theorem

External strictly positive 16-leaf dual P/Q stopping model, terminal observer O=(T,Decision,Z_BU), instantaneous lawful behavioral causal S2/S23 strategies, target F=(a,b,1,0), and full four-observation-atom reduction from prior author-side immutable commit `1a4898a57e952245eeacb38be7adf109faa49f49`. This is an external mathematical model, not a P000 native-X6, three-dimensional slice, time or physical theorem.

**For ALL real parameters 99/100 <= a <= 1 and 1/10 <= b <= 13/100, the exact global minimum across ALL admissible real randomized S2 or S23 strategies is**

```
d2(a,b)=d23(a,b)=(a+3b-1)(7-a-21b)/[12(4a+12b+2)].
```

The theorem extends the older a<=99/100 rectangle along a genuinely open strip to a=1 and matches the full a=1 capacity-axis theorem (project merged PR #1706).

## Exact four-atom differences and matching legal strategy

The feasible variables obey 0<=A,B,c<=1, 0<=U<=A, 0<=V<=B. Write

```
s=(A-a+B-b)/2; t=(A-a+3(B-b))/4; H=Bc/4;
rQ=a/6-Ac/6-U/3-V/4; rP=a/6-Ac/6-U/12-V/2;
DeltaQ=(s,H-s-rQ,rQ,-H);  DeltaP=(t,H-t-rP,rP,-H).
```

Here e=max(||DeltaQ||_1,||DeltaP||_1)/2, so all observable terminal event differences under P/Q have absolute value <=e. Set `delta=(1-a)/3`, `Bstar=b-delta`, `cstar=(7-a-21b)/(4a+12b+2)`, `Hstar=Bstar*cstar/4`. Exact algebra gives Hstar=(a+3b-1)(7-a-21b)/[12(4a+12b+2)].

Select the genuine S23 causal policy
```
A=1, B=Bstar, c=cstar, U=Bstar*(1+cstar), V=Bstar.
```
It gives exact signed observation differences
```
DeltaQ=(delta,Hstar-delta,0,-Hstar);
DeltaP=(0,0,Hstar,-Hstar).
```
In the stated rectangle, Bstar>=1/10-1/300=29/300>0, cstar>=3/7 and cstar<1, U<=2Bstar<=13/50<1=A, V=Bstar, and Hstar>=(29/300)(3/7)/4=29/2800>1/300>=delta. Thus all rates are legal, all positive TV differences have the displayed signs and both P/Q TV losses are exactly Hstar.

## New universal first-layer-capacity observable-event certificate

Law P's first-three-atom event has signed difference H=Bc/4, and its middle-two-atom event has signed difference H-t. Since A<=1, `t=(A-a+3(B-b))/4 <=3(B-Bstar)/4`. If competitor B>=Bstar, then e>=H>=Bstar*c/4. If B<Bstar, then e>=H-t>=B*c/4+3(Bstar-B)/4>=Bstar*c/4 because c<=1. Hence

```
e >= Bstar*c/4
```

for every feasible competitor and every real c∈[0,1] (on this rectangle Bstar>0). The BU source bit is retained, and these are actual terminal events, not unobservable branch choices. At a=1 this reduces to the full-axis certificate e>=bc/4.

## Exact all-c certificate by L0/L3 stitching

The previously validated observable TV certificates from immutable phase source `55d5a6f9ed278a01b36f89952b76e3fe7641a9c3` are

```
e>=L0(c)=[4a-14b-3ac-(a+3b)c^2]/[2(23-2c)]   for 0<=c<=3/7;
e>=L3(c)=c[a-(a+3b)c]/[2(7-2c)]              for 0<=c<=1.
```

L0 strictly decreases on [0,3/7] since its derivative numerator is a(2c^2-46c-61)+b(6c^2-138c-28)<0. L3 has no interior minimum on any subinterval of [0,1]: the derivative numerator 7a-14(a+3b)c+2(a+3b)c^2 is strictly decreasing on [0,1]. Moreover

```
cstar-3/7 = (43-19a-183b)/[7(4a+12b+2)] >=0.
```

The numerator is minimized at (a,b)=(1,13/100) and equals 21/100>0; also cstar<1 because 5(1-a)<33b on the entire rectangle. Exact substitution shows `L3(cstar)=Hstar`.

For the splice u=3/7, exact expressions:

```
L0(3/7)-Hstar=N0/[840(2a+6b+1)];
N0=131a^2+576ab-232a+549b^2-1746b+245;
L3(3/7)-Hstar=(19a+183b-43)(31a+93b-49)/[7224(2a+6b+1)].
```

N0 increases strictly in a since 262a+576b-232>0 on this rectangle, and decreases strictly in b since 576a+1098b-1746<0. Therefore `N0>=N0(99/100,13/100)=89/625>0`. Both factors in the L3-gap are strictly negative: `19a+183b-43<=-21/100` and `31a+93b-49<=-591/100`. Hence both L0(3/7) and L3(3/7) are >=Hstar.

All possible real common continuations c are covered: [0,3/7] by decreasing L0; [3/7,cstar] by endpoint-minimum L3, whose endpoint values are >=Hstar; [cstar,1] by new universal capacity/event bound e>=Bstar*c/4>=Hstar. The matching legal S23 policy proves equality for every real a,b in the rectangle.

## Actual exact checks, source and boundaries

`VERIFY_2D.py` was run in the local Python/SymPy/Fraction environment and passed 18 exact symbolic relations. It reconstructs the 16 strictly positive P/Q leaf masses and realizes full BU-bit terminal TV for six exact rational a,b parameter witnesses, with output stored as `VERIFY_2D_EVIDENCE.txt`. Exact arithmetic checks algebra and actual policies; the universal continuum theorem follows from the preceding inequalities. The published verifier has the same Git blob as the locally executed source.

GLOBAL_KNOWLEDGE_V1 frozen `main@4b3659222a1886c4643af5bdc6a867c745d65043`; initial Enterprise Math frozen `main@8168b9667b766ce95c681e67628de6af10fdec3b`. P000, ACTIVE Heartbeat World X6 plus separately typed time, joint-observer provenance rule and portable research protocol observed. Actual GitHub author awdawmip, native Site research_authority_granted=false, em_control_tasks/dispatch CONTROL_QUOTA; active Owner/CLAIM/native Result/independent Driver review remain unknown/not established. This is author-side research without Foundation admission.

**Next:** find the exact boundary of the capacity-saturated 2D phase beyond this rectangle; derive a variable splice point or a new measurable-event TV certificate and determine the first lawful strict counterexample, while retaining the full a<1 low-rho infeasible wedge and native P000 observer-transfer obligations.
