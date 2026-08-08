# Citation and Intellectual-Lineage Policy

## 1. Scope

This policy applies to external mathematical, computational, physical, historical, and philosophical sources used by Enterprise Math.

The goal is not merely to produce a bibliography. The goal is to make every borrowed definition, structural analogy, contrast class, and novelty boundary auditable.

## 2. Canonical source IDs and registry corpus

Every external source used materially in canonical project prose must have exactly one stable `SRC-*` record in the **canonical source-registry corpus**.

The base registry is `sources.json`. As the project grows, independent research lines may add additive machine-readable shards named `sources_*.json`. All such files form one logical registry: source IDs must remain globally unique across the entire corpus, and a shard may not redefine or shadow a base record.

Canonical prose cites a real source with its registered bracketed source identifier. In documentation examples, use an unbracketed placeholder such as `SRC-EXAMPLE-ID` so that examples cannot be mistaken for registered citations.

Each source record must contain at least:

- stable ID;
- title;
- author or responsible organization;
- year;
- source kind;
- primary URL or DOI;
- relation role;
- exact Enterprise Math use;
- an explicit statement of what is **not** being claimed as our invention;
- verification date.

## 3. Source priority

For technical and historical claims, prefer sources in this order:

1. original research paper or primary publication;
2. official standard or official project/library documentation;
3. author-maintained preprint or institutional archive;
4. authoritative scholarly review when the original is inaccessible;
5. secondary summaries only for navigation, not for load-bearing attribution.

A later review may be cited in addition to the original when it clarifies how a field evolved.

## 4. Relation labels and lineage registry corpus

Every source that materially shapes the project should be classified in the **canonical lineage-registry corpus**.

The base registry is `lineage.json`. Independent additive shards may be named `lineage_*.json`. Component IDs are globally unique across all lineage files; shards inherit the base relation/novelty vocabulary unless they explicitly extend a future schema.

Allowed core relations are:

- `ADOPT`;
- `EXTEND`;
- `REINTERPRET`;
- `COMBINE`;
- `CONTRAST`;
- `INSPIRE`.

A single source may have different relations to different project components.

## 5. Claim-to-source discipline

A citation must support the sentence or proposition it is attached to.

Do not use a source merely because it is thematically related.

Do not cite a paper about a neighboring structure as evidence that the Enterprise Math physical interpretation is true.

When a source and Enterprise Math use the same formula under different semantics, state both the formal match and the semantic difference.

## 6. Novelty language

Historical novelty is a separate claim requiring separate evidence.

Until a dedicated priority review establishes otherwise, the overall framework remains `NOVELTY_UNVERIFIED`.

Safe language:

- “we define”;
- “we propose”;
- “we combine”;
- “we reinterpret”;
- “we investigate”;
- “we have not found an equivalent synthesis in the searches recorded so far”.

Restricted language requiring a dedicated priority review:

- “first”;
- “unprecedented”;
- “never proposed before”;
- “original invention”;
- “no prior work exists”.

Finding new prior art is a successful research contribution, not a threat to the project.

## 7. New-source update protocol

When a new citation is introduced into canonical work:

1. verify the primary source;
2. create or reuse exactly one `SRC-*` record in the source-registry corpus (`sources.json` or an additive `sources_*.json` shard);
3. add the source to the relevant component in the lineage-registry corpus (`lineage.json` or an additive `lineage_*.json` shard);
4. choose the correct relation label;
5. update the relevant bilingual `docs/PRIOR_ART*.en.md` / `.zh-CN.md` corpus so the source and novelty boundary are visible in prose;
6. update any theorem, specification, reference, or physical-comparison document that relies on it;
7. preserve old source records unless they were factually erroneous;
8. run the reference-integrity and bilingual checks.

Prefer a small additive shard for an independent research line when rewriting the large base JSON would create unnecessary merge contention. Sharding is an integration mechanism, not a relaxation of provenance rules.

A source that only fixes a typo or provides a non-material background example need not change the novelty map, but it still needs a source record if cited canonically.

## 8. Internal contribution provenance

External literature and project-origin contributions are tracked separately.

When a definition, theorem, counterexample, proof idea, implementation, or terminology refinement originates in a GitHub Issue, Discussion, commit, or Pull Request, preserve that project provenance in the relevant canonical document when practical.

Do not replace contributor provenance with only an external citation.

## 9. Corrections and disputes

If a source was misread:

- correct both language versions;
- update the exact source/lineage registry file containing the record;
- retain Git history;
- explicitly narrow or retract affected novelty claims.

If two sources conflict, record the conflict instead of silently choosing the one more favorable to Enterprise Math.

## 10. Automated checks

`tools/check_references.py` validates the combined machine-readable provenance graph and stable source IDs across all registry files.

The CI workflow must fail when:

- a source ID is duplicated anywhere in the registry corpus;
- a component ID is duplicated anywhere in the lineage corpus;
- required source metadata is missing;
- a lineage relation points to an unknown source;
- a canonical bracketed `SRC-*` citation points to an unknown source;
- a project component uses an unknown novelty status or relation;
- a source in the machine registry corpus is absent from either language's canonical prior-art prose corpus.

Automation cannot decide whether a citation is intellectually honest. Reviewers still must check that the cited source actually supports the claimed relationship.
