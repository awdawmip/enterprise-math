# RH L5: explicit Weil-form normalization and fixed-window transfer (2026-11-16)
Formal task: RS-RH-WEIL-L5-SCHUR-CERT / TP2-836A025740E28C349B4D.
Provenance: derived directly from Hongmin Li's published-in-rStation 2026-10-23 manuscript at https://rstation.ai/problems/riemann_hypothesis/papers/45/v1 ; exact Source section 2, Theorem 1.1, source Sections 3-7; no independent reproduction of its full certificate performed here.

Define D_a=C_c^infty((-a,a),C). Adopt Li's Fourier convention fhat(t)=int_R f(x) exp(-itx) dx, C_f(u)=int_R f(x+u) overline(f(x)) dx, and exact quadratic form
  Q(f)=(1/(2*pi))int_R [Re psi(1/4+it/2)-log pi] |fhat(t)|^2 dt
        +2 Re[fhat(i/2) overline(fhat(-i/2))]
        -2 sum_{n>=2} Lambda(n)/sqrt(n) Re C_f(log n).
Every term depends on the test function f only: a is a restriction of admissible support, not an independent coefficient. Thus for any 0<a<=b, restriction Q|_{D_a} equals Q|_{D_b}. The norm ||f||_{L2(R)} is likewise identical under zero extension.

Li Theorem 1.1 (source CLAIM, not independently replayed here): for a_*=(log 11)/2=1.198947... both parity restrictions of the full closed Friedrichs realization A_{a_*} have strictly positive spectral infima. The paper gives a full-domain form comparison (4.8), retains signed negative odd pole term in (2.2), completes square on the whole complement in (4.9), and uses interval arithmetic with 400 retained modes, 350 responses, 8000 tail cutoff, 256-bit Arb in section 7. The published claim is a computer-assisted theorem with reproducibility supplement; no independent end-to-end certificate from this author was produced.

Exact transfer theorem:
If Q(f)>=c_* ||f||_2^2 for every f in D_{a_*}, for some c_*>0 (this is what positivity of the same closed A_{a_*} gives), then for EVERY real L in [4/5,(log 5)/2] and every f in D_L,
  Q(f)>=c_* ||f||_2^2.
Reason: log5<log11, so L<=log5/2<log11/2=a_*. D_L subset D_{a_*}; the quadratic form Q and norm are literally unchanged by restriction. For the parity sectors: reflection commutes with Q and the restriction map. The even/odd D_L subspaces inject into matching D_{a_*} subspaces. The source theorem therefore restricts to both sectors. Under the identified closed form domain, the bound extends from the smooth compact core to the closure, by the definition of form closure. No finite samples or separate L-parameter interpolation is involved.

At the right endpoint L=log5/2, the prime-power support in Q is exactly 2,3,4 under the original strict log n < 2L convention: n=5 contributes only measure-zero boundary overlap; the next prime-power threshold does not enlarge the operator on the open compact core. This matches the 2026-09-09 project's cited active set, but the operator equivalence itself follows directly from the full formula above and the support inclusion, not from frozen finite matrices.

Mathematical status:
(a) The above fixed-window transfer is a complete elementary argument, conditional on the exact external theorem's analytic and computer-assisted proof.
(b) The selected normalized full-form family and parity convention are now explicitly pinned; this removes an ambiguity left by the 2026-09-09 RH handoff.
(c) Independently verifying the external complete source, finite-certificate arithmetic, form-domain closure and all infinity tail estimates remains a separate proof-admission task; this note is neither Enterprise Math Driver review nor an accepted Result.
(d) If the external theorem has a substantial error, next action is to identify the first exact failing lemma, retain as scientific obstruction, and resume the native Schur certification at that point. Do not restate an unqualified proof of Weil L5 or RH from unverified external receipts.

Author source comparison: https://github.com/luciferyu666/certified-weil-positivity/tree/b6cd2183c1e79c6c27a34267812a7b2d73ed1b59 ; external stronger October 26 claim https://rstation.ai/problems/riemann_hypothesis/papers/60.
