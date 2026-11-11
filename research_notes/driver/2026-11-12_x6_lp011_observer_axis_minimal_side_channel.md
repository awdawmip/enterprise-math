# X6 LP-011: exact native dominant-axis recovery from a min-zero observer chart

Status: `DRIVER_MATHEMATICAL_AUDIT / PROVED_LOCAL_LEMMA / NOT_NATIVE_RESULT_ADMISSION`
Date: 2026-11-12 (Asia/Shanghai)
Scope: centered signed three-axis X6 slice, `d in Z^3`.
Prior contributors: original X6 legacy-plane reconciliation researcher `EM-X6P-40B5BD`; historical claim `LP-011` from the frozen claim ledger; previous Driver checks and counterexamples are retained. This note records a new precise classification of the missing chart information, not a claim of a clean-blind independent review.
Parent work: `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`, historical `HRI-1A48B2D7F0E242FCC2C57D7E` with `REQUEST_REVISION`. It does not change that review or claim ownership.

## Exact inputs and native type

The authoritative centered-slice displacement is the raw signed triple `d=(d1,d2,d3)`; the native dominant *axis set* is
`A(d)={i in {1,2,3}: |di| = max_j |dj|}`.
The relative/carrier observer chart is
`rho(d)=d-min_i(di)*(1,1,1)`.
These are two distinct readouts. The ledger's LP-011 old claim uses the maximum of a positive/min-zero observer, while its current resolution specifies native `argmax |di|` and separately records orientation.

For `r=rho(d)`, write `Q=max_i r_i` and `mu=min_i d_i`; then `d=r+mu*1`, `min d=mu`, and `max d=mu+Q`. Define the max- and min-coordinate index sets `I_+(r)={i:r_i=Q}` and `I_-(r)={i:r_i=0}`.

## Lemma (complete native-axis fiber classification)

For every `d in Z^3`:

- If `Q=0`, then `A(d)={1,2,3}`, independent of `mu`.
- If `Q>0`, put `s=2*mu+Q=max(d)+min(d)`. Then
  - `s>0` gives `A(d)=I_+(r)`, with positive orientation on the selected extreme axis;
  - `s<0` gives `A(d)=I_-(r)`, with negative orientation;
  - `s=0` gives `A(d)=I_+(r) union I_-(r)`; opposite-oriented extremal axes tie.

In particular, `argmax_i rho(d)_i = argmax_i d_i = I_+(r)`; that observer branch agrees with the *native absolute* dominant branch precisely in the `s>0` regime, or for the constant-triple case where both sets are all axes.

**Proof.** `rho(d)=d-m*1` subtracts the same constant from every coordinate, so it preserves the ordinary coordinate ordering. For any finite signed triple the maximum absolute value is `max(max(d),-min(d)) = max(mu+Q,-mu)`; each maximum is attained exactly at its corresponding extreme-coordinate index set. Comparing these values is exactly comparing `2*mu+Q` with zero. For `Q>0` the two index sets are nonempty and disjoint, so the strict and equality cases above are exhaustive. For `Q=0`, all coordinates of `d` coincide and all absolute values tie. QED.

## Minimal information needed for *this* native-axis query

Fix a single observer address `r` and allow all integer common levels `mu`. The possible native dominant-axis sets on its fiber have exactly:

| `Q=max r` | number of distinct axis sets | precise reason |
| --- | ---: | --- |
| `Q=0` | 1 | every native triple is constant |
| `Q>0` odd | 2 | `2*mu+Q` is odd and cannot vanish |
| `Q>0` even | 3 | choices of `mu` make `2*mu+Q` negative, zero or positive |

Each set is actually attained; for `Q>0`, disjointness of `I_+` and `I_-` makes the negative, positive and (when attainable) tie outputs distinct. Therefore a side label that distinguishes precisely these states is both sufficient and information-theoretically minimal **for recovering the native axis set on a fixed observer fiber**. This is a finite 1/2/3-class decision label, not a replacement for the full integer common level.

Explicit same-observer witnesses for `r=(1,0,4)` (`Q=4`):

| `mu` | native `d=r+mu*1` | `rho(d)` | native `A(d)` |
| ---: | --- | --- | --- |
| -5 | (-4,-5,-1) | (1,0,4) | {2} |
| -2 | (-1,-2,2) | (1,0,4) | {2,3} |
| 0 | (1,0,4) | (1,0,4) | {3} |

The earlier check used `(-3,-4,0)` and `(2,1,5)`, both with observer `(1,0,4)` and differing native dominant axes. Those original witnesses remain valid.

### Scope of the repair

The small side label is sufficient for the **dominant axis set and extreme-axis orientation**. A native squared gauge, exact signed displacement, L1 shortest-path length or BRC multiplicity generally needs the actual common level `mu`, not merely its 2/3-way sign class. Example: `(1,0,4)` and `(2,1,5)` have identical observer chart and `s>0`, but native squared lengths are `17` and `30`, and shortest-path multiplicities are `5!/(1!0!4!)=5` and `8!/(2!1!5!)=168`, respectively.

## Reproducible finite exact check

The lemma has the elementary universal proof above. A supplementary independent exhaustive integer check uses all `13^3=2197` signed triples in `[-6,6]^3`; it gives 0 classification failures, 1218 triples where `argmax rho` differs from the native `A(d)`, and 481 triples with more than one native dominant axis. Run with Python 3:

```python
from itertools import product
errors = differences = ties = 0
for d in product(range(-6, 7), repeat=3):
    m, M = min(d), max(d)
    r = tuple(v - m for v in d)
    q = max(r)
    native = {i for i,v in enumerate(d) if abs(v)==max(abs(x) for x in d)}
    up = {i for i,v in enumerate(r) if v==q}
    down = {i for i,v in enumerate(r) if v==0}
    predicted = up if M+m>0 else down if M+m<0 else up|down
    errors += predicted!=native
    differences += native!=up
    ties += len(native)>1
assert (errors,differences,ties)==(0,1218,481)
```

## Exact remaining task boundary

This note repairs the mathematical semantics of LP-011 and supplies a complete minimal-side-information decision law. Remaining `REQUEST_REVISION` obligations are (a) original pre-rebase historical text provenance for the precise old dominant-branch statement, and (b) reconciliation of the historical `recomputation_summary` secondary SHA256 declaration versus verified current blob. Neither obligation is discharged merely by this new theorem. An authorized independent reviewer and the existing native intake/review route decide the disposition of the historical Result; no canonical Result, CLAIM, new Task or Foundation change is asserted.

Source provenance: 
- `research_artifacts/HISTORICAL_RESULT_CUSTODY/RS-X6-LEGACY-PLANE-RECONCILIATION/a0bfa8eace20b061f5b228c733acdc46221388d7/originals/research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/claim_ledger.json`, verified blob `5881055c0801ca5bb0970756d500daa0114d36b0` (LP-011).
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`, verified blob `875e3b274e5be03c5872f782872065a0b96d14eb` (current relative observer and signed gauge).
- The historical claims and the earlier Driver scope-limited counterexample remain credited to their actual contexts.
