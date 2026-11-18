# EC49FDF — exact joint early/late BRC-cache-key census

Date: 2026-11-07. Frozen scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Model source: sibling EC49FCZ frozen_model.py (Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859). Status: AUTHOR_EXACT_FINITE_THEOREM / EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Question and result

Keep the frozen signed-six-axis primitive alphabet, 9-state observer, 24 observation labels and literal signed primitive prefix cost. The four H2/H3 original words remain fixed: H2:16=fe, H2:32=ge, H3:16=feg, H3:32=gef. Independently vary the *common* integer early key L=(x,y,z) for both H4 and H5, and the *common* integer late key M=(x,y,z) for H6,H7,H8,H9. Every H4–H9 label is free to choose every valid ordered operation word in its full key-specific multiset and DFA-terminal-signature language.

**Theorem (finite joint-key model).** Among all integral pairs of keys meeting the required nonnegative multiplicities and all required endpoint observation labels, the exact smallest 24-word nonempty native signed-prefix union is **112 edges**, attained at L=(4,2,1), M=(6,4,1). All 49 nonnegative integer key pairs have been classified; 16 have every required signature. For the 16 feasible pairs, full-language exact label-mask Trie dynamic programming yields the following complete matrix (columns are late M):

| Early L \\ Late M | (5,5,1) | (6,4,1) | (7,3,1) | (7,3,2) |
| --- | ---: | ---: | ---: | ---: |
| (5,1,1) | 158 | 138 | 130 | 169 |
| **(4,2,1)** | 138 | **112** | 138 | 158 |
| (3,3,1) | 130 | 138 | 158 | 169 |
| (5,1,2) | 174 | 168 | 174 | 146 |

The remaining three nonnegative early keys (5,2,1),(4,3,1),(5,3,1) lack H5 signature 16/32. The remaining three nonnegative late keys (6,5,1),(7,4,1),(7,5,1) lack H9 signature 16/32. Thus the 7×7 product contains exactly 16 feasible pairs.

**Stronger independent corollary.** For L=(4,2,1), M=(6,4,1), optimizing the 20 H4–H9 labels *without any H2/H3 prefix contribution* also gives exact 112. Hence no change to the four H2/H3 words alone can yield fewer than 112 distinct edges when this H4–H9 language is retained, regardless of how the earlier four paths are independently chosen. The prior EC49FDE 24-word witness attains 112 with the original earlier words.

## Complete key enumeration and exact proof

For a horizon h and key (x,y,z), the frozen count law is
a=z−1, e=z, b=c+d=x+y−h−1, f=h+1−y−2z, g=h+1−x.
All operation counts must be nonnegative. For a *single common key* over h_min..h_max, this is equivalent to integer z>=1, x<=h_min+1, y+2z<=h_min+1, x+y>=h_max+1; the identities x=b+f+2z>0 and y=b+g>=0 bound the remaining search. H4,H5 give z>=1, x<=5, y+2z<=5, x+y>=6, exactly seven triples. H6..H9 give z>=1, x<=7, y+2z<=7, x+y>=10, exactly seven triples. For each key and each h, enumerate c=0..b and every ordered word in the corresponding exact multiset, following the pinned observer transition matrix and dropping its dead state 8. Signature feasibility then yields the 16 declared pairs.

For the four fixed words let F be the union of their nonempty literal signed primitive prefixes, |F|=16. Insert each labelled H4–H9 candidate into a signed-prefix Trie; a newly traversed edge has cost 0 precisely when its entire prefix lies in F, otherwise 1. At a Trie vertex v, let D_v(S) denote the minimum additional cost of satisfying exactly label subset S inside its subtree. Initialize every subset of the vertex's terminal-label mask at zero. For each child u merge disjoint subsets A,B:

D_new(A∪B)=min(D_old(A)+D_u(B)+edge(u)*[B nonempty]).

The subtrees partition all remaining signed prefixes, and disjoint label masks select each of the 20 labels exactly once. Induction from leaves proves the recurrence searches every admissible word assignment and counts each distinct prefix edge once. At the root use the full 20-bit mask and add |F|. For the late-only variant set every Trie-edge cost to 1 and omit F. Both variants have an explicit 112 witness via the EC49FDE word assignment, proving the matching upper bound.

## Evidence and reproduction

Run `python VERIFY_EC49FDF.py` in this directory; the source imports the unchanged sibling frozen model by relative path and emits EXACT_RESULTS_EC49FDF.json. The source was executed locally using a copy of the pinned primitive-transition tables and also cross-checked against the prior EC49FDE (L,M)=(4,2,1),(6,4,1) 112 and the original (4,2,1),(7,3,2) 158. Actual verification examined **382,128,898** candidate DP mask pairs across 16 feasible key pairs, plus **21,972,032** in the independent late-only test. There were no floating-point costs or pruning assumptions; all trie edge and label states are exact integers. The companion SUMMARY_CERTIFICATE.json retains each feasible pair's optimum, candidate-word count, Trie size, transition totals, signature gaps for excluded keys, and the SHA256 of the fully generated local JSON. It is an executed-computation certificate pending independent Driver audit.

The explicit 112-edge 24-word witness is in the predecessor EC49FDE README and EXACT_RESULTS_EC49FDE.json; our key pair (4,2,1),(6,4,1) contains that witness unchanged.

**Scope:** This statement classifies common integer L for H4/H5 and common integer M for H6..H9, with fixed H2/H3 literals and unchanged primitive and observer semantics. Further horizon-specific keys, alternative native word constructors and revised BRC carriers remain research directions. P000, provenance, branch order, six-axis signing and the frozen baseline are preserved.

**Next:** EC49FDG should test typed horizon-varying key families or primitive-language enlargement able to change the 20 late/early signed-prefix lower bound, seeking an explicit <=111 witness (then <=93) with full 24-word evidence. Native owner, CLAIM, Result and independent Driver acceptance remain separate authoritative operations.
