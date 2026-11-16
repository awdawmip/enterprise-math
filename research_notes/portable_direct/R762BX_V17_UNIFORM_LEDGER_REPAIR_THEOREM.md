# R762BX — Exact all-length repair budget for directed V17 exchange ledgers

Date: 2026-11-16 (Asia/Shanghai). Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142.
Scientific status: AUTHOR-PROVED / EXACT FINITE CHECK THROUGH NINE SWITCHES / NOT_REVIEWED.

## Frozen inputs, existing frontier, and model

Frozen P000 scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, with taskbook research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Retain the signed X6 Cell torsor, native 120-degree PERP_E relation, separate relational time, and primitive three-force TRIADIC_CLOSURE_E premise unchanged.

V17 source: research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md, Git blob 42b810a8f82c504833027da17884cc4fb2943e5b. The immediately preceding R762BW work, Draft PR #2537@6311bc0d22fe6ea32be4a2837a6518c77b9df91a, proved the first directed-ledger collision at five switches and the first nontrivial zero-current return at six. This paper extends that exact conditional V17 model to a uniform all-length information-repair theorem. The V29 axis-context ledger here is a conditional transducer, not a native signed Cell/Port/Link force-event predicate.

Let U={1,2,3,4,5,6}. A frame f=(a,b,c) is an ordered triple of distinct labels. One switch replaces exactly one of its three occupied slot labels x by one of the three absent labels y. Thus there are 120 frames and exactly nine successors per frame. Start at 123. A based return of length m ends at any ordered permutation of the unordered original triple {1,2,3}; the terminal ordered frame is the internal S3 holonomy h.

Let H be the full 30-vector of nonnegative directed exchange counts H_xy, x!=y, recording how many times replacement x->y occurred. For any H occurring in a length-m based return, define F_m(H) to be the set of distinct possible terminal ordered frames for that same H. Define M_m=max_H |F_m(H)|. When the observer already retains (m,H,terminal unordered triple), the minimum additional *fixed-length* binary code that reconstructs terminal h in the worst H-fiber is b_m=ceil(log2 M_m). The per-fiber code may depend on the observed H. It is not a full-history or native-force provenance compression.

## Main theorem: exact terminal-holonomy repair for every length

In the V17 switch model,

- M_0=1; there are no based returns at m=1.
- M_m=1 for m=2,3,4.
- M_5=2; M_6=4; M_7=5.
- **M_m=6 for every integer m>=8.**

Therefore b_m=0 at m=0,2,3,4; b_5=1; b_6=2; and **b_m=3 for every integer m>=7**. The empty m=1 return domain has no repair obligation. In particular, even an arbitrarily long directed-axis-count history needs at most three extra bits to recover terminal S3 holonomy, *for precisely this declared observer and future terminal-frame interface*.

## Proof I: exhaustive and exact small-length cases

Define Reach_0={(123,zero 30-vector):1} and recurse over every valid transition f->g that replaces x by y:

    Reach_(m+1)(g,H+e_(x,y)) += Reach_m(f,H).

The value is the exact positive integer multiplicity of ordered paths. The recursion merges only identical (ordered frame, complete directed H) pairs. This retains all h values and all multiplicities, unlike state aggregation by H alone. Every state has nine successors, so induction establishes that the recursion covers every one of the 9^m switch histories at each m, with no sampling.

The companion Python 3 verifier uses four bits per count for 0<=m<=9, so the packed representation is exactly injective because every H_xy<=m<=9<16. It checks both path multiplicities and the full cardinality distribution of H-fibers.

| m | Based-return paths | Distinct H | H-fiber sizes (size: number of ledgers) | M_m | b_m |
|---:|---:|---:|---|---:|---:|
| 0 | 1 | 1 | 1:1 | 1 | 0 |
| 1 | 0 | 0 | none | — | — |
| 2 | 9 | 9 | 1:9 | 1 | 0 |
| 3 | 36 | 36 | 1:36 | 1 | 0 |
| 4 | 369 | 171 | 1:171 | 1 | 0 |
| 5 | 2,952 | 684 | 1:540, 2:144 | 2 | 1 |
| 6 | 26,937 | 2,571 | 1:1563, 2:936, 4:72 | 4 | 2 |
| 7 | 239,148 | 8,748 | 1:3276, 2:4392, 3:360, 4:486, 5:234 | 5 | 3 |
| 8 | 2,155,617 | 28,209 | 1:7281, 2:13461, 3:1314, 4:3258, 5:1872, 6:1023 | 6 | 3 |
| 9 | 19,371,024 | 84,996 | 1:11958, 2:38622, 3:4236, 4:10608, 5:8670, 6:10902 | 6 | 3 |

