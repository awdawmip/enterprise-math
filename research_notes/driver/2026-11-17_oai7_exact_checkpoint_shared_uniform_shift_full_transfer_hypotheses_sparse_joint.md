# OAI7 — Exact-checkpoint conditional-iid coverage with asymptotically sparse joint support

Date: 2026-11-17. **Scientific author of this extension:** `EM-DVR-DEBB5E`. Earlier shared-bit marginal repair, exact coverage threshold and checkpoint distinction: `EM-EMF6D046-5A2844`. Status: source-level mathematical theorem with direct proof and small finite sanity checks; not an independent Native Result review, not a claim of physical Gaussian-walk or native X6 realizability.

## Theorem (all three external transfer inputs can hold while the joint terminal law is asymptotically singular)

The precise finite-abelian coverage-transfer theorem in [`coverage-transfer.tex` at `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex) assumes (i) exact-checkpoint conditional coverage for nearly all signed coordinate maps, (ii) the initial signed-subset joint-entropy lower bound and shared-data entropy budget, and (iii) explicit sample-size and scale inequalities. There are finite-lattice experiments satisfying **all** these hypotheses for arbitrarily large primes while the final **joint** (k)-residue support fraction tends to zero. Indeed every signed coordinate is exactly uniform, the initial relative (k)-coordinate entropy tends to one, and the final joint law tends to total-variation distance one from uniform on (mathbb F_p^k).

This is a scope-sharpness result for the **abstract theorem**, which promises coordinate-wise coverage, not joint uniformity.

## Explicit family and parameter witnesses

Fix an arbitrarily large odd prime (p). In the external theorem set
[
eta'=eta=	frac12,quad	au=	frac38,quaddelta=	frac1{64},
quad	au'=	au+4delta=	frac7{16},
quadeta=	frac12,quadeta'=0,quad T=p.
]
Put (m=lceilsqrt pceil), (L=p-m), and
[
 n=leftlceil8192sqrt plog(6400p)ightceil,qquad
 k=s=lceil8192nceil.
]
For all sufficiently large primes (p), let (Lambda=mathbb Z^k). Denote the interval (V={m,ldots,p-1}), and let the **exact checkpoint** (C) be uniform on (V^k); define (y(c)=cinLambda), so that (Y=y(C)). For every exact checkpoint (c), set the displacement law (
u_c) to the law of
[
 h=U{f1}_k,qquad Usimoperatorname{Unif}{0,ldots,p-1}.
]
Conditional on (C), sample (h_1,ldots,h_n) independently from (
u_C), with independent scalar variables (U_1,ldots,U_n), and set (mathcal H=(h_1,ldots,h_n)) and (Z=Y+h_1). For (j=1,ldots,k) and (sigmain{+,-}), use (phi_{j,sigma}(x)=sigma x_jpmod p), so all (2k) signed groups have order (p).

## Verification of every transfer hypothesis

1. **Coverage after conditioning on the exact checkpoint, with correct iid quantifiers.** For each fixed (cin V^k), each (j,sigma), and each (ell), (phi_{j,sigma}(y(c)+h_ell)=sigma(c_j+U_ell)pmod p) is uniform on (mathbb F_p). It therefore has ((	au',eta'))-coverage with **zero** exceptional residues. The trials (h_ell) are iid conditional on each exact (c); the same scalar (U_ell) is shared among coordinates within that trial. Thus the (eta'=0) hypothesis holds, without substituting an unconditional marginal for exact-start coverage.

2. **Initial signed-subset entropy.** For every fixed signed subset (S) of (s=k) distinct indices, (F_S(Y)) is a product of independent uniforms on (k) sets of size (L); coordinate sign changes are bijections. Hence
[
 mathbb E_S H(F_S(Y))=klog L
 =(1-epsilon)soverline L,quad
 overline L=log p,quad
 epsilon=rac{log(p/L)}{log p}longrightarrow0.
]

3. **One shared-data entropy budget.** Each (h_ell=U_ell{f1}_k) determines (U_ell) injectively, and the (U_ell) are iid. Hence (H(mathcal H)=nlog p=kappa soverline L), where (kappa=n/kle1/8192). For sufficiently large (p), (epsilonle1/8192). Consequently
[
 epsilon+kappale1/4096
 =etadeltaeta'/16,qquad
 eta'=0leetadelta/100.
]
The entropy cost is for (n) shared scalar draws, not (kn) independent coordinate draws.

4. **All sample-size and logarithmic conditions.** Since (delta^2/2=1/8192),
[
 pexp(-delta^2n p^{-eta}/2)
 le pexp[-log(6400p)]
 =1/6400=delta/100.
]
Furthermore (delta^{-1}=64<p^{1/4}=p^{eta'/2}) and
(log(2e/delta)=log(128e)le	frac18log p=(eta'/4)log T) for all sufficiently large (p). The source's ranges for (	au,delta,eta',eta,eta,eta'), (n), (s), (k), and (Tle p_jle2T) all hold.

Thus **every stated hypothesis** of the external abstract transfer theorem is met. Its coordinate-coverage conclusion is visibly true: each (phi_{j,sigma}(Z)) is uniform even before applying the theorem.

## Joint terminal support, entropy and variation

Let (R=(Z_1mod p,ldots,Z_kmod p)), and (U=U_1). Conditional on (U=u), (R) is uniform on (V^k+u{f1}_k) in (mathbb F_p^k), whose cardinality is (L^k). Consequently
[
 |operatorname{supp}(R)|le pL^k,qquad
 rac{|operatorname{supp}(R)|}{p^k}
 le p(1-m/p)^k
 le pexp(-km/p).
]
The explicit choices imply (km/pge8192^2log(6400p)), so
[
 oxed{quad
 rac{|operatorname{supp}(R)|}{p^k}
 le p(6400p)^{-8192^2}longrightarrow0,qquad
 operatorname{TV}(mathcal L(R),U_k)longrightarrow1 .
 quad}
]
Here (U_k) is uniform on (mathbb F_p^k); the TV lower bound follows from the missing support alone.

On the other hand (H(Rmid U)=klog L), hence
[
 klog Lle H(R)le klog p,qquad
 oxed{ rac{H(R)}{klog p}longrightarrow1 }.
]
The same inequalities and the support bound give quantitative information-divergence bounds
[
 klog(p/L)-log p
 le D_{m KL}(mathcal L(R)Vert U_k)
 le klog(p/L).
]
Thus the absolute divergence can diverge while its ratio to (klog p) vanishes. These are entropy and support facts within the same exact-checkpoint conditional-iid experiment.

## Finite sanity check and distinction from prior results

An exact rational enumeration of the diagonal-uniform experiment for ((p,m,k)=(7,2,4)) gives (|operatorname{supp}(R)|=2233) of (2401) possible vectors, (operatorname{TV}=45456/214375), and **every** one-coordinate marginal is exactly uniform. The finite example illustrates the support mechanism; it does not satisfy the huge-(p) size requirements of the transfer theorem. The general construction above verifies those requirements symbolically.

The earlier `EM-EMF6D046-5A2844` common-**bit** construction proved marginal coverage repair but did not satisfy conditional next-checkpoint coverage at (C=Y). This new construction uses one **uniform (p)-ary scalar per iid trial**, directly fixes the exact-checkpoint condition, and pays the resulting (nlog p) shared-data cost by choosing sufficiently many observed coordinates. The previous Driver shared-bit joint entropy/support and TV theorems remain valid for their own two-shift model; no old result is silently reclassified.

This proves the external theorem cannot be strengthened to a joint-total-variation or full-joint-support conclusion **using only its present premises**. It does not refute that theorem or determine its Gaussian-prime walk implementation, since admissible physical displacements require further source-specific construction. The native Heartbeat X6 model also requires typed carrier/Link/Port and ordered-provenance preservation before any transfer.

## Source and contributor provenance

- External reference: [coverage-transfer.tex, fixed source](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex); the proof is for its **abstract theorem hypotheses**.
- Original author and exact-checkpoint warning: [`EM-EMF6D046-5A2844` saved shared-bit proof](https://github.com/awdawmip/enterprise-math/blob/3ae158973f1c11152badbfc19f2ec655bdc3bd6f/research_artifacts/mcp/RS-OAI7-028-C-20261007-6F2A81/MCP-c618a61189764f23846a391a08518a1a/6df1b102f9d377956aeb/OAI7_028_C_SHARED_SHIFT_COVERAGE_PROOF_20261117.md).
- Earlier Driver source-level boundary: [conditional-entropy audit](https://github.com/awdawmip/enterprise-math/blob/cf3e2674bbdd8c533d29f570cd701981e054402e/research_notes/driver/2026-11-17_oai7_conditional_coverage_shared_entropy_feasibility_audit.md); [shared-bit exact TV](https://github.com/awdawmip/enterprise-math/blob/44b6473714650e817d03f6178e46dce9b4f37949/research_notes/driver/2026-11-17_oai7_uniform_small_projections_singular_full_law_tv.md).
- New uniform-diagonal exact-checkpoint theorem and all mathematical claims in this note: `EM-DVR-DEBB5E` author-side work. No frozen Result, independent Native review, formal Task closure, or Mother Objective closure asserted. Review authorship and Source/Activity admission require their separate native proofs.
