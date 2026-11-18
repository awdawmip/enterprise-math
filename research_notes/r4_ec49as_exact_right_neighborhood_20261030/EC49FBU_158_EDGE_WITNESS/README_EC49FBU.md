# EC49FBU — A 158-edge signed-native X6 nine-window witness

Date: 2026-11-05. Frozen science input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Parent: EC49FBT at `04ffe42946b5ac11f2909fb6a674c3bf55a2efd0`. Scope: author-side **exact constructive upper bound**.

## Proposition

Fix H2={fe,ge} and H3={feg,gef}. Let H4–H5 use the complete BRC-positive cache key L=(4,2,1,0,0,0) and H6–H9 use M=(7,3,2,0,0,0), with the frozen nine-state observer and the native signed six-axis step code of EC49FBS. There is a family of exactly 24 legal operation words that covers the four rank-9 observation clauses at every horizon H2–H9 and uses exactly **158 distinct signed-native primitive-prefix edges**. Thus the minimum E*(L421,M732) for this fixed schedule satisfies **E* ≤ 158**. This improves the constructive upper bound 159 from EC49FBT by one edge.

## Complete witness

| Horizon | Operation words |
|---|---|
| H2 | fe; ge |
| H3 | feg; gef |
| H4 | degf; fegd; cefg; gefc |
| H5 | feggf; geffg |
| H6 | aeeddd; dedead; aeeccc; ceceac |
| H7 | aeeddgf; dedeagf; aeeccfg; ceceafg |
| H8 | feggfead; geffgaed; geffgaec; feggfeac |
| H9 | feggfeafg; geffgaegf |

The companion JSON is the machine-readable certificate. Every word expands using a=(-1,-1), c=(+1,+2,-1,-2), d=(+2,+1,-2,-1), e=(+3,+1,+1,-3), f=(+1,-1), g=(+2,-2), where ±k denotes the signed kth native six-axis step. Every resulting signed displacement is (2,0,0,0,0,0); all positive cache keys and terminal signatures meet the frozen observer. These are ordered signed primitive paths, not quotient chart endpoints.

## Exact verification / constructive proof

Run `node CROSSCHECK_EC49FBU.js` beside `EXACT_REPORT_EC49FBU.json`. The independent Node.js checker derives the nine-state observer outputs from each word, checks all eight four-clause covers, the full positive BRC keys, signed six-axis endpoint, 24-word cardinality and five-key budget. It then counts distinct nonempty signed-native primitive prefixes without importing the search implementation.

The executed checker returned `PASS`, native prefix count **158**, 24 words, five distinct keys and cumulative signed-prefix edge counts **12, 16, 46, 52, 112, 124, 152, 158** for H2–H9. By the EC49FBS lossless codeword-prefix identity, the independent operation-trie calculation gives **170 weighted operation edges − 6 (c/f) − 6 (d/g) = 158**. The two exact integer counts agree. These finite equalities, together with the explicit witness, prove the proposition.

The search enumerated the entire *candidate family* by operation-count equations and the frozen observer (48, 24, 120, 2,520, 10,080 and 3,360 candidates for H4 through H9 respectively, total **16,152**). A seeded multi-start coordinate replacement search, seed 349, found the 158-edge witness at its 14th improvement attempt. This is a constructive feasibility search; no claim of minimum 158 within the schedule is made.

## Next unit EC49FBV

Use the EC49FBS losslessly compressed MILP on the same 16,152 candidates with this 158-edge feasible incumbent; obtain a stronger explicit construction or a certified exact lower bound for the fixed schedule. Compare other L/M schedules and root choices to the broader mother benchmark 80≤E*≤94, without conflating the restricted 158-edge schedule with the global candidate family. Current task ownership, Source Result and independent Driver acceptance remain separate from author-side publication.

BRC usage: exact positive cache keys, signed native path provenance and observer signatures retained (REUSE_APPLIED); the compressed objective is the proved exact EC49FBS identity.
