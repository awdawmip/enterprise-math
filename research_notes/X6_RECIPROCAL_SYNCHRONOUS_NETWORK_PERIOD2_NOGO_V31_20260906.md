# X6 upper V31: reciprocal synchronous pair-coupled networks have no deterministic recurrent period above two

Status: `FREE_RESEARCH / GENERAL FINITE DYNAMICAL NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`, `RS-X6-NATIVE-TIME-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_PURE_TRIADIC_FIELD_COUPLING_V20_20260906.md`;
- `X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md`;
- `X6_CHANNEL_NONRECIPROCITY_CIRCULATION_BRIDGE_V26_20260906.md`.
Checker: `experiments/x6_network_event_ledger_v29_20260906/check_reciprocal_directed_network.py`.

## 1. Question

V20 supplies a canonical symmetric pure-triadic pair coupling. V24-V28 show that a one-Cell memoryless destination law needs a nonreciprocal component to sustain odd-holonomy recurrent loops.

Could **many Cells with dynamically changing neighbor fields** evade that obstruction while every inter-Cell coupling remains reciprocal and symmetric?

For the natural synchronous unique-best-response class, no.

## 2. General finite setup

Let there be finitely many sites i. Each site has a finite state set A and a symmetric admissibility relation

`x ~ y <=> y ~ x`.

Let

`K:A x A -> R`

be a symmetric pair interaction:

`K(a,b)=K(b,a)`.

Let the network coupling coefficients satisfy

`kappa_ij=kappa_ji`.

At discrete event layer t, site i in state `x_i^t` chooses a unique admissible successor `x_i^{t+1}` maximizing

`H_i(y|x^t)=sum_j kappa_ij K(y,x_j^t)`

over `y~x_i^t`.

The theorem only assumes uniqueness along the orbit under study.

## 3. Cross-time score

Define

`E_t=sum_{i,j} kappa_ij K(x_i^{t+1},x_j^t)`.

Because the admissibility relation is symmetric, the previous state `x_i^{t-1}` is an admissible candidate at time t.

Unique maximization gives, for every i,

`H_i(x_i^{t+1}|x^t) >= H_i(x_i^{t-1}|x^t)`,

with strict inequality whenever

`x_i^{t+1} != x_i^{t-1}`.

Summing over i yields

`E_t >= sum_{i,j} kappa_ij K(x_i^{t-1},x_j^t)`.

By symmetry of kappa and K, the right side is exactly

`sum_{i,j} kappa_ij K(x_i^t,x_j^{t-1}) = E_{t-1}`.

Therefore

`E_t >= E_{t-1}`,

and the inequality is strict unless

`x^{t+1}=x^{t-1}`
componentwise.

## 4. Period-two theorem

On a finite periodic orbit, E_t is periodic and cannot increase strictly.

Hence at every event layer on a periodic orbit,

`x^{t+1}=x^{t-1}`.

Therefore every deterministic periodic orbit has period dividing two.

Boxed conclusion:

`RECIPROCAL SYNCHRONOUS UNIQUE-BEST-RESPONSE NETWORK -> PERIOD <= 2`.

This theorem is independent of the number of sites and independent of the detailed finite state set.

## 5. Application to X6 active triads

Take

`A = {three-axis subsets of {1,...,6}}`,

with admissibility the Johnson graph `J(6,3)` adjacency `|S intersect T|=2`.

Use the V20 canonical pure-triadic one-hot coupling

`K(S,T)=C3(e_S,e_T)`.

It is symmetric by construction.

For any reciprocal network weights `kappa_ij=kappa_ji`, a synchronous unique-best-response active-triad network therefore has no recurrent period above two.

A one-site period-two active-triad route is a backtrack

`S -> T -> S`.

The V17 shared-axis replacement transport on the reverse edge is inverse to the forward edge, so the two-step frame holonomy is identity.

Thus the declared reciprocal synchronous class cannot autonomously sustain recurrent odd V17 holonomy.

## 6. Exact three-Cell regression

For a complete graph of three Cells with equal reciprocal couplings and the V20 one-hot C3 interaction, exhaustive enumeration of all

`20^3=8000`

network states finds:

- 2700 states with a unique synchronous successor at all three sites;
- every recurrent component inside that deterministic subgraph is a two-cycle;
- exactly 1350 such two-cycles occur.

This finite enumeration is a regression witness only; the general theorem above supplies the proof.

## 7. Structural consequence

A changing field context is not sufficient merely because it is dynamic.

If the whole coupled update remains reciprocal, symmetric and memoryless in the sense above, the cross-time score forbids recurrent periods above two.

Therefore a deterministic recurrent odd-holonomy network needs at least one structural escape from this theorem, for example:

- directed / nonreciprocal inter-Cell coupling;
- an antisymmetric internal passage term;
- explicit incoming-edge/history memory;
- asynchronous/event-dependent update whose state includes order;
- another nonreciprocal relation not reducible to symmetric pair response.

V32 supplies the simplest directed network construction.

No claim is made that all physical interactions obey unique best response or synchronous updates. The result is a sharp no-go for this declared broad class.
