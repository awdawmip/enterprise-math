# EC49BF — Quantitative observation leakage and a lawful right-neighborhood lower witness

**2026-10-30; AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_SYMPY_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.**

This unit follows EC49BE, which already established the exact eta=1/2 endpoint and *qualitative* strictness to its left. The **new** results are (i) a uniform explicit gap for every real eta<1/2 and (ii) an attainable algebraic lower bound on the still-open interval (99/200,1/2). The model is the auxiliary positive-weight 18+18 probability BRC observer alone, not native signed BRC, X6 or physics. At eta=1/2 the observation kernel has zeros; that endpoint belongs to its nonnegative closure if an implementation insists on strictly positive kernels.

## Fixed model

Hidden w=0,1,2 is uniform. The row-stochastic first action x[w,c] uses c=0,1,2,3,STOP(4) with costs (1,1,2,2,0) and sum of all row costs 43/16 (expected C1=43/48). P_eta(u|w)=1/2+(2u-1)(1-w)eta, u=0,1. At a paid c<4 observable fiber, q_w(c,u)=x[w,c]P_eta(u|w)/3, T=sum_w q_w, V=sum_w[43q_w-16T]_+/172. The purchase coin p(c,u) in [0,1] is observation-only and sum pT=C2=13/16. After buying, acceptance may use only (c,u,z), not unobserved w; the maximal score for fixed x,p is H=sum pV.

## Theorem A: all-real quantitative upper bound

For every real eta in [0,1/2] and every lawful real strategy,

    H <= U(eta) := 351/2752 - (1-2eta)/(172(1+2eta)).

This upgrades EC49BE's qualitative strict inequality to an **explicit leakage rate** and does not depend on EC49AV's sparse-to-edge reduction, enumeration, or dual-price certificates.

**Proof.** Reuse the exact elementary score/impurity lemma from EC49BE, valid for all nonnegative triples q:

    (27/172)T - V >= (32/172)(T-max_w q_w).       (1)

Its all-real proof is a 0/1/2-active-score case split: with q sorted a>=b>=c, at most two of 43q-16T can be positive; with 0 active, 27T>=32(b+c); with 1, the loss is 43(b+c); with 2, the loss is 16T+43c and the excess over 32(b+c) is 16(a-b)+27c>=0. The zero-mass case is immediate.

For each paid action c choose a primary row w_c maximizing x[w,c]; set a_c=x[w_c,c], S=sum_c a_c. The first cost implies

    43/16 >= a_0+a_1+2a_2+2a_3
          = 2S-(a_0+a_1) >= 2S-2,

because a_0,a_1<=1. Thus S<=75/32. The purchased primary-label mass is at most S/3<=25/32, whereas purchased total mass is 13/16=26/32. So the purchased off-primary mass obeys

    O := sum_(c,u) p(c,u) sum_(w!=w_c) q_w(c,u) >= 1/32.  (2)

Let r=(1-2eta)/(1+2eta), the minimum-to-maximum observation likelihood ratio (take r=0 at eta=1/2). Since x[w_c,c]>=x[w,c], the associated observed q_(w_c)>=r q_w for every other w. If the primary q is largest, T-max q is all off-primary mass; if an off-primary label j is largest, T-max q includes the primary q>=r q_j and all other off-primary terms. Therefore

    T-max_w q_w >= r sum_(w!=w_c) q_w.                 (3)

Weight (1),(3) by p, sum and use (2):

    351/2752-H >= (32/172) sum p(T-max q)
                >= (32/172) r O >= r/172.

This proves the **whole continuous real parameter interval**, not a grid approximation. It gives a strictly positive gap for every eta<1/2 and equality of the upper bound at eta=1/2, attained by the previously documented EC49BE endpoint policy.

## Theorem B: exact lawful F lower family on the right interval

