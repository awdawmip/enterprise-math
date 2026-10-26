# Stage157 — open exact primal interval from a dual-only candidate

**Model:** external N=14 ternary iid full ordered-history randomized policy, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6); objective V14(alpha)=min max(E_P tau,E_Q tau) subject to P(decide Q),Q(decide P)<=alpha. This is not native P000/X6.

Consume Stage156 author exact full-real theorem, its portable checker and its certificate in `research_notes/n14_aux_iid_affine_156_20261026/`. Do not repeat the finished Stage156 proof. It has author computation-assisted status only, not independent Driver approval or formal source Result.

**Last proved author endpoint:**
```
alpha156=7319074368089652265/21035720123168587776
V156=5285134543382516317/438244169232678912
K156=L156=109612440/326191
```

At Stage156 the G=(10,5,4) Q/continue coin is saturated at g=1. T=(14,0,0) P/Q coin remains interior at x=660136987826389/327680000000000000. When the equal dual k decreases, G becomes strict Q. A complete exact first-gap ray scan yields
```
t157=63783344160/3434465039,
K157=L157=3342600/10529,
new tie J=(10,2,0) decide P vs continue,
persistent tie T=(14,0,0) decide P vs decide Q.
```
Exact candidate Bellman census: 680 states, two ties, 1238 strictly positive gaps, minimum 232231247/11789784576, no negative gaps. Dual candidate only; no primal interval proved.

**First uncompleted scientific unit:** Under strict minimizers for K157=L157, enumerate true ordered first-hit prefixes for J and T, recording counts and both rational P/Q masses; J's a=2 and T's a=0 indicate disjointness but verify reached histories. Compute all four observer vectors from two structurally independent exact methods (conditional suffix Fraction recursion and literal ordered-prefix integer-weight DFS), then prove or disprove a zero mixed vector. Solve the two-error equality equation for the box-constrained J and T coins, compute full REAL feasible interval, verify E_P tau >= E_Q tau and Bellman support equality. Prove the entire next optimal segment and sharp right endpoint, or exhibit an exact rational infeasibility witness.

Keep ordered BRC branch identity and source provenance before observer-specific iid quotient. Freeze new global/project pins for the next run. Stage156 inputs were GLOBAL_KNOWLEDGE_V1 main@3505cfab9caffaef02ec55bebc3e549d9e4a8389 and Enterprise Math main@10d464f045afb66b679418a1acb386a910228c4b. Native control_tasks returned CONTROL_QUOTA and RESEARCHER session_start STATIC_READONLY_SCOPE_DENIED (operation_sent=false); do not equate source evidence with native CLAIM/Result authority.
