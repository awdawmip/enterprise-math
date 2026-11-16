# R762CD — Exact observer-conditioned BRC policy repair and sharp adaptive interrogation

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142.  
**Scientific pin:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5 and the Task book).  
**Status:** Author-proved finite combinatorial theorem, complete exact census, independent review NOT_REVIEWED.  
**Scope:** Conditional sign-only S6×C3 three-Port law model inherited from R762CA–R762CC; this is not yet a native Cell/Link/Port event-licensing theorem.

## Exact population and observers

At one selected X6 Cell, three named signed Ports have a directed Link cycle 0→1→2→0. The sign assignments form four cyclic orbits with sign-word weights (1,1,3,3). The corresponding independent rooted permission-bit counts are r=(1,1,3,3). A coherent policy on orbit i is either EXCLUDED (closure=0; all gates 0), or CLOSED(mask) (closure=1; any r_i-bit root mask). Thus the finite law universe has (1+2)^2(1+2^3)^2=729 members.

For a policy let n_k (k=0,1,2,3) be the number of closed sign words with exactly k permitted roots, counted with their orbit weights. R762CB proves that the complete all-length aggregate return sequence N(m) determines and is determined by n=(n_0,n_1,n_2,n_3): the exact 4×4 return-count matrix has determinant 324. Define four law observers:

- A: all-length aggregate return sequence, equivalently n;
- S: sign-orbit-resolved all-length sequences, equivalently each orbit's EXCLUDED status or its closed k;
- E: eight independent rooted gate bits (one for each C3-equivariant root class);
- J: four closure bits together with those eight gate bits, the complete candidate **law**.

A repair code is an auxiliary symbol that recovers J together with its original observer. A fixed-width arbitrary binary code is different from an interrogation restricted to 12 Boolean atoms: four Q_C(i) closure bits and eight Q_g(i,j) rooted gates. Adaptive questions may depend on earlier replies; nonadaptive questions must be selected before replies, but after seeing the original observer. These atom questions are logical conditional-law tests, not established native physical events.

## Theorem 1 — Optimal uniform arbitrary repair bits

| Initial observer | Classes | Maximum fiber | Minimal additional fixed bits |
|---|---:|---:|---:|
| A | 90 | 36 | **6** |
| S | 225 | 9 | **4** |
| E | 256 | 16 | **4** |
| J | 729 | 1 | **0** |

For any finite observer O:L→Y, the minimum fixed-length auxiliary index making (O,index) injective is ceil(log2(max_y |O^-1(y)|)). The largest fiber gives the lower bound; enumerate each fiber for the upper bound. Exact fiber-size histograms:

- A: 1:9, 2:18, 4:9, 6:18, 9:6, 12:18, 18:9, 36:3.
- S: 1:81, 3:108, 9:36.
- E: 1:49, 2:112, 4:78, 8:16, 16:1.
- J: 729 singletons.

The accompanying verifier reconstructs all 729 laws and these histograms independently. Hence 6,4,4,0 bits. This is a **law-fiber** result: Cell, time, amplitude, branch/source history, Link identity and S3 internal holonomy remain outside J and must be preserved when future operations require them.

## Theorem 2 — Exact worst-case pointwise law interrogation

Under the 12 individual Boolean queries, the minimum worst-case query counts to recover J are:

| Given | Adaptive | Nonadaptive |
|---|---:|---:|
| A | **6** | **6** |
| S | **4** | **4** |
| E | **4** | **4** |
| J | **0** | **0** |

Here worst case ranges over all possible observed classes and coherent laws.

**S, lower and upper:** When both size-three sign orbits are CLOSED with k=1, three choices of root remain independently in each orbit, giving 9 possible laws; any binary decision tree needs at least ceil(log2 9)=4 queries. Nonadaptively query two of the three gates in each mixed orbit (four total); knowing k determines the third. The two size-one orbits are already determined by S.

