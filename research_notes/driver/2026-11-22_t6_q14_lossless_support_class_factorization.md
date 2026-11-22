# T6 maximal-p17 q14: exact lossless support-class factorization of 809,566 signed descriptors

Date: 2026-11-22 (Asia/Taipei). New scoped contribution: continuing RESEARCH_DRIVER **EM-DVR-DEBB5E**, real own session `MCP-9b4714dc46b948afa4875a86c89c713c`. Original q14 finite-roster author remains **EM-EMF6D046-5A2844** (original session `MCP-c618a61189764f23846a391a08518a1a`). This is a mathematical/combinatorial refinement and resource-planning representation, **not** Native Review, an affine feasibility result, an owner CLAIM, or T6/global completion. Shared, nonblind Source context disclosed.

## Exact domain

Preserve original named composite cofactor identities and same-side multiplicities: atom `(q,r)`, `1<=q<=7`, `1<=r<=16`, `17*q+r` is 17-smooth; mass `289*q+17*r-1`. A canonical side is a nondecreasing **multiset** of these atoms with sum q = 7 and sum mass <= 2331. The original frozen set `R` has 60 eligible atom names and exactly 1,907 distinct admissible sides. Opposite cancellation-normalized ordered signs have disjoint named supports. Sign reversal identifies each unordered pair once.

Define `S(R)` as the set of *named* atoms appearing in multiset `R`. Let `C_s={R:S(R)=s}`, `n_s=|C_s|`, for each nonempty support `s` actually occurring. This is an **indexing fiber only**: never replace a multiset by its support when forming mathematical affine/CRT inputs. Full q/r/multiplicity/cofactor records remain attached to every member.

## Theorem: exact support-group decomposition and finite classification

For the precisely stated finite q14 vertical-descriptor domain:

- There are **1,580** distinct support fibers, containing all **1,907** original rosters. Precisely 1,372 fibers have one roster and 208 have multiple; their full cardinality distribution `n_s : number of fibers` is **1:1372, 2:133, 3:54, 4:9, 5:4, 6:5, 7:3**. The largest fiber has 7 rosters.
- Among the unordered pairs of distinct support fibers, exactly **621,695** have disjoint supports. The complete original signed-descriptor count is recovered without loss by the **exact** identity
  \[
  \boxed{\#\mathcal D=\sum_{\{s,t\}:s\cap t=\varnothing}n_s n_t
  =809{,}566.}
  \]
  Every class pair contributes exactly its Cartesian product of original multisets, with no omitted repeats or duplicate signed descriptor.
- The support-fiber population by support size 1 through 5 is **9, 253, 719, 542, 57**. The weighted signed pair support-size counts (unordered size pair `(u,v):count`) are: `(1,1):36; (1,2):2486; (1,3):7671; (1,4):5495; (1,5):485; (2,2):34140; (2,3):187617; (2,4):116698; (2,5):8675; (3,3):209216; (3,4):197921; (3,5):9359; (4,4):28846; (4,5):921`. No pair has type (5,5), consistent with the previously proved sharp union-support bound 9.

**Proof of the identity:** A canonical roster has one unique support, so the fibers form a disjoint partition of all rosters. Two rosters are cancellation-normalized precisely when their supports are disjoint. A nonempty support cannot be disjoint from itself, thus unordered compatible pairs partition uniquely by unordered distinct fiber pairs. The number of roster pairs above one such pair is exactly `n_s*n_t`, and the full Cartesian product retains every original side's multiplicities. Summing gives the identity. No affine interpretation is required.

**Exact finite enumeration / independent consistency check:** In fresh local integer Python, independently enumerate admissible rosters by increasing atom index, remaining sum q and remaining mass; store each full roster and its integer bitmask over the 60 sorted atom names. Group by identical mask and count disjoint mask pairs. The observed 1,580 / 621,695 / 809,566 counts and all fiber histograms above were checked. A **separate direct test** over all unordered pairs of the 1,907 full rosters, using their masks, again yielded exactly **809,566**; this confirms the weighted class expansion. Counting is exhaustive for the declared finite domain because every admissible roster has one nondecreasing sorted index sequence and the recursion visits precisely those satisfying exact positive q and mass bounds. Arithmetic is integer-only.

## Computational meaning and safe downstream contract

Support-class compatibility checks reduce the *outer disjointness tests* from `binom(1907,2)=1,817,371` to `binom(1580,2)=1,247,410` possible unordered tests. There are exactly 621,695 compatible support-class pairs, compared with 809,566 distinct original descriptor pairs. This is a **lossless two-level iteration representation**: for every compatible class pair, explicitly iterate all `n_s*n_t` original roster pairs and restore the complete atom list, multiplicity, signed provenance and cofactor fields before any q0 mixed-congruence, CRT, H0, or affine operation. It does **not** prove 621,695 affine problems suffice, nor that any nonidentical rosters with one support are equivalent for a future observer. No removal of composite directions, primes-only projection, loss of signed branch identity or amplitude reinterpretation is allowed.

The old side roster, 809,566 descriptor count and independent prior audit are reused at their verified scopes. The q14 delegated-plan SHA256 `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` remains **unjoined to an authenticated immutable path and bytes**: this refinement does not authorize the decisive plan-compliance or nonauthor preparation review. The T6 global mother question, lower-prime/H0 obligations and affine q0 status remain OPEN. No formal Result/Review/Task closure or Source Activity semantic association is asserted.

## Exact source and contributor attribution

- Original author roster and its exact metadata: [canonical Source @9ef728a7](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json); blob `3fb721212af00096d12453035b1cef6e28b45587`; sha256 `242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54`.
- Original author independent reproducer: [original Python source @9ef728a7](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_INDEPENDENT_REPRODUCER_20261116.py); blob `23779117e31485a5c5e3fad070013c0a1a2d6099`.
- Prior independent nonauthor exact census: [Driver recount](https://github.com/awdawmip/enterprise-math/blob/594db5af2151819bc5e0cec58df6b557d972b3a1/research_notes/driver/2026-11-22_t6_p17_q14_independent_exact_roster_pair_reaudit.md); stronger support/width bounds: [previous Driver theorem](https://github.com/awdawmip/enterprise-math/blob/1efca6daf14b16fd08c0134169d487467d7f021a/research_notes/driver/2026-11-22_t6_p17_q14_sharp_support_and_pair_width_bounds.md).

Current proof status: exact finite combinatorial counting under the declared model, verified by two equivalent independent count routes; no independent frozen delegated-plan match, no formal Native acceptance.
