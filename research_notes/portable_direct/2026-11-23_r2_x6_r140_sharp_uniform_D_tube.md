# X6 R140 — sharp uniform centered D-tube over every positive B

Date: 2026-11-23 (Asia/Shanghai). Mathematical status: AUTHOR ANALYTIC / EXACT RATIONAL CERTIFICATE PASS; NOT INDEPENDENTLY REVIEWED.

## Scientific scope and immutable predecessors

Preserve the conditional four-positive-weight, six-pair BRC observer of the declared centered-three-axis slice of native X6, P000 V5 and the ACTIVE Heartbeat World. Integer Port 10, all six relation gaps and strict 3/2 nearness are unchanged. Frozen inputs are:
- R121 optimizer: awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md
- R122 exclusion: awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json
- R138: awdawmip/enterprise-math@e8e20fdfce40d5415e2f02b51983c7c5928d30ce:research_notes/portable_direct/2026-11-23_r2_x6_r138_D500_all_positive_B_rigidity.md
- R139: awdawmip/enterprise-math@2b1956e825436f1c0b722b2b1c511d0d1a047347:research_notes/portable_direct/2026-11-23_r2_x6_r139_uniform_two_parameter_D_tube.md

For any nonzero integer a=(x,y,z), put q(a)=max(sum(max(a_i,0)),sum(max(-a_i,0))), with a and -a identified but integer multiples distinct. Define four heights h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), the six gaps g_ij=|h_i-h_j| (i<j), and capacities

s(B,D)=(136+B,312,136+D,B+176,B+D,176+D).

For w=(136,B,176,D) define F_D(a)=max_j(g_j(a)/s_j(B,D)), eta_D(B)=min_{0<q(a)<=10}F_D(a), and strict-near N_D(B)={a modulo ±:0<q(a)<=10, 2F_D(a)<3eta_D(B)}. There are 1,935 unoriented Port-10 directions.

## New theorem: exact sharp symmetric uniform radius

Let C={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)} modulo ±.

**For all real B>0 and 472<D<528, N_D(B)=C exactly.** Moreover the supremal radius R such that N_D(B)=C for every B>0 and every positive D with |D-500|<R is **R=28**.

This improves R139's certified open symmetric radius 500/41 by the exact factor 287/125.

## Proof part I: seven B chambers with exact affine certificates

Put eta_0=eta_500(B), F_0=F_500. R138's seven rational chambers for B>=0 have endpoints 0,316/7,320/7,46,556/7,796/7,136,+infinity; write eta_0=K/(L0+L1 B), where consecutive (K,L0,L1) triples are (6,500,1), (7,636,0), (2,136,1), (6,500,1), (7,676,0), (3,176,1), (1,104,0).

The newly executed integer/rational certificate establishes, for every real B>0:

(1) For each of the four C directions, both F_500(a)<=125 eta_0/88 and F_472(a)<=125 eta_0/88. For each of 7 chambers, 4 directions, 6 pairs and each d in {500,472}, the checked affine inequality is
125 K s_j(B,d)-88 g_j(a)(L0+L1 B)>=0.
There are exactly 168 checks per d.

(2) For each of the 1,931 outsider directions, in each of seven B chambers one fixed pair j, not depending on B within that chamber, satisfies
5 g_j(a)(L0+L1 B)-8 K s_j(B,500)>=0.
Thus F_0(a)>=8 eta_0/5. Exactly 13,517 outsider certificates pass.

(3) As an independent baseline replay, 13,545 direction/chamber comparisons certify every F_0(a)>=eta_0, and 42 witness pair checks certify a genuine direction attaining eta_0 in each chamber. Every comparison is affine in B. Testing both rational endpoints of a bounded cell and the finite endpoint plus recession slope of the final unbounded ray proves all B>=0. B=0 is used only as a closure; the theorem assumes B>0.

## Proof part II: exact interval extension

Only three denominators involve D. Their positivity gives, for 472<=D<=500,

F_0(a)<=F_D(a)<=500F_0(a)/D,
eta_0<=eta_D<=500eta_0/D.

For 500<=D<=528 the bounds are

500F_0(a)/D<=F_D(a)<=F_0(a),
500eta_0/D<=eta_D<=eta_0.

For 472<D<=500, each insider has F_D(a)/eta_D <= F_472(a)/eta_0 <=125/88<3/2, while each outsider has F_D(a)/eta_D >=(D/500)(8/5)>(472/500)(8/5)=944/625>3/2.

For 500<=D<528, insiders satisfy F_D(a)/eta_D <=(D/500)(125/88)<(528/500)(125/88)=3/2. Outsiders satisfy F_D(a)/eta_D >=(500/D)(8/5)>(500/528)(8/5)=50/33>3/2.

Therefore the complete strict-near set is C everywhere in the stated continuous real-parameter tube.

## Sharpness: explicit boundary loss

Let r>28 and choose any 0<B<min(20,(r-28)/2). Put D=528+2B. Then |D-500|=28+2B<r. Inspecting the six ratios of a0=(1,0,0), we obtain F_D(a0)=2/(B+176), hence eta_D(B)<=2/(B+176). For a1=(9,-5,1), the pair with gap 3 and denominator B+176 gives F_D(a1)>=3/(B+176)>=3eta_D(B)/2. So the previously present direction a1 has exited the strict near set inside every proposed radius r>28. Therefore no larger uniform open symmetric radius exists. This proof of sharpness requires only the displayed two exact direction scores, not an assumed global optimizer beyond D=500.

## Reproducibility and remaining work

Python 3 standard library exact replay script: research_notes/portable_direct/x6_r140_sharp_uniform_D_tube_verify.py (this publication's companion file). Its actual execution returned:

    R140 SHARP UNIFORM OPEN D-TUBE EXACT CERTIFICATE PASS
    population 1935 target [(1, 0, 0), (5, -4, 1), (5, -1, 0), (9, -5, 1)]
    certificates {'optimizer_lower': 13545, 'optimizer_upper': 42, 'outsider_8_5': 13517, 'inside_125_88_D500': 168, 'inside_125_88_D472': 168}
    full_fraction_replays 56 sharp_open_radius 28 uniform_D_interval (472, 528)

It also ran three exact sharpness examples (B=1/1000,1,20) at D=528+2B. The finite replays are crosschecks; the affine and analytic inequalities certify all real B,D in scope. Author proof and exact computation passed; independent review and shared Result/Review adoption are pending. The conclusion remains restricted to the declared BRC observer, not an inference about native six-axis time dynamics.

Next: find the sharp **lower one-sided** uniform radius for D<500, and classify the first outside entry and its adjacent direction sets. A numerical reconnaissance suggests a candidate lower radius 52 near B=20,D=448; that is a conjectural next research target, not a claimed theorem. Source evidence and original frozen pins above remain unchanged.
