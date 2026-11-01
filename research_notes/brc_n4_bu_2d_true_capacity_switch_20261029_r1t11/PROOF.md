# BRC N=4 BU source-bit — exact open two-parameter minimax and genuine capacity switch

2026-10-29. **AUTHOR_ANALYTIC_PROOF / LOCAL_EXACT_SYMBOLIC_AND_16_LEAF_CHECKED / UNREVIEWED / NOT_ADMITTED.** External strictly positive P/Q stopping-tree theorem, not P000 native X6, three-dimensional slice or independent physical-time result.

## Frozen model and inherited proof dependencies

Reuse the complete lawful causal S2=S23 four-atom observation-preserving reduction and event duals from enterprise-math@01959291d98e6d666cf6b769889bcca623caf12c, `research_notes/brc_n4_bu_expanded_rectangle_zero_wedge_20261029_r1t11/PROOF.md`, blob 8dfee379b45b88dfe26f07375e076fa071c19843. Reuse the K observable-event certificate from enterprise-math@bf8837884b110d34ee83766bdf99cb9d7db22409, `research_notes/brc_n4_bu_full_b_axis_low_branch_20261029_r11t11/PROOF.md`, blob 0679c2c52ff2f5a6f93284f112d31e5afc698b74. Both are author results awaiting independent review.

Target F=(a,b,1,0): continue AU, not BU, to stage 3. Four second-level Q branch masses AU,AV,BU,BV are (1/6,1/3,1/4,1/4), P/Q ratios (1,1/4,1,2). AU third-level ratios (9/10,11/10), BU (1/5,9/5), each split equally at level 4; AV/BV ratios remain unchanged. Thus 16 strictly positive leaves and both laws normalize to 1. Observer O=(T,Decision,Z_BU), with source bit of BU upon reaching stage 3. Real causal S2/S23 competitor variables satisfy 0<=A,B,c<=1, 0<=U<=A, 0<=V<=B; AU/BU share instantaneous c. Inherited lossless postprocessing proves this representation is the actual admissible-strategy optimum, not a relaxed occupancy problem.

Write
```
s=(A-a+B-b)/2; t=(A-a+3(B-b))/4; H=Bc/4;
rQ=a/6-Ac/6-U/3-V/4; rP=a/6-Ac/6-U/12-V/2;
DeltaQ=(s,H-s-rQ,rQ,-H); DeltaP=(t,H-t-rP,rP,-H);
e=max(sum_i|DeltaQ_i|/2, sum_i|DeltaP_i|/2).
```
Every signed mass of an observable event has absolute value at most e.

## Theorem: exact rectangle and genuine two-dimensional switch

For EVERY real (a,b) with 979/1000<=a<=981/1000 and 3/100<=b<=1/20, define f(a,b,c)=(a+3b)c²+(3a+8b)c+14b-4a and let c*(a,b) be its unique zero in (3/4,1). Define

```
G(a,b)=5a²+8ab-21b²-2b-5;
beta(a)=(4a-1-sqrt(121a²-8a-104))/21.
```

Then 3/100<beta(a)<1/20, and the **global infimum over all lawful real causal randomized S2 and S23 strategies** is

```
d2(a,b)=d23(a,b)=
   b c*(a,b)/(4+c*(a,b)),                         3/100<=b<=beta(a);
   (a+3b-1)(7-a-21b)/(12(4a+12b+2)),           beta(a)<=b<=1/20.
```
Both expressions agree at beta(a), an actual optimum-policy capacity-collision/switch curve across a nonempty two-dimensional open domain, not merely an intersection of feasible upper bounds.

## All-c event dual lower bounds

For all lawful real competitors with common c, existing certified measurable event combinations give
```
L0(c)=[4a-14b-3ac-(a+3b)c²]/[2(23-2c)] <= e, 0<=c<=3/7;
L3(c)=c[a-(a+3b)c]/[2(7-2c)] <= e,    0<=c<=1;
R(c)=c(a+3b-1)/12 <= e,                0<=c<=1.
```
L0 uses convex event weights (c+4,3-7c,2(1+4c-c²),2(c²-2c+7))/(23-2c) on events Q2,H-s,P4,P5; L3 uses (c,7(1-c),2c(2-c),2c²)/(7-2c) on events (H-rQ),H,P4,P5. Their exact weighted-sum remainders are +7(c+4)(V-B)/[4(23-2c)] and +7c(V-B)/[4(7-2c)], respectively, so V<=B gives lower bounds. For R, the convex observable combination (1-c/3)H+(c/3)(H-t)=c(a+3b-A)/12 >= R from A<=1.

A further convex combination of signed observable events Q1=s, Q7=H, P6=H-t with weights [c,4-2c,2c]/(4+c) has value
```
K(c)=[c s+(4-2c)H+2c(H-t)]/(4+c)=bc/(4+c)<=e, 0<=c<=1.
L3(c)-K(c)=-c f(a,b,c)/[2(7-2c)(4+c)].
```
Weights are nonnegative and sum to one for 0<=c<=1. f(3/4)=-(19a-347b)/16<0, f(1)=25b>0, f_c=2(a+3b)c+3a+8b>0, hence the unique c* lies in (3/4,1) and L3(c*)=K(c*)=:e_root.

