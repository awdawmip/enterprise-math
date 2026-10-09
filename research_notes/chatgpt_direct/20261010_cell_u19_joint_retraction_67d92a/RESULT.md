# U19: joint retraction, blocked returns and recovery workspace

Event: EM-20261010-CELL-U19-JOINT-RETRACTION-67D92A
Status: CONDITIONAL_MODEL_THEOREMS / EXECUTED_TYPED_BRC / UNREVIEWED
Global read: 49fc56686ae4ebff08bbc86a5cb591068d7caa66
Source intake: 188db27e55ae8650262f854963ea5dbd1d9e40c7

## Continuation and scope

This continues the uploaded U18 SOURCE-RETRACTION-51D8C7 package, whose NOTE blob is eb436370d7f4479bf71a47ad3a53012f6631f347. Its eighteen manifest entries were verified. The repository's U18 RESTORATION-AND-RETURN-A6D3E2 is a distinct directional-race result, read separately rather than misreported as publication of this predecessor.

All four material bodies can now move. The prepared labelled tree, original path suffixes and their meeting Cells remain field-memory inputs. Thus this is restoration of a prepared relationship, not spontaneous contact formation or a freely translating self-bound object. Native X6, twelve signed directions and separate time typing are retained. The weights and serialized update law below are explicit model assumptions; no native triadic-force, mechanical reaction, physical clock or prime criterion is claimed.

## Model and all-time theorem

Actor i has tree degree d_i and chronological stack w_i. Its Cell is x_i^0+displacement(w_i); every incident original leg gamma becomes reverse_opposite(w_i) gamma. Current body Cells are distinct. A past record Cell is not itself a currently occupied material Cell.

Select an actor uniformly. Its return proposal has weight1; EACH native extension has weight lambda^d_i. Normalize by 1+12lambda^d_i. Collisions, empty stacks and capacity failures wait with their original weights. A permitted extension adds d_i edge records through unchanged U9 material(); a return removes those same most recent records. The core suffix is retained in this candidate, not declared immutable in all future research.

Let L=SUM_i d_i|w_i|, o the all-empty stack tuple, and Omega_0 its communicating component. Do not assume all endpoint-admissible tuples belong to that component. Every nontrivial transition has its actual U9 inverse. For an extension w->v of actor i,

    lambda^L(w) P(w,v) = lambda^L(v) P(v,w).

Ignoring exclusion only increases the positive state population. Actor i has12^n possible words of length n. Therefore

    1 <= Z_0=SUM_(w in Omega_0)lambda^L(w)
      <= PRODUCT_i (1-12lambda^d_i)^(-1) < infinity,

for0<lambda<1/12 and every finite connected preparation. The product is a counting majorant, not independent replacement dynamics. Actual BRC positive recurrent closures evaluate its factors. The finite invariant probability lambda^L/Z_0 on the connected countable chain proves eventual restoration with probability1 and finite mean hitting times. Kac's return relation gives E_o T_o^+=Z_0. Standard recurrence theory is attributed to Aldous/Fill, author-hosted book section13.2; the model, source bridge and workspace witness are the present conditional application.

For the original four-body chain AB,BC,CD, degrees are(1,2,2,1). At lambda1/48:

    Z_0 <= 65536/36481;
    pi(o) >= 36481/65536;
    E_o T_o^+ <= 65536/36481.

The last quantity includes waiting returns. Root departure probability is33/386, so the mean excursion AFTER a departure drawn from the root's own exit distribution is at most3738410/401291. This is not a uniform small bound for an arbitrary rare blocked input. Counts are committed proposals, not physical heartbeats.

## Explicit blocked state and minimal recovery

Start A,B,C,D at(0,E1,E1+E2,E2). With G=extend and R=return, execute

    A:G(+E3), D:G(-E2), D:G(-E2), A:R, A:G(+E2), D:R.

All six moves are legal. They leave A at E2 with stack(+E2), D at0 with stack(-E2), and the other stacks empty. The occupied Cell set is unchanged, but both returns target the other leaf's occupied Cell. Every return proposal waits. The extra record count is2 and its next expected change is203/2316>0: the old single-leaf uniform negative-drift proof no longer applies.

A legal recovery is

    D:G(-E2), A:R, A:G(+E3), D:R, D:R, A:R.

