# P017 Mirror Certificate Annex

Status: `ACTIVE RESEARCH ANNEX`  
Scope: exact centered-mirror incidence formulas and aggregate prime certificates  
Depends on: canonical P017 mirror separation (L042–L045)  
Namespace: local labels `MC01–MC06`; this annex deliberately does not consume global `L0xx` numbers.  
Discipline: **this annex does not prove Legendre's conjecture.** Möbius inclusion-exclusion and the Chinese remainder theorem are classical tools; the project-specific content is their finite centered-mirror specialization and the resulting sufficient certificates.

## 1. Mirror data

Let

\[
M=k(k+1),
\qquad
S_k=\{1\le r<k:\gcd(r,A_k)=1\},
\]

where `A_k` is the square-free product of anchor primes `p<=k` dividing `M`. For `r in S_k`, write

\[
P_-(r)=\operatorname{Supp}_{tr}(M-r),
\qquad
P_+(r)=\operatorname{Supp}_{tr}(M+r),
\]

and

\[
a_r=|P_-(r)|,
\qquad b_r=|P_+(r)|.
\]

L043 gives `P_-(r) cap P_+(r)=empty`. Under hypothetical prime-free behavior, L044 forces

\[
a_r\ge1,
\qquad b_r\ge1
\]

for every surviving radius. Define

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

For `K>=0`, `m>=1`, and `1<=rho<m`, use the arithmetic-progression counter

\[
\mathcal C(K;m,\rho)
=
\begin{cases}
0,&\rho>K,\\
1+\left\lfloor\frac{K-\rho}{m}\right\rfloor,&\rho\le K.
\end{cases}
\]

---

## 2. MC01 — Exact first-moment CRT/Möbius formula

Status: `PROVED / CLASSICAL INCLUSION-EXCLUSION SPECIALIZATION`.

Put `K=k-1`. Möbius inclusion-exclusion gives

\[
\boxed{|S_k|=\sum_{a\mid A_k}\mu(a)\left\lfloor\frac K a\right\rfloor.}
\]

Fix a transverse prime `p<=k`. For each square-free `a|A_k`, define

\[
t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
t^-_{a,p}=(-Ma^{-1})\bmod p,
\]

and `rho^+_{a,p}=a t^+_{a,p}`, `rho^-_{a,p}=a t^-_{a,p}`. Then

\[
\boxed{
N_p(k)=\sum_{a\mid A_k}\mu(a)
\bigl[\mathcal C(K;ap,\rho^+_{a,p})+
\mathcal C(K;ap,\rho^-_{a,p})\bigr].}
\]

The two mirror channels are disjoint by L043, hence

\[
\boxed{J_k=\sum_{p\le k,\ p\nmid M}N_p(k).}
\]

**Proof.** Use the standard Möbius indicator for `gcd(r,A_k)=1` and impose one mirror congruence. Writing `r=at` gives the displayed residue classes. Summing over transverse primes gives the prime-indexed mirror-incidence count. ∎

No state inside the square basin is factored by this formula.

---

## 3. MC02 — Exact ordered cross-side formula

Status: `PROVED / CLASSICAL CRT SPECIALIZATION`.

Fix distinct transverse primes `p,q<=k`. Let `N_{p->q}(k)` count surviving radii satisfying

\[
p\mid M-r,
\qquad q\mid M+r.
\]

For every square-free `a|A_k`, write `r=at` and put

\[
c_p=(Ma^{-1})\bmod p,
\qquad
c_q=(-Ma^{-1})\bmod q.
\]

The unique canonical solution modulo `pq` is

\[
\boxed{t_{a;p,q}=c_p+p\bigl((c_q-c_p)p^{-1}\bmod q\bigr),}
\]

with `1<=t_{a;p,q}<pq`. Set `rho_{a;p,q}=a t_{a;p,q}`. Then

\[
\boxed{
N_{p\to q}(k)=
\sum_{a\mid A_k}\mu(a)\mathcal C(K;apq,\rho_{a;p,q}).}
\]

