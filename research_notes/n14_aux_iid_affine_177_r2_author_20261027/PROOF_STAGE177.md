# Stage177 — complete all-real optimal interval in the external N14 ternary IID experiment

**Author status:** EXACT / NOT_ADMITTED / EXTERNAL_AUXILIARY_MODEL. Not a native six-dimensional P000/Cell theorem, Source Result, Lean theorem, or independently approved Driver result.

## Source and problem

Frozen GLOBAL_KNOWLEDGE_V1 main c255c049665e04da1b3f7b5f3b6f36e8594a22e7, Enterprise Math main 2145832abbeece95c8e7a847204c1884b8689878; P000 projection matched canonical Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Parent Stage176 author certificate: immutable commit 1198e05fe284be7143682dd68dba389d50c4925e. Stage177 dual-only candidate came from that parent.

For length N=14, use three-symbol IID measures P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). A randomized stopping/decision strategy may depend on **the entire ordered history**; it stops by depth 14, chooses P or Q. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau). Define

V14(alpha) = min_{eP,eQ<=alpha} max(tP,tQ).

The finite strategy space is compact, so optimal policies exist.

**Theorem (all real alpha):** For every real delta between zero and 251195378125/300094765349732352 inclusive,

V14(alpha176+delta) = V176 - (3693899955/8461318)*delta,

where

alpha176=5148159682306058186075/14750257906470044565504,
V176=338735964098497111620725/29500515812940089131008.

The resulting Stage177 endpoint is

alpha177=5148172029061283786075/14750257906470044565504,
V177=338725183820868439620725/29500515812940089131008.

For alpha>alpha177, **this particular Bellman supporting line** is strictly below the true V14(alpha). This does not rule out later different supporting segments.

## 1. Dual calculation and complete lower bound

For count state s=(n,a,b), where a counts symbol 0 and b counts symbol 1, Q/P likelihood ratio on every corresponding ordered history is ell(s)=2^(a+b)/3^a. Let K=1870855299/8461318 and L=911522328/4230659, both positive. Define backward Bellman

h(s)=min{K ell(s), L, 1+sum_i P_i h(child(s,i))},

where child(s,i)=(n+1,a+[i=0],b+[i=1]); continuation is disallowed at n=14. A fully exact Fraction recurrence scans sum_{n=0}^{14} C(n+2,2)=C(17,3)=680 count states and computes

H=h((0,0,0))=148336146012983121522325/905303534551638736896.

The **only** states with multiple minimizing actions are T=(8,2,0), with P vs continue (P/C), and U=(12,5,2), with P/C. The other 1,238 nonwinning action gaps are all strictly positive, smallest 2003135/203071632. There are zero negative gaps. The attached Python exact checker reproduces all results and verifies the expected H.

At each ordered prefix the Bellman one-step inequality holds, regardless of any full-history randomization. Taking expectations and inducting over finite remaining depth gives for every policy

tP + K eQ + L eP >= H,

hence max(tP,tQ) >= H-(K+L)alpha with K+L=3693899955/8461318 whenever both errors are <=alpha.

## 2. First-hit cones: a corrected combinatorial fact

Although T's symbol-zero and symbol-one counts do not exceed U's counts, **T cannot be an ancestor of U**: between depths 8 and 12 there are only 4 symbols, but reaching U from T requires 5 extra non-symbol-2 observations (3 zero and 2 one). Conversely U has greater depth and cannot precede T. Thus T/U first-hit cones are disjoint, refuting only the Stage176 packet's tentative suspicion of nested cones.

Positive ordered-history first-hit data from unmerged DFS:
T: 28 paths; P-mass 109375/746496; Q-mass 109375/1679616.
U: 4,864 paths; P-mass 59375/573308928; Q-mass 59375/1088391168.

