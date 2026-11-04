# PREFIX-487 — Exact N-bearing source-mask generating functions and Presburger rationality

Date: 2026-11-04 (Asia/Shanghai). Class: author-side mathematical research; not independently reviewed, admitted, or a formal Source Result.

## Authority and exact model

Continuation of PREFIX-486 at enterprise-math@83a08de960769517241eb947e7523ef216914811. The task's scientific-source pin is f42f2906d77f24085c123f3ccfe9667d41caa96d; it is not advanced by this note. Research is within the restricted ordered-path observer embedded in native signed X6: ten freely legal signed ordinary steps a/A through e/E plus sixth-axis special positive x. The special x is legal only initially or immediately following a completed KMP gate word w and resets the gate. The gate is w=aab or w=aba for the explicit formulas.

At fixed path length n, retain the base BRC-KMP observer O=(s,y_a,y_b,y_c,y_d,y_e,V,W,q), where s counts x, y_i=u_i-v_i, p_i=min(u_i,v_i), S=sum_i p_i=(n-s-sum_i |y_i|)/2, V=p_b+2p_d+p_e, W=p_c+p_e, and q is terminal KMP state. The source tag is N until any b/B/c/C appears, B if the first such letter is b/B, C if the first is c/C. Let a fiber's source mask be its subset of {N,B,C} realized by at least one legal ordered path. All statements concern existence of realizations, not path multiplicity, physical time, signed amplitudes, or another source query. The full branch histories remain available in the underlying path population.

## Theorem 1 — exact classification of all N-bearing fibers

An N path uses only a/A,d/D,e/E (possibly preceded by one initial x). Let P=p_a, D=p_d, E=p_e for its ordinary counts and let U=u_a. Its observed tuple determines these six ordinary direction counts uniquely:
p_e=W, p_d=(V-W)/2, p_a=S-p_d-p_e, with the signed displacements y_a,y_d,y_e. Thus a distinct N count vector represents a distinct base observer fiber.

The reachable N terminal KMP states are:
- aab: q=0 iff no ordinary letter or at least one non-a ordinary letter exists; q=1 iff U>=1 and the ordinary word is not pure a^m with m>=2; q=2 iff U>=2.
- aba: q=0 under the same condition; q=1 iff U>=1. No N realization reaches q=2 for aba.

For any N-bearing base fiber with an allowed terminal q, the exact source mask is
- {N,B,C} iff P>=1, E>=1, and U>=q+1;
- {N,B} iff P>=1, D>=1, E=0, and U>=q+1;
- {N} in all remaining cases.

Proof. Take an alternative realization with the same observer, and set h=p'_c, t=p'_d-D. Equality of S,V,W forces
p'_e=E-h, p'_b=h-2t, p'_a=P+t-h.
The signed displacements stay equal, hence y_b=y_c=0 and any occurrence of b/B or c/C requires the corresponding cancellation pair p'_b>0 or p'_c>0. For B, p'_b>=1 implies t-h<=-1, so p'_a<=P-1 and U>=q+1 (q final positive a letters are required for q>=1). If h=0, then t<=-1 and D>=1; if h>=1, then E>=1. For C, h>=1, giving E>=1 and p'_a<=P-1. These prove the necessary conditions.

If E>=1, P>=1 and U>=q+1, replace (P,0,0,D,E) by (P-1,1,1,D,E-1), preserving S,V,W and every y; order the b/B and c/C pairs with b first or c first and reserve the required terminal suffix (q=0: uppercase non-prefix letter; q=1: uppercase non-prefix letter then a; aab q=2: uppercase non-prefix letter then aa). These realize B and C with the same q. If E=0 and D>=1, replace by (P-1,2,0,D-1,0), which preserves S,V,W; order the two b/B pairs first and reserve the same suffix. This realizes B but not C because W=0 forces p'_c=0 for every realization. The source-mask classification follows, including nonexistence of an N,C-only mask.

## Theorem 2 — four explicit rational generating functions

Let R_N,w(n) be the number of base fibers supporting N, R_NB,w(n) the number supporting exactly {N,B}, T_w(n) the number supporting {N,B,C}, and R_Nonly,w(n) the number supporting exactly {N}. Put F(z)=sum_{n>=0} F(n) z^n, and a binomial with upper argument less than lower argument equal to zero.

For gate aab:
R_N,aab(z)=(1+z)[(1+z+z^2)/(1-z)^6-(z+z^2)/(1-z)].
R_NB,aab(z)=z^4(1+z)^2(1+z+z^2)/(1-z)^5.

