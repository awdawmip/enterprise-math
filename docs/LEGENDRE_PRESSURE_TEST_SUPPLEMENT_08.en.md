# Legendre Pressure Test — Supplement 08

Status: `ACTIVE CONSOLIDATION NOTE`  
Scope: exact identification of the new cofactor-window recursion with the earlier square-basin hit-count / carry machinery  
Depends on: P017 L002–L003 and L020–L036  
Discipline: this supplement introduces no new foundational object. Its purpose is to remove duplicate routes by proving that two recent representations are exactly the same finite counting events.

## 1. Why another consolidation is necessary

The earlier P017 line studies the exact number

\[
H_d(k)
=
\#\{n:k^2<n<(k+1)^2,\ d\mid n\}.
\]

The newer least-factor line studies, for a prime `p<=k`, an exact cofactor window

\[
W_p(k)=[A,B]
\]

such that

\[
L_p(k)=\{pq:q\in W_p(k),\ q\text{ p-rough}\}.
\]

At first these looked like two separate proof languages:

- modular basin hits in the original variable `n`;
- rough cofactor windows in the divided variable `q=n/p`.

They are not separate. The quotient window is exactly the image of the old hit-count problem after factoring out `p`.

---

## 2. L037 — Cofactor-window endpoints are the direct quotient endpoints

Status: `PROVED`.

Let `p<=k` be prime. The L021 centered formulas are

\[
A
=
k+1+r-1+\left\lfloor\frac{(r-1)^2}{p}\right\rfloor,
\qquad
r=k+1-p,
\]

and

\[
B
=
k+1+r+\left\lfloor\frac{r^2-1}{p}\right\rfloor.
\]

They simplify exactly to

\[
\boxed{
A=\left\lfloor\frac{k^2}{p}\right\rfloor+1
}
\]

and

\[
\boxed{
B=\left\lfloor\frac{(k+1)^2-1}{p}\right\rfloor.
}
\]

### Lower endpoint proof

Since

\[
r-1=k-p,
\]

we have

\[
\left\lfloor\frac{(r-1)^2}{p}\right\rfloor
=
\left\lfloor\frac{k^2}{p}\right\rfloor-2k+p.
\]

Also

\[
k+1+r-1=2k+1-p.
\]

Adding gives

\[
A=\left\lfloor\frac{k^2}{p}\right\rfloor+1.
\]

The upper endpoint follows by the identical expansion of

\[
r^2-1=(k+1-p)^2-1.
\]

Thus `W_p(k)` is simply the integer quotient interval obtained by dividing the open square basin by its known factor `p`.

---

## 3. L038 — Raw cofactor-window length is exactly the old square hit count

Status: `PROVED`.

From L037,

\[
|W_p(k)|
=B-A+1
\]

is

\[
\left\lfloor\frac{(k+1)^2-1}{p}\right\rfloor
-
\left\lfloor\frac{k^2}{p}\right\rfloor.
\]

But this is exactly the definition of the number of multiples of `p` strictly between the two squares. Hence

\[
\boxed{|W_p(k)|=H_p(k).}
\]

Therefore the newer window-width identities are not a competing invariant. They are refinements of the same `H_p(k)` seen after quotienting by the known least factor.

In particular the L024 bulk-plus-boundary-carry formula is another coordinate form of the original Euclidean basin descent / square-carry decomposition.

---

## 4. L039 — Every second-factor child count is H_(p ell)(k)

Status: `PROVED`.

Fix any positive integer `ell`. The number of multiples of `ell` inside the cofactor window is

\[
M_\ell
=
\#\{q\in W_p(k):\ell\mid q\}.
\]

Multiplication by the already-extracted factor `p` gives a bijection

\[
q
\longmapsto
n=pq
\]

between those cofactor values and square-basin states divisible by `p ell`.

Therefore

\[
\boxed{
M_\ell=H_{p\ell}(k).
}
\]

This identity is exact for every `ell`; no high-band assumption is needed.

### High-band consequence

If

\[
p^2\ge2k
\]

and `ell>=p`, then

\[
p\ell\ge2k.
\]

The open square basin consists of exactly `2k` consecutive integers, hence has span `2k-1`. A modulus at least `2k` can therefore occur at most once. Thus

\[
\boxed{
H_{p\ell}(k)=M_\ell\in\{0,1\}.
}
\]

So the L034 binary second-factor branch is exactly the large-modulus specialization of the original P017 hit count.

---

## 5. Common-center form of the same binary event

Status: `PROVED`.

Let

\[
d\ge2k
\]

and write the square-basin center

\[
M=k(k+1).
\]

Every basin state has the form

\[
M+s,
\qquad
1-k\le s\le k.
\]

Let

\[
a=M\bmod d,
\qquad
0\le a<d.
\]

Because the basin has fewer than `d+1` states, at most one offset can solve

\[
M+s\equiv0\pmod d.
\]

The negative representative `s=-a` lies in the basin exactly when

\[
a<k.
\]

The positive representative `s=d-a` lies in the basin exactly when

\[
a\ge d-k.
\]

Hence

\[
\boxed{
H_d(k)
=
\mathbf 1[a<k]
+
\mathbf 1[a\ge d-k],
\qquad d\ge2k.
}
\]

The two indicators are disjoint in this range.

When a hit exists, the unique state is explicitly

\[
\boxed{
 n=
 \begin{cases}
 M-a,&a<k,\\
 M+(d-a),&a\ge d-k.
 \end{cases}
}
\]

Taking

\[
d=p\ell
\]

recovers exactly the L034 candidate state obtained from the cofactor-window residue step.

Thus three descriptions are identical:

\[
\boxed{
\text{cofactor residue hit}
=
\text{quotient-response carry bit}
=
\text{large-modulus square-basin hit }H_{p\ell}(k).
}
\]

---

## 6. Consequence of the audit

Several structures introduced during the research can now be collapsed.

### Do not maintain these as separate P017 routes

- raw cofactor-window branch bits;
- old `H_d(k)` large-modulus hit indicators;
- quotient-response carry events for the same modulus.

They are coordinate presentations of the same finite event.

### Keep the representation that helps the current proof step

- use `H_d(k)` for global basin identities and modular descent;
- use cofactor windows for positive least-factor / Buchstab recursion;
- use response/carry language only for transport/coherence identities.

This is the intended role of the P018 audit: new notation survives only when it changes what can be proved, not when it merely renames an existing count.

## 7. New narrowed target

After this identification, the high-band three-prime problem becomes:

1. choose a second prime `ell>=p`;
2. test the single old hit bit
   \[
   H_{p\ell}(k)\in\{0,1\};
   \]
3. if it is `1`, divide the unique hit by `p ell`;
4. test whether the resulting tail is a prime at least `ell`.

The only project-specific question still open is whether the family of common-center residues

\[
k(k+1)\bmod(p\ell)
\]

for varying `ell` has correlations strong enough to beat generic short-interval sieve bounds.

If no such correlation can be proved, the route should stop there.
