# N14 auxiliary ternary iid Stage132 — exact full-real optimal affine interval

**Status:** AUTHOR_EXACT_FINITE_COMPUTATION_ASSISTED_PROOF. Two locally run author implementations, independently structured; no independent Research Driver review or native CLAIM/Result. **External auxiliary iid model only**, not a theorem on P000, X6 or Heartbeat.

## Statement and model

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14. Allow arbitrary randomized stopping and decisions based on literal ordered histories. Define eP=P(declare Q), eQ=Q(declare P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=inf max(tP,tQ) under eP,eQ<=alpha.

The preceding author-verified Stage131 endpoint is alpha131=36696744092375906695/105616844785075617792 and V131=660257035708884947227/52808422392537808896.

**Exact theorem:** for every real delta in the closed interval

0 <= delta <= **165455959375/3223170312044544**,

**V14(alpha131+delta) = V131 - (9360948956/7563701)*delta.**

Consequently
- **alpha132=12234055251084235565/35205614928358539264**;
- **V132=72989119067006060803/5867602488059756544**.

The affine supporting line is right-sharp; this is not a claim that tests are infeasible beyond alpha132.

## Universal dual on all ordered histories

At s=(n,a,b), count the first two symbol occurrences; every ordered prefix of that count has ratio r_s=Q(h)/P(h)=2^(a+b)/3^a. Fix K=4830610068/7563701 and L=4530338888/7563701. Compute exactly by backward induction

H(s)=min{K*r_s (declare P), L (declare Q), 1+sum_j P_j H(s+e_j) (continue if n<14)}.

A full Fraction enumeration contains 680 count states, exactly 1238 strictly positive nonchosen-action gaps, zero negatives, minimum strict gap 27060626/5513938029, and only two action ties:
- B=(11,0,1), Q/continue;
- E=(8,3,0), P/continue.

H(root)=244470485409835455673973219/552457976844897119895552.

This Bellman bound applies to **all literal ordered-history policies**, not merely count-based policies: the iid conditional suffix law and likelihood ratio are identical at every ordered prefix sharing a count. In P units, for every policy

H(root) <= tP + L*eP + K*eQ <= max(tP,tQ)+(K+L)*alpha.

## Exact weighted BRC first-hit and moment carriers

Retain positive rational P/Q weight products **per literal word**, ordered provenance, action, and stopping depth until the declared four-observer quotient M=(eP,eQ,tP,tQ). This is real reuse of T0_BRC positive weighted alternative/serial branch calculus; the quotient is scoped only to those four observers and their conditional iid suffix operations. It does **not** identify native P000 observers nor represent signed cancellation.

A differently coded top-down integer-product literal-history DFS gives actual first-hit data under the strict Bellman actions:

| tie | first-hit words | P mass | Q mass |
|---|---:|---|---|
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| E=(8,3,0) | 56 | 21875/497664 | 21875/1679616 |

These ties lie in **disjoint descendant cones**: E has three occurrences of symbol0 at depth8 and cannot reach B with zero such occurrences at depth11; B cannot precede E due to depth order. Accordingly, B/E mixed observer difference vanishes.

Let w be the probability of immediate Q declaration at B and u immediate P declaration at E, each otherwise continuing. For every real w,u in [0,1],

M(w,u)=M00+w*dB+u*dE,

with the exact vectors below, independently confirmed at all four deterministic corners:

~~~
M00=(
2432101679948080769/7011906707722862592,
446766722673041/1283918464548864,
10981948749188861711/876488338465357824,
1282024318342933/106993205379072)
dB=(
4619140625/2229025112064,
-751953125/417942208512,
-25673828125/278628139008,
-17939453125/104485552128)
dE=(
-5043959375/23776267862016,
175590625/626913312768,
-17110778125/330225942528,
-935440625/52242776064)
M11-M10-M01+M00=(0,0,0,0).
~~~

The independent integer-word DFS visits respectively 756514,747778,756382,747646 prefix nodes for corners (w,u)=00,01,10,11, and has 504343,498519,504255,498431 terminal ordered words. No sampling or floating approximation is used.

## Balanced full-real primal family

Solving eP=eQ exactly gives

**w(u)=23520944430861437/81438720000000000 + (20223469/159060000)*u**, 0<=u<=1.

Its endpoints satisfy 0<w(0)<w(1)=3079578232623767/7403520000000000<1. Direct exact substitution yields

eP=eQ=alpha131+(165455959375/3223170312044544)*u,

tP=V131-(51192689603125/805792578011136)*u
    =V131-(9360948956/7563701)*(165455959375/3223170312044544)*u.

The exact tP-tQ margins at u=0 and u=1 are respectively
- 90328566298908296807/158425267177613426688 >0;
- 86558755630978696807/158425267177613426688 >0.

By affinity, tP>tQ everywhere on the real closed interval. Every action in this mixed policy is a Bellman minimizer; hence tP+L*eP+K*eQ=H(root). This attains the unrestricted dual lower bound throughout the full continuum, proving the optimality formula.

## Right-sharpness, including prefix-specific coins

Suppose alpha>alpha132 and a feasible policy achieves the same dual supporting line. The finite behavioral policy domain is compact and its four moment observables continuous, so an optimum exists. Since K,L>0, saturation of the dual chain forces eP=eQ=alpha, tP=max(tP,tQ), and only Bellman zero-gap actions on all positive-mass visited ordered prefixes. Exact strict-gap enumeration leaves randomization only at B and E. For each tie count, all its ordered prefixes have one fixed Q/P likelihood ratio and the same conditional iid suffix. Thus even prefix-dependent tie coins reduce, for the four declared observers, to a P-first-hit-mass-weighted effective stop probability in [0,1]. Because the B and E cones do not overlap, there is no interaction term. The balancing law then forces alpha=alpha131+eta132*u<=alpha132, contradiction. Hence the supporting affine line is right-sharp for unrestricted literal ordered-history policies.

## Verification and limits

Actually executed locally:
1. Python stdlib exact Fraction bottom-up Bellman/four-corner verifier, checking 680 states, every action gap, all tie states, exact duality, margins, endpoints and affine slope.
2. Separately structured top-down integer numerator DFS over literal ordered words, checking actual first hits, complete four-corner moments, 4 prefix visit counts, terminal histories and endpoint identities.
Both PASS. The portable source and exact certificate accompanying this note are author-side publication, not a remotely executed check or an independent Driver review.

**Frozen inputs:** GLOBAL_KNOWLEDGE_V1 main@90a2dbab9e17c77b3a4c74bea4785e6f0e240321; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math input main@49f0bdada7acc91157a9967b5d6374219cd9de25. Native tasks/dispatch returned CONTROL_QUOTA; session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Live owner, CLAIM, native Result, and independent Driver acceptance remain unverified; this ordinary GitHub proof does not impersonate them.

## Next unit: Stage133 dual only

At endpoint u=1, E always immediately decides P while B stays mixed. Scanning K+t*(-1), L+t*(-112/129) closes the first positive gap at t=271154841202800/8917611042701. Candidate K133=717127668/1179001, L133=675046888/1179001; root=36407190671104521664854919/86115052294916278321152. Only ties B=(11,0,1) Q/C and newly F=(8,1,2) Q/C, with 1238 other strict gaps, minimum 129758627/4074627456. **This is DUAL_CANDIDATE_ONLY.** Stage133 primal balance/feasible real interval and sharpness remain open.