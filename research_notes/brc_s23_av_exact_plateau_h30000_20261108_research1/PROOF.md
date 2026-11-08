# S23/AV exact saturation plateau through H=30000

Date: 2026-11-08 Asia/Shanghai. Status: author-side exact finite theorem; independent mathematical review pending.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor: PR #1777, cc2fb563907b0197a3036a3ee47cf21690dc2bad, and the earlier complete endpoint certificate N(7000)=2455069. We reuse the exact H=510 lower bound (11-residue modular certificate). New endpoint is H=30000.

## Theorem

Consider the two-point iid S23/AV auxiliary model, with labels (1,3,4), P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28). Let N(h) be the minimum prefix length n for which attainable prefix likelihood scores occupy every open cell determined by all length-at-most-h future likelihood thresholds (label 3 supplies padding). Then

    N(h) = 2,455,069  for all integer h with 510 <= h <= 30000.

This extends the prior 510..7001 plateau by 22,999 additional integer horizons.

## Exact mathematics and complete finite certificate

Define r=ln(7)/ln(10/7), t(v,j)=r*v-j for integer v,j>=0, v+j<=H. All threshold coordinates are distinct: r is irrational since a rational r=p/q would yield 7^q=(10/7)^p, contradicting unique factorization. Prefix scores E(k,l)=k-r*l have k,l>=0 and k+l<=n, and every such pair is attainable with label-3 padding.

The 45-term atanh rational series with explicit positive tail bound, for log(2), log(8/7) and log(5/4), proves LO/Q<r<HI/Q, where

    Q=10^26
    LO=545569623581288298975349314
    HI=545569623581288298975349315.

Put P=2074774, D=380295. With gcd(P,D)=1, H=30000<D, and

    H * max(abs(LO*D-P*Q), abs(HI*D-P*Q)) < Q,

every comparison between distinct t(v,j) is exactly equivalent to comparing integer keys P*v-D*j. Proof: a nonzero difference in v has magnitude <=H, and the rational P*(delta v)/D differs from every integer by at least 1/D; the perturbation from r is strictly less than 1/D. For delta v=0 the ordering is exactly the integer order in j. Thus integer keys are injective and give the precise irrational threshold order.

For each v=0..H, the threshold row is sorted as j=H-v,H-v-1,...,0. An integer priority-queue merge emits every point, using H+1 live nodes. The compiled executable STREAM_GAP_CLASSES.cpp made an exhaustive pass of all M=(H+1)(H+2)/2=450,045,001 points, thereby covering all 450,045,000 consecutive bounded cells. It groups every actual adjacent pair left=(v,j), right=(v+dv,j+dj) by its integer difference (dv,dj). It records V=max left-v, J=max left-j, S=min(left-v+left-j), and class cardinality.

Uniform class-lift lemma: Given integers K,L with

    K>=J, L>=V, K+L<=n+S,
    0 < K-r*L < r*dv-dj,

the class has a valid prefix witness in every cell, namely (k,l)=(K-left-j,L-left-v), of length at most n. The last two strict inequalities are certified with only integers:

    K*Q > HI*L,
    (K+dj)*Q < LO*(L+dv).

Both comparison coefficient sides L and L+dv are nonnegative by construction; all 78 classes passed the explicit verifier. The dominant class (79,431) has 434,874,286 cells; its uniform witness (K,L)=(2074774,380295) has maximum length exactly n=2,455,069. The maximum prefix length among all 77 remaining classes is only 163,728.

The two exterior cells have valid prefix witnesses (k,l)=(0,5499) and (163671,0), respectively. Their signs follow from the rigorous LO/HI enclosure; both lengths are <= n. Thus N(30000)<=2455069.

Previously published exact N(510)=2455069 supplies the sharp lower bound. As T_510 is contained in T_h and T_h is contained in T_30000 for 510<=h<=30000, monotonicity gives N(h)>=N(510) and N(h)<=N(30000), establishing the theorem.

## Executed verification

A new optimized C++17 exact integer-key streaming implementation (STREAM_GAP_CLASSES.cpp) emitted all class records. A separate Python Fraction/int certificate checker (VERIFY_CLASS_CERTIFICATES.py) established the log enclosure, key-order horizon condition, all class witness inequalities, cardinality sum and both exteriors. The code was executed locally under C++17 g++ 14.2.0 and Python standard library. Transcript: RUN_EVIDENCE.txt; complete exhaustive class statistics: CLASS_H30000.csv.

Cross-implementation regression H=7000: 33 classes and class digest 2aef3d6d6f687ae0ebed385e34653a822139f49c881d2a0dfaf7ce325643242d, exactly identical to the earlier Python stream certificate.
H=10000: 50,015,001 points, 39 classes, digest aa7d947b3709623c6dd458d9313307fba46d645e81edbc2707277213deb52cbb.
H=20000: 200,030,001 points, 59 classes, digest 21a2363035e1ba787d02f7785cacdecf3c488a8b01ec6ad5e655735454962972.
H=30000: 450,045,001 points, 78 classes, digest 610f04c716a9cf82173f340e813c38cfa0ca5ed5768a607885d0c543830a4193.
The class digest is SHA-256 of newline-separated decimal rows dv,dj,V,J,S,count,K,L,K+L-S in decreasing count then coordinate order. Actual C++ H=30000 streaming pass: 33.2337s. The Python H=30000 certificate finished with zero unresolved classes.

## Scope and next mathematical unit

BRC retention: (k,l) is the joint count of labels 1 and 4, with label-3 padding, and every future threshold cell remains observable. This theorem is for the two-point auxiliary sign observer, with full six-source ten-label mother-model mapping and four-observation minimax delta_4 retained as separate questions.

The immediate next unit is to determine whether the same n works at H>30000, ideally via a nonenumerative characterization of consecutive displacement classes in a triangular lattice cut by the irrational projection. Study the non-dominant max-witness growth, formulate a uniform class-generation rule, and find the first exact empty cell if one emerges. No native Owner/CLAIM was acquired: the gateway status call returned BACKEND_IDENTITY_OR_VERSION_MISMATCH/STATUS_DATABASE_UNAVAILABLE with operation_sent=false on 2026-11-08. This is author-side proof evidence for future independent mathematical review.