For gate aba:
R_N,aba(z)=(1+z)[(1+z)/(1-z)^6-z/(1-z)].
R_NB,aba(z)=z^4(1+z)^3/(1-z)^5.

For either gate, the exact N-only generating function is
R_Nonly,w(z)=R_N,w(z)-R_NB,w(z)-T_w(z),
where PREFIX-486 established
T_aab(z)=z^4(1+z)(1+z+z^2)/(1-z)^6,
T_aba(z)=z^4(1+z)^2/(1-z)^6.

Proof. A nonnegative six-tuple (u_a,v_a,u_d,v_d,u_e,v_e) of sum m has generating function (1-z)^(-6). The above terminal suffix tests give, for aab, q=0 series (1-z)^(-6)-z/(1-z), q=1 series z(1-z)^(-6)-z^2/(1-z), q=2 series z^2(1-z)^(-6). For aba only q=0 and q=1 occur, with respective series (1-z)^(-6)-z/(1-z), z(1-z)^(-6). Including the optional initial x multiplies by (1+z).

For exactly {N,B}, the classification reduces to U>=q+1, v_a>=1, u_d>=1, v_d>=1, and min(u_e,v_e)=0, with allowed q. Its ordinary-length generating function is z^(q+4)(1+z)/(1-z)^5: four independent bounded-below counts contribute z^(q+4)/(1-z)^4, while the e/E pair on the two coordinate rays contributes (1+z)/(1-z). Sum q=0,1,2 for aab or q=0,1 for aba, and multiply by (1+z) for optional x. The exact mask partition supplies N-only by subtraction. All formulas hold for every n>=0.

## Theorem 3 — general exact-mask rationality in this fixed-dimensional BRC observer family

Fix any finite gate word w on the ordinary signed alphabet and any finite-state terminal source automaton with finitely many outputs. For each exact support mask A of those outputs, the set of (n,s,y,V,W,q) whose legal paths realize precisely A is effectively Presburger-definable. The count of distinct such observer tuples at each n has a rational univariate generating function and is eventually quasi-polynomial in n.

Proof. The legal ordered-path language with gate word w, x reset, terminal KMP state q and a specified terminal source output is regular (product of finite automata). Its Parikh image in the eleven letter counts is effectively semilinear. The coordinate map from raw signed counts to (n,s,y,V,W,q) is a finite piecewise-linear integer map: each p_i=min(u_i,v_i) is Presburger-definable. Existence of a path with a specified output and given observer tuple is therefore a Presburger formula with existentially quantified Parikh counts. Exact support masks are formed by finite Boolean combinations of these formulas. For each fixed n there are finitely many observer tuples, as all count coordinates are bounded by n. Presburger counting and its rational-generating-function characterization thus apply to this one-parameter counting function. This is an effective existence and constructive-reduction result; calculating a closed form for B-only/C-only/BC-only masks and the growth period remain subsequent explicit tasks.

External supporting results: Anthony Widjaja To, Parikh Images of Regular Languages (2010), https://arxiv.org/abs/1002.1464; Kevin Woods, Presburger Arithmetic, Rational Generating Functions, and Quasi-Polynomials, Journal of Symbolic Logic 80(2), 2015, pp. 433-449, DOI 10.1017/jsl.2015.4. Theorems 1-2 above are direct derivations in the present observer, not quotations from those works.

## Executed certificate, evidence scope, next unit

The companion Node.js certificate propagates sets of all reachable BRC-KMP-source states for w=aab and aba, n=0..9. It independently checks all three exact N-bearing mask formulas at every length; for n=0..4 it also exhaustively enumerates ordered paths and compares every observer mask. At n=8, aab has N=4043, exactly {N}=3506, exactly {N,B}=251, exactly {N,B,C}=286; aba has N=3331, {N}=2847, {N,B}=225, {N,B,C}=259. The logged final marker is ALL_CHECKS_PASS. The infinite-length claims are analytic and rest on the proofs and cited general results; computations confirm the stated finite window.

Next PREFIX-488: obtain B-only, C-only and BC-only mask formulas, calculate their periods and leading terms, and build a finite automata-to-Presburger normalization prototype with a declared complexity/bit-cost account. Preserve full source history for other queries. Native Source registration/CLAIM remains pending actual authenticated service capability. The service currently reports SOURCE_TREE_SIZE_LIMIT at session_start and CONTROL_QUOTA at task listing; an author-side GitHub research note does not grant task ownership or mathematical admission.
