# R255 — Constructive optimal rank/unrank for BRC provenance fibers

**2026-10-24 · author-side finite-carrier theorem and exact computation · UNREVIEWED / NOT ADMITTED / NATIVE_HEARTBEAT_BRIDGE_PENDING**

## Frozen sources and semantics

Account-global source: awdawmip/chatgpt-global-knowledge main at e209497cea450b0ef02e3844215db1497479c53f. Original P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches P000_STARTUP; status ACTIVE_LOCKED. Enterprise Math Source read at c6ba00a05c04ef0bbf1fae4a2ec4a4df4aa06ca0. Relevant native interface blobs are brc_transport.py be1debe367263931bd5e93fd750be3ed54624fe1 and brc_control_port.py 44def6b8ac787e798d3cc2c6be16f873f91b9db8. Predecessor R254, research-note version 76eba4115d1809178705575f40ac00333e24c14e, proved the *existential* worst-fiber tag lower bound and linear shared-path DAG; those are consumed, not claimed anew.

The formal spatial carrier has six native signed displacement axes of the Heartbeat World; time is a distinct ordered composition port. Control labels and the holonomy sign are not extra spatial dimensions. The actions below are six-axis algebraic effects, not proven legally admissible native heartbeat updates or final Cell address transformations.

## Exact positive BRC carrier

Let controls Q={0,1,2}, source-local selector symbols a∈{0,1}, each branch having unit positive weight and multiplicity one. Let the formal affine action

\[
F_{\varepsilon,k}(z)=\operatorname{diag}(\varepsilon,\varepsilon,1,1,1,1)z+k e_1
\quad(\varepsilon=\pm1,\ k\in\mathbb Z).
\]

The confirmed native Affine.then order (first left, then right) is

\[
(\varepsilon,k)\operatorname{then}(\eta,b)=(\eta\varepsilon,\eta k+b).
\]

The entire edge table, as triples (next control, eta, b), is:

| control | selector 0 | selector 1 |
| --- | --- | --- |
| 0 | (2, -1, -1) | (2, +1, -1) |
| 1 | (0, -1, -1) | (0, +1, -1) |
| 2 | (1, +1, +1) | (2, +1, -1) |

An ordered selector history w of length m, starting at s, is observed only as the terminal control and complete affine effect O_m(w)=(q_m,eps_m,k_m). The native EffectHistogram retains joint (weight,action) multiplicity per terminal block but does *not* retain each ordered edge-selector word.

## Theorem A — backward exact completion counts

Fix terminal control t. Define C_l(q;t,sigma,c) to count *all* length-l selector histories beginning at q, ending at t, with complete chronological affine effect (sigma,c). Then

\[
C_0(q;t,\sigma,c)=
\begin{cases}1&q=t,\ \sigma=1,\ c=0\\0&\mathrm{otherwise,}\end{cases}
\]

and if the two outgoing edges from q are (q_a,eta_a,b_a),

\[
\boxed{C_{\ell+1}(q;t,\sigma,c)=
\sum_{a=0}^1 C_\ell(q_a;t,\sigma\eta_a,\ c-\sigma\eta_a b_a).}\tag{R255-1}
\]

Proof: after first edge (eta_a,b_a), a remaining suffix of effect (tau,d) gives total (tau eta_a,tau b_a+d). Equaling (sigma,c) forces tau=sigma eta_a and d=c-sigma eta_a b_a. The first physical selector partitions distinct positive source words into disjoint sets, hence the sum counts exactly their positive multiplicities. Induction from the base establishes the statement for all horizons.

Suppose a prefix u has reached control q_u and composite effect (eps_u,k_u). If target final observation is O=(t,eps*,k*) and total depth m, the *exact number of compatible continuations* is

\[
\boxed{N(u;O)=C_{m-|u|}\big(q_u;t,\ \epsilon_*\epsilon_u,\ 
k_*-(\epsilon_*\epsilon_u)k_u\big).}\tag{R255-2}
\]

Indeed, solving (eps_u,k_u) then (sigma,c)=(eps*,k*) uniquely determines the needed suffix effect. The formula is a true all-depth equality, not inferred from finite tests.

## Theorem B — optimal history tags are constructively encodable and decodable

For a fixed initial state s, depth m and final observation O, let M(O)=N(empty;O). Order the selector words in the fiber O_m^{-1}(O) lexicographically. All compatible words split into the disjoint first-symbol-0 and first-symbol-1 parts. Equation (R255-2) computes the size z of the zero part without listing the words.

