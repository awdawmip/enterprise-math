# PREFIX-507 — Uniform semilinear V-interval sums and weighted moments for BRC source supports

Date: 2026-11-05 (Asia/Shanghai). Research mode: independent author-side mathematical result. Researcher-ID: EM-DIRECT-7029EA (MCP service-issued Source session, not an authenticated formal Task CLAIM). Scientific inputs: immutable `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; current normative context read separately from both canonical main repositories. Predecessors: PREFIX-499 through PREFIX-506; direct immediate dependency is the PREFIX-499 three-letter suffix/Parikh lifting and PREFIX-500 fixed-inequality support certificate.

## Mother objective, selected unit, and precise observer

Mother objective: exact gapless ranking/unranking of the native X6 signed-path observation, with preserved support for future append of a primitive signed direction. This is the previously declared X6 *five-axis restricted path family*, whose sixth spatial axis is unoccupied, not a stand-alone native five-dimensional world. Retain path length n, displacement y=(y_a,y_b,y_c,y_d,y_e), BRC cancellation coordinates p_i=min(number of positive and negative primitive steps on axis i), joint observers V=p_b+2p_d+p_e and W=p_c+p_e, KMP terminal prefix length q for gate g in {aab,aba}, and absorbing first-source tag t in {N,B,C}. Source B is the first b/B, source C the first c/C. Full observation includes (q,t). The selected unit asks for an exact *sum over all V in an integer interval* and the first V moment, not merely support at a single V.

For fixed g, n, y and W let C_g(n,y,V,W) be the reachable (q,t) support; put
`k_g(n,y,V,W)=|C_g(n,y,V,W)|`.
Define, for any integers L<=H,

    F_g(L,H;n,y,W) = sum_{V=L}^H k_g(n,y,V,W)
    T_g(L,H;n,y,W) = sum_{V=L}^H (V+1) k_g(n,y,V,W).

Unreachable V contribute zero, including invalid parity/length cases.

## Theorem (uniform fixed-formula semilinearity and exact V-range moments)

For each fixed gate g in {aab,aba}, there exists an *effective finite offline compilation* depending only on g and the above observer (not on n,y,W,L,H) which computes F_g and T_g exactly, for all integer parameters and all L<=H, using a constant number of integer arithmetic operations and O(1) auxiliary integer words. With admissible parameters of path length n and intervals inside [0,2m], where m=(n-sum_i |y_i|)/2, all intermediate integer magnitudes have O(log(n+2)) bits. The compiling formulas and constants can be very large. The theorem is an existence and exact-algorithm construction based on Presburger quantifier elimination; an optimized compiler is a subsequent implementation problem.

### Proof: a fixed existential integer formula

Handle invalid n or m and all 2^5 fixed sign cases of y separately; min/max and parity are then expressible by fixed linear integer conditions. For each of the at most 5^min(3,n)<=125 fixed five-color suffixes of PREFIX-499, and the finite q/t cases, write the exact original occupancy equations

    p_a=m-V-W+d+e,  p_b=V-2d-e,  p_c=W-e,
    d=p_d>=0, e=p_e>=0.

The counts in five action colors a,b,B,c,x are

    k_a=p_a+max(y_a,0),
    k_b=p_b+max(y_b,0),
    k_B=p_b+max(-y_b,0),
    k_c=2p_c+|y_c|,
    k_x=p_a+max(-y_a,0)+2(d+e)+|y_d|+|y_e|.

The condition that a given suffix is realizable is `k_i >= count_i(suffix)` for all colors. Its terminal q is determined by the suffix, and first-source t has a finite exact disjunction: a nonempty B-source prefix; a nonempty C-source prefix; or no source in the prefix, when the suffix determines its first source. For n<3 use the entire word as suffix. Thus, for each fixed (q,t), membership in C_g is equivalent to a *single fixed Presburger formula*

    Phi_{g,q,t}(n,y,W,V) = OR_{finite suffix/branch cases}
                             EXISTS d,e in Z: AND_{finite} (a*d+b*e+c*V+linear(n,y,W)+constant >= 0),

with congruence/parity and sign-case guards included. All integer coefficients and the numbers of variables, atoms and branches are constants depending only on g. This is an exact reformulation of PREFIX-499 and PREFIX-500, with V left free rather than numerically instantiated.

### Proof: elimination, interval partition and summation

By effective quantifier elimination for Presburger arithmetic in the language expanded by fixed divisibility predicates, each fixed Phi_{g,q,t} is equivalent to a *fixed finite* Boolean combination of (i) linear inequalities `a*V+beta(n,y,W)>=0` and (ii) congruences `c*V+gamma(n,y,W) == 0 (mod M)`, with fixed coefficients and fixed positive moduli. The converted expression is computed once from the fixed formula, not separately for each n.

After substituting n,y,W, every inequality changes truth at at most one integer threshold in V (or is constant), and every congruence has truth determined by V mod a fixed modulus. Let Lambda be the least common multiple of all resulting fixed moduli; it is a model constant. Sort the finitely many V thresholds together with L and H+1. There are only O(1) integer slabs. Within each slab and each residue r mod Lambda, all atomic truths, and thus each Phi, are constant; one test classifies the whole slab/residue. The number of satisfying V in [A,B] of residue r mod Lambda is

    N= floor((B-r)/Lambda) - floor(((A-1)-r)/Lambda).

When N>0 the first satisfying V is
`v_first=r+Lambda*ceil((A-r)/Lambda)`, the last is `v_last=v_first+(N-1)*Lambda`; the arithmetic progression contributes
`N` to F and `N*(v_first+v_last+2)/2` to T. The numerator is even. Sum over the fixed list of slabs, residues and all 12 possible (q,t) states (some intrinsically absent). This counts each *controller state* separately, so reachable support multiplicity and the precise KMP/first-source observers remain recoverable. The V interval itself is the queried aggregate, not an equivalence that discards controller state.

All loops after fixed offline formula compilation have constant bounds. That proves the theorem. Bit cost is governed by exact arithmetic on O(log(n+2))-bit integers, including an O(log n)-bit multiplication for T; no unit-cost bit-complexity claim is needed.

## Why congruence classes are essential: a minimal exact hole

For g=aab, n=2, y=(0,0,0,0,0), W=0 and controller state (q,t)=(0,N), the reachable V values are exactly {0,2}. A native a/A cancellation can give V=0 and a d/D cancellation gives V=2. V=1 forces a b/B cancellation (which changes first source to B), because an e/E cancellation would have W=1. Hence V=1 is a genuine hole. An unqualified contiguous-interval criterion would give an incorrect state support. The same gap holds for gate aba. This explicitly motivates integer residues in the interval compiler.

## Consequences for the established rank indexing routes

For PREFIX-503, each W-row total and V prefix can in principle be supplied by F in O(1) arithmetic per row/boundary, replacing the O(n) sequence of single-V membership calls. For PREFIX-504's block index of width b, each block total can be obtained by one F query, reducing its support acquisition from O(n^6) to O(n^5+n^6/b) *compiled aggregate queries*, matching the count of rows/boundaries. PREFIX-505/506 additionally use C(i,j)=T(i,j-1)-i*F(i,j-1); the theorem supplies exact O(1) block-cost queries when compiled, while choosing optimal adaptive block boundaries still incurs the proved near-linear DP cost. Each conclusion assumes the fixed compiled Presburger expression is available; this round does not assert competitive concrete constants or a deployed compiler. Support at a selected V and its (q,t) ordinal remains available via the existing PREFIX-500 membership oracle. Native append is handled by the established append-then-reencode route in the declared observer horizon.

## Executed certificate, range, and evidence meaning

The companion standalone JavaScript file directly enumerates *all ordered ten-direction native words* at lengths n=0..6 for both g, independently enumerates all ten-letter occupancy vectors and lifts their five-color suffix supports at n=0..9, compares complete (n,y,V,W,q,t) sets for n<=6 and checks F and T on every V interval of every observed (y,W) row in that range. Computed values are exact safe integers on these bounded instances. The script records the {0,2} gap. The resulting JSON reports ALL_CHECKS_PASS. This is a finite validation of the exact Parikh observer input and moment definitions; the universal O(1)-arithmetic claim is proved by the fixed Presburger formula and standard effective elimination, **not** by finite tests. No compiled quantifier-elimination implementation or measured large-n acceleration is claimed.

## Sources, status, next discriminating question

Sources: original frozen scientific pin above; committed PREFIX-499 and PREFIX-500 proofs and PREFIX-506 predecessor; D. C. Cooper, "Theorem Proving in Arithmetic without Multiplication" (1972), Machine Intelligence 7; Derek C. Oppen, "Elementary Bounds for Presburger Arithmetic" (STOC 1973), https://doi.org/10.1145/800125.804033; Christoph Haase et al., "An efficient quantifier elimination procedure for Presburger arithmetic" (2024), https://arxiv.org/abs/2405.01183. The general quantifier-elimination theorem is established mathematics; the fixed-template application and resulting BRC V-range/moment algorithm are the present derivation.

Scientific state: AUTHOR_PROVED_FROM_STANDARD_QE / EXACT_FINITE_OBSERVER_CHECKED / UNREVIEWED / NOT_ADMITTED. Independent mathematical review and practical compiler validation are open.

Next PREFIX-508: actually compile the two-quantifier linear support templates to an explicit interval/residue decision program; use the single-V oracle as a reference and test arbitrary [L,H] on full native observations n<=9. Measure compiled expression size, preprocessing, full V-row sum versus repeated membership calls, b-block construction and adaptive Monge planner; if generic elimination constants are excessive, specialize the d/e Fourier-residue elimination, retaining the exact {0,2} hole.
