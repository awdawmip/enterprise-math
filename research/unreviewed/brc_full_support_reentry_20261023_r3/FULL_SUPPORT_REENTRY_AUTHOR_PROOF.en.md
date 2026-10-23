# A full-support robust reentry theorem for a four-label BRC occupancy observer

**Exact author-side result, 2026-10-23. UNREVIEWED / NOT ADMITTED / NOT NATIVE X6.** Extends the earlier three-action witness at `awdawmip/enterprise-math@1209c4c37206a2f04266da36dfa01762020f91d6`; it does not modify P000.

## The model and theorem

Take hidden labels `0,1,2,3` and good exact-occupancy sets `G={{0,1},{1,2},{1,3},{2,3}}`. For independent draws governed by a public word `w`, define `delta_t=P(occupied-label set at t is in G)`, `Delta_t=delta_t-delta_(t-1)`, `M_t=max_{0<=s<=t}delta_s`, and `R_t=sum_{j=2}^t max(Delta_j,0)-M_t`.

Let `w=032020`, with the full-support action laws, written in label order and sharing denominator 1000:

`Q0=(1,665,1,333)/1000`, `Q2=(333,333,1,333)/1000`, `Q3=(1,1,1,997)/1000`.

**Theorem:** The strict residual-growth times up to length six are exactly `{4,6}`. The same assertion, including strictly positive mass at every label/action, holds for every three-vector family `(Q'0,Q'2,Q'3)` satisfying `TV(Q'a,Qa)<1/2000` for all actions. Therefore an open full-dimensional subset of the product of three four-label probability simplexes exhibits two separated growth episodes. Full support by itself does not entail the two-action one-episode conclusion.

## Exact integer certificate

For each good pair `{i,j}`,

`P(D_t={i,j})=prod_{s=1}^t(Q_{w_s,i}+Q_{w_s,j})-prod_s Q_{w_s,i}-prod_s Q_{w_s,j}`.

Summing the four disjoint events, the exact integers `N_t=1000^t delta_t` for `t=0..6` are

`[0,0,666000,554226216,626011982376,429146205098784,436231737917062944]`.

Hence

`Delta_3=-111773784/10^9`, `Delta_4=71785766376/10^12`,
`Delta_5=-196865777277216/10^15`, `Delta_6=7085532818278944/10^18`.

The largest occupancy through round six occurs at `t=2`, where `delta_2=0.666`; the largest later occupancy is `delta_4=0.626011982376`. Thus the running peak is frozen for all `t=2..6`. The strict residual gain is positive at round four, zero at five, and positive at six, with the exact fractions above.

## Proof of the open-neighborhood assertion

Let `eta=1/2000`. By maximal independent coupling of each draw, if every action law is TV-distance `<eta` from its reference, every prefix occupancy event obeys `|delta'_t-delta_t|<=t eta`. Consequently

`|Delta'_t-Delta_t|<=(2t-1)eta` and
`|(delta'_2-delta'_t)-(delta_2-delta_t)|<=(t+2)eta`.

For `t=3,4,5,6`, the displayed exact fractions satisfy `|Delta_t|>(2t-1)/2000`; the narrowest inequality is `Delta_6=0.007085532818278944>11/2000=0.0055`. Furthermore each `delta_2-delta_t >= 0.039988017624>8/2000 >= (t+2)/2000`. Therefore every perturbed sequence retains the sign pattern `-,+,-,+` and a unique earlier peak at `t=2`, proving the growth pattern `{4,6}`. Each probability coordinate changes by at most its distribution's TV, so it remains `>1/1000-1/2000=1/2000`.

**Explicit parameter interval:** From the original `q0(z)=(0,(1+z)/3,(1-z)/3,1/3)`, set `Q0(z)=(996/1000)q0(z)+(1/1000)(1,1,1,1)`, holding `Q2,Q3` as above. Then `TV(Q0(z),Q0(1))=(83/250)(1-z)<1/2000` for all `663/664<z<=1`; hence two episodes persist on that entire interval with full support.

## Evidence and boundaries

The accompanying integer verifier implements a 16-mask occupancy recurrence and independently computes the four exact good-pair inclusion-exclusion products; they agree at all prefixes. Fraction arithmetic checks the TV-margin assertions. The result is a scoped auxiliary-model counterexample. It neither supplies a necessary-and-sufficient criterion on general action families nor establishes a faithful transfer to P000 native X6 Cell geometry and operations. Next mathematical unit: find a testable closure/order property on admissible action families that ensures a single growth episode for all words.

Snapshot: global `6a791715af63fdb1a7f291c976f3c1baf97cac6f`; EM main `1da5fc197dab4e64dc27c97f298cb347475b2e6f`. Native research controller reported `CONTROL_QUOTA`; new session was denied `STATIC_READONLY_SCOPE_DENIED` (`operation_sent=false`). No authoritative current Owner, formal CLAIM or Driver-admitted Result is asserted.
