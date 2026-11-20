# X6 Unit185 — one-bit-per-transition exact streaming update of terminal relative-depth rank

**Date:** 2026-11-20. **Parent objective:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Published Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Research lane:** `chatgpt-research-onhour-enterprise-math-20260923`; the separate CONTROL_PLANE_MAINTENANCE lane is excluded. **Status:** AUTHOR_PROVED / EXACT_INTEGER_FINITE_EXECUTED / SOURCE_VERIFIED / UNREVIEWED / NOT_ADMITTED. This is an author scientific note, not Native PROGRESS, review, Result or P000 promotion.

**Frozen science:** `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, with `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`) and `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md` (blob `aa005cd62c45d7f4105632257db9186b115c5b29`). Original historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, especially `src/enterprise_math/weighted_relation_field.py` (blob `e50bf991e4dc4280063556a7aad1028f9f9404ed`) and its actual consumer test `tests/test_weighted_relation_field.py` (blob `51748dfe340c385907c4f2218fa1ae5ae2260522`). Already-known mathematics: Unit182 endpoint-fiber summation, Unit183 ordered-trace lift, and Unit184 exact terminal fiber size and optimal bit bound. These are consumed, not re-originated.

## Exact problem

The native coordinate graph has state `z∈Z^6`, initial point `0`, and twelve primitive signed moves `v∈{±e_1,…,±e_6}`. At exact horizon `M∈N_0`, observe only `a=q(z)=z−min_i(z_i)·1` and retain a rank `j` within the set of all **possible** full native terminal lifts. Unit184 proved the nonempty interval

\[
H_M(a)=\{h∈\mathbb Z:\sum_i|a_i+h|\le M\}\quad
(M\equiv\sum_i a_i\pmod 2).
\]

Let `H_M(a)=[\ell_M(a),u_M(a)]∩Z`, and let `j=h−\ell_M(a)`. When an identified next signed primitive direction `v` occurs, can we update the rank without reconstructing the entire historical path or storing an unbounded new label per transition? The exact statement below concerns anchored terminal endpoint recovery and the declared signed-coordinate event; full decorated Path-formal and arbitrary state-dependent weights remain separately typed.

## Theorem 1 — sharp local interval expansion

Set

\[
b=q(a+v),\quad c=\min_i(a_i+v_i)\in\{-1,0,1\},
\quad H_{M+1}(b)=[\ell',u']\cap\mathbb Z.
\]

For **every** reachable `(M,a)` and **every** signed primitive direction `v`, the following two differences are in `{0,1}`:

\[
\boxed{
\epsilon_L=\ell_M(a)+c-\ell'\in\{0,1\},
\qquad
\epsilon_R=u'-u_M(a)-c\in\{0,1\}.
}
\]

Equivalently,

\[
\boxed{
H_{M+1}(b)=[\ell_M(a)+c-\epsilon_L,\;
u_M(a)+c+\epsilon_R]\cap\mathbb Z.
}
\]

Every one of the four possible pairs `(\epsilon_L,\epsilon_R)` occurs.

**Proof.** Every native depth `h∈H_M(a)` is reached by some length-`M` word. Appending the specified primitive signed move `v` gives final state

\[
a+h\mathbf1+v=b+(h+c)\mathbf1.
\]

Thus `H_M(a)+c⊆H_{M+1}(b)`. The parity congruence is inherited because `v` is one primitive step. Since both nonempty fibers are integer intervals, `\epsilon_L,\epsilon_R≥0`.

Put `d_a(h)=\sum_i|a_i+h|`, an integer convex function. Because six is even, `d_a(h)≡\sum_i a_i≡M\pmod2` for *all* `h`. At `\ell=\ell_M(a)`, we have `d_a(\ell)≤M`, whereas `\ell−1\notin H_M(a)` gives `d_a(\ell−1)≥M+2`. By discrete convexity, its successive backward differences are nondecreasing as we move left, so

\[
d_a(\ell−2)-d_a(\ell−1)\ge
d_a(\ell−1)-d_a(\ell)\ge2;
\quad d_a(\ell−2)\ge M+4.
\]

Any hypothetical next lift at `\ell+c−2` corresponds before the primitive move to `h=\ell−2`. The \(\ell_1\) triangle inequality gives

\[
d_a(\ell−2)\le d_b(\ell+c−2)+1\le(M+1)+1=M+2,
\]

contradiction. Hence `\epsilon_L≤1`. The same argument from `u+1,u+2` proves `\epsilon_R≤1`. □

**Sharpness witnesses:** Independent enumeration supplies explicit reachable witnesses for each pattern. In particular `M=5`, `a=(2,1,0,1,3,0)`, `v=−e_5` has `H_5(a)={−1}`, `c=0`, `H_6(q(a−e_5))={−2,−1,0}`; hence `(\epsilon_L,\epsilon_R)=(1,1)`. Cases `(0,1)` and `(1,0)` already occur at `M=2`; `(0,0)` at `M=0`.

## Theorem 2 — exact streaming rank and sourced six-unit-capacity consumer

The native depth after the actual specified move is `h'=h+c`. Thus, with old rank `j=h−\ell_M(a)` and new rank `j'=h'−\ell_{M+1}(b)`,

