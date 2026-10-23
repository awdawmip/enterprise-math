# C271 / Research2 — 79-node auxiliary collision-seam theorem and exact 595-hull audit

**AUTHOR_EXACT_AUXILIARY / NOT ADMITTED / NO NATIVE CLAIM.** The target is only the C195/H168 79-node positive-rational interpolation auxiliary; it is not a native GF(2)-BRC phase/port theorem, a six-dimensional X6 Cell theorem, a physical singularity, an admitted Source Result, or an amendment of P000.

## Frozen provenance and no repeated progress

Read GLOBAL_KNOWLEDGE_V1 canonical main **7c1187e2493cbf4a087a013bf4cfd4580e7027b6**, including both normative entry files, P000, ACTIVE worldview, mathematical research policy and BRC method contract. Read Enterprise Math source main **ee3f360b93c18bb4d4681de656dc0428290d8876**, including the current portable research and research activity protocols. Account connector identity: awdawmip.

The preexisting *unmerged author-only* C270 R2 handoff at branch research/c270-r2-final-seven-fourshared-20261024 already reports 213 strict-negative witnesses, 150 positive entire pole-free two-box hull certificates, and 0 unresolved **among the historically eligible 363 hulls**. This result does **not** count either of the previously covered pairs (18,27) or (18,33) as new. It investigates the **other 232 pairs**, excluded from that full-pole-free-domain enumeration, and records a newly noticed C254 primitive-box boundary issue. Source author status and true independent Driver review remain distinct.

## Exact model

Take I={5,50,55,56}, J={0,...,78}\I, Q=2^128, H=2^166, Z=141421356237309504880/10^20, and A=6912*50000^2/17^2. The strictly increasing 79 original exact rational nodes u_0,...,u_78 are embedded in the sibling fully self-contained verifier. For j in J the fixed-branch positive integer is

B_j=floor( (Q*A/H) / ((2-u_j^2)*(3-u_j^2))^3 * PROD_(r != j) ((Z-u_r)/abs(u_j-u_r)) ) >0.

On the admissible pole-free domain define

F(v)= SUM_(j in J) B_j * PROD_(p in I) [ (Z-v_p)/(Z-u_p) * abs(u_j-u_p)/abs(u_j-v_p) ]
 + SUM_(k in I) [ (Q*A/H)/((2-v_k^2)*(3-v_k^2))^3
                  * PROD_(j in J) (Z-u_j)/abs(v_k-u_j)
                  * PROD_(p in I, p!=k) (Z-v_p)/abs(v_k-v_p) ].

The moving-branch collision v_55=v_56 makes F undefined. Always distinguish a theorem on the admissible punctured region from an assertion about a finite-valued function on the entire closed hull.

## Theorem A — all 595 unordered parent-box hulls

Start from the immutable C254 list of 35 basic rational four-coordinate boxes numbered 0,...,34. For i<j take the coordinatewise closed interval hull H(i,j). Put gamma(i,j)=upper_55(H(i,j)) - lower_56(H(i,j)).

Using rational arithmetic only, exhaustively comparing all C(35,2)=595 pairs gives:

| Hull category | Strict exact test | Count |
| --- | --- | ---: |
| Entire closed outer hull separated from the 55/56 collision pole | gamma<0 | **363** |
| Closed outer hull touches collision only along its boundary | gamma=0 | **124** |
| Closed outer hull crosses the collision surface in its interior | gamma>0 | **108** |
| Total | disjoint and exhaustive | **595** |

The 363 gamma<0 pairs coincide *item-for-item* with the C255 historically eligible pair registry. The 232 excluded pairs are exactly the 124+108 collision-hull cases, not an additional unresolved part of the 363. For gamma>=0 the 55/56 coordinate intervals overlap on [lower_56,upper_55]; therefore each such closed hull contains a point v55=v56=t with u55<t<u56, and there are admissible v55<v56 points approaching it. All comparisons and exact anchor checks are rerun by the sibling standard-library Python script.

**Additional audit caveat:** already at the C254 primitive-box level, box number **3** has upper55-lower56=**15/2626>0**, an interior collision, and box number **11** has upper55-lower56=**0**, a touching boundary. The other 33 primitive boxes are pole-free as full closed boxes. Thus it is false to assert without restriction that each original basic C254 closed rectangle is everywhere pole-free, even though a positive result on its genuinely admissible subset may remain valid. Audit any lower-bound proof which silently crosses the 55/56 pole.

## Theorem B — strictly positive collision residue for every admissible seam point

For fixed legal a=v5, b=v50 and u55<t<u56, define

q(t)= (Q*A/H) / ((2-t*t)*(3-t*t))^3
      * PROD_(j in J) ((Z-u_j)/abs(t-u_j))
      * PROD_(p in {5,50}) ((Z-v_p)/abs(t-v_p)),

