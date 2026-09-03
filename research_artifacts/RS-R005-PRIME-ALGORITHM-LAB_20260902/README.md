# RS-R005-PRIME-ALGORITHM-LAB — 2026-09-02 checkpoint bundle

This bundle continues the R005-A p=2 least-basis frontier from repository
commit `14db099861661d3a57133374c2fb3b7cfe6012ec`.

Primary result: exact bounded-deficit prime-gap shadow inversion.  The first
deficit-two seam `q=78553` is reduced to a complete, attested catalog of exact
916-gaps in a finite cofactor-floor band.  The included empty catalog template
is intentionally rejected; no frontier extension is asserted without the
missing completeness evidence.

Run validations:

```bash
cd experiments
python3 r005a_p2_gap_shadow_inversion_regression.py
g++ -std=c++17 -O2 -Wall -Wextra -Werror \
  r005a_p2_one_unit_guard_regression.cpp -o /tmp/r005_guard
/tmp/r005_guard
python3 r005a_p2_gap_shadow_inversion.py --q 78553 --describe-only
```

See `docs/R005A_P2_DEFICIT_SHADOW_INVERSION_20260902.md` and
`returns/RS-R005-PRIME-ALGORITHM-LAB.md`.