\[
\boxed{j'=j+\epsilon_L.}
\]

The rank update is therefore **an addition of either 0 or 1** at every primitive step; no other depth data need be preserved for the declared terminal coordinate observer. At time `M`, its worst-case storage remains sharply bounded by the Unit184 value

\[
\boxed{b(M)=\left\lceil\log_2(\lfloor M/3\rfloor+1)\right\rceil}.
\]

This is an information-storage theorem, not an O(1)-runtime implementation or a bit-complexity speedup claim: computing the interval bound and \(\epsilon_L\) has a separately accountable cost.

The true frozen A3 producer `weighted_relation_field` with **unit capacities on six named indices** yields `Z_{ij}=z_i-z_j`. Under a signed primitive move `v`,

\[
\boxed{Z'_{ij}=Z_{ij}+v_i-v_j},\qquad
\boxed{b_i=\max_j Z'_{ij}}.
\]

These update rules depend only on the observed relation field and the specified direction, not on the hidden common depth. The existing production consumer `recover_totals_from_weighted_field` takes `(m,Z,C)` and recovers the original integer totals. The **new adapter** constructs

\[
h'=\ell_{M+1}(b)+j',\qquad C'=\sum_i b_i+6h',
\]

then passes `m=(1,…,1)`, `Z'`, and `C'` to that actual consumer, recovering the exact native terminal `z'`. The source has a real consumer test; the X6 streaming adapter presented here is mathematically derived and independently tested, **not** asserted to be an already deployed production integration.

**Exact BRC scope.** The full length-`M` endpoint count remains `N_M(z)` from frozen V17. The rank restores the native terminal endpoint, so the original exact BRC count for that endpoint is recoverable from `M,b,j'`; the rank does not recover all individual path decorations, a lost ordered history, or state-dependent weights violating Unit183's diagonal-invariance condition. No native R063 benchmark is repeated.

## Independent exact-integer execution

The independently written Python checker enumerates all reachable signed six-axis terminal relative states for `M=0,…,9` and all twelve marked primitive outgoing directions. It directly enumerates both the old and new native depth intervals, verifies the two epsilon margins, cardinality change and rank update for every old depth.

| Evidence | Exact result |
|---|---:|
| Relative-state / marked-step transitions | 677,820 |
| Source-depth rank-update checks | 1,192,620 |
| `(\epsilon_L,\epsilon_R)=(0,0)` | 382,272 |
| `(0,1)` | 131,604 |
| `(1,0)` | 131,604 |
| `(1,1)` | 32,340 |
| Violations | **0** |

The checker was actually executed in Python normal, `-O` and `-OO` modes, returning identical JSON bytes with SHA256 `c9bc678b7faf0732cfa31dbafa3a6bc472b8f61caf1b7770652c173371476a9b`. It raises runtime exceptions on mismatches, not removable `assert` statements. Universal claims use the preceding proof, not a finite-window extrapolation.

**Remaining parent-task obligations:** real frozen 28-LP producer/consumer audit and repairs, especially unresolved LP011/LP019 offending `commit:path:line`; old Native semantic historical Units149–152 and author Units175 onward need present same-lane owner/CLAIM/RUN verification; formal independent review remains `UNREVIEWED/NOT_ADMITTED`. Keep previously completed R063 native 17/17 and 512/512 tests as already-consumed evidence; do not rerun or substitute the portable mathematical checker. Current original owner is not inferred from mere recovery metadata.

**Next scientific discriminator:** implement the exact finite-horizon interval endpoint algorithm on a true source-backed consumer and quantify its full bit operations and time cost. For state-dependent transition weights, test Unit183's diagonal invariance before declaring quotient-only weighted execution safe.
