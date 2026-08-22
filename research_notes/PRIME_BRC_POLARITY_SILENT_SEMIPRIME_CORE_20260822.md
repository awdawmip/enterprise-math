# Prime-BRC Polarity-Silent Semiprime Core

Status: `OWNER-LOCAL L3 RESEARCH NOTE / PROVED ELEMENTARY THEOREMS + EXECUTABLE REPLAY / NOT LEGENDRE`
Date: `2026-08-22`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Setup

Let

\[
L=k^2,\qquad M=k(k+1),\qquad U=(k+1)^2.
\]

For an integer divisor coordinate `d>=2`, define the Prime-BRC signed midpoint defect

\[
\chi_d(k)
=2\left\lfloor\frac Md\right\rfloor
-\left\lfloor\frac Ld\right\rfloor
-\left\lfloor\frac Ud\right\rfloor
\in\{-1,0,+1\}.
\]

For an interior integer `n`, define its proper-divisor polarity signature

\[
\Pi_k(n)
=\{(d,\chi_d(k)):1<d<n,\ d\mid n,\ \chi_d(k)\ne0\}.
\]

Call a composite state **polarity-silent** if

\[
\Pi_k(n)=\varnothing.
\]

A prime also has empty proper-divisor polarity signature.  Thus a polarity-only runtime encoding is not prime-complete; e.g. at `k=8`, composite `65=5*13` and prime `67` both have empty proper-divisor polarity signatures.  This is a concrete R023-style no-resurrection boundary, not a proof obstruction for richer encodings.

The question here is: how large can the silent composite ambiguity actually be?

---

## 2. Theorem S1 — silence forces the least factor above k/2

Assume

- `k>=2`;
- `1<=r<k`;
- `gcd(r,M)=1`;
- `n=M-r` or `n=M+r` is composite and polarity-silent.

Let

\[
p=\operatorname{spf}(n),\qquad q=n/p.
\]

Then

\[
\boxed{p>k/2.}
\]

### Proof

Every composite state in the strict square basin has `p<=k`.

Suppose instead `p<=k/2`.  Since `n>k^2`,

\[
q=\frac np>\frac{k^2}{k/2}=2k.
\]

The strict square basin contains exactly `2k` integer states.  Consecutive multiples of `q` are separated by more than `2k`, hence the basin contains at most one multiple of `q`.  It contains `n`, so it contains exactly one.

Equivalently, the left/right half counts of `q`-multiples differ by one, hence

\[
\chi_q(k)=\pm1.
\]

But `q` is a proper divisor of `n`, contradicting polarity silence.  Therefore `p>k/2`. ∎

This is already a strong localization: the polarity-only ambiguity cannot hide in the ordinary small-factor part of the sieve.

---

## 3. Theorem S2 — for k>=10 every silent composite is a semiprime

Assume the hypotheses of S1 and `k>=10`.  Then

\[
\boxed{n=pq}
\]

with distinct primes satisfying

\[
\boxed{k/2<p\le k<q<\frac{2(k+1)^2}{k}.}
\]

In particular, the ambiguity core is `P_2`, not an arbitrary-depth Buchstab branch.

### Proof

By S1, `p>k/2`.  If `Omega(n)>=3`, then

\[
n\ge p^3>\left(\frac k2\right)^3.
\]

For `k>=10`,

\[
\frac{k^3}{8}>(k+1)^2=U.
\]

The inequality holds at `k=10` (`125>121`) and its left-minus-right difference is increasing thereafter.  Hence `p^3>U`, contradicting `n<U`.

Thus `Omega(n)=2`.  Since `n` is composite, `n=pq` for primes `p<=q`.  Equality `p=q` is impossible because then `n=p^2<=k^2=L`.  Hence `p<q`.

Also

\[
q=n/p>k^2/p\ge k,
\]

with strict `q>k` because `n>k^2`, while

\[
q<U/p<\frac{(k+1)^2}{k/2}=\frac{2(k+1)^2}{k}.
\]

Anchor survival implies neither factor divides `M`, so both are transverse. ∎

Small pre-threshold silent composites can have deeper factorization, e.g. `k=5`, `27=3^3`; this is why the theorem keeps the explicit `k>=10` threshold.

---

## 4. Theorem S3 — one silent semiprime at most per fixed p

Let `k>=10`, and let `p` be a prime with

\[
k/2<p\le k,
\]

transverse to `M`.  Then among all anchor-surviving polarity-silent semiprimes in the strict square basin whose least prime factor is `p`, there is at most one.

Therefore

\[
\boxed{
\#\{\text{anchor-surviving silent composite endpoints}\}
\le \pi(k)-\pi(k/2).
}
\]

### Proof

Write

