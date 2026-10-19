# R5 — 严格正可逆核的最优全边际单步层析（作者级，未经审查）

Date: 2026-10-20. Status: AUTHOR_PROOF_UNREVIEWED / EXACT_RATIONAL_CHECKED / AUXILIARY_MODEL / NATIVE_BRC_TRANSFER_PENDING.
Activity: RA-R5-FULLMARGINAL-20261020-0740-A01. Identity: locally assigned research author, no native CLAIM.
Sources: GLOBAL_KNOWLEDGE_V1 main@d68fb9c8426eb927f04fd35c6d71650499e5da10; Enterprise Math main@25c86bd3090c296b4e7e0e048a9f9bb4ab444689.

## Precise experiment
Take joint-label histograms H in Q^{mn}_{>=0}, m,n>=2, and let A(H) be all row and column marginals. Each one-step experiment applies a known *strictly positive symmetric doubly-stochastic rational* K to an independent exact copy of the same H, and reads the complete **expectation** marginal vector AKH. No fixed bound is imposed on integer path counts. This auxiliary label model does not assert a native six-dimensional Cell representation.

## Sharp theorem
The least number of one-step experiments needed to reconstruct every possible H from AH and AK_1H,...,AK_qH is exactly

$$q_{\min}=\left\lceil\frac{(m-1)(n-1)}{m+n-2}\right\rceil.$$

The bound is achievable with all K_j strictly positive, rational, symmetric and doubly stochastic, hence reversible for a common uniform stationary distribution. In particular **3×3 requires only one experiment** if the complete marginal vector is read.

**Lower bound:** W=ker(A) has dimension r=(m-1)(n-1). For h in W, mass conservation implies AKh has both row-total and column-total zero, so at most s=m+n-2 independent output coordinates are possible. q experiments have rank <=qs on W. If qs<r, choose a nonzero rational Z killed by A and every AK_j, clear denominators and add it to a sufficiently large constant nonnegative integer H. Two different nonnegative integer H share all declared observations. Thus q>=ceil(r/s).

**Explicit construction:** Use mutually orthogonal integral zero-sum vectors
u_i=(1,...,1,-i,0,...,0) in Z^m (i initial ones, 1<=i<m) and analogous v_j in Z^n. The r hidden basis vectors are X_{ij}=u_i tensor v_j; the s visible zero-total basis vectors are Y_i^R=u_i tensor 1_n and Y_j^C=1_m tensor v_j. X and Y are orthogonal, and the A Y vectors are nonzero and pairwise orthogonal. Order X_1,...,X_r and Y_1,...,Y_s. Divide X into consecutive batches of at most s elements. For batch b put

$$E_b=\sum_{a=1}^{\min(s,r-(b-1)s)}(X_{(b-1)s+a}Y_a^T+Y_aX_{(b-1)s+a}^T).$$

Let N=mn, B=max_{b,i,j}|(E_b)_{ij}|, eps=1/[2N(B+1)], J=1_N1_N^T/N and K_b=J+eps E_b. Every E_b is symmetric with E_b1=0; consequently each K_b is symmetric/doubly stochastic and every entry exceeds 1/(2N). It is a strictly positive reversible Markov kernel with rational probabilities.

For h in W, J h=0 and all Y_a^T h=0, so

$$AK_bh=\varepsilon\sum_a AY_a\,\langle X_{(b-1)s+a},h\rangle.$$

Orthogonality gives the coefficient formula

$$\langle X_{(b-1)s+a},h\rangle=\frac{\langle AY_a,AK_bh\rangle}{\varepsilon\|AY_a\|^2}.$$

Given input marginals R,C and total M, define the rational baseline (H_0)_{ij}=R_i/n+C_j/m-M/(mn). Then AH_0=AH and h=H-H_0 lies in W. Measurements of AK_bH yield AK_bh by subtracting computable AK_bH_0. Since X is an orthogonal basis, recover

$$H=H_0+\sum_t\frac{\langle X_t,h\rangle}{\|X_t\|^2}X_t.$$

This constructs the inverse, proving the upper bound and the theorem.

## Exact 3×3 witness
Choose u_1=v_1=(1,-1,0), u_2=v_2=(1,1,-2), X=(u1⊗v1,u1⊗v2,u2⊗v1,u2⊗v2), Y=(u1⊗1,u2⊗1,1⊗v1,1⊗v2). The single explicit kernel

$$K=J+\frac1{1000}\sum_{i=1}^4(X_iY_i^T+Y_iX_i^T)$$

has min entry 107/1125 and max entry 277/2250, is symmetric doubly stochastic, and rank([A;AK])=9 versus rank(A)=5. For H=E00+E11 and H'=E01+E10, AH=AH' but AK(H-H')=(3/250,-3/250,0;0,0,0).

## Verification and limits
Exact SymPy tests: six sizes (2×2,2×3,3×3,3×4,4×4,5×5), 72 integer reconstructions, algebraic rank, stochasticity, positivity and orthogonality. An independent standard-library Fraction solver verified 100 further 3×3 reconstructions and the witness. See reproducible source/certificate in this research namespace, and the conversation archive ZIP. Finite checks are evidence, **not** a substitute for the general proof. No independent mathematical review, formal Lean proof, or native BRC transport call was performed.

**Relation to previous result:** R5 controlled-swap tomography required (m-1)(n-1) probes under a narrower interface with *one new scalar per probe* and restricted two-branch swaps. Full-vector observations and unrestricted rational reversible kernels explain the sharper q_min here; the theorems are not contradictory.

**Typed BRC reuse:** REUSE_APPLIED: existing finite-positive-rational branch mass conservation and observer/provenance discipline. Kernel columns admit a mathematical positive branch decomposition; a state-indexed native BRC realization and original path-identity preservation are unverified. Negative coordinates appear only in differences/linear proof, never as negative branch probabilities. P000's six-dimensional native Cell, 120-degree orthogonality, triadic balance, separate time typing remain assumptions; the m×n label chart is no native two-dimensional plane and has no automatic X6 embedding.

**Next exact unit:** For the actual typed source-indexed BRC kernel family, determine attainable interaction-to-marginal rank per operation under source-provenance and reset constraints; derive a matching lower bound and constructive exact certificate. No transfer to native six-dimensional dynamics until admissible address, branch, readout, and future-operation maps are proved.

Background: P. Buchholz (1994), Exact and ordinary lumpability in finite Markov chains, DOI 10.2307/3215235; B. Geiger & C. Temmel (2012), arXiv:1212.4375. These are conceptual prior art, not independent verification of this construction.
