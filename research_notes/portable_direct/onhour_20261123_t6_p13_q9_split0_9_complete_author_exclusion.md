# T6 / maximal p13 / q-order 9 / split(0,9): full named-roster exclusion (author computation)

Date: 2026-11-23. Research lane: `chatgpt-research-onhour-enterprise-math-20260923`.
Frozen task scientific input: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca:research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`.
Status: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
The global mother question `T6=2332` remains **OPEN**. This is portable mathematics, not a native winning CLAIM, semantic PROGRESS, review or admission.

## Precise claim

In the established maximal-prime 13, 13-valuation-one subcase, under the previously saved elimination of all higher 13-valuations and the verified saturated twelve-dimensional q0 lattice, **no original admissible collision has vertical total q-order 9 and side split (0,9)** with both original exponent masses at most 2331.

Each vertical atom is identified by `(q,r)`, denominator `a=13(13q+r)`, `q>=1`, `1<=r<=12`, exponent mass `a-1`. Signed q0 compensation `u_r` represents the named denominator `13r`. Keep multiplicity, side, full denominator identities and mixed congruences; lower-prime factors are not suppressed.

The exact necessary conditions from the original observer `H_0,...,H_6`, using the previously established valuation-localization and binomial inversion, are

```
sum_{r=1}^{12} u_r * r^(-j)
 - sum_{(q,r) in V_minus} (13*q+r)^(-j) == 0 mod 13^j,
for j=1,...,6.
```

A complete vertical roster of weight 9 is a multiset with nondecreasing q, with same-q residues nondecreasing, and `sum(q)=9`. The prior verified author calculation completely covers roster lengths 1..6 (630,656 configurations). The new calculation completely covers lengths 7..9 (1,039,064 configurations), in the **four and only four** remaining q-patterns.

| q-pattern | Complete named rosters | Vertical mass exceeds 2331 | Exact weighted-GS recursion nodes | Affine ball leaves | Both masses <=2331 |
|---|---:|---:|---:|---:|---:|
| (1,1,1,1,1,1,3) | 148,512 | 7,999 | 386,908 | 3 | 0 |
| (1,1,1,1,1,2,2) | 340,704 | 16,248 | 894,688 | 8 | 0 |
| (1,1,1,1,1,1,1,2) | 381,888 | 71,145 | 855,438 | 8 | 0 |
| (1,1,1,1,1,1,1,1,1) | 167,960 | 59,651 | 296,858 | 2 | 0 |
| **New lengths 7–9** | **1,039,064** | **155,043** | **2,433,892** | **21** | **0** |
| Prior complete lengths 1–6 | 630,656 | 1,386 | 1,745,382 | 7 | 0 |
| **Complete length 1–9** | **1,669,720** | **156,429** | **4,179,274** | **28** | **0** |

Thus the independently enumerated vertical-mass-overrun total **156,429** exactly matches the prior order-9 integer roster census; **1,513,291** configurations survive the preliminary *vertical-only* budget screening, but none survives the full two-sided lattice/mass test.

## Exhaustiveness and arithmetic

Use the exact `13^21`-index saturated q0 modular lattice. The complete ordered HNF/weighted LLL basis and rational Gram–Schmidt data are obtained by the published exact checker. Its minimum squared GS diagonal is

```
78577530278042129705264382752517501995032553011464356025
------------------------------------------------------------------
4243983974238642688103181306691645151538473248349
```

which is strictly greater than `2*2331^2=10,867,122`. For vertical cost `c<=2331`, every admissible q0 compensation must lie inside squared weighted radius `2331^2+(2331-c)^2 <=2*2331^2`. At each GS coordinate there can therefore be at most the two adjacent integer candidates around the translated center. The exact recursive two-candidate search enumerates every lattice element inside this necessary ball. For a leaf, compute `M_plus=sum_r(13r-1)*max(u_r,0)`, `M_minus=c+sum_r(13r-1)*max(-u_r,0)`; recheck all six modular equalities exactly.

All 21 new ball leaves are stored with the full `(q,r)` roster, signed twelve-dimensional q0 vector, squared radius and exact masses. Each violates at least one side cap. A separate local merge audit independently recomputed source-order enumerator cardinalities/digests, all 21 modular congruences and exact two-sided mass values.

Each source-order slice is a half-open interval, with no gaps/overlaps. Per-pattern roster SHA256 and each slice digest are recorded in the certificate. The enumeration program can regenerate any individual slice with `--pattern`, `--start`, `--end`, `--output`; the helper is a reproducible author checker, not an independent outside review. Original local calculations were actually executed with `fractions.Fraction` and exact integer arithmetic; no floating-point tolerance determines inclusion.

## Immutable evidence

- New complete certificate: `research_checks/T6_P13_Q9_SPLIT0_9_LEN7TO9_AUTHOR_EXACT_CERT_20261123_0900.json`; commit `deab1f069a2f880102a8266217c1bc185c527dad`, blob `c378f9a1a215594b04be8fcf8154cc278bbd1626`.
- Exact replay checker: `research_checks/T6_P13_Q9_SPLIT0_9_LEN7TO9_EXACT_REPLAY_20261123_0900.py`; commit `ef508b179aea89b9926178fb93cd82457ed76876`, blob `15982d93d4154bf594853aa3d3d5b27613a19b5f`. This published checker has not separately undergone post-publication full replay.
- Prior author boundary: `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split0_9_len1to6_exact_author_boundary.md` at `43d7037dce2d58f749bacb6555c992bfa9092401`.
- Local full intermediate calculation file SHA256 `d02116a335d86bb8619e31abbaed501a71e8e82e373ad02a76155f6e6ebbf9bd`; faithful GitHub certificate contains its full witnesses and source-order digest summaries.

## Remaining actual question

This closes only **p13 q-order9 split(0,9)**. The next unworked order-9 sign split is `(1,8)`, followed by `(2,7)`, `(3,6)`, `(4,5)`, with all exact original observer and lower-prime-completion obligations retained. The native formal Source has a *separate* p17 q14 split(7,7) preflight frontier; this portable result does not silently replace that TASK scope.

Current Research-lane identity for the historical Activity record remains unresolved; preserve the original 328 events and do not manufacture a session/claim or review. Native continuation request `onhour-20261123-0818-t6-exact-continuation-ro-v1` was consumed as SUCCEEDED/error=null at its exact Source as-of snapshot; it does not authorize a protected write.
