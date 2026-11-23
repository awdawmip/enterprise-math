# T6 p13 q-order 9, signed split(1,8): exact cancellation-normalized negative roster lengths 1–4

Date: 2026-11-23. Frozen task scientific input: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`. This is an author computation, not formal native PROGRESS/Result or mathematical admission.

**Result:** Under maximal prime 13, valuation-one, exactly one named q-order-1 vertical atom on the positive side and total q-order 8 on the negative side, **all negative vertical rosters of lengths 1, 2, 3 and 4** are excluded after preserving original two-side mass budgets and full six 13-adic mixed congruences. Shared vertical named atoms are cancelled to previously handled lower-order cases rather than counted as new disjoint support.

| Negative roster length | Raw sign-ordered pairs | Cancelled by common named atom | Exact GS recursion nodes | Ball leaves | Budget-valid |
|---|---:|---:|---:|---:|---:|
| 1–3 (earlier in this run) | 81,432 | 5,328 | 193,809 | 3 | 0 |
| 4 (new follow-up) | 411,372 | 54,432 | 893,564 | 3 | 0 |
| **Complete lengths 1–4** | **492,804** | **59,760** | **1,087,373** | **6** | **0** |

For length4 the five exhaustive q partitions are (1,1,1,5), (1,1,2,4), (1,1,3,3), (1,2,2,3), and (2,2,2,2), respectively representing 52,416, 134,784, 73,008, 134,784, 16,380 sign-ordered named configurations with a positive q1 residue. They yield 103,365, 285,100, 154,381, 309,280, 41,438 exact Gram–Schmidt recursion nodes; the only three affine-ball leaves have side mass pairs (1231,4574), (2440,4659), (3388,4197), and thus are all invalid at cap2331.

In the inherited exact 12-dimensional saturated q0 lattice of index 13^21, reconstruct signed `u_r` satisfying
```
sum_{r=1}^{12}u_r*r^(-j)
+sum_{(q,r) in plus}(13q+r)^(-j)
-sum_{(q,r) in minus}(13q+r)^(-j) == 0 mod 13^j, j=1..6.
```
For named vertical side masses cp and cn, the original signed-side mass restrictions imply weighted q0 norm square no more than `(2331-cp)^2+(2331-cn)^2`. The exact minimum Gram–Schmidt diagonal square exceeds `2*2331^2`, so the two-neighbor recursive enumeration is exhaustive. All inclusion and congruence tests use integer and rational arithmetic, then both original side costs are checked.

The full new length4 witness certificate is `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN4_AUTHOR_CERT_20261123_0900.json` at commit `602b3ce685598d1d0cd194a63ca251055c18d65e`; exact replay code for lengths1–4 is `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py` at commit `8676c08bdf43da3ade4364f24eba22b583b30c7c`. Both were successfully read back by the GitHub connector. The compact published checker has not separately undergone post-publication replay. The earlier length1–3 exact certificate is at `9509ae14b87f5edc5768c5002beb998476b7b35a`.

Also during this same run, **all 1,669,720** p13 order9 split(0,9) rosters were completed with zero original-admissible candidate; the authoritative author note is `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split0_9_complete_author_exclusion.md` at `0423e5bc23e3d074e89e0e5c33818013e004c98f`.

**Next exact scientific unit:** p13 q-order9 signed split(1,8) negative roster **length5** (all nondecreasing q compositions and canonical residue multisets); preserve signed full atom identities, cancel common support and test six exact congruences, the same q0 integer affine class and original two side budgets. Thereafter length6–8, then signed splits (2,7), (3,6), (4,5). Global T6=2332 remains OPEN. Independent nonauthor verification and native Source acceptance still pending. Native formal p17 q14 split(7,7) preflight has a distinct Source author/owner boundary and is unmodified.
