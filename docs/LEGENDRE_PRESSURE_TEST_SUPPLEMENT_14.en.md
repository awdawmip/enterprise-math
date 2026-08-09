# Legendre Pressure Test — Supplement 14

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact first- and second-order centered-mirror incidence certificates  
Depends on: P017 L042–L045 and canonical L049  
Discipline: **this note does not prove Legendre's conjecture.** Möbius inclusion-exclusion and the Chinese remainder theorem are classical. The project-specific result is the finite certificate obtained by combining them with the already-proved centered-mirror obstruction.

## 1. From mirror separation to a certificate

Let

\[
M=k(k+1),
\]

and let \(A_k\) be the square-free product of the primes \(a\le k\) dividing \(M\). Recall

\[
S_k=\{1\le r<k:\gcd(r,A_k)=1\}.
\]

For \(r\in S_k\), define

\[
P_-(r)=\operatorname{Supp}_{\mathrm{tr}}(M-r),
\qquad
P_+(r)=\operatorname{Supp}_{\mathrm{tr}}(M+r),
\]

and

\[
a_r=|P_-(r)|,
\qquad
b_r=|P_+(r)|.
\]

L043 proves \(P_-(r)\cap P_+(r)=\varnothing\). If the square basin were prime-free, L044 would force

\[
a_r\ge1,
\qquad
b_r\ge1
\]

for every surviving radius.

This gives two finite obstruction moments:

\[
J_k=\sum_{r\in S_k}(a_r+b_r),
\qquad
E_k=\sum_{r\in S_k}a_rb_r.
\]

Under hypothetical prime-free behavior they must satisfy

\[
J_k\ge2|S_k|,
\qquad
E_k\ge|S_k|.
\]

The purpose of this supplement is to evaluate both moments exactly from small-prime residue data, without factoring or primality-testing the states in the square basin.

---

## 2. Residue-class counter

For \(K\ge0\), \(m\ge1\), and a canonical positive residue \(1\le\rho<m\), define

\[
\mathcal C(K;m,\rho)
=
\#\{1\le r\le K:r\equiv\rho\pmod m\}.
\]

Then

\[
\boxed{
\mathcal C(K;m,\rho)
=
\begin{cases}
0,&\rho>K,\\
1+\left\lfloor\dfrac{K-\rho}{m}\right\rfloor,&\rho\le K.
\end{cases}
}
\]

---

## 3. L050 — Exact first-moment CRT/Möbius formula

Status: `PROVED / CLASSICAL INCLUSION-EXCLUSION SPECIALIZATION`.

Put \(K=k-1\).

### Surviving radii

Möbius inclusion-exclusion on the square-free anchor product gives

\[
\boxed{
|S_k|
=
\sum_{a\mid A_k}
\mu(a)
\left\lfloor\frac{K}{a}\right\rfloor.
}
\]

### Incidence of one transverse prime

Fix a transverse prime

\[
p\le k,
\qquad p\nmid M.
\]

Let \(N_p(k)\) count surviving radii for which \(p\) divides one mirror state. For each square-free divisor \(a\mid A_k\), impose \(a\mid r\) together with

\[
r\equiv M\pmod p
\quad\text{or}\quad
r\equiv-M\pmod p.
\]

Because \(\gcd(a,p)=1\), define

\[
 t^+_{a,p}=(Ma^{-1})\bmod p,
\qquad
 t^-_{a,p}=(-Ma^{-1})\bmod p.
\]

Both lie in \(\{1,\ldots,p-1\}\). The canonical positive representatives modulo \(ap\) are

\[
\rho^+_{a,p}=a t^+_{a,p},
\qquad
\rho^-_{a,p}=a t^-_{a,p}.
\]

Hence

\[
\boxed{
N_p(k)
=
\sum_{a\mid A_k}
\mu(a)
\left[
\mathcal C(K;ap,\rho^+_{a,p})
+
\mathcal C(K;ap,\rho^-_{a,p})
\right].
}
\]

L043 guarantees that the plus and minus channels never describe the same radius for a transverse prime. Therefore

\[
\boxed{
J_k
=
\sum_{\substack{p\le k\\p\nmid M}}N_p(k).
}
\]

### Proof

The formula for \(|S_k|\) is the standard identity

\[
\mathbf 1_{\gcd(r,A_k)=1}
=
\sum_{a\mid\gcd(r,A_k)}\mu(a)
\]

summed over \(1\le r\le K\). The formula for \(N_p(k)\) applies the same identity while imposing one of the two mirror congruences. Writing \(r=at\) gives the displayed residues. Summing over transverse primes is exactly the L045 prime-indexed reindexing. ∎

No state in \((k^2,(k+1)^2)\) is factored in these formulas.

---

## 4. L051 — First-moment prime certificate

Status: `PROVED`.

If

\[
\boxed{J_k<2|S_k|,}
\]

then

\[
\boxed{
\exists q\text{ prime with }k^2<q<(k+1)^2.
}
\]

### Proof

If the basin were prime-free, every surviving mirror pair would be double-composite. L044 would give \(a_r+b_r\ge2\) for every \(r\in S_k\), hence L045 would force \(J_k\ge2|S_k|\), contradiction. ∎

This certificate is sufficient, not necessary. At \(k=31\),

\[
|S_{31}|=15,
\qquad
J_{31}=30,
\]

so the certificate does not fire, although \(967\) is prime and satisfies \(31^2<967<32^2\).

