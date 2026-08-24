# P017 — P2/Chen Carry Bridge, Supplement 01

Status: `PROVED_WIP + EXACT FINITE-INTEGER PROOFS + ANALYTIC BOUNDARY / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-24`

Researcher-ID: `EM-PRIMEBRC-7F3A21`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Parent note: `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`

Scope: sharpen the pointwise P2 detector, isolate square-power loss by exact integer bounds, and expose the shallow super-root switching geometry of the binary P017 remainder.

---

## 1. P2-R06 — Sharp half-visible plus half-square detector

Let

\[
I_K=\{K^2+1,\ldots,K^2+2K\},
\qquad W=K+1.
\]

For `n in I_K`, define the number of distinct visible prime factors

\[
\omega_{<W}(n)
=
\#\{p<W:p\text{ prime},\ p\mid n\},
\]

and the squarefull indicator

\[
\sigma_2(n)
=
\mathbf 1_{\exists p\text{ prime}:p^2\mid n}.
\]

Define

\[
\boxed{
\mathfrak w_K(n)
=
1-\frac12\omega_{<W}(n)-\frac12\sigma_2(n).
}
\]

### Theorem

For every `K>=2` and every `n in I_K`,

\[
\boxed{
\mathfrak w_K(n)>0
\iff
\Omega(n)\le2.
}
\]

Equivalently,

\[
\Omega(n)\ge3
\Longrightarrow
\mathfrak w_K(n)\le0.
\]

### Proof

Because `n<W^2`, at most one prime factor of `n` can be at least `W`; such a factor can occur only to the first power.

If `Omega(n)=1`, then `n` is a prime larger than `W`, so `omega_<W(n)=0` and `sigma_2(n)=0`. Thus `mathfrak w_K(n)=1`.

If `Omega(n)=2`, then `n` cannot be a prime square, because no perfect square lies strictly between `K^2` and `W^2`. Hence `n=pq` with distinct primes. The two primes cannot both be `<W`, since then both are at most `K` and `pq<=K^2<n`. They also cannot both be `>=W`, since then `pq>=W^2>n`. Therefore exactly one factor is visible, `sigma_2(n)=0`, and

\[
\mathfrak w_K(n)=\frac12>0.
\]

Now suppose `Omega(n)>=3`.

If `n` is squarefree, at most one of its prime factors is `>=W`, so at least two distinct prime factors are visible. Therefore

\[
\mathfrak w_K(n)
\le
1-\frac12\cdot2
=0.
\]

If `n` is not squarefree, every repeated prime is `<W`, since `p>=W` would imply `p^2>=W^2>n`. Thus `omega_<W(n)>=1` and `sigma_2(n)=1`, giving

\[
\mathfrak w_K(n)
\le
1-\frac12-\frac12
=0.
\]

This proves the equivalence. ∎

### Sharpness of both coefficients

The coefficient `1/2` on visible distinct factors cannot be reduced in a universal detector of this form. At

\[
K=6,
\qquad n=42=2\cdot3\cdot7,
\qquad W=7,
\]

exactly two distinct prime factors are `<W`, and `n` is squarefree. A coefficient `c<1/2` would give `1-2c>0` on an `Omega=3` state.

After fixing the first coefficient at `1/2`, the squarefull coefficient cannot be reduced either. At

\[
K=2,
\qquad n=8=2^3,
\qquad W=3,
\]

there is one visible distinct prime and a square factor. A square penalty `d<1/2` would give `1-1/2-d>0`.

Hence the pair

\[
\boxed{(1/2,1/2)}
\]

is componentwise sharp for this two-observable detector.

---

## 2. P2-R07 — Sieve-compatible square-incidence minorant

Fix `2<=z<W` and restrict to states with no prime factor below `z`. Define

\[
\boxed{
\mathfrak w_{K,z}^{\Sigma}(n)
=
1
-\frac12\sum_{\substack{z\le p<W\\p\mid n}}1
-\frac12\sum_{\substack{z\le p<W\\p^2\mid n}}1.
}
\]

The second sum is at least the single indicator `sigma_2(n)`, while the first sum is exactly `omega_<W(n)` on the `z`-sifted set. Therefore

