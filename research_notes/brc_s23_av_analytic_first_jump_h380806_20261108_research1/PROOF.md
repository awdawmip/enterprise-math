# S23/AV: analytic plateau through h=380805 and its exact first jump at h=380806

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_SIDE_ANALYTIC_PROOF_WITH_EXACT_RATIONAL_CERTIFICATE; independent mathematical review pending.
Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
This study continues existing Draft PR #1777.

## Theorem

For the two-point iid S23/AV auxiliary likelihood-sign experiment with labels (1,3,4), P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28), the likelihood ratio after counts (k,ell) of labels 1,4 is 7^(k+ell)/10^k. The label 3 adds no log likelihood ratio and allows padding to a common prefix length.

Let T_h={10^i/7^s : integers 0<=i<=s<=h}. Define N(h) as the minimum common prefix length n such that each open cell in the partition by T_h contains at least one attainable prefix ratio. Then

    N(h) = 2,455,069 for every integer 510 <= h <= 380,805,
    N(380,806) = 4,530,352.

In particular, h=380,806 is the FIRST strict change after h=510, and the exact jump is 2,075,283. The earlier h=5000 and h=18000 exact enumeration certificates are subsumed by this analytic theorem; they remain independent finite corroboration.

The lower inputs are two already published author-side analytic results:
(1) N(510)=2,455,069, from research_notes/brc_s23_av_unimodular_first_entry_20261108_r1/FULL_SATURATION.md at immutable commit 85b53d06d6ba775e516c566c1d79828b6ca9bb1f.
(2) the scaled adjacent cell J_t=(10^431/7^(510+t),1/7^t) has exact first-entry length 4,530,352 for t=380,296, from research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md at that immutable commit.
The following proof supplies two previously missing FULL threshold-cover upper bounds.

## Coordinates and rational certification

Define

    r=ln7/ln(10/7)>0,
    epsilon=79r-431,
    eta=11r-60,
    gamma=eta-epsilon=371-68r,
    K0=2,074,774, L0=380,295, n0=K0+L0=2,455,069,
    d=K0-r L0,
    H0=L0+510=380,805, H1=H0+1=380,806,
    n1=4,530,352.

Define threshold t(v,j)=rv-j for (v,j) in the integer triangle D_H={v,j>=0, v+j<=H}. A prefix count (k,ell) occupies a cell with consecutive endpoints t(p)<t(q) iff t(p)<k-r ell<t(q).

The accompanying VERIFY_ANALYTIC.py evaluates exact rational bounds, using 45 rational atanh terms and a strict positive remainder bound, for

    Q=10^26,
    LO=545569623581288298975349314,
    HI=545569623581288298975349315,
    LO/Q < r < HI/Q.

Its integer assertions establish all of the following strict inequalities simultaneously for H1:

    0<d<epsilon,  epsilon<2d,  0<epsilon<eta,
    eta>4000 epsilon, gamma>6epsilon,
    epsilon*H1<2,  epsilon*(H1+79)<2,
    79gamma+epsilon*H1<3,
    d+gamma-6epsilon>0.

The inequalities are entirely mathematical exact-rational certificates, with the scripts preserving their source computations and actual stdout.

## Lemma 1: no adjacent threshold gap narrower than epsilon

For any distinct p,q in D_H1 satisfying t(q)>t(p), let (dv,dj)=q-p and x=t(q)-t(p)>0.

The integer vectors u=(79,431) and w=(11,60) satisfy det(u,w)=-1, so every integer difference has unique decomposition (dv,dj)=a u+b w. Consequently,

    x=a epsilon+b eta,
    b=79x-epsilon*dv is an integer.

Suppose 0<x<epsilon. As |dv|<=H1, the exact bounds above give

    -2 < -epsilon*H1 < b < epsilon*(H1+79) < 2,

so b is one of -1,0,1.

If b=0, x=a epsilon>0 makes a>=1 and x>=epsilon, impossible.
If b=1, a epsilon+eta<epsilon and eta>4000epsilon yield a<=-4000, so dj=431a+60<=-1,723,940 < -H1, impossible.
If b=-1, a epsilon-eta>0 yields a>=4001, so dj=431a-60>H1, impossible.

Therefore every positive threshold distance in D_H1 is >=epsilon. In particular, every actual consecutive bounded cell has width >=epsilon. This conclusion holds for all H<=H1.

## Lemma 2: every high-v gap has width >=gamma, with one exception at H1

Take p=(v,j) in D_H1 with v>L0. Then j<=H1-v<=510. Suppose q>p in the t order and x=t(q)-t(p) lies in (0,gamma). With b=79x-epsilon*dv,

    -2 < b < 79gamma+epsilon H1 <3,

so b belongs to {-1,0,1,2}.

If b=-1, x=a epsilon-eta>0 entails a>=4001 and dj=431a-60>H1: impossible.
If b=2, x=a epsilon+2eta<eta-epsilon implies a<=-4002, so dj=431a+120< -H1: impossible.
If b=1, x=a epsilon+eta<eta-epsilon implies a<=-2, hence dj=431a+60<=-802. But p has j<=510, so q.j=j+dj<0: impossible.
If b=0, x=a epsilon>0 entails a>=1 and q.v+q.j=p.v+p.j+510a. Because p.v+p.j>=L0+1, feasibility q.v+q.j<=H1=L0+511 requires a=1 and p=(L0+1,0). This is the unique exceptional high-v left endpoint.

