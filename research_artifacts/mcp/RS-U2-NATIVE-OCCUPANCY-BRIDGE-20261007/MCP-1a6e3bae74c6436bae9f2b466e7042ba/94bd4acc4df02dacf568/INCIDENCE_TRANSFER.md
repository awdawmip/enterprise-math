# U2 incidence transfer: the row-mass condition for a degree-only return

Status: **CONDITIONAL_CIRCUIT_DERIVATION / EXECUTED_TYPED_BRC / NATIVE_ADMISSION_UNKNOWN**.

Task: `RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007`, publication `TP2-E49C20B8D0A6569355F6`.
Authorized execution: Researcher `EM-DIRECT-FA0C27`, activity `RA-283C0A8BF9F924806C568F05`.
This bounded contribution is by a temporary collaborator of the same execution. It is not an independent review, a new CLAIM, or a new researcher identity.

## 1. Exact scope and retained state

Assume the locked P000 and full native X6 Cell substrate. Let signed ports be
`P={0,...,11}`, with `2j=+E_(j+1)`, `2j+1=-E_(j+1)`, and opposite port
`bar(p)=p xor 1`. The six-entry coordinates below are raw displacements from a
chosen Cell anchor, **not final public Cell addresses**. All six native axes remain
present; there is no native plane or lower-dimensional replacement world.

This note studies the fixed-position, positive response circuit of the frozen U2
source. The initial occupied Cells are `c` and `c+E_1`; they are prepared inputs,
not an occupancy solution. A step index is primitive-edge **relation depth**. It
is not physical time or a heartbeat count. A physical occupancy successor and its
separately typed time/order relation remain UNKNOWN.

At each occupied Cell `a`, for every incoming port `p`, choose a finite nonempty
family `H_p^(a)` of distinct three-port subsets. Every member contains `p` and
uses three distinct native axes. Choice among these triples is uniform, and each
packet has three equal legs. No packet gate, storage delay, nonuniform source
preparation, or extra constitutive operation is introduced here. A globally
consistent undirected hypergraph is sufficient but not needed for the formulas.

These are **circuit-syntax assumptions**. They do not establish that any listed
signed triple satisfies native `TRIADIC_CLOSURE_E`, that fractional response is an
indivisible action, or that alternative paths are simultaneous primitive forces.
Three emitted one-edge legs are not a closed triangle of X6 displacements.

Retain material/source identity, signed initial and current input ports, packet
membership, ordered outgoing ports, target Cells, relation depth and positive CWM
state. The executable retains every depth-two leaf with its full packet/path
history. Summing mass below is a declared observer of that retained carrier; it
does not delete joint information or replace signed amplitudes by positive mass.

## 2. What arbitrary anchored incidence preserves

For a unit input at `p`, the outgoing response matrix is

