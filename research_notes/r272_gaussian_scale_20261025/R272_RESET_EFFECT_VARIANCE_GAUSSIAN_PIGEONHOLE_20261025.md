# R272 — Exact reset translation moments and a Gaussian-scale provenance-fiber lower bound

Date: 2026-10-25. Status: AUTHOR-SIDE PROOF + TWO EXACT IMPLEMENTATIONS; not Source Result, independent Driver review, R193/native-heartbeat validation, or Foundation acceptance.

## Immutable input context and mathematical scope

GLOBAL_KNOWLEDGE_V1 read: main@0091504c9bb7adee5c459ec721dda9b53b420272.
Enterprise Math canonical control Source read: main@dd8d3a05d2fde3d318d16591eff949fc2dd58ee9.
P000 startup ACTIVE_LOCKED; original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc verified. Its six-native-axis world is an axiom, not a theorem tested here.

Prior author-side results consumed: R270, commit ae394b2d4846e14763af593a49c1129fa1f9a25e, plus both R271 research branches research/r271-fibonacci-reset-entropy-20261025-r3 and research-draft/r271-sharp-fibonacci-effect-growth-20261025-r4-0225. This paper improves their pigeonhole denominator from order n to order sqrt(n); their sharp exponential base phi is reused, not restated as a new contribution.