For m=9 the algorithm merges the 9^9=387,420,489 possible path histories into 4,549,824 exact (frame,H) keys; the resulting based-return multiplicity 19,371,024 is still counted in full. Each table entry, state count and explicit witness set is an executable assertion, rather than a fitted numerical pattern.

## Proof II: six different holonomies with the same eight-step ledger

The following six legal eight-switch paths all have exactly one each of the directed arcs 1->2,1->3,1->4,1->5,2->1,3->1,4->1,5->1, and zero of every other arc; their terminal frames exhaust S3:

    123 523 521 523 513 523 123 423 123
    123 423 413 453 451 452 412 432 132
    123 523 521 523 513 543 143 243 213
    123 523 521 524 514 534 134 234 231
    123 523 513 543 541 542 142 342 312
    123 523 521 524 514 524 124 324 321

Every arrow replaces one occupied label by a currently absent label, preserving the two other slots. Thus M_8>=6. Since only six orderings of {1,2,3} exist, M_8<=6.

## Proof III: explicit nine-step witnesses and uniform extension

The following legal nine-switch paths each have a common ledger: H_(1,2)=2, and H_(1,3)=H_(1,5)=H_(2,1)=H_(2,4)=H_(3,1)=H_(4,1)=H_(5,1)=1; all other counts are zero. Their final frames again exhaust S3:

    123 523 521 523 543 513 523 513 523 123
    123 523 513 523 521 541 542 512 532 132
    123 523 521 523 543 143 243 143 243 213
    123 143 243 241 245 215 235 135 235 231
    123 523 513 523 521 541 542 142 342 312
    123 143 243 241 245 145 345 315 325 321

Thus M_9=6. From any ending frame which is a permutation of 123, the slot containing label 1 can execute a legal two-switch loop 1->4->1, or a legal three-switch loop 1->4->5->1, and end with precisely its previous ordered frame. The same label-based loop adds exactly the same directed counts to every one of the six eight-step paths, leaving their six different holonomies unchanged. For every integer m>=10, m-8 is a nonnegative combination 2a+3b; append a copies of the 2-loop and b copies of the 3-loop to every eight-step witness. Therefore M_m>=6 for all m>=10. Combined with the explicit m=9 witness and universal M_m<=6, the theorem holds for every m>=8.

The lower bound b_m>=ceil(log2 M_m) is the pigeonhole principle within a fixed known H-fiber; equality follows by indexing the at most M_m distinguishable terminal frames in that fiber. This proves the claimed exact worst-case repair width, not merely an upper bound.

## BRC significance and further work

Population: full ordered conditional V17 switch histories with exact path multiplicity. Observer: length m, full directed-axis exchange counts H, and unordered returning triad. Required future output: terminal internal S3 frame and any subsequent operation depending only on (H,h). An H-fiber-aware three-bit terminal-holonomy repair is therefore sufficient for this interface at all m>=7. If future operations query intermediate event order, signed Cell/Port provenance or native force constraints, those need separately preserved BRC structure; no global observer descent is claimed.

Native scientific next action: inspect actual signed TRIADIC_CLOSURE_E Cell/Link/Port event permission and the V17/V29/V39 event-to-frame transducer, then restrict the legal switch alphabet and recompute exact observer fibers with signs, Cell positions, Port directions and event order retained. This construction is conditional V17 mathematics and has not been admitted as actual native event dynamics. Independent review remains NOT_REVIEWED.

Companions: research_notes/portable_direct/R762BX_V17_LEDGER_UNIFORM_REPAIR_VERIFY.py and R762BX_V17_LEDGER_UNIFORM_REPAIR_EVIDENCE.json.