\[
 K_a(q,p)=\frac{\#\{h\in H_p^{(a)}:q\in h\}}{3|H_p^{(a)}|}.
\]

Each triple contributes three legs of weight `1/(3|H_p^(a)|)`. Hence, for every
input `p`,

\[
 K_a(q,p)\ge0,\qquad \sum_qK_a(q,p)=1,\qquad
 K_a(p,p)=\frac13,\qquad K_a(\bar p,p)=0.
\]

The last two identities use anchoring and distinct axes. They are statements
about total response, not conservation of branch counts. Exactly `2/3` of each
pure input changes axis, and a fixed linear positive mixture has exactly `2T/3`
source-tagged changed-axis response. This reuses the prior U2 interface theorem;
it is not a new proof of native force balance. Input-adaptive kernels, unaccounted
sources and missing/empty anchor families are outside this statement.

Define the row mass `r_a(q)=sum_p K_a(q,p)`. Column conservation implies only
`sum_q r_a(q)=12`. **It does not imply `r_a(q)=1` separately.** This is the missing
condition when transporting the default kernel's isotropic-emission calculation
to a newly restricted incidence.

## 3. Correct first emission and two-edge return

Use `0<lambda<1/12` and `rho=12 lambda`. Each labeled material source injects total
one, divided equally among its twelve input channels. An occupied Cell scatters
by `rho K_a`; an empty Cell has twelve outgoing edges of weight `lambda`. A leg
traveling out along `q` arrives at the adjacent Cell with incoming port `bar(q)`.

Consequently, the first outgoing response from source `a` along `q` is

\[
 E_a^{(1)}(q)=\sum_p\frac1{12}\rho K_a(q,p)=\lambda r_a(q).
\]

A two-edge own return must take the exact reverse signed edge on its second
step. If the neighbor is empty, its return factor is `lambda`. If it is occupied
by material `b`, its incoming and returning outgoing port are both `bar(q)`, so
the factor is `rho K_b(bar(q),bar(q))=rho/3=4 lambda`. This remains true when
materials use different anchored families; the first row mass is the **source
material's**, and only the neighbor's diagonal is needed for this return.

For `N_a={q:c_a+d(q) is occupied}`, the exact coefficient is therefore

\[
\begin{aligned}
R_a^{(2)}
 &=\lambda^2\sum_{q\notin N_a}r_a(q)
   +4\lambda^2\sum_{q\in N_a}r_a(q)\\
 &=\boxed{\lambda^2\left[12+3\sum_{q\in N_a}r_a(q)\right]}.
\end{aligned}
\]

There is no omitted-depth error in this exact depth-two coefficient. Cross-source
response is retained separately and is not included in this own-return observer.

The old `R_a^(2)=(12+3d_a)lambda^2`, `d_a=|N_a|`, holds for a **particular fixed
layout** exactly when `sum_(q in N_a) r_a(q)=d_a`. Full row balance is sufficient,
but is not necessary for that one layout: deviations can compensate or lie on
unoccupied directions. If the same fixed kernel must obey the degree-only law
for **every possible one-neighbor placement**, it holds if and only if every
`r_a(q)=1`, by testing each singleton `N_a={q}`.

The stored U2 default of all forty anchored signed triples is row-balanced and
its previously reported degree-only values remain valid. This note limits their
transfer to a new incidence law; it does not invalidate those default checks.

## 4. A globally consistent, manually auditable circuit witness

Take one common hypergraph at both materials, writing signed axis names:

\[
H=\{\{+1,+2,+3\},\{-1,-2,-3\},\{+4,+5,+6\},
       \{-4,-5,-6\},\{+1,+4,+5\}\},
\qquad H_p=\{h\in H:p\in h\}.
\]

Every signed port belongs to at least one triple. All triples use three distinct
axes, and the same global triple is visible from each of its anchors. This
avoids assuming unrelated anchor families. Native signed-triad admission still
has not been supplied.

Ports `+1,+4,+5` have degree two; every other port has degree one. Contributions
to `r(+1)` from input `+1,+2,+3,+4,+5` are respectively
`1/3,1/3,1/3,1/6,1/6`, totaling `4/3`. The negative triple gives
`r(-1)=1/3+1/3+1/3=1`. Thus uniform injection is not uniform emission even under
global incidence consistency.

The exact row masses, ordered `+1,-1,+2,-2,+3,-3,+4,-4,+5,-5,+6,-6`, are

\[
(4/3,1,5/6,1,5/6,1,7/6,1,7/6,1,2/3,1).
\]

For the adjacent pair, source A has occupied direction `+1`, while source B has
occupied direction `-1`. Both have one occupied neighbor, but

\[
 R_A^{(2)}=16\lambda^2,\qquad R_B^{(2)}=15\lambda^2.
\]

At the declared check value `lambda=1/48`, actual BRC returns are respectively
`1/144` and `5/768`. This is a counterexample to an **unqualified extension** of
the degree-only formula to all anchored/global hypergraphs. It is not a native
physical counterexample, a uniqueness theorem, or evidence that the preparation
can arise without external control.

## 5. The l1 tail does not require row balance

On the countable state space `(source, Cell, incoming)`, divide each transport
coefficient by `rho`. At empty Cells the twelve coefficients are `1/12`; at each
occupied Cell they form one column of its `K_a`. Thus every column sums to one,
including for material-dependent fixed families. The resulting positive
operator `P` has `||P||_(1->1)=1`. For finite total injected response `N`,

\[
\Phi=\sum_{n\ge0}(\rho P)^nJ,\qquad
\|\Phi-\sum_{n=0}^{L}(\rho P)^nJ\|_1
 \le \frac{N\rho^{L+1}}{1-\rho}.
\]

For nonnegative injection and this conservative circuit, each layer's total is
exactly `N rho^n` and its omitted global mass equals that expression. Contraction
gives the unique l1 solution. Row balance is irrelevant to this proof. The
statement is about the same fixed linear positive circuit; a native reaction,
storage or occupancy update would require its own conservation/closure argument.
Finite CWM path counts do not imply a finite all-depth count or bounded bit cost.

## 6. Executed evidence and resource ledger

Run `python incidence_check.py` in this directory. The check imports the unchanged
frozen `source/packet_router.py` (blob `7465f5aa16cbb8fba61ba4be80f8a6884b879c53`)
and its pinned `source/sources/brc_weighted.py` (blob
`3f205696709e847909958a153f8fe10d3f6b70f0`, SHA256
`4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f`).
Both belong to frozen U2 commit `fe9ce58293ac77b72092512620e8670ca9be2d78`.
The existing loader removes only its two unused relative imports and verifies
that every function/class AST is unchanged. No scientific kernel was rewritten.

Reuse resolution is `T0_BRC: REUSE_EXECUTED / COMPOSE_APPLIED`: `packets` performs
actual positive serial partition by `1/|H_p|`, then `1/3`; the actual CWM edge,
propagation and recoalescence functions handle every path contribution and mass
readout. The one-state recurrent CWM implementation supplies the tail comparison.
Rational literals specify input shares and expected symbolic certificate values;
there is no parallel ordinary-fraction field solver. No pi, classical trigonometry,
matrix exponential or numerical reference propagator was run.

Actual result: **97 assertions passed**. Calls: `cwm_edge=60`,
`cwm_propagate=1221`, `cwm_recoalesce=1776`, `one_state_recurrent_cwm=1`.
Five global triples produce fifteen anchored basis packet classes. The labeled
layers contain `24,90,1008` records at depths `0,1,2`; material emissions create
`30,12` joint packets at the two transitions. Maximum observed total-response
numerator/denominator bit lengths are `5/14`; maximum CWM-count bit length is `10`.
These bounds describe this finite check, not asymptotic complexity. The JSON is
424,947 bytes in the recorded run, including all depth-two source/port/packet
histories, kernel columns, row readouts and source-separated returns. Wall time
was about `0.020 s`; no remote scientific computation was used.

The own-return CWMs are `(45,1/144,1/1728)` and `(48,5/768,1/3456)`, retaining
different branch counts and dominant weights. The global tail after depth two is
`1/24` for `N=2,rho=1/4`; it is an omitted positive response bound, not a structural
or physical residual. The source pins and exact call/resource counts are saved
in the compact `incidence_check.json`.

The complete original 424,947-byte JSON is retained **byte for byte** in
`incidence_trace.json.gz.b64`, using gzip level 9 with `mtime=0` followed by
standard base64 and a final LF. Its uncompressed SHA256 is
`741b47960228e7d997458abbe6622ee1f88fbd36a9f061aba7ad92fa136639fe`.
The gzip is 14,801 bytes and the base64 file is 19,737 bytes, requiring two 16 KB
transport parts. The compact summary records all three encoding hashes/sizes
and a verified lossless roundtrip. Every one of the `24,90,1008` labeled records
is retained. This is a storage encoding, not a mathematical quotient.

The same single command `python incidence_check.py` now emits the compact summary
and the compressed full trace. Optionally use
`python incidence_check.py --full-evidence /chosen/path/full.json` to retain a
second, uncompressed copy. A fresh run records its own measured wall time and
therefore its own full-byte hash; exact mathematical data and call counts are
checked independently of wall time. The published compressed artifact preserves
the original run above, not a silently regenerated substitute.

New information is the incidence-sensitive return formula, its exact quantifier,
and the global-H witness. Column conservation, the `2/3` interface, and positive
tail reasoning are preserved/reused, not counted as rediscoveries. The smallest
unresolved native issue is still the sourced admission of signed triads together
with a reaction/storage-to-occupancy relation. This result supplies neither.

Researcher-ID: EM-DIRECT-FA0C27 / RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007
