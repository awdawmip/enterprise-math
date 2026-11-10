# C62: optimal consumption-schedule scales and shortest hidden synchronization

Progress-Event-ID: prime-c62-schedule-extrema-20261110-a1
Date: 2026-11-10 Asia/Taipei
Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING
Researcher-ID: EM-DIRECT-DE46F9 / TASK_RESEARCH
Research-Activity-ID: RA-144CDF0D55DEB009440F261D
Global-read: c08518a572311588d7e409897a32abb60c7478df
EM-control-read: 88161d0c9685145337adde5015262281dec564c6
Pre-publication-main: 95cfc6181ddfbd5c3814f53f7f646bb4df2d5b0a

## 1. Scope and fixed model

Continue C61@d3e4ee811a53f85f70dd7f0eace26a0a9ee00814, research_notes/divisor_extrema/20261107_c61_consumed_hidden_order_and_feedback.md, blob25b54961982a886c174cbfc203a088e72acacbfa, and its actually mounted complete reproduction archive. Parent question: whole-path conditions, prime-factor order, and persistence of historical distinctions.

Three states0/1/2 have rates for(2,3,5,7)=(1,1,z_s,1), z=(1/4,1,4). Next-symbol probability is rate times remaining multiplicity, normalized. Symbol2 increments state capped at2. The first two3s reset for preparation; later3s retain with e(xi)=1/(4+xi^2), otherwise reset0. Symbols5/7 preserve state. xi=2X23-n2*n3 is evaluated before the update. Histories h0=3223,h1=2332 reach36 with the same xi0 and prepare pure states0/1. Keep signed scores, positive masses, complete word provenance and rho_1 separately; words/states remain internal records over the retained Heartbeat X6 identity.

At complete counts(a,b,c,d), A=2(X23-X25+X27+X35-X37)-(ab-ac+ad+bc-bd), B=2X57-cd. Final selection uses the same positive W(A,B) at equal scores. Main extrema concern reference conditional state TV, with separate common-future readout bounds.

## 2. Complete scheduling class at a fixed integer

For k>=2, N_k=36*6^k*5^(k+1)*7. Class S_k contains every interleaving of k-1 copies of5 into the fixed visible subsequence(23)^k, in all2k+1 gaps, followed by a reserved complete tail5^2*7. Its size is binom(3k-1,k-1). Delta(sigma) is TV between the two histories' conditional state distributions after the common prefix sigma.

If5s occur only at boundaries between23 blocks, weak compositions(g0,...,gk) with sum k-1 describe all binom(2k-1,k) arrangements. Their three final tail scores are(k,k+1),(k,k-1),(k,k-3). Allowing m copies inside2...3 changes A to k-2m; terminal-score strata are retained separately.

Every3 in these prefixes sees xi=-2, so retention remains1/8. After each23 the state is pi(u)=(7/8,u/8,(1-u)/8). After the first block the two pure histories give u1/0, even if some5s precede or occur inside that first block.

## 3. General pre/mid-block map

Before a block, r visible pairs, c copies of5, and one7 remain. Observe g copies of5, then2, then b copies of5, then3. Let L_i be the first hidden segment's likelihood in state i; D_i=2r+(c-g)z_i+1. Let J_i be the middle hidden segment's likelihood, with2r-1 visible inputs still pending, and E_i=2r+(c-g-b)z_i. After dropping common r^2 numerators:
q0=L0*J1/(D0*E1), q1=L1*J2/(D1*E2), q2=L2*J2/(D2*E2).
The exact map is F(u)=7q0/[7q0+q2+(q1-q2)u].
Thus synchronization is exactly q1=q2. The ratio rho=q1/q2=(L1/L2)*(D2/D1) is independent of the middle hidden segment. All branch weights are positive.

## 4. Universal nonzero lower bound and fastest possible leading scale

Here V=2r+1 is odd. For g preceding5s,
rho=product_(j=0)^g(V+4c-4j)/[4^g product_(j=0)^g(V+c-j)].
For g>=1 the numerator is odd and denominator divisible by4, so rho!=1. For g0, rho=(V+4c)/(V+c)>1. Every block is therefore injective; final hidden-only conditioning is a positive diagonal reweighting. Delta(sigma)>0 for every finite k and sigma in S_k.

Positive likelihood ratios and ordered rates give
1/64<=q1/q0,q2/q0<=16^(g+b).
The integer expression gives |rho-1|>=1/[4^g(3k)^(g+1)] for g>=1; the same bound holds for g0. Consequently, for every u in[0,1],
|F'(u)|>=(7/4096)*1024^(-(g+b))*(3k)^(-(g+1)).
Across the k-1 interior blocks, both sum(g+b) and sum g are at most k-1. A final segment of j fives has positive likelihood ratio at most16^j. Positive reweighting and its inverse have TV Lipschitz constant at most maxW/minW: differentiate an event probability along the line between the two measures and bound the oscillation of W(1_E-c).

