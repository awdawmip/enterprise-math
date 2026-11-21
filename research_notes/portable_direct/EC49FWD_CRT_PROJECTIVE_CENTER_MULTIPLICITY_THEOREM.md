# EC49FWD — CRT projective coordinates classify the exact optimal reflection multiplicity

Date: 2026-11-22 (Asia/Shanghai). Mode: independent portable continuation; no shared Task CLAIM.
Status: AUTHOR_PROVED / EXACT_FINITE_CRT_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED.
Scientific freeze: BRC16943. Immutable predecessor: awdawmip/enterprise-math@afcbc42bed7e11dbe24a1018751fb0a9f9629e90:research_notes/portable_direct/EC49FWC_UNIT_HOMOTHETY_AND_ANTIPODAL_THEOREM.md.

## Model, terminology and question

P10 is the frozen 44-cell subset of (Z/10Z)^2 appearing as the **nonconfluent auxiliary factor** of the complete mod-11 Bernoulli projective nonroot predicate. Its exact construction from the BRC16943 rational constants is reproduced in the associated executable verifier. For each primitive direction (a,b) modulo 10 (gcd(a,b,10)=1), select an affine base point (h0,n0) with (b-a)h0-a*n0=-1 mod 10 and define S(a,b)={t mod 10 : (h0+at,n0+(b-a)t) belongs to P10}. A different base point cyclically rotates S.

Let delta(a,b)=min_c |S triangle (c-S)| and N(a,b)=#{c mod 10: |S triangle (c-S)|=delta}. The predecessor proved that there are 18 orbits of four unit-related directions, giving representative multiplicities 2,6,6,4 for (delta,N)=(0,1),(2,1),(2,2),(2,4), but did not identify the arithmetic indices of those orbits or a class formula for N.

## Theorem — canonical 3 by 6 CRT projective classification

Put epsilon=(a mod 2,b mod 2), a nonzero vector of F2^2, and lambda=[a:b] in P^1(F5). Normalize lambda=b/a in F5 when a nonzero, and lambda=infinity when a=0.

1. The map (a,b) -> (epsilon,lambda) partitions all 72 primitive mod-10 directions into precisely 3*6=18 classes; each class contains exactly four directions and is one full orbit under diagonal multiplication by units U(10)={1,3,7,9}. This identification is intrinsic to CRT and is independent of the frozen P10 construction.
2. In the specified frozen P10 model, delta=0 if and only if epsilon=(1,0) and lambda is 2 or infinity. Else delta=2.
3. In the same model, the number of *all minimizing reflection centers* is exactly

N(epsilon,lambda) =
  2                                      if epsilon=(1,1);
  1+3*[lambda in {1,3}]                   if epsilon=(1,0);
  1+3*[lambda in {0,infinity}]            if epsilon=(0,1).

Here brackets denote the Boolean indicator, and all comparisons are within F5 / P^1(F5).

Equivalently the complete classification table gives (delta,N):

| epsilon / lambda | 0 | 1 | 2 | 3 | 4 | infinity |
|---|---|---|---|---|---|---|
| (1,0) | (2,1) | (2,4) | (0,1) | (2,4) | (2,1) | (0,1) |
| (0,1) | (2,4) | (2,1) | (2,1) | (2,1) | (2,1) | (2,4) |
| (1,1) | (2,2) | (2,2) | (2,2) | (2,2) | (2,2) | (2,2) |

In particular, the formerly enumerated 6/6/4 representative multiplicities now have an exact arithmetic interpretation: among the 18 CRT classes, six are nonperfect with one minimizing center, six are nonperfect with two, and four are nonperfect with four. There are additionally two perfect classes. Multiplying by four gives the previously verified 72-direction census: (0,1):8, (2,1):24, (2,2):24, (2,4):16. The 136 optimal defect-two center events follow as 24*1+24*2+16*4=136.

## Proof

The Chinese remainder theorem supplies Z/10Z ≅ F2×F5 and U(10) ≅ F5^×, because F2 has only one nonzero scalar. A direction is primitive precisely when its two components are nonzero in F2^2 and F5^2. The three nonzero F2^2 vectors determine epsilon, and each nonzero F5^2 vector lies on exactly one of the six lines of P^1(F5). Four scalar representatives exist per line, establishing 3*6*4=72 and free transitivity of U(10) on each class.

The predecessor's exact P10 unit-covariance identity implies S(ua,ub) is a cyclic rotation or reversal of S(a,b): the speed substitution is t -> u^2*t, with u^2 congruent to +1 or -1 mod 10. Thus both delta and N are invariant on the four-member class.

It remains to compute one representative for each CRT class. For normalized lambda choose (a5,b5)=(1,lambda), or (0,1) for infinity, then obtain (a,b) by the unique separate CRT lifts satisfying epsilon. There are exactly 18 such lifts. Construct P10 exactly from the frozen constants, choose the lexicographically first affine base point, and compute the ordered pair-sum counts

K_c(S)=sum_{t mod 10} 1_S(t)*1_S(c-t), so |S triangle(c-S)|=2(|S|-K_c(S)).

For each of the 18 lifts, take the maximum of the ten integer K_c and count its attaining centers. The attached verifier computes this pair-sum certificate; it checks every row against the three displayed cases, verifies P10 cardinality 44 and full unit covariance on all 100 ambient cells, then independently repeats the center computation on all 72 primitive directions, checking uniqueness and completeness of the CRT classes. All arithmetic is exact integers modulo 10/11, and it returns ALL PASS. This is an exhaustive finite 18-case certificate after an analytic CRT factorization, rather than a claim that the frozen P10 table has a fully symbolic, enumeration-free derivation.

## Why both CRT coordinates matter

The parity direction alone does not determine N: for epsilon=(1,0), lambda=0 gives N=1 while lambda=1 gives N=4. The mod-5 projective line alone does not determine N either: lambda=0 produces N=1,4,2 for epsilon=(1,0),(0,1),(1,1) respectively. Therefore one cannot discard either coordinate *from this particular CRT description* while claiming it individually determines N. This does not assert the 18-class pair is a minimal encoding of the four-valued (delta,N) observer.

The unit factor u is legitimately quotiented only for the declared unsigned observer (delta,N). Reconstructing a particular direction, signed correction orientation, original point or later interaction requires the unit/orientation/provenance label: the present quotient is not a lossless representation for arbitrary downstream operations.

## Verification, dependencies and limits

Associated executable: EC49FWD_CRT_PROJECTIVE_CLASSIFICATION_VERIFY.py. Captured result: EC49FWD_CRT_PROJECTIVE_CLASSIFICATION_OUTPUT.json. An independent Python reconstruction and an independent JavaScript finite reconstruction both returned ALL PASS at the same 3 by 6 table. No floats, probabilistic tests or native-X6 operator computations were used.

The P10 factor is not the complete certificate: the separate confluent mod-11 factor, the Bernoulli-to-projective bridge, and global Farey-gap claims remain inherited from the frozen ancestor. This result concerns only modular arithmetic of a typed auxiliary observation, not native six-axis geometry, a three-dimensional slice or a change to P000. It gives no new formal CLAIM, Result, Review or mathematical admission.

## Next scientific unit

Investigate whether the parity-stratified row formulas admit a direct symbolic derivation from the mod-5 fiber geometry of P10, avoiding even the 18 finite representative calculations. Preserve the mod-11 confluent factor and signed/CRT coupling before applying the classification to a moving Farey-gap argument. The global conjecture lim_{H to infinity} H G_max(H)=1 remains open.
