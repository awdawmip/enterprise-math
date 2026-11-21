# X6 native time — Unit247: directed-centre Port forces an extra C24 precision coset

Date: 2026-11-22 00:00 Asia/Hong_Kong. Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Task `RS-X6-NATIVE-TIME-DYNAMICS`, publication `TP2-91D4A7C2F63805BE21A3`, parent `PO-X6-UPPER-STRUCTURE-20260906`. Author-side Research provenance: `chatgpt-research-onhour-enterprise-math-20260923`; historical researcher `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`. No current live winning CLAIM is asserted.

## Exact existing scientific inputs and question

Reuse frozen P000 X6 six signed native axes and relative chosen Cell pivot `P` at `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; the proven OUTER C12 native Cell microtrace; Unit241's *hypothetical, not physically admitted* additive precision link increments `g_5=g_10=3`, others 0, signed inverses, total one-ring holonomy `H=6`; Units245–246's immutable 36 one-ingress/one-egress shortest guarded whole-triad BRC witnesses. Viète's static principal `±3` root addresses are a different precision operator and are **not** assumed to be dynamically measured.

Question: after admitting a *candidate* pair of directed center Port transfers `x_i→P→x_j`, each with precision increment 0, can Unit241's fixed-origin precision register of `2^m` values still implement all allowed chronological local transitions at the same labelled Cell in `C_(6·2^m)`? Does inspecting only completed opposite-winding paths detect the missing intermediate state?

The model retains relative signed Cell source and target, the original labels of complete force triads, serial target-empty guard, and full BRC event order. Single-triad graph reachability below permits both directions on the ring and only the declared one-way center Port pair. The 36 two-triad paths are separately checked with their original guard and identities.

## Theorem A — exact closed-walk precision image

Let `N=6·2^m`, `m≥0`, and write `g_k=3` for `k=5,10`, `g_k=0` otherwise. The ring graph has forward edge `x_k→x_(k+1)` with precision weight `g_k mod N` and inverse weight `−g_k`. Its twelve-step holonomy is `H=Σg_k=6`. Admit directed composite center passage `x_i→P→x_j`, where `i,j∈{0,2,4,6,8,10}` and each center edge has weight zero. Put

\[
 d=(j-i)\bmod 12,\qquad A(i,j)=\sum_{r=0}^{d-1}g_{(i+r)\bmod12}.
\]

For any closed walk of **one labelled intact triad** beginning and ending at the same ring Cell, let `L` count signed original ring edges, `c≥0` completed directed center passages, and `z=(L+dc)/12∈Z` the winding of the path after expanding each center passage to its clockwise `d`-edge ring arc. Then its accumulated additive precision change is

\[
 \boxed{\Delta=6z-A(i,j)c\pmod N.}
\]

Proof: substituting the clockwise ring arc for each passage gives a closed ring-only walk with winding `z` and weight `6z`; the original center passage has weight zero instead of the substituted arc's weight `A`. All signed reverse events retain negative weights. No temporal ordering or BRC labels are discarded in the actual event model; this substitution is solely a proof of the scalar readout.

The full set of reachable *closed-walk precision differences* at the fixed labelled Cell is exactly

\[
 \boxed{G_{i,j}=\langle6,-A(i,j)\rangle\subseteq C_N,
 \quad |G_{i,j}|=\frac{N}{\gcd(N,6,A(i,j))}.}
\]

Necessity follows from the formula. Sufficiency: a forward complete ring gives generator `+6`, and `x_i→P→x_j` followed by `d` **reverse** ring edges `x_j→x_i` is an actual directed closed walk giving `−A`. Concatenations attain nonnegative multiples of both; because `C_N` is finite, those nonnegative multiples generate the same subgroup, including their additive inverses. Ring-cell translation of the basepoint is connected by signed ring paths and does not change closed holonomy. This proves an exact reachability classification for the stated single-triad graph.

## Theorem B — precise fixed-Cell state inflation and a local counterexample

Without center links, `G_ring=<6>` has `2^m` values, the sharp fixed-origin precision memory proved in Unit241. For the six even ingress/egress choices, `A(i,j)` is always 0, 3 or 6, so exactly half of the 36 ordered pairs leave this count unchanged and half **double** it:

\[
 |G_{i,j}|/2^m=\begin{cases}1,&A\equiv0\pmod6,\\2,&A\equiv3\pmod6.\end{cases}
\]

Ordered ingress/egress `0,2,4,6,8,10` yield the exact factor matrix:

| ingress / egress | 0 | 2 | 4 | 6 | 8 | 10 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 2 | 2 | 2 |
| 2 | 1 | 1 | 1 | 2 | 2 | 2 |
| 4 | 1 | 1 | 1 | 2 | 2 | 2 |
| 6 | 2 | 2 | 2 | 1 | 1 | 1 |
| 8 | 2 | 2 | 2 | 1 | 1 | 1 |
| 10 | 2 | 2 | 2 | 1 | 1 | 1 |

For every diameter pair `j=i+6 mod12`, the clockwise arc has precisely one weight-3 edge and hence `A=3`. The **eight native event** single-triad closed walk

\[
 x_i\to P\to x_{i+6}\to x_{i+5}\to\cdots\to x_i
\]

contains two signed center primitive steps and six signed inverse ring primitive steps. It returns to the **same Cell** with precision change `−3 mod24 =21`, whereas any ring-only return changes the precision by a multiple of 6. Repeating this actual candidate graph walk, the eight distinct C24 values `0,21,18,15,12,9,6,3` occur. Four ring-only precision states are therefore insufficient; **eight precision states, or 3 bits, are sharp at a fixed Cell in C24**. More generally the minimum increases from `2^m` to `2^(m+1)`. A construction simply retains the reachable `3·Z_N` precision residue and updates by the declared edge weights. This concerns the fixed-initial-origin precision register; independent initial cosets require additional state.

The center transfer cannot be implemented inside Unit241's fixed `z(x_q,k)=B(q)+6k` fiber with zero center weight when `B(j)-B(i)\equiv3 mod6`; after one passage, the arrival Cell has the wrong mod-6 coset. Thus the added bit is a **local transition-observer obstruction**, not merely an additional global winding counter.

## Theorem C — why complete opposite-winding paths miss this bit

For a diameter pair, closure forces `c` even. With original ring winding `L=12w` and `A=3`, Theorem A becomes

\[
 \Delta=6(w+c/2)-3c=6w\pmod N.
\]

Thus **all** opposite-winding two-triad Unit245 diameter witnesses, including the two 28-event global optima `(i,j)=(6,0),(8,2)`, have the same terminal C24 precision increments for labelled triads A and B:

\[
 \boxed{(\Delta_A,\Delta_B)=(18,6)\in C_{24}^2.}
\]

The six diameter shortest full BRC histories were actually replayed; each preserved signed ring winding `L_A=-12,L_B=+12`, target-empty occupancy, and full labelled event order. A terminal-only observer of the labelled Cells, these ring windings, and C24 precision deltas cannot distinguish the extra center-fiber coset. The eight-event single-triad experiment above distinguishes it using an intermediate closed Port loop. This is a **horizon-specific BRC observer counterexample**: a safe terminal quotient for those paths is not an operation-safe state representation on the extended native event graph.

## Verification / scientific status

A dependency-free JavaScript checker loaded the original immutable Unit245 full 36-case certificate, replayed all 36 chronological labelled A/B traces under the guarded Port law, tested all six exact precision layers `C6,C12,C24,C48,C96,C192`, and independently enumerated every reachable signed graph state `(Cell,z)` by BFS. The exact subgroup sizes, six diameter collision identities, and 18/18 split passed. **Actual in-session V8 exact assertions: 3187; total BFS states visited across checks: 44226; failures: 0.** Node checker is saved for reproduction but execution claimed here is the V8 runtime, not an independently run Node CLI.

This adds an exact discriminating local precision-fibre test; it does not create a Source-admitted signed force/Port law or an actual physical C12/C24 measurement. An admitted center Port, a genuine signed whole-triad event update, environment response and actual independently sensed precision remain the live empirical evidence obligations. It does not rerun the separate R063 native benchmark or promote any static Viète root to a physical clock. Unit246's full event counts and original Source case pins are preserved as prior results. Independent Driver review and Result admission remain pending.
