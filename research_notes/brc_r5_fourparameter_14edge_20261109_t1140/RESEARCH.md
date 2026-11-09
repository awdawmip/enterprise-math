# R5: an exact four-physical-parameter, three-observer-parameter, 14-edge Blackwell chart

2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING. This is a research note, not a formal Result or mathematical admission.

## Frozen input and purpose

Continue the P/Q-BRC seven-likelihood-ratio-node model with ratios (1/10,1/2,3/4,1,5/4,3/2,19/10), FULL_HIST source, seedless F target, and g=b. Predecessor PR #1873 at immutable commit 2cd0988e8461607db04312b05304dcb1c4630340; its Blackwell and physical-flow definitions reuse PR #1859 at f63a0250714f2445e8b406754b85f26d983ec3a6. Frozen scientific source pins stated by the predecessor: GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Current operational policy was read separately.

The mother objective is the uniform <=14-positive-edge transport question for every lawfully Blackwell-feasible g=b physical strategy pair, versus a real >=15-edge-necessary pair. This result enlarges a local constructive chart; it is not mother-objective closure. These likelihood-ratio/statistical coordinates do not change P000's six native spatial dimensions and independent time.

## Theorem (sharp uniform-radius 4D rectangular chart)

Physical flow order is (g,a,b,u,v,w,z). Set

    X0 = (999/1000,1/6,999/1000,1/20,29/240,11/160,1/120).
    Y  = (1,2002911/10904720,26095487/40892700,
          442758619/6542832000,11037627/68154500,
          394502727/2180944000,2002911/109047200).
    H = 17774559/17507527960,
    rho_star = 17774559/225414193300.

The target Y is seedless F (g=1 and z=a/10). Work with the same fourteen candidate edges S as PR #1873, in target/source index order:

    (0,0),(0,1),(3,1),(5,1),(0,2),(2,2),(3,2),
    (2,3),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6).

The exact baseline transport E0 and four edge derivatives V1,V2,V3,V4 are given, in this edge order, as rational vectors in the accompanying VERIFY.py. V4 is the predecessor's exact epsilon derivative. Define the four physical directions

    U1=( 1/2,-7/2, 1/2,1,0,0,0),
    U2=(-1/2,-1/2,-1/2,0,1,0,0),
    U3=(-3/2, 5/2,-3/2,0,0,1,0),
    U4=(0,0,0,0,0,0,1).

For real p,q,r,epsilon, put

    X=X0+p U1+q U2+r U3+epsilon U4,
    E=E0+p V1+q V2+r V3+epsilon V4.

For EVERY real 0<=rho<rho_star and EVERY real point in the box

    -rho <= p,q,r <= rho,
    H/4 <= epsilon <= 3H/4,

X is a lawful g=b FULL_HIST source, Y is the fixed lawful seedless target, the two stopping times agree exactly (17609/6000,33857/12000), and E is a legal Blackwell coupling with EXACTLY 14 strictly positive edges. All 21 mass/likelihood-ratio-moment equations hold as exact affine identities over this full real box.

At rho=rho_star all physical conditions and nonnegative coupling conditions still hold. Exactly two box vertices acquire zero edges:

    (epsilon,p,q,r)=(H/4,-rho,+rho,+rho): E_(5,1)=0;
    (epsilon,p,q,r)=(3H/4,+rho,-rho,-rho): E_(5,5)=0.

The radius is SHARP for this fixed epsilon interval, symmetric p/q/r box, and affine transport chart. For any larger radius the first displayed corner makes E_(5,1)<0, because its limiting baseline is 219439/2180944000 and the sum of absolute p/q/r edge coefficients is 16537/12960.

A concrete fully positive certificate uses rho=1/100000. Exhausting the 16 rational vertices gives minimum strictly-required physical slack (excluding the identically tight equality g-b=0) equal to 39/40000, and minimum coupling edge

    15520417067 / 176656464000000 > 0.

At the SHARP radius, the minimum remaining physical slack is 904888979/1127070966500 > 0, and the minimum edge is zero only at the two designated vertices.

## Four physical directions, exactly three observable directions

Let C be the 21-by-14 matrix mapping the fourteen edge weights to seven target marginals, seven source marginals, and seven source LR moments. Its (i,j) edge column carries 1,1,r_i in the relevant rows. Let B be the derivative of those 21 right-hand sides with respect to the seven source variables. Append g=b and both fixed stopping-time derivatives to (C | -B). The resulting exact 24-by-21 rational matrix has rank 17 and nullity 4. Every pair (Vk,Uk) is an explicit null vector. The four Uk are linearly independent because their u,v,w,z entries form the standard basis. Hence these four directions span the ENTIRE affine equality solution space for this fourteen-edge support, fixed target, times, and g=b.

The physical-to-statistical mass observation map along these four directions has rank exactly 3. Its observer-row (0,1,2), direction-column (U1,U2,U3) minor is

    det = -295513/324000 != 0.

An exact observer-kernel parameter vector is

    k=(-33345/591026,132145/295513,-33345/591026,1).

Its physical image is the previously obtained kernel direction

    K=(-49400/295513,-49400/295513,-49400/295513,
       -33345/591026,132145/295513,-33345/591026,1).

Exact derivative tests give DMass[K]=0 and sum(k_i Vi)=0. Thus this 4D physical chart maps onto a genuine 3D marginal region and retains one transport-invariant physical residual direction; no native X6 dimension is added.

## Phi bridge and atlas residual

On the entire chart, the predecessor's saturated-face dual observer has the exact single-bridge representation

    Phi(M(Y),M(X)) = E_(5,1)
       = (421/4000)p - (11749/12960)q
         - (9511/36000)r + (3211/8100)epsilon.

For rho<rho_star this bridge is strictly positive. The old sixteen-edge atlas's out-of-support mass for THIS explicit coupling is

    Escape(E) = 8555233477/73606860000
                - (35053/36000)p + (40873/23328)q
                + (748223/324000)r - (51623/72900)epsilon.

It is not claimed as a minimum over all couplings.

## Proof and validation scope

The accompanying self-contained Python Fraction verifier checks each of four direction equations, exact matrix ranks, Phi and atlas-mass identities, all 21 Blackwell equalities and physical/slack/time conditions at 16 vertices of rho=1/100000 and at 16 vertices of rho_star, including both sharp endpoint zeros and a strictly negative edge for a larger radius. Every equality and inequality is affine in (p,q,r,epsilon); the 16 rational corner checks therefore prove the entire real box by convexity. The exact stdout is provided in EXACT_OUTPUT.txt. No floating-point LP solution or numerical rank threshold is part of the proof.

Tool reuse: REUSE_APPLIED to the predecessor's rational mass/slack/time and fourteen-edge chart; EXTEND_EXISTING_TOOL with exact four-parameter rank and corner certificates. This is author-side exact proof verification; independent review and formal task admission remain separate.

## Next discriminating action

Perform exact adjacent-support pivots at the two active boundary edges (5,1) and (5,5) and test which support substitutions create another legal full-dimensional chart, then continue the all-physical 14-versus-15 question. Preserve the frozen inputs and task-owner state; no formal CLAIM/Result is asserted by this note.
