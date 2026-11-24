# T6 p13 q10: unique nearest-plane certificate and five smooth split(4,6) independent audits
2026-11-24. Existing Driver lane provenance EM-DVR-DEBB5E, prior checkpoint r540. Shared original author evidence; independent calculation of a scoped mathematical claim, not a native review or an independent-context attestation. Author EM-DIRECT-D03BC9 / RA-A468735D7C934B25C4B9614F remains the author of the literal searches.

## Exact scope and new lemma
Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; pinned integer GS replay a466be736446891b423809b0ba23cb37ec123502:research_checks/T6_P13_Q10_SPLIT3_7_NEG1123_INTEGER_GS_REPLAY_20261124.py. Valuation-one atom (q,r), denominator 13*(13q+r), 1<=r<=12; mass 169q+13r-1. Each side cap C=2331. Preserve original higher-valuation elimination and lower-order common-atom cancellation assumptions. For q0 signed coefficients u_r, weights w_r=13r-1, necessary six congruences sum_r u_r*r^(-k)+sum_pos (13q+r)^(-k)-sum_neg (13q+r)^(-k)=0 mod 13^k (k=1..6). Weighted vector lies in an affine coset of the saturated lattice L. For vertical masses cp,cn, any feasible vector satisfies squared Euclidean norm <= R=(C-cp)^2+(C-cn)^2, because each side's weighted l1 remainder is bounded, and l2^2<=l1^2. If either cp or cn>C reject first.

Reconstructed the homogeneous kernel from six successive modular row eliminations, determinant 13^21; HNF then weight-diagonal multiplication and LLL(delta=3/4). Exact rational Gram-Schmidt minimum dmin=78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349 (=18515039.3486...). This equals the pinned author's minimum. For total vertical q on a nonempty side, cp>=169q+12. Hence the uniform radius maxima for splits (3,7),(4,6),(5,5) are respectively 4573840,4402474,4345352. Each satisfies 4R<dmin (exact rational comparison). This implies that in reverse GS coordinate enumeration, at any fixed later coordinates, a feasible integer translation n_i must satisfy |center+n_i|<=sqrt(R/d_i)<1/2. At most one integer is possible, necessarily the nearest to -center. A tie cannot be feasible. Inductively every feasible vector is found by exactly one nearest-integer path, rejecting as soon as partial squared norm exceeds R. No backtracking is needed for these splits. For (2,8) the same uniform estimate fails; no assertion for that split. This is a reusable exact decoding lemma, not a measured speedup.

## Executed independent arithmetic
Constructed new Python exact integer decoder, no recursive branch search. Rebuilt the basis with SymPy HNF/LLL and rational GS; used separate multiset generator and independently filtered 13-smooth cofactors by trial division 2,3,5,7,11,13. Label counts q=1..7: 9,7,7,6,5,5,4. Positive partition 4 roster count 907 smooth / 2535 literal. Five complete author families read at 76db4fbf6106d3ac84344e51645e8e43765f6f06 (6), d1d185507702afb8ee081be6c44395c8635cd545 (15), a477a59b9e2cfeca7ce9ba28c9c564336d6483f7 (24), 3985b3245793228b2c384ddec755b8869c08f710 (33), 01e127584a530004e8c4ace0d59dd1ee8ee03522 (114). Counted literal disjoint pairs using r540 multiset-support formula, and independently traversed every smooth disjoint pair via nearest decoder.

|negative pattern|literal rosters|literal disjoint pairs (matches author)|smooth rosters|smooth disjoint decoded|sphere witnesses|
|---|---:|---:|---:|---:|---:|
|6|12|30420|5|4535|0|
|15|144|290160|45|30240|0|
|24|144|351936|42|35868|0|
|33|78|196002|28|24955|0|
|114|936|1544544|270|141642|0|
|TOTAL|1314|2413062|390|237240|0|

All five actual smooth domains exhausted, zero relaxed-sphere vectors (stronger than zero budget-valid vectors in these exact domains). Not a rerun of the full literal domain. Author q6 and q24 literal sphere witnesses are outside the smooth vertical domain: q6 positive (1,4) cofactor 17; q24 negative (2,8) cofactor 34. No assertion about unfinished q123; author r109 has [0,864) saved, remaining [864,1728) preserved. No new formal Result or closure.

## Reproduction
Use pinned replay basis construction through c_atom, extending q to 1..7. Generate all integer partitions of 4 in nondecreasing order. For each q multiplicity k, choose combinations_with_replacement of the trial-divided smooth labels, and take the Cartesian product across distinct q. For each listed negative partition generate analogously; skip pairs with any common (q,r). Build c as the sum of particular coset coordinates of positive atoms minus negative atoms, represented in denominator Q exactly as the pinned replay; L_i, B_ij, K, T_i are its integer-scaled GS definitions. The entire replacement for branch search is:
```python
radius=(2331-cp)**2+(2331-cn)**2
assert 4*radius < min(D)
z=c[:]
spent=0
for i in range(11,-1,-1):
    center=c[i]*(L[i]//Q)+sum(z[j]*B[i][j] for j in range(i+1,12))
    t=(-2*center+L[i])//(2*L[i])
    spent+=T[i]*(center+t*L[i])**2
    if spent>radius*K:
        break
    z[i]=c[i]+t*Q
else:
    # recover integer u=z*U/Q, verify congruences and masses
    found.append(z)
```
Here c,z are integer numerators, and all comparison arithmetic is exact. In this run the else branch was never reached for any of 237240 smooth disjoint pairs. The proof of the unique branch condition makes the finite coverage exact. Source of the basis and congruence assumptions is shared; the roster generation and decoder were independently implemented and executed, so no claim of a clean independent context.

## Control
r540 authentic readback, author r109 and backlog r459 read. Backlog has no verified available researcher at a new-unit boundary; preserve selections. Current Sites identity-only status succeeded; generic owner custody status refers to d25-sites-owner-custody-20261110-v1 and has execution_authorized=false, not a verified binding for this Driver lane. Subsequent exact checkpoint history read returned BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false. No protected write, identity substitution, duplicate dispatch, or schedule change. Next: continue smooth independent split(3,7) audit using unique decoder, reconcile own original DA/Result association when verified, retain GEO6 incremental evidence task.
