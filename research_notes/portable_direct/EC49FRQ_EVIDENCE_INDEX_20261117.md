# EC49FRQ exact original BRC research evidence index

**Result:** Uniform, complete Pareto domination by three fixed original named trees A/B/C simultaneously for *all* real x in [1,3] and all lambda in [0,1], quantified as FOR ALL legal original deterministic complete trees Q, THERE EXISTS one T in {A,B,C}, FOR ALL parameters in the rectangle, C_T <= C_Q.

**Proof:** \`EC49FRQ_LOW_PRICE_UNIFORM_PARETO_COLLAPSE_20261117.md\`.

**New programs in this PR:** \`EC49FRQ_LOW_PRICE_PARITY_DP_20261117.py\` (all 228 original observations, 209 equal-price/equal-partition reductions, full witness reconstruction) and \`EC49FRQ_INDEPENDENT_ALL228_20261117.py\` (independent raw 94-family BRC master/CSV parsing; all 228 original observation indices, no partition quotient). Files in the self-contained archive carry equivalent executable program names without the GitHub date suffix, together with raw data, inherited certificates, four new parity witnesses and complete original A/B/C tree files.

**Exact frozen scientific input:** \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`.
Original BRC master SHA256 \`cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`.
Original root-cost/profile CSV SHA256 \`a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`.

**Primary original-state computation:** 310 configurations, 141 complete named profiles, 228 named physical observations, 209 same-price-distinct partitions, 12,922 Bellman subset states per run. At x=1 and objective 24U1+M1: exact minimum even/odd (7861,7886). At x=1 and objective 19U1+2M1: exact minimum even/odd (7080,7099). Supplementary x=2 parity objective 49U2+M2 yielded (15561,15561). All feasible primary parity witness trees checked by replay over original named profiles.

**Independent implementation:** reconstructs all raw 228 physical named observations from the original master and profile CSV, does not import primary response vectors, does not collapse duplicate observations, and returns **(7861,7886)** and **(7080,7099)** on the 141-state original universe. Both methods used exact integer min-plus parity DP, with full-subset coverage justified in the theorem. This is a separately implemented author-side check, not a formally independent mathematical review.

**Inherited checked premises:** From original frozen EC49FRI/FRJ/FRP, the Bellman scalar minima U1=296, M1=690, U3=308, M3=700; x3 parity objective 19U3+2M3 even/odd minima 7290/7311; terminal indistinguishable named pairs {8,139} and {46,140} with multiplicity one; root observation bound U_R>=4, and U_R=4 implies M_R=4. Replayed full original A/B/C tree cost vectors respectively (6,290,6,751), (5,293,5,704), (5,295,5,685). Sources: [EC49FRP PR #2639](https://github.com/awdawmip/enterprise-math/pull/2639), earlier EC49FRJ PR #2624, EC49FRL PR #2630.

**Complete local archive produced this turn:** \`EC49FRQ_LOW_PRICE_STRIP_UNIFORM_PARETO_FULL_EVIDENCE_20261117.tar.xz\`, 220,704 bytes, SHA256 \`5336a97f56e2d6408a8e03e8ffc72ed27fb486ed9bd8122e0c96fb9d7843561f\`. All 18 internally listed manifest entries were read from the decompressed archive and had equal file byte counts and SHA256 digests. This conversation's archive contains uncommitted-by-this-PR original raw source and full machine witness payloads. GitHub PR files are the durable proof/code/small machine summary; the archive is the full self-contained reproducibility package.

**Evidence/admission:** AUTHOR_PROVED / EXACT_FINITE_CHECKED_WITH_TWO_IMPLEMENTATIONS / NOT_REVIEWED. Unchanged P000 and ACTIVE worldview. This is an independently saved portable research unit and asserts no native Task publication, winning CLAIM, activity write, Result, Review or owner/lease authorization.

**Next mathematical problem:** replace uniform price classes with individual observation cost perturbations while retaining original native response labels and joint-relation observer preservation, and determine the region of perturbations for which a price-uniform finite Pareto basis is possible.
