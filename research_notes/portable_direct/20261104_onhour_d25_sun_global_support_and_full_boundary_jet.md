# D25 — Uniform support of the two Sun p³ defects and complete boundary z-jet transport
Date: 2026-11-04. TASK_RESEARCH author-side portable mathematical research. **UNREVIEWED / NOT_ADMITTED**; no native claim/run/Result.
Logical research provenance: chatgpt-research-onhour-enterprise-math-20260923 (not the maintenance lane).
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **frozen scientific pin** c47e13e4aba0e006366f989d6334d443f6333ae3.
Mother objective: Delta_p-R_p=0 (mod p), p=13,19 (mod 24); original weighted 216–2304 mod p³ cancellation and separate p=373 native H0/B0 benchmark remain open.

## Original arithmetic and theorem

For d=3 or 4, p>=5 prime, write
 c_k^{(d)} = prod_{h=0}^{k-1}[(dh+1)(dh+d-1)]/[d²(h+1)²], B_k=binom(2k,k),
 F_d(X)=sum_{k=0}^{p-1}c_k X^k, H_d(t)=sum_{k=0}^{p-1}B_k c_k t^k,
 E_d(X)=(F_d(X)²-H_d(X(1-X)))/p² (mod p).
This is exactly the previously used Sun polynomial defect for alpha=-1/d, with d=3 = original 216 and d=4 = original 2304. The existing Sun mod p² congruence makes coefficientwise division by p² valid. Work over Z_(p) until division, retain degree, sign, source, p-adic valuation and the distinction between evaluation and differentiation.

Let L be the first k with v_p(c_k)>=1, and R the first k with v_p(c_k)>=2 (k<p). Precisely:
| model | p class | L | R | degree bound K=2R-2 | # positive boundary degrees J=K-p |
|---|---|---|---|---|---|
| d=3 | p=3m+1 | m+1 | 2m+1 | 4m | m-1 |
| d=3 | p=3m+2 | m+1 | 2m+2 | 4m+2 | m |
| d=4 | p=4m+1 | m+1 | 3m+1 | 6m | 2m-1 |
| d=4 | p=4m+3 | m+1 | 3m+3 | 6m+4 | 2m+1 |

**THEOREM A (global support).** For every p>=5 and d in {3,4},
    E_d(X) belongs to X^(p+1) F_p[X] and deg E_d <= K_d=2R_d-2.
Thus the full p³ defect has **at most J_d original boundary coefficients**, not an unrestricted p-1-degree tail. This degree bound holds simultaneously for the value and the formal derivative observer.

**Proof.** For 1<=k<p, all denominators d²(k!)² are p-units, and all numerator factors dh+1, dh+d-1 lie below p². For d=3 the two hits are p and 2p; for d=4 they are p and 3p; the classes above identify the first and second k. Consequently v_p(c_k)=0 for k<L, 1 for L<=k<R, and 2 for R<=k<p.
For k<p, v_p(B_k)=floor(2k/p). Every k>=R is above p/2, hence v_p(B_k c_k)>=3; modulo p³ the composed H_d(X(1-X)) therefore has degree <=2(R-1).
For [X^n]F_d², if n>2(R-1), at least one pair member i>=R has valuation 2. The other index j=n-i >=2R-p >=L since p+L<=2R in every table row, so v_p(c_i c_j)>=3. Thus the F² tail also vanishes mod p³. For n<p, the exact infinite Clausen series identity already equates the truncated coefficients. At n=p the only omitted-tail residue is (B_p-2)c_p; Wolstenholme gives B_p=2 (mod p³). Hence E_d starts at X^(p+1). QED.

**THEOREM B (exact top-boundary identity).** Set K=2R-2, and I=1 when d=3 and p=3m+1, I=0 otherwise. Then
 [X^K]E_d == (c_(R-1)^2 + 2I c_(p-1)c_(L-1) - (-1)^(R-1) B_(R-1)c_(R-1))/p² (mod p).
All quotients are p-integral as a combined numerator. Proof: terms of H with k>=R vanish; k=R-1 contributes its maximal-degree (-1)^(R-1) term. For the square, the surviving pair is (R-1,R-1), plus the two corners (p-1,L-1) and (L-1,p-1) precisely when p+L=2R. Every other pair has valuation >=3. QED.
This is a full-source signed formula; 70 independent finite audits found the top coefficient nonzero in their stated range, while the theorem itself asserts the displayed value and the upper bound.

## THEOREM C: all surviving coefficients from a universal second-order z-jet

Fix d=3 or 4, C=(d-1)/d², and write the rational rising-factor series:
 c_j(C)=prod_{h=0}^{j-1}(h(h+1)+C)/(j!)²,
 U_i(z)=prod_{h=0}^{i-1}((z+h)(z+h+1)+C)/(z+h+1)²,
 V_i(z)=prod_{h=0}^{i-1}(2z+2h+1)(2z+2h+2)/(z+h+1)².
Define for any fixed j>=0
 Phi_j(z;C)=2 sum_{i=0}^j (-1)^(j-i) binom(z+i,j-i)V_i(z)U_i(z)
            -2 sum_{i=0}^j U_i(z)c_(j-i)(C),
 q_j(C)=[z²]Phi_j(z;C) in Q.
For every p>=5 and 0<=j<=J_d (thus j<=p-2), the following is an exact finite-field identity:
    [X^(p+j)]E_d(X) = C*q_j(C) (mod p).
