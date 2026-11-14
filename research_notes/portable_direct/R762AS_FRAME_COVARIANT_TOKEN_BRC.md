# R762AS — Frame-covariant ordered BRC, exact repeatability and atomicity witness

**2026-11-15; author-side proof and finite exact checker; NOT_REVIEWED.** Task: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\` / \`TP2-8B7E13C5904A2D6F1142\`. Researcher \`EM-X6-3050F6\`, original session \`MCP-4b2d70a97f594366a7c94a0f8b45df38\`. Frozen scientific input \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.

## Exact question and input typing

R762U proves the sharp minimal initial inventory over arbitrary reorderings of a V29-like event multiset. R762AR proves the exact **fixed-order** inventory residual \`(Delta,H)\` and shows that a fixed word with nonzero Delta cannot be repeated indefinitely from a finite stock **when port labels stay fixed**. V17 separately defines conditional \`S3\` holonomy on active-triad internal frame slots; V29 defines actual nonnegative count-ledger \`PASS\` and \`TRANSFER\` increments but imposes no token-availability precondition. This note tests an explicitly declared *source-port bridge* under which frame holonomy permutes the port labels used by a conditional causal-token lift.

Let V be a finite set of individually named, typed \`Cell:Port\` vertices; let \`G <= Sym(V)\` act faithfully by permutation on inventories and directed edges. A word \`w=(a_i->b_i)_{i=1}^m\` is an ordered sequence of V29-typed PASS/TRANSFER occurrences with individually retained IDs, satisfying the declared link skeleton. For the **extra causal-token semantics**, firing \`a->b\` requires at least one nonnegative integer token at tail a and moves exactly one token from a to b, including when a=b. All counts are exact integers; signed differences are derived, not signed token inventory.

For each prefix let \`D_w(v,k)=#out(v,<=k)-#in(v,<=k)\`. Define
\`\`\`
Delta_w(v) = D_w(v,m)
H_w(v) = max(0, max_{i: a_i=v} [ D_w(v,i-1)+1 ])
\`\`\`
with the maximum over an empty set omitted. These are the verified R762AR quantities. The exact fixed-frame feasibility of w from stock n is \`n >= H_w\` coordinatewise, with final stock \`n-Delta_w\`.

**Additional frame-port bridge assumption B:** a fixed declared identification \`beta\` identifies the three relevant active-frame slots with three port labels in V; a V17 holonomy \`h in S3\` acts on these port labels as \`sigma=beta h beta^{-1}\`. The macro-event consists of the word w in the current active port frame, followed by an internal frame transport \`sigma\` that has no **additional** token inventory effect. The real operator that couples V17 to V29 has not been admitted; B defines the conditional mathematical model studied here. With current frame g, the actual executed word is \`g(w)\` and the next frame is \`g sigma\`. Thus the state transition is
\`\`\`
(n,g) --(w,sigma)--> (n-g Delta_w, g sigma),
enabled iff n >= g H_w.
\`\`\`
Here permutations act on vector *coordinates*: \`(g x)(g v)=x(v)\`, and products act right-to-left. The full state retains the named port mapping and frame; neither the original event IDs nor any V39 based-loop observer is erased by this token-only quotient.

## Theorem AS1 — exact semidirect max-plus BRC residual

For any two macros A=(Delta_A,H_A,sigma_A), B=(Delta_B,H_B,sigma_B), executing A then B in the same global frame has residual
\`\`\`
A star B =
( Delta_A + sigma_A Delta_B,
  max(H_A, Delta_A + sigma_A H_B),
  sigma_A sigma_B ).
\`\`\`
The maximum is coordinatewise. Identity is \`(0,0,id)\`. This operation is associative. For the observer that, for every starting inventory and starting frame, returns FAILURE or SUCCESS together with complete final inventory and final frame, two realizable macros have the same action iff their triples agree (assuming G acts faithfully and frame is directly observed).

**Proof.** A requires \`n >= g H_A\` and leaves \`n-g Delta_A\`. B then requires \`n-g Delta_A >= g sigma_A H_B\`; equivalently \`n >= g(Delta_A+sigma_A H_B)\`. On success, final inventory is \`n-g(Delta_A+sigma_A Delta_B)\` and final frame \`g sigma_A sigma_B\`. This proves the formula and its associativity by equality with actual serial execution. If frame permutations differ, final frame distinguishes them. If Delta differs, choose n large enough for both to succeed; final inventory distinguishes them. If Delta agrees but H differs, choose n with a threshold separating some port H values and all other coordinates sufficiently large; one macro succeeds, the other fails. QED.

This is a frame-covariant extension of the **already established** ordered BRC residual, not another proof of R762U's Euler-decomposition result. Its lossless scope is precisely the declared inventory+frame observer.

## Theorem AS2 — exact repeated-macro seed and orbit-balanced indefinite execution

Fix a macro \`A=(Delta,H,sigma)\` and let q be the finite order of sigma. Define
\`\`\`
D_r = sum_{j=0}^{r-1} sigma^j Delta,
H_r = max_{0<=j<r} ( sum_{k=0}^{j-1} sigma^k Delta + sigma^j H )
\`\`\`
with coordinatewise maximum and the empty prefix taken as zero. Then \`A^{star r}=(D_r,H_r,sigma^r)\`; from identity frame the unique componentwise smallest seed for exactly r macros is H_r.

Put \`B=D_q\`. For k>=1:
\`\`\`
D_{kq}=kB,
H_{kq}=H_q+(k-1) max(0,B).
\`\`\`
As every primitive edge moves one token, \`sum_v B(v)=0\`. Therefore the same finite stock can execute arbitrarily many successive frame-covariant copies of A **iff** \`B=0\`, equivalently
\`\`\`
sum_{v in O} Delta(v)=0   for every orbit O of sigma on V.
\`\`\`
When this holds, H_q is sufficient for all future repetitions and is the least such stock. For a transitive 3-cycle on exactly three ports, token conservation alone enforces this orbit condition. For a transposition exchanging two ports and fixing a third, it demands no net deficit on the fixed port and cancellation across the exchanged pair.

**Proof.** The first formula follows by successive application of AS1: macro j occurs in frame \`sigma^j\`, and its local H is added after all prior net deficits. Since \`sigma^q=id\`, the q-macro block has ordinary fixed-label residual \`(B,H_q,id)\`. Apply R762AR's r-fold formula to k identical q-blocks to get the displayed expression. A fixed stock exists for all k iff every B(v)<=0; conservation then forces B=0. On an orbit O of length d dividing q, \`B(v)=(q/d) sum_{u in O}Delta(u)\` for every v in O, proving orbit equivalence. If B=0, every q-block returns both stock and frame unchanged, so the seed H_q also enables every partial suffix forever. Necessity of H_q is immediate from the first q blocks. QED.

**Important new distinction:** R762AR's fixed-port indefinite-replay condition \`Delta=0\` is the special case \`sigma=id\`. With an actual port-permuting frame bridge, indefinite resource feasibility can hold while \`Delta != 0\`.

## Theorem AS3 — a three-source explicit frame-holonomy witness

Let three typed local ports be \`a,b,c\` in one declared Cell and take the **ordered V29 PASS word**
\`\`\`
w = (a->b)(b->c)(c->a)(a->b).
\`\`\`
The first three occurrences have exactly the unsigned 3-cycle count pattern of V27's atomic triadic passage; the fourth supplies one further count increment. This is one chosen **sequential** V29 realization, not an assertion that the V27 aggregate event has itself been endowed with this firing order. Set the conditional frame-port transport \`sigma=(a b)\`, fixing c, via an explicitly declared \`beta\` mapping from the corresponding V17 transposition.

Direct prefix computation gives
\`\`\`
Delta_w=(1,-1,0),   H_w=(1,0,0).
\`\`\`
Starting from one token at a, the first word leaves one token at b. In the transported frame, the second word is
\`\`\`
(b->a)(a->c)(c->b)(b->a)
\`\`\`
and returns the token to a. Consequently
\`\`\`
A star A = ( (0,0,0), (1,0,0), id ).
\`\`\`
One token at a executes **every** number of repeated frame-covariant macro-events; zero tokens cannot fire the initial event. The fixed-label repetition of the same w, by contrast, requires r tokens at a for r copies (R762AR, H_r=(r,0,0)). Thus a genuine frame-to-port transport *can* turn a linearly growing seed requirement into a bounded one in this exact source-labelled auxiliary model.

A separate, equally sharp **atomicity witness** uses the three-event cycle \`(a->b)(b->c)(c->a)\`. Its ordered serial firing has \`H=(1,0,0)\` (one token), whereas a simultaneous atomic reservation rule requiring all three outgoing tokens at the macro's start requires \`n(a),n(b),n(c)>=1\` (three tokens). V29's original cumulative count-ledger events have no such token gate. Hence selecting a serial, jointly reserved atomic, or ledger-only admission law is a substantive dynamics choice, detectable already on the three-port cycle.

## Exact verification

Runnable JavaScript: \`R762AS_FRAME_COVARIANT_TOKEN_BRC_VERIFY.js\` (Node.js standard runtime only; integer operations, no floating-point model). It exhausts every 3-port directed word of lengths 0..3, including loops (820 words), all six port permutations and repeat lengths 1..8: **39,360** independent formula-versus-expanded-word comparisons. It also directly executes each computed minimum inventory, checks every positive component's one-token sharp failure (**79,536** checks), and classifies all **4,920** word/permutation macro pairs by the finite orbit criterion. All passed in the author execution; the JSON file is the verbatim checker output. These finite tests independently validate the implementation and the displayed examples; AS1–AS3 have general algebraic proofs above.

## Sources, scope, next unsolved unit

- Frozen P000 spatial/triadic definition: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
- Actual V29 ledger law: \`research_notes/X6_NETWORK_EVENT_LEDGER_AND_CONTRAST_TRANSDUCER_V29_20260906.md\` on canonical main (read 2026-11-15, blob \`6849ebd3fc776fb7da3b46627376490aba3dad99\`).
- V17 conditional active-frame holonomy: \`research_notes/X6_ACTIVE_TRIAD_HOLONOMY_CONTROL_V17_20260906.md\` (blob \`42b810a8f82c504833027da17884cc4fb2943e5b\`).
- V27 unsigned atomic triadic passage count pattern: \`research_notes/X6_ATOMIC_TRIADIC_PASSAGE_DRIVES_ODD_HOLONOMY_V27_20260906.md\` (blob \`c5a02e6727dfc1f70ae4594c3ee807d1760c0be9\`).
- R762U Euler seed theorem: \`research_notes/R762U_CAUSAL_TOKEN_LIFT_AND_SEED_MINIMALITY.md@f2a0a3a63dcc024cb4df5d3f056a7ad1e8a2d288\`.
- R762AR sharp chronological \`(Delta,H)\` monoid and original 22-occurrence witnesses: \`research_notes/portable_direct/R762AR_CHRONOLOGICAL_TOKEN_RESIDUAL.md@6b6b61f926e344de14a183ce6dc86f5944b5113a\`.

The fully native \`TRIADIC_CLOSURE_E\` predicate still requires an independently specified signed force/Cell/Link/Port incidence, an authorized frame-to-port bridge, and explicit atomicity/restart rules. V39 based-loop holonomy is a separate observer to be joined only with a preserved typed loop/source history. The next discriminating test is to obtain the actual allowed \`beta\`, the real event's V29 subevent ordering/reservation semantics, and the V17 loop that transports that same Cell's source ports; if an admissible joint event is defined, recompute the semidirect residual on that exact event alphabet and test V39 loop readout. Preserve all full provenance in the meantime.

**No change to P000, six-dimensional X6, three-dimensional restricted slice, or native 120-degree PERP_E.**