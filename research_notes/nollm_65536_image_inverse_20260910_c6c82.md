# Exact 65,536-state image atlas and inverse pixel analysis

Status: RESEARCH_NOTE / EXACT_FINITE_ENUMERATION_AND_ELEMENTARY_DERIVATIONS / NOT_PROMOTED
Progress-Event-ID: NOLLM-65536-IMAGE-INVERSE-20260910-C6C82
Researcher-ID: EM-DIRECT-C6C82
Research-Activity-ID: RA-nollm-hecke-views-20260909-c6c82
Session: local-chat-nollm-hecke-20260909-c6c82 (local continuity key, not a server ID)
Mode: direct user-selected TASK_RESEARCH; no formal Task-ID or CLAIM
Date: 2026-09-10
Source snapshot: enterprise-math@2f2dcd390f6c2c50610f043f56b6bd7fa6c53ba4

## Scope

The user asked to draw these 65,536 numbers exactly and analyze the images backwards. The population is declared as n=0,...,65535, all 16-bit unsigned states. The preceding 65536 was the Q16 denominator, NOT evidence of 65,536 existing semantic memories. The full-scale Q16 endpoint 65536 would be an additional value and is not in this population. No random samples are substituted for this finite set.

This uses ordinary integer/pixel and Euclidean hex-lattice observer coordinates. It does not alter P000, Nollm runtime, physical layers, or an accepted mathematical statement. Repeated 3/4 scoring is a synthetic scalar test, not the preceding actual-kernel path experiment.

Executable: experiments/nollm_65536_image_atlas_20260910_c6c82.py. The support fixed_point.py is the unchanged Nollm helper at repository awdawmip/Nollm, commit 91bd14ab394e87931b45baaaa87671f30fcfd706, path packages/nollm-core/src/nollm_core/fixed_point.py, Git blob 9ea00e3c84a82f480c692a6ca0ca717a579dab60. It is actually imported to recover normalize_q16_weights([72,4,4,4,4,4,4]). The preceding physical-audit package is provenance, not a new full runtime execution or proof that it has been published remotely.

## Exact forward images and inverse reading

Three layouts contain each label exactly once:

1. Row: n=x+256y, 0<=x,y<256.
2. Bit-interleaved (Morton): n=sum_i(x_i+2y_i)4^i. Eight even binary positions go to x, eight odd positions to y.
3. Hex spiral: label 0 at (0,0); ring r starts at (0,-r) and follows directions (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1), with r sites along each side.

The square data images are 256x256, with one 16-bit grayscale sample per label. The hex axial raster is 297x297 with a separate occupancy mask: empty pixels and label zero are never identified. Physical-looking hex previews use coordinates (q+r/2,sqrt(3)r/2), but the exact integers remain in the axial raster.

All three label PNGs are decoded back from disk; mask, min/max, unique-count and sorted-value checks recover exactly 0..65535. PNG headers are checked for 16-bit grayscale. Derivative/period/fiber analysis reads these decoded image arrays, not resampled preview colors. All 55 generated data/mask PNGs are byte-identical across fresh executions. Pseudo-color previews and screen antialiasing are not data encodings and cannot distinguish all 65,536 identities visually.

## Image finding 1: the visible six rays are quadratic sequences

Read the first 147 complete-radius points along the six hex vertex rays. Each ray has constant second difference 6; exact reconstruction is

n_j(r)=3r^2+(j-3)r+1, j=0,...,5.

The six complete finite prime counts are respectively 52,28,36,24,36,20 out of 147 ray points. There are 6,542 primes in the whole declared population. The first ray begins 1,7,19,37,61,91,127,169,217,271,331,397.

Its expression 3r(r-1)+1 avoids factors 2 and 3 for every integer r, which helps explain its visibly dense prime stripe. It does NOT always give primes: 91=7*13, 169=13^2, 217=7*31. The ray formulas arise from this chosen spiral order; no new prime-distribution theorem, asymptotic prime density or natural preferred axis is inferred.

The spiral has 65,269 sites through radius147, then 267 sites from radius148. A complete radius148 hexagon would have 66,157 sites. Moreover 65,536=4 mod6; a finite distinct point set invariant under a 60-degree planar rotation has cardinality 0 or 1 mod6. Thus literal full sixfold symmetry at this cardinality is impossible, irrespective of the chosen spiral. This does not exclude weighted symmetry, covariance isotropy or other populations.

## Image finding 2: encoded blocks are not evidence of emergent number-theoretic symmetry

The decoded row image has horizontal first difference 1 and vertical first difference 256 everywhere. The Morton image has zero mixed second difference. Its horizontal differences are

1,3,11,43,171,683,2731,10923,

with respective counts 32768,16384,8192,4096,2048,1024,512,256. Vertical differences are twice these. If a coordinate increment carries through j trailing one bits, its label change is (2*4^j+1)/3.

Every aligned side-2^k square contains exactly a consecutive block of 4^k labels. All blocks at k=0,...,8 are checked. The visual self-similarity therefore has an exact encoding explanation. On the infinite bit-interleaving chart, multiplication by4 doubles both coordinates. In the present fixed 16-bit population, wraparound matters:

