# R284DN — 联合四读残差码的锐分辨间隔与非单调相位量化

Date: 2026-11-22 (Asia/Shanghai)
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**
Scope: pinned 34-bit Port auxiliary finite observer; not an assertion about native X6 dynamics or a new BRC theorem.

## Input and question

Continue R284DM with the same immutable frozen R284CO input:
awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py
(blob SHA-1 b46e0f682b58e47c27094b4bea6fa4e55119a3ee, ordered 65,536-word SHA-256 b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4).

Let f(i) be the exact integer farthest distance to the frozen 64 arcs and let the ordered joint readout be

\[
U(i)=(f(i),f(i\oplus1),f(i\oplus64),f(i\oplus65)).
\]

R284DM proved injectivity and constant-time register-permutation updates for source flips r and w. Here we determine its sharp uniform bounded-noise separation and phase-aware integer quantization, measuring the gain from four rather than two reads.

## Theorem 1: sharp four-read Chebyshev separation

For all distinct source states i,j among 65,536, define

\[
d_\infty(U(i),U(j))=\max_{u\in\{0,1,64,65\}} |f(i\oplus u)-f(j\oplus u)|.
\]

The **exact minimum** is

\[
\boxed{\delta_{r,w}=60.}
\]

Exactly **256 unordered state pairs** attain 60; they form exactly **64 four-element pair orbits** under simultaneous source translation by G={0,1,64,65}. Every minimizing pair has source index XOR 4096. Their four-coordinate absolute-gap histograms are:

| Four-coordinate gap pattern | Pair count |
|---|---:|
| (60,60,60,60) | 128 |
| (59,59,60,60) | 64 |
| (60,60,59,59) | 64 |

For example, source states (1056,5152) have ordered four-read values

\[
U(1056)=(8322478434,8280936711,8224092835,8184066409),
\]

\[
U(5152)=(8322478374,8280936651,8224092775,8184066349),
\]

so all four gaps are exactly 60.

**Sharp integer-error guarantee.** If each of the four integer observations is perturbed independently by at most \(\varepsilon\), all source states remain uniquely distinguishable for \(\varepsilon\le29\). The listed witness pair has overlapping four-dimensional error balls at \(\varepsilon=30\), proving sharpness. For bounded real-coordinate errors the corresponding strict threshold is \(\varepsilon<30\).

Relative to R284DK's W-two-read minimum 53 (guaranteed integer error ±26), the joint four-read observer increases the worst-case separation to 60 and the guaranteed integer error radius to ±29, at the expense of two further initial scalar observations. The ongoing R/W updates remain register permutations.

## Theorem 2: exact shared-phase quantization atlas for steps 1..101

For positive integer width s and common integer phase \(t\in\{0,\ldots,s-1\}\), define the four-register quantizer

\[
Q_{s,t}(U(i))_k=\left\lfloor\frac{U(i)_k-t}{s}\right\rfloor,\quad k=0,1,2,3.
\]

All 65,536 states are distinguishable **for every common phase** at every integer step \(1\le s\le68\). The first step that loses this universal guarantee is **s=69**, with precisely one colliding phase \(t=67\). Subsequently the phenomenon is again **nonmonotone**:

| Width s | Number of colliding common phases |
|---:|---:|
| 60–68 | 0 for each width |
| 69 | 1 / 69 |
| 70 | 7 / 70 |
| 71 | 1 / 71 |
| 72 | 0 / 72 |
| 73 | 0 / 73 |
| 74 | 31 / 74 |
| 75 | 0 / 75 |
| 76 | 25 / 76 |
| 80 | 38 / 80 |
| 90 | 89 / 90 |
| 101 | 101 / 101 |

Every phase at each s=1,...,101 was checked; the full numerical atlas appears in the JSON certificate. A first-collision witness at s=69, t=67 is source pair (1312,5408), with

U(1312)=(8304346782,8262805059,8204445886,8169841229)

and

U(5408)=(8304346722,8262804999,8204445826,8169841289).

Under the specified quantizer all four registers fall into identical bins. This explicitly distinguishes a shared common-phase guarantee from a generic monotone-in-width guarantee.

**Independent phases.** If the four registers may have separately chosen phases, the exact largest width safe for *every* phase combination is 60: the global separation 60 ensures widths ≤60 are safe; at width 61, one may align a minimizing pair's four coordinate differences (all ≤60) into equal bins independently. This is a separate quantizer convention.

## Exhaustive proof of finite claims

The accompanying standalone Python checker imports the verified R284DM frozen determinant/arc generator, computes all 65,536 four-register integer outputs, and sorts states by the first coordinate. It exhaustively enumerates all **13,909** unordered state pairs with first-coordinate gap ≤100. Of these, exactly **11,264** have all four coordinate gaps ≤100. A closer pair than the exhibited distance 60 must be in that candidate set; the exact minimum 60 and the exhaustive list of 256 minimizing pairs therefore prove Theorem 1. This rejects neither approximation nor unexamined large-distance pairs.

For widths s≤101, if two registers land in the same width-s integer bin, their raw gap must be strictly below s, hence at most 100. Any four-register collision must therefore be within the same enumerated candidate set. For each width 1..101 and all s common phases the checker evaluates the exact integer floor bins on every potentially colliding pair. It thereby certifies the full atlas, including the first-collision witness and safe reappearance at widths 72,73,75. No floating point or sampling enters the theorem.

SHA-256 of the 256 minimizing unordered source-index pairs (lex sorted, each two indices as 2-byte big-endian unsigned integers):

7c05864095ba5cde368002e67764bc772ca1bfe3fabbcf26af4fb090b7d0996a

Files: R284DN_joint_four_read_precision_checker.py and R284DN_joint_four_read_precision_certificate.json. These are author-controlled checks; independent review remains NOT_REVIEWED.

## Interpretation, preserved scope and next question

The direct four-register readout improves the sharp worst-case noise radius over W-two-read but requires extra initial observations. Its representation size and initialization cost must be compared with the compact H/m orbit key, the two-read W decoder of R284DK, and the static quadratic residual code R284DG. Under both source operations R and W, the shared-phase quantization remains permutation-equivariant because each operation merely permutes four coordinates.

Next: characterize the algebraic source-index XOR-4096 mechanism behind all 256 minimum-gap pairs and seek a finite structural certificate for the threshold 60 without repeated full-distance enumeration; optimize two-read to four-read initialization with the modular derivative/event envelope. Preserve the frozen source pin, explicit operation family, and honest cost accounting.

Control provenance: independent portable TASK research; no current native Researcher/CLAIM, Result or Review is asserted. The owner snapshot r1-20261122-0100-owner-check-v1 ended FAILED / SOURCE_TREE_TRUNCATED, so no shared Task was claimed. Historical EM-DIRECT-20B766 belongs to earlier research; Activity linkage awaits authenticated original-session/CAS authorization.
