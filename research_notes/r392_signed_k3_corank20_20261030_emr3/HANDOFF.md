# R392 research handoff (2026-10-30)

Goal: classify corank 20 signed K₃ BRC finite Newton PF₂; consume R391 without taking another Source owner's active task.

Theorem: C₂₀(θ) is PF₂ iff −1<θ≤η₂₀, where η₂₀ uniquely solves T₂₁=0 in (1865779/1e6,1865780/1e6), approximately 1.8657794536126395. Top coefficient c₄₀=6564120420(30−16θ)^40. At θ=15/8, T₂₁ has a fourth-order zero but T₁₈<0. Another simple crossing of T₂₁ in (1884701/1e6,1884702/1e6) occurs with c₂₁<0, so PF₂ remains false.

Reproduce: python r392_symbolic.py && python r392_certify.py in a Python+sympy environment. The first produces R392_POLYNOMIALS.json; the second produces R392_EVIDENCE.json. Actual run succeeded, 560 independent exact rational checks, 84 certificate objects, 92 rational covering intervals, 94 Bernstein calls and 4644 positive control coefficients. The expected polynomial SHA256 is 28ce55a4e7bc56648c8a755ff81e9bb9b0b6be6591031e107ff46544945e9646, certificate-control SHA256 bccc2b0c022b043230f40a4c775715ac59518d6d3fd5fd344498ba98c76de451, and generated evidence JSON SHA256 1baf83442658d128f78c9860a3cd288bbbdb285ad54f81280e27e0bd69c3b949.

Lineage: signed K/J R346_verify.py blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1; R391 PR #1708 commit cf8fadf8403eb26c7a681c07102acc4321c6efb8. Fixed global knowledge main deea36780a2a41ad266f13246db23d98ef7bcb7e and Enterprise Math main 30e4fe72a8d1d4cd7cbaa043e5868f907a69fc15. P000 and ACTIVE worldview unchanged.

Status: AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING / OWNER_UNVERIFIED. Authenticated GitHub login awdawmip; no canonical Source CLAIM/Result/Review claimed. This is a fixed finite raw-D observation, not full infinite Q, full D TP₂ or native X6 dynamics.

Next: prove/falsify all-corank parity law for critical Turán vanishing at θ=15/8, then independent Driver checks of signed original K/J, normalizations and strict Bernstein certificate leaf coverage.