with v5=a, v50=b. Assume the chosen a,b,t avoid all denominator zeros (satisfied for the 232 exact rational anchors below). Put v55=t-epsilon/2, v56=t+epsilon/2 for sufficiently small epsilon>0 inside the selected hull. Then

**lim_(epsilon -> 0+) epsilon*F(a,b,t-epsilon/2,t+epsilon/2) = R(a,b,t) = 2*(Z-t)*q(t) > 0.**

Proof: the two colliding moving branches satisfy the *exact* identities

M55 = q(v55)*(Z-v56)/(v56-v55),
M56 = q(v56)*(Z-v55)/(v56-v55).

Multiplying by epsilon=v56-v55 gives a limit of 2*(Z-t)*q(t). All 75 fixed branches and the moving k=5,50 branches are finite near the seam since t lies strictly between the original adjacent active nodes, so epsilon times their sum tends to zero. Every factor in R is strictly positive; no signed/phase cancellation is implied.

**Exact quantitative witness family:** for each of the 232 colliding outer hulls choose a,b at the respective first/second coordinate midpoints and t=(upper55+lower56)/2. Every chosen point is a valid rational seam anchor, with an admissible approach. Direct exact Fraction evaluation for all 232 anchors proves the strict, *anchor-specific* double inequality

**Q/4096 < R(a,b,t) < Q/2048**.

This bound is **not** asserted uniformly over all real a,b,t; the general positive-residue theorem is the analytic claim.

## Theorem C — strictly positive even quadratic correction

The **two colliding moving terms only** admit an even analytic normalization E(epsilon)=epsilon*(M55+M56), satisfying

E(epsilon)=R+C*epsilon^2+O(epsilon^4),

C=q(t)/4 * [ (Z-t)*(L'(t)^2+L''(t)) + 2*L'(t) ],

where L'=q'/q and

L'=6t/(2-t²)+6t/(3-t²) - SUM_(j in J)1/(t-u_j) - SUM_(p in {5,50})1/(t-v_p),
L''=6(2+t²)/(2-t²)^2+6(3+t²)/(3-t²)^2 + SUM_(j in J)1/(t-u_j)^2 + SUM_(p in {5,50})1/(t-v_p)^2.

**The coefficient C is strictly positive for every admissible t in (u55,u56), not merely for the 232 enumerated anchors.**

Proof: u54=7/9, u56=17/21 and fixed index 54 belongs to J. For t in (u55,u56),

0<t-u54<u56-u54=2/63<Z-u56<Z-t,

so the positive j=54 summand alone gives L''>1/(Z-t)^2. Therefore

(Z-t)*(L'^2+L'')+2L'
= (Z-t)*(L'+1/(Z-t))^2 + (Z-t)*L'' - 1/(Z-t) > 0.

Since q(t)>0, this establishes C>0. The absence of a linear epsilon term applies **only to E for the colliding two branches**; other regular F branches yield generally nonzero linear terms in epsilon*F. No global evenness of epsilon*F is claimed.

## Evidence, scope and next precise question

The branch's self-contained exact executable (standard-library Fraction; no network, checkout, third-party package or historical ZIP) embeds the original 79 nodes and all 35 original C254 boxes. It verifies the 595 exhaustive classifications, the separate C254 #3/#11 anomalies, all 232 positive rational residues and anchor bounds Q/4096<R<Q/2048, and the completed-square strict positive second-order coefficient. Expanded exact rational fractions and Python full-source audit are retained in the attached session ZIP and are distinct from a Driver review.

No new complete pole-free hull is added to the C270 author 363-pair frontier. In the 108 interior-crossing hulls, the open mathematical problem is to partition the *admissible* v55<v56 subdomain into legitimate pole-free rational cells and classify F>Q there, or exhibit an exact rational F<Q witness. Independently inspect C254 boxes #3 and #11 for sound denominator-order assumptions in their original certificates. Do not promote any auxiliary positive-mass result to native GF(2)-BRC signed/phase/port/branch/time fidelity without a typed correspondence proof.

Authority: native live dispatch attempt failed with TimeoutExpired; real task owner and CLAIM not established. GitHub source branch is author-level durable evidence, not canonical task-machine admission. No Drive fallback used to evade an authorization barrier.

Status: C271_AUTHOR_EXACT_SEAM_POLE / 595_PAIR_HULLS / 363_FULL_CLOSED_POLEFREE / 124_TOUCH / 108_CROSS / 232_STRICT_POSITIVE_POLE_RESIDUES / UNIVERSAL_QUADRATIC_CORRECTION_POSITIVE / GITHUB_AUTHOR_BRANCH / NO_NATIVE_CLAIM / NOT_ADMITTED.

Global-Knowledge-Sync: main@7c1187e / GLOBAL_KNOWLEDGE_V1
