# J1 saturation prior-art boundary — bounded Source checkpoint

Status: LOCAL_UNIT_COMPLETE / NONTERMINAL_TASK / REQUIRES_DRIVER_INTEGRATION.
Date: 2026-10-11 UTC.
Task: RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT.
Publication: TP2-39ACFC69F85D8661CFBF.
Researcher: EM-NATIVE-0B2763; session MCP-f0c0c2f0adbb42e0879a2f6c73d4c15d.
Activity: RA-612994534461F71FBF68059B; execution ER-D49D38085FD1FC68BA94.
Winning claim: MCP-3eebf4317c7ce03d7a37f25c; run RUN-cbc479fc9c78917c8dc774d9, generation 1.
Own open request: canonical-research-open-20261011-12, actual authorized SUCCEEDED at 07:24:26Z.

## Finding and scope

The inherited J1 rational-map/fiber/cardinality kernel remains EXACT_DUPLICATE, and the entire Enterprise J1 row remains PARTIAL_ANTECEDENT. This unit adds a precise antecedent for pointwise membership in a reduced modular-hyperbola sumset. It finds no source asserting the project-specific containment Im Lambda_s ⊆ J_s in the bounded passages audited below. The latter disposition is only NO_MATERIAL_MATCH_IN_AUDITED_SET, where the set is explicitly limited by read extent. It is neither a novelty verdict nor an exhaustive literature claim.

This is one source-boundary unit. It does not re-prove accepted J1/J2, reopen the closed cardinality search, finish the six-row external audit, create a new branch, or grant mathematical acceptance.

## Frozen dependency and inherited frontier

The statement-strength dependency is the accepted Driver review at Source 7f3671187aca1c041294766fa4704715698e3dc6, blob 80b550aa21d0695d0ca9e4853bd707319f6413e4, SHA256 5f08f144d6b4729d661556062411698739b1e4d077519db0dcae6f7e6728e6d5. The corresponding frozen replication return is blob 0a4596c8cb8bcfb64863becb1009ff13f3980a09, SHA256 1e40bfe1b3b24a604f703233887200b30a2816acc56a38f63711e4b3bf640d3e, read at the same Source.

The verified predecessor checkpoint at Source 33e6a1ba9c299c7c20a5a9dd9a6be6edeea8d038 has blob 888b78daf3b9b48d3a046e47e3bf40090c2bc722 and SHA256 f6ab4b1dfa846a9d777f2ed8f42cd4722cfab7451e127dd43c6d309c76585af7. Its J1 report is blob 13299f94ba47be9e7e1daface3180dcdf88e762a, SHA256 55a0c09794240ca4339afd7c6d3eeec9f5ecf229782984725e18919c529c6a1b. Both complete original contents were consumed and byte/hash verified. Preserve contributors EM-DIRECT-5DD273 and EM-NFHJPA-5B519F.

That report already closes Zheng–Wang–Yang–Wang, “Rational functions of degree two or three that are many-to-one on the projective line”, Theorem 3.1, DOI https://doi.org/10.1016/j.ffa.2026.102901, as the exact generic fiber/cardinality antecedent. It was accepted/public in 2026; its February 2027 journal issue is not represented as elapsed publication. This unit consumes that finding rather than repeating it.

## Exact comparison interface

The interval comparison here uses the prime-field restriction q=p, p odd, odd s≥3 and p∤2s. It does not infer interval order in a general extension field. J_s means the residue SET of integers −r through r modulo p, r=(s−1)/2; repetitions are reduced as sets, and |J_s|=s is not assumed without injectivity.

Put alpha=s/2 and u=sa. The inherited normalization gives Lambda_s(a)=−(u+alpha/u). Thus Im Lambda_s is the negative of the reduced coordinate sumset of uv=alpha. Bower–Evans–Luo–Miller [B], Lemmas 2.2–2.3, specialize at exponent one to:
2k∈Sbar_2(alpha;p) iff k²−alpha is a square modulo p, including zero.
With k=−t/2, this is exactly t∈Im Lambda_s iff t²−2s is a square modulo p. No nonzero root is lost because alpha≠0.

Consequently the containment interface is equivalently eta(t²−2s)=−1 for EVERY residue t outside J_s. This is a comparison reformulation of an already accepted saturation criterion; it is not an assertion that containment holds for arbitrary (s,p). [B] supplies the generic membership test. Checking a designated complement universally is an extra requirement. Scalar changes preserve fiber/cardinality structure but need not preserve consecutive residue placement.

