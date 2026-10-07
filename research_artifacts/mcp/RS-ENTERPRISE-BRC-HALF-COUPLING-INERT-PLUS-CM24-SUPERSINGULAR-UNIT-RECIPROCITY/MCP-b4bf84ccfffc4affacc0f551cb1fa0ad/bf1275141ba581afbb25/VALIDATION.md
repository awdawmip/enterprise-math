# CM(-24) UR: shared-context adversarial proof-interface audit

Audit classification: `SHARED_CONTEXT_NOT_BLIND_NOT_INDEPENDENT_DRIVER_REVIEW`.
Researcher context: `EM-DIRECT-49ADE6`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-SUPERSINGULAR-UNIT-RECIPROCITY`.

## Verdict and scope

`PASS_COMPLETE_PROOF_COMPOSITION`; no mathematical blocking issue was found in the final combined review of `RETURN.md` and `prior_art/APPLICABILITY_PROOF.md`. The initially outstanding actual-model applicability condition is resolved by the verified calculation summarized below. The candidate imports a proved **weighted mod-p²** theorem and translates it to precisely the current first-digit target. The translation is bidirectional and does not assume Sun A14(ii), JT0, UR or LIFT.

This audit consumed the immutable taskbook, the three frozen parent references, the original published CDLNS Theorem 1 and its supersingular-proof ending, Guillera normalization as recorded in `prior_art/IMPORT_AUDIT.md`, and the later explicit restatement in Babei–Roy–Swisher–Tobin–Tu, Theorem 2.1. It then cross-checked the complete root return and the separate applicability proof, including their exact Weierstrass-invariant calculations. CM recognition consumes the frozen accepted discriminant -24 class polynomial; no fresh numerical CM identification is made. No Source/control-plane mutation or Driver acceptance is made.

### Final combined applicability check

For the theorem's exact model `y²+xy+(t/27)y=x³`, its coefficients give `b2=1`, `b4=t/27`, `b6=t²/729`, `b8=0`. Consequently `c4=(9-8t)/9` and `Delta=t³(1-t)/27³`; no factor of 1728 is missing in the stated discriminant formula. With `s²=2`, `t=(2-s)/4`, one has `t(1-t)=1/8`, `t²=(3-2s)/8`, and

\[
j=1728(5+2s)^3/(3-2s)
 =1728(245+166s)(3+2s)
 =2417472+1707264s.
\]

Both branches therefore match the already accepted CM(-24) values exactly. Equality of these j-invariants identifies the geometric CM property needed by the theorem; it does not require asserting that the two displayed plane models are identical over the base field. The invariant algebra, denominators, good-reduction argument using the unit product `t(1-t)=1/8`, unramified quadratic field of discriminant 8, rational-unit hypotheses for `alpha=6` and `lambda=1/2`, and the two character signs all check. No target prime is excluded or silently assumed split in `Q(sqrt(2))`.

The root return's degree-by-degree finite Clausen display consumes the frozen coefficient law and valuation blocks. Its only support inference is the explicit inequality `i+j >= 6m+1 > 4m`; it does not solve anew the reflected-tail coefficient, the five deformation sums, CM0, SIMPLE or LIFT. This is within the taskbook's permission to use frozen identities to translate a candidate proof.

## 1. Exact coefficient, cutoff and derivative normalization

Write

\[
 b_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\quad
 B_k=b_k2^{-k},\quad
 F_N(z)=\sum_{k=0}^{p-1}b_kz^k,\quad \theta=z\partial_z.
\]

Then the frozen quantities are exactly

\[
 g=F_N(1/2),\qquad h=((1+12\theta)F_N)(1/2).
\]

The essential factor-of-two identity is

\[
 F_N(1+12\theta)F_N=(1+6\theta)F_N^2.
\]

The finite Clausen coefficient interface identifies the coefficients of degrees `0,...,p-1` in `F_N²` with

\[
 c_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}.
\]

Therefore, with no infinite p-adic series evaluation or truncation exchange,

\[
 gh=W_p+T_p,\qquad
 W_p=\sum_{k=0}^{p-1}(6k+1)c_k2^{-k},
\]

\[
 T_p=\sum_{\substack{0\le i,j<p\\i+j\ge p}}
 (1+6(i+j))B_iB_j.
\]

This is the exact already-frozen finite product/tail interface, merely displayed with the imported theorem's weight. Its cutoff is `p-1`, precisely as in CDLNS. It does not truncate at `(p-1)/2`, `m`, or `2m`.

The frozen tail theorem gives `T_p = p² R_p (mod p³)`, so only its direct consequence is used:

\[
 gh\equiv W_p\pmod{p^2}.
\]

As a support-level check on this use, the frozen valuations are `0,1,2` in the blocks `0..m`, `m+1..2m`, `2m+1..6m`. If `i+j >= 6m+1`, at least one index is larger than `2m`; hence every displayed tail summand has valuation at least two. The integer derivative weight cannot decrease valuation. This is a readout of the accepted valuation/tail interface, not a re-opening of its reflection or harmonic bookkeeping.

**Precision counterexample to an invalid shortcut:** for `p=19`, this exact weighted tail is `4332 mod 19³`, namely `12*19²`, and is nonzero. It is zero mod `19²`. Consequently the valid product congruence mod `p²` must not silently be upgraded to mod `p³`.

## 2. The derivative factor is exactly -6

The accepted finite polynomial transport is

\[
 H_m(z)=Q_m(1-z)\quad(\bmod p).
\]

Its accepted derivative interface gives

\[
 h\equiv\Psi\equiv Q_m(1/2)-6Q'_m(1/2)
       \equiv -6Q'_m(1/2)\pmod p.
\]

The first `6` here is `12z` evaluated at `z=1/2`; the minus sign is the chain rule for `1-z`; CM0 removes `Q_m(1/2)`. There is no derivative with respect to `t` or `t²` still to be converted. SIMPLE makes this surviving scalar nonzero. The accepted `p | g` means `g/p` is p-integral, so multiplication by this mod-p interface is legitimate.

Thus the exact bidirectional chain is

\[
\begin{aligned}
\mathrm{UR}
&\iff (g/p)\,h\equiv1\pmod p\\
&\iff gh\equiv p\pmod{p^2}\\
&\iff W_p\equiv p\pmod{p^2}.
\end{aligned}
\]

Only one factor of `p` is divided out. This costs one digit and supplies precisely UR, not LIFT. It also shows, once the imported theorem applies, that `v_p(g)=1` and that the normalized unit is the reciprocal of `-6Q'_m(1/2)`.