\[
\mathfrak w_{K,z}^{\Sigma}(n)
\le
\mathfrak w_K(n).
\]

For a prime or semiprime in `I_K`, the state is squarefree and has zero or one visible prime, so the minorant remains positive. Consequently, on the `z`-sifted set,

\[
\boxed{
\mathfrak w_{K,z}^{\Sigma}(n)>0
\iff
\Omega(n)\le2.
}
\]

Let `A=I_K`, let `P(z)` be the product of primes below `z`, and write

\[
S(A_q,P,z)
=
\#\{n\in I_K:q\mid n,\ (n,P(z))=1\}.
\]

Then the total detector weight has the exact sieve decomposition

\[
\boxed{
\begin{aligned}
\mathcal W_{1/2}(K,z)
={}&S(A,P,z)
-\frac12\sum_{z\le p<W}S(A_p,P,z)\\
&-\frac12\sum_{z\le p<W}S(A_{p^2},P,z).
\end{aligned}
}
\]

Thus a positive lower bound for `mathcal W_(1/2)` proves the existence of a P2 in `I_K`.

This detector is simpler than the logarithmic detector in the parent note. The logarithmic detector gives strict negativity on every bad state; the half-square detector needs only nonpositivity, which is sufficient once the aggregate weight is strictly positive.

---

## 3. P2-R08 — General prime-power incidence bound

For an integer `j>=2`, define

\[
Q_j(K,z)
=
\sum_{\substack{z\le p<W\\p\text{ prime}}}H_{p^j}(K).
\]

### Theorem

For every integer `Y>=z`,

\[
\boxed{
Q_j(K,z)
\le
\frac{2K}{(j-1)(z-1)^{j-1}}
+Y
+\frac{W^2}{Y^j}.
}
\]

### Proof

For `z<=p<=Y`,

\[
H_{p^j}(K)
\le
\frac{2K}{p^j}+1.
\]

Therefore

\[
\sum_{z\le p\le Y}H_{p^j}(K)
\le
2K\sum_{n\ge z}\frac1{n^j}+Y
\le
\frac{2K}{(j-1)(z-1)^{j-1}}+Y.
\]

For `p>Y`, write a contributing state as `n=a p^j`. For fixed `a`, the prime `p` lies in

\[
\left(
\left(\frac{K^2}{a}\right)^{1/j},
\left(\frac{W^2}{a}\right)^{1/j}
\right).
\]

Its length is

\[
a^{-1/j}\bigl(W^{2/j}-K^{2/j}\bigr)\le1,
\]

because `0<2/j<=1`. Hence each positive integer `a` contributes at most one integer `p`. Since `p>Y` implies `a<W^2/Y^j`, the high-prime contribution is at most `W^2/Y^j`. Adding the two ranges proves the theorem. ∎

Taking

\[
Y=\max\left(z,\left\lceil W^{2/(j+1)}\right\rceil\right)
\]

gives a root-balanced bound. In particular, whenever `z<=ceil(W^(2/3))`,

\[
\boxed{
Q_2(K,z)
\le
\frac{2K}{z-1}+2W^{2/3}+1.
}
\]

Similarly, for cubes,

\[
Q_3(K,z)
\le
\frac{K}{(z-1)^2}+2W^{1/2}+1.
\]

For every fixed `beta>0`, choosing `z=K^beta` yields

\[
Q_2(K,z)
=
o\!\left(\frac K{\log K}\right).
\]

Therefore the square-incidence term in P2-R07 is not the analytic obstruction. The only difficult part is the first-order distinct-prime sum.

---

## 4. P2-R09 — Ideal main coefficient and the exact threshold suggested by the detector

This subsection is an asymptotic route diagnostic, not a completed sieve theorem.

At the random-divisibility main-term level,

\[
\sum_{z\le p<W}\frac1p
\sim
\log\frac{\log W}{\log z}.
\]

For a power cutoff

\[
z=W^\beta,
\]

the half-visible detector therefore has ideal normalized coefficient

\[
\boxed{
C_{1/2}(\beta)
=1-\frac12\log\frac1\beta.
}
\]

It is positive exactly when

