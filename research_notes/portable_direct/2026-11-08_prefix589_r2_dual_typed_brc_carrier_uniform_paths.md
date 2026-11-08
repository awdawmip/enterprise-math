# PREFIX-589-R2 — Reversed-phase dual BRC carrier, uniform open-path identity, and sharp positive boundary repair

2026-11-08. **AUTHOR-SIDE EXACT PROOF AND EXECUTED CERTIFICATE; UNREVIEWED / NOT ADMITTED.**

Frozen scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. No change to P000, native path semantics, axes, branch bits, or gate. Continues PREFIX-587 (combinatorial phase reversal) and PREFIX-588 (common positive cone) at research branch commit ad374b750ab728efcad841706b55f5ecf2886e63, PR #1797. Original native carrier: 48 phases, 96 ordered (phase,bit) ports, all 576 labelled transitions.

## Question and result

Is the positive conjugate W^{-1} A(x,z) W an explicit source/branch-typed BRC graph, and can it improve exact path evaluation once full costs are counted?

**Yes, it is a reversed-phase carrier with 96 ports, 576 typed edges, the same six source-axis weights and exactly three marked gate edges.** It is not an original-port relabeling: the original gate has three separate source ports with one gate edge each; the dual has one gate source with three gate edges. Remarkably, the original and dual have the SAME complete all-length uniform-boundary open-path generating polynomial for every sequence of nonstationary axis/gate weights. Arbitrary boundary observations require exact W/W^{-1} repair. The ordinary weighted edge count remains 576 per step on both carriers, so no sparse-core speedup has been established.

## Input structure

Use the original four STARs (1,3,6), (1,4,5), (2,3,5), (2,4,6). The 48 original phases are triples (a,p,c), where c is the signed current axis. S is the original 48×48 successor incidence matrix (exactly three 1s per row), and R is the 48-phase involution (a,p,c) → (a,c,p). Write X=diag(x_|c_i|) on phases and use a 2-bit port lift of S,R,X. For each phase i let M_i(z)=[[1,1],[1,z]] only if i=t=(0,1,-3), and [[1,1],[1,1]] otherwise. D(z) is the block diagonal matrix of those 48 two-bit matrices. The original marked X6-BRC operator is

    A(x,z) = Xhat Shat D(z).

The two exact combinatorial identities are

    R S R = S^T,
    S R = W0,   W0[i,j] = 1 if c_i=c_j and i!=j, else 0.

They are checked at all 2,304 positions each, with original four-STAR phases and successor rules. W=W0⊗I_2 has 24 four-port J4-I4 blocks and inverse J4/3-I4 per block. Because X depends only on current signed axis, Xhat commutes with W.

## Theorem 589.1: explicit positive dual typed carrier

For all formal parameters, over Q[x1,...,x6,z],

    T(x,z) = W^{-1} A(x,z) W
           = Xhat Rhat D(z) Rhat Shat^T.

Proof: substitute W=Shat Rhat into W^{-1} Xhat Shat D W; commute Xhat through W, use W^{-1}Shat=Rhat and Rhat Shat Rhat=Shat^T. All identities are polynomial, including zeros among x and z.

The dual has *reversed* phase successors: each source phase i has three target phases j with S[j,i]=1. The phase reversal moves the two-bit gate factor from the single original target t to the single dual source R(t)=(0,-3,1). Each dual port has six labelled actions (three successors times two target bits), all carrying the original source-axis weight x_|c_i|; exactly the three edges leaving (R(t),bit=1) with target bit=1 also carry z. The seven fixed dual coefficient matrices have disjoint 0/1 supports of sizes

    axis1 at z=0:93; axes2–6:96 each; gate x1*z:3.

Together 93+5*96+3=576 distinct labelled edges; at x=z=1, every row and every column has six edges. Original gate-marked outdegree pattern is (1,1,1) at three distinct ports; dual pattern is (3) at one port. A port permutation cannot change this pattern, so the dual graph is not a gate-labelled original-port relabeling. It is a faithful **linear observation carrier**, not an ontological replacement of native ports.

