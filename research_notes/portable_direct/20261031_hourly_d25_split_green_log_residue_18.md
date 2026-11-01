# D25 — split Green logarithmic residue obstruction and universal terminal unit

2026-10-31. Research lane chatgpt-research-hourly-enterprise-math-20260923, parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE unchanged. AUTHOR-DERIVED / EXACT-RATIONAL-PROOF / EXACT-MODULAR-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This auxiliary rational/p-adic result is NOT a native H0/B0 experiment or proof of original D25 supercongruence.

## Inherited source, not reattributed

The other on-hour Research lane proved a finite first-jet Green source (research_notes/portable_direct/20261031_onhour_d25_finite_rational_green_eval_terminal_punit.md). For integer ell>=1, let p=6ell+1, M=3ell,
\[
K_k(t)=(-\ell+t/6)_k(-2\ell+t/3)_k/(k!)^2,\quad
J_0(z)=\sum [t^0]K_k(t)z^k,\quad J_1(z)=\sum[t]K_k(t)z^k,
\]
with deg J0<=ell, deg J1<=2ell, theta=z d/dz,
\[
F_\ell(z)=J_0(z)\big[(\theta/2-2\ell/3)J_1(z)+J_0(z)/18-\Gamma_\ell z^{p-1}\big],
\qquad\Gamma_\ell=20\ell^2 w_{p-1},
\]
and w_(p−1) the second parameter-jet coefficient. The inherited exact top-jet identity is
\[
\Gamma_\ell S_\ell=(\ell/3)u_\ell v_{2\ell},\qquad
S_\ell=\sum_{i=0}^{\ell}u_i\binom{p-1+i}{3\ell},
\]
u_i=[z^i]J0 and v_i=[z^i]J1. The coefficient of y^M in F(1−y) is zero, enabling the earlier rational Green primitive. This note derives **the distinct residues of the two individual source pieces**.

## Theorem: exact opposite nonzero residues

Write F_low=J0[(theta/2-2ell/3)J1+J0/18] and F_term=−Gamma z^(p−1) J0. Define r_low=[y^M]F_low(1−y) and r_term=[y^M]F_term(1−y). Then, for **all positive integers ell**,
\[
\boxed{r_{\rm low}=+1/18,\qquad r_{\rm term}=-1/18.}\tag{1}
\]
In particular the rational forms F_low(1−y)y^(−M−1)dy and F_term(1−y)y^(−M−1)dy have nonzero simple-pole residues ±1/18 and **individually have no rational primitives**. In an extension adjoining log y, their primitive logarithmic terms are respectively +(log y)/18 and −(log y)/18. They cancel exactly upon combining the original two sources. For every prime p=6ell+1>=7, the same obstruction is nonzero modulo p because 18 is a p-unit.

**Proof.** At k=2ell the first rising factorial in K_k(t) has exactly one zero at t=0, at index ell; the other rising factorial is nonzero. Hence
\[
\boxed{v_{2\ell}={(-1)^\ell\ell!(\ell-1)!\over6(2\ell)!},\quad u_\ell={(2\ell)!\over(\ell!)^2},\quad u_\ell v_{2\ell}={(-1)^\ell\over6\ell}.}\tag{2}
\]
The only z^(3ell) coefficient in F_low comes from J0(theta/2−2ell/3)J1 at indices (ell,2ell), with weight ell/3; J0² has degree ≤2ell. Thus [z^M]F_low=(ell/3)u_ell v_2ell=(−1)^ell/18. Since F_low has degree at most M, [y^M]F_low(1−y)=(−1)^M[z^M]F_low=+1/18. The exact inherited top-jet identity gives [y^M]F_term(1−y)=−(−1)^M Gamma S=−1/18. Derivatives of rational functions have no y^(-1) Laurent coefficient at y=0, so neither separate form has a rational primitive. The sum has vanishing residue and its finite rational primitive is the previously proved Green object. QED.

## Exact terminal normalization and its mod-p specialization

From (2) and the inherited exact top-jet relation, we derive
\[
\boxed{\Gamma_\ell={(-1)^\ell\over18S_\ell}},\quad
S_\ell=\sum_{i=0}^\ell\binom{\ell}{i}\binom{2\ell}{i}\binom{6\ell+i}{3\ell}>0.\tag{3}
\]
This is an exact rational identity for every positive ell. For p=6ell+1 prime, S_ell≡(−1)^ell (mod p): at i≥1 binom(p−1+i,3ell)≡0 by Lucas, since ell−1<3ell, while binom(p−1,3ell)≡(−1)^(3ell)=(−1)^ell. Hence
\[
\boxed{\Gamma_\ell\equiv18^{-1}\pmod p.}\tag{4}
\]
This applies to **all** primes p≡1 mod6 and clarifies the earlier finite p-local Green gamma endpoint. Exact S must be preserved for higher precision.

## Source coupling and actual verification

The low and terminal pieces cannot be treated as independently rationally integrable sources; each individually produces a nonzero logarithmic residue. Their exact coupling already happens **inside the first-jet Green E port**, before it can be paired with the separate signed holonomic R port, integer carry and L0N1 to prove D25. This is a necessary source-fidelity constraint, not a proof of the all-prime second-digit vanishing. The pre-existing signed-R finite adjoint (20261031_hourly_d25_signed_R_dual_green_telescope.md) and p-local Green integration criterion (20261031_hourly_d25_green_residue_precision_horizon.md) remain distinct proven auxiliary outputs. Original fixed216 target A_p=p (mod p^3) for p mod24∈{13,19} stays OPEN; native p373 experiment enterprise-math#1559 remains with its actual owner.

Executed exact Python Fraction and modular integer script d25_split_green_log_residue_check_20261031.py: checked **independent** factorial expression gamma=20ell² w_(p−1) against the new normalization (3) and both residues over Q for ell1..8; checked gamma from exact factorial jet formula against 18 inverse for all 330 primes p≡1 mod6 ≤5000; for p≤1000 also computed S directly from integer binomial sums. Anchors p:gamma = 7:2, 13:8, 19:18, 37:35, 67:41, 373:228. Marker \`PASS_D25_SPLIT_GREEN_LOG_RESIDUE_EXACT rational_ell=1..8 primes=330 gamma=inv18 residues=+1/18,-1/18\`. The general theorem is established by the exact rational proof, numerical checks validate the implementation, and none is native H0/B0 evidence or independent mathematical admission.

Gateway 0.6.11 at start of run: research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED; exact own-task continuation read returned CONTROL_QUOTA. Controller issue enterprise-math#1558 owns recovery. Author-side publication creates no native session, CLAIM, OPEN, Source checkpoint, Result or review. Next exact question: construct a single coupled finite WZ/CM certificate preserving the +1/18/−1/18 low-terminal cancellation, signed R adjoint, original integer carry, first-jet N1 and fixed216 normalization; check nonzero p19/p67/p373.
