# PREFIX-1116 — convergent-lattice coordinates and convex interval sieve

Date 2026-11-27 Asia/Shanghai. Continuation of EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / NOT_REVIEWED.

## Frozen source and scope

Parent PREFIX-1115: ddf71410e78ccd4f8eee59e8d96d8bab94ce03e5:research_notes/portable_direct/2026-11-27_r6_prefix1115_signed_jet_threshold_order.md. P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; joint relation observer preservation and native X6 time unchanged. Same Stage46 X6 chart O, incoming -e1, signed reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. Preserve native cell, port, signed phase and ordered branch multiplicity. This work is a lossless auxiliary arithmetic coordinate change on the integer candidate band of the inherited BRC observation; not new native propagation, not a replacement for the joint carrier or a native spatial plane.

Assume PREFIX-1107 strict sign rule for E=400000, m>=10^8, E/m^2 <= |j-f(m)| <= 2 and PREFIX-1097 global last-negative monotonicity, where f(m)=rho*m+c+d/m. Reuse the exact coefficient boxes of PREFIX-1115 (8000 and 8400). The latter original command produced complete JSON but exit was unconfirmed; the parent finite verifier passed. No new anchor computation or independent mathematical review here. All new finite claims conditional on these inherited analytic/anchor premises.

## 1. Exact convergent-lattice change of coordinates

Let R=[rho_l,rho_u], C=[c_l,c_u], T=[d_l,d_u], d_l>0. On integer [L,H], L>=10^8, define lower/upper
 B_-(m)=rho_l*m+c_l+d_l/m-E/m^2,
 B_+(m)=rho_u*m+c_u+d_u/m+E/m^2.
The candidate set consists exactly of all (m,j) with B_-<=j<=B_+.

For any coprime integers p,q, q>0, use h=q*j-p*m. This is an exact integer-coordinate transform: m satisfies m == -p^{-1}h (mod q), and j=(p*m+h)/q. For q=1 the residue is 0. Neither sign nor original m,j is lost. In particular all possible h lie in the explicitly computable integer interval [ceil(A),floor(B)], where
 A=q*(min((rho_l-p/q)*L,(rho_l-p/q)*H)+c_l+d_l/H-E/L^2),
 B=q*(max((rho_u-p/q)*L,(rho_u-p/q)*H)+c_u+d_u/L+E/L^2).
These inequalities follow termwise using positive m,d and E. Endpoints are closed, exact, and no candidate can be missed.

Fix h in that interval and r=(-p^{-1}h) mod q. Write m=r+qn with ceil((L-r)/q)<=n<=floor((H-r)/q). Define
 u_-(m)=(rho_l-p/q)*m+c_l-h/q+d_l/m-E/m^2,
 u_+(m)=(rho_u-p/q)*m+c_u-h/q+d_u/m+E/m^2.
The candidate condition is precisely u_-(m)<=0<=u_+(m). Under d_l*L>3E, the second derivatives are
 u_-''=2d_l/m^3-6E/m^4>0,
 u_+''=2d_u/m^3+6E/m^4>0.
Both sequences indexed by n are convex because restriction to equally spaced points preserves nondecreasing first differences. Find a discrete minimum by binary search on f(n+1)-f(n)>=0; then binary search the first and last nonpositive index on the two monotone branches. Empty sequences and singleton intervals are covered. The closed sublevel of u_- is one integer interval A_h; the strict negative sublevel of u_+ within A_h is one interval B_h. The exact retained set is A_h minus B_h: at most two integer intervals. Strict inequality for the removed region retains all exact equalities. Transforming back produces at most two arithmetic progressions of candidate pairs on each line. This proves exact completeness and soundness of the compressed representation, with no assumption that all lines actually contain points.

## 2. Precision/resource theorem

Let x=(rho_l+rho_u)/2 and w=(rho_u-rho_l)/2. In [L,H] with H<2L choose the last ordinary continued-fraction convergent p/q of the rational x with q<=L. If x is reached exactly take that convergent. Otherwise next denominator Q>L and |x-p/q|<1/(q Q) (ordinary consecutive convergents identity, or the exact continued fraction recurrence). The real enclosing h-range width is at most
 q*|x-p/q|*(H-L)+2q*w*H+q*(c_u-c_l+d_u/L-d_l/H+2E/L^2).
The first term is <1, or zero for exact rational termination. This bound is obtained by writing rho_l=x-w, rho_u=x+w and bounding min/max of the linear terms by the x-p/q term plus wH. Thus the number J of enumerated integer h is at most 1+floor(B-A) when nonempty; in particular J=O(1+w L^2+L width(C)+d_u+E/L) for positive d_l, with universal constants. Each nonempty line has at most 1+floor((H-L)/q) lattice positions; three monotone searches per sublevel, at most two sublevels per line, require O(1+log(1+(H-L)/q)) exact rational evaluations, plus Euclidean preprocessing for the convergent/inverse and integer arithmetic bit costs. Output at most 2J progressions, and expanding them costs actual candidate count. No claim of uniform bit complexity independent of precision, and no uniform bound on number of true near-integers from fixed finite boxes. If w=O(L^-2) and width(C)=O(L^-1), d_u bounded, then only O(1) lines per doubling window, even for an arbitrarily large partial quotient and very long progressions. This is a useful separation of the precision supply problem from exact candidate enumeration.

