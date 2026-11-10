# Empty-prefix and tracked-region evidence on the original BRC programs

## Reproduction

The delivery's root README describes the included running dependencies. This
directory imports the sibling `directed/`, `incremental/`, and `parent_bundle/`
modules; the tracked-region controller also imports `regional/region.py`.
The original programs keep their existing behavior.

Run from the reproduction root:

```bash
python future/check_prefix_certificate.py costs --output future/costs.json
python future/check_prefix_certificate.py regressions --output future/regressions.json
python future/check_prefix_certificate.py path_tradeoffs --output future/path_tradeoffs.json
python future/check_prefix_certificate.py audit1 --output future/audit_r1.json
python future/check_prefix_certificate.py audit2 --output future/audit_r2.json
python future/check_prefix_certificate.py omissions --output future/omissions.json
python future/check_prefix_certificate.py protected --output future/protected.json
python future/check_region_certificate.py costs --output future/region_costs.json
python future/check_region_certificate.py regressions --output future/region_regressions.json
python future/check_region_certificate.py audit1 --output future/region_audit_r1.json
python future/check_region_certificate.py audit2 --output future/region_audit_r2.json
python future/check_region_certificate.py omissions --output future/region_omissions.json
python future/check_region_certificate.py protected --output future/region_protected.json
python future/check_region_certificate.py regional_gain --output future/region_gain.json
python future/check_region_certificate.py path_tradeoff --output future/region_path_tradeoff.json
python future/check_horizon_costs.py --output future/horizon_costs.json
```

Each saved JSON is one completed execution. The `costs` outputs distinguish
primitive commands, extra vacancy bit reads, business identity bit reads, the
existing prefix-tree decisions, and new evidence-maintenance events.

## Implementation

`PrefixCertificateController` retains the complete empty low-prefix class
`(depth,prefix)` proved by the inherited query. It first keeps the old selected
residue when it remains legal and inside the class. Otherwise it selects the
first legal residue in that class. A nonempty binding inside the class retains
the opposite next-bit child; a matching singleton binding consumes the class.
Empty binding, request copy/drop, and source changes preserve the certificate.

`RegionController` instead retains the original empty class together with exact
current occupancy introduced through observed business operations. A copied
request increases the corresponding residue's multiplicity; dropping or
overwriting its final reference restores that residue. Full key zero is empty;
a nonzero full key whose residue is zero remains a genuine occupied residue.

Both controllers wrap the unchanged original `directed.Controller.step`.
Physical Boolean output, real reads, source-conflict checks, source creation,
business identity reads and primitive command execution all use that code. The
wrapper recovers a query's terminal node from its actual branch decisions only
when `target_searches` increased. A cached witness hit therefore never invents
an empty root node. Exact request-table access begins at the explicit
verification boundaries in the two new modules.

## Selected actual results

All counts below are original BRC core primitive attempts.

| Preparation and process | Single point | One shrinking class | Tracked region |
|---|---:|---:|---:|
| r=2, empty references, create target 0, bind slot 0, create target 3 | 106 | 95 | 95 |
| Same process, extra vacancy reads | 3 | 2 | 2 |
| r=6, empty references, 32 create/bind-slot-0/release rounds | 2,580 | 2,550 | 2,580 |
| Same process, extra vacancy reads | 6 | 6 | 6 |
| Same process, inherited prefix-tree searches | 32 | 16 | 1 |
| Same process, inherited prefix-tree node visits | 95 | 47 | 2 |
| r=6, requests 1,2,3,5,6,7, alternate targets 0/4 for 32 creates with releases | 1,056 | 1,056 | 1,056 |
| Same stable process, extra vacancy reads | 8 | 8 | 8 |
| Same stable process, inherited prefix-tree searches | 32 | 1 | 1 |
| Same stable process, inherited prefix-tree node visits | 96 | 3 | 3 |
| r=14, half references key 2 and half key 3, 8 create/bind/release rounds | 920 | 920 | 880 |
| Same process, extra vacancy reads | 27 | 27 | 21 |
| Same r=14 preparation, 32 rounds | 3,032 | 3,022 | 3,016 |
| r=6, half references key 2 and half key 3, 32 rounds | 2,520 | 2,522 | 2,536 |
| Same r=6 process, extra vacancy reads | 11 | 11 | 9 |

For the r=6, 32-round empty-reference process, the tracked region additionally
uses 109 successor-node visits and 189 update-node visits. These are separate
control operations. The original command counts and inherited tree counters do
not subsume them.

The exact r=10 mixed preparation in `path_tradeoffs.json` gives the reverse
comparison for the shrinking-class policy: 642 versus 656 commands and 25 versus
26 extra vacancy reads. The tracked-region policy has the same reverse counts
in `region_path_tradeoff.json`. Different selected safe keys change later bindings and
therefore later query paths. The algorithms retain their stated cumulative and
per-query bounds while this measured comparison depends on the preparation.

`horizon_costs.md` proves the exact original-command difference for the
half-key-2/half-key-3 family `r=2^b-2`, `b>=3`. For `T>=2` rounds, tracked region
minus single point is `2*floor(T/2)-8*(r/2-1)`; their first round is equal.
The equality horizons are 16/17 for r=6 and 48/49 for r=14. Four original-kernel
runs verify all 68 cumulative prefixes through T=18 and T=50 respectively.

## Completed finite verification

The shrinking-class controller executes every one-slot preparation (77 states)
and every two-slot preparation (1,900 states) on three specified mixed sequences:
5,931 batches and 33,609 API actions. The tracked region executes the same finite
preparation domains on two alias/reclamation sequences: 3,954 batches and 35,586
API actions. Every API boundary checks the complete core matching, result, both
identity encodings and observation-prefix state. The region additionally checks
each slot mark, multiplicity and represented free point.

The original regional audit used dictionary residue counters. The final region
module uses fixed-domain indexed counters with the same observable operations.
After that representation refinement, the focused original-kernel regressions,
two-slot full preparation audit, strict-gain cases, reverse case and horizon
runs were completed again or newly executed. The separate control verifier
checks the indexed representation's finite domains. The earlier unchanged
primitive-path checks retain their stated scopes.

Focused cases include empty business bindings inside an even class, nonempty full
key 8 at residue zero, copied aliases, overwriting the representative, self-copy,
source execution that retains its request identity, reacquiring a new region,
and the prior physical-register case. An existing source C retains its original
creation through all 344 tested primitive prefixes in both implementations.

Every single omission position is executed for one doubled primitive sequence:
304 positions for the shrinking class and 440 for the tracked region. Adaptive
branches, final core matching and evidence state agree with the corresponding
unomitted run.

Both controllers execute inside the inherited real holding interval in both
rotation-gate phases. A separate complete competing bind is attempted at every
body boundary; each is refused before handoff and preserves the core. The
contender then succeeds after the actual handoff. The shrinking class uses a
390-command body plus 31 wrapper commands, with 391 boundary attempts per phase;
the tracked region uses 391+31 commands, with 392 boundary attempts per phase.
These checks exercise the stated boundary-attempt schedule.

The protected instance retains 367 members and 1,914 candidate relations. The
ordinary three-target r=6 instance retains 330 members and 1,886 candidates.
Neither controller adds persistent BRC members or candidate relations. Their
temporary decision structures are accounted for separately in the proofs.
