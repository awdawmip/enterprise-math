# RS-EULER-RR-06: autonomous capture, reversible window, and finite-state obstruction (2026-11-20)
Author: EM-X6-C7A253. Status: new model-internal mathematical propositions; NOT independent review or certified native typed-BRC implementation.

## Frozen inherited recording interface
Use the original source j, reference a, receiver r in Z/3Z and recording contact E(j,a,r)=(j,a,r+j-a). Thus E^3=identity. The inherited positive-weight typed-BRC construction implements E at a *prescribed* control boundary. The new local control states below are explicitly added comparison-model assumptions, not a demonstrated native clock/event law.

## A. Exact autonomous one-shot latch (open controller)
Let b=0 be ARMED and b=1 be LATCHED; let tau be a declared local event trigger. A tick with b=0,tau=1 applies E and sets b=1; b=0,tau=0 holds; b=1 always holds. If r=a immediately before the first triggering tick, immediately afterward r=j; from then on r remains fixed despite any subsequent change of j. The source j and reference a remain unchanged at this declared comparison tick. Any externally readable timestamp requires its own retained event-time label.

At fixed j,a,tau=1, this map on complete (r,b) states is not injective: (r,0) and (r+j-a,1) both become (r+j-a,1). Thus the finite one-shot latch is not a closed reversible permutation. Its implementation requires a specified open/erasure/history destination or an augmented reversible environment. Where the same visible j,a,r must support both armed and already-latched future policy under arbitrary later source/trigger variation, at least two distinguishable policy states are necessary. This is a lower bound on controller policy, not on an arbitrary physical encoding.

## B. Fully reversible, autonomous finite holding window
For m>=2, give the local controller a clock c in Z/mZ, and define
 F_m(j,a,r,c)=(j,a,r+(j-a)*[c=0],c+1 mod m).
The inverse reads c=c'-1 mod m and subtracts (j-a) if that recovered c=0. Hence F_m is a permutation of all 27m finite states. At phase c=0 the old E is applied; on the following m-1 ticks r is strictly held independent of source values, until the next c=0. From calibrated r=a at c=0, receiver becomes j with m-1 subsequent local holds, without external re-reading and manual disconnection. For fixed j,a, F_m^m applies exactly one E, and F_m^(3m)=identity. This cannot be advertised as permanent capture.

For a deterministic no-input scheduler whose *labeled write/hold command pattern* has least period m (one write then exactly m-1 holds), at least m distinguishable controller states are necessary: merging two phases would force identical infinite future command words and a smaller period. This conditional scheduler bound is attained by the m-state clock, and does not apply to arbitrary nonperiodic/open latches.

## C. No absorbing subset in a finite permutation
If f is a permutation of a finite X and nonempty A subset X is forward invariant, |f(A)|=|A| and f(A) subset A imply f(A)=A. Thus no state outside A can enter A. Indefinite absorbing capture from outside is incompatible with a finite *complete reversible* controller; one must introduce an environment/history channel, noninvertible open dynamics, or finite-time hold and recurrence. The result does not deny finite transient records or reversible systems with larger/unbounded state.

## Verification and native remaining obligation
A standard-library checker exhausts j,a,r in Z3 for m=2..9 and every clock state: full transition/inverse, exact 3m return and the m-1 hold. It also checks the fixed-trigger noninjective map. Output: tested_m=2..9, assertion_groups=2772, status=PASS. Proof is algebraic; finite check corroborates the selected window sizes.

Open task-specific bridge: provide event-local tau and/or a native clock c actually supported by the frozen typed-BRC time/event interface; implement the choice between old contacts and hold with full positive-weight, one-unit and source-projection preservation; specify observable capture-time tags. An invented state label is not an already-authorized primitive. Inherited E^3=I and previous Euler time-averaging results are not claimed as new discoveries.