## 3. Actual computation and independent cross-check against previous sieve

Input archive PREFIX-1115-execution-evidence.zip: all 22 manifest entries checked, input root_8000_result.json SHA256 11e9c6b31913cce05749d258fbd20eaabdfc0be5d7de742bae2ea41c02b06bbd, root_8400_result.json 5f99a39ec9e70b5c853197d865cb15486d8075f19170acc8dd5da1ed4adcd332, root_8000_window_result.json c63652a3c38287c58d45277d54358a96c4b988e0dafd441a314ca510abe71abc. Exact endpoints are also in parent paper section 3, denominator 10^85. The new Python Fraction code executed twice normally, seed 1116, 500 small-window comparisons against direct enumeration including negative rho and exact rational inputs, all passed. The first 90 windows [10^8,123794003928538027489912422400000000) using 8000 box reproduce all 22 previous candidate pairs exactly, 266 lines and 1399 function evaluations. Using 8400 box directly gives zero candidates in same 90 windows, 237 lines and 1340 evaluations. Parent 8000 floor-sum tree visited 5170 nodes; these are different operation types, not an end-to-end speedup ratio.

The previously observed three-line property is now explained constructively. p=143902715590973366560782416004716377, q=6711868895915652573356270627256609 are a convergent of the 8000 midpoint (checked exactly). Over the interval from first to last prior candidate m, six h values are enumerated and exactly three nonempty progressions result (149 exact function evaluations):
 h=665421464266317843049826956490052992, m=30614983299972440557741525569009913 .. 91021803363213313717947961214319394, step q, 10 pairs;
 h=665421464266317843049826956490052993, m=71262205932283536391237667500006467 .. 118245288203693104404731561890802730, step q, 8 pairs;
 h=665421464266317843049826956490052994, m=98485690772763327078021268176489803 .. 118621297460510284798090080058259630, step q, 4 pairs.
Expanding and sorting exactly matches the earlier list. The new method obtains them as progressions, rather than inferring lines after enumerating points.

## 4. New window

Reuse 8400 box unchanged and extend seven doublings beyond parent endpoint to exclusive 15845632502852867518708790067200000000. Total 23 possible h lines, 136 exact function evaluations, seven candidate pairs; maximum eight lines per window. Counts by doubling: 0,0,0,0,0,1,6.
Full new candidate list:
7757516269187633236376884843293826946 166321433670519293441295926909297619632
8029375108335613962851362331891203406 172150097164618579774322299890250148613
8301233947483594689325839820488579866 177978760658717866107348672871202677594
13405393052718353258393988631858509325 287412119301738801320114923022866308862
13677251891866333984868466120455885785 293240782795838087653141296003818837843
13949110731014314711342943609053262245 299069446289937373986167668984771366824
14220969570162295437817421097650638705 304898109784036660319194041965723895805

All other m in [10^8,15845632502852867518708790067200000000) retain the strict sign certificate and uniform floor formula with the same 8400 midpoint integers as PREFIX-1115 (they lie in the boxes). Band width <1 on this range by endpoint bound, so each candidate scale has exactly one possible undecided integer. First undecided m=7757516269187633236376884843293826946, continuous no-candidate count 7757516269187633236376884843193826946. Cumulative covered count excluding seven is 15845632502852867518708790067099999993. These are conditional finite certificates, not exact-zero exclusions for the seven. No new native CT or anchor computation.

## 5. Reproduction and next question

Actual code at 2ec540692bf1ba695b60416903db654f797f3e67:research_notes/portable_direct/2026-11-27_r6_prefix1116_convergent_lattice.py; Git blob e507a3ac0a53a81236a43e1de1924c00146e3a5a matches executed file; SHA256 5cd060ab595053b2453a8c982e6765d33d8a70a3ac59730cd143bf024a4e9247. Run python prefix1116_lattice.py alongside the three parent JSON files. Output prefix1116_result.json SHA256 b8629530f3cc11912243f13414c027d8945c6055c5966d098f3690b4fc053014. Local evidence archive PREFIX-1116-execution-evidence.zip contains actual code, exact input/output JSONs, log and SHA256 manifest, ZIP integrity checked. The 8000 input list is also reconstructible from the three exact progressions above and the prior certified endpoints. No other hidden numeric inputs.

Next: use common slope threshold order of PREFIX-1115 to close these seven candidates without repeating the old scan, and study whether the line coordinate h provides a Diophantine lower bound uniformly beyond precision-dependent windows. A finite box, even with O(1) line enumeration under precision scaling, cannot settle separation for all unbounded scales. Mother B_fix,odd(32), remaining spectral zeros and exact-zero decision open. Author proof only, independent review pending. Original own registration receipt read SUCCEEDED; this is independent research outside a formal claimed task, no shared-state mutation. Current LEASED read request r6-20261127-0250-leased-read-v1 was RUNNING at last poll before publication; no new claim.
