# PREFIX-488 — Exact seven-mask Ehrhart classification on a zero-displacement BRC slice

Date: 2026-11-04 Asia/Shanghai. Researcher-ID: EM-DIRECT-33A971; Research-Activity-ID: RA-6043A829ECC5A25016F40D16. Status: author-side proved and exact-integer checked; not independently reviewed or admitted.

Continuation: PREFIX-487 at enterprise-math@09941b1e0c3fab9fa6b995c401206ff3fd714396. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d, unchanged. This is an explicitly restricted observable family within full native signed X6, not an independent two-dimensional native space.

## Exact question and typed observer

Use the ten signed ordinary steps a/A,...,e/E, and a sixth-axis special step x. Gate word w is aab or aba. A source tag begins N and becomes B or C according to whether the earliest b/B/c/C letter comes from the b/B or c/C family. Terminal gate state q is the KMP suffix state.

Fix a path length n=2m, with m>=0, zero special steps s=0, all five signed displacements y_i=0, and final KMP state q=0. Then u_i=v_i=p_i>=0, sum p_i=m. The base BRC observer is (n,s,y,V,W,q), where V=p_b+2p_d+p_e and W=p_c+p_e. We count distinct observed fibers with each possible source SUPPORT MASK (not ordered-path multiplicities).

For either gate, uppercase letters reset q to zero. Every nonempty balanced raw-count vector contains an uppercase letter. Given any such raw vector, it can be ordered with a selected first b/B or c/C event and uppercase last; thus N is realized precisely by p_b=p_c=0, B by p_b>=1, and C by p_c>=1. These are existence statements, and the underlying ordered-path population retains branch identities. The empty path has q=0 and tag N.

## Theorem A — saturated BRC lattice image

The set of feasible observer pairs (v,w) for every m>=0 is precisely

    P_m = {(v,w) in Z^2 : 0<=w<=m, 0<=v<=2m-w}.

Proof: The five cancellation-pair columns (V,W) for a,b,c,d,e are (0,0),(1,0),(0,1),(2,0),(1,1). For fixed w, allocate w columns among c/e, whose attainable v-values are exactly 0..w. The other m-w columns among a/b/d span all 0..2(m-w). Integer intervals add without gaps, so every v in 0..2m-w occurs. Conversely the columns obey these bounds.

Consequently |P_m|=(m+1)(3m+2)/2, the Ehrhart lattice count for a polygon of area 3/2 and boundary count 5.

The exact support tests for any (v,w) in P_m are:

    N <=> v>=w AND v-w even AND v+w<=2m
    B <=> 0<=w<=m-1 AND 1<=v<=2m-w-1
    C <=> 1<=w<=m AND 0<=v<=2m-w-1.

For N, setting p_b=p_c=0 yields w=p_e, v=2p_d+p_e, p_a=m-p_d-p_e. For B, subtract one b cancellation pair, shift (v,w) by (-1,0), and apply the saturated image with m-1 pairs. For C, subtract one c pair, shift (v,w) by (0,-1). These constructions prove necessity and sufficiency, including m=0.

## Theorem B — exact classification of all seven masks

For every m>=1, using bit masks N=1, B=2, C=4:

| Exact support | Number of observer fibers |
|---|---:|
| N only | m+2 |
| B only | m |
| C only | 2m-1 |
| NB only | m-1 |
| NC only | 0 |
| BC only | (m-1)^2 |
| NBC | m(m-1)/2 |

At m=0 there is exactly one N fiber and zero in the other six classes. Both gate words share the formulas for this slice.

Proof: B-only occurs at w=0, v odd in [1,2m-1], giving m fibers. NB-only occurs there for v even in [2,2m-2], giving m-1. C-only consists of the left edge v=0, w=1..m and the top edge w=m,v=0..m-1, which meet once: 2m-1 points. NBC corresponds to w=1..m-1 and d=(v-w)/2=0..m-w-1; hence sum (m-w)=binom(m,2). The B∩C interior strip 1<=w<=m-1,1<=v<=2m-w-1 has (m-1)(3m-2)/2 points, so BC-only is (m-1)^2. The number of N points equals the count of (p_a,p_d,p_e) summing to m, binom(m+2,2); subtract NB-only and NBC to obtain m+2 N-only. NC-only is empty since every N∩C point is also in B. The classes partition P_m, and their sum is |P_m|.

## Corollary — rational generating functions and growth

Let z count original path length n and t=z^2. With coefficients indexed by m=n/2, the exact series are

    G_N(t)  = 1+t/(1-t)^2+2t/(1-t)
    G_B(t)  = t/(1-t)^2
    G_C(t)  = t(1+t)/(1-t)^2
    G_NB(t) = t^2/(1-t)^2
    G_NC(t) = 0
    G_BC(t) = t^2(1+t)/(1-t)^3
    G_NBC(t)= t^2/(1-t)^3
    G_ALL(t)= (1+2t)/(1-t)^3.

The seven sequences are explicit quasi-polynomials of period dividing 2 when indexed by the original length n, since odd lengths have no zero-displacement paths. Their even-n leading terms are: B-only m, C-only 2m, BC-only m^2, and NBC m^2/2.

## Exact executed evidence and scope

The companion Python 3 certificate uses only exact integer arithmetic. It enumerates all five-axis pair-count vectors for m=0..34 (575757 vectors), compares their aggregated masks with the direct polygon predicates and closed formulas for every (v,w), and independently enumerates all distinct ordered paths compatible with each pair-count vector for m=0..3 (11181 words per gate). The ordered-path check explicitly computes terminal q and source tags for both gates. Full log: PREFIX488_EXACT_EXECUTION.log, final marker ALL_CHECKS_PASS.

The finite checks confirm the code and tested examples. The proof above covers all m>=0. This is a Boolean source-support observer theorem, not a replacement for full path multiplicities, provenance, positive mass, signed amplitudes or arbitrary-future continuation. It leaves existing P000, ACTIVE X6 ontology, joint observer-preservation, BRC method and frozen scientific input intact.

The proof uses direct integer interval saturation and lattice counting. Contextual sources: Kevin Woods, "Presburger Arithmetic, Rational Generating Functions, and Quasi-Polynomials", Journal of Symbolic Logic 80(2), 2015, doi:10.1017/jsl.2015.4; Pick's theorem. They support the general counting framework, not the specific enumerated mask formulas.

## Next executable question

Extend this exact classification to s=0, y_b=y_c=0, free y_a,y_d,y_e, with q=0, accounting for pure terminal a-word exceptions, then allow q>0 and x>0. The full B-only/C-only/BC-only counts from PREFIX-487 remain open. Native authenticated session was registered in RA-6043A829ECC5A25016F40D16; neither the session nor this GitHub author-side artifact creates a formal CLAIM, independent review or admission.
