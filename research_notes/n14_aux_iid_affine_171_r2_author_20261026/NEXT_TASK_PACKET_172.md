# Stage172: precise next mathematical unit (dual candidate only)

**Status:** Stage171 is author-exact, full-real optimality on the external N14 IID model; Stage172 has an exact **dual-only** candidate. No native Task dispatch, ownership, CLAIM, Source Result, independent Driver acceptance or P000-native inference is asserted.

## Frozen inputs / provenance

GLOBAL_KNOWLEDGE_V1 main df7e8fb68cec1d6f5925f8947a36d9c5c04eee65; Enterprise Math scientific main c69f657436d0dd0b5ad9ed848f055da9e5eb7c2f; immutable Stage170 proof 12755060786f7ef9b6657c3ea7d014d271bcb87b; Stage171 in this research branch (PROOF_STAGE171.md, VERIFY_STAGE171_REFERENCE.py, certificate171.json). Read source hashes/ref before any later reuse.

Frozen external model: P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6) on ternary **ordered** IID observations. A policy may randomize on complete histories and must stop at n<=14. Define eP=P(decide Q), eQ=Q(decide P), tP=E_P tau and tQ=E_Q tau; optimize V14(alpha)=inf max(tP,tQ) over eP,eQ<=alpha.

Verified Stage171 endpoint:

    alpha171=882435274780741015735/2530093150022563528704
    V171=4191188444229937372757/361441878574651932672
    r171=1284898704522779/1689088000000000-641597/3694880000

Exact Stage172 dual ray from (K171,L171)=(378837/1529,1128472/4587), following dK=-1 and dL=-10592/12501. Fix the previously tied R=(10,0,1) at stop-Q/continue and the Stage171-saturated U=(12,4,3) at stop Q.

A full rational 680-state first-closure scan returns:

    positive-ray step = 86081055229118646/15486841263522695
    K172 = 2453276570264541/10128738563455
    L172 = 7332367848199016/30386215690365
    H172 = 7500321462434479703133415412645/41614318285465632307238928384
    tied states: R=(10,0,1) [Q,C]; Y=(5,4,1) [P,C]
    strictly positive action gaps: 1238
    minimum strict gap = 3442966771823/273475941213285
    first newly closing gap: Y, stop P, derivative -10128738563455/1548057940328448

This is exact **dual feasibility only**; there is not yet a Stage172 primal theorem or legal randomized balanced interval.

## First independently executable question

Compute exact four deterministic first-hit observer corners for R and Y under the candidate (K172,L172), by (i) Fraction conditional count-state suffix recursion and (ii) integer-numerator **unmerged full ordered-history** DFS. Check both marginal terminal masses equal 1, all four observers agree across implementations and cross term vanishes. The two first-hit cones are disjoint: Y at depth 5 requires four zero-symbol outcomes; R at depth 10 requires zero.

Solve the exact balance relation eP=eQ for r(y); verify Stage171 endpoint recovery when y=0, 0<=r(y),y<=1 for an actual interval, tP>=tQ, strictly increasing common error, the Bellman dual equality and the sharp supporting-line right endpoint. If any condition fails, report the precise rational obstruction instead of fitting a numerical interval. After the candidate is settled, retain source/validation evidence and seek appropriately independent review and native Task publication when authorized.

Scientific constraints: all path masses remain separately positive and tagged with ordered provenance; this auxiliary problem is **not** native heartbeat/BRC-Shor or six-dimensional Cell dynamics. Native owner was not verified because em_control_tasks returned CONTROL_QUOTA and native session_start returned STATIC_READONLY_SCOPE_DENIED; no task should be claimed or reallocated by this author packet.