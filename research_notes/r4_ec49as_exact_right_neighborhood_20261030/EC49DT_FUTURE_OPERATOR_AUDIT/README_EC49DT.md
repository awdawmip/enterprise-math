# EC49DT — native returning-future factorization and a minimal grammar-extension residual

2026-11-02. Status: AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_CHECKS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Frozen scientific inputs and authority

Continue EC49DS at PR #1730 commit 0add7c0870c7c8b905684eedd4d6c26fda694459. Frozen science: GLOBAL_KNOWLEDGE_V1 main 773d538180bfb49e24cffeb35c3ee75eb0628e2e; Enterprise Math main fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Current applicable normative reads: global main ee8c1042ad173c4a767bbf96bdf523902dca6274; EM main a4504e17ac306f4956d1c976e2516d553f720ecc. P000 and ACTIVE worldview are unchanged.

A historical word is a genuinely ordered native six-axis signed path of length n and displacement D=-2E1. The operations a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3) are finite native step words. Future words are distinguished (not pooled), have length h in operations, and are accepted only if the full six-dimensional displacement returns. An observer column records a final A/B joint bucket for one future word separately in the positive x-product BRC channel, positive y-product BRC channel, or unweighted count. A is consecutive (+E1,+E2), B is consecutive (+E2,+E1); cross-boundary events count. All x_i,y_i are arbitrary strictly positive real numbers; negative steps have weight one.

For a history define its A/B flags and last-step port L=1 for +E1, L=2 for +E2, L=0 otherwise. Let z=(z00,z01,z10,z11,pA,pB), where zij indicates the old joint flags, pA=1[A=0,L=1] and pB=1[B=0,L=2]. For a history collection H let H6 have rows (Wx*z,Wy*z,z), and H5 analogously with u=(1,A,B,pA,pB).

## Theorem 1: exact six-feature operator audit (all horizons, all positive weights)

For every finite history collection and all x,y>0, the actual full returning-future observer O_h satisfies rank(O_h)=rank(H5) for every even h>=2, rank(O_h)=rank(H6) for every odd h>=3, and rank(O_1..h)=rank(H6) for every cumulative horizon h>=2. At h=1, e preserves the four old joint labels.

Proof. Every basic operation ends in a negative primitive step, so no adjacent-positive A/B is born between two operations. Only c has internal A; only d has internal B; e/a/b have neither. The first step is +E1 for c, +E2 for d, +E3 for e and negative for a,b. Thus with C=1[future includes c], F=1[future includes d] and s the first primitive future step,

A'=A OR C OR (L=1 AND s=+E2),
B'=B OR F OR (L=2 AND s=+E1).

If C=F=0, s cannot be +E1/+E2 and the old flags remain. If C=1,F=0 then A'=1, B'=B+1[s=+E1]*pB. If C=0,F=1 then B'=1, A'=A+1[s=+E2]*pA. If both occur then A'=B'=1. Consequently every output label indicator is a linear combination of six coordinates z. The return equation is exactly #b=0 and #e=#a+1; hence h=2#a+1+#c+#d. For even h, #c+#d is positive odd, so every returned future already contains internal A or B, and all its output columns lie in span(1,A,B,pA,pB).