Hence for all sigma in S_k:
Delta(sigma)>=(1/8)*(7/2^22)^(k-1)/(3k)^(2(k-1)).
In particular log min Delta >= -2k log k-O(k). This covers every insertion slot, including between2 and3.

## 5. A family attaining the fastest leading scale

A_k=5(235)^(k-2)2323 has boundary gaps(1,...,1,0,0). Compared with C61's G_k=(235)^(k-1)23, scheduled5s are advanced by one visible block, preserving the complete target and the three terminal columns.

An interior block has r>=2,c=r+1,d1 and consumes one5. Its coefficients F_r(u)=1/(1+a_r+b_r u) are
 a_r=(9r+4)(9r+5)/[14(6r+1)(6r+5)],
 b_r=-3(9r+4)(9r+5)/[56(3r+1)(3r+2)(6r+1)(6r+5)].
The likelihood ratio is
rho_r=1-3/[4(3r+1)(3r+2)].
The arithmetic source is (2c-1)^2-4c(c-1)=1: exact cancellation is impossible but the normalized defect is order r^-2.

For every r>=2,u in[0,1],
1/(200r^2)<=F'_r(u)<=1/(100r^2).
After clearing positive denominators and substituting r=t+2, both bound differences have strictly positive polynomial coefficients, retained in symbolic_checks.json.
The last empty23 block is275/(280+6u), whose absolute derivative is between825/40898 and33/1568. Thus
[825/(8*40898)]200^(-(k-2))/((k-1)!)^2 <= Delta(A_k)
 <=[33/(8*1568)]100^(-(k-2))/((k-1)!)^2.
Uniformly in u, r^2 F'_r(u)->42/4225; the exact difference product gives
lim [Delta(A_k)*((k-1)!)^2]^(1/k)=42/4225.

Combining the construction and universal lower bound proves
log min_(sigma in S_k) Delta(sigma)=-2k log k+O(k).
This is an optimal leading scale, distinct from claiming an exact finite minimizer for every k.

The last block confines u to[25/26,55/56]. The logit derivative there is at most3136/55. Positive common future kernels and matched positive terminal weights do not increase projective distance; their output TV is therefore at most(6272/55)Delta(A_k).

## 6. Slowest possible scale over the same full class

The2x2 positive map has logit derivative
-(q1-q2)u(1-u)/[q2+(q1-q2)u].
Its maximum absolute value is tau(rho)=|sqrt(rho)-1|/(sqrt(rho)+1), attained at u=sqrt(q2)/(sqrt(q1)+sqrt(q2)). This is the elementary two-dimensional positive-matrix contraction formula.

The preceding hidden word gives4^-g<=rho<=4. Thus tau<=1/3 for g0, and tau<=(2^g-1)/(2^g+1) for g>=1. For integer g>=0,
tau<=3^(g-1)*5^(-g/2).
Check g0..3 directly; for g>=4 the right side exceeds1.
The first positive interior block puts the initial endpoint pair at projective distance at most max(g,1)log4. At most k-1 preceding5s are available in total. The remaining block contraction product and the final positive diagonal reweighting therefore give, for every schedule,
Delta<=min{1,[3(k-1)log4/4]*5^(-(k-1)/2)}.
Since log4<3/2, an exact rational squared bound is Delta^2<=(9(k-1)/8)^2/5^(k-1).

The delayed C61 witness L_k=(23)^k5^(k-1) has
Delta(L_k)>=45/[(k+2)(k+3)(k+4)(k+5)]*(21/16384)^(k-1).
This follows from the inherited C60 positive lower bound at c=k+1,d1 and the final likelihood ratio at most(k+2)(k+3)(k+4)(k+5)/360. Hence
max_(sigma in S_k)Delta(sigma)=exp[-Theta(k)].
The fastest and slowest asymptotic types are thus both determined for one fixed target family, model and state observer.

## 7. Shortest hidden synchronization block

For arbitrary hidden word v with a fives,b sevens, length n=a+b, inventories r>=1,c>=a,d>=b and c>=1, let V=2r+d and m_j=count of5 in the first j letters. Then
rho(v)=product_(j=0)^n[V+4c-j-3m_j]/[4^a product_(j=0)^n(V+c-j)].
Its equality to1 is necessary and sufficient for synchronization of all pi(u) through v followed by23.

Length0 has rho>1. A single7 also has rho>1. A single5 would require
V^2=4c(c-1)=(2c-1)^2-1,
so(2c-1-V)(2c-1+V)=1, whose only nonnegative possibility has V0,c1, incompatible with r>=1.

Length2 is achieved by75 at c7,V28:
rho=56*55*51/(4*35*34*33)=1.
Every r1..13,d=28-2r realizes it with positive remaining hidden inventory. For e1/8, all pi(u) map to(7/8,1925/18896,437/18896). Reversed57 has rho52/55 and state TV588525/538382056>0 for the two actual histories. The shortest length is therefore exactly2 in this block design; no claim of globally smallest integer carrier is made.
Eight specified complete words were also evaluated using independent explicit latent-branch sums. Their matched four-word ratio is1 for75 and a strict nonunit rational for57.

