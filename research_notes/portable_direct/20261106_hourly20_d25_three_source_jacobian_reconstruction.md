# D25 — three-source first-jet observability and exceptional weighted-coordinate repair

Date: 2026-11-06. Status: **AUTHOR-PROVED algebra / finite exact check (206 primes) / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`; frozen scientific input: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Prior author context: `research_notes/portable_direct/20261106_hourly20_d25_first_jet_original_216_source_port.md`. This result concerns a *declared coefficient-level first-jet observer*, not the native original-class H0/B0, Frobenius/eta/kappa, or the still-open universal Theta identity.

## Theorem A: source-wise linearized coefficient readout has full rank three

Let `p=6m+1` be prime, `p>=13`, `s=(2m,3m,4m)`, and `F_p=Z/pZ`. For `1<=j<=2m` and formal infinitesimal `x=(x_1,x_2,x_3)` define

`U_j(x)=(-1/2)^j prod_{i=1}^3 binom(s_i+x_i,j)`, `u_j=U_j(0) !=0` in `F_p`, and `h_i(j)=sum_{r=0}^{j-1}(s_i-r)^(-1)`.

The linearized normalized source readout is
`delta_j(x)=u_j^(-1)*dU_j(x)|_{x=0}=sum_i h_i(j)x_i`.

For `j=1,2,3`, the Jacobian `J=[h_i(j)]_{j=1,2,3;i=1,2,3}` is invertible in `F_p`.

**Proof.** Subtract each preceding row from its successor (in descending order). The resulting rows are
`C_{r,i}=(s_i-r)^(-1)`, `r=0,1,2`. This is a Cauchy matrix. Its determinant, up to sign, is
`prod_{i<k}(s_k-s_i)*prod_{r<t}(t-r)/prod_{i,r}(s_i-r)`.
Every factor is a p-unit: the three `s_i` are distinct and in `[2m,4m]`, `0,1,2<2m` (because `m>=2`), and `p>=13`. Thus `det J !=0`. QED.

A constructive inverse is particularly simple. For `y_j=delta_j(x)`, put
`gamma_0=y_1`, `gamma_1=y_2-y_1`, `gamma_2=y_3-y_2`;
`Q(z)=prod_i(s_i-z)`. Interpolate the unique quadratic `P` with
`P(r)=Q(r)*gamma_r` for `r=0,1,2` using three-point Lagrange interpolation, and recover each source coefficient by
`x_i=P(s_i)/prod_{k!=i}(s_k-s_i)`.
This is an exact finite-field inverse, not numerical reconstruction.

## Theorem B: the weighted coefficient observer retains rank three after one index repair

The D25 signed weighted coefficient readout is
`Y_j(x)=(6j+1)U_j(x)`. Its first-jet row is `(6j+1)u_j[h_i(j)]_i`.
For `p>=31`, rows `j=(1,2,3)` have nonzero weights and constitute an invertible 3x3 map. For `p=13`, use rows `j=(1,3,4)` (normalized determinant `12 mod 13`). For `p=19`, use `j=(1,2,4)` (normalized determinant `2 mod 19`). Each selected row has `u_j(6j+1)!=0`.

**Proof.** For primes `p>=31`, `m>=5` and the exceptional weight-zero index `j=m` does not occur among `1,2,3`; Theorem A applies after multiplying by three invertible row scalars. The only remaining prime cases `13,19` are verified by the explicit rational-harmonic 3x3 determinants above, with all denominators invertible. QED.

**Scoped information-loss witness.** Taking the distinct source perturbation `x=(2m,-3m,0)` gives `delta_1=0` but
`delta_2=(3m-2m)/[(2m-1)(3m-1)] !=0 mod p`.
Consequently the first single coefficient observer alone cannot reconstruct the three source directions. The full coefficient-level first-jet family has *minimal source dimension three* for linear lossless representations. This does not conflict with an independently proved scalar final-`B` expression using one directional derivative; different observers have different retention obligations.

## Executed exact certificate

The adjacent `d25_source_jacobian_reconstruction_20261106.py` uses integer binomials, modular inverses, finite-field Gaussian determinants and Lagrange recovery. All **206** primes `p=1 mod 6`, `13<=p<=3000` passed: rank three, nonzero weighted chosen coordinates, and the explicit Cauchy inverse for `p>=31` (204 primes). Spot-check normalized determinants: `p13:12`, `p19:2`, `p31:27`, `p373:71`, `p1009:649`. Single-coordinate loss witnesses: at `p13,p19,p373`, `delta_1=0` and `delta_2=1,11,31` respectively.

No numerical check is used as the all-prime proof: Theorems A and B follow from the Cauchy determinant and the two exact boundary computations. This is an ordinary finite-field coefficient/observer result, not a claim that the Enterprise six-axis spatial theory has been formally instantiated.

## Research continuation

Mother objective remains `Delta_p-R_p=0 (mod p)`, `p=13,19 (mod 24)`. This unit supplies a source-faithful witness and a three-coordinate reconstruction interface for subsequent signed telescope construction. Next: apply the 3-direction inverse to the *specific* regular/one-carry first-order source expressions in the current pinned D25 input; inspect whether the final scalar Theta observes a particular kernel subspace, keeping the original-class p373 H0/B0 and independently owned four-channel second-digit work separate. Do not treat the invertible source map as a proof of `Theta=0` or as a native Source checkpoint; no owner claim, run authorization or review is asserted.