\[
\boxed{\beta>e^{-2}.}
\]

At `beta=1/6`,

\[
C_{1/2}(1/6)
=1-\frac12\log6
\approx0.10412.
\]

This is a larger ideal margin than the root-linear detector from the parent note, whose corresponding coefficient at `beta=1/6` is approximately `0.04157`.

The comparison does not prove that the half detector closes the sieve. It says that the pointwise detector itself is no longer the source of the loss.

---

## 5. P2-R10 — Why the high-prime tail still cannot be discarded trivially

Let the available one-dimensional sieve level be `D approximately K`, and let `z=K^beta` with fixed `beta>0`. After fixing a prime `p`, an ordinary upper sieve on `A_p` retains at least one `z`-scale only while

\[
p\lesssim D/z\approx K^{1-\beta}.
\]

For the remaining band `K^(1-beta)<p<K`, the pointwise bound `S(A_p,P,z)<=H_p(K)` loses the roughness factor `V(z)`. Its harmonic main mass is not small:

\[
\sum_{K^{1-\beta}<p<K}\frac1p
\longrightarrow
\log\frac1{1-\beta}>0.
\]

Thus the constant-half detector would lose a fixed positive multiple of `K`, whereas the target main scale is only `K/log K`.

Even the root-linear weight does not remove this obstruction. Writing `p=K^u`, its unsieved tail mass is proportional to

\[
\int_{1-\beta}^{1}\frac{1-u}{u}\,du
=
-\log(1-\beta)-\beta
>0.
\]

The vanishing endpoint weight reduces the constant but not the order of magnitude.

Therefore the correct analytic conclusion is:

\[
\boxed{
\text{the high-prime tail still needs averaged roughness, switching, or a two-dimensional/bilinear estimate.}
}
\]

The square-power correction is elementary; the parity-breaking high-prime first-order sum remains the true boundary.

---

## 6. P2-R11 — Exact shallow super-root switching

For every `m>=1`, the binary count has the quotient form

\[
\boxed{
O_m(K)
=
\#\left\{
q\text{ odd}:
K^2<mq<(K+1)^2
\right\}.
}
\]

Let `eta>0` and suppose

\[
K<m\le K^{1+\eta}.
\]

Then every contributing odd quotient satisfies

\[
\boxed{
K^{1-\eta}<q\le K.
}
\]

Indeed, the lower inequality follows from `mq>K^2`, while `m>=K+1=W` and `mq<=W^2-1` imply `q<W`, hence `q<=K`.

Now put `m=pd`. For fixed `p` and `q`, the admissible integer `d` lies in

\[
\frac{K^2}{pq}<d\le\frac{K^2+2K}{pq},
\]

an interval of length

\[
\frac{2K}{pq}.
\]

Therefore

\[
\boxed{
pq>2K\Longrightarrow\text{at most one admissible integer }d.}
\]

In particular, if `p>=K^alpha`, `eta<alpha`, and `K^(alpha-eta)>2`, then every shallow super-root incidence has a unique `d` after fixing the prime endpoint `p` and switched odd quotient `q`.

Combined with the previously proved uniqueness of `m=pd` when `p>z` and `d` is supported on primes below `z`, the shallow super-root carry family becomes a partial bipartite matching

\[
(p,q)\longleftrightarrow d,
\]

rather than an unrestricted three-variable divisor cloud.

This is exact structural compression. It does not by itself supply cancellation in the centered discrepancy `O_m-K/m`; that remaining cancellation is precisely the Chen/Iwaniec bilinear frontier identified in the parent note.

---

## 7. Updated frontier

The route has now separated into four layers:

1. **pointwise P2 detection:** closed by the sharp half-visible/half-square detector;
2. **prime-power contamination:** closed asymptotically by the exact `Q_j` bounds;
3. **binary carry identity and switching geometry:** closed exactly by P2-R03 and P2-R11;
4. **high-prime averaged roughness / bilinear cancellation:** still open for an explicit square-specialized theorem.

The earlier idea that the endpoint-vanishing weight alone makes the high-prime tail negligible is false: it suppresses only the coefficient, not the missing roughness factor.

No Legendre theorem and no all-`K` P2 theorem is claimed.