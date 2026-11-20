# X6 time: exact reachable-diamond criterion for observer-safe chronology compression

Date: 2026-11-21. Task `RS-X6-NATIVE-TIME-DYNAMICS`; frozen taskbook `TP2-91D4A7C2F63805BE21A3`; author provenance `EM-X6-FB6990`, original Research SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Prior result and new operation

Reuse the preceding verified conditional resource model (`research_notes/X6_TIME_GUARDED_TRIADIC_TRACE_COUNTS_AND_MARKOV_QUOTIENT_20261121.md@7b83f17a9a8d31cbf7ec8465086d4485c454a876`): m disjoint sources, each may fire one of three distinct labeled ports once, with q_i in {bottom,0,1,2}. That source proved future **enabling-language** quotient q-used of 2^m states, port-observable current q of 4^m and ordered-trace count. The present new question is whether discarding order stays safe when subsequent relations include a coupled environmental state.

Take an arbitrary set E with initial e0. Every candidate event a=(i,r) has an environment update F_a:E->E, and an ordinary guarded transition (q,e)->(q[i:=r],F_a(e)) when q_i=bottom. The action is a **declared conditional environment operation**; it is not a physical rotation/force law supplied by P000. All environment updates are total functions; active guard depends on q only. Different source labels have disjoint triadic resources but may nevertheless act on the same environment E.

## Theorem: reachable diamond criterion (necessary and sufficient)

The following two claims are equivalent:

(A) From every state (q,e) reachable from (bottom^m,e0), any two legal continuations consisting of the *same finite distinct source-port actions* in different orders have identical resulting (q,e), whenever those continuations begin from the same state.

(B) At every reachable (q,e), for any two distinct unused sources i,j and any ports r,s, the **reachable diamond** holds:

    F_(j,s)(F_(i,r)(e)) = F_(i,r)(F_(j,s)(e)).

Proof B=>A: any two permutations of the same distinct actions are connected by swaps of adjacent actions from different sources. At the common prefix of each swap both sources are still unused. Their q updates commute (distinct coordinates), and B gives equality of their environment updates. The suffix is then identical. Induct over adjacent swaps.

Proof A=>B: take the two legal continuations (i,r),(j,s) and (j,s),(i,r) from the chosen reachable state. Their final q agrees. A equates their e; this is exactly B.

A is *future-operation* equality, not path reconstruction. It retains the original source/port labels and preserves the order as separate provenance until a downstream observer is fixed. Stronger global pairwise function commutation `F_a F_b=F_b F_a` suffices, but is not necessary outside the reachable portion of E.

## Sharp integer counterexample (order affects an observer)

m=2, initial e=0, independent spatial resources. For two selected ports set
    F_(1,0)(e)=e+1,    F_(2,1)(e)=2e.
Then the legal trace (1,0);(2,1) yields e=2, while (2,1);(1,0) yields e=1. Both result in the same port q=(0,1) and two events. The nonzero diamond residual equals 1 (sign depends on order convention). Therefore **even 2m port-state bits are not sufficient to preserve this environmental observer** in the candidate model; one extra distinction between the two legal histories is necessary under this observer.

For affine maps F_(i,r)(e)=a_(i,r)e+b_(i,r), two distinct-source actions have commutator difference
    F_b(F_a(e)) - F_a(F_b(e))
      = (a_b-1)b_a - (a_a-1)b_b,
which is independent of e. Consequently global order independence for every starting e is equivalent to vanishing of each such integer cross-source pair residual. It is also sufficient to test from a single e0 in the affine case.

## Exact finite experiment

Standard-library checker `research_checks/X6_TIME_REACHABLE_DIAMOND_CHECK_20261121.py` enumerates every q in 4^m and every permutation of its selected source-port actions for m=1..5. In the translation control F_(i,r)(e)=e+(3i+r+1), all q have exactly one final environment value. In the noncommuting affine control F_(i,r)(e)=(i+1)e+(r+1), the number of q configurations with distinct order-dependent outputs is respectively 0,9,53,239,1003 for m=1,2,3,4,5. Independently enumerated cross-source nonzero affine commutator pairs are respectively 0,9,26,51,86. All tested global confluence flags agree with the independent commutator criterion, with zero discrepancies.

This finite check supports the full conditional theorem's exact witness, and does not count as original R063 six-file Native benchmark, physical calibration or formally admitted Result.

## Connection to the parent objective

The required native-time state depends on the observer's allowed *future actions*: with source disjointness plus independent commuting environmental updates, current q and fixed e0 suffice for exact future observer outputs. A nonzero reachable diamond creates chronology-sensitive residual, which cannot be erased by using the BRC endpoint, event count, or port configuration alone. The research objective now has a precise acceptance test for any candidate admitted X6 rotation/triadic environment law: type its actual transition, compute reachable two-event diamonds under all relevant observers, then prove safe quotient or preserve the extra trace state. Current evidence establishes this conditional test; no current P000 physical link/environment admission is assumed.