## 3. Imported arithmetic strength and signs

CDLNS, *p-adic analogues of Ramanujan type formulas for 1/pi*, Mathematics 1 (2013), DOI `10.3390/math1010009`, Theorem 1, printed page 12, states the weighted truncation congruence **mod p²** with `sgn = -1` in the supersingular case. It does not restrict the weighted conclusion to ordinary primes. The original proof's final paragraph expressly handles supersingular reduction via the multiplication-by-`-p` map; relying on the theorem statement therefore imports its supersingular branch, not a split ordinary unit-root formula.

With `d=3`, `lambda=1/2`, `a=6`, and the separately verified supersingular hypothesis, its conclusion is

\[
 W_p\equiv -\left(\frac{1/2}{p}\right)p\pmod{p^2}.
\]

For the two retained, separately labelled residue classes,

| `p mod 24` | `p mod 8` | `(1/2 / p) = (2 / p)` | supersingular `sgn` | product sign |
|---|---:|---:|---:|---:|
| 13 | 5 | -1 | -1 | +1 |
| 19 | 3 | -1 | -1 | +1 |

Hence the theorem supplies exactly `W_p = p (mod p²)` for both classes. The branch signs are not fitted to finite data or averaged together.

Babei et al., arXiv:2408.08844v3, Theorem 2.1 explicitly restates both signs. Its revision in Theorem 2.2 concerns the **unweighted** companion, especially an ordinary nonsquare case. This proof does not import that companion theorem and does not use an ordinary unit root. The modern restatement is corroborating documentation, not a claim of an independent proof.

