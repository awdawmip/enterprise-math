# Complete native-word certificates for reuse

This unit implements the sufficient certificate proposed in the frozen adaptive package's `precision_theory/PREFIX_INDEPENDENT_WORD_CERTIFICATE.md` at Enterprise Math commit `c0f04346c520fddc8016c86227b3b6cc2e9f30f6`. Its role is to replace repeated covariance-dependent tests for one omitted feedback word with a paid reusable bound. It does not remove the sampler's mass/correlation queries, provide a generally efficient sampler, or reproduce the RP1 low-precision experiment. This is shared-author work, not independent admission.

`WordCertificateBank(program)` reconstructs every supplied complete native word by actual full-carrier forward, inverse and inverse-recovery basis replay. The inherited complete-word cache is explicitly cleared before each word. It binds the exact native words, all columns, the complete carrier and any exact codec. Every entry of the full 61-dimensional matrices below has an address into an actually executed signed `PositivePathObserver` expression:

\[
G^T G-I,\quad D=I-G,\quad B=D^T D,\quad B^2-sB,
\qquad s=\tfrac12\operatorname{tr}B.
\]

Identical expression factor sequences share one actual observer receipt. Contributions with a zero source factor are absent paths; even a wholly zero expression points to one executed zero observation. This avoids repeating thousands of identical zero computations while retaining all 61-by-61 entry arrays and their receipt indices. No principal-plane target angle is substituted.

The word passes precisely when every residual entry is zero and `0 <= s <= 4`. Symmetry and positivity of `B` follow from its observed construction, and its eigenvalues then belong to `{0,s}`. Hence `||I-G||^2 <= s`, with equality for this trace witness, including `G=I,s=0`. A failed scalar witness is retained, not promoted to a bound. A complete single native reflection is a deliberate failure fixture: `s=2` but the `(0,0)` entry of `B^2-sB` is `8`.

If the actual chronological feedback products differ only by omitting this word, write them as `L G R` and `L R`, with common orthogonal factors. Their difference has the same operator norm as `G-I`; no factors are commuted. The adaptive instrument theorem therefore permits a rational local charge `e` whenever

\[
0\le e\le1,\qquad 8s-s^2\le16e^2.
\]

This bound holds for every input, including zero raw-mass prefixes. Conditioning on such a prefix remains invalid; the caller's probability method must still reject normalization of zero mass. The uniform policy and its path-consistent charge ledger are implemented and checked in the sibling `uniform_execution` unit.

`check(program)` binds exact program phase columns and codec and deliberately excludes `N`, `a`, work modular powers and history. Thus one bank may be reused across admitted programs with precisely the same phase bank and codec. It performs host source-data comparisons/serialization, not fresh scientific observations. This CPU work is not claimed free. `get(m)` returns a frozen record with `s`, `accepted` and `certificate_sha256`; the bank itself is frozen. Exported evidence is a detached copy. Arbitrary monkeypatching of Python classes or `object.__setattr__` bypasses is outside this trusted in-process interface.

`restore(program, serialized)` accepts a JSON object or serialized JSON bytes/string. It verifies the logical hash, pays fresh full-native construction and observations, and compares the complete logical payload using strict JSON bytes. Rehashed altered scalars, full columns, residuals, observer outputs, codec claims and boolean/integer substitutions are not accepted. A failed fresh replay comparison retains the newly incurred setup evidence. Historical timing/call-index fields are provenance rather than mathematical premises; the returned bank always contains this replay's newly observed setup receipts.

The six-coordinate case is checked only after complete 61-column replay. Both forward and inverse cross-block entries must vanish, and the complement must be exactly identity. The norm witness itself is still computed on all 61 coordinates. A full-61 bank and a six-coordinate bank are separately bound objects even if their scalar bounds agree.

The complete execution result and cost counts are recorded in `WORD_CERTIFICATE_SUMMARY.json` and the full `WORD_CERTIFICATE_RESULTS.json.gz`. Setup receipts separate inherited program/bank admission from this certificate constructor, retain complete native-word replay and observer call intervals, and include failed and replayed candidates. Stored matrix/column counts are explicit scalar-slot counts, not total memory measurements: entry-address maps, words, native receipts, Python objects and serialization storage are additional. Warm reuse savings must be measured together with the cold setup and the underlying sampler; a faster per-prefix decision alone is not an end-to-end speedup claim.

The bounded checker compares the complete-61 and exact-six certificates, reuses one bank across four admitted programs, exercises serialized fresh replay and mutation controls, and preserves both the failed reflection and the all-identity boundary. These finite checks certify their supplied words only. A more general determinant-positive trace bound is discussed separately by the mathematical reviewer; it is not silently substituted into this version's acceptance rule.

The recorded run passed. The actual scalar witnesses for phase indices `2,3,4` are respectively `2`, `38415/65536`, and `640927/4194304`. The three-word cold certificate construction used 205 distinct signed observer calls and took 8.16 seconds in this run, after separate native bank/program admission. The complete-word cache was cleared and all 61 basis columns were replayed each time, while the lower-level primitive cache was already warm: complete replay incurred zero *new core calls*, not zero native-word application or CPU cost. Twelve checks and 36 lookups across `N21/a2`, `N21/a4`, `N65/a3`, and `N15/a2` incurred no additional core calls. Twelve negative controls passed; the failed reflection's nonzero residual and the identity's `s=0` are both retained. Full and encoded carriers gave equal scalar witnesses.

The whole checker, including admission, positive and negative fresh replays and extra boundary fixtures, used 2,100 core calls and 84.52 seconds. Its raw evidence is 15,151,836 bytes (SHA-256 `c4a88c9bd19b9ac6c3b96ac9f42f339f436a48c32fdcb6a5230d37cb3a666e44`), stored losslessly in a 398,808-byte gzip. The primary cold bank's logical evidence occupies 1,382,158 serialized bytes and explicitly stores 44,652 full-matrix scalars plus 22,326 complete-column scalars, before the additional address/observer records. These are bounded execution measurements, not a matched end-to-end speed comparison.

Global-Knowledge-Sync: main@4b04602b / GLOBAL_KNOWLEDGE_V1
