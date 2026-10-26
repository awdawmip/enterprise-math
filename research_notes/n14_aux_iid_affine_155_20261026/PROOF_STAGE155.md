# Stage155 — complete exact full-real N14 auxiliary optimum and right sharpness

**Evidence class: AUTHOR exact-rational computation-assisted mathematical proof.** No native CLAIM, Result, independent Research Driver acceptance, Lean proof or P000/X6/Heartbeat-native transfer is claimed.

## Frozen source and model

Research fixed GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge@6e84481e58c479a0f3945b5317a8c09feabbf3af`, P000 projection canonical blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` verified against original, and ACTIVE worldview. Scientific predecessor source `awdawmip/enterprise-math@cdbfbfdf64459c80354ed2ed084edededa0e129a`, Stage154 author proof and Stage155 candidate; current source `docs/PORTABLE_RESEARCH_PROTOCOL.md` read at initial project snapshot.

External ternary iid experiment N=14: P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). Every complete ordered-history randomized policy defines eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau). Let V14(alpha)=minimum max(tP,tQ) subject to eP,eQ<=alpha.

## Main theorem

At Stage154 author endpoint:

    alpha154=18373341782531446925/52808422392537808896
    V154=318626571958867301813/26404211196268904448.

For EVERY real

    0 <= delta <= 56111350751198065/5069608549683629654016

the exact optimum is

    V14(alpha154+delta) = V154 - (11472/17)*delta.

Its new endpoint and value are

    alpha155=7319074367111079265/21035720123168587776
    V155=5285134557084071317/438244169232678912.

This Bellman supporting line is **strict beyond alpha155** (no larger alpha attains equality in the same support).

## Global exact Bellman lower bound

At count state s=(n,a,b), Q/P=2^(a+b)/3^a. Set K=L=5736/17. Exact backward recursion:

    H(s)=min { K*(Q/P)(s), L, 1+sum_i P_i H(child_i(s)) },

