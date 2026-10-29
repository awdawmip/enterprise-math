# BRC N=4 BU source-bit: expanded two-dimensional exact capacity-switch region

2026-10-29 | AUTHOR_ANALYTIC_PROOF / EXACT_SYMBOLIC_AND_16_LEAF_CHECKED / UNREVIEWED / NOT_ADMITTED

## Fixed model and theorem

Freeze the positive 16-leaf dual-probability stopping tree and observer O=(T,Decision,Z_BU) from the inherited author proof (enterprise-math@01959291d98e6d666cf6b769889bcca623caf12c, research_notes/brc_n4_bu_expanded_rectangle_zero_wedge_20261029_r1t11/PROOF.md). Four second-level Q masses AU,AV,BU,BV are 1/6,1/3,1/4,1/4, with corresponding P/Q ratios 1,1/4,1,2. AU child ratios are 9/10 and 11/10; BU child ratios 1/5 and 9/5; at the last level both children split equally. Every leaf has strictly positive P,Q mass; each law sums to one. The full lawful-causal S2/S23 reduction is inherited author-side evidence awaiting independent replication.

Competitors: 0<=A,B,c<=1 and 0<=U<=A, 0<=V<=B, with common instantaneous AU/BU continuation c. Define s=(A-a+B-b)/2, t=(A-a+3(B-b))/4, H=Bc/4, rQ=a/6-Ac/6-U/3-V/4 and rP=a/6-Ac/6-U/12-V/2. The four observable signed-mass vectors are DeltaQ=(s,H-s-rQ,rQ,-H), DeltaP=(t,H-t-rP,rP,-H), so error e=max(||DeltaQ||_1,||DeltaP||_1)/2. Under the inherited causal reduction this is the exact all-strategy minimax problem.

**New theorem.** For every real a in [97/100,99/100] and b in [1/100,1/8], set
f(c)=(a+3b)c²+(3a+8b)c+14b-4a,
G(a,b)=5a²+8ab-21b²-2b-5,
beta(a)=(4a-1-sqrt(121a²-8a-104))/21,
and let c* be the unique f-zero in (3/7,1). Then the exact common S2 and S23 minimax is

- b*c*/(4+c*) when b<=beta(a);
- (a+3b-1)*(7-a-21b)/[12*(4a+12b+2)] when b>=beta(a).

The two branches and their legal minimizing policies coincide at b=beta(a), where the root policy reaches A=1. This rectangle strictly contains the previously proved [979/1000,981/1000] by [3/100,1/20] rectangle and has 115/2 times its area.

## Observable-event total-variation duals

For every lawful real strategy and common c,

L0=[4a-14b-3ac-(a+3b)c²]/[2(23-2c)] <=e for 0<=c<=3/7;
L3=c[a-(a+3b)c]/[2(7-2c)] <=e for 0<=c<=1;
R=c(a+3b-1)/12 <=e and K=bc/(4+c) <=e for 0<=c<=1.

These are convex combinations of *observable signed events*: for L0 use Q2=H-s-rQ, H-s, P4=rP and P5=t+rP with weights (c+4,3-7c,2(1+4c-c²),2(c²-2c+7))/(23-2c); the exact L0-minus-event-sum is +7(c+4)(V-B)/[4(23-2c)] <=0. For L3 use Q3=H-rQ,Q7=H,P4,P5 with weights (c,7(1-c),2c(2-c),2c²)/(7-2c); the L3-minus-event-sum is +7c(V-B)/[4(7-2c)] <=0. R uses (1-c/3)Q7+(c/3)P6=c(a+3b-A)/12>=R where P6=H-t. K uses [c Q1+(4-2c)Q7+2c P6]/(4+c)=bc/(4+c), with Q1=s. All weights are nonnegative and each list sums exactly to 1.

L0 strictly decreases on [0,3/7]: its derivative numerator is a(2c²-46c-61)+b(6c²-138c-28)<0. L3 has no interior minimum on any subinterval of [0,1], since its derivative sign D=7a-14(a+3b)c+2(a+3b)c² has derivative D'=(a+3b)(4c-14)<0; any stationary point is a maximum. Identities L3-K=-c*f/[2(7-2c)(4+c)] and L3(ccap)=R(ccap)=ecap hold, with ccap=(7-a-21b)/(4a+12b+2), ecap=ccap*(a+3b-1)/12.

## Parameter geometry and exact root branch

The derivative f_c>0 for c>=0; f(1)=25b>0, and f(3/7)=-(124a-881b)/49<0 because 124a-881b>=2031/200. Hence unique c* in (3/7,1). The cap crossover ccap is decreasing in a and b, with derivatives (72b-30)/(4a+12b+2)^2<0 and -(72a+126)/(4a+12b+2)^2<0; consequently 677/1492<=ccap<=97/100, entirely inside (3/7,1). Also a+3b-1>=0.