On 0<=c<=3/7, L0 strictly decreases: its derivative has sign a(2c²-46c-61)+b(6c²-138c-28)<0. On all c in [0,1], L3 derivative has sign D(c)=7a-14(a+3b)c+2(a+3b)c², and D'(c)=(a+3b)(4c-14)<0, so L3 has no interior minimum on any subinterval. K strictly increases. Exact endpoint evaluations:
```
L0(3/7)=(124a-713b)/2170 > 131/12000;
L3(3/7)=3(4a-9b)/602 > 131/12000.
```
Both inequalities hold uniformly over the stated rectangle (minimize the right expressions at a=979/1000,b=1/20). Since e_root<=b/5<=1/100, partition any competing c into [0,3/7], [3/7,c*], [c*,1]; L0, L3 endpoint-minimum principle, K respectively yield e>=e_root for every real competitor.

Now set ccap=(7-a-21b)/(4a+12b+2), ecap=ccap(a+3b-1)/12. Uniformly 3/7<ccap<1 and a+3b-1>0. Exact identity L3(ccap)=R(ccap)=ecap holds, and R increases. Moreover ecap <= (981/1000+3/20-1)/12=131/12000. Split any c into [0,3/7], [3/7,ccap], [ccap,1] and use L0, L3 endpoint-minimum principle, R to obtain the independent uniform lower bound e>=ecap for every real competitor. These lower bounds are established without a grid or inaccessible hidden history.

## Matching strategies and exact capacity-collision geometry

Root policy: at c=c*, choose H=bc/(4+c), A=a+3H, B=4b/(4+c), U=B(1+c), V=B. Algebra using f=0 gives s=H,t=0,rQ=0,rP=H, so DeltaQ=(H,0,0,-H), DeltaP=(0,0,H,-H): both TV values equal H=e_root. Here 0<B<=b, U<=2b<=1/10<a<=A, V=B, and c in (3/4,1); remaining capacity is exactly A<=1.

For fixed a, parameterize the f=0 root by b(c)=a(1-c)(4+c)/(3c²+8c+14), H(c)=ac(1-c)/(3c²+8c+14). On 3/4<c<1, derivatives db/dc=a(c²-52c-74)/D²<0, dH/dc=-a(11c²+28c-14)/D²<0 (D=3c²+8c+14); thus H strictly increases in b. At b=3/100: A<=a+3b/5<=999/1000<1. At b=1/20: c>3/4 implies A>a+9b/19>=979/1000+9/380>1. Unique capacity collision lies inside this rectangle.

At A=1, H=(1-a)/3 and c=4(1-a)/(a+3b-1); substitution into f gives -6b G/(a+3b-1)²=0. On this rectangle G_b=8a-42b-2>0, G(a,3/100)<0 and G(a,1/20)>0. Hence the unique collision is the explicit beta(a); the root witness is lawful exactly for b<=beta(a). An exact rational parameterization of this capacity component is
```
a=(3c²+8c+14)/(14+11c), b=(1-c)(4+c)/(14+11c), 3/4<c<1,
```
restricted to the rectangle. This gives the exact 2D capacity collision, not a numerical fit.

Capacity policy for b>=beta(a): A=1, B=(a+3b-1)/3, c=ccap, U=B(1+c), V=B. All causal constraints hold (0<B<=b<=1/20, U<=2b<=1/10, c in (3/7,1)). It yields
```
DeltaQ=((1-a)/3, ecap-(1-a)/3,0,-ecap);
DeltaP=(0,0,ecap,-ecap).
```
The exact identity ecap-(1-a)/3=G/[8(2a+6b+1)] is >=0 iff b>=beta(a) in the rectangle. Consequently both TVs are ecap and match the global lower bound. At G=0, f(a,b,ccap)=-3(5a+21b)G/[4(2a+6b+1)²]=0, hence c*=ccap and the two policies meet at A=1. This proves a **true global minimax branch switch** over an open interval in a.

## Evidence and scope

The locally run Python/SymPy extension reconstructed all 16 positive Q/P leaves with exact P,Q total mass one, checked the general observable-event dual identities, root/cap witness signed mass vectors, six rational parameter points (including rational-c exact root witnesses), and three beta values; output: PASS_EXACT_BU_N4_2D_CAPACITY_SWITCH_AUTHOR. The archived SHA256 manifest, complete expanded PROOF.md, actual local VERIFY.py and raw output are in the research evidence package. A GitHub release verifier is provided separately; identical source-byte execution is not claimed for that shorter program. Continuous-domain optimality is the analytical dual+causal-witness proof, not finite tests.

GLOBAL_KNOWLEDGE_V1 frozen input main@b1e7fde83e3a3fa41d56f7f7e772a486507e48d8; Enterprise Math frozen scientific input main@c7c8b0ea6797e9a549073d0babe7ec67e78cb893. GitHub login awdawmip. Service 0.6.11 reports research_authority_granted=false; owner query CONTROL_QUOTA; no Source CLAIM/Result/Driver acceptance. P000 remains the locked native X6 + three-dimensional slice + separate time model; no fidelity transfer was proved.

**Next task:** maximize the connected 2D semialgebraic domain where this K/L3-to-L3/R switch proof continues, classify first endpoint-dual and causal-capacity failures, and compare the alternative e0=b(2a-7b)/[8(a+2b)] branch. Independently review the inherited four-atom causal reduction before any admission.