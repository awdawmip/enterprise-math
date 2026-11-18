# EC49DK — Uniform origin-fibre saturation at eight native signed-X6 steps

**2026-11-01 · AUTHOR ANALYTIC FINITE-CERTIFICATE THEOREM / EXACT Q-CHECK PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.**

## Fixed authority, sources and scientific scope

- GLOBAL_KNOWLEDGE_V1 verified canonical `main@7e623e2746c8af0a97a8b6fcff6ebf7f93f2dff0`: `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, P000 V4 (`projects/enterprise-math/P000_REALITY_FOUNDATION.json`), its startup projection, ACTIVE `我眼中的世界.md`, mathematics/BRC/code and research-activity policies.
- Enterprise Math canonical `main@c1b3200a053883f81951d54f5d55356daec114ce`: current AGENTS entry, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, native signed-X6/BRC typing. Existing author frontier: EC49DJ PR #1730 `e65fb62955a5326c70b03acc01f1a5fdd1579287`; this result does not modify P000 or worldview.
- Source unchanged native kernel: Git Blob `300a96e3dc24bf6fff73743037a0347a8bc83176` (`native_signed_brc.py`, also shipped verbatim in predecessor EC49DB/EC49DC evidence). The separate executable `CROSSCHECK_EC49DK_NATIVE.py` invokes its `endpoint_weight` and `return_multiplicity`, and checks against an independently coded closed-walk multinomial sum at lengths 0,2,4,6,8.
- **Scope:** finite future observer of *literal ordered 12 signed spatial primitive step alphabet* `±E1,...,±E6` with complete six-component endpoint `D=0`. This is a path/BRC algebraic observer, not six-dimensional physical-time dynamics, signed amplitude cancellation, or a three-dimensional slice theorem. All prefixes are counted as distinct paths; ordered A/B tags and seam interactions are retained. No model assumption about a native 2D plane is made.

## Exact object

The primitive axis steps are signed integers `±1,...,±6`. Only **positive** steps on axis `j` multiply the two separate positive BRC instruments by `(x_j,y_j)`; negative steps multiply by one. Path-count instrument is `1`. The strict-positive affine-collinear reference parameter is

```
x=(2,3,1,2,3,4)
y=(5,7,3,5,7,9)=2x+1.
```

The final joint A/B tag is `(A_exists,B_exists)` with ordered *adjacent* native step pairs `A=(+E1,+E2)` and `B=(+E2,+E1)`; label values `0=none, 1=B only, 2=A only, 3=both`. The complete future alphabet is

```
a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2),
d=(2,1,-2,-1), e=(3,1,1,-3).
```

For a prefix of any fixed even length `n` ending at `D=0`, the exact-depth `h` observer has one independent output coordinate per complete future operation word of length `h`, final tag, and instrument (`W_x,W_y,count`), and only uses returning suffixes. The cumulative observer uses lengths `1..h`. All comparisons are exact rational-linear ranks. Returning operation words for `h=2` are precisely `ae,cc,cd,dc,dd,ea`; for cumulative `1..2` add `c,d`.

## Theorem — uniform all-h origin-fibre saturation at absolute native length 8

For this reference parameter and *every integer* `h>=2`, the origin-return fibre at primitive-prefix length `n=8` reaches its maximal future-observation rank:

\[
 \dim O_{D=0,n=8}^{=h}=\begin{cases}18&h\text{ even},\\15&h\text{ odd},\end{cases}
 \qquad \dim O_{D=0,n=8}^{1\ldots h}=18.
\]

Moreover, for **each** language the first even native prefix length with the above full rank is **exactly `n=8`**. These are *local origin-fibre* saturation lengths, not global `n_sat(h)` across all returning displacement fibres. They do not contradict EC49DJ's extreme-fibre obstruction at `2h+8` or EC49DI's different parameter stratum at `2h+10`.

### Upper bounds: six safe ordered-history features

For each prefix let `F00,F01,F10,F11` be the indicators of its own complete A/B tag. Let `p_A=1[no A and final primitive step +E1]` and `p_B=1[no B and final primitive step +E2]`. Each whole future operation **ends negative**, so there is no new A/B pair between complete operations. An A/B seam with the prefix can arise only if the first operation is `d` (new A from trailing `+E1`) or `c` (new B from trailing `+E2`). Thus *all* future tag functions are linear combinations of

\[F_{00},F_{01},F_{10},F_{11},p_A,p_B.\]

For example `cc` has final tag A-only exactly on `F00+F10-p_B`; `dd` has final B-only exactly on `F00+F01-p_A`; `ae` preserves each of the four prefix tags. Because each returning whole future suffix has a path-independent multiplicative BRC factor, the full output lies in the span of these six features times three independent instruments: rank at most 18 at any horizon.

When `D=0` and `h` is **odd**, the number of `a` and `e` operations is equal and `b` cannot occur; therefore at least one `c` or `d` occurs, forcing final tag A or B. In this odd exact language all outputs factor through five features

\[1,\quad F_{00}+F_{10},\quad F_{00}+F_{01},\quad p_A,\quad p_B.\]

The rank is therefore at most 15, for *all* odd `h`.

### Actual full-rank eight-step signed-native witnesses

`EC49DK_WITNESS.json` contains **18 distinct literal ordered primitive prefixes of length 8**, all with exact six-axis endpoint 0, four positive and four negative steps, and their fully named future output coordinates. The standard-library `VERIFY_EC49DK.py` reconstructs every complete prefix/suffix word, BRC product and seam tag; it does not accept a supplied rank without recomputation.

For the **even base** `h=2`, the 18×18 integer minor consists of four `ae` final-label blocks (3 instruments each), one `cc` A-only block (3 instruments), and one `dd` B-only block (3 instruments). Its *exact signed integer determinant*, recomputed by fraction-free Bareiss elimination, is

\[
 \boxed{\Delta_{\rm even}=-26018196083657455104000000000000000000\ne0.}
\]

Modulo 1,000,003 and 1,000,033 this is respectively `914238` and `266603`. The 18 rows are genuine signed-X6 prefixes, not abstract feature placeholders. This yields exact rank 18 for `=2`, and for every cumulative horizon `1..h` with `h>=2` because these original six suffixes are included.

For the **odd base** `h=3`, 15 of those stored paths and 15 specifically named `ace,ade,cae,dae` returning suffix/tag/channel coordinates give another exact integer minor

\[
 \boxed{\Delta_{\rm odd}=-3902729412548618265600000000000000000000\ne0.}
\]

The respective prime residues are `135289` and `989163`. Thus the exact-3 language attains its 15-dimensional upper bound at length 8. The certificate is stored in `odd_h3` of the same JSON and recomputed, not trusted, by the checker.

### Uniform extension of either certificate to *arbitrary h* (not extrapolation)

The complete two-operation suffix `ae` has exactly zero six-axis displacement, contains neither A nor B, starts negative and ends negative. For each initial returning future word `w` append `(ae)^k`. The suffix remains returning, its final A/B tag on the complete prefix-plus-suffix stays exactly the same, and its three BRC/count channels multiply by

\[(4^k,75^k,1).\]

For every selected three-instrument output block the determinant is multiplied by `(4\cdot75)^k=300^k`. Since the even minor has six full instrument blocks and the odd minor five,

\[\Delta_{=2+2k}=300^{6k}\Delta_{\rm even}\ne0,\qquad
\Delta_{=3+2k}=300^{5k}\Delta_{\rm odd}\ne0.\]

These identities establish the universal quantifiers `h>=2` without enumerating an unbounded future language or silently erasing provenance. The checker independently rebuilds each extended integer matrix for `h=2,...,9` and confirms the exact scaling formula.

### Proof of first saturation at length 8

A returning primitive prefix of length `n=2m` has *exactly m positive steps*. All return prefixes at lengths `0,2,4,6` can be **exhaustively generated** by choosing a positive six-axis multiset of size `m` and permuting the multiset together with its equally many negative steps. Counts are `1,12,396,19920`, with no missing path families. From each actual word the checker builds (a) the full `=2` and `1..2` observer response, (b) the six-feature instrument response and (c) the five-feature response for odd horizons, and computes their **exact rational** ranks (not just modular lower bounds):

| prefix n | total actual zero-return native words | full six-feature rank | odd five-feature rank |
|:---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 2 | 12 | 4 | 4 |
| 4 | 396 | 9 | 9 |
| 6 | 19920 | 15 | 13 |

The exact-depth `h=2` and cumulative `1..2` full direct observer ranks equal the six-feature column rank in all four rows. For arbitrary even `h`, the six-feature rank bounds the output; for odd `h`, the five-feature rank bounds it. Consequently at every native length below 8 the full rank 18/15 cannot occur. Odd primitive lengths cannot have six-axis endpoint zero at all. This proves minimality **for the displayed parameter**, using exact finite enumeration to supply the small universal prefix-side bounds, and the algebraic source-independent feature-factorization to propagate those bounds to all h.

## Generic affine-positive extension (bounded statement)

Keep `x_i>0`, `a,b>0`, `y_i=a x_i+b`. Both eight-step witness determinants are polynomials in these eight real parameters. Their nonzero values at the displayed strictly positive point prove that their product is a *nonzero polynomial*. Hence on a **nonempty Euclidean-open, dense (indeed relative Zariski-open) subset** of the positive affine parameter domain, the same eight-step witnesses saturate both parity-specific exact observers and every cumulative observer, uniformly in every finite `h>=2` by the same `ae` lift. This generic statement is about **attainment by n=8**; the above exact pre-eight rank table and hence odd-h first-attainment assertion were established for the **displayed parameter**. No claim of an exhaustive classification of the exceptional weight hypersurfaces is made.

## Validation actually executed

- `python3 VERIFY_EC49DK.py`: `PASS`; exact 18×18 and 15×15 Bareiss determinants, nonzero residues modulo 1,000,003 and 1,000,033, eight independently rebuilt suffix extension matrices (`h=2..9`), **1+12+396+19,920=20,329** exhaustively generated native words for exact rational short-length ranks, and the two full future languages `=2`/`1..2`. The `EC49DK_EXECUTED.json` and `EC49DK_RUN.log` capture the output.
- `python3 CROSSCHECK_EC49DK_NATIVE.py`: `PASS`; actually runs the unmodified BRC `endpoint_weight`, `return_multiplicity` kernel, separately comparing independent combinatorial sums for `n=0,2,4,6,8`. At `n=8`: **1,281,420** closed native paths, aggregate `W_x=46,647,930`, `W_y=1,582,111,020`. `EC49DK_NATIVE_CROSSCHECK.json` records the exact values and native Git Blob.
- Search provenance: an exploratory seeded balanced-word search selected the 18 path witness from genuine eight-step zero-return words; the published deterministic verifier reconstructs the final certificate without relying on randomness or that search procedure. All exact rational ranks use Python's `fractions.Fraction`, with no floating approximation.
- **Independent review not yet performed.** This is an author-side mathematical proof in the *specified* finite observer, not a formal task Result, accepted theorem, native physical evolution or an assertion about all displacement fibres.

## Live control and scope

Native Sites gateway reported `research_authority_granted=false`, control Source `UPSTREAM_CODE_REVIEW_REQUIRED`; bounded active-owner inventory returned `CONTROL_QUOTA`. No task owner, own source-issued research session, formal CLAIM, Research-Activity, Result, or independent Driver review was established. This non-privileged portable scientific unit is authored as `PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`; no project Worldview/P000 change. The GitHub PR handoff is durable research material, not canonical admission.

## Next precise research unit: EC49DL

Classify when the same universal eight-step origin-fibre theorem persists *on exceptional affine-positive parameter subvarieties*, distinguishing certificate polynomial zeros from actual reduced rank. In parallel, for the **same explicit affine-collinear reference**, find a genuinely new uniform-length local certificate or exact lower-rank obstruction for **other internal return displacement fibres**. Reuse the six-feature quotient and neutral two-operation suffix as exact tools, and do not infer global `n_sat(h)` from this origin result. Independently audit the six-feature upper-bound proof and two integer minors before any formal admission.
