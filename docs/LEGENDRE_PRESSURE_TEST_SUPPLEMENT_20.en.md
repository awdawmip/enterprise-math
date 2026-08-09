# Legendre Pressure Test — Supplement 20

Status: `PROVED RESEARCH NOTE`  
Scope: complete classification of lower-band actual-root collisions and the minimal shell-repair alphabet  
Depends on: P017 L054–L055, P023-S8 image separation, P023-S9 task-refinement repair calculus  
Discipline: this supplement proves square-basin lower-band shell structure. It does not claim a proof of Legendre's conjecture.

## 1. Continue past the eventual no-collision theorem

L055 proves that for `k>=9` the actual root images of distinct lower-band least-prime shells are pairwise disjoint. It also records a bounded audit where the only smaller realized collisions occur at `k=5,6,8`, all for `p=2,r=3`.

A closer reading of the ordinary proof shows that the exclusion of every `r>=5` never uses `k>=9`, and the exclusion of `s>=8` for `(2,3)` also never uses it. The `k>=9` hypothesis enters only when the final finite range is reduced to `9,10,11`.

Thus L055 already contains almost all of a stronger complete collision-classification theorem.

## 2. Notation

Let

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right]
\]

and

\[
G_p(k)=\{R_2(q):q\in W_p(k)\}.
\]

The lower-band condition is `p^2<2k`. A tuple `(k,p,r,s)` with `p<r` and `s in G_p(k) cap G_r(k)` is a realized lower-band cross-shell root collision.

## 3. L056 — Complete classification of all lower-band actual-root collisions

Status: `PROVED`.

For every positive integer `k` and distinct lower-band primes `p<r`,

\[
G_p(k)\cap G_r(k)\ne\varnothing
\]

if and only if

\[
\boxed{
(k,p,r,s)
=
(5,2,3,3),
(6,2,3,4),
(8,2,3,5).
}
\]

The entire lower-band actual-root collision set therefore contains exactly three points.

### 3.1 Every `r>=5` is impossible

Sections 5–8 of L055 show that a common root with `r>=5` would imply

\[
k^2<p\,s(s+2),
\qquad
rs^2\le k^2+2k,
\qquad
k^2<r(s+1)^2,
\]

and hence

\[
2s^2<(3r-3)s+r+1.
\]

Then `r>=11` contradicts the lower-band condition, `r=7` forces `k<=22` while lower-band requires `k>=25`, and `r=5` forces `k<=11` while lower-band requires `k>=13`. None of those arguments uses `k>=9`.

Thus every realized collision must satisfy

\[
\boxed{r=3,\quad p=2.}
\]

### 3.2 A `(2,3)` collision forces `s<=7`

For `(p,r)=(2,3)`, L055 derives

\[
k^2<2s(s+2),
\tag{I}
\]

\[
3s^2\le k^2+2k.
\tag{J}
\]

Section 9.1 uses only these inequalities and integer square comparisons to prove `s<=7`. Therefore `k^2<126`, so `k<=11`. Since prime 3 is lower-band only when `9<2k`, one also has `k>=5`.

Only `k=5,6,7,8,9,10,11` remain.

### 3.3 Seven exact finite cases

The exact quotient-window formula gives:

- `k=5`: `W_2=[13,17]`, `G_2={3,4}`; `W_3=[9,11]`, `G_3={3}`; collision root 3;
- `k=6`: `W_2=[19,24]`, `G_2={4}`; `W_3=[13,16]`, `G_3={3,4}`; collision root 4;
- `k=7`: `G_2={5}`, `G_3={4}`; no collision;
- `k=8`: `W_2=[33,40]`, `G_2={5,6}`; `W_3=[22,26]`, `G_3={4,5}`; collision root 5;
- `k=9`: `G_2={6,7}`, `G_3={5}`; no collision;
- `k=10`: `G_2={7}`, `G_3={5,6}`; no collision;
- `k=11`: `G_2={7,8}`, `G_3={6}`; no collision.

Exactly the three listed collisions remain. ∎

## 4. L055 is strengthened rather than replaced

The sharp eventual threshold `k>=9` remains correct, but L056 says more:

\[
\boxed{\text{all realized lower-band cross-shell root collisions in the family occur only three times}.}
\]

Moreover, `r>=5` never participates in an actual lower-band root collision. All real conflict is concentrated in the smallest prime pair `(2,3)` and three small square basins.

## 5. From classification to minimal repair

L056 gives the local shell split multiplicity of the unrepaired root coordinate. At `k=5,6,8`, one root fiber contains both shell labels `p=2,p=3`, so the maximum multiplicity is 2. At every other `k>=4`, each root fiber contains at most one lower-band shell label, so the maximum multiplicity is 1.