## 4. Complex coefficient versus delta normalization

The complex Ramanujan formula must first be written in CDLNS's normalization `sum (a*k+1)c_k lambda^k = delta/pi`. Guillera's table uses `sum (A+B*k)c_k lambda^k = 1/pi`, with

\[
 A=1/(3\sqrt3),\qquad B=6/(3\sqrt3),\qquad \lambda=1/2.
\]

Dividing by `A` gives exactly `a=B/A=6` and `delta=1/A=3 sqrt(3)`. The theorem's arithmetic right side is `sgn*((1-lambda)/p)*p`; it has no extra multiplier `delta`. Neither multiplying the congruence by `3 sqrt(3)` nor setting its `a` equal to Guillera's `A` or `B` is licensed. CDLNS requires `a` and `lambda` to be p-adic units; it does not require importing a p-adic square root of three from this display.

## 5. Noncircular dependency boundary

The load-bearing chain is:

1. A proved complex normalization fixes `d=3`, `lambda=1/2`, `a=6`.
2. The exact CDLNS elliptic model has CM and good supersingular reduction, with the required unramified extension; `prior_art/APPLICABILITY_PROOF.md` supplies this check and the final combined audit above verifies the calculation.
3. CDLNS Theorem 1 then proves the weighted `W_p = p mod p²` value.
4. Accepted finite Clausen/tail and derivative interfaces translate that value bidirectionally to UR.

The proof never assumes Sun A14(ii), any weighted mod-p³ conclusion, the desired first-digit equality, the unknown parameter-normal displacement, an ordinary unit root, or LIFT. The original taskbook explicitly permits ending the second-route search once one route closes or refutes UR. A proof by this genuinely applicable published theorem is such a closure; it should be described as a specialization plus exact interface translation, not as a new independent p-adic normalization theorem or historical-priority discovery.

CM0 and SIMPLE remain frozen inputs. The accepted historical proof of `p | g` does not have to be replayed or strengthened. No information needed for a future second-digit lift is discarded from the retained carrier merely because this observer is mod p.

## 6. Small transcription falsifier and reuse

`check_interface_smoke.py` actually imports and executes the frozen `direct_Bs`, `frac_mod`, and `q_value_and_derivative` callables. The 3F2 coefficient is separately represented by `(2k)!(3k)! / ((k!)^5 216^k)`. The script checks exact rational finite-product equality, the needed tail precision, the weight/factor conversion and one minimum prime from each branch. It does not call either predecessor's full regression runner or calculate `R_p`, `Delta_p`, JT2 or LIFT.

| p | `(g/p) mod p` | `h mod p` | `Q'_m(1/2) mod p` | `W_p mod p²` |
|---:|---:|---:|---:|---:|
| 13 | 11 | 6 | 12 | 13 |
| 19 | 8 | 12 | 17 | 19 |

A deliberate wrong `h` weight `6k+1` yields product residues `91 mod 169` and `190 mod 361`, rejecting that transcription. The script and `interface_smoke_result.json` are exact bounded falsification aids, **not an all-prime proof**, independent Driver review, a repeated 77-prime regression or a new tool family. The relevant executable reuse resolution is `REUSE_EXECUTED`.

## Final boundary

The combined proof closes UR at the research-return level with no mathematical blocking issue found. The geometric applicability condition initially left to a separate component has been resolved in this audit. The `p=19` tail calculation is only a counterexample to an invalid precision upgrade; it computes neither the `LIFT` discrepancy nor `R_p` and makes no second-digit theorem claim. The full parent second-digit LIFT, Sun A14(ii), Working Truth, Foundation status and canonical promotion remain untouched. Publication/freeze and mathematical independent Driver acceptance remain distinct.


## Portable reproduction

