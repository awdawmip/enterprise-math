# BRC N=4 BU source-bit observer: a two-dimensional exact high-b phase switch

Date: 2026-10-29 (Asia/Shanghai). Status: **AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Model, source, and theorem

Freeze the strictly positive 16-leaf P/Q stopping tree, BU-bit complete observer O=(T,Decision,Z_BU), shared instantaneous continuation, and observation-preserving all-causal reduction of [the source finite model](https://github.com/awdawmip/enterprise-math/blob/88492f07eacb063891464c536ec906e8298fcd71/research_notes/brc_n4_bu_expanded_2d_rectangle_20261029_r11/PROOF.md). This reduction remains an **inherited, author-side dependency** until independent review. The new theorem is mathematical within that precise finite model; it is not a P000-native X6 or physical-time theorem.

For real `97/100 <= a <= 99/100` and `307/2100 <= b <= 1`, target policy F=(a,b,1,0), define

```text
Q(a,b)=a^2+38ab-7a+105b^2-14b,
gamma(a)=[7-19a+sqrt(256a^2+469a+49)]/105,
c_p=(7-a-21b)/(4a+12b+2),  e_p=c_p(a+3b-1)/12,
c_0=(2a-7b)/(2a+4b),       e_0=b c_0/4.
```

**Conditional all-causal minimax theorem.** For every such real pair, both S2 and S23 have the same exact minimum (over all lawful real causal randomized competitors)

```text
d2(a,b)=d23(a,b)=
  e_p,   307/2100 <= b <= gamma(a);
  e_0,   gamma(a) <= b <= 2a/7;
  0,     2a/7 <= b <= 1.
```

The formulas agree at both boundaries. The curve gamma(a) has nonempty two-dimensional neighborhoods on either side of it; this is an actual **minimax policy switch**, not merely a comparison of two feasible policies. Combining the preceding already-published rectangle 1/100<=b<=307/2100 with this theorem gives an author-side exact piecewise phase chart for a in [97/100,99/100] and b in [1/100,1]. The unstudied b<1/100 part remains distinct.

## Four-atom representation, legitimate duals, and universal partitions

Every observation-preserving competitor uses `0<=A,B,c<=1`, `0<=U<=A`, `0<=V<=B`. Put

```text
s=(A-a+B-b)/2, t=(A-a+3(B-b))/4, H=B c/4,
rQ=a/6-A c/6-U/3-V/4, rP=a/6-A c/6-U/12-V/2,
DeltaQ=(s,H-s-rQ,rQ,-H),
DeltaP=(t,H-t-rP,rP,-H).
```

Its loss `e=max(||DeltaQ||_1,||DeltaP||_1)/2`. Reuse the **explicit nonnegative observable-event TV certificates** established in the frozen predecessor (including the correction terms proportional to V-B<=0):

```text
L0(c)=[4a-14b-3ac-(a+3b)c^2]/[2(23-2c)] <=e   for 0<=c<=3/7;
L3(c)=c[a-(a+3b)c]/[2(7-2c)]            <=e   for 0<=c<=1;
R(c)=c(a+3b-1)/12                       <=e   for 0<=c<=1.
```

L0 is decreasing on [0,3/7]; L3 has no interior minimum on [0,1] (its derivative numerator is strictly decreasing); R is increasing because a+3b-1>0 here. Thus every later interval split genuinely covers all real c, not a sampled grid. Exact new reusable identities are

```text
L0(c0)=L3(c0)=e0,
L3(cp)=R(cp)=ep,
cp-c0=(1-a)(5a+21b)/[2(a+2b)(2a+6b+1)]>0,
e0-ep=(a-1)Q(a,b)/[24(a+2b)(2a+6b+1)].
```

Q is strictly increasing in b in the stated rectangle; its a derivative is also positive in [97/100,99/100] by [3/20,4/25]. The exact endpoint inequalities

```text
Q(99/100,3/20)=-111/2500<0;
Q(97/100,4/25)=993/2000>0
```

prove `3/20 < gamma(a) < 4/25` everywhere. Moreover `307/2100>8(99/100)/61`, so `c0<=3/7` for every b>=307/2100 with b<=2a/7.

**Capacity phase, b<=gamma(a).** Here 0<c0<cp<1, e0>=ep, so partition every lawful c:

* c in [0,c0]: e>=L0(c)>=L0(c0)=e0>=ep.
* c in [c0,cp]: e>=L3(c)>=min(L3(c0),L3(cp))=ep.
* c in [cp,1]: e>=R(c)>=R(cp)=ep.

The lawful matching policy is `(A,B,c,U,V)=(1,(a+3b-1)/3,cp,B(1+cp),B)`. All bounds hold since `0<B<=b<=4/25`, `0<cp<1` and `U<=2b<1`. It yields

```text
DeltaQ=((1-a)/3, ep-(1-a)/3,0,-ep);
DeltaP=(0,0,ep,-ep).
```

The remaining required sign is `ep-(1-a)/3=G/[8(2a+6b+1)]` with `G=5a^2+8ab-21b^2-2b-5`. G increases in a and is concave in b; on the enclosing rectangle b in [307/2100,4/25], `G(97/100,307/2100)=1283/13125>0`, `G(97/100,4/25)=177/2000>0`. Therefore both TV losses equal ep. This proves capacity **global** optimality until gamma.

**Alternative phase, gamma(a)<=b<=2a/7.** The lawful matching policy is `(A,B,c,U,V)=(a,b,c0,b(1+c0),b)`. Since `0<=c0<=3/7`, `b<=2a/7` gives `U<=20a/49<a=A`. Its observed signed vectors are

```text
DeltaQ=(0,e0,0,-e0); DeltaP=(0,0,e0,-e0).
```

For the lower bound define `c1=3bc0/(a+3b-1)`. Here `c0<=c1<1` because `c1/c0=1+(1-a)/(a+3b-1)<=15/14` (for c0>0 and b>=gamma>3/20), hence c1<=45/98<1. We have `R(c1)=e0` and the exact identity

```text
L3(c1)-e0 =
 -b(a-1)(2a-7b)Q(a,b) /
 [8(a+2b)(a+3b-1)(7a^2+29ab-7a+63b^2-14b)] >=0.
```

Its denominator is positive: its final factor equals `(a+2b)(a+3b-1)(7-2c1)`. Since b>=gamma, Q>=0. Partition any c into [0,c0] using decreasing L0, [c0,c1] using the endpoint-minimum property of L3, and [c1,1] using increasing R. Every region yields e>=e0; the matching actual policy yields equality. At b=2a/7 the same policy has c0=e0=0.

**Zero phase, b>=2a/7.** The legal `(A,B,c,U,V)=(a,b,0,2a/7,2a/7)` has DeltaQ=DeltaP=0, since `U<=a` and `V<=b`, proving exact zero optimum.

## Exact discriminating witnesses

At (a,b)=(99/100,3/20), c_p=143/388 and d=1573/116400, establishing capacity optimality beyond the previous b<=307/2100 rectangle. At (99/100,151/1000), a legal alternative has c0=923/2584 and TV_P=TV_Q=139373/10336000; capacity extrapolation would give 1257677/93264000, which is **strictly worse by 433/481988352**. The true switch at this a is

```text
gamma(99/100)=(-1181+142*sqrt(379))/10500
             ~=0.15080428299222032.
```

Thus these two exact rational points straddle a proved real switch curve.

## Verification, scientific boundary, continuation

SymPy exact symbolic identities and six complete four-observation-atom rational witnesses were executed from the accompanying VERIFY.py with PASS output recorded in VERIFY_EVIDENCE.txt. The continuous theorem comes from the analytic event-dual partitions; the finite checks test the algebra and witness implementation. The predecessor's positive 16-leaf model and causal reduction are **not independently reconstructed by this verification program**. No native P000 X6/slice/time faithful transfer, Lean proof, formal CLAIM/Result, independent Driver review, or admitted theorem is asserted.

Next: independently audit the 16-leaf-to-four-atom full causal reduction and extend the two-dimensional b<1/100 root phase, or broaden the gamma(a) phase beyond the declared a strip; preserve the exact signed-event and observer assumptions.