\[
k=p+t,\qquad 1\le t\le p-2,
\]

and

\[
t(t+1)=hp+s,\qquad 0<s<p.
\]

Let

\[
Q=\left\lfloor\frac Mp\right\rfloor
=p+2t+1+h.
\]

For a transverse prime, the two directional centered carry bits are

\[
b_-=\mathbf 1[s<t],\qquad
b_+=\mathbf 1[s\ge p-t].
\]

The signed midpoint defect is

\[
\chi_p=b_--b_+.
\]

A polarity-silent semiprime requires `chi_p=0`, so `b_-=b_+`.  Since `p>k/2`, one has `floor(k/p)=1`; the exact number of strict basin multiples of `p` is

\[
2+b_-+b_+.
\]

Hence only two cases exist.

### Case 1: two p-hits

Here

\[
b_-=b_+=0.
\]

There is exactly one `p`-multiple on each side of `M`, with consecutive cofactor values

\[
Q,\quad Q+1.
\]

Both cofactors exceed `k>=10`, so any prime cofactor is odd.  Two consecutive integers cannot both be odd primes.  Thus at most one silent semiprime exists in this shell.

### Case 2: four p-hits

Here

\[
b_-=b_+=1,
\]

so

\[
p-t\le s<t.
\]

The four cofactor candidates are

\[
Q-1,\ Q,\ Q+1,\ Q+2,
\]

with `Q-1,Q` on the lower side and `Q+1,Q+2` on the upper side.

Since all candidate prime cofactors exceed `k>=10`, only one parity pair can possibly be prime:

- `Q,Q+2`, or
- `Q-1,Q+1`.

It remains to show that in either pair, both cannot be polarity-silent.

#### Subcase 2A: Q and Q+2

The lower state with cofactor `Q` is

\[
pQ=M-s.
\]

Since `Q>k`, the condition `chi_Q=0` would require the next `Q`-multiple `(p+1)Q` to lie by the upper endpoint:

\[
(p+1)Q\le U.
\]

Using `pQ=M-s` and `U-M=k+1`, this implies

\[
Q\le k+s+1.
\]

Substituting `Q=p+2t+1+h` and `k=p+t` gives

\[
t+h\le s.
\]

But `s<t`, contradiction.  Thus the lower `Q` candidate is not silent.

#### Subcase 2B: Q-1 and Q+1

The upper state with cofactor `Q+1` is

\[
p(Q+1)=M+(p-s).
\]

Since `Q+1>k`, the condition `chi_{Q+1}=0` requires its previous multiple `(p-1)(Q+1)` to lie strictly above `L`:

\[
(p-1)(Q+1)>L.
\]

Using `M-L=k`, this gives

\[
Q<k+p-s-1.
\]

Substituting `Q=p+2t+1+h` and `k=p+t` yields

\[
t+h+s+2<p.
\]

But `s>=p-t`, so the left side is at least `p+h+2`, contradiction.  Thus the upper `Q+1` candidate is not silent.

Therefore the four-hit shell also contains at most one silent semiprime.  This proves the fixed-`p` capacity bound.  Summing over possible least primes `p in (k/2,k]` gives the stated global bound. ∎

---

## 5. BRC interpretation

The theorem is deliberately weaker than prime existence but sharper than the earlier raw no-resurrection witness.

A runtime encoding retaining only nonzero `chi` polarity cannot distinguish every prime from every composite.  However, the lost information is not spread arbitrarily through the square basin:

\[
\boxed{
\text{polarity-only ambiguity}
\Longrightarrow
\text{high least-factor semiprime core}
\Longrightarrow
\text{at most one silent state per }p>k/2.
}
\]

This supplies an exact **ambiguity budget**:

\[
\boxed{
A_{\rm silent}(k)\le \pi(k)-\pi(k/2).
}
\]

It does not yet control non-silent composite endpoints.  Hence it does not prove Legendre, Oppermann, or a prime lower bound.

The next useful question is now narrower:

> can the non-silent endpoint mass be bounded by signed midpoint-polarity / mirror-crossing constraints strongly enough that, after adding the silent ambiguity budget, total composite capacity is strictly smaller than the available mirror endpoint capacity?

If this reduces to the existing mirror incidence / sieve cover without a new signed bound, it should be demoted rather than renamed.

---

## 6. Executable replay

Owner-local implementation:

- `src/enterprise_math/prime_brc_silent_core.py`;
- `tests/test_prime_brc_silent_core.py`.

The code provides:

- proper-divisor polarity signatures;
- silent-core classification;
- fixed-`p` two-hit/four-hit certificate;
- dense finite capacity replay.

Finite replay is falsification evidence only; the theorems above are the elementary integer arguments.
