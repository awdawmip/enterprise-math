# D25 — exact Gauss second-jet Green carry, nonremovable terminal

2026-10-31 Asia/Hong_Kong. **AUTHOR-SIDE / PROVED ALGEBRAIC IDENTITY / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Logical research lane: `chatgpt-research-onhour-enterprise-math-20260923`, separate from CONTROL_PLANE_MAINTENANCE. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. P000 ACTIVE_LOCKED / ACTIVE worldview unchanged. This is external p-adic algebra, **NOT** original H0/B0 native execution, full LIFT or Source Result.

## Input / precise unresolved question

Reuse the established top-parameter Clausen jets and signed unique-overdegree identification from `research_notes/portable_direct/20261031_onhour_d25_clausen_jet_unique_overdegree_R.md`, commit `3380c77a4d5c5556d7c63698c274e8a5f537aa55`, without recrediting them. The full original question remains
[
A_p=sum_{n=0}^{p-1}(6n+1)inom{2n}{n}^2inom{3n}{n}/216^n
stackrel?{equiv}ppmod{p^3},qquad pequiv13,19pmod{24}.
]
For prime `p=6l+1>=7`, let `theta=z*d/dz` and
[
K_k(t)=rac{(-l+t/6)_k(-2l+t/3)_k}{(k!)^2},quad
J_r(z)=sum_{k=0}^{p-1}[t^r]K_k(t)z^k,quad r=0,1,2.
]
The parameter `t` is *formal*, not Enterprise native time. Previously established support: `deg J0<=l, deg J1<=2l, deg J2<=p-1`.

## Theorem 1 — EXACT second-jet Gauss differential system

Set `L0=theta^2-z(theta-l)(theta-2l)` and `D=theta/2-2l/3`. **Exact polynomial equalities over Q** are
[
L_0J_0=0,qquad L_0J_1=zDJ_0,qquad
oxed{L_0J_2=zDJ_1+rac z{18}J_0-gamma_p z^p}.
]
Here (gamma_p=20l^2w_{p-1}), with the *previously sourced* quadratic cross-wall coefficient
[
w_{p-1}=rac{(-1)^l l!(2l)!(5l-1)!(4l-1)!}{18((6l)!)^2}.
]
For **every** prime `p=6l+1>=7`, (gamma_pinmathbb Z_{(p)}^	imes), because every factorial argument is smaller than p, l is a unit and 18 is a unit. Hence dropping the terminal (-gamma_p z^p) produces an identity **false even mod p**, for every such prime. This only rules out the terminal-free second-jet shortcut, not all WZ/CM approaches.

*Complete proof.* The exact recurrence is
[
k^2K_k(t)=(k-1-l+t/6)(k-1-2l+t/3)K_{k-1}(t).
]
Writing (F(t,z)=sum_{k=0}^{p-1}K_k(t)z^k) gives
[
L_tF=-z^p(p-1-l+t/6)(p-1-2l+t/3)K_{p-1}(t)
]
and direct multiplication gives (displaystyle L_t=L_0-tzD-t^2z/18) (the constant of D is (-2l/3), **not** (-l/2)). Two terminating zero factors imply (K_{p-1}(t)=t^2w_{p-1}+O(t^3)). Comparing t^0,t^1,t^2 and ((p-1-l)(p-1-2l)=20l^2) proves all displayed formulas. QED.

## Theorem 2 — exact signed adjoint Green identity AND nontrivial p carry

Define
[
Phi(z)=z(1-z)^{-3l}(J_0J_2'-J_2J_0'),quad
{cal L}_p=[z^{p-1}](1-z)^{-3l-1}J_0(DJ_1+J_0/18),quad
{cal G}_p=[z^p]Phi.
]
Then, **as an exact rational equality in (mathbb Z_{(p)})**,
[
oxed{mathcal L_p-gamma_p=pmathcal G_p}.
]
Consequently ({cal L}_pequivgamma_ppmod p), and the quotient is legitimate:
[
oxed{({cal L}_p-gamma_p)/pequiv{cal G}_ppmod p}.
]
A fully finite source-faithful expression of the left hand side is
[
{cal L}_p=!!sum_{substack{0le ile l\0le jle2l\i+jle p-1}}
inom{3l+p-1-i-j}{p-1-i-j}u_i
left[left(rac j2-rac{2l}{3}ight)v_j+rac{u_j}{18}ight]
]
with (u_i=[t^0]K_i(t), v_j=[t^1]K_j(t)). This source sum uses only the first two jets, while the right hand side keeps the original **signed** J2 Wronskian current.

