# Legendre Pressure Test — Supplement 20

Status: `PROVED RESEARCH NOTE`  
Scope: complete classification of lower-band exact-window and realized-shell root collisions, plus exact minimal repair  
Depends on: P017 L054–L055, P023-S8 admissibility-filtered image separation, P023-S9 task-refinement repair calculus  
Discipline: this supplement proves square-basin lower-band shell structure. It does not claim a proof of Legendre's conjecture.

## 1. Continue beyond the eventual no-collision theorem

L055 proves a strong envelope statement: from `k>=9`, distinct lower-band **exact-window** root images are pairwise disjoint. Realized least-prime-shell images are subsets, so they inherit the theorem.

The proof can be read more aggressively. Its `r>=5` exclusion does not use `k>=9`, and its `(p,r)=(2,3)` argument excluding `s>=8` does not use it either. Therefore every possible exact-window collision in the entire family is forced into seven finite values of `k`.

The realizability filter then removes one of the three surviving window collisions.

## 2. Notation

For prime `p<=k`, write the raw cofactor window

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}p\right\rfloor
\right]
\]

and its exact-window root image

\[
G_p^{\rm win}(k)=\{R_2(q):q\in W_p(k)\}.
\]

The actual least-prime shell cofactor set is

\[
Q_p^{\rm sh}(k)=
\{n/p:\ k^2<n<(k+1)^2,\ \operatorname{spf}(n)=p\},
\]

with realized root image

\[
G_p^{\rm sh}(k)=\{R_2(q):q\in Q_p^{\rm sh}(k)\}.
\]

Always

\[
G_p^{\rm sh}(k)\subseteq G_p^{\rm win}(k).
\]

## 3. L056-A — Complete classification of exact-window root collisions

Status: `PROVED`.

For distinct lower-band primes `p<r`,

