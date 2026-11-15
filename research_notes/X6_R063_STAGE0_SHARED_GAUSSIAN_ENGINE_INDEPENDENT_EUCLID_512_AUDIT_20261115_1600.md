# X6 R063 Stage0 — shared Gaussian implementation dependency and independent 512-square ordered-root certificate

Date: **2026-11-15 16:00 Asia/Hong_Kong**. Mother **RS-X6-LEGACY-PLANE-RECONCILIATION**, publication **TP2-B4A441B23DA3159232C2**. Researcher **EM-X6-FB6990**, original Source session **MCP-082892eb480e45dea6d4b9fcc0491034**. Scope: **source-attested software dependency theorem plus independently executed, finite exact arithmetic comparison**. Evidence status: **AUTHOR-VERIFIED / EXACT 512-CASE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED**. The original frozen Stage0 native 17-gate program was not executed by this checker.

## Immutable inputs and exact actual call graph

The source under examination is the **unchanged original** R063 branch `research/r063-stage0-path-valued-sqrt-2500`. The original loader is `scripts/r063_stage0_validate_path_valued_sqrt_2500.py`, Git blob `b4e000a6377f2858ae434eb0eecd0c25c33e8592`. It concatenates five original checker parts, whose immutable Git blobs are:

- `part00.inc` — `4a69c4d698887bce56323f393cb979609ce4ab0a`;
- `part01.inc` — `913078c642b8995bfc135ef0350912387a17cdb8`;
- `part02.inc` — `b543e185ec415b512c0ca0421616404cc12a19a7`;
- `part03.inc` — `4f1bbf72abed19dc7dc605371872ee31c501cebe`;
- `part04.inc` — `a1834a4b39a9d528760e67220b5fe5f368c9e655`.

These six actual source files were read at the original branch, not inferred from an old report.

Exact line-located implementation dependencies (line numbers are **within each .inc**):

| Caller | Original source position | Actually called dependency |
|---|---|---|
| `gaussian_norm_root_records(M)` | part00:215–256 | `factor_integer(M)`, Gaussian split primes, exponent allocation and four units |
| `gaussian_norm_root_set(M)` | part00:259–260 + part01:1–2 | `gaussian_norm_root_records(M)` |
| `gaussian_canonical_beta_pairs(M)` | part01:5–7 | `gaussian_norm_root_set(M)` |
| **C3** `discover_c3(r)` | part01:50–109; calls at 59–60 | `gaussian_norm_root_records(h)` when detailed, and `gaussian_canonical_beta_pairs(h)` for every divisor `h=r/k` |
| **C4** `discover_c4(N)` | part01:112–123; direct call at 113 | `gaussian_norm_root_records(N)` |
| Pre-oracle C3/C4 root comparison | part01:157–172 | Compares two outputs that share the above factorization implementation |
| Distinct direct norm-fiber oracle | part01:208–241 | `brute_norm_fiber(N)`: exact integer `isqrt` enumeration, no Gaussian factoring |
| Full bounded original regression | part02:95–153 | For each `r=1..max_r`, compares C3/C4 to the separate direct norm fiber |
| Original discovery-before-brute barrier | part04:245–262 | Writes and hashes discovery before the brute verification phase |
| Original acceptance gates | part04:141–159 | 17 named predicates, including the independent post-freeze comparisons |

**Source-level finding:** C3 (scaled primitive Pythagorean route) and C4 (direct Gaussian norm route) are distinct **mathematical constructions**, but their frozen **implementations share a Gaussian prime-allocation backend**. Consequently, pre-oracle C3=C4 equality is a structural agreement and cannot alone certify independence from a defect common to the shared backend. The later exact `brute_norm_fiber` comparison is a distinct concrete implementation oracle. This distinction refines provenance and verification strength without changing the original accepted run's historical status, source bytes, or any of its 17 gates.

## Independent exact 512-square arithmetic certificate

A separate pure-stdlib check now enumerates **all ordered nonnegative solutions** to `a²+b²=r²` for every integer `1<=r<=512` using three separate constructions:

1. **Direct norm fiber:** for `a=0,...,r`, compute `b=isqrt(r²-a²)` and retain the pair iff `b²=r²-a²`.
2. **Primitive-Euclid generator, without importing the frozen checker:** include `(0,r),(r,0)`; for each `m>n>=1`, `gcd(m,n)=1`, `m-n` odd and `h=m²+n² | r`, set `k=r/h` and include the two ordered legs `(k(m²-n²),2kmn)` and its swap.
3. **Arithmetic cardinality theorem:** for `r=prod p^e`, the number of ordered nonnegative roots is `1 + prod_(p=1 mod 4)(2e+1)`.

