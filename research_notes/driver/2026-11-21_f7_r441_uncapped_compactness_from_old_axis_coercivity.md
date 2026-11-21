# CBRC F7 Driver r441 — Axis coercivity removes the uniform-cap hypothesis in finite-to-infinite minimax

Date: 2026-11-21 (+08:00). A new auxiliary mathematical theorem and independent axis-identity check by the existing Driver line `EM-DVR-DEBB5E`. It extends the previously saved r440 bounded-class compactness theorem; it does not alter the original F7 researcher's `EM-CBRCF7-83A1D4` authorship, the frozen Result `RR-AA38973D56330E59D315`, or the status of its native Review. This two-coordinate scalar representation is an auxiliary F7 model, not a replacement for P000 native six-dimensional geometry.

## Model and statement

Use the exact F7 mixed involution on `z=(n,m,p,l) in Z^4`:

```text
A = [ 2 -2 -1  2
      1 -1 -1  2
     -1  2  2 -2
     -1  2  1 -1 ] .
```

Let `Q` be the unrestricted scalar class of functions `q:Z^2 -> R_{≥0}` with
`q(0,0)=0`, `q(n,m)=q(-n,m)`, `q(t,0)=1` for every nonzero integer `t`, `q(x,y)>=1/2` on every nonzero pair, and the exact marks `q(2,1)=q(-1,-1)=1/2`. No upper bound on `q` is assumed. Define

```text
D_q(z) = q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(n,m)-q(p,l)
M_B(q) = max_{z in [-B,B]^4 intersect Z^4} |D_q(z)|
E_B = inf_{q in Q} M_B(q)
E_infty = inf_{q in Q} sup_{z in Z^4} |D_q(z)| .
```

**Theorem A (uniform global coercivity of finite-defect scalars).** For every `q in Q` with global defect `sup_z |D_q(z)| <= epsilon < infinity`,

```text
1/2 <= q(u,v) <= 3/2 + epsilon       for every v != 0,
q(u,0) = 1 for u != 0,  q(0,0)=0 .
```

The bound is independent of `u,v`; the theorem applies to the *original unrestricted function class*.

**Theorem B (unrestricted compactness and exact limit).** For every integer `B>=1`,

```text
E_infty = sup_{B>=1} E_B = lim_{B->infty} E_B,
```

and the infinite-domain infimum **is attained** by an admissible `q_*`. In addition, because the already constructed global r435 candidate has defect `4/7`, a minimizer can be chosen with

```text
0 <= q_*(u,v) <= 3/2 + 4/7 = 29/14
```

on all integer pairs, while satisfying all fixed scalar conditions. Equivalently, imposing the cap `q<=29/14` leaves the original *global* optimum unchanged.

**Finite feasibility-to-global equivalence (unrestricted).** For every finite `epsilon>=0`, there exists `q in Q` with `|D_q(z)|<=epsilon` for every `z in Z^4` if and only if, for every integer `B>=1`, there is a (not necessarily compatible) `q_B in Q` with `M_B(q_B)<=epsilon`.

## Proof: exact old-axis witness

For arbitrary integers `u,v`, choose

```text
z(u,v)=(u-v, 0, u-2v, 0).
A z(u,v)=(u, v, u-3v, -v).
```

This equality is an exact integer matrix identity. It yields

```text
D_q(z(u,v))
 = q(u,v)+q(u-3v,-v)-q(u-v,0)-q(u-2v,0).
```

When `v != 0`, the second output pair has a nonzero second coordinate and therefore `q(u-3v,-v)>=1/2`. Each of the two input old-axis values is either 0 (origin) or 1 (nonzero axis), so their sum is at most 2. From `D_q(z(u,v))<=epsilon`,

```text
q(u,v) <= 2+epsilon-q(u-3v,-v) <= 3/2+epsilon.
```

The corresponding lower bound is one of the model's original hypotheses. This proves Theorem A.

For Theorem B, let `L=sup_{B>=1}E_B`. The values `E_B` are nondecreasing, and `L<=4/7` by the already available global r435 candidate. For each `B`, select `q_B in Q` with `M_B(q_B)<=E_B+1/B` (the infimum definition suffices; r438 separately proves finite rational attainment).

Fix any scalar coordinate `(u,v)` with `v != 0`. For every sufficiently large `B >= max(|u-v|,|u-2v|)`, the old-axis witness `z(u,v)` belongs to the finite cube. The same calculation now gives the eventual, coordinatewise bound

```text
1/2 <= q_B(u,v) <= 3/2 + E_B + 1/B <= 29/14 + 1/B.
```

The old axis and origin have fixed bounded values. Because `Z^2` is countable, diagonal subsequence extraction produces a sequence `B_j->infty` along which every `q_{B_j}(u,v)` converges to a real value `q_*(u,v)`. The original parity, nonnegativity, positive lower bound, axis values and marked equations are all closed coordinate conditions, so `q_* in Q`, and `q_*(u,v)<=29/14` for all coordinates.

For any fixed `z in Z^4`, eventually `z in [-B_j,B_j]^4`. The defect `D_q(z)` involves only four scalar values and is continuous under coordinatewise convergence. Thus `|D_{q_*}(z)|<=L` for every `z`, so `E_infty<=L`. The reverse inequality follows directly from `M_B(q)<=sup_z |D_q(z)|` for every `q,B`. Consequently `E_infty=L`, and `q_*` attains the infimum.

For fixed `epsilon`, repeat the diagonal argument using finite `epsilon`-feasible tables (with no `1/B` slack), yielding `q_*<=3/2+epsilon` and a global `epsilon`-feasible scalar. The converse is immediate.

## Exact verification and implications

The identity `A(u-v,0,u-2v,0)=(u,v,u-3v,-v)` was independently checked with integer arithmetic over all 81 pairs `u,v in [-4,4]`, in addition to the symbolic row expansion above. The proof is algebraic for **all** integers, not inferred from the finite check.

The r440 theorem for the subclass `q<=1` remains valid. This r441 theorem removes its explicitly open upper-cap hypothesis for the original unrestricted F7 scalar minimax, at the cost of the rigorously obtained cap `29/14` for a global minimizer. It does **not** show the optimal value equals `1/2`. The established quantitative frontier remains

```text
1/2 <= E_infty = sup_B E_B <= 4/7.
```

Next discriminating question: obtain a single finite exact dual obstruction `E_B>1/2`, or a construction/certificate establishing `E_B=1/2` for all `B`; the latter would now imply a genuinely global admissible `q` with defect `1/2`, without any extra cap assumption. Source/Activity association, review acceptance, Task closure and mother-objective closure remain separate native questions.

### Provenance

- Original frozen F7 researcher: `EM-CBRCF7-83A1D4`, Result `RR-AA38973D56330E59D315`.
- Earlier auxiliary proof: `research_notes/driver/2026-11-21_f7_r440_bounded_scalar_finite_infinite_compactness.md`, immutable commit `87201c78fd892269cc2443d7ed8c4b188b901fc6`.
- Matrix, finite LP and exact model: `research_notes/driver/2026-11-21_f7_r438_exact_sparse_epigraph_lp_and_b12_exploration.md`, immutable commit `5260880f50468bd6aa9ef232e28b49dcd36504bb`.
- Global `4/7` candidate: existing Driver r435 source, `80bc36253e1e4b5210dc665206a6f2bff746157c`.
- New theorem: auxiliary Driver continuation; mathematical proof and Source publication are not native review, accepted Result or authorized task completion.
