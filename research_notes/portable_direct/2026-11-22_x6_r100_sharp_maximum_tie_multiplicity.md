# X6 R100 — Sharp maximum tie multiplicity and its unique parameter witnesses

Date 2026-11-22 (Asia/Shanghai).  
Evidence: SYMBOLIC_AUTHOR_PROOF / EXACT_INTEGER_FINITE_PARAMETER_CROSSCHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.  
Science parent: R99 complete ten-direction tie core, research_notes/portable_direct/2026-11-22_x6_r99_ten_direction_universal_tie_core.md. Frozen P000 input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json.

## Statement and scope

Use exactly R98/R99's conditional four-channel positive-count BRC star-moment histogram observer, all real S,T >= 1, integer Port budget p >= 11, and unoriented nonzero integer differences. Let m_p(S,T) denote the *number of all globally minimizing directions* of the exact F objective. Then

\[
\boxed{\max_{S,T\ge1} m_p(S,T) =
\begin{cases}6,&11\le p\le16,\\7,&p\ge17.\end{cases}}
\]

The maximizing parameter locus is **exactly** {(5,23)} for 11 <= p <= 26, and exactly {(5,23),(11,11)} for p >= 27.

At (S,T)=(5,23), all six directions of Port <= 11 are tied:
(1,0,0), (4,-1,0), (5,-4,1), (6,-4,1), (9,-5,1), (10,-5,1).
A seventh, (15,-9,2), enters at p=17. At (11,11) there are seven ties precisely from p>=27, namely
(5,-4,1), (9,-5,1), (10,-5,1), (14,-9,2),
(15,-9,2), (19,-10,2), (24,-14,3).
In both cases the optimum equals 1/2.

## Universal analytic proof

By R99 every global minimizer is in the ten-direction core. Four core candidates have U=0, namely d=(6,-4,1), b=(9,-5,1), e=(15,-9,2), c=(24,-14,3); the other six have U=1. Since s=(10,-5,1) always has F=1/2, any optimum strictly below 1/2 has at most four ties. Therefore a tie multiplicity of at least five must occur at optimum 1/2.

By the R98 exact-value theorem, the optimum equals 1/2 precisely on the following domain:

- 11 <= p <= 26: T<=23 and (S<=5 or T<=11);
- p >= 27: T<=23, S<=11 and (S<=5 or T<=11).

All parameters are >=1 throughout. In these domains, a candidate in the ten-core is tied if and only if its F<=1/2, because the global minimum is 1/2. From its exact gap vector (U,V,H,K), this is equivalent to
U<=1, S>=2V-1, T>=2H-1, S+T>=2K.

For the ten directions, these conditions simplify, respectively, to:

| a | q | necessary and sufficient for F<=1/2 |
|---|---:|---|
| (1,0,0) | 1 | S>=5, T>=13 |
| (4,-1,0) | 4 | T>=23 |
| (5,-4,1) | 6 | S>=5, T>=11 |
| (6,-4,1) | 7 | T>=23 |
| (9,-5,1) | 10 | S>=5, T>=11 |
| (10,-5,1) | 11 | always |
| (14,-9,2) | 16 | S>=11 |
| (15,-9,2) | 17 | S>=5, T>=11, S+T>=18 |
| (19,-10,2) | 21 | S>=7, T>=11 |
| (24,-14,3) | 27 | S>=11 |

(The constraints omitted in each row follow automatically from S,T>=1 and the shown conditions.)

**Region S<=5.** The objective=1/2 region also requires T<=23. Monotonicity of each core score in S,T means the core tie set anywhere in this region is a subset of the tie set at (5,23), which has 6 directions available for p<=16 and 7 for p>=17. Equality in the respective *maximal cardinality* requires S=5 and T=23: if S<5 only s and possibly d/(4,-1,0) can tie, at most 3; if T<23, d and (4,-1,0) disappear and at most 5 remain. Thus the unique maximum in this region is (5,23).

**Region T<=11 and S>5.** If p>=27, the objective=1/2 condition includes S<=11. Every tie here is among the seven candidates
(5,-4,1), (9,-5,1), (10,-5,1), (14,-9,2), (15,-9,2), (19,-10,2), (24,-14,3).
At T<11 only the last two U=1 candidates with H=1, namely s,(14,-9,2), plus c may tie, at most 3. At T=11, all seven tie exactly when S=11; if S<11 both (14,-9,2) and c fail, so at most 5. Consequently the unique sevenfold tie in this region is (S,T)=(11,11), available only for p>=27.

If 11<=p<=26, the c direction is infeasible and the same T<=11 region has at most six tied candidates for any S (regardless of how large S becomes). For 11<=p<=16, at most four tie in this region, because e and (19,-10,2) are also infeasible; for 17<=p<=26 the count is at most six and cannot beat the seven at (5,23). This proves the stated maxima and uniqueness of the maximizing loci. QED.

## Evidence and boundary

Exact author-side integer crosscheck enumerated all pairs S,T in {1,...,40} and every p from 11 through 40; the asserted maximum and maximizing locations agreed in all 30 budgets. These are **finite confirmations only**. The proof for all real S,T>=1 and all p>=11 follows from R98's global exact-value theorem and R99's global exhaustive ten-direction tie carrier.

This is a conditional positive-count histogram BRC result. It does not constitute a native P000 six-axis Cell/Link/three-force/time-trajectory observer theorem. Neither the R99/R100 proofs nor the scientific publication is an authenticated CLAIM, Result, independent Review or Foundation promotion.

Next: describe closed equality-chamber geometry as reusable integer/rational constraints and investigate a typed observer-fiber conservation interface for the original native X6 objects.
