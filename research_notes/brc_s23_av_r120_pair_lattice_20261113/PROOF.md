# R120-LATTICE — Arbitrary-separation S23 pair feasibility by a 2D integer lattice projection

Date: 2026-11-13 (Asia/Shanghai). Enterprise Math Research1 author-side auxiliary mathematical result. Frozen scientific-input pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Predecessors: R118 and R119.2 at \`825beb42ae5439b529e2bb2727833d25b0018f70\`. The S23 ranked Boolean observer is the theorem's model; native Cell/Link/Port permissions and formal promotion remain separate.

## Model and question

Fix integers j,a,c,N,d with d≠0; rational x; and a bounded rational parameter interval I. Define frac(z)=z−floor(z), Y_t(θ)=x+(t−j)θ, A(θ)=frac(aθ), C(θ)=frac(cθ). M_t(θ)=1 when frac(Y_t(θ)) lies in the positively directed half-open circular arc [A(θ),C(θ)); coincident endpoints mean the empty arc.

Given an old parameter atom J=(l,h) on which all old historical source eligibility bits are constant, determine exactly the jointly attainable pairs (M_N(θ),M_{N+d}(θ)) and recover rational witnesses. No Cartesian-product independence of the two bits is assumed. Existing R119.2 subdivided at relative-phase cuts that can number Θ(|d|); here d is arbitrary.

## R120.1 Exact fixed-dimension reduction

**Theorem.** On each old open atom after, if needed, further splitting only at integer crossings of aθ,cθ,(a−c)θ, each of the four prescribed joint Boolean pairs is attainable if and only if at least one of at most four rational two-variable integer linear systems is feasible. Every feasible system produces an exact rational θ in J witnessing both original predicates. The generated systems have constant numbers of constraints and coefficients of polynomial binary length in the input, including log(|N|+2)+log(|d|+2), without enumerating new-time or relative-time phase cuts.

**Proof, arc segmentation.** On such an atom the fractional A,C and their order are rational-affine with fixed ordering. The circular bit-1 arc and bit-0 complementary arc each become at most two real segments [L(θ),U(θ)) in [0,1), with rational-affine endpoints. For A=C throughout the atom, bit 1 has no segments and bit 0 is [0,1). Isolated phase endpoints are evaluated directly using M_t. For one chosen segment of each bit, put s₀=N−j, s₁=N+d−j. There exist θ∈(l,h) and n,m∈Z satisfying both chosen bits exactly when

    x+s₀θ−U₀(θ) < n ≤ x+s₀θ−L₀(θ),
    x+s₁θ−U₁(θ) < m ≤ x+s₁θ−L₁(θ).

These are simply the identities Y_N−n∈[L₀,U₀) and Y_{N+d}−m∈[L₁,U₁). There are at most 2×2=4 segment pairs.

**Proof, strict-boundary elimination.** Let D_i(θ)=x+s_iθ−U_i(θ), H_i(θ)=x+s_iθ−L_i(θ). Introduce a continuous common slack ε:

    0 ≤ ε ≤ 1,
    l+ε ≤ θ ≤ h−ε,
    D₀(θ)+ε ≤ n ≤ H₀(θ),
    D₁(θ)+ε ≤ m ≤ H₁(θ).

The original open-atom and half-open inequalities are feasible if and only if these conditions hold for some ε>0. Clear all rational coefficients and constants in these eight affine inequalities with one common positive denominator Q. Let M≥1 bound the absolute integer coefficients of θ and ε in the resulting scaled inequalities (enlarge it to bound all coefficient sizes if desired). For fixed integers n,m, the feasible (θ,ε) set is compact, since θ∈[l,h] and ε∈[0,1]. If its maximum ε is positive, a vertex attains that maximum. At a vertex, two independent active integer-coefficient rows determine (θ,ε); Cramer's rule gives a strictly positive ε with numerator a nonzero integer and denominator of absolute value at most 2M². The integer parameters n,m enter only the right-hand sides, so this bound holds uniformly across all pairs. Thus existence of some ε>0 is equivalent to feasibility with the fixed

    ε₀ = 1/(2M²).

This rational ε₀ has polynomial binary length, and fixes all strict endpoints exactly: the resulting inequalities are closed rational linear inequalities.

**Proof, two-dimensional lattice.** With ε=ε₀, write each inequality as

    α_i θ + β_i n + γ_i m ≤ δ_i.

If α_i>0 it gives an upper affine bound on θ; if α_i<0 a lower affine bound; if α_i=0 a direct rational inequality in n,m. Pair all lower bounds with all upper bounds to eliminate θ by one-variable Fourier–Motzkin projection. The result is a constant-size rational system in integer n,m only, feasible exactly when the mixed system is feasible. The original finite interval and [0,1) phases bound n,m. Clear remaining denominators to obtain an ordinary **two-variable integer linear feasibility problem**. Any feasible integer pair admits θ between the largest lower and smallest upper bounds; their rational midpoint is a witness. This proves exact equivalence and preserves open/closed endpoint semantics.

**Complexity corollary.** Lenstra's standard fixed-dimensional integer programming theorem gives polynomial-bit-time feasibility for each such two-integer system. Thus **for two new times**, at most 16 fixed-dimensional integer-programming calls per original old atom suffice over all four bit pairs, with bit complexity polynomial in the coefficient/input binary length and no Θ(|d|) enumeration. The polynomial assertion uses the classical fixed-dimensional ILP theorem, not a new proof of Lenstra or a claim about an unimplemented optimized solver. The number of old atoms, old history cost and output signatures remain explicit. Reference: H. W. Lenstra, Jr., “Integer Programming with a Fixed Number of Variables,” *Mathematics of Operations Research* 8(4):538–548 (1983), DOI [10.1287/moor.8.4.538](https://doi.org/10.1287/moor.8.4.538).

## R120.2 History and rational witness

Old history eligibility signatures remain constant within each input atom. Therefore every recovered θ inherits the exact old source identities, ranking, membership provenance and all old eligibility bits at that atom. Process disconnected atoms independently, then union complete signature tuples. Singleton rational atoms require only direct exact evaluation. Thus the method extends R119's two-time joint feasibility to arbitrary signed integer separation without treating separately attainable bits as jointly attainable.

## Exact verification and execution scope

Files \`check_r120.py.gz.b64\` (gzip/base64 of complete standalone Python 3 \`Fraction\` checker) and \`verification_r120.json\` accompany this proof. Decode with \`base64 -d ... | gzip -d > check_r120.py\`. The checker constructs the exact epsilon bound and 2D projection, **exhaustively enumerates bounded integer pairs only on small tests**, extracts rational witnesses and compares attained bit pairs with an independently constructed full six-phase cut atomization. It also checks two positive huge signed certificates without enumerating their cuts. Executed result:

    R120_REDUCTION_PASS
    120 randomized cases; 1,086 base atoms; 5,512 full-cut atoms;
    2,412 bit-oracle calls; 63,077 small integer pairs checked;
    1,480 exact rational witnesses; 2 huge signed positive witnesses.

These finite tests are implementation evidence for the equivalence. A general exact Lenstra/2D-ILP implementation is **not present in this checker**; the arbitrary-large-separation polynomial bit-complexity conclusion is a proved reduction **conditional on using the published fixed-dimensional ILP algorithm**. Huge signed cases verify only their displayed positive witness conditions.

## Next frontier

Implement a genuinely exact two-variable integer-programming witness solver; compare total integer bit costs against R119.2 for small |d| and the full phase-cut enumeration for large |d|. Explore multi-time extensions with m new integer variables and whether particular shared S23 structure admits reductions better than generic fixed-m ILP. Preserve P000's six-dimensional native space, three-dimensional research-slice status, signed provenance, and the separate auxiliary-to-native correspondence obligation.
