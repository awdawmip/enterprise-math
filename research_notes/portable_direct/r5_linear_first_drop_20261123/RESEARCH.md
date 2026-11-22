# R5 — First exact strict reduction of the degree-≥1 quasipolynomial period (threshold 69)

Date: 2026-11-23. Status: **AUTHOR_EXACT_PROOF / FINITE_FIELD_REPRODUCIBLE / NOT_REVIEWED**. Independent portable scalar-model continuation; **not** a native X6/BRC theorem, formal CLAIM, Result, or mathematical admission.

## Immutable scientific input and existing frontier

Frozen five-event scalar observer: \`awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15\`. Price domain \`p=214,...,314\` and five failure sets:
- S0 = 214..218;
- S1 = {214,216,217,218,219,220,221};
- S2 = {215,216,217,218,219,220,221};
- S3 = 223..290;
- S4 = 296..312.

For threshold m≥1 and total cost N, count nonnegative integer vectors a with total cost N meeting at least one failure event \`sum_{p in Si} a_p < m\`. Write \`F_m(q)=sum_N f_m(N)q^N=R_m(q)/D(q)\`, \`D(q)=prod_{p=214}^{314}(1-q^p)\`, and define \`M_m^(>=1)\` as the least simultaneous period of the quasipolynomial coefficient functions of \`N^j, j>=1\`. Previous proof and source verifier: \`enterprise-math@9194681d8b318cca415df3b178b30b876ea89fcd:research_notes/portable_direct/r5_linear_hasse_jet_m1_m30_20261123/\`.

Let \`Lambda=814202665467037976682352800\`, the lcm of all primitive orders d where the denominator zero multiplicity \`n_d=#{p in 214..314 : d|p}>=2\`. The earlier evidence establishes \`M_m^(>=1)=Lambda\` for 1≤m≤30. This note extends and refines that exact frozen problem.

## Main result

**Theorem 1 (first reduction and all 73 initial thresholds).** In the pinned scalar model,

\`\`\`
M_m^(>=1) = 814202665467037976682352800     for 1 <= m <= 68,
M_m^(>=1) =  11153461170781342146333600     for 69 <= m <= 73.
\`\`\`

Thus **m=69 is the first positive integer threshold at which the degree-≥1 coefficient period is strictly below Lambda**, and the factor lost at m=69 is precisely 73.

**Theorem 2 (infinite 73-cancellation family).** For every positive integer m with \`m mod 73 in {0,69,70,71,72}\`, the primitive-73 contribution has no pole of order ≥2, hence
\`M_m^(>=1) | Lambda/73\`.
No other prime-order combination with \`n_d>=2\` contains a factor 73: \`d=73\` is the sole such order. Theorem 2 is a global upper-bound family; equality at all such m is not asserted.

**Theorem 3 (infinite 54-cancellation family).** For every positive integer m with \`m mod 54 in {0,38,39,...,53}\`, \`R_m(zeta_54)=0\` for any primitive 54th root. Since \`n_54=2\`, the primitive-54 contribution drops out of the degree-≥1 coefficient functions. At thresholds 38..54, a primitive-27 contribution survives (witnessed at first Hasse jet in characteristic 109), so the full period remains Lambda there. The disappearance of one primitive order is not equivalent to dropping its prime power from the overall lcm.

## Structural proof of the two infinite cancellation families

**Root-of-unity consecutive-residue lemma.** Let zeta be primitive order d and E a set of k prices having distinct nonzero residues modulo d, where \`1<=k<d\`. Put \`h_j=h_j((zeta^p)_{p in E})\`. Then

\`\`\`
sum_{j>=0} h_j t^j = prod_{p in E} (1-t zeta^p)^(-1)
                   = U_E(t)/(1-t^d),
U_E(t) = prod_{r mod d, r not in E}(1-t zeta^r).
\`\`\`

\`deg U_E=d-k\` and residue r=0 belongs to the complement, hence \`U_E(1)=0\`. The coefficient sequence \`h_j\` is periodic with period d, vanishes at \`j=d-k+1,...,d-1\` modulo d, and its period sum is zero. Therefore
\`sum_{j=0}^{m-1}h_j=0\` whenever \`m mod d in {0,d-k+1,...,d-1}\`.
Multiplying by the nonzero factor \`prod_{p in E}(1-zeta^p)\` shows that the total-count failure numerator \`H_{E,m}(zeta)\` vanishes on these classes. This is a characteristic-zero exact identity for every positive m.

For d=54: all three overlapping sets S0,S1,S2 contain 216, divisible by 54, so every term of their joint inclusion–exclusion numerator \`A_m\` contains \`1-q^216\`, and \`A_m(zeta_54)=0\`. S3 contains 270, so \`B_m(zeta_54)=0\`. S4 has 17 distinct nonzero residues 26..42 mod 54; by the lemma \`C_m(zeta_54)=0\` for m mod 54=0 or 38..53. Since the three group unions are disjoint,
\`R_m = 1-(1-A_m)(1-B_m)(1-C_m)\`, yielding Theorem 3.

For d=73: inclusion–exclusion terms involving S1 or S2 contain the factor \`1-q^219\` and vanish at a primitive 73rd root. The remaining overlapping term equals the singleton failure numerator for S0. The respective nonzero residue sets are S0: 68..72 (k=5); S3: 4..71 (k=68); S4: 4..20 (k=17). The lemma gives zero respectively for threshold residues 69..73, 6..73, 57..73, where 73 represents residue 0. Their intersection is 69..73. Thus \`A=B=C=0\` and \`R_m(zeta_73)=0\`. The denominator has exactly two factors vanishing at order 73, from prices 219 and 292, and no other primitive order divisible by 73 has n_d>=2. Therefore 73 cannot divide the degree-≥1 coefficient period, proving Theorem 2.

## Finite-field proof of the exact initial ranges

Every primitive order d with \`n_d>=2\` yields a possible degree-≥1 component; no others can. Reuse the previous 18 lcm-covering orders
\`32,54,25,49,11,13,17,19,23,29,62,37,41,43,47,59,61,73\`,
whose lcm is Lambda. For each threshold and chosen order, find a prime p, a finite-field element z of **exact multiplicative order d**, and a Hasse coefficient \`[t^j]R_m(z(1+t)) != 0 mod p\` with \`0<=j<=n_d-2\`. This contradicts \`Phi_d^(n_d-1) | R_m\` over the integers and proves a pole of order at least two at a primitive dth root over characteristic zero, whence d divides the exact coefficient period.

The supplied C++17 verifier implements the correct three-overlap multivariate truncated DP and the correct complete-homogeneous total-count numerators for S3/S4. It checks finite-field jets j=0,1,2 (j bounded also by n_d-2). It searches primitive conjugates within the same prime when the initial one vanishes; it never mistakes a zero at one finite-field conjugate for a characteristic-zero cyclotomic zero.

Observed exact runs: 1,387 (73 thresholds x 19 orders including backup 27) root/jet rows. The only rows without a witness at their initial prime **and all of its primitive conjugates** are (m,54) for m=38..54 (17 rows) and (m,73) for m=69..73 (5 rows). These zero rows have independent characteristic-zero explanations above; finite-field silence alone was not used as proof of zero. The 1..30 subset independently reproduces the archived 540 witnesses (507 at jet 0, 32 at jet 1, 1 at jet 2), including the exceptional (m,d,p,z,j,residue)=(20,11,23,4,2,11).

To prove Theorem 1:
- m=1..37 and m=55..68: all 18 original orders have successful finite-field witnesses, so \`Lambda|M_m\`.
- m=38..54: replace the vanished order 54 by order 27. Every remaining original order (including 73) and the backup 27 has a successful witness, and \`lcm(27,32,25,49,11,13,17,19,23,29,62,37,41,43,47,59,61,73)=Lambda\`.
- m=69..73: all 17 original orders other than 73 have successful witnesses, and their lcm is exactly \`Lambda/73\`. Theorem 2 supplies the matching upper bound.
- The denominator pole bound \`M_m|Lambda\` is valid for every m. Combining bounds gives both asserted strict equalities.

Verification totals, using the required lcm-covering witnesses: m=1..30: 540; 31..37: 126; 38..54: 306 (including the d=27 backup); 55..68: 252; 69..73: 85. All required witnesses pass. The exact integer \`Z[x]/(x^18-x^9+1)\` auxiliary check independently confirms the order-54 zero interval 38..54 and nonzero 37/55; this is not needed for the algebraic proof.

## Reproduction, provenance and boundaries

Compile \`VERIFY_FIRST_DROP.cpp\` with \`g++ -O3 -std=c++17\`; run \`./verify_first_drop 1 73 > witness.csv\`. The standalone output columns are m,d,n_d,prime,root,first_nonzero_jet,jet_residue,root_coverage. It includes the backup d=27 to make 38..54 independently inspectable. Validate primitive-root exact orders, successful jet range, failure-pattern enumeration, and the lcms before using a finite-field row as proof. Independent historic Python reference: \`enterprise-math@9194681d8b318cca415df3b178b30b876ea89fcd:research_notes/portable_direct/r5_linear_hasse_jet_m1_m30_20261123/VERIFY_R5_M1_M30_JET_PERIOD.py\`.

All checks are exact modular/integer computations, not floating point. The characteristic-zero upper-bound and infinite-family zeros are algebraic. No new claims are made about the native six-axis X6 observer, P000, BRC, or the discrete-world ontology without a proven observer-preserving transfer. Status stays \`NOT_REVIEWED\`; the first-73 classification is an author-side exact result, not a formal accepted Result.

**Next:** study whether any further primitive orders drop for m>73, and which canceled orders can be replaced by divisors of those orders. A useful tool is the root-of-unity complement lemma above applied to the other event blocks and the complete pole-order jets. Retain the original frozen source, author contributions, and independently established activity history. Do not launch a competing formal CLAIM or rewrite a predecessor proof.
