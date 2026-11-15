# R5 — A five-cycle exact partial-control transducer: seven states, but eight with self-loop resets

Date: 2026-11-16 (Asia/Shanghai).
Frozen scientific input: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Evidence: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTIVE / NOT_REVIEWED.
Scope: source-labelled *auxiliary integer indexed-centre* cycle-of-triangles repair model, not the native X6 metric or heartbeat dynamics. P000 and the active worldview remain unchanged.

## Precise question

Let raw masks be \(u\in\{0,1\}^5\), encoded as integers 0,...,31 with bit 0 at the least significant position. The unit 5-cycle observer is
\[
q(u)=\sum_{i=0}^4 u_i u_{(i+1)\bmod5}.
\]
The inherited common-source theorem supplies genuine source-labelled libraries \(L(v)\) of size \(25+q(v)\). Such a library serves a raw mask \(u\le v\), with resource slack \(q(v)-q(u)\). The same theorem says every arbitrary common library serving \(B\ne\varnothing\) costs at least \(25+q(\bigvee B)\).

Fix slack \(s=2\), with only two future commands: \({\rm Set}_0(0)\) and \({\rm Set}_0(1)\). A deterministic Moore source transducer has a chosen initial state for each raw mask, emits one real source-labelled library from each internal state, and must preserve feasibility and the slack bound under *every finite command word*. Let \(M_{\mathrm{stat}}\) be the minimum number of distinct outputs without commands, \(N_{\mathrm{dyn}}\) the minimum number of dynamic states, and \(N_{\mathrm{loop}}\) the same minimum when both commands must leave **every internal state unchanged**.

## Theorem — exact finite separation

\[
\boxed{M_{\mathrm{stat}}(5,2)=N_{\mathrm{dyn}}(5,\{0\},2)=7
\quad<\quad N_{\mathrm{loop}}(5,\{0\},2)=8.}
\]

Thus single-coordinate control **does not increase** the seven-output static minimum in this exact instance, but genuine transitions between internally stored source beliefs **save one state** relative to any controller that treats both named resets as internal self-loops. This is an explicit, exact separation between a moving-belief controller and an inert controller, within the original labelled-source semantics.

## Seven-state witness (complete finite transition certificate)

A state is a set of raw masks. Encode the set \(B\) by the 32-bit integer \(\sum_{u\in B}2^u\). For state \(t\), take its true source centre \(r_t=\bigvee B_t\) and output \(L(r_t)\):

| State | Belief hex | Centre \(r_t\) | \(q(r_t)\) | Set0→ | Set1→ |
|---|---|---:|---:|---:|---:|
| 0 | \`000000ff\` | 7 | 2 | 0 | 0 |
| 1 | \`00003333\` | 13 | 1 | 1 | 1 |
| 2 | \`00330033\` | 21 | 1 | 2 | 2 |
| 3 | \`01040400\` | 26 | 1 | 3 | 4 |
| 4 | \`02080800\` | 27 | 3 | 3 | 4 |
| 5 | \`54404000\` | 30 | 3 | 5 | 6 |
| 6 | \`e8808000\` | 31 | 5 | 5 | 6 |

The seven belief masks cover all 32 possible raw states. Direct integer checks establish (i) every \(u\in B_t\) satisfies \(u\le r_t\) and \(q(r_t)-q(u)\le2\); (ii) the image of \(B_t\) under either named reset is contained in its indicated target state. The first condition supplies the genuine fixed labelled library at each state; the second gives a simple induction on arbitrarily long reset words. This proves \(N_{\mathrm{dyn}}\le7\).

## Exact lower certificate for seven

For every centre \(v=0,\ldots,31\), define the canonical static coverage mask
\[
C(v)=\{u:\ u\le v,\ q(v)-q(u)\le2\}.
\]
By the inherited common-source theorem, any output library serving some raw family can be replaced by the canonical \(L(\bigvee B)\) at no greater resource cost. Consequently a six-output dictionary exists only if **six** of these 32 canonical sets cover the entire raw cube. The attached standard-library integer checker enumerates **all \(\binom{32}{6}=906192\)** choices and verifies each fails to cover the 32 states. Any dictionary of fewer than six may be extended to six centres, so the same test excludes all dictionaries with \(\le6\) outputs. As a transducer with seven internal states emits at most seven different libraries, this proves \(N_{\mathrm{dyn}}\ge M_{\mathrm{stat}}\ge7\). Combined with the explicit witness, both minima equal seven.

## Exact self-loop lower and upper certificates

If both named resets are self-loops at every internal state, the raw masks represented by each state must be closed under the bit-0 flip \(u\mapsto u\oplus1\). Such a state represents pairs \(\{2t,2t+1\}\), with \(t=0,\ldots,15\). Any nonempty self-loop state has OR-centre \(v\) with \(v_0=1\).

For each of the 16 odd centres \(v=1,3,\ldots,31\), define the largest admissible pair set
\[
P(v)=\{t:\ 2t\le v,\;2t+1\le v,\;
q(v)-q(2t)\le2,\;q(v)-q(2t+1)\le2\}.
\]
Every self-loop state served by some actual labelled library has represented pairs contained in one of these 16 canonical sets; replacing the library by \(L(v)\) is valid by the common-source theorem. The checker exhausts **all \(\binom{16}{7}=11440\)** selections of seven centres and verifies none covers all 16 pairs. Smaller solutions are thereby excluded. Conversely the eight centres
\[
(11,15,19,21,23,27,29,31)
\]
have \(\bigcup P(v)=\{0,\ldots,15\}\). For each \(P(v)\), use the source library \(L(v)\), initialize a raw pair in any covering state, and leave the internal state unchanged under either reset. This gives exactly eight states and proves \(N_{\mathrm{loop}}=8\).

## Reproducibility and verification scope

Run the adjacent \`R5_K5_SINGLE_CONTROL_EXACT.py\` with Python 3 standard library; its output is the adjacent \`R5_K5_SINGLE_CONTROL_EVIDENCE.json\`. The script verifies all 7 source centres, memberwise exact slack bounds, both transitions, the 32-mask cover, all 906192 six-centre static candidates, all 11440 seven-centre invariant candidates, and the eight-centre upper witness. All checks use Python integer arithmetic; no solver, floating point or tolerance. The finite exhaustive argument is specific to \(k=5,s=2,J=\{0\}\), and depends on the inherited source-labelled common-library theorem in precisely that model. Independent review: NOT_REVIEWED.

### Provenance and next question

Source: \`r5_partial_set_future_safe_20261116/PARTIAL_NAMED_SET_FUTURE_SAFETY_THEOREM.md\`, \`r5_slack_dynamic_source_20261116/SLACK_SOURCE_COVER_AND_DYNAMIC_BELIEF_THEOREMS.md\`, \`r5_shared_source_helly_20261116/SHARED_SOURCE_HELLY_AND_ROBUST_CONTROLLER_THEOREM.md\` at the inherited frozen pin. Historical author provenance: \`EM-DIRECT-B78E55\`, \`RA-33C87C2B703418F0706695E9\`; present Task/CLAIM permission is a separate control matter.

Next: determine whether \(N_{\mathrm{dyn}}(k,\{0\},2)=M_{\mathrm{stat}}(k,2)\) persists for any unbounded \(k\)-family, and whether an exact non-inert advantage persists for \(k\ge6\). Search for structural finite-state constructions that reuse a static covering dictionary; seek explicit lower certificates for \(k=6\) before extrapolating.