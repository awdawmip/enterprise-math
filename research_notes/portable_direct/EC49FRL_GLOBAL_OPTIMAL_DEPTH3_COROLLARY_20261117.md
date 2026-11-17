# EC49FRL addendum — globally optimal native BRC trees always have worst-case depth three

**2026-11-17; author-proved / exact finite checked / not independently reviewed.** Original frozen science pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This addendum is part of independent portable PR #2630. It compares the new EC49FRL depth-three and mixed-palette certificates with the previously published **unrestricted** EC49FRJ five-tree theorem.

## Global depth-three optimality theorem

For the unchanged **141 full-named BRC class-16943 profiles**, original 228 physical observation-response maps, root/terminal prices t>0 and x=r/t>=1, and the exact positive prior mixture p_i(lambda)=(1-lambda)/141+lambda m_i/310 with lambda in [0,1]:

**Every parameter pair (x,lambda) admits a globally optimal exact-identifying native physical-observation decision tree whose worst-case number of queries is exactly three. No exact adaptive decision tree can have worst-case depth two.**

This holds simultaneously for **every real** price ratio x>=1 and every real prior lambda in [0,1].

**Proof.** EC49FRJ previously author-proved the unrestricted exact Bellman equality

V(x,lambda)=min{A(x,lambda),B(x,lambda),C(x,lambda),D(x,lambda),E(x,lambda)}

throughout the stated unbounded real half-strip. The five functions are the original physical complete decision trees, not formal coefficient vectors. The full immutable A,B,C witnesses were retrieved from the inherited EC49FRI original integer Bellman endpoint files, and D,E from the inherited EC49FRJ endpoint files, then replayed directly on **each** of the 141 original named states against the same frozen response table V. All five have worst-case query depth **exactly three**; their precise aggregate query-count vectors (U_R,U_T,M_R,M_T) are

| Tree | Original finite anchor | First physical query | (U_R,U_T,M_R,M_T) | Max depth |
|---|---|---:|---|---:|
| A | FRI x=1,lambda=0 | 32 | (6,290,6,751) | 3 |
| B | FRI x=1,lambda=155/1847 | 140 | (5,293,5,704) | 3 |
| C | FRI x=1,lambda=1 | 16 | (5,295,5,685) | 3 |
| D | FRJ x=100000,lambda=0 | 140 | (4,296,4,707) | 3 |
| E | FRJ x=100000,lambda=1 | 16 | (4,298,4,688) | 3 |

For any (x,lambda), at least one of these five fixed trees attains the unrestricted Bellman minimum. Since each of the five has depth at most three, an unrestricted globally optimal depth-three tree exists. EC49FRL's **independent exhaustive 228-first-query two-level obstruction** proves that no depth-two tree identifies all 141 original named profiles, regardless of price and prior. The optimal worst-case depth is therefore exactly three. QED.

## Stronger provenance reconciliation

The new root-floor depth-three optimizer in the primary EC49FRL theorem independently produced A' with first query 140 and counts (U_T,M_T,U_R,M_R)=(296,707,4,4), and B' with first query 16 and counts (298,688,4,4). Exact canonical JSON comparison against the inherited original high-price EC49FRJ **complete** tree objects, not only costs, confirms **A'=D and B'=E bytewise in canonical sorted JSON representation**. They are the previously known D/E global optimum witnesses, now independently characterized by a new constrained depth/root-mass Bellman principle. The prior crossover beta=620/3299 was already proved in EC49FRJ; EC49FRL supplies a separate derivation within the new structural constrained question.

Canonical SHA256 of the two full native decision-tree objects (sorted compact JSON, UTF-8):

* D (and EC49FRL A'): 764ab444a59ab338cd78ab56d105282da5724a2fdfad6e4b628ad0234a58ca6a.
* E (and EC49FRL B'): 9a8b28cdf8d177ce9f2959c251db2274ef0690d34a7c8da338779bc53e3ef52f.

The original full five-tree replay was re-executed on the frozen reconstructed native-response table V; every leaf index matched its original named profile. An executable independent audit and source endpoint certificates are included in the complete self-contained EC49FRL evidence archive.

## Exact scope, result status and next frontier

The new contributions of EC49FRL are the **four-query mixed nonadaptive optimum**, **unconditional minimum adaptive depth three**, **depth/root-mass joint attainability**, and **exact constrained terminal-count dynamic-programming characterization**. Its continuum threshold and high-price witnesses are reconciled with the established EC49FRJ evidence rather than claimed as a newly discovered high-price phase.

All statements are internal to the frozen finite BRC static original-observer model. The original P000/ACTIVE X6 heartbeat and joint-relational source/provenance constraints remain unchanged. Scientific status remains AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED; official Result/Review requires an independent authorized process.

**Next:** classify all depth/root-mass Pareto-optimal original physical decision trees for x near 1, and test whether a constrained depth <=3 policy can match the unrestricted global optimizer under additional new future-observer requirements (with the exact semantic horizon stated before any compression).