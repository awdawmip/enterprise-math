# T6 p13 q13 split(6,7) length-two common-fiber counting audit; p17 q14 routing correction

2026-11-28. Existing Driver EM-DVR-DEBB5E, informed shared context. Original p13 author EM-DIRECT-D03BC9. This is a nonauthor exact combinatorial count audit, not a new execution of the author's affine kernel or an independent review of this Driver's own q14 theorem.

## 1. Exact p13 coverage and compression

Read immutable author certificate `7142362dd1345519f4573c92964ab1ac32f2c14d:research_checks/T6_P13_Q13_SPLIT6_7_LEN2_COMPLETE_CERT_20261128.json`, blob fd54667707884b0d13d5398ec79ab2cc6f4f07f7. Negative q partitions (1,6),(2,5),(3,4), all eleven positive partitions of 6. Atoms (q,r), 1<=r<=12, cost 169q+13r-1. A side of order Q<=7 has mass at most (169+155)Q<=2268<2331, so no vertical-only budget truncation of these pattern domains.

For a q group with n available r values and multiplicity m, write M(n,m)=binom(n+m-1,m), M(n,0)=1. For a fixed negative/positive partition, raw pair count is product over q of M(n_q,m_q^-) M(n_q,m_q^+). The two negative q values are distinct. A pair cannot have common named atoms from both negative q groups: their orders sum to 7, while the positive order is 6. Therefore any pair with common support cancels exactly one atom; no double-counting between the two cases. For a shared q, after removing the common atom, the number of residual descriptor pairs is
F_q = product_j M(n_j,m_j^- - 1_{j=q}) M(n_j,m_j^+ - 1_{j=q}).
Every residual descriptor has exactly n_q original representatives obtained by reinserting one shared r, including repeats on the positive side. The residual negative side has only the other q, so no other shared atom can arise. Thus C=sum_q n_q F_q is the raw common-pair count, and F=sum_q F_q is the count of common fibers. The residual pair retains complete signed multiplicities. For fixed residual descriptor the shared atom spends identical positive mass on both sides and cancels in every signed congruence; a representative with the smallest shared mass covers all feasible original members under the independent upper budgets. This proves a sufficient representative rule, not that the author's implementation actually uses it. The source kernel and actual representative selection still require a separate review.

In the author's relaxed domain n_q=12. Independent exact arithmetic over all 33 rows matches every raw count, every common count, and every representative count (raw-common+common/12). Totals: raw 18,409,248; common 2,025,504; disjoint 16,383,744; common fibers 168,792; representatives 16,552,536. A mistaken interpretation of representative_search as disjoint count would incorrectly report 19 row mismatches; the exact fiber count explains all 19. Node count 27,264,515 and one leaf are author-reported counters, not independently rerun.

True maximal-p13 restriction: 13q+r is 13-smooth; counts n_q for q=1..7 are (9,7,7,6,5,5,4). Same formula gives:

| Negative partition | raw | common | disjoint | common fibers | representative upper domain |
|---|---:|---:|---:|---:|---:|
| (1,6) | 440910 | 140310 | 300600 | 15594 | 316194 |
| (2,5) | 342930 | 32060 | 310870 | 4598 | 315468 |
| (3,4) | 411516 | 12054 | 399462 | 1774 | 401236 |
| Total | 1195356 | 184424 | 1010932 | 21966 | 1032898 |

These counts do not certify affine exclusion. The representative count is exact for this pattern-local grouping, not a claim of global minimum across pattern boundaries. True raw domain reduction 93.5068% relative to 18,409,248, disjoint count reduction 93.8297% relative to 16,383,744. No cross-pattern dedup or solver speedup claimed.

Independent witness check: pos [(1,6),(1,9),(2,1),(2,7)], neg [(3,11),(4,10)], q0 signed u=(50,2,9,-4,-8,4,3,3,4,1,2,-2). For k=1..6, compute sum_pos (13q+r)^(-k) - sum_neg (13q+r)^(-k) + sum_j u_j j^(-k) modulo 13^k by extended Euclid; all six residues zero. Direct mass sum gives (4065,2480), both exceed 2331. Cofactors (19,22,27,33,50,62); 19 and 62=2*31 violate 13-smoothness. Thus the reported witness is not a true-model collision.

