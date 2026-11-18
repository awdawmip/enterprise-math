# Stage271 — exact successor across Stage270 E–F

Date: 2026-10-29. Portable author handoff only; not a native Source Task/CLAIM/Result or independent Driver review. Parent: Stage270 proof and `REPRO_STAGE270.py` (same immutable Git commit as this handoff) on Enterprise Math PR #1571. Stage269 at `b35a4b8167e6c55e076c484968fd87c7a73d66df` and Stage270 are completed author-level research; consume, do not redo absent contrary evidence.

## Frozen scientific problem

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=12, arbitrary full ordered-history randomized policies; observers (eP,eQ,tP,tQ), objective min max(tP,tQ), errors capped by (a,b). Stage270 proves R270=conv(C,D,F,E), Bellman support lambdaP=134304895492096/947487230457, lambdaQ=48948392988/643236409, theta=(0,1), H=34613913912513106850567/458327437076524179456. Its all-real equality area is 123370733132421875/69007679864054552199168. Full corner vectors are in the parent proof.

## New proved feasible exterior point

Take Stage270 E policy (T=(0,0,5) stop-P, U=(1,2,2) continue) and switch the 20 reached histories of count (1,2,3) from stop-Q to continue, otherwise using the same deterministic choices. Call this policy `E+`. Mix `49/100 E + 49/100 F + 1/50 E+`. Independent count and ordered-word rational mass checks in Stage270's actual executed program give

    a271=133853268599/1761205026816
    b271=431993556815/557256278016
    V12(a271,b271) <= 89124381535/15479341056.

The mixture's tQ>tP. Orientation `orient(E,F,target)=−4050750660078125/69007679864054552199168`, while C is on the opposite positive side: the target is strictly exterior to R270.

## Exact unresolved research

Find a global exact Bellman dual matching this primal or another cap-saturating primal, determine the exact optimum, and prove the all-real equality face or a rigorous obstruction. Useful *independently calculated but not yet published as a Stage271 theorem* directional-support candidate preserving the old (0,0,5) P/C tie is

    lambdaP*=7566375964672/51849608449
    lambdaQ*=4026978326268/51849608449
    H*=1717930741512259706653/22294382577836949504.

A local exploratory exact Bellman call at this support showed ties at (0,0,5): P/C and (1,2,3): Q/C and 817 positive action gaps. Recompute these facts independently in the formal Stage271 certificate; classify candidate-only evidence accurately. Note a smaller parameter contact at (7,5,0) is *unreached* by Stage270's E policy, so it need not form the next observable full-dimensional face. Never infer face adjacency from an unreachable action tie.

## Acceptance

Full exact 455-state / 1274-action Bellman verification, precise rational primal-dual equality, complete ordered-history DFS verifying P and Q probability conservation, error/timing vectors, all-real iff proof including tie-ancestry and convex face dimensions, strict E–F adjacency, and an informative Stage272 successor. Native control owner/CLAIM must be checked afresh before any protected Source write. Keep research evidence `AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED` pending independent Driver acceptance, and retain the native P000 X6 mapping as a separate unproved task. Publish code/proof/actual stdout on an authorized GitHub research branch, with remote content readback; do not alter existing Stage269/270 proofs.
