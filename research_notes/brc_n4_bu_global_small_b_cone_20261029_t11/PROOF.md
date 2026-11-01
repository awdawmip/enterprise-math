# BRC N=4 BU: global small-b exact root-phase cone

Date 2026-10-29 (Asia/Shanghai). **AUTHOR_ANALYTIC_PROOF / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.** Scope: external strictly positive 16-leaf dual-probability BRC stopping model, not a native P000/X6 or physical-time result.

## Frozen input and claim

Reuse the complete terminal observer O=(T,Decision,Z_BU), behavioral instantaneous S2/S23 policies, and their exactly equivalent four-observation-atom minimax representation from Enterprise Math commit `1a4898a57e952245eeacb38be7adf109faa49f49`, path `research_notes/brc_n4_bu_full_causal_reduction_audit_20261029_r1t11/PROOF.md`. Its theorem status remains author-side pending independent review. Define feasible real A,B,c,U,V by 0<=A,B,c<=1, 0<=U<=A, 0<=V<=B and

```
s=(A-a+B-b)/2; t=(A-a+3*(B-b))/4; H=B*c/4
rQ=a/6-A*c/6-U/3-V/4
rP=a/6-A*c/6-U/12-V/2
DeltaQ=(s,H-s-rQ,rQ,-H)
DeltaP=(t,H-t-rP,rP,-H)
e=max(||DeltaQ||_1,||DeltaP||_1)/2.
```

**New continuous-real theorem.** For ALL real pairs in the explicit nonempty cone

```
0<a<1,    0<b<=60*a/737,    a+3*b/5<=1,
```

let c* be the unique root in (3/7,1) of f(c)=(a+3b)c²+(3a+8b)c+14b-4a=0. Then, for ALL lawful real randomized causal competitor policies,

```
d2(a,b)=d23(a,b)=b*c*/(4+c*).
```

The numerical slope 60/737 is a **sufficient proof-certificate threshold**, NOT a claimed true phase boundary. Unlike the earlier narrow [97/100,99/100] a-strip, this gives exact answers at every 0<a<1 for a positive interval of b values.

## Existence and attainable upper bound

f'(c)=2(a+3b)c+3a+8b>0 for c>=0; f(1)=25b>0 and f(3/7)=(-124a+881b)/49<0 because 60/737<124/881. Define h=b*c*/(4+c*) in (0,b/5) and set

```
A=a+3h,  B=4b/(4+c*),  c=c*,  U=B(1+c*),  V=B.
```

This is an actual S23 policy: A<=a+3b/5<=1; B<=b<=1; U<=2b<=120a/737<a<=A; V=B. Implement AV/BV continuation rates U/A and V/B=1; AU/BU share c; at time three stop with BU->Q and others->P using the already established current-likelihood separation. Substitution modulo f(c*)=0 yields exactly

```
DeltaQ=(h,0,0,-h),   DeltaP=(0,0,h,-h),
```

so both probability laws attain TV=h.

## Uniform dual lower bound without parameter sampling

For every lawful A,B,c,U,V, the signed observable-event TV certificates below are valid:

```
L0(c)=[4a-14b-3ac-(a+3b)c²]/[2(23-2c)] <= e, 0<=c<=3/7;
L3(c)=c[a-(a+3b)c]/[2(7-2c)] <=e, 0<=c<=1;
K(c)=bc/(4+c) <=e, 0<=c<=1.
```

Their complete nonnegative-mixture witness is as follows. Signed differences of actual observable events are Q1=s, Q2=H-s-rQ, Q3=H-rQ, Q7=H, P4=rP, P5=t+rP, P6=H-t, Qs=H-s; each is bounded by the applicable law's TV and therefore by e. L0 is the convex combination of (Q2,Qs,P4,P5) with coefficient numerators (c+4,3-7c,2(1+4c-c²),2(c²-2c+7)) over (23-2c), **plus** 7(c+4)(V-B)/[4(23-2c)]<=0. L3 is the convex combination of (Q3,Q7,P4,P5) with numerators (c,7(1-c),2c(2-c),2c²) over (7-2c), plus 7c(V-B)/[4(7-2c)]<=0. K equals (c Q1+(4-2c)Q7+2c P6)/(4+c). The coefficients of each mixture are nonnegative on its displayed domain and sum to one. In particular this argument retains the BU source bit rather than replacing it by unlabeled total mass.

L0 is strictly decreasing on [0,3/7] because its derivative numerator is a(2c²-46c-61)+b(6c²-138c-28)<0 (denominator 2(23-2c)²). L3 has no interior minimum on any interval contained in [0,1], since its derivative numerator D(c)=7a-14(a+3b)c+2(a+3b)c² strictly decreases there: D'(c)=4(a+3b)(c-7/2)<0.

Exact endpoint identities are

```
L0(3/7)=(4a-23b)/70; L3(3/7)=3(4a-9b)/602;
L0(3/7)-b/5=(4a-37b)/70>=0;
L3(3/7)-b/5=(60a-737b)/3010>=0;
L3(c)-K(c)=-c*f(c)/[2(7-2c)(4+c)].
```

The first inequality uses 60/737<4/37; the second b<=60a/737. Thus L3(c*)=K(c*)=h, and K increases in c. For any competitor, partition the entire continuum of c:

```
0<=c<=3/7:       e>=L0(c)>=L0(3/7)>=b/5>h;
3/7<=c<=c*:      e>=L3(c)>=min(L3(3/7),L3(c*))>=h;
c*<=c<=1:        e>=K(c)>=K(c*)=h.
```

The universal lower bound e>=h matches the legal competitor upper bound; the previously derived observer-preserving S2->S23 reduction gives d2=d23.

## Exact scale corollary and concrete rational witnesses

For any lambda in (0,1], (lambda a,lambda b) also lies in the cone, c*(lambda a,lambda b)=c*(a,b) by homogeneity of f, and d2(lambda a,lambda b)=lambda d2(a,b) (same for d23). This is an exact observable-stop-model scaling law, **not** a claim about all P000 dynamics.

The executed author verifier reconstructed all sixteen strictly positive leaf weights under both P,Q laws and checked the exact observation distributions; 20 symbolic checks and five rational witness cases passed. In particular (a,b,c*,TV_Q,TV_P) equals (1/10,2/465,4/5,1/1395,1/1395), (1/2,2/93,4/5,1/279,1/279), (9/10,6/155,4/5,1/155,1/155). See VERIFY_EVIDENCE.txt and local full execution bundle. These finite checks verify algebra/implementation; the continuous-real claim is proved by the explicit analytic inequalities, not extrapolation.

Provenance: GLOBAL_KNOWLEDGE_V1 main@e2ebb4e3129e575fe74ddb16f6b78f8dc47c4ab4; Enterprise Math input main@3dfed4dee9f046d23b62c8d9d1c8fd6834378996. GitHub actor awdawmip, local label EM-R1-T11-20261029-1802 (not service-issued identity). Native em_status: research_authority_granted=false; em_control_tasks read returned CONTROL_QUOTA, so active owner not verified and no CLAIM/Result/Driver review is asserted. No native X6 Cell/slice/rotation/time observer-preservation bridge is established.

**Next:** sharpen 60/737 by optimizing the c split; distinguish loss of this dual certificate from true minimax switching or the capacity wall a+3h=1. See NEXT_TASK.md.