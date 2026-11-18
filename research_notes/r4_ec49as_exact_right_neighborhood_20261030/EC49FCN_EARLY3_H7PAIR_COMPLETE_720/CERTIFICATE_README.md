# EC49FCN complete 720-group per-group compact certificate

The UTF-8 base64 file `EC49FCN_720_GROUP_COMPACT.json.gz.b64` is a deterministic gzip (mtime=0) encoding of an exact 720-element JSON array. Decode with `base64 -d | gzip -d` and parse as JSON.

For indices i=0,...,719, the row is `[f_i,[n_1,...,n_k]]`, where `f_i` is the number of distinct signed primitive-step prefix edges in the nineteen fixed witness paths, and each `n_j` is the retained strict-improvement inclusion-minimal antichain count after stage j of the five selected slots. The order of the 720 groups is `itertools.product(combinations(EARLY,3), combinations(H7,2))` where EARLY and H7 have the exact order in the published `VERIFY_EC49FCN.py`.

The last retained stage count is zero in **every** row. Together with the frozen admissible 158-edge witness, these per-group counts give the exact value 158 throughout this finite family. A complete recomputation is available using the Python verifier in the same directory; it outputs `minimum` for each index and verifies the rows. The full original JSON report SHA-256 is `106dad58a04b6d857f928fa561e6ace849d72e30c7c6e3554bd578ea2dda9231`. The exact compressed base64 text in this directory has SHA-256 `580ae342dac8c22cca1314ebb4f781a83a9b6b9878c1f3d619e44c5ecf4b181f` including its final newline. The compact file was decoded and checked locally for length 720 and every terminal zero.

Model input freeze: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Claim classification: author-side exact computation, pending independent Driver review.
