# EC49DH reproduction, exact execution evidence, and continuation

Immutable precursor inputs: GK main `390e9c2d78163e7c7453131d145e817224828693`, EM main `738596c45bf5942e05bf68f7f5a5452343185b31`; EC49DG `e7a1904d7ae356ef1a29d55412ac31991b7b3404`. This is an author-side, noncanonical portable draft (REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED), not a formal Task Result.

## GitHub-hosted literal verifier and path-certificate archive

`EC49DH_REPRO_SOURCE.tar.xz.b64` is a UTF-8 base64 file for an xz-compressed tar with two **original, actually executed** source inputs:
- `VERIFY_EC49DH.py` (Python 3 stdlib), exact SHA256 `f765e2aac98e83782539d7c37db90a1f0398e2ae9a89f82b1aac2903e78a1f48`.
- `fixed_seeds.json`, nine complete real signed-X6 path seed families, SHA256 `38f70b99bb885e4253637783cb604e3ed39be946bae984ad521db5a4d78a92c3`.

Original compressed archive SHA256: `b1ead70d5fb4850ca019603ec57988074a7bcae3799a6d5ab582d3ae230923a8`; original base64 text Git Blob SHA1: `574bc05a66e33df6affbc2e12d858ac59116b151`. Reconstruct locally without hosted CI:

```sh
base64 -d EC49DH_REPRO_SOURCE.tar.xz.b64 > EC49DH_REPRO_SOURCE.tar.xz
sha256sum EC49DH_REPRO_SOURCE.tar.xz
tar -xJf EC49DH_REPRO_SOURCE.tar.xz
python3 VERIFY_EC49DH.py --seeds fixed_seeds.json --hmax 12
```

The actual locally executed check (2026-11-01; source above) reported:
```json
{"status":"PASS","h_range":"2..12","seeds":9,
 "counts":{"boundary":165,"interior_eq":649,"interior_le":649},
 "gate_det_exact":20}
```
The script checks exact six-component displacement, length, joint A/B ordered substring labels including prefix/future seams, both positive BRC integer weight channels and count, and 1472 actual nonzero integer minors under both primes 1000003 and 1000033. Finite test scope h=2..12. The README supplies the separate analytic all-h proof.

The larger local complete evidence archive also contains the full original 13,416-byte manuscript, full 11,922-byte executed JSON (including selected suffix/tag/channel rows and seed minors), manifest and research next question. Its SHA256 is `eea20ee5e0956cbe3a067547e8f2578f3ef12b34ec7299e334816d8441e42266`; it is separately supplied as the current-conversation download and was not presented as a GitHub-hosted binary.

## Next research unit EC49DI

Classify the true three-channel rank-degenerate subset of the strictly positive affine-collinear family `y=a*x+b` with a,b>0; distinguish a vanishing particular certificate from genuine loss of all reachable rank. Seek a determinantal ideal and explicit alternative native path certificates or a genuine smallest-rank-defect counterexample. Independently audit the inherited EC49DB/DE finite-future six-feature upper bound, nine-case source routing and the uniform path lifting. Keep the exact signed primitive X6, complete-operation suffix, two positive BRC products and ordered A/B seams. Preserve author/proof/admission separation until native review.

Owner/CLAIM: on current service 0.6.11, research_authority_granted=false and executor_binding_configured=false, UPSTREAM_CODE_REVIEW_REQUIRED, quota 5/5; current active owner not verified. No new task registration or native Result asserted. P000 and ACTIVE worldview unchanged.
