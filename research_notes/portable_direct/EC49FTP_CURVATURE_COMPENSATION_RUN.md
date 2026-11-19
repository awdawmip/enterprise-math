# EC49FTP executed verification log (2026-11-19)

Scientific dependency: BRC16943 frozen science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; price-prior formulas from EC49FTO PR #2788. This is **author-side exact polynomial postprocessing**, not a native Bellman execution.

## Author execution

Command: `python /mnt/data/ec49ftp_verify.py` using Python standard-library `fractions.Fraction`.

Observed stdout certificate:

```json
{
  "schema": "EC49FTP_EXACT_POLYNOMIAL_PRIOR_CERT_V1",
  "date": "2026-11-19",
  "status": "AUTHOR_PROVED_EXACT_FRACTION_REPRODUCED_PARENT_DEPENDENT_NOT_REVIEWED",
  "original_science": "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
  "price_parent": "EC49FTO PR2788@d790653d2e61b3d4db0a8fe066e746d0ad6196d7",
  "prior": {
    "f": "1+(a-3/4)^2",
    "g": "b",
    "f_logconcave": false,
    "g_logconcave": true,
    "f_logcurvature_upper_bound": "2",
    "g_logcurvature_upper_bound": "-16384/3249"
  },
  "clipping_probability": "3636023540431/8037720298125",
  "clipping_num": "3636023540431/149158845480960000",
  "weight_den": "1388657/25769803776",
  "tp2_margin_rational": "14050088/138163725",
  "dmax": "7/960",
  "cdf_checks": 23310,
  "inverse_grid_points": 468,
  "m_grid_size": 36,
  "threshold_grid_size": 37,
  "native_bellman_rerun": false,
  "formal_review": false
}
```

The exact-rational checker stored in this branch differs from the executed local script only in a nonfunctional comment: `# exact check for 1080 inverse points` was shortened to `# exact check for inverse points`. All code paths and parameters are identical. Git Blob readback of the published source is the publication verifier, not a mathematical review.

## Independent symbolic integration

Separately executed `sympy.integrate` twice, integrating the polynomial integrand `b*(1+(a-3/4)**2)` for `a_c(b)≤a≤49/64`, `7/16≤b≤57/128`; compared with exact normalized total weight. Actual result:

```text
numerator = 3636023540431/149158845480960000
denominator = 1388657/25769803776
probability = 3636023540431/8037720298125
```

Both independent evaluations agree exactly. The 23,310 CDF comparisons and 468 inverse checks are finite regression evidence. The continuous stochastic-order theorem is established by the separate derivative/TP2 and atom-ratio argument; no independent formal review or native Bellman rerun was performed.