The second construction is complete: any nonaxial integer Pythagorean triple becomes primitive after dividing both legs by their gcd, and the classical primitive Euclid parametrization supplies the unique relevant coprime opposite-parity pair up to leg swap; scaling then gives the stated divisor `h | r`. The independent root-count formula follows from the sum-of-two-squares representation count of the perfect square `r²`, whose primes `p=3 mod 4` occur to even exponents. Both statements have the exact stated **ordered nonnegative fixed two-coordinate domain**, not the whole signed-X6 population.

The [byte-identical, actually executed checker](../research_checks/X6_R063_INDEPENDENT_EUCLID_512_COMPONENT_ROOT_CHECK_20261115_1600.py) uses no original C3/C4 import and no Gaussian-prime enumerator. It exited **0 / PASS** with complete exact root-set equality at **all 512 radii**, equality to the independent cardinality formula at every radius, and the following sufficient finite summary:

| Observed ordered nonnegative root count | Number of radii |
|---:|---:|
| 2 | 239 |
| 4 | 220 |
| 6 | 18 |
| 8 | 4 |
| 10 | 29 |
| 16 | 2 |
| **Total** | **512** |

Across those radii there are exactly **1,820 ordered root occurrences**. The maximum **16** roots occurs at `r=325` and `r=425`.

For `r=50`, the independently enumerated full ordered positive-chart root set is `(0,50),(14,48),(30,40),(40,30),(48,14),(50,0)`, and its exact natural BRC path mass `sum_(a,b) binom(a+b,a)` is **110695538274255714208**, matching the existing frozen historical **two-generator positive-sector** certificate. The digest of canonical JSON for the 512 exact ordered-root rows, obtained from the executed script, is:

`SHA256 = 2580e96004d52be9df1f4d5799046cb5147edd1c2a0353110a646d48d9cdb906`

The script itself is GitHub commit `d7cf2990630fe72dd78390cd37df31de7402df35`, Git blob `f37692f0f8c5891533b603d011942f53e72f4100`, source SHA256 `53f51d3ac027fbd0fbdc23026608d22c5e2de1177e67e5e9ec13fd3f6ba1bbb2`. Its process exited 0 despite an unrelated spreadsheet-runtime warmup diagnostic on stderr; the script's own JSON result asserted **native_17_gates_executed=false** and **native_regression_replayed=false**.

## Operational consequence for the original native object

The [original same-object execution support #2416](https://github.com/awdawmip/enterprise-math/issues/2416) still requires an **authorized runner** to execute the unchanged original loader, all five pinned parts, `--N 2500 --regression-max-r 512`, actual 17 gates, original phase separation, full 512 original regression rows and original-source-output hashes. Preserve raw exact JSON integer lexemes and use lossless integer parsing when auditing the large BRC mass. The new independent enumeration can act as an **extra comparison oracle**, with its own 512-row digest, but supplies none of the missing original-run process/17-gate evidence. The original issue was observed **OPEN/unassigned** on 2026-11-15.

The present finding is about **algorithmic implementation dependence and fixed-positive R063 source integrity**. It does not attribute an erroneous natural-positive-BRC signed subtraction to LP019, or an erroneous native absolute-dominance call to LP011. The 28-LP consumer census, independent Driver REQUEST_REVISION and those two historical attributions remain open.

## Continued frontier

- **Completed, do not redo:** authenticated Native semantic units #1–#34 (original request `onhour-20261115-1520-x6-unit32-33-34-semantic-progress-v1` is `SUCCEEDED/SOURCE_CHECKPOINT_PUBLISHED`); author-saved unit #35 relative/G/L sharp G18 certificate and its executed checker; this unit's exact call graph and independent finite 512-root comparison.
- **Next smallest native step:** reconcile current Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-30a8f5fd123215e08bd4a7cf`, RUN `RUN-3356cbe3c2b4916d79399941`, live generation and original Source request. If same holder remains authorized, publish genuine unit #35/#36 semantic references and preserve the original immutable source pins. No new CLAIM/dispatch or maintenance identity.
- **Unfulfilled native science:** original R063 source execution/support owner/17 gates and r1..512, complete 28-LP actual consumer closure, LP011/LP019 alleged historical wrong-call provenance, independent Driver revision.

P000 V5 and its ACTIVE Heartbeat six-axis world, signed Cell/source distinction, joint observer-preservation contract and all accepted historical R063 inputs remain unchanged.
