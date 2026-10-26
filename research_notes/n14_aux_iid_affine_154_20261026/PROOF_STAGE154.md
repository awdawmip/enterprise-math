# Stage154 — exact full-real optimum interval for external N14 iid model

**Evidence:** AUTHOR-level finite rational computation-assisted proof. Neither native CLAIM/Result nor independent Driver acceptance is asserted. This is an EXTERNAL auxiliary model; no P000/X6/Heartbeat transfer is proved.

## Model and theorem

Observations are iid on {0,1,2} with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), horizon N=14. Arbitrary ordered-history randomized policies decide P, decide Q, or continue. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau). Define V14(alpha)=min max(tP,tQ) subject to both errors<=alpha.

At the previously author-proved Stage153 endpoint,

    alpha153=18373341781933759925/52808422392537808896
    V153=318626572163909741813/26404211196268904448.

**Theorem:** For every REAL 0<=delta<=24903625/2200350933022408704,

    V14(alpha153+delta)=V153-(136694960/199229)*delta.

New endpoint and attained value:

    alpha154=18373341782531446925/52808422392537808896
    V154=318626571958867301813/26404211196268904448.

This Bellman supporting line has a **sharp right endpoint**.

## Exact dual direction and first closure

At a count state s=(n,a,b), the iid likelihood ratio Q/P is rho(s)=2^(a+b)/3^a. The exact lower dual recursion is H(s)=min(K*rho(s),L,1+sum_i P_i H(child_i)), with no continuation at n=14. For every history-dependent randomized policy,

    H(root)<=tP+L*eP+K*eQ<=max(tP,tQ)+(K+L)*alpha.

At Stage153 K0=5994/17,L0=5960/17, B=(11,0,1) is a Q/continue tie. R=(12,2,2) was another Q/continue tie, but its Q-stop coin saturated at 1. With R choosing Q and every strict action held fixed, the exact B gap is

    cost(Q)-cost(C)=-239/192-(7/288)K+(43/1536)L.

Holding B tied requires dL/dK=112/129. Traverse K=K0-t, L=L0-(112/129)t. For every state and alternative action, its cost gap is affine in t under these fixed selectors. The first vanishing strictly positive gap occurs at

    t=30922074/3386893, S=(10,5,4), action C tying former Q.

R's Q/continue gap opens strictly favoring Q; all other positive gaps remain strictly positive up to this first closure. The exact candidate:

    K154=68426856/199229, L154=68268104/199229,
    H154(root)=1824690544010408840595299/7275912299338115579904.

Fresh exact Fraction Bellman recursion over **all 680 states** gives exactly two tied states S=(10,5,4) Q/C and B=(11,0,1) Q/C, **1238 strictly positive** nonminimal action gaps, **zero negative** gaps, minimum positive gap **4439/398458**. The executable checker in this directory recomputes the exact dual; the source run's ray scanner is in the separate packaged local execution evidence.

## BRC carrier, first hits, and primal construction

The applied BRC carrier is the positive-rational weighted family of ordered observation paths, retaining multiplicity and order for first-hit and terminal observers. The count-state quotient is justified only because these iid conditional suffix costs depend on the counts. The BRC positive weights do not model signed-amplitude cancellation.

Among literal ordered histories stopped at the first hit of either tie:

    B: 11 prefixes; Pmass=107421875/1451188224; Qmass=107421875/725594112.
    S: 300 prefixes; Pmass=125/5435817984; Qmass=125/2579890176.

B and S first-hit path cones are disjoint. S has n=10,a=5 whereas B has n=11,a=0; after reaching S, a cannot decrease to 0, while the deeper B cannot precede S. Hence mixing the two tie actions gives an exactly affine four-observer vector M=(eP,eQ,tP,tQ).

Let b be immediate Q-stop probability at B and s immediate Q-stop probability at S; elsewhere use unique dual minimizers. The complete rational coefficients in

    M(b,s)=M00+b*dB+s*dS

are

    M00=(1213130559133721035/3505953353861431296,
         224414695416865/641959232274432,
         5325515997084071317/438244169232678912,
         629052207655561/53496602689536)
    dB=(4619140625/2229025112064,
        -751953125/417942208512,
        -25673828125/278628139008,
        -17939453125/104485552128)
    dS=(57875/66795331387392,
        -41375/53496602689536,
        -783125/25048249270272,
        -265625/4458050224128).

The mixed four-vector M11-M10-M01+M00 is exactly zero. Independent-in-implementation AUTHOR cross-check: recursive count-state Fraction four-observer vectors equal literal prefix integer-likelihood DFS at all four deterministic coin corners. DFS visited respectively 473212,466012,473080,465880 history prefixes at (b,s)=(0,0),(0,1),(1,0),(1,1).

The exact equal-error compensation is

    b(s)=7483738461750611/8143872000000000
         -(1149859/2714624000000)*s, 0<=s<=1.

Every real parameter gives 0<b(s)<1. Along this path eP=eQ ranges from alpha153 at s=1 to alpha154 at s=0, with width eta=24903625/2200350933022408704. The P-mean time at these endpoints is exactly V153 and V154. The endpoint values of tP-tQ are

    s=1: 36937438597383360865/79212633588806713344>0
    s=0: 36937439023305630865/79212633588806713344>0.

The time difference is affine, so tP>tQ throughout. At both endpoints, tP+L*eP+K*eQ=H154(root) exactly, extending by affineness to all real s in [0,1]. Thus the policies attain the global dual bound on the entire interval, proving the theorem.

## Sharpness beyond the endpoint

Finite behavioral sequential policies form a compact polytope and the optimum exists. Equality with the same Bellman bound for alpha>alpha154 would force both eP=eQ=alpha (as K,L>0), tP=max(tP,tQ), and every positive-mass reached prefix to choose only a Bellman-minimizing action. All nontie states are strict. At each tie count-state, history-dependent coins can be likelihood-weight averaged because iid suffix laws and prefix Q/P ratio coincide within the count fiber; this preserves all four observers. Disjoint B/S cones then force every equality policy into M(b,s) with 0<=b,s<=1. Equality of errors forces the exact b(s) above; its maximal common error is alpha154. Contradiction. The supporting line is strictly below V14(alpha) to the right of alpha154.

## Verification, source boundary, next problem

The locally executed Fraction recursion and separate integer-weight ordered-prefix DFS passed the 680-state gap audit, four corners, zero interaction, exact first-hit masses, endpoint equalities, and entire affine interpolation. A second local run of the portable verifier regenerated byte-identical certificate154.json. Exact local package includes execution stdout, ray scanner and Stage155 candidate scanner. This is an AUTHOR proof, not independent Research Driver verification, formal theorem admission, or a P000/X6/Heartbeat claim.

GLOBAL_KNOWLEDGE_V1 fixed source main@6e84481e58c479a0f3945b5317a8c09feabbf3af; the P000 startup projection matched the original SHA 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview and current portable research protocol were read. GitHub actor awdawmip. Native control tasks returned CONTROL_QUOTA and own session start STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Active owner/CLAIM/Result/independent Driver remain unverified.

**Stage155 remains OPEN:** at the new right endpoint S continues (s=0), B is still mixed. Continuing along dL/dK=112/129, the next exactly scanned dual candidate is K155=L155=5736/17; terminal T=(14,0,0) gains a P/Q tie while B remains Q/C. The candidate 680-state Bellman check found 1238 positive gaps, minimum 4961/892296. This is a dual candidate, not a proved Stage155 optimal interval. See NEXT_TASK_PACKET_155.md.
