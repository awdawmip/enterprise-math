# T6 p13 q10 split(3,7), negative pattern (1,1,1,2,2): scoped non-author audit

2026-11-24. Existing Driver EM-DVR-DEBB5E, shared author context disclosed. Original author EM-DIRECT-D03BC9, Activity RA-A468735D7C934B25C4B9614F, frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Each side's mass cap 2331. This audit counts the complete roster domain but checks author traversal only in the two supplied intervals [8192,8704), [8704,12800) at the certificate level; no independent GS traversal.

## Source
- research_checks/T6_P13_Q10_SPLIT3_7_NEG11122_8192_8704_AUTHOR_EXACT_CERT_20261124.json @ a09c7d7ab8ca563eb54e1c02ffa0c2e4186aad0e
- research_checks/T6_P13_Q10_SPLIT3_7_NEG11122_8704_12800_AUTHOR_EXACT_CERT_20261124.json @ 81d2860e2873691fe7b2f64d324a56d2996b1e15
- Author readback observations @0df89054534873c4f211881f65981d14a7997edd and @6f585b491e1ef9833fb60c8962f61c690193d681. Preserve original author and existing Activity; no duplicate full calculation or publication of an author result.
- Reuse definitions and budget interpretation from prior scoped audit @8f43217fefd6ee6bf189e6b0d236910668283ffe.

## Exact domain count and smoothness reduction
Atom (q,r) denotes denominator 13(13q+r), mass 13(13q+r)-1, 1<=r<=12. Positive patterns (3),(1,2),(1,1,1) give 520 rosters. Negative pattern (1,1,1,2,2) gives C(14,3) C(13,2)=28392. Raw pairs 14763840. For a fixed negative roster let t be its number of distinct q1 residues and s its number of distinct q2 residues. Disjoint positive rosters are exactly
D(t,s)=12+(12-t)(12-s)+C(14-t,3).
The three terms correspond to the three positive patterns; q3 cannot coincide with any negative atom. The number of such negative rosters is C(12,t) C(2,t-1) C(12,s) C(1,s-1), for 1<=t<=3, 1<=s<=2. Summing gives 8423064 disjoint pairs, 6340776 common-atom pairs.

For maximal prime 13, exact trial division gives allowed r for q1: {1,2,3,5,7,8,9,11,12}; q2: {1,2,4,6,7,9,10}; q3: {1,3,5,6,9,10,11}. Thus positive smooth count 235, negative smooth count C(11,3) C(8,2)=4620, raw smooth pairs 1085700. Smooth disjoint count follows by replacing D with 7+(9-t)(7-s)+C(11-t,3) and the two residue-choice binomials with C(9,t), C(7,s). Sum 522396. This is 6.202% of the literal disjoint domain (93.798% reduction). The full domain count is a combinatorial result, not a claim of full search completion.

Actual JS integer enumeration of all 28392 lexicographically sorted negative rosters (nested a<=b<=c and d<=e in 1..12), using D and the smooth analogue independently of the author GS traversal, gives:
| interval | raw | common | disjoint | smooth negatives | smooth disjoint |
|---|---:|---:|---:|---:|---:|
|[8192,8704)|266240|123770|142470|74|7915|
|[8704,12800)|2129920|928102|1201818|738|83008|
|full domain|14763840|6340776|8423064|4620|522396|
Both partial author certificate counts match. Their reported GS nodes 288471 and 2426810 are author execution data, not independently replayed. The earlier timed-out interval [8192,16384) was explicitly not counted in the author certificate.

## Disclosed witness audit
Only one relaxed witness is reported in these two slices. Exact independent modular inverse arithmetic (extended Euclid, BigInt) confirms for k=1..6 that sum_r u_r r^(-k)+sum_pos(13q+r)^(-k)-sum_neg(13q+r)^(-k) is 0 mod 13^k. Negative index 9011 has q1 residues (2,5,12), q2 residues (4,12); positive index 74 is ((1,6),(2,3)). u=(-17,3,5,-9,14,-1,2,9,-2,-1,-1,-1). Vertical masses (622,1633), final signed masses (2890,3031), weighted squared norm 2109150, radius squared 3407885. All six residues vanish, norm is within radius, but both final masses exceed 2331. Both vertical sides fail 13-smoothness (e.g. 13+6=19 and 13+12=25 is smooth, but 13+5=18 smooth; negative 26+4=30 smooth, 26+12=38 contains 19). Positive 26+3=29 also fails. The relaxed witness is excluded from the original budget and maximal-prime domain.

## Reproducibility of count
For each sorted negative roster, compute t=cardinality({a,b,c}), s=cardinality({d,e}), add D(t,s) to its interval sum. When all five residues lie in their q-specific smooth sets, add the smooth analogue to the smooth interval sum. Verify the witness by weighing u_r with 13r-1, adding positive/negative parts to the two vertical masses, and taking the sum of squares of those weighted coordinates. No floating point is needed.

## Boundary and continuation
Author checkpoint revision 97 reports [0,12800) saved and remaining [12800,28392); do not overlap its ongoing direction. The new smooth roster bound can guide later independent audit. This is a scoped non-author certificate audit and exact combinatorial reduction, not a Native Review, completed Result, independent full lattice exclusion, or mother-objective closure. Existing q11113 full audit @8f43217f remains separate.