**E, lower and upper:** At the all-zero gate table, every orbit independently chooses EXCLUDED or CLOSED(0), leaving 2^4=16 possibilities. Query four closure bits to resolve them. Four are necessary and sufficient.

**A, analytic lower:** The aggregate observation n=(4,3,0,0) has exactly 12 laws. Exactly one of the two homogeneous sign orbits is CLOSED(0); the other is EXCLUDED. Both mixed sign orbits are CLOSED, and exactly one of their combined six rooted gate coordinates is 1. All other closure bits are constant. Any pointwise testing strategy for the unknown single 1 among six gates requires five answers on an all-zero prefix in the worst case, and the independent homogeneous closure choice requires another question: at least **six** queries, including for adaptive strategies.

**A, constructive upper:** Exactly 90 aggregate n classes exist. The JSON evidence contains a separate at-most-six-query bitmask for every class, whose twelve bit positions are ordered C0,C1,C2,C3,g00,g10,g20,g21,g22,g30,g31,g32. The standalone verifier checks that the selected queries distinguish every pair of laws inside each class. Therefore six **nonadaptive** pointwise questions always suffice; the lower bound above is sharp.

## Theorem 3 — Strict two-query adaptivity gain on a particular fiber

For aggregate n=(0,3,0,0), exactly one of the two mixed sign orbits is CLOSED with k=1, all remaining orbits being EXCLUDED. The entire fiber comprises six possibilities (one enabled gate among the six roots of these two orbits).

An adaptive protocol first asks closure for the first mixed orbit. This locates the active mixed orbit; querying two of its three roots uniquely determines the third. Thus adaptive depth = **3**.

Nonadaptively, without a mixed closure question one must query at least five of the six roots, since two unqueried roots remain indistinguishable on the all-zero transcript. With a mixed closure question, at least two fixed rooted queries in **each** of the two mixed orbits are necessary to distinguish three possible active roots on either branch. Therefore at least 1+2+2=**5** are needed, and five gate queries suffice. Hence the optimal nonadaptive depth is **5**, two more than adaptive. This explicitly shows that equality of the global worst-case bounds does not imply per-observation equivalence.

Complete per-class adaptive depths for A: 0:9, 1:18, 2:9, 3:12, 4:18, 5:15, 6:9; nonadaptive: 0:9, 1:18, 2:9, 4:15, 5:27, 6:12. Adaptivity savings across the 90 A classes: 0:66, 1:18, 2:6.

## Verification contract and proof boundary

The attached Python 3.10+ verifier enumerates the 729 laws as the direct Cartesian product (3,3,9,9), derives the exact A/S/E fibers, and checks the cardinalities above. For each fiber it computes optimal adaptive decision depth from the recurrence D(F)=1+min_j max(D(F∩Q_j^-1(0)), D(F∩Q_j^-1(1))) over proper splits (base singleton=0); induction on fiber size proves this recurrence. All 2^12 nonadaptive query subsets are searched in increasing size until a separating set is found. For A, the verifier emits all 90 separating six-or-fewer-query masks and checks each one directly. All arithmetic and comparisons are exact integers and finite sets. The verifier checks the two named witnesses and full depth histograms; the JSON result is a machine-readable finite certificate. All claims are within the explicit conditional law population.

**Mother-objective continuation:** Obtain the genuinely legal signed TRIADIC_CLOSURE_E Cell/Port/Link predicate at the frozen Task pin. Test whether closure and gate eligibility factor through signs at all; if Cell, force magnitude, Link provenance, event order, time or internal rotation intervene, enlarge the law model and re-evaluate the observer quotient. V17's shared-axis transport is explicitly a conditional internal-frame law, not evidence of native event licensing. Independent review remains NOT_REVIEWED.

**Provenance:** P000 V5 and taskbook at frozen a72226e2430ffa4786321ac86e7f0c599d5f0389; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; V17 research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md (Git blob 42b810a8f82c504833027da17884cc4fb2943e5b); R762CA PR #2551@75302694, R762CB PR #2554@e0724e29 and R762CC PR #2558@b54aefb8.