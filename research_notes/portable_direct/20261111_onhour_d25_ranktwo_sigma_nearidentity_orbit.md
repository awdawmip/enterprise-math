# D25/JT2: One near-identity gauge orbit in the rank-two Frobenius p² lift fiber

Date 2026-11-11 Asia/Hong_Kong. **AUTHOR_SIDE / PROVED_IN_DECLARED_MODEL / FINITE_EXACT_EXECUTED / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.**
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; TP2-B6F4FC938FF94941C1B7. Frozen science Source c47e13e4aba0e006366f989d6334d443f6333ae3. Declared logical Research lane chatgpt-research-onhour-enterprise-math-20260923, separate from CONTROL_PLANE_MAINTENANCE; declaration is not service-issued execution authority.

## Consumed prior lemma and new theorem

Consume, without recrediting, the prior fixed-basis fiber classification from \`20261111_onhour_d25_native_ranktwo_frobenius_second_digit_fiber.md\`: for odd prime p with (2/p)=-1, in R₂=(Z/p²Z)[T]/(T²−2) with σ(T)=−T, F*=[[0,1],[p,0]], the complete set of matrices F≡F* mod p and Fσ(F)=pI mod p² is

  F(b,d)=[[-pσ(d),1+pb],[p,pd]] mod p², b,d∈R₁=F_(p²),

and has p⁴ different **fixed-basis** elements. The original proof did not classify gauge orbits.

**New theorem:** All those p⁴ matrices form **one orbit** of the near-identity change-of-basis group K₁={I+pY : Y∈M₂(R₁)}, acting by F↦G⁻¹Fσ(G). For each b,d the exact representative is

  G(b,d)=[[1−pb,0],[−pd,1]],  G(b,d)⁻¹=[[1+pb,0],[pd,1]] mod p²,

and **G(b,d)⁻¹F*σ(G(b,d))=F(b,d) mod p²**.

Moreover Stab_K₁(F*) consists *exactly* of I+p[[σ(z),v],[0,z]] for z,v∈R₁. Its size is p⁴, while |K₁|=p⁸; orbit size p⁸/p⁴=p⁴. Applicable to both p≡13,19 mod24 target classes.

**Complete proof:** Set N=F* mod p=[[0,1],[0,0]], Y=[[u,v],[w,z]]. Expand using p²=0 modulo p²:

  (I+pY)⁻¹F*σ(I+pY)=F*+p(Nσ(Y)−YN),
  Nσ(Y)−YN=[[σ(w),σ(z)−u],[0,−w]].

Choosing w=−d, z=0, u=−b, v=0 produces F(b,d). The bracket is zero precisely when w=0, u=σ(z), with independent v,z, proving the stabilizer and count. Every I+pY is invertible. QED.

**Observer consequence (BRC):** Taking the gauge orbit forgets all four F_p-valued second-digit parameters b,d but a fixed source-basis coefficient F₁₂=1+pb does vary in that orbit. At p=373, F(0,0) has F₁₂=1 and F(T,1+T) has F₁₂=1+373T mod139129; they share Fσ(F)=373I, mod373 N and explicit G. Gauge-class data can support only compatible gauge-invariant observers; any native fixed-basis [X]U or signed κ comparison needs the genuine basis/eta and covariantly transported original observer. This is a conditional rank-two matrix theorem, not an identification of the actual original H0/B0 rank/operator or the project's X6 space.

## Executed exact checks

The companion Python standard-library checker \`d25_ranktwo_sigma_gauge_orbit_20261111.py\` directly checks every one of 625 fixed-basis F(b,d) at p=5, verifies conjugacy and p²-square, and independently all 625 explicit stabilizer elements. It additionally checks exact p=13,19,373 witnesses. No floats and no native original-class H0/B0 computation. Result:

  p=5: fixed_basis_lifts=625, stabilizer=625, K1_order=390625, gauge_orbits=1;
  p=13,19,373: three explicit exact congruence witnesses PASS;
  native_h0b0_run=False.

## Highest native frontier, Source separation and next action

Actual Task/JT2 still open: original frozen Δ_p−R_p=0 modp for p≡13,19 mod24, and Issue #1559 remains OPEN/PENDING_OWNER/NATIVE_NOT_EXECUTED. Highest actual missing evidence is original same-class H0/B0 divided-power **[X]U mod139129** p=373, actual module rank, semilinear Frobenius direction and η normalization, full odd signed Green/Hesse κ, original Δ−R, independent raw rerun. An authorized native evaluator must run and publish that exact object with source/basis/operation pins; where an actual rank-two comparison is proven use explicit gauge to transport its labelled observables rather than assume a basis-free second digit. Retain p19 and both target classes for any uniform theorem. No surrogate/scalar or model computation closes this native gate.

Source exact read request \`onhour11-20261111-0406-exact-cont\` was SUCCEEDED on d437f76a2d52b617e938130c9cb9e8e61257c5a9; route PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER, execution_authorized=false, takeover_readiness=NO_LIVE_CLAIM. Own recovery_status returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED; no authenticated own claim/open run or Source native checkpoint was issued. Existing native latest_checkpoint.json source-backed blob 3401c64cc5be5bfdd99629bf79f12a2008ed0d99 is preserved, along with prior contributions, frozen pin and original request. This author-side project Git artifact does not grant a Task claim, Result, reviewer status or accepted theorem. Do not use the maintenance logical conversation identity or replay a blocked mutation.