## Subclaim/source matrix

| Subclaim or candidate | Exact source scope actually inspected | Relation and limitation |
|---|---|---|
| J1 fibers and image cardinality | Inherited Zheng et al. Theorem 3.1, as verified in predecessor Source report | EXACT_DUPLICATE already closed. No new count proof or novelty claim. |
| Generic pointwise image membership | [B] reduced two-dimensional sumsets; Lemmas 2.2–2.3 and Appendix A.2, odd prime specialization | EXACT_DUPLICATE of the comparison membership subclaim after alpha=s/2 and t=−2k. No specified J_s containment theorem. |
| Distribution inside coordinate intervals | [S] §3.1 Theorem 13 and rectangular specialization equation (10): coprime a,m, coordinate intervals of lengths X,Y under the displayed bounds; count phi(m)XY/m² plus O(m^(1/2+o(1))) | STRUCTURALLY_ADJACENT. A count with error is not universal containment of a sum projection. No zero-outside conclusion follows merely by citing it. |
| Sum/difference projections | [S] §4.1 Question 24 and ensuing discussion | STRUCTURALLY_ADJACENT. Question 24 is a question, not a proved saturation theorem. Its displayed S_a,m uses ordinary integer representative sums; reduction modulo m must be stated separately. |
| Concentration in a short square | [C] Introduction and Theorem 1: large prime p, lambda coprime to p, 1≤M≤p; I2 counts xy=lambda with each coordinate in a length-M interval; bound M^(4/3+o(1))/p^(1/3)+M^o(1) | STRUCTURALLY_ADJACENT. Restricted-coordinate count/upper bound, not containment of the full-domain sumset in the central target interval. |
| Joukowski dynamics | [U] Introduction and §2 interface: q=p^n, odd p, k∈F_p*, projective map k(x+x^−1); indegrees from a quadratic and selected dynamical cases | STRUCTURALLY_ADJACENT. Projective dynamics supplies neither a central consecutive target set nor an all-input interval conclusion in these passages. |
| Inverses in sequences of intervals | [BH] Introduction/Theorem 1: prime p; J pairs of intervals in (0,p), lengths H,K, first family disjoint; J sufficiently large relative to p³ log⁴p/(H²K²) guarantees a solution in at least one pair | STRUCTURALLY_ADJACENT. Existential solvability in a coordinate box differs from universal inclusion of a projected image. |
| Improved inverse-interval existence | [Ba] Introduction, Theorems 3–4: prime modulus, spacing/equispacing hypotheses on interval centers and displayed size bounds | STRUCTURALLY_ADJACENT at inspected scope. It improves existence conditions, not the Enterprise central sum-image inclusion. |
| Enterprise-specific ALL-output central containment | Union of the bounded passages above plus the inherited closed kernel | NO_MATERIAL_MATCH_IN_AUDITED_SET. Does not assert absence in unread passages, all works, all languages, or later literature. |

## Primary source register

[B] Amanda Bower, Ron Evans, Victor Luo, Steven J. Miller, “Coordinate sum and difference sets of d-dimensional modular hyperbolas”, https://arxiv.org/pdf/1212.2930v1. Read Lemmas 2.2–2.3/Appendix A.2. Header: 12 Dec 2012; internal Date September 24, 2018 is not a v2 date. Prime-power residue rings are not extension fields.

[S] Igor E. Shparlinski, “Modular Hyperbolas”, https://arxiv.org/pdf/1103.2879v4, header 3 June 2012, internal date November 8, 2018. Read definitions, notation, §3.1 Theorem 13/equation (10), §4.1 Question 24 and bibliography entries 70/182. Survey context is not a claim that every cited original paper was read.

[C] J. Cilleruelo, M. Z. Garaev, “Concentration points on two and three dimensional modular hyperbolas and applications”, https://arxiv.org/pdf/1007.1526v2, header 12 October 2010. Read Introduction/Theorem 1. The journal's “Concentration of points...” title is a title variant, not an extra independent antecedent.

[U] Simone Ugolini, “On the iterations of certain maps x↦k·(x+x^−1) over finite fields of odd characteristic”, https://arxiv.org/pdf/1304.3283v2, header 3 July 2013; journal DOI https://doi.org/10.1016/j.jnt.2014.02.024. Read Introduction and §2 definitions/conjugacy interface. No complete-paper negative claim is made.