## 8. Fixed hidden multiset ordering and constructive near matching

Swapping adjacent75 to57 changes rho by(D-4)/(D-1)<1, where D is state2's total pending rate before the swap. Subsequent counts coincide. Therefore
rho(5^a7^b)<=rho(v)<=rho(7^b5^a).
The maximal endpoint projective spread H=max(rho,1/rho) is attained at one of these two extreme orders.

If these extremes bracket1, an adjacent-swap chain from7^b5^a to5^a7^b crosses1 within ab swaps. Choose the neighboring word with smaller H. If D_fin=2r+4(c-a)+(d-b), then
H^2<=1+3/(D_fin+1).
Any common future/terminal readout has TV at most tanh{log[1+3/(D_fin+1)]/8}. Exact rational comparisons certify the crossing; no assertion of an exact discrete intermediate value is required.

## 9. Executed finite results

Boundary-slot schedules k2..10: all125475 candidates compared exactly. A_k is the unique minimum state-TV schedule at each tested k. Independent per-schedule replay and shared-prefix enumeration agree through k9; neither prunes candidates.
All insertion positions k2..7: all46147 candidates compared with terminal-score strata retained. The minimum is again Delta(A_k). A second equal state-TV arrangement places the initial5 between the first2 and3, namely253(523)^(k-2)23; its different final A remains explicit.

Finite minima are not extrapolated as exact all-k optimizer identities; Sections4-6 prove their asymptotic extremal types.
The boundary-slot finite maximum is not generally the delayed word. For k3 it has gaps(0,2,0,0); k5:(0,2,2,0,0,0); k10:(0,2,2,0,3,0,2,0,0,0,0).

Exact rational TV values displayed as decimals:
k5: fast1.66660707132e-12, gradual1.05052061576e-8, delayed9.43818025868e-8.
k10: fast3.49593138308e-31, gradual5.68624445963e-19, delayed4.31574553509e-16.
k20: fast1.45689838023e-74, gradual4.35997589751e-42, delayed2.63165363042e-33.
k50: fast1.94328117330e-226, gradual1.46272748961e-121, delayed1.48672470864e-85.
k100: fast3.06406887179e-513, gradual2.54317241866e-270, delayed6.18621889927e-173.

Additional checks:756 integer-product/positive-likelihood matches;1137 adjacent-swap identities;72 ordering extrema and72 projective extrema;4368 construction domains with402 certified brackets;13 shortest-block inventory realizations and13 controls;100 fast coefficients/defects/derivative bounds;174 small schedules against inherited three-state channels and522 terminal-score matches;96 pre/mid-block identities,192 channel rows and288 universal derivative bounds;30 terminal-weight cancellations;6 arbitrary future-readout checks. Initial1..5 retain the original rule. Counts overlap, not independent samples.

Unchanged BRC kernel8138 bytes/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1 was matched to current Source metadata and executed36 positive serial/recoalescence operations on terminal-equivalent fibers. Signed arithmetic differences are observer labels, not negative branch mass. No Monte Carlo.

Two expensive k10 replay attempts hit the45-second tool limit without completion. Reusing identical prefix computations while visiting every leaf completed all primary extrema; a SymPy structural-equality assertion was repaired to exact difference reduction without changing the mathematical identity. Rational outputs retain arbitrarily small positive masses; float underflow is null with separate rational and Decimal scientific fields.

## 10. Provenance, preservation and next question

Actually read Turner et al. author documentation, Introduction to PlackettLuce section1, for generic sequential choice. Retrieved the publisher abstract/search result for Birkhoff's contraction coefficient; direct full-page open returned403, so no full-paper inspection is claimed. The two-dimensional contraction calculation used here is proved directly. General probability methods retain existing attribution; no comprehensive novelty or independent-review claim.

Full Chinese RESEARCH_NOTE.md, schedule_extrema.py, all_slots.py, run_checks.py, symbolic_checks.py, exact enumeration records, logs and inherited modules are preserved in prime_quantum_schedule_extrema_c62.zip. This Source note contains the recoverable theorem scope, load-bearing arguments and verification record.

Native session_start succeeded this turn with canonical readback at327535c0002503ab11c68e3cf338d627aa502c56. ActivityRA-144CDF0D55DEB009440F261D and identityEM-DIRECT-DE46F9 are current; formal Task/CLAIM and mathematical acceptance remain separate. Scientific checkpoint publication is recorded separately.

Next: characterize exact finite-k extremizing schedules and the long-scale pattern of maximal schedules; separately extend the integer matching classification when7 is also consumable. The complete S_k fastest/slowest leading scales and the two-step shortest block are the completed author-derived results of this turn.