\[
G_p^{\rm win}(k)\cap G_r^{\rm win}(k)\ne\varnothing
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

### Every r>=5 is impossible

L055 derives from a common exact-window root `s` the necessary inequalities

\[
k^2<p\,s(s+2),
\qquad
rs^2\le k^2+2k,
\qquad
k^2<r(s+1)^2.
\]

For `r>=5` these imply

\[
2s^2<(3r-3)s+r+1.
\]

The same L055 argument excludes `r>=11`, then `r=7`, then `r=5`, without using `k>=9`. Hence every exact-window collision must have

\[
(p,r)=(2,3).
\]

### The remaining (2,3) cases are finite

For `(2,3)`, L055 obtains

\[
k^2<2s(s+2),
\qquad
3s^2\le k^2+2k,
\]

and proves `s<=7` without using `k>=9`. Therefore `k<=11`. Since prime 3 is lower-band only for `k>=5`, only

\[
k=5,6,7,8,9,10,11
\]

remain.

Exact windows give:

- `k=5`: `G_2^win={3,4}`, `G_3^win={3}`;
- `k=6`: `G_2^win={4}`, `G_3^win={3,4}`;
- `k=7`: `{5}` versus `{4}`;
- `k=8`: `{5,6}` versus `{4,5}`;
- `k=9`: `{6,7}` versus `{5}`;
- `k=10`: `{7}` versus `{5,6}`;
- `k=11`: `{7,8}` versus `{6}`.

Exactly the three stated window collisions remain. ∎

## 4. L056-B — Complete classification of realized-shell root collisions

Status: `PROVED`.

For distinct lower-band least-prime shells,

\[
G_p^{\rm sh}(k)\cap G_r^{\rm sh}(k)\ne\varnothing
\]

if and only if

\[
\boxed{
(k,p,r,s)
=
(5,2,3,3)
\quad\text{or}\quad
(8,2,3,5).
}
\]

### k=5 and k=8 are realized

At `k=5`,

\[
26=2\cdot13,
\qquad
27=3\cdot9,
\]

lie in `(25,36)`, have least prime factors 2 and 3 respectively, and both cofactors have root 3.

At `k=8`,

\[
66=2\cdot33,
\qquad
75=3\cdot25,
\]

lie in `(64,81)`, have least prime factors 2 and 3, and both cofactors have root 5.

### k=6 is filtered out by admissibility

The only `p=3` cofactor in `W_3(6)=[13,16]` with root 4 is `q=16`. But

\[
3q=48
\]

has least prime factor 2, so `q=16` is not a realized `p=3` shell state. The actual `p=3` cofactors are odd and remain at root 3.

Since every realized shell image is a subset of its exact-window image, L056-A leaves no other possible collision. ∎

## 5. Local split multiplicity of the actual root coordinate

Take the coarse quotient to retain only `R_2(q)` and let the target retain both root and least-prime shell identity.

L056-B gives the exact maximum number of shell labels inside one actual root fiber:

\[
\boxed{
\max_s m_k(s)=
\begin{cases}
2,&k\in\{5,8\},\\
1,&k\ge4,\ k\notin\{5,8\}.
\end{cases}}
\]

The `k=6` window overlap contributes nothing because the conflicting state is inadmissible.

## 6. L057 — Exact minimum root-shell repair alphabet

Status: `PROVED`.

By P023-S9-T03, the minimum alphabet of any repair coordinate that upgrades actual root to `(root,shell)` is exactly the maximum local split multiplicity. Therefore

\[
\boxed{
R_{\min}(k)=
\begin{cases}
2,&k\in\{5,8\},\\
1,&k\ge4,\ k\notin\{5,8\}.
\end{cases}}
\]

So an extra binary state is genuinely necessary only in two square basins in the entire lower-band family. ∎

## 7. A uniform informative p=2 feature

Define

\[
\boxed{
\beta_k(q)=
\mathbf 1\!\left[
q>\left\lfloor\frac{k(k+2)}3\right\rfloor
\right].
}
\]

For every actual lower-band state with `k>=4`, this bit equals the indicator that the least prime is 2.

### For p>=3

If `q` belongs to a realized `p>=3` shell, then certainly `q in W_p(k)`, so

\[
q\le
\left\lfloor\frac{k(k+2)}p\right\rfloor
\le
\left\lfloor\frac{k(k+2)}3\right\rfloor.
\]

Hence `beta_k(q)=0`.

### For p=2

Every `q in W_2(k)` satisfies

\[
q\ge\left\lfloor\frac{k^2}{2}\right\rfloor+1.
\]

For `k>=4`,

\[
\frac{k(k+2)}3\le\frac{k^2}{2},
\]

so

\[
q>\left\lfloor\frac{k(k+2)}3\right\rfloor.
\]

Thus `beta_k(q)=1`. Therefore

\[
\boxed{\beta_k(q)=1\iff \operatorname{spf}(n)=2}
\]

on the actual lower-band states. ∎

## 8. Informative feature is not the same as necessary repair

The uniform bit `beta_k` distinguishes the `p=2` shell even when the root coordinate already distinguishes every shell.

At `k=6`, for example, both bit values occur on actual states, so `beta_6` is informative. But L056-B says there is no actual cross-shell root collision, hence

\[
R_{\min}(6)=1.
\]

A constant repair is sufficient.

Therefore

\[
\boxed{
\text{informative feature}
\neq
\text{task-necessary repair}.
}
\]

Necessary precision is measured by the split of the **current coarse fibers under the target task**, not by how much unrelated information a feature can reveal.

## 9. L057-C — A canonical minimum repair coordinate

Define the task-minimal repair

\[
\boxed{
\rho_k(q)=
\begin{cases}
\beta_k(q),&k\in\{5,8\},\\
0,&\text{otherwise}.
\end{cases}}
\]

For every `k>=4`, the state

\[
\boxed{
\widetilde R_k(q)=(R_2(q),\rho_k(q))
}
\]

recovers the lower-band least-prime shell label.

At `k=5,8`, the two repair symbols separate the only actual conflicting shell fibers. At every other `k`, root alone already separates actual shells and `rho_k` uses the unique one-symbol alphabet. Hence `rho_k` attains the lower bound of L057 for every `k>=4`. ∎

The uniform `beta_k` remains a convenient sufficient decoder feature, but it is intentionally not called minimal where no repair is needed.

## 10. Precision hierarchy after the correction

The lower-band route now has five distinct levels:

1. exact cofactor `q`: shell identity is recoverable from `k>=4`;
2. actual root plus task-minimal repair `rho_k`: shell identity recoverable for every `k>=4`;
3. actual root alone: fails only at `k=5,8`; its sharp eventual threshold is `k>=9`;
4. exact-window root image: has the extra false collision `k=6`, so its small collision set is `5,6,8`;
5. enlarged L052 candidate pairs: uniform disjointness only from `k>=15`.

Thus each relaxation of state semantics can manufacture additional resource competition.

## 11. Feedback into number-theoretic recursion

The actual lower-band cross-shell ambiguity is now completely localized to two finite basins. It should not contribute any asymptotic multiplicity penalty.

For `k>=9`, and in fact for every `k>=4` except `5,8`, root alone identifies the least-prime shell. If a uniform implementation still carries `beta_k`, that is optional information rather than mathematically required precision.

The remaining P017 difficulty is therefore pushed toward within-shell many-to-one root collapse, the `p`-rough cofactor capacity, high-band large-prime structure, and mirror/CRT compression.

## 12. Executable specification

- `src/enterprise_math/p017_root_shell_repair.py`
- `tests/test_p017_root_shell_repair.py`

The executable layer uses actual `first_factor_shell` states rather than all integers in the raw cofactor window. Tests pin the exact realized collision set `{5,8}`, the disappearance of the `k=6` window-only collision, the uniform `p=2` feature, the minimum repair profile, and the adaptive minimum repair coordinate.

Bounded enumeration is regression only; L056-A/L056-B/L057 are ordinary proofs above.
