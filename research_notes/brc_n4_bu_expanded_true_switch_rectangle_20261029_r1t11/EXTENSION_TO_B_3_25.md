# BRC N4 BU 2D capacity-switch theorem: exact extension to b <= 3/25

2026-10-29. AUTHOR_ANALYTIC_PROOF / LOCAL_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED. This supplement strengthens the PROOF.md in this directory. Inputs are its strictly positive 16-leaf P/Q law, full BU-source observer (T,Decision,Z_BU), target F=(a,b,1,0), full lawful real causal S2/S23 strategy set, and its inherited four-atom causal reduction plus L0,L3,K,R observable TV certificates. The four-atom reduction and existing duals remain author-side dependencies, awaiting independent review.

## Exact strengthened theorem

On the full rectangle D'=[39/40,99/100] x [1/50,3/25], let G=5a²+8ab-21b²-2b-5, let c* be the unique root in (3/7,1) of f(c)=(a+3b)c²+(3a+8b)c+14b-4a, and set cC=(7-a-21b)/(4a+12b+2). Then, for all real (a,b) in D', over all lawful real causal randomized strategies,

  d2=d23=b*c*/(4+c*) when G<=0;
  d2=d23=(a+3b-1)*(7-a-21b)/[12*(4a+12b+2)] when G>=0.

The two formulae agree exactly at G=0; G=0 is an actual optimal causal-strategy capacity switch, not a mere witness coincidence. The domain has 75/2 (=37.5) times the area of the earlier [979/1000,981/1000] x [3/100,1/20] rectangle. Both G<0 and G>0 subsets have nonempty interior.

## Exact endpoint and capacity bounds

Let c0=3/7. Uniformly on D' (all rational endpoint evaluations exact):

- f(c0)=(-124a+881b)/49 <= -759/2450<0, f(1)=25b>0 and f'(c)>0. Thus c* is unique in (c0,1). On the G<=0 region, b<1/16 implies f(1/2)=(-9a+75b)/4<0, so c*>1/2 there if desired.
- G_b=8a-42b-2>=19/25>0, G(a,0)=5(a²-1)<0, G(a,3/25)>=5869/40000>0. Also G(a,1/16)>=43/1280>0, so G<=0 forces b<1/16 and E_K=b*c*/(4+c*)<1/80.
- cC>c0 exactly when 43-19a-183b>0; its minimum is 223/100. cC<1 exactly when 5a+33b-5>0; its minimum is 107/200.
- L0(c0)=(4a-23b)/70 >=57/3500>7/500;
  L3(c0)=3(4a-9b)/602 >=423/30100>7/500.
- Define E_C=cC*(a+3b-1)/12. Its a,b derivatives have signs opposite to D_a=a²+6ab+a+9b²+30b-11 and D_b=7a²+42ab-2a+63b²+21b-14. Both polynomials increase in a,b throughout D'; their upper-right maxima are -367/80 and -281/400, respectively. Hence E_C is increasing in both parameters and
  E_C<=E_C(99/100,3/25)=2443/177600<7/500.

These exact inequalities replace the former 1/80 global endpoint threshold with 7/500; E_K remains below 1/80 on its own G<=0 branch.

## Lower bound over all legal real strategies

The inherited positive-weight observable TV event certificates remain valid for every competitor and shared c:
 L0(c)=[4a-14b-3ac-(a+3b)c²]/[2(23-2c)], 0<=c<=c0;
 L3(c)=c[a-(a+3b)c]/[2(7-2c)], 0<=c<=1;
 K(c)=bc/(4+c), R(c)=c(a+3b-1)/12, 0<=c<=1.

All are lower bounds for competitor e=max(TV_P,TV_Q), with L3(c)-K(c)=-c*f(c)/[2(7-2c)(4+c)] and L3(cC)=R(cC)=E_C. L0 decreases on [0,c0]. The L3 derivative has strictly decreasing numerator 7a-14(a+3b)c+2(a+3b)c², so L3 has no subinterval interior minimum. K increases, and R increases since a+3b-1>=7/200>0.

For G<=0, partition c in [0,c0], [c0,c*], [c*,1]. The relevant L0, L3, K lower bounds each dominate E_K; L0(c0)>7/500>E_K, L3(c0)>7/500>E_K, L3(c*)=K(c*)=E_K, and K grows.

For G>=0, partition c in [0,c0], [c0,cC], [cC,1]. L0, L3, R each dominate E_C; the first two endpoint constants exceed 7/500>E_C and L3(cC)=R(cC)=E_C. These partitions cover all c in [0,1], establishing a global all-real-strategy bound without a parameter grid.

## Matching causal upper bounds and true switch

For G<=0 choose c=c*, H=bc/(4+c), A=a+3H, B=4b/(4+c), U=B(1+c),V=B. Then Q signed atom differences are (H,0,0,-H), P differences (0,0,H,-H); each TV is E_K. B<=b<=3/25, U<=2b<=6/25<39/40<=A. To show A<=1 exactly on G<=0, on the f=0 curve use b(c)=a(1-c)(4+c)/(3c²+8c+14), H(c)=ac(1-c)/(3c²+8c+14). Both decrease strictly with c>3/7; A strictly increases with b. At b=0, A=a<1. At b=3/25, c*>3/7 yields H>3b/31 and A>a+9b/31>=6261/6200>1. Hence there is a unique collision A=1. The algebraic collision identity is f(4(1-a)/(a+3b-1))=-6b G/(a+3b-1)², so uniqueness and G_b>0 give A<=1 iff G<=0.

For G>=0 choose A=1, B=(a+3b-1)/3, c=cC, U=B(1+c),V=B. Since a<=1, 0<B<=b<=3/25 and U<=2b<=6/25<1, all causal constraints hold. Q differences are ((1-a)/3,E_C-(1-a)/3,0,-E_C), P differences (0,0,E_C,-E_C). E_C-(1-a)/3=G/[8(2a+6b+1)]>=0, so both TVs equal E_C. When G=0, the identity f(cC)=-3(5a+21b)G/[4(2a+6b+1)²] gives cC=c*, A=1, and both optimal policies coincide.

## New high-b exact witness and verification scope

At a=39/40,b=3/25 (outside the previously proven b<=2/25 domain),
 G=5869/40000>0, cC=701/1468, and d2=d23=46967/3523200.
The feasible alternative e0=b(2a-7b)/[8(a+2b)] is larger at this point by 473/1268352.

Actual local VERIFY_EXTENSION.py (SymPy/Fraction) execution verifies 11 new exact corner identities, both four-atom P/Q TVs for this high-b legal policy, and 16 strictly positive P/Q source leaves with exact unit mass. Output is PASS_EXACT_BRC_N4_BU_EXTENSION_TO_B_3_25. Actual local extended VERIFY.py additionally checks the original 17 symbolic/event identities and all prior plus the new witness; output PASS_EXACT_BRC_N4_BU_EXPANDED_2D_RECTANGLE_TO_B_3_25. Continuous-domain optimality comes from the analytic argument and the inherited reduction; numerical sample checks do not substitute for it.

Status: AUTHOR_ANALYTIC_PROOF / LOCAL_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED. Native P000 X6 (six-dimensional cells, three-dimensional slice and separately typed time) and joint residual/time fidelity are separate unproved correspondence tasks.

Next: hold a=39/40, raise b above 3/25; locate the first failure of cC>3/7, the L0/L3 endpoint gap, lawful causal capacity, or dominance against e0; certify an exact new switch or exhibit one exact lawful counterexample.