Keep P and Q positive-rational masses as **separate labeled measures**, in accordance with BRC residual/provenance semantics. Because Q/P is constant on a count state, any history-dependent tie coin can be replaced by its positive-P-mass weighted average without changing P or Q errors or expected times. Since the T and U cones are disjoint, no interaction remains; the full Bellman-optimal family has affine observables.

## 3. Independent exact primal observations

Let t be probability of deciding P at first-hit T (else continue), u the corresponding probability at U. All other states take their unique Bellman actions. Let M=(eP,eQ,tP,tQ). Exactly,

M(t,u)=M00+t*dT+u*dU,

M00=(153187818587049839/438244169232678912,
27935332957655/80244904034304,
633635672818036049/54780521154084864,
74702335499363/6687075336192).

dT=(-1210671875/1114512556032,
2319296875/1253826625536,
-16248859375/92876046336,
-9353640625/104485552128).

dU=(-415625/110075314176,
653125/156728328192,
-1484375/13759414272,
-771875/13060694016).

Two distinct exact methods evaluated each of the four (t,u) in {0,1}^2: rational suffix DP (grouping only future counts) and **unmerged ordered DFS with independent integer numerator path masses p/24^n and q/12^n**. All four observables and all stopping masses agreed exactly (P/Q terminating mass 1). DFS node counts were 296764,267580,292900,263716, total 1120960. The four-coordinate mixed coefficient M11-M10-M01+M00 is exactly zero. The attached actual executed code and exact witness certificate allow reproduction without floating-point tolerances.

## 4. Balanced legal policies and full interval proof

Solving eP=eQ gives the unique affine relation

t(u)=1870960582929997/3860125696000000 -(40793/15078616)*u.

For **every real** u in [0,1], both coin values are legal; t(u) is strictly between zero and one. The old endpoint u=1 has t=1860517574929997/3860125696000000 and matches Stage176 exactly. The new endpoint u=0 has the displayed alpha177,V177. The common error is strictly increasing as u decreases, by total amount

alpha177-alpha176=251195378125/300094765349732352>0.

At the u=1 end tP-tQ equals 10455836014844563234957/29500515812940089131008>0; at u=0 it equals 1161161876520242492773/3277835090326676570112>0. Also at **both** endpoints tP+K eQ+L eP=H. Every observable is affine in u; error balancing, time dominance, dual equality and strict monotonicity therefore hold at all real intermediate u. The explicit legal strategy achieves the universal lower bound, completing the proof.

## 5. Strict right-support boundary

If a feasible strategy at alpha>alpha177 attained H-(K+L)alpha, the chain

max(tP,tQ) >= tP >= H-K eQ-L eP >= H-(K+L)alpha

and K,L>0 would force eP=eQ=alpha and Bellman equality at every reached positive-P-mass ordered prefix. All nontied actions are strict; only T/U can vary. At each tie, ordered-history coins can be P-weight averaged because Q/P is fixed and both T/U cones are disjoint. Therefore its observables would equal M(t,u) for some t,u in [0,1]. Equal errors require the above t(u), on which the largest common error is alpha177, contradiction. Thus this support line is strictly below the actual optimum to its right. This does **not** describe subsequent segments.

## Verification, limits and next question

Execution of the exact Python checker concluded STAGE177_AUTHOR_EXACT_FULL_REAL_PASS; Bellman states 680/680, strict gaps 1238, zero mixed term, both deterministic-corner algorithms consistent, 1120960 ordered nodes, legal continuum and both endpoint identities checked. A separate exact rational continuation-ray scan gave Stage178 **DUAL_ONLY**; see NEXT_TASK_PACKET_178.md. BRC reuse applied to positive-rational branch-labelled first-hit observers, not to native X6 dynamics. No scientific claim is promoted to P000, Working Truth or Foundation.

Actual authenticated GitHub user awdawmip has repository push permission. Native task query returned CONTROL_QUOTA; native session creation returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). No live owner, formal CLAIM, Source Result or independent Driver admission was confirmed. GitHub readback establishes storage, not remote execution.