[BH] T. D. Browning, A. Haynes, “Incomplete Kloosterman sums and multiplicative inverses in short intervals”, https://arxiv.org/pdf/1204.6374v1, header 28 April 2012. Read Introduction and Theorem 1.

[Ba] S. Baier, “Multiplicative inverses in short intervals”, https://arxiv.org/pdf/1208.3393v1, header 16 August 2012. Read Introduction and Theorems 1–4, treating Theorem 1 as the explicitly attributed Browning–Haynes result.

Reference-only candidates, excluded from no-material-match support: Eichhorn–Khan–Stein–Yankov's 2009 original chapter (journal index located, full chapter not obtained); Shparlinski–Winterhof 2008, DOI https://doi.org/10.1016/j.jnt.2007.04.016 (author-institution abstract only); Shparlinski 2007 distribution chapter (query metadata only). No theorem is attributed to their unread full texts.

## Query evidence and coverage

Own successful open preceded new research queries. Shared standard turn b8d7d14d-77c2-4a4b-8719-e1230a7029a0 used exactly three jobs, now frozen; no new turn bypass.

Bridge issue 3621 / batch 44e0965e-ff7b-4703-82d1-c15f25e92595, original result comment 6106660769, outer PARTIAL: arxiv “modular hyperbolas” intervals was PROVIDER_ERROR, retrieval_verified=false; scholar “Joukowski” “finite fields” “interval” COMPLETED with three irrelevant metadata/abstract-preview records and incomplete coverage. The failed arxiv item is not an empty search.

Issue 3622 / batch bf73c65c-b9cc-4d7a-90ce-dc43e8559743, comment 6106696289, outer FAILED: scholar “modular hyperbolas” “short intervals” inner PARTIAL, retrieval_verified=true, five bounded metadata records, coverage BOUNDED_SELECTION_LIMIT. These records located [BH], [C], [Ba] and reference-only entries. Returned metadata does not mean provider full text was read; primary passages were read separately through the public web tool. Neither batch supplies NO_HIT evidence. Exact extracted JSON is preserved alongside this report; global professional cache status at this checkpoint is ARCHIVE_PENDING, to be updated only by actual root-controlled publication/readback.

## Contribution, exposure, and method boundary

New contribution: bounded primary-source comparison, exact modular-sumset membership normalization, target placement versus cardinality/box-count/existence distinctions, honest query failure/coverage record, and a recoverable remaining-row frontier. This is directed, source-exposed research, not clean or blind independent replication. Prior session_start prior_contribution_ids=[] truthfully describes this new agent's own prior history; it does not erase inherited contributors. Parent/helper bibliographic checks are factual assistance, not independent mathematical acceptance of this authored comparison.

BRC: selected question is external containment antecedents; carrier is the typed pair (source hypotheses, source conclusion), observer is exact Boolean implication to the designated subclaim. Generic membership is actually reused under the written transformation. Weighted branching/positive-mass composition is NOT_APPLICABLE here; no measure/support substitution or new physical inference is introduced. P000's native ontology and provenance restrictions remain intact. External finite-field comparisons do not promote anything into native physical claims, WT or Foundation.

## Durable continuation boundary

Completed locally: this bounded J1 saturation source-boundary unit, with the exact generic membership antecedent identified and the specified interval assertion unmatched only in the inspected finite source set.

Still unfinished: Driver integration and any separately authorized decisive review of this comparison; external antecedent rows H1, H2, J2, C1, C2 and the full six-row report/Result contract. Their accepted mathematical statement-strength verdicts remain unchanged.

Next control action: Driver consumes the verified Source checkpoint and actual query archive status, obtains the required separate review before any new acceptance, and routes the next unclassified external row. This researcher releases after verified Source handoff; it does not self-start another branch.

Do not repeat: frozen collision/cardinality proof; closed Zheng kernel audit; accepted six-row independent replication; completed P11/D25/FREE units; this bounded source comparison absent a specific changed-evidence need. Negative lookup never becomes novelty. No Task-terminal Result is frozen by this checkpoint.

Global-Knowledge-Sync: main@dfa8794 / GLOBAL_KNOWLEDGE_V1.