At h=2 the returned words are ce,ec,de,ed. Their four-label bucket sums yield 1, the (1,1) bucket for ec gives B, the same bucket for ed gives A, while (ce,11)-(ec,11)=pB and (de,11)-(ed,11)=pA. Thus they span precisely the five features. At h=3, the four (A,B) buckets of aee give z00,z01,z10,z11; (cce,11)-(ecc,11)=pB; (dde,11)-(edd,11)=pA. Thus h3 spans six features. Appending (ae)^k after any return word keeps full return displacement and preserves every A/B label; the multipliers are (x3*x1^2)^k and (y3*y1^2)^k, nonzero. Hence each base h2/h3 span embeds into all same-parity horizons, while the preceding feature bounds cap them. The positive-product factor of an arbitrary future word is (x1*x2)^(#c+#d)*(x3*x1^2)^(#e), and analogously for y; separate future-word columns are scaled by nonzero values. This proves the exact weighted rank equalities. QED.

## Theorem 2: one added neutral native future raises minimal state size from six to seven

Define a DIFFERENT allowed future alphabet by additionally permitting f=(+E1,-E1), which has zero native displacement and contains no internal A/B. Set q=1[A=0,B=0,L=2], z7=(z00,z01,z10,z11,pA,pB,q). For this extended future language, the universal 12-state formal transfer rank is four at h=1, seven at EVERY h>=2, and seven for cumulative h=1..h, h>=2. The seventh feature is necessary.

Proof. The only extra case not already covered by z is a word beginning f with neither c nor d. Then final label indicators in 00,01,10,11 order are (z00-q,z01+q,z10-(pB-q),z11+(pB-q)). All other extended futures still factor through z. At h=2, ef reproduces the four old labels, ce/ec and de/ed recover pB and pA, and (ef,00)-(fe,00)=q. These seven columns are linearly independent on the 12 formal states. At h=3, eff reproduces four labels, cce/ecc and dde/edd recover the ports, and (eff,00)-(ffe,00)=q. Appending (ae)^k proves the same seven-dimensional rank at all even h>=2 and odd h>=3. QED.

The difference is observable with TWO POSITIVE POPULATIONS of genuine native histories, not merely a signed algebraic trick. Fix n=10, D=-2E1 and positive counts (1,3,0,0,0,0). The executed report contains four actual histories with states (0,0,2),(0,0,0),(1,0,2),(1,0,0). Define P+=(history 002)+(history 100) and P-=(history 000)+(history 102). All six z aggregates are identical for P+ and P-; the positive-counts also match, so both BRC product channels and unweighted counts coincide for every original returned future. For the newly permitted returning word fe the final 00 bucket has zero mass for P+ and unit count for P- (strictly positive BRC gap). This is a concrete observer-language sensitivity certificate.

## Theorem 3: all-parameter necessary/sufficient 21-rank criterion in length 10

Let C11 consist of (1,3),(2,2),(3,1) supported on core axes 1/2 and (1,2,e_j),(2,1,e_j) for j=3,4,5,6. For p∈C11 write X(p)=product x_i^p_i and Y(p)=product y_i^p_i. Let G_C be the 11x3 matrix whose rows are (X(p),Y(p),1). For every strictly positive x,y and original native historical n=10,D=-2E1,

rank O_extended(h)=21 for any/every h>=2  IFF  rank G_C=3.

Proof. The executed certificate supplies ELEVEN groups of SEVEN actual 10-step native paths, each group with a single p in C11, full X6 displacement -2E1 and an exact 7x7 z7 feature determinant +1. Thus three linearly independent G_C rows yield 21 histories with a nonzero 21x21 weighted-observer minor equal, up to ordering, to (det G_3)^7 times the three nonzero seven-feature minors. Necessity: every history with both A and B must contain positive 121 or 212; with only four positive steps, p must lie in C11. If rank G_C<3, a nonzero linear functional supported on the z11 feature across the three instruments annihilates every row, preventing rank21. Theorem 2 translates the historical full rank to every extended h>=2. At any original history length n<=8, there are at most three positive steps; a path containing both A and B has at most two possible core positive-count patterns, so its z11 instrument rank cannot reach three. Therefore n=10 is the minimum original even history length at which the 21-dimensional full rank can occur. QED.

Example x=(2,3,1,2,3,4), y=(5,7,3,5,7,9): G_3 determinant 420, native 21x21 determinant 2305393332480000000=420^7.

## Reproducibility and status

VERIFY_EC49DT.js is the exact self-contained JavaScript verifier executed for this report; run node VERIFY_EC49DT.js. It generates and checks all 77 original native histories, eleven 7x7 determinants, the exact 21x21 BigInt Bareiss determinant, and the positive-population collision. It checks original horizons 1..7, all 4,081 returning words, with transfer ranks [4,5,6,5,6,5,6], and extended horizons 1..5, all 866 returning words, with ranks [4,7,7,7,7]. The proof of all infinite horizons is analytic, not an inference from finite tests. EC49DT_EXECUTED.json contains all 77 explicit native paths. The original six-feature theorem is tied to the declared a/b/c/d/e operation alphabet and separate future-word outputs; the added f is an explicitly hypothetical diagnostic.

The native MCP status v0.6.11 read back research_authority_granted=false; live owner query returned CONTROL_QUOTA. There is no authenticated RA, CLAIM, Result, independent Driver review or Foundation admission. Store as author-side portable research in Draft PR #1730. No P000/worldview change.

Next question: EC49DU — add other independent zero-return X6 native operations beginning +E1 or +E2, determine the resulting minimal future-observer feature dimension on reachable native fibers, and examine the defective G_C parameter strata.