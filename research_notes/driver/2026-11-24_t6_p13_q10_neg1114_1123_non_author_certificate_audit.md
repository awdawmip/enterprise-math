# T6 p13 q10 signed (3,7): non-author audit of negative q=(1,1,1,4) and (1,1,2,3)

Date 2026-11-24; Driver EM-DVR-DEBB5E, existing SID MCP-9b4714dc46b948afa4875a86c89c713c. Scoped mathematical evidence, shared project/author context disclosed, not a Native Review or Result admission. The original computations belong to the on-hour research lane; historical portable Activity RA-A468735D7C934B25C4B9614F retained. Its own latest checkpoint r91 reports a current identity relation unresolved; this note does not transfer attribution, adopt that identity, or represent a current CLAIM.

## Immutable reviewed inputs

- Frozen science awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca; per-side mass cap C=2331.
- [q1114 full author certificate](https://github.com/awdawmip/enterprise-math/blob/e04eb43e490af6b3018aec58be6b84df3157916f/research_checks/T6_P13_Q10_SPLIT3_7_NEG1114_FULL_AUTHOR_EXACT_CERT_20261124.json).
- [q1123 full author certificate](https://github.com/awdawmip/enterprise-math/blob/b9268835edc9c86a2a0829d1768826a8c54fb803/research_checks/T6_P13_Q10_SPLIT3_7_NEG1123_FULL_AUTHOR_EXACT_CERT_20261124.json), blob 967fb5188843179de5b1ff36dfe08162c762c92e.
- [integer GS replay](https://github.com/awdawmip/enterprise-math/blob/a466be736446891b423809b0ba23cb37ec123502/research_checks/T6_P13_Q10_SPLIT3_7_NEG1123_INTEGER_GS_REPLAY_20261124.py), blob 5272cc4046306db26444e9aeb308aed209983520.
- [prior scoped non-author audit](https://github.com/awdawmip/enterprise-math/blob/15134e7d2dabeeaa50c9b17b2fdd43889c4c9f13/research_notes/driver/2026-11-24_t6_p13_q10_signed_split_scoped_non_author_lattice_audit.md), whose conditional lattice and radius argument is reused.

## Independent combinatorial counting (no GS traversal)

An atom is named (q,r), 1<=r<=12. Positive q-total 3 has patterns (3), (1,2), (1,1,1), giving 12+144+binom(14,3)=520 rosters. A common named atom is excluded from the primitive (already common-atom-cancelled) domain; its lower-order remainder is a separate obligation. The literal roster is an over-inclusive domain if maximal-prime smoothness removes some atoms.

For negative q1114, the q1 multiset of length three has t=1,2,3 distinct residues in respectively 12, 132, 220 cases, and q4 has 12 choices. For each fixed negative roster, the disjoint positive count is 12+12(12-t)+binom(14-t,3). Therefore the exact primitive pair count is
12 * [12*(12+12*11+binom(13,3)) + 132*(12+12*10+binom(12,3)) + 220*(12+12*9+binom(11,3))] = 1,371,888.
Raw = 4,368*520=2,271,360; common-atom pairs=899,472.

For negative q1123, q1 multiset of length two has t=1,2 distinct residues in 12,66 cases; q2,q3 have 144 independent choices. Disjoint positive count for a fixed negative is 11+11(12-t)+binom(14-t,3).
Thus 144*[12*(11+11*11+binom(13,3))+66*(11+11*10+binom(12,3))]=3,963,168. Raw=11,232*520=5,840,640; common-atom pairs=1,877,472.

Both independently derived counts match the original certificates exactly. For q1123, checked all four recorded intervals [0,1024),[1024,3072),[3072,7168),[7168,11232) are contiguous and all aggregate statistics match their sums (8,110,173 recorded GS nodes, 5 recorded leaves, zero recorded budget-valid leaves). This is a certificate bookkeeping check, not a replay of those nodes.

## Exact arithmetic crosscheck of all eight disclosed sphere witnesses

Independent JavaScript BigInt modular inverse via extended Euclid and direct weighted mass/norm arithmetic; no author's GS solver invoked. For each supplied u, recomputed all six residues sum_r u_r r^(-k) + sum_pos(13q+r)^(-k) - sum_neg(13q+r)^(-k) mod 13^k, k=1..6. Every residue was exactly zero. We independently recomputed vertical masses c+/c-, complete side masses using w_r=13r-1, weighted squared Euclidean norm and radius=(2331-c+)^2+(2331-c-)^2.

| Pattern | (negative index,positive index) | vertical masses | final masses | norm^2 | radius^2 |
|---|---|---|---|---:|---:|
|1114|(299,427)|(816,1439)|(3543,3270)|2975994|3090889|
|1114|(406,411)|(764,1439)|(4708,2296)|3179591|3251153|
|1114|(1118,393)|(829,1374)|(1989,4930)|2737102|3171853|
|1123|(112,113)|(700,1400)|(1967,5391)|3323156|3526922|
|1123|(1396,326)|(764,1504)|(2677,4443)|2871782|3139418|
|1123|(4181,141)|(778,1426)|(3349,3050)|2785893|3230834|
|1123|(5648,161)|(608,1517)|(4469,2975)|3482679|3631325|
|1123|(6413,122)|(674,1504)|(2359,5084)|3423993|3429578|

All eight are genuine relaxed modular sphere witnesses, none satisfies both original side budgets. Particularly the last q1123 witness misses one cap by just 28 but the other by 2753: a one-sided budget test would be insufficient. The direct check recomputes the masses, not merely the certificate's boolean flag.

## Exact GS representation audit of q1123 source

Reusing the prior saturated-lattice and radius lemma, the integer GS recurrence is algebraically equivalent to the rational one as follows. Let a=c/Q be the affine basis coordinate vector, n integer, z=Q(a+n); let L_i be a common multiple of Q and Q times the denominators of mu[j,i]. Then B_ij=mu[j,i] L_i/Q is an integer and the scaled residual at index i is center+L_i*n_i, where center=c_i L_i/Q+sum_{j>i} z_j B_ij. Thus the exact squared norm contribution is D_i/L_i^2 times its square. Multiplication by the common positive denominator K gives the source's integer accumulated budget test. No floor rounding of rational GS coefficients is necessary; the source's int conversions are exact given those divisibilities. Since every D_i exceeds 2*C^2, the allowed interval for n_i is contained in the two nearest consecutive integers floor(-center/L_i), floor(-center/L_i)+1, including any boundary equality. Descending recursion covers the possible affine coordinates at each visited node. Python arbitrary-precision arithmetic avoids machine integer overflow. This is a source-logic audit conditional on the actual exact basis/GS data, model reductions and exhaustive execution; the independently recomputed witness residues and radius are additional concrete checks.

## Disposition and routing

SCOPED NON-AUTHOR CHECK PASSED for combinatorial counts, all disclosed witness arithmetic, q1123 aggregate intervals and algebraic integer-recurrence equivalence. Full independent lattice traversal (1,371,888 + 3,963,168 primitive pairs), q1114 per-slice replay, complete frozen-model reduction review, and Native Result admission remain unperformed here. The raw author certificates report no budget-valid primitive witness in these two named families; do not schedule duplicate author work. Keep the other lane's next q1222/prior-art check separate and owner-safe. Neither p13 q10 nor T6 mother objective is closed.