# Stage448-B — Asymmetric POP + APPEND alignment-window support

Parent: Stage447-B `research_notes/n12_x6_native_brc_stage447b_output_word_dp_20261105_RESEARCH2` (2026-11-05). Frozen science GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.

## New exact question

Let m<n, P and Q binary A/B initial ordered X6 paths with A endpoints and isolated internal B, and current O=(m,n,Vp,Vq,Jp,Jq,K) fixed. Extend Stage447-B's Q-static, P-only r APPEND model by allowing one P POP at an arbitrary time (possibly after APPEND), with the usual stack semantics and separately bounded counts. Maintain the labelled trace of both full endpoints, directed adjacency histograms, and positional match K at every intermediate step.

Find an exact necessary/sufficient future-repair key and finite-state positive-integer support counter, or a concrete counterexample to a proposed key. In particular test whether (P_m, P_(m−1), Q_(m), Q_(m+1)...Q_(min(n,m+r))) suffices for every POP/APPEND interleaving, and whether part of it can be replaced by equality bits without loss. Compare the new key to Stage439-B's author-side general repair key and its frozen hypotheses.

## Small executable check

Start at m=5, n=7, kP=1, kQ=1, d=1, pP=1, rP=2; enumerate original histories and all 12-direction labelled POP/APPEND traces exactly, preserving legal stack state. For any two candidate-merged histories, produce the shortest distinguishing action sequence or a complete finite-equivalence certificate. If an obstruction appears, record the specific boundary/history feature that causes it.

## Output

Supply statement, proof or verified counterexample, exact integer population and rank costs, executable program plus actual output, limits of enumeration, and next open question in the same PR. Preserve canonical owner/CLAIM/Result/Driver authority as separately checked mutable states.