## Theorem 589.2: complete uniform-open generating identity

For arbitrary finite n≥0 and independent weight sets (x^(k), z_k), let A_k=A(x^(k),z_k) and T_k=T(x^(k),z_k). Then

    1^T A_n ... A_1 1 = 1^T T_n ... T_1 1.

Proof: A_k=W T_k W^{-1}. Every four-port block J4-I4 has row and column sums 3, so W 1=3·1 and W^{-1}1=(1/3)·1, with the corresponding left relations. Telescope all W^{-1}W factors and cancel the boundary 3×1/3. The identity is an equality of full generating polynomials in independently labelled parameters at each step, hence preserves the exact six-axis/gate-weighted uniform open-path enumeration for every finite depth, including nonstationary products.

For arbitrary left/right port boundaries l,r, the *exact* relation is

    l^T A_n ... A_1 r
      = (W^T l)^T T_n ... T_1 (W^{-1}r).

Fixed unchanged individual port boundaries are generally NOT equivalent. This separates observer fidelity from one-to-one path provenance.

## Theorem 589.3: exact positive domain and minimal compensator

For a four-port original block g let s_g=Σ_{i∈g}r_i. Then for each i in g,

    (W^{-1}r)_i = s_g/3 - r_i.

For original r≥0, this is nonnegative iff 3r_i≤s_g for ALL i. A single original port e_i maps to (-2/3,1/3,1/3,1/3), hence not every original positive native state lifts to a single positive dual state.

The smallest uniform nonnegative additive buffer for arbitrary nonnegative original block r_g is

    t_g = max(0, max_{i∈g}(3r_i-s_g)).

Indeed, 3(r_i+t)≤s_g+4t iff t≥3r_i-s_g, with equality attainable. For r_g=e_i the sharp buffer is 2. Let b be blockwise constant with this t_g; both r+b and b lie in W R_+^96. The decomposition

    r = (r+b) - b

therefore gives TWO individually positive dual evolutions under any nonnegative T-product, with an explicit signed subtraction at observation/reconstruction. It is not a one-channel Markov or probability conjugacy; the sign/cancellation is retained rather than concealed.

## Proposition 589.4: actual cost

W on a 4-port block uses one shared four-term sum (3 additions) and four differences; W^{-1} uses a shared sum, one divide-by-3, and four differences. Over 24 blocks, each boundary transform is O(96) scalar operations (24 divisions by 3 for W^{-1}); rational bit costs depend on input sizes. Both original and dual direct sparse matrix-vector products involve exactly 576 labelled weighted edge terms per step. For n steps, this baseline is 576n on either carrier, plus generic endpoint transforms and possible doubling for two-positive-buffer channels. Uniform-to-uniform boundary transforms cancel entirely. These are exact cost counts for the declared direct sparse evaluation strategy, NOT an asymptotic superiority claim or a lower bound against other algorithms.

## Reproducibility and remaining question

Original source definitions and prior transformation are reused (COMPOSE_APPLIED / EXTEND_EXISTING_TOOL), not replaced by new scientific inputs. The companion executed standard-library Python certificate reproduces all 48 native phases, original phase successors, 96 ports, six axis labels and gate marks. It verifies all 2,304 positions of both incidence identities; all 7×96×96=64,512 rational coefficient entries against independently generated dual edges; all 576 labelled edges and source-axis rows; gate topology; 24 positive-cone blocks, 96 singleton and sharp buffer cases; complete open-path equality through depth six for four parameter sets, plus a four-step inhomogeneous test. Result: ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED. General depth and symbolic-parameter claims rest on the preceding exact polynomial proof, not on finite samples. Full original project-module imports and independent Driver review were not executed in this run.

Next PREFIX-590: search for reusable positive-boundary buffering across batches of original-port queries; compare conditional-output costs to direct native state propagation, retaining all transfer, precision, source reconstruction and verification costs. Native Source task authorization, live Owner, CLAIM, Native Result and independent Driver review remain separate from GitHub author-side persistence.