**Rank algorithm:** maintain the exact running control/effect; on reading symbol 1, add z to an integer accumulator; then advance the running control/effect with the actual symbol. **Unrank algorithm:** given 0<=r<M(O), choose 0 if r<z; otherwise choose 1 and replace r by r-z; advance and repeat. The exact completion formula applies at every recursive partition. By induction, these greedy algorithms are mutually inverse for every possible word and every admissible rank.

Writing M_m=max_O M(O) for the fixed initial state, the minimum uniform binary tag width that permits exact recovery of an arbitrary individual selector history **given O** is

\[
\boxed{b_m=\left\lceil\log_2 M_m\right\rceil.}\tag{R255-3}
\]

Necessity: M_m different histories in the largest observation fiber need M_m distinct tag values. Sufficiency: use their conditional ranks 0..M(O)-1; identical rank codes can be reused across different observed fibers. The rank decoder achieves this lower bound with a compact exact dynamic program. Nothing here recovers a path that was previously erased *without* a retained tag, source record, or another discriminating observation.

Because |k|<=l at suffix depth l, a fixed-terminal layer contains at most 2|Q|(2l+1) (q,sign,k) states. Precomputation through depth m costs O(|E|m²) exact integer arithmetic additions and O(|Q|m²) stored entries for fixed target; computing for all three t changes only the finite control factor. Cached-prefix rank or unrank takes O(m) table queries and integer operations; big integers have O(m) bits, so these are arithmetic-operation rather than bit-time bounds. Explicit enumeration of 2^m words has exponential output cost.

At depth 3 starting at control 0, the different original words 000 and 101 have the same terminal/full affine observation (0,+1,-1) but receive distinct optimal ranks 0 and 1. This first positive-multiplicity collision establishes that the information distinction is real, not just a counting artifact.

## Independently executed exact checks

R255_rank_unrank.py performed exact direct enumeration plus every-word rank/unrank at each m=0..12 for each of the 3 source controls: 24,573 word checks. R255_independent.cpp independently implemented the count/rank/unrank algorithms, exhaustively checked m=0..10 for all 3 sources: 6,141 word checks. Both used exact integers, and both cross-checked selected optimal fiber ranks at m=3,12,24,40,48,64,96.

| m | distinct words | max observed fiber M_m | min tag bits |
| ---:| ---:| ---:| ---:|
|3|8|2|1|
|12|4,096|250|8|
|24|16,777,216|705,854|20|
|40|1,099,511,627,776|35,345,337,418|36|
|48|281,474,976,710,656|8,233,429,852,978|43|
|64|18,446,744,073,709,551,616|465,428,353,188,420,746|59|
|96|79,228,162,514,264,337,593,543,950,336|1,625,701,140,345,181,560,104,470,766|91|

Rows beyond the directly enumerated horizon are computed by exact positive-multiplicity DP and sampled rank round trips; *not* by enumerating 2^96 histories. Theorem A/B's universal depth validity comes from induction, not finite extrapolation.

## Unresolved native and governance obligations

- The actual R193 path-source observer, its physical edge tokens, time-port and query semantics were not independently located and frozen. Formal local-selector histories are **not** asserted to be R193's physical source records.
- The native enterprise_math Python implementation was source-read but *not actually imported/executed* in a matching environment. Native BRC semantics and six-axis algebraic applicability are distinct from legally admissible heartbeat update dynamics.
- Authenticated GitHub principal was awdawmip. Native task inventory returned CONTROL_QUOTA. Native session-start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No exact active owner or CLAIM, native Result/freeze, independent Driver review or Foundation admission is claimed.
- The optimality statement covers individual word tags conditioned on full terminal/effect observations. It does not assert a universally minimal shared-DAG circuit or minimum tags for an unknown future R193 query language.

## R256 continuation

Identify R193's actual source path-observation contract at a pinned Source revision. If its provenance predicates are regular-language predicates, extend the exact completion DP by a finite-automaton product to retain only query-relevant residuals, then prove the exact observation/future-operation quotient before any erasure. Run the previously written native ControlPacket integration test with a pin-matched original module and verify raw control blocks and actual six-axis effect allowance. Preserve the current formal author proof independently of pending formal CLAIM/review.