*Complete proof.* The differential form of ((L_0/z)y) is
[
z(1-z)y''+[1+(3l-1)z]y'-2l^2y.
]
Its integrating factor is (mu=(1-z)^{-3l-1}), since ((mu z(1-z))'=mu[1+(3l-1)z]). Multiply the J2 equation by (mu J_0/z), multiply the homogeneous J0 equation by (mu J_2/z), and subtract. Terms in y cancel and give the exact *formal power series* Green identity
[
Phi'(z)=(1-z)^{-3l-1}J_0(z)
ig(DJ_1(z)+J_0(z)/18-gamma_p z^{p-1}ig).
]
Take ([z^{p-1}]). The left side is (p[z^p]Phi=pmathcal G_p). The rightmost term contributes exactly (-gamma_p) because (J_0(0)=1). This proves the identity **before** any division by p. All coefficients of the terms are p-local units/integer binomials; (mathcal G_pinmathbb Z_{(p)}). QED.

## Actually executed exact check and observer fidelity

Executed `d25_gauss_jet_green_carry_20261031.py` with Python standard-library integer modular arithmetic on **all 45 primes `7<=p<=500`, `p=1 (mod6)`**. At each prime: independent coefficient recurrence modulo p² for each jet, all three differential equations for degrees 0..p, separate original factorial terminal, and two distinct signed finite sums for (mathcal L_p) and (mathcal G_p), verifying the exact carry modulo p². All passed. Rows `(p,gamma modp,L modp,G modp)`:
`(7,2,2,2), (13,8,8,12), (19,18,18,6), (37,35,35,9), (67,41,41,47), (373,228,228,50)`.
Marker `PASS_D25_GAUSS_JET_GREEN_P_CARRY_EXACT`. Universal scope comes from the proof, finite tests only corroborate the implementation.

**BRC COMPOSE_APPLIED**, not name-only: population `(p,l,k,formal-jet-order,original-index,source,weight,valuation,top-terminal)`; operators `theta, signed Wronskian, coefficient extraction, p-division after exact divisibility`. The lower forcing, nonzero terminal (gamma_p), and Green carry (mathcal G_p) remain separate. For p=373 the terminal/forcing residue is 228, the Green carry is 50, while the preexisting distinct Clausen signed overdegree (mathbf{R}_{373}=196). **This new Green current is not identified with R or native Green/Hesse.** No information-loss certificate covers such a collapse or native X6 transfer.

## Current source frontier / one exact next action

The frozen original p³ congruence and its four-source cancellation remain **OPEN**. Next: construct a finite p-local *evaluation adjoint at z=1/2* transporting the above Green source and terminal to the full original signed Clausen lower-jet obstruction, explicitly testing p19/p67/p373 and keeping both gamma and Green carry. Do not silently equate (mathcal G_p) and (mathbf R_p).

Native issue `awdawmip/enterprise-math#1559` (read 2026-10-31) is OPEN with no confirmed executor: fixed373 original H0/B0 divided-power [X]U modulo139129, module rank, semilinear Frobenius/eta, signed Green/Hesse, kappa and independent replay **NOT_EXECUTED**. Own Research lane recovery `awdawmip/kimi-query-bridge#6632`: no own claim/run and source_authority_verified=false; original dispatch `#6633` terminal FAILED/UPSTREAM_CODE_REVIEW_REQUIRED. No mutation was retried, no maintenance identity used, and no Source-native checkpoint, Result, review or formal admission is asserted. Historical staging remains separate. Original recurring task unchanged.