---

## 5. L052 — Exact ordered cross-side prime-pair formula

Status: `PROVED / CLASSICAL CRT SPECIALIZATION`.

The first moment forgets that the small-prime resources must occur on opposite sides of the **same** radius. The first genuinely cross-side moment is

\[
E_k=\sum_{r\in S_k}a_rb_r.
\]

Fix distinct transverse primes \(p,q\le k\). Let \(N_{p\to q}(k)\) count surviving radii satisfying

\[
p\mid M-r,
\qquad
q\mid M+r.
\]

For each square-free \(a\mid A_k\), write \(r=at\) and define

\[
c_p=(Ma^{-1})\bmod p,
\qquad
c_q=(-Ma^{-1})\bmod q.
\]

The unique canonical solution modulo \(pq\) is

\[
\boxed{
 t_{a;p,q}
=
c_p
+p\left((c_q-c_p)p^{-1}\bmod q\right),
}
\]

with \(1\le t_{a;p,q}<pq\). Put

\[
\rho_{a;p,q}=a t_{a;p,q}.
\]

Then

\[
\boxed{
N_{p\to q}(k)
=
\sum_{a\mid A_k}
\mu(a)
\mathcal C(K;apq,\rho_{a;p,q}).
}
\]

Double-counting ordered choices of one lower-side and one upper-side transverse prime gives

\[
\boxed{
E_k
=
\sum_{\substack{p,q\le k\\p,q\nmid M\\p\ne q}}
N_{p\to q}(k).
}
\]

### Proof

The CRT formula is the two-congruence version of L050. Because \(a,p,q\) are pairwise coprime, there is exactly one residue modulo \(apq\). L043 excludes \(p=q\). At a fixed radius, the number of ordered pairs \((p,q)\) with \(p\in P_-(r)\), \(q\in P_+(r)\) is exactly \(a_rb_r\); summing over radii or ordered prime pairs gives the same integer. ∎

---

## 6. L053 — Cross-side product certificate

Status: `PROVED`.

If

\[
\boxed{E_k<|S_k|,}
\]

then the open square basin contains a prime.

### Proof

Under prime-free behavior, every surviving mirror pair is double-composite, so L044 gives \(a_r,b_r\ge1\). Thus \(a_rb_r\ge1\) for every \(r\in S_k\), hence \(E_k\ge|S_k|\), contradiction. ∎

This certificate is independent of L051. For \(k=46\),

\[
|S_{46}|=22,
\qquad
J_{46}=47\ge44,
\]

so L051 fails, while

\[
E_{46}=18<22,
\]

so L053 proves prime existence. Indeed \(2129\) lies in \((46^2,47^2)\).

Conversely, for \(k=37\),

\[
|S_{37}|=17,
\qquad
J_{37}=33<34,
\qquad
E_{37}=18\ge17.
\]

Here L051 fires while L053 does not.

---

## 7. L054 — Two-moment certificate

Status: `PROVED`.

Combining the two independent sufficient conditions:

\[
\boxed{
J_k<2|S_k|
\quad\text{or}\quad
E_k<|S_k|
\Longrightarrow
\exists q\text{ prime with }k^2<q<(k+1)^2.
}
\]

Neither branch dominates the other.

---

## 8. Computational pressure test

Status: `COMPUTATIONAL`, not a theorem.

On the bounded range

\[
3\le k\le1000,
\]

the reference implementation gives:

- L051 first-moment certificate: 273 roots;
- L053 cross-side certificate: 323 roots;
- both: 269 roots;
- L053-only: 54 roots;
- L051-only: 4 roots;
- combined L054 coverage: 327 roots.

Thus the cross-side product moment strictly adds proving power, but the combined first two moments still certify only a minority of roots in this bounded range.

This is a useful negative boundary: the next step should not be an unstructured tower of moments. It should exploit information deliberately forgotten by these two moments, such as same-side joint collisions, exact-support closure, least-factor depth, or correlations between different radii.

---

## 9. Relation to the other P017 cross-state tools

The current layers have distinct roles:

- L041: exact-support closure after one large support hit;
- L042–L045: centered mirror separation and the basic resource obstruction;
- L046–L048: bounded CRT capacity of a whole side-sign pattern;
- canonical L049: high-band resource occupancy by realized hit-state unions;
- L050–L054: exact additive first- and second-order mirror certificates.

L052 is deliberately between the coarse first moment and the full CRT support cell: it fixes one ordered opposite-side prime pair, which retains real cross-state structure while remaining summable over the basin.

---

## 10. Executable validation

`src/enterprise_math/p017_mirror_certificate.py`, `src/enterprise_math/p017_mirror_cross.py`, and their tests check that:

- the L050 formulas for \(|S_k|\), every \(N_p(k)\), and \(J_k\) agree with direct mirror-support counts on bounded domains;
- the L052 ordered-prime-pair CRT formula agrees with direct surviving-radius enumeration;
- summing ordered pair counts equals \(\sum_r a_rb_r\);
- whenever either certificate fires on bounded domains, direct inspection confirms at least one basin prime;
- \(k=31\), \(k=37\), and \(k=46\) lock the stated boundaries;
- the `3<=k<=1000` coverage counts equal 273, 323, 269, 54, 4, and 327 as stated above.

Finite computation audits implementation and coverage statistics; L050–L054 are proved by the exact inclusion-exclusion, CRT, and double-counting arguments above.
