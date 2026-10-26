# Stage153 — exact full-real optimal affine segment, N=14 auxiliary iid

**Evidence:** AUTHOR-level finite rational computation-assisted proof. No native task CLAIM/Result, independent Driver acceptance, formal proof assistant check, P000/X6 or Heartbeat-model theorem.

## Statement and frozen model

Ternary iid sequential decision experiment P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14, with arbitrary randomized decisions at complete ordered histories. Put eP=P(decide Q), eQ=Q(decide P), tP=E_P tau, tQ=E_Q tau, V14(alpha)=min max(tP,tQ) with eP,eQ<=alpha.

    alpha152 = 18373003413933759925/52808422392537808896
    V152     = 318745538371909741813/26404211196268904448
    eta153   = 10326171875/1611585156022272
    alpha153 = 18373341781933759925/52808422392537808896
    V153     = 318626572163909741813/26404211196268904448

**Theorem** (every REAL parameter): for all 0<=delta<=eta153,

    V14(alpha152+delta) = V152 - (11954/17)*delta.

This new Bellman lower support is strict for all alpha>alpha153; its right end is sharp.

## Bellman dual valid for all ordered histories

Take K=5994/17, L=5960/17. If s=(n,a,b) records counts, the exact prefix ratio Q/P is r(s)=2^(a+b)/3^a. The dual backward recurrence is

    H(s) = min( K*r(s), L, 1+sum_i P_i*H(child_i(s)) )

with continuation omitted at n=14. The three actions decide P, decide Q, continue. Conditional iid suffix laws depend only on s; hence this recurrence is a global lower bound for ANY randomized, fully history-dependent decision policy:

    H(root) <= tP+L*eP+K*eQ <= max(tP,tQ)+(K+L)*alpha.

Exact Fraction computation of all 680 count states gives

    H(root)=79691642847444362851/310422953206480896.

There are exactly two action ties: B=(11,0,1) Q/continue and R=(12,2,2) Q/continue. The other 1238 nonminimal action gaps are positive, with minimum 71917/33841152; negative gaps: 0.

## Provenance-preserving ordered first hits and four observers

Let b,r in [0,1] be Q-stop probabilities at B,R, with strict dual minimizers elsewhere. Literal ordered-prefix integer-weight DFS stopped at each FIRST hit gives:

    B: 11 ordered prefixes, Pmass=107421875/1451188224, Qmass=107421875/725594112.
    R: 1555 ordered prefixes, Pmass=607421875/61917364224, Qmass=607421875/34828517376.

The two path cones are disjoint. In the sole step from B's n=11 to R's n=12, a would have to increase from 0 to 2, impossible because a increases by AT MOST 1 per observation; R cannot precede B because R is deeper. This resolves a genuine uncertainty in the Stage153 task packet: do NOT infer overlap merely from a_R>a_B.

The full four-vector of observers M=(eP,eQ,tP,tQ) is therefore exactly affine:

    M(b,r)=M00+b*dB+r*dR,

    M00=(1212593154171464035/3505953353861431296,
         74830814973455/213986410758144,
         5330352655382516317/438244169232678912,
         210020984822687/17832200896512)

    dB=(4619140625/2229025112064,
        -751953125/417942208512,
        -25673828125/278628139008,
        -17939453125/104485552128)

    dR=(607421875/3962711310336,
        -607421875/5015306502144,
        -607421875/55037657088,
        -7896484375/417942208512).

The EXACT mixed four-vector difference M11-M10-M01+M00 equals zero. Independent-in-implementation AUTHOR cross-check: recursively computed count-state Fraction four-observer vectors agree at all four deterministic corners with literal-prefix integer-likelihood DFS, which visited 475342, 466012, 475210, 465880 prefixes at (b,r)=(0,0),(0,1),(1,0),(1,1). Signed derivatives here are observer differences of positive branch measures, not primitive BRC signed cancellation.

## Whole-real primal attainment

The equation eP=eQ uniquely forces

    b(r)=2686983670724537/2714624000000000 - (9019/127248)*r.

For every real 0<=r<=1, this gives a legal strict-interior b in (0,1). In particular b(1)=7483735012173611/8143872000000000. Along the entire segment,

    eP=eQ=alpha152+eta153*r,
    tP=V152-(3630560546875/805792578011136)*r.

The two endpoint differences tP-tQ are positive:

    r=0: 12253888791127786955/26404211196268904448
    r=1: 36937438597383360865/79212633588806713344.

Since tP-tQ is affine in r, tP remains the worst expected time for all real r. At r=0 and r=1, exact computation gives tP+L*eP+K*eQ=H(root); linearity extends the equality throughout. Therefore these legal randomized policies attain the global Bellman support at EVERY real alpha in [alpha152,alpha153], giving the slope K+L=11954/17, and the stated new endpoint.

## Right-sharpness proof

Finite ordered-history behavioral policies form a compact polytope, their four observers are continuous, and a minimum exists. If a policy at alpha>alpha153 attained equality in the same dual lower bound, K,L>0 would force eP=eQ=alpha, tP=max(tP,tQ), and every positive-mass reached prefix would use only Bellman-minimizing actions. Other states are strict. Within each tie's count-state fiber the iid conditional suffix laws and Q/P prefix likelihood ratio are identical, so any history-dependent stop coins may be weighted-averaged into one effective coin while preserving all four observers. As the B and R first-hit cones are disjoint, every equality policy must lie on M(b,r). Equalizing errors gives precisely b(r), and with r in [0,1] the common error cannot exceed alpha153. Contradiction. Hence the affine lower support is strict beyond alpha153. A new dual direction after alpha153 is not claimed.

## Reproducible scope and next scientific unit

Actually executed local exact Python Fraction Bellman and four-observer recursion, with separate ordered-prefix integer DFS on all four deterministic corners. 680 states, 1238 positive action gaps, two ties, zero negatives; all exact endpoint and dual equalities PASS. The executed source, portable variant, JSON certificate, and stdout form the author evidence. This is not independent Research Driver review nor proof-assistant certification.

BRC use preserves positive-rational ordered path identities, counts, and likelihood weights until a proved iid suffix-observer quotient is safe. This EXTERNAL auxiliary model is not identified with the P000 six-axis primitive or Heartbeat world; no native transfer theorem exists. This turn's fixed GLOBAL_KNOWLEDGE_V1 snapshot: main@43639a1bd021e9c6e90e699fbb7b5021855fbef7, with P000 projection blob matched original and ACTIVE worldview loaded. GitHub principal awdawmip can write. Native task listing CONTROL_QUOTA; own session_start STATIC_READONLY_SCOPE_DENIED, operation_sent=false. Active owner, native CLAIM, Result, Driver review not verified and not asserted.

Stage154 OPEN: starting at alpha153 with R's Q-stop probability saturated to 1 while B remains interior, determine the first exact dual-ray action-gap closure, preserve true first-hit path relations, and solve the next entire real primal interval or an exact infeasibility witness. Formal Source-native task publication/claim/review are separate gates.