```json
{
  "status": "PASS",
  "command": [
    "python",
    "-I",
    "check_cm24_translation.py",
    "--output",
    "REPRODUCED.json"
  ],
  "source_files_copied": [
    "check_cm24_translation.py",
    "REUSED_SOURCE_MANIFEST.json",
    "RUN.json",
    "check_enterprise_brc_half_coupling_inert_plus_reflected_derivative_product_bridge.py",
    "check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate_independent.py",
    "brc_weighted.py",
    "brc_logarithm.py",
    "exact_arithmetic.py",
    "core.py",
    "division.py"
  ],
  "temporary_directory_removed": true,
  "records_equal": true,
  "trace_hash_equal": true,
  "stdout": "{\"status\": \"PASS\", \"primes\": 8, \"negative_controls_detected\": 40, \"finite_only\": true, \"output\": \"REPRODUCED.json\", \"elapsed_seconds\": 0.960491}",
  "stderr": ""
}
```


## Exact transcription and precision witness

```json
{
  "schema": "CM24_SHARED_CONTEXT_INTERFACE_SMOKE_V1",
  "status": "PASS",
  "classification": "FINITE_TRANSCRIPTION_FALSIFIER_ONLY_NOT_PROOF_NOT_DRIVER_REVIEW",
  "cases": [
    {
      "p": 13,
      "residue_mod_24": 13,
      "g_over_p_mod_p": 11,
      "h_mod_p": 6,
      "Qprime_mod_p": 12,
      "W_mod_p2": 13,
      "weighted_tail_mod_p2": 0,
      "weighted_tail_mod_p3": 0,
      "wrong_h_weight_6k_plus_1_product_mod_p2": 91,
      "exact_finite_product_identity": true
    },
    {
      "p": 19,
      "residue_mod_24": 19,
      "g_over_p_mod_p": 8,
      "h_mod_p": 12,
      "Qprime_mod_p": 17,
      "W_mod_p2": 19,
      "weighted_tail_mod_p2": 0,
      "weighted_tail_mod_p3": 4332,
      "wrong_h_weight_6k_plus_1_product_mod_p2": 190,
      "exact_finite_product_identity": true
    }
  ],
  "reused_functions": [
    "bridge.direct_Bs",
    "bridge.frac_mod",
    "jacobi.q_value_and_derivative"
  ],
  "reuse_resolution": "REUSE_EXECUTED",
  "source_sha256": {
    "coverage/source/scripts/check_enterprise_brc_half_coupling_inert_plus_reflected_derivative_product_bridge.py": "d5cc45f491ed030b6ec2e112dd5f7a92a8658a0d5fa2dffdc173232dc07c2623",
    "coverage/source/scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate_independent.py": "93934cdcfa89b46067ca2d3598dd08de083f63d907ed7d650e1d794298b9c05c"
  },
  "precision_boundary": "No LIFT calculation, no mod-p3 weighted theorem, no 77-prime replay."
}
```


## Tool coverage before scientific execution