Explicit **formal** positive unit-weight BRC model: each path is an ordered word in 0,1. Control q in {0,1,2} starts at 0. q=0 has 0 -> (q'=2,eta=-1,b=-1) and 1 -> (2,+1,-1); q=1 has 0 -> (0,-1,-1), 1 -> (0,+1,-1); q=2 has 0 -> (1,+1,+1), 1 -> (2,+1,-1). The authentic formal affine effect g=(epsilon,k) starts (+1,0) and composes chronologically by g THEN (eta,b)=(eta epsilon,eta k+b). The action on six FORMAL slots is F_g(z1,...,z6)=(epsilon z1+k,epsilon z2,z3,z4,z5,z6). These six slots do not assert a native P000 X6 physical embedding. A source automaton has r=0 if no 00 and the last symbol is 1 or word empty, r=1 if no 00 and the last symbol is 0, r=2 absorbing after 00. All transitions carry positive weight 1.

A reset word ends at (q,r)=(0,0). Let a_n be its count, s_n its sum of translations k, t_n its sum of k^2. Let M_n=max_(epsilon,k) P_n(q=0,r=0,epsilon,k).
The six observed channels are C=((0,0),(0,1),(1,0),(1,1),(2,0),(2,1)), with the second bit h=1 if and only if r=2. Let H_n(c,g) count words in channel c with complete effect g, and B_n=max_g min_(c in C) H_n(c,g). All maxima are over a finite set at each n.

## R272.1: exact moment rational functions

The first-return words from (q,r)=(0,0) are uniquely
A_j=1^(j+1)01, j>=0, length j+3, effect (+1,-(j+1));
B_j=01^(j+1)01, j>=0, length j+4, effect (-1,-(j+2)).
Every reset word is a unique concatenation of them, including the empty concatenation.

Let A_i(z), B_i(z) denote the generating functions in word length weighted by the i-th powers of the positive translation magnitudes of the respective blocks, i=0,1,2:
A0=z^3/(1-z); B0=z^4/(1-z);
A1=z^3/(1-z)^2; B1=z^4(2-z)/(1-z)^2;
A2=z^3(1+z)/(1-z)^3; B2=z^4(4-3z+z^2)/(1-z)^3.

Appending A_j sends a previous translation x to x-(j+1); appending B_j sends x to -x-(j+2). Consequently the complete, not sign-truncated, first and second moments obey identities of formal power series:
C(z)=1+(A0+B0)C(z);
S(z)=(A0-B0)S(z)-(A1+B1)C(z);
T(z)=(A0+B0)T(z)+2(B1-A1)S(z)+(A2+B2)C(z).
Since A0-B0=z^3 and B1-A1=-z^3, solving gives EXACTLY:

C(z) = (1-z) / [(1-z-z^2)(1+z^2)]
S(z) = -z^3(1+2z-z^2) / [(1-z)^2(1+z^2)(1-z-z^2)(1+z+z^2)]
T(z) = z^3(1+6z+2z^2-z^3) / [(1-z)(1+z^2)(1-z-z^2)^2(1+z+z^2)].

Here C=SUM_n a_n z^n, S=SUM_n s_n z^n, T=SUM_n t_n z^n; a_0=1, s_0=t_0=0. This is an exact signed-translation moment identity for positive branch counts, not a signed-mass cancellation.

## R272.2: limiting mean and linear variance of reset translation

Put phi=(1+sqrt(5))/2, rho=1/phi=(sqrt(5)-1)/2. For every n>=3 the reset sector is nonempty; K_n is the translation under the uniform probability on its a_n original words. Then:

E[K_n] -> mu = -(9+3 sqrt(5))/4;
Var(K_n) = nu*n + O(1), where nu=3/2 + 7 sqrt(5)/10 > 0.

PROOF: Each displayed rational generating function has a unique pole of least complex modulus rho from 1-z-z^2; every other pole is on or outside |z|=1 (at z=1, cubic roots, ±i, or z=-phi). Elementary partial fractions, multiplying the rational functions by (1-z/rho) or (1-z/rho)^2 and setting z=rho, establish the principal parts:
C(z) ~ (1/5)/(1-z/rho);
S(z) ~ (mu/5)/(1-z/rho);
T(z) = (nu/5)/(1-z/rho)^2 + O(1/(1-z/rho)).
The other poles yield a_n=(1/5)phi^n+O(1), s_n=(mu/5)phi^n+O(n), and t_n=(nu/5)n phi^n+O(phi^n). Thus E[K_n]=s_n/a_n=mu+o(1); E[K_n^2]=t_n/a_n=nu n+O(1). Subtracting the bounded squared mean proves the claim. This holds for all sufficiently large n in the asserted asymptotic sense, rather than by extrapolating finite computation. QED.

## R272.3: sqrt(n)-denominator pigeonhole theorem

The following constants are explicit:
liminf_(n->infinity) [M_n sqrt(n)/phi^n] >= 1/[15 sqrt(3 nu)] > 0;
liminf_(n->infinity) [B_n sqrt(n)/phi^n] >= phi^(-7)/[15 sqrt(3 nu)] > 0.

PROOF OF FIRST: Fix R>sqrt(nu). Chebyshev and R272.2 give that at least 1-nu/R^2-o(1) of all reset words have |k-E[K_n]|<=R sqrt(n). Every n-step translation k has parity n because eta and b are each ±1, so such an interval contains at most R sqrt(n)+2 admissible integer translations. The sign epsilon offers only two values. Thus at most 2(R sqrt(n)+2) complete effects cover that fraction of a_n=(1/5+o(1))phi^n reset words. A single complete-effect fiber must contain at least a_n(1-nu/R^2-o(1))/[2(R sqrt(n)+2)]. Therefore the first liminf is at least (1-nu/R^2)/(10R). Maximizing over R gives R=sqrt(3nu) and constant 1/[15 sqrt(3nu)].

PROOF OF SECOND: An independently checked seven-step base fiber has the identical complete effect (+1,-3) in all six channels, with positive counts b_7=(2,2,3,1,1,9). Every maximizing length-m reset word returns to the initial (q,r) with the same complete effect g_m. Concatenating such a reset word with each base word is injective on ordered selector words and preserves its channel, yielding for n=m+7 one common effect g_m THEN (+1,-3) and H_n(c,g)>=M_m b_7(c). Consequently B_(m+7)>=M_m; the first bound, with n=m+7, proves the second. QED.

THIS ADVANCES R271: it upgrades its elementary phi^n/O(n) effect-fiber lower bound to phi^n/O(sqrt(n)), with explicit positive liminf constants. A variance estimate alone does NOT give a local central limit theorem, a matching O(phi^n/sqrt(n)) upper bound, or an asymptotic equivalent for M_n or B_n.

## R272.4: decoder information-loss corollary and exact boundary

For a D(d) positive rational BRC aggregator with authentic affine labels and a deterministic, possibly time/effect-dependent single-valued terminal channel decoder D(v,n,g), each of d internal states can contribute to at most one channel at a fixed (n,g). Thus for 1<=d<=5, its best possible worst-effect UNNORMALIZED channel L1 error has:
liminf [sqrt(n)/phi^n * max_g ||H_n(.,g)-Hhat_n(.,g)||_1] >= (6-d)phi^(-7)/[15 sqrt(3nu)].
If total unmarked mass is also exact for that same effect, the right side doubles. The statement neither rules out d=6 nor gives a normalized-by-2^n positive error floor. The broad six-vs-seven representability problem remains open.

## Reproduction, source usage, and next research unit

R272_verify.py uses exact-integer full (q,r,epsilon,k) recurrences to depth 100; independently enumerates 4095 raw words through length 11; verifies a_n,s_n,t_n coefficient-by-coefficient against the above three rational functions by integer polynomial arithmetic; confirms seven-step b_7 and R270's separate P_30(q=r=0,+1,-4)=16482. R272_independent.cpp uses a different moment-semiring recurrence directly on A_j/B_j concatenations through length 100, independently obtaining matching integers. All checked locally; neither program is a native Enterprise Math execution or formal theorem prover. See R272_REPORT.json and R272_CPP_OUTPUT.txt for exact finite-scope receipts.

Read-authority evidence: authenticated GitHub identity awdawmip and repo push; native em_status version 0.6.11, but em_control_tasks returned CONTROL_QUOTA. Therefore no active owner/CLAIM verification, native session, formal Result, independent Driver review, or mathematical admission is asserted. Reuse state is REUSE_APPLIED for the existing positive BRC affine THEN and original-word histogram; source-native module execution is pending. No adjustment to protected P000/worldview.

Next scientific question A: prove or disprove a matching local-limit/anti-concentration upper bound O(phi^n/sqrt n), taking sign and parity periodicity and control-state conditioning into account. Next distinct question B: settle D(6) versus D(7) exact effect-conditioned positive representation via an actual six-state system or a valid cross-depth impossibility certificate. Future work must not conflate these independent claims.
