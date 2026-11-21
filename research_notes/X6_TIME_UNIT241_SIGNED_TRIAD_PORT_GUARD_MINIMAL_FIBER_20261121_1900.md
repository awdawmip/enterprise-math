# X6 Native Time — Unit241: whole-triad signed-Port selection and minimal C24 loop memory

Date: 2026-11-21 (Asia/Hong_Kong). **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Parent objective PO-X6-UPPER-STRUCTURE-20260906; Task RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3. Historical original on-hour Research lane: chatgpt-research-onhour-enterprise-math-20260923; historical Researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. This file is a portable author proof and does not claim current live Native CLAIM or execution authorization. No maintenance-lane identity is used.

## Precise source scope

The frozen scientific input is awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389, containing the P000 signed-six-axis native Cell torsor, and the source-proved OUTER C12 microtrace in research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md. One three-axis STAR is a chosen relative X6 sub-torsor, not a replacement native world or a globally distinguished spatial origin.

The separately authored candidate [guarded triadic resource law](https://github.com/awdawmip/enterprise-math/blob/f41c2690daba467ecbde99615a1337e67be46ffd/research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md) transports an intact positive force triad only via positive Port directions, with occupied-source, empty-target and available-Port guards. Its physical transfer is unadmitted. Unit240 already proved that this alphabet cannot realize a full frozen C12 microcycle and that an explicitly *conditional* signed-direction whole-triad extension can serially execute one. Unit230 already classified abstract loop holonomy, and Unit233 supplied a candidate Link cochain. The new contribution here is the exact minimum memory and a constructive source-compatible observer realization for the *guarded* whole-triad Port interface; these inherited lemmas are not being re-proved as new results.

## Source-native cycle and state model

Fix chart pivot P and selected native primitive axes e₁,e₂,e₃. Put

\[
a_0=e_1,\quad a_1=e_2,\quad a_2=e_3,\quad
a_3=-e_1,\quad a_4=-e_2,\quad a_5=-e_3,\qquad a_{r+6}=a_r.
\]

Define twelve native Cells indexed modulo 12:

\[
x_{2r}=P+a_r,\qquad x_{2r+1}=P+a_r+a_{r+1},\quad r=0,\ldots,5.
\]

They are pairwise distinct. The forward OUTER transitions \(x_{2r}\to x_{2r+1}\to x_{2r+2}\) consist of primitive steps \(+a_{r+1}\) and \(-a_r\). Backward traversal uses their exact reverse edges.

A *conditional* signed-Port update moves one labeled intact nonzero positive triad \(F=(+E_1,+E_2,+E_3)\), with declared TRIADIC_CLOSURE_E(F), from its occupied source to an empty target along an available signed directed primitive Port. The entire triad and its labels move atomically; no token is split into a one- or two-force balance. There is exactly one occupied Cell. Every edge in this 12-cycle is assumed available. Negative *travel* direction is distinct from negative *force-token* sign. A physical admission or resource sensor is not supplied by P000.

## Theorem A — sharp chirality selection cost

Assume a deterministic time-homogeneous Port selector. At each current native Cell its only visible current inputs are the Cell, the unchanged triad F and the fixed co-translated chart/Port-availability environment, unless an explicit separate routing state is retained. Require the same implementation to realize both source-possible forward and backward complete OUTER cycles, with direction chosen by different initial states rather than by an external time-varying command.

**Result:** At any of the twelve Cells, a minimum of two distinct routing states is necessary, and one chirality bit is sufficient.

**Proof.** The two prescribed successor Cells from \(x_q\) are \(x_{q+1}\) and \(x_{q-1}\), which are distinct. A deterministic function of identical complete current input cannot choose both. Distinguishing the two initial modes therefore requires at least two routing states. Let \(\chi\in\{-1,+1\}\) be a persistent bit and select the directed signed Port \(x_q\to x_{q+\chi}\). The primitive steps are source-native, the unique-triad occupancy guard succeeds at every transfer, the frame remains intact, and after 12 transfers the original \((x_q,F,\chi)\) returns. Every directed transfer has the reverse signed-Port transfer as its occupancy inverse. Hence one bit is sharp. QED.

The deterministic fixed-environment hypothesis matters. External commands, nondeterministic Port choice or evolving external Port guards assign this memory to a different resource; they are different models rather than counterexamples to the theorem. The 12-entry routing lookup is relative to P and the selected STAR, preserving X6 origin freedom.

## Theorem B — a complete-state loop cannot have nonzero state-observable precision holonomy

If the complete observed Markov state is only \((Cell,F,\chi)\) and the triad and chirality are preserved on the twelve signed Port events, the full return is exactly the same state. Thus any single-valued precision readout factoring through this state returns the same value. In particular a genuine before/after \(+6\) or \(-6\) nonzero shift at C12 or C24 is impossible under that *complete-state premise*.

**Proof.** The native cycle closes, the single occupied Cell returns, and F and \(\chi\) are unchanged. Equal full states have equal values under every state function. QED.

This is an observer factorization obstruction. A physical hidden fiber, stateful environment or history-reading observer can supply extra state; none is presently Source-admitted as a physical Port precision law.

## Theorem C — exact additional loop memory and a constructive Link-cochain witness

For \(m\ge 0\), fix \(N=6\cdot2^m\) and *hypothesize* an additional state-observable fine precision address \(z\in C_N\), increasing by \(+6\) after each complete forward loop and decreasing by \(6\) after each reverse loop, with the same law on all repeated loops.

At a fixed base Cell and a fixed chirality, the exact number of distinguishable loop checkpoints required is

\[
\operatorname{ord}_{C_N}(6)=\frac{N}{\gcd(N,6)}=2^m.
\]

Consequently at least \(m\) bits of loop-state memory are required. To also select both distinct deterministic chiralities from the same Cell, at least \(2^{m+1}\) combined states, or \(m+1\) bits, are required. These bounds are sharp **for one fixed initial precision-origin orbit**.

**Necessity.** The readout at full-return number k is \(z_0+6\chi k\pmod N\). The first \(2^m\) values are pairwise distinct, so an observer-preserving hidden state needs at least \(2^m\) checkpoint values per fixed chirality. At each such checkpoint the two possible next Cells are different for opposite chirality, requiring disjoint deterministic routing modes. QED.

**Constructive sufficiency, preserving Unit233's prior hypothetical Link cochain.** Assign signed oriented outer-edge increments

\[
g_5=g_{10}=3,\qquad g_q=0\text{ for all other }q,\qquad H=\sum_{q=0}^{11}g_q=6,
\]

with reverse event increment \(-g_q\). Define \(B(0)=0\), \(B(q)=\sum_{j=0}^{q-1}g_j\) for \(1\le q\le11\), and retain only a counter \(k\in\mathbb Z/2^m\mathbb Z\) alongside the chirality bit. At phase Cell \(x_q\) set the typed readout

\[
\boxed{z(q,k)\equiv B(q)+6k\pmod{6\cdot2^m}.}
\]

On \(q\to q+1\) increment k only when \(q=11\); on \(q\to q-1\) decrement k only when \(q=0\). Otherwise k remains unchanged. Substitution yields *on every primitive event*

\[
z(q+1,k')-z(q,k)\equiv g_q,\qquad
z(q-1,k')-z(q,k)\equiv -g_{q-1}\pmod N.
\]

This is exactly the pre-existing two-edge \(+3,+3\) cochain, including its inverse, realized by a \(2^m\)-state counter. Whole-triad occupancy moves and the register update are atomic. After one forward/reverse loop, z changes by \(+6/-6\); after \(2^m\) full loops it returns. Thus the combined hidden routing/fiber state count at a fixed native Cell is exactly \(2^{m+1}\), establishing sharpness. QED.

The compressed register describes a **fixed initial z-origin orbit**. For arbitrary independently initialized precision values, extra conserved coset information may be required. The resulting conditional model does not establish physical sensing or a P000 dynamical law.

| Readout level | Distinct loop values for one chirality | Both chiralities' sharp hidden states at one Cell | Bits | One forward / reverse lap |
|---|---:|---:|---:|---|
| C6 | 1 | 2 | 1 | 0 / 0 |
| C12 | 2 | 4 | 2 | 6 / 6 |
| C24 | 4 | 8 | 3 | 6 / 18 |
| C48 | 8 | 16 | 4 | 6 / 42 |
| C96 | 16 | 32 | 5 | 6 / 90 |
| C192 | 32 | 64 | 6 | 6 / 186 |

## Executed exact finite checks and physical next discriminator

A standard-library Python checker exhaustively verified the twelve distinct native Cell positions, oriented signed primitive edges, all-source single mobile whole-triad resource guards, clockwise/anticlockwise inverses and full returns; six precision moduli C6–C192 with exact loop periods; all minimal \((q,k,\chi)\) compressed-state edge increments; and inverse signed-edge C24 checks for every q, z and direction.

**Actual executed result: 12,247 exact integer assertions; 0 failures.** Separate exact program and JSON certificate are in research_checks under the corresponding X6_TIME_SIGNED_PORT_CHIRAL_GUARD_AND_C24_FIBER names dated 20261121_1900.

The next decisive Source test is a *real* signed directed Cell/Link/Port update with authenticated three-token conservation, occupancy/resource guards and a same-Cell C12/C24 before/after precision-fiber observation for both directions. Under the current conditional model, a measured C24 \(+6/-6\) would distinguish the hypothesized internal register from a Cell/F/chirality-only state, while the original 2026-11-18 positive-only candidate does not implement the required negative Ports. A conditional construction does not count as a physical measurement or signed-Port admission.

The old R063 six-file Native benchmark is a distinct task RS-X6-LEGACY-PLANE-RECONCILIATION / support #2416, not replaced or executed here. Independent Driver review, Result admission and protected native semantic PROGRESS remain unperformed. Existing claim was previously expired; original terminal rejected writes/typed preparations are not retried. Engineering support [#2903](https://github.com/awdawmip/enterprise-math/issues/2903) remains open as observed in this research run.
