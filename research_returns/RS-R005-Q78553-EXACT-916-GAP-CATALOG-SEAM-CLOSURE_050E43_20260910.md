# R005 q78553 exact-916 catalogue and seam closure — research return

Researcher outcome: **Q78553_SEAM_CERTIFIED_CLOSED**.
Driver review and canonical admission remain required.

Researcher-ID: EM-R005Q53-050E43
Task: RS-R005-Q78553-EXACT-916-GAP-CATALOG-SEAM-CLOSURE
Publication: TP2-09D6ECE7F315F0766FE1
Execution: ER-8ABFD24CCC477A03ED13
Actual claim: r005q53-050e43-20260910 / Issue240 comment 5606578580
Parent: OBJ-R005-PRIME-ALGORITHM-LAB-RELAY-20260909

## Result

The complete exact-916 gap catalogue in the frozen start band
[1291005053866735,1294364244470160] is empty.
The actual maximum consecutive gap in that band is 730, witnessed by
1292271366466303 and 1292271366467033.

The unchanged accepted scanner returns CERTIFIED_UNDER_ATTESTED_CATALOG,
exit 0, and zero candidate failures. Under the accepted DSI reduction, the
entire seam 2822453183434 <= k <= 2826122804521 is closed.
The frozen q=78553, Q=6170573809, G=916 and d_max=2 were not changed.
The canonical frontier was not advanced by this researcher; it remains
K <=2822453183433 pending Driver acceptance. No next q was executed.

## Complete construction and checks

The production run covered [1291000000000000,1295000000000000) using 4000
disjoint half-open blocks, each of width 1000000000, with three numeric worker
processes. Padding permits independent counts at four published 1e12 boundaries.
The exact task band remains the catalogue's scope.

| Half-open cell | Constructed and independently expected prime count | Maximum within-cell observed gap |
|---|---:|---:|
| [1291e12,1292e12) | 28739946181 | 720 |
| [1292e12,1293e12) | 28739548370 | 730 |
| [1293e12,1294e12) | 28738840817 | 720 |
| [1294e12,1295e12) | 28738157321 | 726 |

Total: 114956492689 primes and 114956492688 consecutive pairs.
Every block boundary was included: 114956488689 internal pairs plus 3999
cross-block pairs. The three cross-cell pairs have gaps 76,92,20.
The observed first/last primes bracket the required band with a wide margin.
The production reducer took 2163.4557326 seconds; actual command timings and
streams are retained separately from the earlier pilots.

The complete source invariant, gap-start coverage proof and attestation basis
are in [the completeness certificate](../research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910/COMPLETENESS_CERTIFICATE.md).
The [audit](../research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910/construction_audit.json)
validates every block and all four independent count differences.
[The catalogue](../research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910/catalogue.json)
contains zero rows with the canonical empty-row SHA-256.
[The exact scanner output](../research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910/accepted_scanner_result.json)
and its actual argv/exit records are included.

Independent trial-division verification used a separately constructed complete
prime basis through 35981714. It verified both prime endpoints and supplied
composite factor witnesses for every interior integer of seven important gap
witnesses. This verifier does not call libprimesieve. There are no dangerous
916 rows or candidates left to verify; that absence follows from the complete
construction, not from the pilot. All 4000 original block records were
losslessly packaged and byte-for-byte roundtrip checked.

## Provenance and method boundary

The existing libprimesieve 7.5 implementation was executed unchanged through
its official Python 2.3.0 distribution. The compatible isolated runtime,
wheel hashes, adapter code, independent checks, source tables, complete raw
block archives and every numerical command's argv/exit/stream digests are
preserved. The [source ledger](../research_artifacts/R005_Q78553_CATALOGUE_050E43_20260910/SOURCE_COVERAGE_LEDGER.md)
distinguishes first-occurrence data, aggregate counts and actual local coverage.

BRC was applied as an observer/provenance constraint: labeled gap events and
ordered boundary ports were retained before threshold projection. Counts or
first occurrences were not substituted for start positions. The complete
sieve and existing accepted scanner were reused; the independent verifier
composes the canonical integer trial-division seed helper with an independent
sieve. This is a finite computational result and task-specific certificate
adapter, not a new general tool family or a formal compiler/hardware proof.

This task was nonblind and used the supplied accepted sources. Independence
claims above concern distinct numerical algorithms and reference data, not
a clean blind researcher context.

## Durable handoff and remaining authority

Use FINAL_SOURCE_MANIFEST.json for final delivery paths and byte/Git blob
hashes. The original startup is pinned at ec8275ee4bf0a7ff9da925dcfd96bcec3c09f1df;
the pilot/first-cell source is dbbe3da5f02901671c19f2a2bffc7049c8c6c2e3.
Earlier checkpoint manifests retain their source-time meaning.

The new immutable Result binds this return to the actual execution. The Driver
must review the finite coverage, count references, archive roundtrip, independent
witnesses, scanner and exact source bindings before acceptance or a frontier
change. Parent closure, later-q dispatch, Working Truth and Foundation remain
separate decisions. No mathematical completeness residue remains for this
finite band under the stated recorded-execution assumptions.

