# R273 research handoff — sharp six-channel local limit

**Author-side status:** ANALYTIC_ARGUMENT_COMPLETE / EXACT_SYMPY_VERIFIED / INTEGER_DP_0_TO_400 / GITHUB_BRANCH_PERSISTED / NATIVE_OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED. The conclusion is for the fixed six-channel positive ordered **auxiliary BRC** model; it is not P000 native physics.

**Verified mathematical increment.** Let \(\varphi=(1+\sqrt5)/2\), \(\sigma^2=3/2+7\sqrt5/10\). In the unchanged R268–R272 model, set \(P_n(g)=H_n((0,0),g)\), \(\Lambda_n=\max_gP_n(g)\), \(B_n=\max_g\min_{c\in C}H_n(c,g)\). This turn proves

\[
\exists N<\infty\ \forall n\ge N:\ B_n=\Lambda_n,\qquad
B_n\sim\Lambda_n\sim
\frac{\varphi^n}{5\sqrt{2\pi\sigma^2n}}.
\]

The proof does **not** produce a numerical N. An independently executed finite exact computation verifies equality at each n=12,...,400, but that observation does **not** justify replacing N by 12 universally.

**Core proof method.** Keep the full affine effect and exact positive path multiplicities. Change mark to t=epsilon*k; build 8-state no00 and 6-state unrestricted Laurent transfer matrices; prove the two exact characteristic polynomials, primitive Perron eigenvectors/projections and nonzero variance. Fourier spectral equality plus two opposite-sign selfloops excludes every peripheral frequency except θ=0,π. A lattice local limit follows uniformly in terminal state and all t, with parity factor2. Any maximizing reset effect has t=o(sqrt n). At the *same* maximizer, clean control states q1 and q2 dominate the q0 reset fiber by asymptotic factors phi and 2phi, and each dirty channel dominates on 2^n/sqrt n scale, forcing B_n=Lambda_n eventually.

**Evidence:** Full Chinese proof \`R273_SHARP_SIX_CHANNEL_RESET_LOCAL_LIMIT_AUTHOR_PROOF.zh-CN.md\`; actual executed verifier \`R273_verify_publish.py\`; \`EXACT_EVIDENCE.json\`. Local extended proof, extended executed checker and full evidence also retained in a separately linked local ZIP. Original words independently checked 8191 (length 0–12); integer DP length 0–400, exact equality 389 consecutive lengths, strict exceptions 7–11. No native \`enterprise_math\` execution, formal Lean, or P000/R193 transfer validation.

**Source provenance:** GLOBAL_KNOWLEDGE_V1 main@ad082b1ef072ce8fc4d748964b7fdfe293d84d73; pinned P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math control read main@9eb552f86709355b6fecaef69bf4cbc4b5f202ec; R271 be4d5bb132f99fd932be70201161faab7a8f334d, R272 39c4801a51850d58f75ef71c9d4721e9ed8c6316. Relevant BRC spectral antecedents R262 and R264 retain their prior **unreviewed author-side** classification. BRC tool reuse: REUSE_APPLIED + COMPOSE_APPLIED (existing ordered-positive carrier and exact Laurent transfer laws).

**Research activity:** RA-EMR3-20261025-0433-R273RESETLLT is local-client-identity registration on EM source, not native Researcher session or formal Task CLAIM. Native \`em_control_tasks\`: CONTROL_QUOTA; \`em_session_start\`: STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Owner cannot be authoritatively established, no Source Result or independent Driver review.

**Next smallest question:** find an explicit/effective N (ideally prove equality for all n≥12 via same-effect injections or coefficientwise inequality), or find an n≥12 counterexample; then calculate the exact next-order 1/n correction and optimal affine mark offsets. Separately, D(6) exact positive aggregation and R193/P000 native mapping remain open.