Reproducer for counts, applied to the 33 frozen rows (JS exact integer arithmetic, all integers <2^53):
```js
function C(n,k){if(k<0||k>n)return 0;let v=1;for(let j=1;j<=k;j++)v=v*(n-j+1)/j;return v}
function M(n,m){return m===0?1:C(n+m-1,m)}
function counts(neg,pos,ns){
 let a=Array.from({length:8},(_,q)=>neg.filter(x=>x===q).length),b=Array.from({length:8},(_,q)=>pos.filter(x=>x===q).length);
 let raw=1;for(let q=1;q<=7;q++)raw*=M(ns[q],a[q])*M(ns[q],b[q]);
 let common=0,fibers=0;for(let q of neg){if(!b[q])continue;let f=1;for(let j=1;j<=7;j++)f*=M(ns[j],a[j]-(j===q?1:0))*M(ns[j],b[j]-(j===q?1:0));fibers+=f;common+=ns[q]*f;}
 return {raw,common,disjoint:raw-common,fibers,representatives:raw-common+fibers};
}
// let ns=[0,12,12,12,12,12,12,12] or [0,9,7,7,6,5,5,4];
// sum counts for the actual rows; compare raw/common/representatives to source fields.
```

## 2. Critical p17 q14 route correction (existing evidence, no new computation)

The previous 00:05 report and the rationale of newly submitted synthesis dvr-20261128-0100-t6-scoped-synthesis-v1 mistakenly describe the q14 plan mapping as unresolved. Same Driver's already-published correction at `7b39dde704a8b9cf2f2626b0a4b6b57dbec1f0d6:research_notes/driver/2026-11-27_t6_frontier_rebase_plan_match_and_no_duplicate.md` explicitly resolves this. Read the actual original plan-byte reconciliation `99e369a4bdb0abefa154f6e8c4dd6e9f62678ee0:research_notes/driver/2026-11-24_t6_p17_q14_unique_split_mass_smoothness.md` blob fc4355795b6d3d256f1c10a51e0277805b18ed58. Current main capsule path `driver_reviews/mcp/MCP-10b3bf1d95f645ce8c0e419e458a2e49/3a113cad9007f35a7c79/T6_Q14_DIRECTION_AND_PAPER_BOUNDARIES_CAPSULE.json` has the same verified blob d7ff901960b862031c247bbc093d2cde3bede839. Prior extraction verified 18938-byte member T6_ORDER14_SINGLE_CONTINUATION_EXECUTION_SPEC.json SHA256 b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24. No new decompression performed.

The alternative full-observer q14 exclusion already exists at `3af9771cfdacb44a3932a79bc54f1f790d812ea5:research_notes/driver/2026-11-23_t6_p17_q14_full_valuation_cancellation_synthesis.md`: 17^2 cancellation via 67-profile three-moment injection, once-17 q14(7,7) via 55,347-profile four-adic injection, arbitrary 17-free completion allowed, and the true mass/smoothness bound forces (7,7). It matches the original frozen plan's scientific domain. Author-side proof and implementation crosscheck, not genuine independent review of Driver-authored proof. Preserve original EM-DVR-F73673, EM-PARITYREV-12B648, EM-EMF6D046-5A2844, EM-X6-FB6990 contributions and other predecessors. Do not repeat roster, old checker or 809,566-affine campaign merely due to stale task wording. Next legitimate step is a genuinely nonauthor decisive audit of the alternative theorem, then permitted native linkage. No automatic cancellation of owner's plan or formal admission.

## 3. Native review control

Original dvr-20261128-0005-t6-post-reference-flow-v1 SUCCEEDED, exact current set as of receipt: DR-0D8591E64A4073A61E6A RETURN_TO_OWNER, RVP-EF36B793D82544FB6AFB RECORDED, DFU-A781ABC4981EC521CA0B followup ready. Current RR blob 62e50de0541fcb25492cffd9354afa8d3a3cda52 unchanged. Submitted new synthesis dvr-20261128-0100-t6-scoped-synthesis-v1 under original own SID/DA, nonterminal RETURN_TO_OWNER preserving existing followup, last RUNNING. Correct its stale q14 ancillary rationale by this explicit source note; disposition remains justified by open global target, not by missing plan. Consume exact original terminal receipt; do not replay or cancel unknown write; if recorded, preserve immutable record and use actual authorized correction route if needed. No new native Result acceptance or Task completion. No claims or task reassignment, no schedule changes.
