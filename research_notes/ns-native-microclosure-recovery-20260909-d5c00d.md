# Recovered event 11: microscopic matching and primitive-action audit

Event: NS-NATIVE-MICROCLOSURE-20260909-D5C00D-11
Researcher: EM-DIRECT-D5C00D / TASK_RESEARCH
Activity: RA-D5C00DF7D77F4AA2ACE0
Status: TESTING; recovery of previously executed work, not a new execution or independent review.

This is a faithful condensed project landing of the prior local-only checkpoint. It does not claim to be byte-identical to the original full paper. The original package remains attached to the originating conversation. Its full note SHA256 is b9e123a07c97aa143de3d0eeb6cc76280ac58eb229efdea8da795606997acbee; checker SHA256 bd8c991533ca3e7786505bc363e14734dc979c42678577232a3f112ec379d2c4; result SHA256 1117e0ebaa5e5feff2ee38c359372c699f79b643b12fa0f7237720d363ecae77. These bytes were recovered and hash-checked during event 12. The source count law remains X6-DENSITY-PORT-1 at 6f119ea99021f83141321a5241dcb33b70f5af44. This landing preserves the mathematical frontier; the complete original event-11 code and long-form note are retained in the recovery download, not claimed to be separately published here.

## Exact microscopic endpoints and all-horizon descent

At an active event (j,sigma,l,m), the incoming channels are (sigma E_j,+E_l,-E_l) and outgoing multiset is {sigma E_j,+E_m,-E_m}. There are six bijective particle matchings: two keep the spectator particle in its old channel and change the other two, while four change all three. Two fixed identity-preserving implementations are

PAIR: sigma E_j -> sigma E_j; +/-E_l -> +/-E_m.
THREE: sigma E_j -> sigma E_m; sigma E_l -> sigma E_j; -sigma E_l -> -sigma E_m.

Apply either role-based matching simultaneously at all active Cells and then stream every persistent particle identity one native signed-axis step. With pi the count projection and F the frozen count rule, the local output multiset is identical, so pi U_pair=F pi=pi U_three. Integer induction proves pi U_pair^t=F^t pi=pi U_three^t for every finite horizon. This is exact count-observer descent, not a claim that identities, full paths, or force observables are redundant.

The sum A of squared channel changes is four in PAIR and six in THREE, because each changed channel crosses two different component axes. For M events, A_pair=4M and A_three=6M although all count histories coincide. A is a diagnostic, not energy or work. The required joint observer is K_vw, the number of persistent particles mapped from v to w: its row and column sums are the incoming and outgoing counts, while A=sum K_vw ||w-v||_E^2. Equal marginals do not determine K.

## Event order

Let C_z collide only at Cell z. It preserves every Cell's total count. Since all neighboring scores use only those totals, C_z and C_y commute for z!=y. Updating each Cell exactly once in a collision phase may therefore be serialized in any order. Repeating a Cell, or interleaving streaming, is not covered.

Collision and streaming do not commute: put C_2(1,+) at the anchor and one +E1 particle at E3. Collision first rotates the neutral pair to axis3; streaming first separates the core. The two resulting finite count states differ in L1 by four. Hence collision/streaming phase cannot be erased from the update contract.

For fixed neighbor scores and spectator j, the pair-axis map phi satisfies phi^3=phi. To see this, inspect the five score values on axes other than j. If the maximum has at least three ties, every state is fixed. With two top ties, these two axes form a two-cycle and all lower axes are fixed. With a unique top axis, every other pair axis moves to it; it either stays there when the runner-up is tied or swaps with the unique runner-up. These cases exhaust the score orders. The exact checker covered all 541 normalized weak orders.

A finite five-particle noninjectivity witness uses C_l(1,+) at0, with l any of the five other axes, and two +E1 particles at E3. All five full outputs coincide. This is permitted information collapse, not a proof of reversibility or a violation of count conservation.

## Eight-variable joint dependence

For four candidate-axis scores x_i+y_i with x_i,y_i in {0,1}, the indicator that candidate1 is the unique maximum is

g=(x1+y1-2x1*y1) product(i=2..4)[(1-x_i)(1-y_i)] + x1*y1 product(i=2..4)(1-x_i*y_i).

Its full eight-variable multilinear coefficient, equivalently its eighth mixed finite difference, is -3. All 256 inputs were checked; 29 select candidate1. Thus a sum of functions each omitting one of these eight inputs cannot reproduce the gate. This is not a count of primitive forces: a lower-arity circuit can compute it, but intermediate state, timing and exchanges must then be specified. A circuit with at most three inputs per gate and eight distinct necessary input leaves needs at least four gates and depth at least two, by edge counting and 3^depth>=8.

## Failed additive primitive-kick interpretation

For one THREE matching write incoming (a,b,-b), outgoing(c,a,-c), with a,b,c signed units on distinct axes. Net changes are (c-a,a-b,b-c). They sum to zero but are not individual signed-axis primitive changes. Under the ADDITIONAL trial interpretation using unit additive channel-coordinate kicks, each changed particle needs at least two kicks, six in all. Parity forbids remaining within the twelve unit channels after its first kick. Of eight shortest two-stage schedules, two use three distinct axes in the first stage; their total first-stage increment is +/-(a+b+c), with squared norm three. A stagewise conserved additive-moment interpretation needs an internal exchange of the opposite increment. That number is an obligation, not a constructed reservoir. Defining an unknown state equal to this deficit is not accepted as a force realization.

This does not refute P000. It rejects an overly restrictive bridge that identifies the independent primitive-force relation with additive channel-coordinate changes. No TRIADIC_CLOSURE_E certificate has been obtained.

## Previously executed checks recovered intact

Each of the two labelled lifts tracked 46,875 particles for three ticks. Their count mismatch was zero at all three ticks, while 4,816, 4,936 and 5,288 particle-ID states differed. There were 281,250 validated primitive streaming edges. Perturbed/reference collision counts were respectively (2408,2400), (704,640), (208,0). Perturbed-versus-reference L1 was 34,290,1122. There were 3,320 perturbed events, giving diagnostics 13,280 versus19,920. The free finite boundary contributes 2,400 first-tick collisions; it was not deleted or pinned. These finite-box numbers must not be replaced by infinite-background values.

The recovered output also records 1,440 matching cases, 345,600 S6 comparisons, 480 global inversions, 541 weak score orders, 256 Boolean gate inputs, 252 collision-serialization/commutation checks, 7,680 primitive-kick schedules and ten two-phase macro-step identities. These were performed in event11, not rerun or renamed as new event12 discoveries.

No viscosity, physical force closure, natural-law uniqueness, continuum NS theorem, Lean build or independent review is asserted. The next object is independently specified native incidence and exchange dynamics. Event12 investigates an incidence-parameterized restriction without promoting a carrier atlas into that missing physics.