At H0=L0+510, even this exceptional step is infeasible. Consequently at H0 ALL high-v bounded outgoing intervals have width >=gamma. At H1, all high-v bounded outgoing intervals except the single one starting at

    p_*=(L0+1,0)=(380296,0)

have width >=gamma. At the exceptional endpoint the outgoing step +u gives

    q_*=(380375,431), q_*.v+q_*.j=H1,
    t(q_*)-t(p_*)=epsilon.

By Lemma 1 no closer positive threshold exists, so this is exactly one adjacent cell of width epsilon. It is the previously studied scaled J_380296 cell.

## Seven translated witness types cover every other cell

For a bounded cell with left endpoint p=(v,j), find nonnegative K,L such that

    0<K-rL < next_threshold - t(p),
    k=K-j>=0, ell=L-v>=0,
    k+ell=K+L-(v+j)<=n0.

The prefix then satisfies

    (k-r ell)-t(p)=K-rL

and thus lies strictly inside that cell.

For v<=L0, take K=K0, L=L0. Its offset is d in (0,epsilon), and Lemma 1 certifies it fits inside every such cell. Since j<=H1<K0, both counts are nonnegative; their sum is n0-(v+j)<=n0.

For v>L0, except p_*, choose the SMALLEST m in {1,2,3,4,5,6} such that v<=L_m, with

    K_m=K0+371+431m,
    L_m=L0+68+79m,
    d_m=K_m-rL_m=d+gamma-m epsilon.

As L_6=380837>H1, such m always exists. The exact inequalities imply for 1<=m<=6

    0<d+gamma-6epsilon<=d_m<gamma

(the upper bound follows from d<epsilon<=m epsilon). Lemma 2 thus places this prefix strictly inside every nonexception high-v bounded cell. Here j<=510<K_m, v<=L_m and

    (K_m+L_m)-(v+j)
      <= n0+439+510m-(L0+1)
      <=n0

since 439+510*6=3499<L0+1. Hence each nonexception bounded cell at H0 or H1 has a valid prefix of length <=n0, which can be padded using label 3.

The two outer intervals have independent easy witnesses. The minimum threshold is -H (at (0,H)); choose (k,ell)=(0,floor(H/r)+1) which has E=-r ell<-H. The maximum threshold is rH (at (H,0)); choose (k,ell)=(floor(rH)+1,0) with E=k>rH. At H1 the exact integer witnesses are (0,69800) and (2077562,0), both much shorter than n0. Exact rational inequalities check the strictness.

Therefore all open cells at H0 have a prefix with length <=n0 and

    N(H0)<=n0.

Combine with the inherited exact lower bound N(510)=n0 and T_510 subset T_h subset T_H0 to obtain

    N(h)=n0 for all 510<=h<=H0.

## Exact first jump at H1

At H1, the seven translated witness types cover all bounded open cells EXCEPT the unique exceptional interval immediately above p_*; the outer intervals are also covered. For that gap the previous scaled-gap lattice result gives first-entry counts

    (k,ell)=(4,149,979,380,373),
    k+ell=4,530,352=n1.

A direct arithmetic check verifies that the corresponding point (ell+380296,k)=(760669,4149979) equals 2*(L0,K0)+(79,431), so its offset from t(p_*) is

    k-r(ell+380296)=2d-epsilon.

The exact inequalities 0<d<epsilon<2d imply 0<2d-epsilon<epsilon. Thus this prefix occupies the exceptional open cell; its length is n1 and padding handles the remaining cells at common length n1. Hence N(H1)<=n1.

The prior exact first-entry theorem for J_380296 establishes N(H1)>=n1. Combining both:

    N(380806)=4,530,352.

Since N(h)=2,455,069 for all preceding integers 510<=h<=380805, the first strict change is H1=380806, of size 2,075,283. QED.

## Verification, information scope and future work

VERIFY_ANALYTIC.py rederives the log enclosure with exact Fraction, checks all numeric strict bounds used in the proof, certifies the complete seven-witness family, both outer cells at H0 and H1, and the exceptional first-entry witnesses. The actual run is RUN_EVIDENCE.txt. The quantifier-eliminating lattice lemmas above prove the infinite-looking range 510..380806 symbolically; no O(H^2) threshold enumeration is needed.

BRC-preserved carrier: joint (label1,label4) counts, label3 padding provenance, and threshold order for all allowed future suffix operations up to h. The result applies to this explicit two-point S23/AV auxiliary likelihood-sign observer. The full-parameter delta4 minimax and six-source/ten-label mother-model observation transfer remain separately open. P000 and ACTIVE worldview unchanged. GitHub PR is author-side durable proof, pending independent mathematical review, native Source owner/claim still unconfirmed when gateway STATUS_DATABASE_UNAVAILABLE.

Next: determine whether larger horizons after 380806 retain N=4530352; classify the next gap family and exact change. Attempt a general staircase theorem with unimodular displacements and finite witness families rather than quadratic threshold enumeration.
