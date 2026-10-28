# R5 — Exact joint feasible region for two-law total variation at a fixed likelihood-ratio mean

Author-side portable research, 2026-10-28, TASK_RESEARCH, local researcher label LOCAL_EM_R5_20261028_1844_JOINTTV; not an authenticated native Source session. AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED.

Frozen global knowledge: awdawmip/chatgpt-global-knowledge main@1c2f11b5864d7379e6439c2e2036f72984928917. Project input: awdawmip/enterprise-math main@d2c0f93feaa3fc9350f843a074591c715b3bbddc. Read canonical entry/manual, P000, ACTIVE worldview and portable research contract. Direct predecessor: research_notes/brc_r5_fixed_mean_tv_diameters_20261028_t1740/PROOF.md. Its simultaneously sharp independent TV diameters do NOT classify the joint feasible set.

## Theorem: complete joint TV polygon and exact strict-positive locus

Fix integer n>=3, 0<s1<...<sn and s1<r<sn. Two source-tagged Q conditional kernels q,q' have nonnegative entries, sum to one, and satisfy both weighted means sum(s_i q_i)=sum(s_i q'_i)=r. Their P kernels are p_i=s_i q_i/r, p'_i=s_i q'_i/r. Put u=TV(q,q')=sum|q_i-q'_i|/2 and v=TV(p,p')=sum|p_i-p'_i|/2.

**Necessary and sufficient:** the feasible (u,v) over all real nonnegative kernels is exactly the intersection of these linear halfspaces:

    u >= 0
    s2*u <= r*v <= s[n-1]*u
    r*v - s1*u <= r-s1
    sn*u - r*v <= sn-r.

The inequalities also imply 0<=u<=1. For n>=4 this is a convex polygon; for n=3 it is a line segment (s2=s[n-1]). When n=2 the feasible set is only (0,0).

**Strict positivity:** q_i,q'_i,p_i,p'_i>0 for every i is possible precisely at (0,0), and at every u>0 satisfying the ratio wedge above together with STRICT last two inequalities. The wedge edges remain attainable with strictly positive kernels. Strict inequalities imply u<1. Rational signatures, r, u, v yield rational witnesses.

**Four-signature witness:** every feasible pair over nonnegative kernels has a realization with both Q kernels supported on the four signatures {s1,s2,s[n-1],sn} (three signatures for n=3). This preserves only the pair of TV observers; it does not preserve a future sequential experiment or full BRC branch provenance. For strict positivity construct common full-support positive overlap as below.

## Proof of necessity

Let d=q-q', a_i=(d_i)_+, b_i=(-d_i)_+, c_i=min(q_i,q'_i). Then q=c+a, q'=c+b, a_i*b_i=0; the equal zeroth and first moments imply

    sum a = sum b = u,
    sum s_i*a_i = sum s_i*b_i = r*v.

For u>0 write m=r*v/u. The disjoint-support probability laws a/u and b/u both have mean m. If m<s2, each of these laws necessarily has positive mass at the unique signature s1 below s2, contradicting disjoint support; similarly m>s[n-1] requires both to use sn. Hence s2<=m<=s[n-1], yielding the wedge. If u=0 then q=q' and v=0.

The shared overlap c has total mass 1-u and first moment r-r*v. Since c>=0 with signatures in [s1,sn],

    s1*(1-u) <= r-r*v <= sn*(1-u),

equivalent to the two outer halfspaces. Their sum implies u<=1. If q and q' are strictly positive, then c_i>0 for all i and its moment lies strictly between the two extreme moments; the two outer inequalities are strict.

## Proof of sufficiency (explicit construction over all real points)

For u=0 take any common positive kernel of mean r. For u>0 set m=r*v/u in [s2,s[n-1]].

Choose probability A supported on {1,n}, with A1=(sn-m)/(sn-s1), An=(m-s1)/(sn-s1). It has mean m. If n>=4 choose B supported on {2,n-1} with B2=(s[n-1]-m)/(s[n-1]-s2) and B[n-1]=(m-s2)/(s[n-1]-s2). If n=3, m=s2 and B is point mass at index 2. In either case A and B have disjoint supports and the same mean m.

The outer halfspaces give an overlap vector c>=0 of total mass 1-u and moment r-u*m. If u<1, let mu=(r-u*m)/(1-u) in [s1,sn], and choose c=(1-u) times the two-endpoint distribution with mean mu. If u=1, both outer inequalities must be equalities, forcing m=r, and take c=0. Set q=c+u*A and q'=c+u*B. These two kernels are normalized, have mean r, and q-q'=u*(A-B) with disjoint positive/negative supports. Thus TV_Q=u and TV_P=(u*m)/r=v. This proves all four inequalities are sufficient without approximation or finite-grid assumptions.

For the strict-positive locus, the two strict outer inequalities give u<1 and s1<mu<sn. There exists an all-coordinate-positive probability law of mean mu: add an arbitrarily small positive uniform component and adjust the remaining component on the extreme signatures. Taking c=(1-u) times this law makes every q_i and q'_i strictly positive without changing their difference and both TVs. All rational inputs permit rational choices. QED.

## Geometric corollaries

For each m in [s2,s[n-1]], the sharp possible range is 0<=u<=tau(m), v=(m/r)*u, where

    tau(m) = min{1, (r-s1)/(m-s1), (sn-r)/(sn-m)}.

The polygon's at-most-four vertices are (0,0), (tau(s2),s2*tau(s2)/r), (tau(s[n-1]),s[n-1]*tau(s[n-1])/r), and (1,1) when s2<=r<=s[n-1], with duplicates removed. Thus for ANY real signed coefficients alpha,beta the exact maximum of alpha*u+beta*v is the maximum over just these vertices; the exact minimum is the corresponding minimum. For fixed feasible u, the exact sharp conditional interval is

    max(s2*u, sn*u-sn+r)/r <= v <= min(s[n-1]*u, r-s1+s1*u)/r.

Both two-law TV extrema of the earlier R5 note follow by projecting this polygon.

## Rational diagnostic (strict false-positive removed)

With s=(1/2,1,2,3), r=3/2, the joint polygon has vertices

    (0,0), (3/4,1/2), (1,1), (2/3,8/9).

Earlier independent maxima R_Q=R_P=1 and the sharp ratio wedge 2u/3<=v<=4u/3 would permit (u,v)=(1,2/3). The NEW facet 3u-(3/2)v<=3/2 excludes it by an exact violation 2>3/2. A strictly positive example of an actually attainable pair is

    q=(12/25,1/10,1/10,8/25),
    q'=(3/25,2/5,2/5,2/25),
    (u,v)=(3/5,3/5).

Both Q means are exactly r, and P distributions are strictly positive as well.

## Verification, provenance and limits

The accompanying executable uses Python Fraction with zero floating point operations. It verifies six rational parameter settings n=3..6, constructs 378 strict-positive exact examples, enumerates and audits 491 rational-grid law pairs, and checks the excluded false-positive and independent positive witness. The original run output ends ALL EXACT JOINT-TV-POLYGON CHECKS PASSED. A finite check supports examples only; the universal statement follows from the proof above.

BRC interface resolution: REUSE_APPLIED to strictly positive branch mass, hidden source provenance, P/Q likelihood ratio transport and the signed first-moment residual. The TV pair is a deliberately narrow observer, not an X6-native state quotient. No original Heartbeat X6 trajectory, time evolution, native BRC-only operation, or global signed support-hull equality is established. P000 stays unchanged.

Prior art background only (not a novelty or priority claim): Charalambous, Tzortzis, Loyka and Charalambous, 2013, Extremum Problems with Total Variation Distance and their Applications, https://arxiv.org/abs/1301.4763.

Native control reads: em_control_tasks returned CONTROL_QUOTA; em_status declared research_authority_granted=false; em_session_start was rejected STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Accordingly this is an author-side research artifact only, not a live native CLAIM, Result or independent review. Next: impose cross-level continuation/occupation flow constraints on the product of these local TV polygons, and seek an exact rational witness proving the global feasible set strictly smaller than their product; only then revisit signed support equality of full versus LR behavior.