# R749 — Exact V29/V39 event-permission separation and minimal C1 witness obstruction

Status: author-side theorem and finite exact checks; native permission NOT asserted.
Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Run RUN-aea48b2b684b1204bf7fd828, generation 1, checkpoint revision 1; CLAIM MCP-aa543cb564e2a231d3fe6017.
Frozen P000 science: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Preserve R747/R748 author-side results without repeating them.

## Exact source contracts
V29: research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md, current main read 2026-11-12.
PASS(x;a->b) changes only M_x[a,b] += 1. TRANSFER(x:a->y:b) changes only Rout_x[a] += 1 and Rin_y[b] += 1, on a declared allowed connection. Derived Delta u for PASS is e_a-e_b; transfer is -e_a at x and +e_b at y. Both conserve network scalar Q.
V39: research_notes/X6_CYCLE_CURRENT_S3_OPERATION_SAFE_PORT_V39_20260906.md, current main read 2026-11-12. (j,h) is coarsest exact quotient for a DECLARED based-loop future language L_JH, where j is transfer cycle chain and h is S3 frame transport. V39 does not define primitive C1 force updates or permit a one-port replacement as a PASS.
P000: definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, frozen pin. Primitive stable nonzero balance iff 3 quanta and TRIADIC_CLOSURE_E. X6 spatial Cell torsor is Z^6; port/internal decoration is not a spatial axis.
R747: research_notes/portable_direct/2026-11-12_R747_C1_framed_port_connection_exact_S3_holonomy.md at ed44c4e1f6c7bd2adc545fa60047619f71a59992. Its retained-slot replacement is a candidate incidence update, explicitly NOT a native V29 PASS or V39 Link/Port event.

## Theorem 1 (no C1 mutation from a pure V29 event)
Let the decorated state be (L,F,C,P), with L=(M,Rin,Rout) the V29 count ledger, F a framed signed C1 port triple, C its triadic closure certificate, and P provenance. Interpret the exact V29 primitive event definitions literally: the PASS and TRANSFER maps modify only the specified L entries; all other fields are unchanged. Then every finite V29-only event word fixes F,C,P. In particular it cannot realize an R747 one-port replacement F -> F' != F, nor a change in the triadic closure certificate.

Proof: each generator fixes F,C,P by definition; induction on event-word length.

Scope: this is a theorem about the literal primitive V29 grammar, not a universal impossibility of an augmented coupled event. An extended scheduler may legally combine a V29 count update with a separately declared typed force/port update, provided the extension receives its own event permission and provenance law.

## Theorem 2 (sharp ledger observer obstruction)
The V29 projection pi(L,F,C,P)=L cannot determine TRIADIC_CLOSURE_E for arbitrary decorated C1 candidates. Take the same Cell c, same nonnegative ledger L=0, same three distinct signed unit ports and equal nonzero quanta. Decorate one candidate with a valid declared C1 cyclic closure witness C=true and a second with no admitted closure witness C=false. Both have identical L, u and Omega, but the first is primitive stable under P000 and the second is not. Thus no count-only function f(L) can return closure for all such states.

This uses the declared possibility of nonclosed three-force candidates; P000 expressly says not every triple is balanced. If a future substrate forces all chosen triples to be closed, the witness must instead vary an independent legal closure/incidence decoration, or the scope must be restricted. The theorem does not assert two contradictory closure values for one identical FULL native state.

## Theorem 3 (minimal composite event interface)
A proposed R747 replacement with one signed port changed requires at least one event beyond the V29 primitive count grammar, or an explicit coupled transition that updates the C1 port/closure/provenance decoration. A minimal typed candidate is:
  (1) PRE: same Cell c, q>0, distinct signed axes, exactly two retained identical signed ports, valid closure witness and declared allowed Link/Port incidence for the removed/new port;
  (2) COUNT: a legal PASS or TRANSFER increment per V29;
  (3) PORT: replace the third signed port while retaining the two surviving named slots and their provenance, as in R747;
  (4) CERT: explicitly verify or produce TRIADIC_CLOSURE_E for the new triple, and retain the transition's source edge ID;
  (5) DEPENDENCY: order the coupled event against other updates that inspect the same frame/Cell; do not infer commutation from additive ledger increments.
These are necessary typing/verification obligations for an extension, NOT a proof of existence or native authorization. V39 (j,h) is operation-safe only for its declared loop future language and cannot erase the additional C1/closure/provenance obligations.

## Exact finite check
For three local port labels, enumerate 3*3=9 PASS(a,b) increments and 3*3=9 matched TRANSFER(a,b) endpoint increments. All 18 preserve scalar network Q exactly. For a fixed three-port frame, 3*2=6 distinct one-port slot substitutions change the frame, whereas any V29-only event leaves it invariant. The checks use integer arithmetic and direct enumeration; the universal statements above are proved by generator induction.

## Unresolved
1. Obtain the exact native permission guard for a coupled C1+PASS event, if one exists outside V29/V39. These two sources alone do not grant that permission.
2. Test R748 adaptive selector against declared source/target closure certificate and native Link/Port allowed connections.
3. Construct a fully legal reverse-compensation PASS witness with both count and closure certificate, or return a guard-specific counterexample.
4. Independently review and promote only the supported theorem scope; no native mathematical acceptance is claimed.
