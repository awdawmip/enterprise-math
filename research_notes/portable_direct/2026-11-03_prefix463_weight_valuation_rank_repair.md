# PREFIX-463 — Optimal prime-valuation repair of exact weighted X6 BRC occupation fibers

2026-11-03, Asia/Shanghai. Author proof with exact integer regressions. UNREVIEWED / NOT_ADMITTED. Successor to PREFIX-462. Frozen scientific source pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Question, native model and declared observer

Use the signed X6 chart and eleven primitive native directions D={+e1,±e2,...,±e6}; an X6 endpoint is a chart displacement rather than the public final Cell address. Fix word length m, history residue sector, a unilateral count s, and y=(y2,...,y6). Following the rigorously established PREFIX-462 occupation normal form, pi=min(ci+,ci-) for five opposite pairs, sum pi=p=(m-s-sum|yi|)/2. Exactly four integers are required to recover the entire unordered occupation label. We now restrict the observer to endpoint plus *individual positive-rational word-product weight and its exact integer histogram count*; operations querying explicit occupations or intermediate source order use the richer carrier.

## Theorem A — exact valuation signature for all lengths

Let the unilateral letter weight be w0>0 in Q and let wi+,wi->0 in Q be the five pair weights. Put rho_i=wi+ wi- (1<=i<=5). For i=2..5 form the rational ratios tau_i=rho_i/rho_1. Let P be the finite union of prime supports of tau_i and let B=(v_l(tau_i))_{l in P, i=2..5} be an integer matrix, allowing negative entries. For u=(p2,p3,p4,p5), all occupations at a fixed (m,s,y) satisfy

  WORD_WEIGHT = w0^s (prod_i (wi+)^max(yi,0) (wi-)^max(-yi,0)) rho_1^p (prod_{l in P} l^((B u)_l)).

Two occupations at that endpoint have equal individual word-product weights **if and only if** B u = B u' as integer vectors. The exact histogram count at one weight is the sum of multinomial contributions m!/[s! prod_i ci+!ci-!] over its corresponding B u fiber. Fixed −e1 steps in the last history sector N=q+m−1 under the independent letter-weight model contribute the usual interleaving factor C(N,q−1) and the (−e1 letter weight)^(q−1) to total *mass*. They do not restore erased path-order provenance.

**Proof.** The normal form gives ci+=max(yi,0)+pi, ci-=max(-yi,0)+pi. The fixed-signed-endpoint factor can be separated, leaving prod rho_i^pi = rho_1^p prod_{i=2}^5 tau_i^pi. Unique factorization of positive rationals into integer prime valuations makes equality equivalent to B u=B u'. The multinomial formula counts exactly the ordered native words with a specified occupation, and positive integer addition gives the weight histogram. QED.

## Theorem B — optimal count of universally additive integer repair coordinates

Write r=rank_Q(B), with 0<=r<=4. There is an integer-linear r-coordinate signature with precisely the same equal-weight equivalence for *every* admissible m,s,y. Any integer group homomorphism C:Z^4→Z^t having the same kernel as B must satisfy t>=r. Thus r is the minimal number of additive independent integer coordinates for that declared product-weight observer; it is not a bit-length optimality statement for bounded m.

**Proof.** The image of B:Z^4→Z^|P| is a subgroup of a finite-rank free abelian group and hence is itself free abelian of rank r. Choose an integral basis of im(B), obtaining the r-coordinate signature and identical kernel. For any C with ker C=ker B, im(C)≅Z^4/ker B has rank r, so t>=r. This comparison truly tests all formal occupation differences: given any z∈Z^4, choose nonnegative u,u' with u−u'=z, choose p>=max(sum u,sum u'), and set p1=p−sum u, p1'=p−sum u'. Both then occur at the legitimate endpoint s=y=0 of the same native residual length m=2p. QED.

## Exact two-coordinate example and information-loss witness

Choose w0=5, every wi+=1, and (wi-)=(6,12,18,24,36). Then tau=(2,3,4,6), and B has rank two. With reference pair 1, define A=p2+2p4+p5, C=p3+p5. Every pair-allocation weight for fixed p is 6^p 2^A 3^C; a five-pair occupation can be represented by two additive integers when only this weight observer and its histogram are queried. At m=4, s=0, y=0, the allocations (0,2,0,0,0) and (1,0,0,1,0) each give word-product weight 144 but correspond to 6 and 24 ordered words respectively. Their exact weight-histogram count is therefore 30. An occupation-sensitive future distinguishes the allocations.

## Executed finite certificate

The independently executable JavaScript `prefix463_weight_rank_certificate.js` uses BigInt arithmetic, exact integer Gaussian elimination and complete composition enumeration. It tests four rational-integer families with valuation ranks 0,1,2,4. For each family and m=0,...,6 it calculates exact endpoint/weight histograms by the occupation/multinomial formula and independently by ordered-step branch dynamic programming, and checks total ordered-word mass 11^m. It separately verifies the valuation signatures and their exact equality fibers for all pair partitions p=0,...,4, plus the explicit weight-144 collision. The actual output is `PREFIX463_EXACT_EXECUTION.log`, ending in `ALL_CHECKS_PASS`. A separate stdlib Python/Fraction certificate was also executed locally and its source/output provided in the conversation evidence package.

## BRC reuse, future operations and next question

REUSE_APPLIED: frozen positive-rational weighted BRC foundation and PREFIX-462 toric occupation fibers. This quotient is exact for endpoint/weight-histogram observers and weight-only future operations; explicit axis-occupation, branch order, history and typed provenance remain separate. A scalar total mass is not a substitute for the histogram when future observations distinguish weights.

Open PREFIX-464: implement unimodular Smith/Hermite lattice coordinates and measure actual bits, preprocessing cost and ordered/occupation-sensitive fallback on frozen BRC types. The distinct all-degree polynomial-moment rank problem on W_m remains open; this valuation theorem does not change the degree-(m+1) evaluation conjecture.

Authority: authenticated GitHub login awdawmip, repository admin/push. Native Sites gateway research_authority_granted=false, task listing returned CONTROL_QUOTA; no verified active owner, native Researcher-ID, CLAIM, independent Review or Admission. Author-side project Source publication only.