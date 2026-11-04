# D25: original 216 has no all-k single-term rational Gosper primitive

**Date:** 2026-11-05. **Role:** TASK_RESEARCH, author side only, lane `chatgpt-research-onhour-enterprise-math-20260923` (never maintenance). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Status **EXACT SCOPED PROOF / AUTHOR-SIDE PUBLISHED / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN**.

## Smallest next research route and exact result

The current mother question is the original LIFT `Delta_p-R_p=0 (mod p)` for `p=13,19 (mod 24)`; the already proved source-port alignment makes it equivalent to `W_p=p (mod p³)`, with
[
t_k=(6k+1)rac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3}
=(6k+1)rac{inom{2k}{k}^2inom{3k}{k}}{216^k},quad W_p=sum_{k=0}^{p-1}t_k.
]
An attractive first attempt at the as-yet-unproved finite terminal identity is direct one-index Gosper telescoping of this original *unshifted* summand. The following exact theorem eliminates that class without ruling out the genuine p-dependent terminal WZ.

**Theorem (all-k rational-antidifference no-go).** For every integer `K>=0`, there exists **no** `R(k) in Qbar(k)` defined on every integer `k>=K` for which
[
t_k=R(k+1)t_{k+1}-R(k)t_kqquad(kge K).
]

**Proof.** Directly from the original hypergeometric factors,
[
rac{t_{k+1}}{t_k}
=rac{6k+7}{6k+1}
rac{(k+1/2)(k+1/3)(k+2/3)}{2(k+1)^3}
longrightarrowrac12.
]
The positive `t_k` therefore decay exponentially; any rational `R(k)` grows at most polynomially along all sufficiently large integers, so `R(k)t_k -> 0`. Telescoping the claimed identity from `K` to `N` and sending `N->infinity` gives `sum_{k>=K} t_k = -R(K)t_K in Qbar`. The preceding finite prefix is rational; thus the entire original 216 weighted series would be algebraic. But the **established Guillera/Ramanujan evaluation** (recalled in Roman Le Lan, *Series for 1/pi arising from Cauchy product*, 2026, Lemma 2, arXiv:2604.03327, https://arxiv.org/abs/2604.03327) is
[
sum_{k=0}^infty t_k=rac{3sqrt3}{pi}.
]
As `pi` is transcendental, its nonzero algebraic multiple's reciprocal `3 sqrt(3)/pi` is transcendental: otherwise `pi=3 sqrt(3)/(3 sqrt(3)/pi)` would be algebraic. Contradiction. QED.

The source of the 1/pi evaluation is **external accepted mathematics**; this note does not claim novelty for that formula or for the classical irrationality of pi. The proved new *task-scope route conclusion* excludes rational/algebraic unshifted Gosper primitives, including any alleged certificate valid only after deleting finitely many initial terms. It does **not** exclude finite p-dependent telescopers with singular p endpoints, two-index WZ, parameter deformation, or native H0/B0.

## Executed bounded second test

The checker `d25_original216_gosper_no_go_check_20261105.py` verifies the *original* integer binomial numerator, three-Pochhammer expression and adjacent-term ratio at 30 exact rational indices. SymPy's `gosper_term` returns `None` both on the original summand and on the truly **centered terminating** candidate
[
f_n(k)=(6k+1)rac{(-3n)_k(-2n)_k(-4n)_k}{2^k(k!)^3}
]
with symbolic `n`. The centered output is only a bounded diagnostic; **no** general symbolic no-go for centered/parameter-dependent WZ follows. Independent high-precision summation reproduces `3 sqrt(3)/pi` to 45 shown digits, as a numerical implementation check, not a proof. These are actual checks, not native results.

## BRC carrier, unchanged frontier, and next executable action

BRC source-preserving routing: keep the `216` model, sign, `6k+1` weight, summation index, `p`-adic valuation, and the **finite** `p-1` endpoint distinct from the all-k analytic theorem. Do not collapse the signed upper-shell `p² T_A` or its nonzero first omitted original term `-p² U_p`.

Next **scientific action** is a *terminating*, parameter-dependent creative-telescoping ansatz on the already-proved centered half-sum's first and second p-jets, specifically aiming at `D0+S2=-T_A (mod p)` for both target residue classes. The single zero at `k=K=(p-1)/3`, nonzero boundary at `k=N+1=(p+1)/2`, and reflected 4F3 shell must be present in the SAME certificate. An ansatz failure is a local negative experiment, not a refutation of LIFT. Previous centered 3-jet, original weighted terminal, Sun/Green/CM proofs, reflected shell and source-port Delta/R equality are **consumed**, not reproduced here.

Native p373 same-original-class fixed H0/B0 divided-power `[X]U mod139129`, rank, semilinear Frobenius orientation/eta, original kappa and odd signed readout, Delta-R and independent replay remain **NOT_RUN / PENDING_OWNER**, support Issue #1559 unchanged; this no-go neither substitutes nor blocks that experiment.

Source continuation `onhour11-20261105-0558-current-cont` was read `SUCCEEDED`, `execution_authorized=false`; no own authenticated native CLAIM/open/run/checkpoint/Result was obtained. Other sessions' IDs, owners and claims are not adopted. This is an author-side repository research contribution, **UNREVIEWED / NOT_ADMITTED**, not a formally frozen Result or scientific completion.

Prior source note: `20261026_onhour_d25_native_lift_source_port_identity.md`; current exact three-jet: `20261105_onhour_d25_original_216_half_three_jet_p3.md`; weighted terminal: `20261105_onhour_d25_original_weighted_terminal_shell_bridge.md`. All frozen source pins unchanged.
