# RH rough threshold complex: exact Betti shell and Morse-count no-go

Status: `RESEARCH FRONTIER / EXACT SHIFTED-COMPLEX FORMULA + ASYMPTOTIC MORSE NO-GO / NOT RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `rough squarefree complex / Björner topology / Betti numbers / discrete Morse / rough Möbius / critical cutoff`

## 0. Prior-art boundary

Anders Björner, *A cell complex in number theory* (Adv. Appl. Math. 46 (2011), arXiv:1101.5704), studies the full complex

`Delta_X={prime-support sets of squarefree n<=X}`,

proves it is shifted and homotopy equivalent to a wedge of spheres, and gives exact Betti-number formulas. In particular the total Betti number of the full complex is asymptotic to `2X/pi^2`.

The present note applies the same shifted-complex theorem to the **prime-cut rough subcomplex** appearing in the current RH/BRC route, derives its exact Betti shell, and uses the critical cutoff `y=(log X)^2` to rule out a hoped-for `sqrt(X)` total-critical-cell discrete-Morse compression.

No historical novelty is claimed for shifted-complex topology itself.

---

## 1. Rough threshold complex

Fix `X>=1` and `y>=2`. Define

`Delta_(X,y)={S subset {p prime:p>y}: prod_(p in S)p <= X}`.

The empty face corresponds to 1. Faces correspond exactly to squarefree y-rough integers.

Let q be the smallest prime strictly larger than y. Order the vertices increasingly, with q first.

If a face contains a prime p and p is replaced by a smaller allowed prime p'>y, then the product decreases. Hence `Delta_(X,y)` is shifted.

Björner's shifted-complex theorem therefore applies verbatim.

---

## 2. Exact Betti shell

For a shifted complex with smallest vertex q, Björner's theorem says that `beta_k` equals the number of faces F of cardinality k+1 such that `F union {q}` is not a face.

A face F not containing q corresponds to a squarefree integer b satisfying

`b<=X`, `P^-(b)>q`, `omega(b)=k+1`.

The condition that adjoining q leaves the complex is exactly

`q b > X`.

Therefore

`beta_k(Delta_(X,y))`
`= #{b: X/q < b <= X, mu(b)^2=1, P^-(b)>q, omega(b)=k+1}`.

Freeze exact interface:

`ROUGH_SHIFTED_BETTI = PRIME-CUT BOUNDARY-SHELL ARITY COUNT`.

Thus all reduced homology is supported on a single multiplicative boundary shell.

---

## 3. Euler characteristic equals the signed Betti shell

Define the rough Möbius sum

`R_y(X)=sum_(n<=X, P^-(n)>y) mu(n)`.

Split according to whether q divides n:

`R_y(X)=R_qplus(X)-R_qplus(X/q)`,

where `R_qplus(U)=sum_(n<=U,P^-(n)>q)mu(n)`.

Equivalently,

`R_y(X)=sum_(X/q < b <= X, P^-(b)>q)mu(b)`.

Using the exact Betti formula and `mu(b)=(-1)^(k+1)` on the k-th Betti shell gives

`R_y(X)=sum_(k>=0)(-1)^(k-1) beta_k(Delta_(X,y))`.

This is exactly the Euler--Poincare relation in arithmetic form.

Hence the topology does not replace rough parity by a smaller object: it rewrites it as the even/odd imbalance among homology spheres in the boundary shell.

Freeze:

`ROUGH_EULER_PARITY = BETTI-DIMENSION PARITY OF THE BOUNDARY SHELL`.

---

## 4. Total Betti count at the critical cutoff

Let

`B(X,y)=sum_k beta_k(Delta_(X,y))`.

By the exact shell formula,

`B(X,y)`
`= #{X/q < b <= X: mu(b)^2=1, P^-(b)>q}`.

Let `Phi(U,q)` be the number of integers `<=U` with no prime factor `<=q`. Buchstab's theorem gives, uniformly in the present range,

`Phi(U,q)=U/log q * [omega(log U/log q)+O(1/log q)]`.

At `q~y=(log X)^2`, both

`log X/log q -> infinity`

and

`log(X/q)/log q -> infinity`.

Since Buchstab's function tends to `e^-gamma`,

`Phi(X,q)~e^-gamma X/log q`,

`Phi(X/q,q)~e^-gamma X/(q log q)`.

The squarefree restriction changes these counts only by

`O(X sum_(p>q)p^-2)`
`=O(X/(q log q))`,

because a non-squarefree q-rough integer is divisible by `p^2` for some p>q.

Therefore

