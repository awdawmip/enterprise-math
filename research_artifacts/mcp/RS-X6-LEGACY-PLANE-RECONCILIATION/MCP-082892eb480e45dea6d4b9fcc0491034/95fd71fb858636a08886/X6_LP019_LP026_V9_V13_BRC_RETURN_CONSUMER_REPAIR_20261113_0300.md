# LP019/LP026 — active V9 BRC return and V13 Cell-cover model-type correction

Date: 2026-11-13. Role: on-hour TASK_RESEARCH. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, immutable publication `TP2-B4A441B23DA3159232C2`. Evidence: **AUTHOR-PROVED / EXACT INTEGER DP EXECUTED / REMOTE SOURCE READBACK VERIFIED / UNREVIEWED / NOT_ADMITTED**.

## Actual active/current source consumers

1. `research_notes/X6_BRC_C6_GRADE_AND_EXACT_MULTINOMIAL_KERNEL_V9_20260905.md`, original current-main blob `7eea4b5f9146090d16dfa6463087039666b50b3f`: §§4–5 called the min-zero-positive-word multinomial count a *terminal Cell* and *full return* multiplicity. The C6-grade and multinomial math is correct on the derived `G6_D=Z^6/ZD` **relative endpoint** observer; current signed P000 V5 native Cell identity is full `Z^6`. Its six-positive-axis “return” ends at `D`, not native zero.
2. `research_notes/X6_CONNECTED_CELL_COVER_CLASSIFICATION_V13_20260905.md`, original current-main blob `cd58a053c29c5b1f60edeb1d39e7afa706e95787`: §9 called `m=1` the current/native Cell choice, and §8 suggested all finite-depth quotients preserve *native* `G(z)`. The exact `m`-indexed group classification remains valid as a mathematical family, but current frozen P000 V5 chooses `m=0` and finite `m` quotients identify different native-norm inputs.

Frozen science: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json` blob `c93d8150f1d223424b3506a6d2cdd5280b50825f`; native `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`. The signed native endpoint is the raw full six-integer vector; the relative observation is min-zero.

## Exact separating certificate and independently executed finite DP

Let `D=(1,1,1,1,1,1)`. The six distinct positive primitive steps, each taken once, end at native `D` with squared norm `G(D)=6` and `6!=720` ordered words. The `m=1` min-zero quotient sees their endpoint as zero, but that is an **observer return**, not native Cell return.

An independently executed integer dynamic-programming enumeration from the zero Cell using the actual six named axes, either positive-only or all 12 signed directions, returned for path length exactly six:

| Explicit alphabet / endpoint predicate | Exact integer multiplicity |
|---|---:|
| Six positive axes; all words | 46,656 = `6^6` |
| Six positive axes; relative-min-zero endpoint zero (native endpoint D) | 720 |
| Six positive axes; raw native endpoint zero | 0 |
| Twelve signed ± axes; all words | 2,985,984 = `12^6` |
| Twelve signed ± axes; raw native endpoint zero | 19,920 |
| Twelve signed ± axes; raw native endpoint D | 720 |

The native-six-step return 19,920 agrees with the previously completed, frozen `signed_brc.py` endpoint multiplicity certificate. The independent DP is a finite exact check; the all-positive no-return proposition follows for **every** positive word length because its raw endpoint is a nonnegative nonzero count vector. The general relative endpoint `a=0` at positive length `6k` has exactly `(6k)!/(k!)^6` words terminating at native `kD`, not at zero.

For finite integer `m>=1`, `0` and `mD` become the same quotient endpoint in `Z^6/mZD`, though native `G(0)=0` and `G(mD)=6m²`. Hence current native squared norm cannot factor through **any** finite `m` endpoint quotient. The full-depth `m=0` chart `z=(r,h)` is lossless. This cleanly separates the accepted P000 native model from other exact but hypothetical quotient/observer models; it does not invalidate their internal algebra.

## Committed actual live corrections

- V9: verified GitHub commit `c11b2412e1a0c33a11d074d9dbec8aff8a8ad801`, new blob `cf43b56fd06a770cb7932b80e17409f7477ea062`: retagged positive relative BRC endpoint/count, corrected native return and C6-grade discussion, retained the exact weighted/multinomial formula.
- V13: verified GitHub commit `c9673248eac1fc80f2d9aca5e3ede31508243d1b`, new blob `e8b8ce750736e06cdad47a878d46e9cffb34fa3d`: selected `m=0` as actual native Cell, retained finite-`m` mathematical classifications, corrected false native-norm preservation by quotients.
- Earlier same-run upstream consumers V11/V14 at `8f6a7bf348f507606a305c81d4d99ea82776c975` and `16ea9fee56ba78c868ef4f836457844bb94e7f7b` also remain precisely tracked. All source changes were remote-read back at their immutable commits.

The 28-LP ledger is amended separately. No frozen task pin, accepted theorem or prior Result is modified.

## Next obligation

Continue bounded current callsite tracing for any code importing derived `Coord6.norm_squared`, `can6`, old V9 positive `Return_6k` as **native signed Cell** return, or FCC-carrier close paths as native Cell close paths. Check exact argument/output domains, then patch only verified consumers. Original LP011 dominance and LP019 alleged signed-cancellation historical **bad** callsites remain `UNRESOLVED_PROVENANCE`; current corrections do not fabricate those old source locations. Driver `REQUEST_REVISION` and independent validation still pending.