X(2n mod65536)=(2y mod256,x),
X(4n mod65536)=(2x mod256,2y mod256).

The first operation includes an axis interchange/reflection and anisotropic scaling, not a pure rotation. It is not the actual Nollm 22.5-degree layer transform.

The row prime image excludes (except the primes themselves) the diagonals x+y=0 mod p for p=3,5,17, because all three divide 255 and 256=1 mod p. The Morton image instead satisfies n mod3=popcount(x)+2 popcount(y) mod3. These mask changes explain why prime stripes can turn into multiscale textures after a coordinate change.

Morton 180-degree rotation sends n to65535-n. The prime mask and its 180-degree rotation have zero overlapping prime sites. This is not a deep complement law: the sum is odd, so a prime pair would require one member2, while65533=13*71^2.

## Image finding 3: occupancy alone hides odd modular multiplication

For f_a(n)=a n mod65536, each occupied target has gcd(a,65536) preimages, with65536/gcd(a,65536) occupied targets. Checked a=2,3,4,5,6,7,11,16,256.

Examples: times2 gives32768 targets of multiplicity2; times4 gives16384 of multiplicity4; times3,5,7,11 each permute all65536 labels. Hence a binary occupancy image cannot distinguish these odd multiplications. Label channels or a declared provenance field are necessary to invert that observation. Retaining (floor(an/65536), an mod65536) recovers the full integer product and the input for every tested a>0. This is separate from Q16 multiplication.

## Image finding 4: a one-unit weight change has a structured, exactly measurable fingerprint

Define the actual Q16-style scalar map F_w(n)=floor(w n/65536) and the discarded remainder R_w(n)=w n mod65536. Decode their image files and count fibers:

w=2730: 2730 distinct quotients; 2714 quotient fibers of size24 and16 of size25; 32768 distinct remainders; remainder period32768.
w=2731: 2731 distinct quotients; 8 quotient fibers of size23 and2723 of size24; all65536 distinct remainders; remainder period65536.
w=49152: 49152 distinct quotients;32768 fibers of size1 and16384 of size2;4 remainders; period4.

The difference F_2731-F_2730 is1 on32767 pixels and0 on32769 pixels. Every affected result changes by exactly ONE Q16 unit; this is not evidence that half the memories disappear or that the absolute error is large. A floor-sum check gives the same count independently.

The pronounced interference-like bands are explained by

24*2731=65536+8; 24*2730=65536-16.

Therefore advancing24 labels drifts the remainder phase by+8 or-16 modulo65536. Adjacent differences of the decoded remainder image recover the multiplier exactly. The image can thus be used backwards to recover this arithmetic parameter, once the row-coordinate convention is declared.

In particular2731 is odd, so R_2731 is a permutation of all16-bit states. The seemingly intricate discarded remainder alone retains enough information to recover n; the smoother quotient has only2731 values. For all tested weights, the pair (F_w,R_w) exactly recovers n=(65536F_w+R_w)/w. This is a modular-information distinction, not a recommendation to preserve every pixel of arbitrary data.

## Additional finite check: balancing weights is not balancing already rounded products

The earlier three-phase example has neighbor weights2731,2731,2730, whose sum is8192 exactly. However

floor(n/8) - [2 floor(2731n/65536)+floor(2730n/65536)]

is0 for14337 inputs,1 for32768, and2 for18431. Thus the exact three-phase weight average does not remove intermediate flooring. This does not contradict the previous claim about the WEIGHTS; it prevents extending it silently to rounded signal products.

## Execution and files

The full CSV lists every n and its row, Morton, hex coordinates, primality and bit statistics. There are52 raw16-bit scalar images plus3 occupancy masks. Two runs give byte-identical results.json, raw_manifest.json, image_ray_analysis.json and CSV, and all55 PNG files. The source produces these assets without a remote service.

The offline viewer has14 observation modes, three layouts and a180-degree toggle, with exact hover/click values. Browser validation used Chromium with an in-memory copy of the generated HTML:36 inverse-picking checks passed across all three layouts and both orientations; all14 modes rendered without page errors. This is not an exhaustive browser test for every platform.

BRC: REUSE_EXECUTED of the pinned fixed-point normalization. COMPOSE_APPLIED: retain label, position map, occupancy mask, quotient, remainder and branch multiplicity separately. Boolean prime masks, preview colors and occupancy are intentionally lossy observers; none is treated as a full identity map. Existing bit-interleaving is used as a comparison encoding, not claimed as a new tool family or semantic index for Nollm.

Classical context: W3C Portable Network Graphics (Third Edition), https://www.w3.org/TR/png-3/; NVIDIA Thinking Parallel, Part III: Tree Construction on the GPU, https://developer.nvidia.com/blog/thinking-parallel-part-iii-tree-construction-gpu/. PNG and Morton encoding are established. The present output is a complete finite image experiment and its explicit inversion audit, not a priority claim.