`B(X,y)`
`~ e^-gamma X/log q`.

At the canonical RH cutoff,

`y=(log X)^2`, `q~y`, `log q~2loglog X`,

so

`B(X,y)~ e^-gamma X/(2loglog X)`.

In particular

`B(X,y)=X^(1-o(1)) >> X^(1/2+epsilon)`

for every fixed epsilon<1/2.

---

## 5. Discrete-Morse total-critical-cell route is impossible

For any discrete Morse function on a finite simplicial complex, the number of critical k-cells is at least `beta_k` over any coefficient field. Hence the total number of critical cells is at least the total Betti number.

Therefore every discrete-Morse matching on the critical rough complex satisfies

`#critical cells >= B(X,y)`
`~ e^-gamma X/(2loglog X)`

when `y=(log X)^2`.

So the proposed route

`MORSE MATCHING -> only X^(1/2+o(1)) unmatched/critical rough Cells -> RH`

is structurally impossible.

Freeze no-go:

`ROUGH_THRESHOLD_MORSE_TOTAL_CRITICAL_COUNT_CANNOT_REACH_RH_SCALE`.

This is stronger than a failure of one explicit pivot matching: homology itself supplies the obstruction.

---

## 6. The canonical smallest-prime matching is already homology-scale optimal in count

The standard elementary matching using the smallest rough prime q pairs a face S not containing q with `S union {q}` whenever the latter remains feasible.

The unmatched q-free faces are exactly

`X/q < prod(S) <= X`.

These are precisely the faces counted by the Betti formula above, separated by dimension.

Thus, at the level of total unmatched-cell count, the most obvious q-pivot matching already lands on the intrinsic homology shell. There is no hidden `sqrt(X)` collapse left for a more elaborate Morse matching to discover.

At the critical cutoff q is polylogarithmic, so `X/q` is much smaller than X; consequently the boundary shell contains almost all q-rough faces in the main asymptotic sense. Prime-cutting to the RH critical y therefore makes total-cell topological compression especially weak.

---

## 7. Relation to the positive rough-arity histogram

The current RH criterion uses the positive rough-arity histogram

`N_r(T;y)>=0`

and its final parity observer

`sum_r (-1)^r N_r(T;y)`.

The rough complex identifies the homological boundary counterpart of the same arity coordinate:

`beta_(r-1)(Delta_(T,y))`

counts q-free rough squarefree Cells of arity r in `(T/q,T]`.

Hence topology can move the parity readout from all faces to a boundary homology shell, but the positive shell mass remains `T^(1-o(1))`.

The remaining difficulty is therefore **parity cancellation across homological dimensions**, not lack of a sufficiently aggressive matching.

Freeze observer boundary:

`MORSE_CRITICAL_COUNT != EULER/PARITY CANCELLATION`.

Any future topological route must exploit signed relations between Betti dimensions or a deeper invariant; total Betti/critical-cell compression alone is closed.

---

## 8. Cosine weighting does not evade the obstruction

For `w(x)=cos(pi x/2)` on `[0,1]`,

`w(x)=int_x^1 (pi/2)sin(pi t/2) dt`.

Thus any weighted rough Möbius flow is a positive layer-cake average of unweighted threshold rough Euler characteristics:

`sum_(n<=T,P^-(n)>y)mu(n)w(n/T)`
`=int_0^1 (pi/2)sin(pi t/2) R_y(tT) dt`.

Therefore cosine smoothing averages the same threshold-complex Euler characteristics over scale; it does not turn their large total Betti mass into a small critical-cell count.

This is compatible with the first Brownian/cosine criterion being RH-equivalent.

---

## 9. Current admissible frontier after the Morse audit

The topology lane contributes a precise negative boundary:

- the rough threshold complex is shifted;
- its homology has an exact prime-cut boundary-shell basis count;
- total homology is `~e^-gamma X/log y`;
- at `y=(log X)^2` this is `X/(2e^gamma loglog X)`, far above square-root;
- discrete Morse cannot reduce total critical cells below that scale.

Therefore T11 is useful here as a structural localization tool, not as a direct RH-scale compression mechanism.

The smallest surviving non-topological bottleneck remains the one isolated in

`RH_COMMUTING_PRIME_SHIFT_CRITICAL_OPERATOR_20260908.md`:

the action of the single commuting primitive-prime discrepancy exponential

`exp(-E_(y,N))`

on the specific continuum critical state.

A future topological contribution would have to control the **even/odd Betti imbalance** of the boundary shell itself. But that imbalance is exactly the rough Möbius quantity, so any such theorem must be audited for hidden RH strength.