G increases in a (G_a=10a+8b>0) and in b (G_b=8a-42b-2>=51/100>0). G(99/100,1/100)=-53/1250<0 and G(97/100,7/100)=3/625>0. Thus each a has exactly one zero beta(a) in (1/100,7/100), with sign G<0 below and G>0 above. The root parametrization
b(c)=a(1-c)(4+c)/(3c²+8c+14),
H(c)=ac(1-c)/(3c²+8c+14)
has db/dc=a(c²-52c-74)/D²<0 and dH/dc=-a(11c²+28c-14)/D²<0 on c>=3/7. Therefore root-policy A=a+3H strictly increases with b. At b=1/100, A<=99/100+3/500<1; at b=1/8, A>=97/100+9/248>1. Eliminating c between f(c)=0 and A=1 yields G=0. Hence root policy is legal precisely for b<=beta(a).

On that root branch, b<7/100 and e_root=K(c*)<=b/5<=7/500. Sharp rational dual endpoints are L0(3/7)>=227/7000>7/500 and L3(3/7)>=39/2408>7/500, since both expressions increase in a and decrease in b. Partition arbitrary competitor c as [0,3/7], [3/7,c*], [c*,1]. Respectively use decreasing L0, endpoint-minimum L3, increasing K to prove e>=e_root for every lawful real competitor.

Matching legal root policy:
A=a+3H, B=4b/(4+c*), U=B(1+c*), V=B, H=bc*/(4+c*).
Then B<=b<=1/8, U<=2b<=1/4<a<=A<=1. Using f(c*)=0 gives DeltaQ=(H,0,0,-H), DeltaP=(0,0,H,-H), so both TVs equal e_root.

## Capacity branch, all-c lower bound and witness

Let N0=131a²+576ab-232a+549b²-1746b+245. Exact endpoint identities:

L0(3/7)-ecap=N0/[840(2a+6b+1)];
L3(3/7)-ecap=(19a+183b-43)(31a+93b-49)/[7224(2a+6b+1)].

N0_a=262a+576b-232>0 and N0_b=576a+1098b-1746<0 in the rectangle, yielding N0>=N0(97/100,1/8)=135441/40000>0. Moreover 19a+183b-43<=-263/200<0 and 31a+93b-49<=-1337/200<0. Both dual endpoints therefore strictly exceed ecap.

Since a+3b-1>=0, R increases in c. Split every competitor's c into [0,3/7] (L0), [3/7,ccap] (L3 endpoint-minimum), [ccap,1] (R): all three give e>=ecap without any grid/exhaustiveness assumption.

For b>=beta(a), choose A=1, B=(a+3b-1)/3, c=ccap, U=B(1+c), V=B. Here 0<=B<=b<=1/8 and U<=2b<=1/4<1, so this is a causal randomized policy. Its exact signed masses are DeltaQ=((1-a)/3,ecap-(1-a)/3,0,-ecap), DeltaP=(0,0,ecap,-ecap). Since ecap-(1-a)/3=G/[8(2a+6b+1)]>=0 in this branch, both TV values equal ecap. At G=0, f(ccap)=-3(5a+21b)G/[4(2a+6b+1)^2]=0 and the root/cap witnesses meet. Thus this is a genuine global minimax policy switch on the declared two-dimensional rectangle.

## Independent exact witnesses and verification scope

Root-side rational witness outside the old rectangle: a=97/100, c*=3/4, b=1843/34700, policy (A,B,c,U,V)=(8633/8675,388/8675,3/4,679/8675,388/8675), and both TVs=291/34700.

Cap-side rational witness: a=97/100, b=1/8, ccap=227/492, B=23/200, U=16537/98400, both TVs=5221/393600.

Local extended SymPy/Fraction VERIFY.py was executed on 2026-10-29 and returned PASS_EXACT_BU_N4_EXPANDED_2D_RECTANGLE. It reconstructs all 16 strictly positive leaves, checks total P=Q=1, four observable-event dual identities and root/cap polynomial identities, exact rectangle endpoints, and the full four-atom signed TV vectors of both rational policies. The finite verification checks algebra and implementation; the continuous quantifiers follow from the displayed proof. A published concise verifier may differ in coverage from the local extended file.

Boundaries: inherited causal-postprocessing equivalence is author-side and requires independent audit; no Lean formalization, Source-native CLAIM/Result or independent Driver review was obtained; no native P000 X6, 3D slice or physical time fidelity transfer. Next: locate the first b>1/8 dual/capacity failure, especially exact N0=0 or L3 endpoint equality, and produce either a new dual or exact lawful rational counterstrategy.