At a fixed radius there are exactly `a_r b_r` ordered choices `(p,q)` with `p in P_-(r)` and `q in P_+(r)`. Therefore

\[
\boxed{E_k=\sum_{p\ne q,\ p,q\le k,\ p,q\nmid M}N_{p\to q}(k).}
\]

This is ordinary CRT plus double counting; L043 removes the diagonal `p=q`. ∎

---

## 4. MC03 — Primitive prime-free slacks

Status: `PROVED`.

Define

\[
\boxed{U_k=J_k-2|S_k|,}
\qquad
\boxed{V_k=E_k-J_k+|S_k|.}
\]

If the square basin is prime-free, then

\[
\boxed{U_k\ge0,\qquad V_k\ge0.}
\]

**Proof.** Put `x_r=a_r-1` and `y_r=b_r-1`. Under prime-free behavior, `x_r,y_r>=0`, and

\[
U_k=\sum_r(x_r+y_r),
\qquad
V_k=\sum_r x_ry_r.
\]

Both are sums of nonnegative integers. ∎

Also

\[
\boxed{E_k-|S_k|=U_k+V_k.}
\]

---

## 5. MC04 — Two-slack prime certificate

Status: `PROVED`.

If

\[
\boxed{U_k<0\quad\text{or}\quad V_k<0,}
\]

then there exists a prime `q` with

\[
k^2<q<(k+1)^2.
\]

This is the contrapositive of MC03.

The channels are independent. For `k=37`,

\[
|S|=17,\ J=33,\ E=18,\quad U=-1,\ V=2,
\]

while for `k=46`,

\[
|S|=22,\ J=47,\ E=18,\quad U=3,\ V=-7.
\]

The latter basin contains the prime `2129`.

---

## 6. MC05 — Aggregate quadratic envelope

Status: `PROVED`.

Under prime-free behavior,

\[
\boxed{4V_k\le U_k^2.}
\]

**Proof.** With the nonnegative `x_r,y_r` from MC03,

\[
4x_ry_r\le(x_r+y_r)^2.
\]

Therefore

\[
4V_k\le\sum_r(x_r+y_r)^2
\le\left(\sum_r(x_r+y_r)\right)^2=U_k^2.
\]

∎

Hence `4V_k>U_k^2` is a third sufficient prime certificate even when `U_k,V_k>=0`.

---

## 7. MC06 — Three-channel certificate and boundary

Status: `PROVED`.

\[
\boxed{
U_k<0\quad\text{or}\quad V_k<0\quad\text{or}\quad4V_k>U_k^2
\Longrightarrow
\exists q\text{ prime with }k^2<q<(k+1)^2.}
\]

At `k=31`,

\[
|S|=15,\ J=30,\ E=15,
\qquad U=V=0,
\]

so none of the three channels fires, although `967` is prime in `(31^2,32^2)`. MC06 is therefore sufficient, not a characterization.

---

## 8. Computational pressure test

Status: `COMPUTATIONAL`, not a theorem.

For `3<=k<=1000`, the reference implementation gives:

- `U_k<0`: 273 roots;
- `V_k<0`: 594;
- both negative: 140;
- negative-slack union: 727;
- additional quadratic-only certificates: 6;
- full MC06 union: **733**;
- weaker raw `E_k<|S_k|`: 323.

The remaining 265 roots satisfy all three aggregate prime-free inequalities. This annex intentionally stops the unstructured moment expansion here.

## 9. Research boundary

The next route should use information discarded by `(U_k,V_k)`: exact-support closure, least-factor depth, or correlations among distinct radii. A particularly promising candidate is **least-factor gating**: use the unique least transverse factor on one mirror side while retaining the full support on the opposite side. This sits strictly between one ordered prime pair and a complete support cell and should be pressure-tested before promotion.

Executable validation is in `src/enterprise_math/p017_mirror_certificate.py`, `src/enterprise_math/p017_mirror_cross.py`, `tests/test_p017_mirror_certificate.py`, and `tests/test_p017_mirror_cross.py`.