```json
{
  "schema": "CM24_MINIMUM_TOOL_COVERAGE_PREPARATION_V1",
  "source_commit": "9cd16ea1d377ba0caff2609f3897a68ed93f9010",
  "scope": "READ_ONLY_PREPARATION_NO_RESEARCH_COMPUTATION",
  "coverage_verdict": "REUSE_EXISTING_TOOL",
  "verified_surface": {
    "registry_blob": "3889506451091ebcfbf7a58cda6517c4af8c3597",
    "inventory_blob": "9289039bc689c638fbef10f9f4489e3793e999f0",
    "router_blob": "56ad1ee65527f28065d6aec89a802a8e029f0c6e",
    "source_tree": "dab9ff9d181dca8f3ae2220088b7d181dfd277c0",
    "inventory_addenda_tree": "e0e4cb465f66e0c54009fab99d760536e7d65c88",
    "local_source_tree_verified_identical_to_remote_pin": true,
    "local_source_dirty": false
  },
  "applicable": [
    {
      "id": "task_local.reflected_derivative_product_bridge",
      "path": "scripts/check_enterprise_brc_half_coupling_inert_plus_reflected_derivative_product_bridge.py",
      "blob": "373490d2b7a81c14d07a8ef19eda2887e332c021",
      "api": {
        "frac_mod(Fraction, modulus)": "exact modular reduction, rejects nonunit denominator",
        "direct_Bs(p)": "exact Fraction B_k, 0<=k<p",
        "taylor_coefficients(m)": "exact tuple F0,F1,F2,J0,J1"
      },
      "recommended_resolution_after_actual_execution": "REUSE_EXECUTED",
      "boundary": "Existing finite regression is not UR proof; reuse narrow callable values in new certificate only, do not relabel the old 77-prime scan as new research."
    },
    {
      "id": "task_local.terminating_jacobi_independent",
      "path": "scripts/check_enterprise_brc_half_coupling_inert_plus_terminating_jacobi_jet_certificate_independent.py",
      "blob": "baaccc59041db27c8396d1b093832be65d7d23fc",
      "api": {
        "q_value_and_derivative(m,p)": "Q_m(1/2),Q'_m(1/2) mod p",
        "legendre_value_derivative(n,p)": "P_n(t),P'_n(t) in F_p[t]/(t^2-1/2)",
        "frac_mod(Fraction,modulus)": "exact modular observation"
      },
      "recommended_resolution_after_actual_execution": "REUSE_EXECUTED",
      "boundary": "Do not rerun main() merely to repeat accepted CM0/SIMPLE/77-prime regression; derivative evaluator can be reused as a falsifier."
    },
    {
      "id": "t0.weighted_brc_rational_holonomy",
      "path": "src/enterprise_math/brc_rational_holonomy.py",
      "blob": "2591640fe348da9cd7f293a957bea9ae92c82943",
      "api": {
        "rational_prime_valuations(int|Fraction)": "sorted tuple(prime,exponent), positive q only",
        "rational_from_prime_valuations(mapping|sequence)": "positive Fraction reconstruction"
      },
      "recommended_resolution": "REUSE_EXECUTED only if full prime valuation carrier is actually required; otherwise NOT_APPLICABLE to modular scalar computation",
      "boundary": "Rejects zero/negative; factors full numerator/denominator using reference trial division. It does not retain signed unit residue or implement CM/Gamma/Jacobi identities."
    },
    {
      "id": "T0_BRC",
      "method_ids": [
        "recent.cbrc_f0.signed_group_completion",
        "t0.weighted_brc_cwm"
      ],
      "recommended_resolution": "REUSE_APPLIED only after exact declared carrier law is applied in scientific work",
      "boundary": "Positive CWM cannot represent signed/amplitude cancellation or parameter derivatives. Signed completion requires retaining exact typed witnesses; current lookup alone is not reuse."
    }
  ],
  "excluded_semantic_matches": [
    {
      "id": "T1_SCALE_ENUMERATION_VALUATION",
      "reason": "Scale enumeration valuation, not p-adic unit reciprocity."
    },
    {
      "id": "t0.weighted_brc_critical_ratio_jet",
      "reason": "Positive weighted recurrent branch ratio/critical spectral jet, not hypergeometric parameter Taylor jet."
    },
    {
      "id": "module:group_ring_affine_character",
      "reason": "jacobi_symbol is a quadratic arithmetic symbol, not a finite-field Jacobi-sum / Gross-Koblitz implementation."
    },
    {
      "id": "heartbeat.* / Shor",
      "reason": "Outside this task; lexical p-adic/valuation matches provide no missing CM24 identity."
    }
  ],
  "missing_exact_capability": "No matching curated/current executable source implementing the supersingular CM(-24) Gauss-Manin/Wronskian unit comparison, hypergeometric parameter-jet UR proof, finite-field Jacobi-sum or p-adic Gamma normalization was located. This is a scoped lookup result, not proof of global nonexistence and not authorization to create a new general tool family.",
  "reuse_status": "Coverage lookup executed; scientific functions not executed, no proof/application reuse claimed yet.",
  "artifacts": [
    "FETCH_MANIFEST.json",
    "coverage_router_readonly.json",
    "source/"
  ]
}
```

The source-read coverage report records its pre-execution status. Actual REUSE_EXECUTED calls and their outcomes are in RUN.json. The two-prime precision witness is reported to delimit this proof, not to evaluate LIFT.