Record counts are2->3->2->3->2->1->0. Labelled positions, original paths and resource assignments return. No head-on swap or primitive diagonal is introduced. Three simultaneous extra records are necessary: at cap2 no grow can begin and all returns are blocked. Six proposals are necessary: zero extensions cannot begin; one temporary extension frees one leaf but the other then returns into the first leaf's pending parent, blocking cleanup. At least two extensions and four returns are required. The displayed path attains both bounds.

Complete shortest-layer BRC enumeration gives180 six-proposal recovery histories, each weight1/36000000, total1/200000. This is a shortest-path event probability, not the eventual return probability. The preparing six-proposal history has positive weight1/82944000000.

## Capacity changes reachability, not just a long-record tail

For total-record cap B, let Omega_B be the ROOT component after replacing over-cap growth by waiting. Its stationary law is lambda^L/Z_B on Omega_B. Complete checks give:

    B0: admissible1, root component1, Z_B=1;
    B1: admissible21, root component21, Z_B=17/12;
    B2: admissible446, root component401, Z_B=911/576;
    B3: admissible7274, root component6730, Z_B=10129/6144.

All52 labelled rows and stationary incoming masses were checked. The swapped-leaf state is admissible with L=2 but absent from Omega_2; it belongs to Omega_3. From this explicitly prepared input, return probability is0 at cap2 and1 at cap3. The cap2 process starting at o cannot spontaneously enter that disconnected trap; its preparation used a third slot.

Twenty-three states with L<=2 are absent from Omega_2 but present in Omega_3. Consequently the cap2 stationary approximation has an IN-RANGE missing-mass lower bound

    TV(pi_2,pi_infinity) >= 23lambda^2/Z_0
                        >= 839063/150994944.

A long-word-tail-only error statement would miss this. Nevertheless Omega_B increases to Omega_0, since every finite legal path has a finite maximum record count. Hence Z_B increases to Z_0 and TV(pi_B,pi_infinity)=1-Z_B/Z_0 tends to0. Quantitative rates need recovery-workspace bounds as well as present length.

## Executed resources, reproducibility and remaining target

The finite resource implementation uses actor-local LIFO bundles. Every extension depth carries d_i distinct edge IDs. Unused records move in that actor's backpack at the actual one-edge carry stage; older bound records stay at their old heads. Reservation/detachment, carrying, and attachment/release preserve disjoint free/held/bound identities and their Cell locations. Each leg retains its head and meeting even while temporarily unmatched. Capacities(2,1,1,2) provide eight extra records plus the three original core records. Five padded work stages per proposal remove an unreported degree-dependent clock bias. These are recorded logical/transport stages, not calibrated physical duration.

All four bodies were also translated serially by+E3 using unchanged U9 operations, retaining six added records, then restored. This differs from freezing three bodies; the old field-memory sites still remain.

New checks:490586 assertions; complete cap0..3 graphs;23192 full U9 bridge checks;364 resource transactions and valid inverses;180 shortest recovery histories; positive all-length normalizer. An isolated process reproduced results and compressed trajectory bytes exactly. This is same-author replay, not independent review. The earlier U18 full suite was not recounted as new work.

Full proofs, new code, pinned dependencies and detailed traces are in the conversation package cell_closure_u19_evidence.zip. This Source report and its paired result/checkpoint are durable scientific evidence; they are not a claim of a standalone Source-only full-suite installation. Dependency blobs: returning_path.py4b5cf21a58583c469548ef508a16e0d4d752520c; local_latent.py67408af5b977bed7295f7225cdd3f550c41b9729; connected_retention.py569e6171d0052fbfd41cf007b09a8327b339228b; packet_router.py7465f5aa16cbb8fba61ba4be80f8a6884b879c53; brc_weighted.py3f205696709e847909958a153f8fe10d3f6b70f0. Old scientific functions were unchanged. A development checker sign error in the inverse label of POP was corrected before the final full tests; it is an implementation error, not structural residual.

Results SHA256:8b49ab0322fe90ab69d5825c2f76d990606e734db5396b4270aac179e12abbfe.
Trace SHA256:29afc3b727fca00702456c9afba1a01e26bf372c082598ad44e634ad5d6cf9ac.
Compressed trace SHA256:d06514f00a83b4a2fd9b686f7d0168b281a881c63c89bcf821b7b5c3b6935cc4.

Research activity registration remains unresolved; no historical role/session, formal Task/CLAIM/Result or native admission is borrowed. The next target is a sourced interaction that creates or updates the retained core/meeting structure while preserving useful joint-return properties, including material/field/support reaction. This unit supplies an all-moving prepared-contact recovery benchmark, not a natural law selected by square or prime identity.