P023-S9-T03 therefore determines the exact minimum repair alphabet when the target retains both root and least-prime shell identity.

## 6. L057 — Minimal lower-band root-shell repair alphabet

Status: `PROVED`.

For every `k>=4`, let `E_root` retain only the actual root index and let `E_root+shell` retain root plus least-prime shell label. Then

\[
\boxed{
R_{\min}(k)=
R(E_{\rm root}\to E_{\rm root+shell})
=
\begin{cases}
2,&k\in\{5,6,8\},\\
1,&k\ge4,\ k\notin\{5,6,8\}.
\end{cases}}
\]

This is exactly the maximum local split multiplicity from L056, by P023-S9-T03. ∎

## 7. One uniform canonical repair bit

Define

\[
\boxed{
\beta_k(q)=
\mathbf 1\left[q>\left\lfloor\frac{k(k+2)}3\right\rfloor\right].
}
\]

### L057-A — On actual lower-band states, `beta_k` is exactly the `p=2` indicator

Let `q in W_p(k)` and `k>=4`.

If `p>=3`, then

\[
q\le\left\lfloor\frac{k(k+2)}p\right\rfloor
\le\left\lfloor\frac{k(k+2)}3\right\rfloor,
\]

so `beta_k(q)=0`.

If `p=2`, then

\[
q\ge\left\lfloor\frac{k^2}{2}\right\rfloor+1.
\]

For `k>=4`,

\[
\frac{k(k+2)}3\le\frac{k^2}{2},
\]

because this is equivalent to `2(k+2)<=3k`. Hence

\[
\left\lfloor\frac{k(k+2)}3\right\rfloor
\le\left\lfloor\frac{k^2}{2}\right\rfloor<q,
\]

so `beta_k(q)=1`.

Therefore

\[
\boxed{\beta_k(q)=1\iff p=2}
\]

on every actual lower-band shell state. ∎

## 8. L057-B — The repaired root recovers the shell from k=4 onward

Define

\[
\boxed{\widetilde R_k(q)=(R_2(q),\beta_k(q)).}
\]

For every `k>=4`, realized repaired images of distinct lower-band prime shells are pairwise disjoint.

By L056, any collision of the root coordinate alone must be between `p=2` and `p=3`. By L057-A, all `p=2` states have bit 1 while all `p>=3` states have bit 0, so every possible collision is split by the second coordinate. ∎

P023-S8-T02 then gives a unique shell decoder on the reachable repaired image.

## 9. Why the bit is minimal

At `k=5,6,8` the collision root fiber genuinely contains two shell labels. A one-value repair cannot distinguish them. The two values `{0,1}` of `beta_k` attain the lower bound from P023-S9-T03, so one bit is the exact minimum local state space for this task.

## 10. Four precision thresholds are now rigorously separated

- exact cofactor precision, L054: `k>=4`;
- root plus minimal repair, L057: `k>=4`;
- actual root alone, L055/L056: sharp eventual threshold `k>=9`, with only three small collisions in the entire family;
- enlarged candidate-pair precision, L052: uniform separation threshold `k>=15`.

Thus

\[
\boxed{
\begin{array}{c}
\text{exact cofactor: }4\\
\text{root + minimal repair: }4\\
\text{actual root alone: }9\\
\text{candidate superset: }15.
\end{array}}
\]

Coarser over-approximation can manufacture extra resource competition, while minimal repair restores only detail that the declared task can actually read again.

## 11. Feedback into the number-theoretic route

L056/L057 replace generic lower-band collision counting by

\[
\boxed{\text{actual root channel}+\text{a two-valued repair needed only in three small basins}.}
\]

From `k>=9` the repair is always trivial. Even when the uniform formula is kept from `k>=4`, it is only the `p=2` indicator.

Later P017 recursion should therefore not pay a uniform multiplicity-two cost for lower-band cross-shell competition. The remaining complexity is pushed into within-shell root many-to-one merging, exact p-rough cofactor capacity, the high-band large-prime tail, and further task-relative compression of mirror/CRT state.

## 12. Executable specification

- `src/enterprise_math/p017_root_shell_repair.py`
- `tests/test_p017_root_shell_repair.py`

Regression pins the three small collision witnesses, agreement of `beta_k` with the `p=2` shell indicator, repaired-image separation from `k=4` over a large finite range, and the exact minimum repair-alphabet profile. Large finite checks are regression only; they do not replace the ordinary proofs of L056/L057.