omit continuation at n=14. For any policy, including full-history randomization,

    H(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+(K+L)*alpha.

The frozen Stage154 exact dual-ray first-gap scanner establishes K=L=5736/17 as the first next closure; a fresh Fraction evaluation enumerates all 680 count states with exactly TWO action ties:
- B=(11,0,1), immediately decide Q versus continue;
- T=(14,0,0), terminal decide P versus decide Q.

All other 1238 nonminimal action gaps are strictly positive, minimum 4961/892296; negative gaps zero. Root dual value:

    H(root)=459776515302494289181/1862537719238885376.

Thus the Bellman inequality is globally valid for arbitrary ordered-history policies, not just count-observing deterministic policies.

## BRC ordered first hits and four exact observers

Use positive rational path weights and exact labels of the *ordered observation histories* (BRC carrier), retaining multiplicity and separate P/Q prefix mass until the iid suffix-observer quotient is proved. Literal integer likelihood-weight DFS, stopping at the first tie, obtains:

| tie | distinct first-hit ordered prefixes | P mass | Q mass |
|---|---:|---|---|
| B=(11,0,1) | 11 | 107421875/1451188224 | 107421875/725594112 |
| T=(14,0,0) | 1 | 6103515625/78364164096 | 6103515625/78364164096 |

The first-hit cones are DISJOINT. T has n=14 and cannot precede B at n=11; starting at B with b=1 the b-count never decreases, so T with b=0 cannot be reached. In fact T is exactly the all-symbol-2 sequence. The resulting joint observer is exactly affine and contains no cross term.

Let b in [0,1] be the probability of immediately deciding Q at B (otherwise continue). Let x in [0,1] be the probability of deciding P at terminal T (otherwise decide Q). At all other states take the strict Bellman minimizer. Then

    M(b,x)=(eP,eQ,tP,tQ)=M00+b*dB+x*dT,

where all four coefficients are exact rationals:

    M00=(1213130559133721035/3505953353861431296,
         224414695416865/641959232274432,
         5325515997084071317/438244169232678912,
         629052207655561/53496602689536)
    dB=(4619140625/2229025112064,
        -751953125/417942208512,
        -25673828125/278628139008,
        -17939453125/104485552128)
    dT=(-6103515625/78364164096,
         6103515625/78364164096,
         0,0).

The mixed difference M(1,1)-M(1,0)-M(0,1)+M(0,0) vanishes as an EXACT four-vector. Two distinct author calculation routes agree at the four deterministic corners: iid suffix Fraction recursion on the Bellman DAG and literal unmerged ordered integer-weight DFS. The latter visits respectively 473212,473212,473080,473080 nodes for (b,x)=(0,0),(0,1),(1,0),(1,1). This verification retains branch identity; no signed BRC amplitude cancellation is inferred.

## Every REAL point of the next segment is primal-attainable

The exact error equalization eP=eQ is equivalent to

    b(x)=7483738461750611/8143872000000000 + (320000/7953)*x.

Requiring 0<=b(x)<=1 and 0<=x<=1 yields PRECISELY

    0<=x<=660133538249389/327680000000000000.

At x=0 the policy reproduces the Stage154 endpoint: eP=eQ=alpha154 and tP=V154. At the upper limit b=1 while x remains strictly internal (x<1). At that limit

    eP=eQ=7319074367111079265/21035720123168587776,
    tP=5285134557084071317/438244169232678912,
    tQ=619867207655561/53496602689536.

The error eP=eQ is strictly *increasing affine* in x on the entire legal interval. Its width is

    eta155=56111350751198065/5069608549683629654016.

This covers every REAL alpha in [alpha154,alpha155], without discretization. The tP-tQ gaps at x=0 and at the upper endpoint are, respectively,

    36937439023305630865/79212633588806713344 > 0,
    23020265774412845/48693796581408768 > 0.

Being affine, tP-tQ remains positive throughout. At BOTH endpoints, independently checked by exact rational arithmetic,

    tP + L*eP + K*eQ = H(root).

Affine interpolation therefore preserves dual equality for every real x. Consequently all policies on the line attain the universal dual lower bound. Since K+L=11472/17, the claimed formula and exact endpoint follow.

## Right sharpness

The finite alphabet and finite horizon produce finitely many complete ordered histories. Their randomized behavioral policies form a compact cube; continuous observers attain the optimum. Equality in this same Bellman support for any alpha>alpha155 would require, because K,L>0, eP=eQ=alpha, tP=max(tP,tQ), and exclusively Bellman-minimizing actions at every reached positive-mass history. Every action outside B and T has a strictly positive gap. Within B's count-state fiber the iid suffix law and Q/P ratio are constant; averaging history-specific stop coins with exact P/Q prefix weights preserves all four observers. At T there is only one first-hit prefix. Because the two first-hit cones are disjoint, every equality policy has an effective pair (b,x) in [0,1]^2 and the exact observer M(b,x). Equalizing errors forces the displayed b(x), whose legal x cannot exceed the stated bound, hence common error<=alpha155. Contradiction. The affine support is strict beyond alpha155.

## Evidence scope and next unit

Locally executed exact Python Fraction Bellman/conditional observer recursion and literal ordered-prefix integer-likelihood DFS. Full 680-state enumeration, 1238 positive gaps, exact first-hit P/Q masses, all four deterministic observer corners, mixed term 0, exact endpoints, tP>tQ and dual equality PASS. Complete portable code and JSON certificate are stored in this directory; no result claims formal Lean or independent Research Driver acceptance. The result is an external iid finite-model theorem. Preservation of ordered BRC branch provenance justifies this iid-specific quotient and does not transfer to P000 native six-dimensional Cell dynamics.

Connected GitHub identity: awdawmip. Native control_tasks returned CONTROL_QUOTA; native RESEARCHER session_start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false; active owner, formal native session, CLAIM/Result and review are unverified. The next scientific task starts at B's Q-stop coin b=1 and T's P-stop coin internal, seeking the next exact dual-ray closure and entire primal segment, without conflating GitHub publication with formal task acceptance.