For 99/200<=eta<=1/2, define

    s=sqrt(19-26eta),
    F=(2752eta^2+42eta+1397-172(1-2eta)s)/(8256(1+2eta)),
    t=(27-10eta-4s)/(8(1+2eta)).

Use x[0,:]=((11-8t)/16,0,t/4,0,(5+4t)/16), x[1,:]=(0,1,0,0,0), x[2,:]=(1,0,0,0,0). Buy every positive-mass paid observable fiber except (c,u)=(0,1), where p=(8eta+s)/(4(1+2eta)). On purchase accept only (c,u,z) from {(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)}. This never accesses hidden w before observation.

For eta in the given interval, 12/5<s<5/2 implies 3/4<t<4/5 and 0<p<1. All 24 atomic score expressions are bilinear in (eta,t); their four exact rectangle corners certify the stated acceptance signs for the whole rectangle [99/200,1/2] x [3/4,4/5]. Exact symbolic substitution establishes first cost 43/16, purchased mass 13/16, and **H=F identically**. Hence:

    F(eta) <= Hmax(eta) <= U(eta)       (99/200<=eta<=1/2),

with both bounds meeting at eta=1/2. **Equality Hmax=F for 99/200<eta<1/2 is NOT proved**; EC49BD's actual optimum theorem ends at 99/200.

## Validation, method limitations and next question

Published VERIFY_EC49BF.py was executed locally with Python Fraction/SymPy 1.14.0. Its result EXACT_REPORT_EC49BF.json verifies the rational eta=1/2 policy, 96 exact bilinear score-corner inequalities, algebraic cost/F identities and 3374 finite three-integer sanity examples. The all-real upper-bound proof above is analytic; the finite diagnostic cannot substitute for it. Exact U sample values: eta=99/200 gives 69833/547648; 199/400 gives 140033/1098048; 499/1000 gives 350633/2749248; eta=1/2 gives 351/2752.

A diagnostic reuse of the prior exact scalar-price checker finds no common price across slabs ending at eta=1/2 for 52 of 196 ordinary edges, including arbitrarily short tested slabs; all 196 admit their own endpoint-only price. This is a **certificate-method obstruction**, not a new feasible strategy. Next EC49BG should classify those 52 edges algebraically and prove or refute Hmax=F on the open interval.

Provenance: GLOBAL_KNOWLEDGE_V1 pinned main@7b33f8066e9993e7c941959a9d738ed405248eb8; Enterprise Math source main@72298ad74a277018c9eda7640abb788b14a77b1d; Draft PR #1730 predecessor branch head read 166b438ab6363eb1d6e91e2a1c845d9058d71d43. P000 and ACTIVE worldview read and unchanged. Native research_authority_granted=false, Owner lookup CONTROL_QUOTA; no Source-native CLAIM, Result, independent review or mathematical admission. Signed BRC/X6/Heartbeat transfer remains separately unproved.


## Corollary: rigorous first-order endpoint gap class

Set epsilon=1/2-eta>0 and C=351/2752. The proved upper/lower enclosure gives

    epsilon/[172(1-epsilon)] <= C-Hmax(1/2-epsilon)
                               <= C-F(1/2-epsilon)

throughout 0<epsilon<=1/200. Direct exact differentiation of the displayed radical formula yields

    F'(1/2) = 1/24 + sqrt(6)/48 = (2+sqrt(6))/48.

Therefore, with no assumption about which interior strategy is optimal,

    1/172 <= liminf_(eta↑1/2) [C-Hmax(eta)]/(1/2-eta)
          <= limsup_(eta↑1/2) [C-Hmax(eta)]/(1/2-eta)
          <= (2+sqrt(6))/48.

In particular C-Hmax(eta) is **Theta(1/2-eta)** near the nonnegative-kernel endpoint. This is a rigorous slope **interval**, not a differentiability assertion for Hmax or an identified derivative. The exact derivative above follows from elementary differentiation of F, or direct symbolic substitution.