In particular, with Q_(d,p)(X)=sum_{j=1}^{J_d}q_j(C)X^j reduced mod p,
    **E_d(X)=C X^p Q_(d,p)(X) in F_p[X].**
This supplies all coefficients, not only the first three. The previous source coefficients are recovered by
 q_1=2-6C,
 q_2=(12-22C-39C²)/8,
 q_3=(132-186C-505C²-197C³)/108.

**Proof.** The exact infinite Clausen identity, with finite truncations, gives for 0<=j<=p-2
 [X^(p+j)](F_d²-H_d(X(1-X)))
 = c_p (B_p * sum_i (-1)^(j-i)binom(p+i,j-i)V_i(p)U_i(p)
       -2 sum_i U_i(p)c_(j-i)).
Wolstenholme replaces B_p by 2 modulo p³. The universal p-adic binomial digit gives c_p=C (mod p): in the numerator of c_p the two factors divisible by p are p and (d-1)p, the remaining residues in each of the two progressions have product -1 modulo p, while d^(2p)((p-1)!)²=d² modulo p. All denominators of U_i,V_i,binom(z+i,j-i) at z=0 are p-units for j<=p-2.
Clausen at z=0 gives Phi_j(0;C)=0 exactly. Its first z-derivative also vanishes as a rational number, as follows without assuming a new identity: fix j; for infinitely many primes p>j+1, the Sun p² polynomial congruence and c_p=C !=0 (mod p) imply Phi_j(p;C)=0 (mod p²). Since Phi_j(0;C)=0 and the Taylor denominators are p-units outside a finite set, Phi'_j(0;C)=0 modulo infinitely many primes. A fixed rational number with this property is zero. Hence Phi_j(p;C)=p²[z²]Phi_j(z;C) (mod p³). Divide the exact tail identity by p² and reduce modulo p. Theorem A truncates the surviving polynomial at J_d. QED.

**THEOREM D (observer-order commutator).** On the D25 target classes p=13,19 (mod24), in F_p[s]/(s²-2) choose
 x_3=(2+s)/4, x_4=(3+2s)/6, with x_d^p=1-x_d.
Let C=C_d,Q=Q_(d,p). Formal differentiation of E before Frobenius evaluation gives
 E_d(x_d)=C(1-x_d)Q(x_d),
 E'_d(x_d)=C(1-x_d)Q'(x_d),
 and therefore
 E'_d(x_d) - (d/dX)[C(1-X)Q(X)]_(X=x_d)= C Q(x_d).
The last term is the exact correction lost by first replacing X^p with (1-X) and then differentiating. It is a source-labelled signed jet, not a positive-mass quotient.

## Independent exact execution and mother-objective connection

Node.js BigInt checker `d25_sun_global_support_full_jet_checker_20261104.mjs` uses original c_k modulo p³, independent full F² convolution, original H(X(1-X)) expansion, and separately an F_p[z]/(z³) calculation of every surviving coefficient. No floating-point arithmetic or injected theorem assumptions are used. It verifies Theorems A/B/C and value+derivative observer agreement for every applicable target p; 70 model-prime audits (all primes 5<=p<=151, plus p=373) passed.

| p | d | L | R | deg E (observed) | predicted K | E(x_d) | E'(x_d) |
|---|---|---|---|---|---|---|---|
|13|3|5|9|16|16|6|11+5s|
|13|4|4|10|18|18|1|12+4s|
|19|3|7|13|24|24|18|4+2s|
|19|4|5|15|28|28|17|5+7s|
|139|3|47|93|184|184|138|3+53s|
|139|4|35|105|208|208|122|50+73s|
|373|3|125|249|496|496|132|287+249s|
|373|4|94|280|558|558|137|371+268s|

At p=373, -E_3(x_3)+E_4(x_4)=5, and the previously pinned signed derivative combination (3s/4)E'_3-(s/6)E'_4=222+371s, reproducing the previous complete four-source witness. This round supplies an algebraic all-coefficient construction and a proof of finite support; it does **not** prove the universal weighted cancellation W_p-V_p=0 mod p³.

Research interface / BRC: carrier=(d, k or degree, valuation, signed amplitude, operation tag); algebraic alternative/superposition is maintained in Z/p³ and its two-dimensional quadratic extension; observer=(evaluation, derivative-before-Frobenius, eventual weighted Green transfer). Positive weighted BRC cannot project away the cancellation signs. This is a typed provenance-preserving BRC-style observer composition; no native-X6/Heartbeat physical bridge is claimed. The next scientific step is to combine the two reduced Q_(d,p) with the corresponding periods F_d into one certified signed differential transfer whose sum is zero for all p=13,19 mod24; 13,19,139,373 are exact regression witnesses. Direct Green/WZ cancellation remains an alternative route.

Inputs/authority: Sun, “Note on super congruences modulo p²” (2015), polynomial congruence; classical Clausen and Wolstenholme; previous author D25 Sun polynomial p³ defect and signed-jets notes. Scientific input pin above unchanged. Native p373 H0/B0 [X]U mod139129, module rank, actual semilinear Frobenius and independent replication tracked in #1559 remain NOT_EXECUTED. Native service 0.6.11 observed 2026-11-04 with research_authority_granted=false, control CODE_UPGRADE_AVAILABLE and full_snapshot_verified=false; original onhour-d25-20261104-1702-continuation-read failed SOURCE_TREE_SIZE_LIMIT, no reissue. Current research Source CLAIM/run/checkpoint/Result not established. GitHub author-side archive is not a native Result or a substitute for independent review.
