# Seven positions, jointly scaled common numerator and denominator errors

Use the three overlapping fourth differences of seven consecutive observations. Write G=Δ⁴P=(20,20,20,−100,140,−100), Sₐ=(Gₐ,Gₐ₊₁,Gₐ₊₂), with cyclic indices. All seven observations use the same integer errors (e,d). Define scaled parameters E=25920e/r⁶ and D=4320d/r⁵. The original nearest-signature distance is the maximum norm, with ties counted as failures.

## Uniform asymptotic model

Fix a compact parameter set |E|≤L, |D|≤δ<1. Uniformly over this set and r→∞,

    observed triple = A(E,D) Sₐ + B(E,D)·(1,1,1) + O(1/r),
    A=(1+E)/(1+D)²,
    B=−4[D⁵−121D⁴+70D³E+381D³−365D²E−121D²+185DE+D−5E]/(1+D)⁵.

The compact-set assumption makes all seven exact denominators positive for r sufficiently large. A numerator-only specialization gives A=1+E, B=20E. The two-parameter representation is a limiting family of observed triples; its formula alone does not establish a sharp all-r threshold for every mixed budget ratio.

**Proof.** The frozen source generating functions are z/[(1−z)³(1−z²)(1−z³)(1−z⁶)] for C and z²/[(1−z)⁴(1−z²)(1−z³)(1−z⁶)] for T. Subtract the polynomial parts C₀ and T₀ of their pole at z=1. At all integer q the other poles contribute C(q)−C₀(q)=hₐ q+O(1), T(q)−T₀(q)=O(q). Here 5184h=(−91,59,5,−37,5,59); the non-unit double pole fractions for C are −1/[192(z+1)²]−(z+1)/[54(z²+z+1)²]. In particular Pₐ=−720hₐ exactly. The smooth degrees and leading coefficients are C₀∼q⁵/4320, T₀∼q⁶/25920. The exact data are q³[T(q)+e]/[C(q)+d]−q⁴H₄(q).

Use fixed r, q=rx, x near 1. Replace T by T₀, producing an O(1/r) error. Expanding the denominator in C−C₀ gives the additional leading term

    −q³[T₀(q)+e]hₐq/[C₀(q)+d]²
    = −720 hₐ x⁴(x⁶+E)/(x⁵+D)² + O(1/r)
    = A(E,D)Pₐ + O(1/r)

at each of the seven integer q=r+j, since x=1+O(1/r). The bounded remainder in C−C₀ yields O(1/r) and its square yields O(r⁻⁴). All constants are uniform via the positive lower bound for x⁵+D. For the smooth rational profile after this replacement, expand on x∈[1,1+6/r] with h=1/r. Its leading term is r⁴F(x;D,E), where

    F(x)=(E x³−D x⁴)/[6(x⁵+D)].

The remaining part is r³ times a smooth profile with uniformly bounded first four x derivatives. This follows by extracting the leading constants in the polynomials C₀,T₀ and the polynomial q⁴H₄ and using the mean-value integral in h. Thus a fourth forward difference of the remaining term is O(r⁻¹). The fourth difference of r⁴F equals F''''(1)+O(1/r), uniformly, by integration over the unit four-cube and a uniform fifth derivative bound; this also holds at the next two starts. Evaluation of F''''(1) is precisely the displayed B. Applying the three fourth differences to the oscillating term yields A Sₐ.

For fixed D both A and B are affine in E. To implement sensitivities, ∂EA=1/(1+D)², ∂DA=−2(1+E)/(1+D)³, ∂EB=−4(70D³−365D²+185D−5)/(1+D)⁵. The integral argument yields the same uniform O(1/r) approximations after one parameter derivative on a slightly larger compact set for the rational extension to real bias parameters. At fixed budgets, dr(E,D)/dr=(−6E/r,−5D/r).

## Sharp denominator-only threshold

Put E=0. Let δ* be the unique positive zero of

    15−56δ−41δ²−441δ³−96δ⁴−6δ⁵ = 0.

Numerically δ*≈0.187761900809406. Then, as K→∞, the least all-future cutoff for |d|≤K is

    N(0,K)=(4320K/δ*)^(1/5)+O(1).

For the ideal limiting curve, consider every ordered phase pair a,b. Since |D|<1, multiply all distances by (1+D)⁵ and compare for i=1,2,3 the absolute values of the polynomials (1+D)⁵(A Sₐ,i+B−Sᵦ,i). A change between strict success and failure requires a root of a polynomial equating two signed coordinates, one true and one rival, unless they are identical on the whole interval. Identical polynomials do not create cell boundaries. Isolating and sorting the roots of the 24 distinct normalized nonzero polynomials on [−1/2,1/2] gives 13 distinct root points. On each resulting open interval, the comparison sign between every true-coordinate absolute value and every rival-coordinate absolute value is fixed, hence so is the nearest-signature decision. For the first crossing in each direction the checker evaluates one rational point in every intervening open interval and all intervening real algebraic endpoints, using exact division, root isolation and rational signs. The first negative crossing occurs at D=−δ* for exactly the pairs (true,rival)=(1,0),(5,0). The first positive crossing is √2−1>δ*. Exact executable: denom_scan.py and denom_exact.py (SymPy polynomial arithmetic); no rounded boundary is used to infer endpoint outcomes.

A tie has to persist for the lower bound despite the O(1/r) error. At the negative endpoint, the true phase 1 has S₁=(20,20,−100) and its rival S₀=(20,20,20). Put b₂₀=20A+B and b₋₁₀₀=−100A+B. Nearby the true maximum is on one of the two shared coordinates. For the rival, the shared residual minus the unshared third absolute residual is

    (b₂₀−20)−(20−b₋₁₀₀)
    =−8(6D⁵−96D⁴+441D³−41D²+56D+15)/(1+D)⁵.

At D=−δ* this vanishes simply (positive-coefficient derivative of the δ polynomial after sign), and for slightly more negative D it is strictly positive. The third-coordinate true residual is separated by a fixed positive margin: b₂₀−20 > |b₋₁₀₀+100| near that point. The signs and that strict inequality follow, for instance, by rational interval arithmetic isolating D inside (−188/1000,−187/1000). Thus on the bad side the true and rival distances attain their maximum on the same two coordinates with identical reference values. This gives an exact tie even with unequal finite-r errors on those two coordinates, provided both third-coordinate residuals are below their maximum. Its margin grows at least linearly in |D|−δ*. The reverse phase placement a=5 has the same two shared coordinates in a different order.

The exact cell check and this local formula imply a positive uniform success margin for smaller |D|, bounded below by a fixed multiple of min(1,δ*−|D|). Near the negative endpoint only these two phase pairs close linearly; other pairs stay away from zero. At D=+δ* there remains an open gap to the first positive tie. With ρ=(4320K/δ*)^(1/5), the magnitude 4320K/r⁵ crosses δ* at ρ with derivative −5δ*/ρ. The uniform O(1/r) approximation applies in a fixed neighborhood of the crossing and for all greater r. Hence r≥ρ+B₀ suffices for a universal B₀. For the converse take r≡1 modulo six in [ρ−B₀−6,ρ−B₀] and the common integer d=−K; all denominators remain positive, and both distance maxima are on the identical shared coordinates, giving an exact tie. The choice B₀ absorbs the O(1/r) perturbations by the simple crossing. This proves the sharp additive O(1) statement.

Author-side calculation and exact finite algebraic audit. The statement is for this seven-position auxiliary observer. It does not cover poles corresponding to D→−1 or establish a nonlinear source operation.
