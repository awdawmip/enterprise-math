# P018 — Finite-Precision Proof Calculus, Supplement 08

Status: `ACTIVE RESEARCH NOTE`  
Scope: centered-prime radius representation of near-diagonal factor proof slack  
Depends on: P018 Stages 7–8  
Discipline: symmetric prime representations of an even center are elementary number theory. This note does not assert that every center admits such a positive-radius representation and does not prove Goldbach-type conjectures.

## 1. Recenter Stage 8 at the upper square root

Stage 8 writes a near-diagonal first-factor shell using

\[
s=\sigma(k),
\qquad
p=k-s,
\qquad
q=p+2(s+1).
\]

Introduce the upper-square center

\[
\boxed{c=k+1}
\]

and the positive radius

\[
\boxed{r=s+1.}
\]

Then

\[
\boxed{
p=c-r,
\qquad
q=c+r.}
\]

Thus the Stage-8 prime pair is exactly symmetric around `c`, and

\[
\boxed{p+q=2c.}
\]

The unique shell state becomes the difference of two squares

\[
\boxed{pq=c^2-r^2.}
\]

This centered coordinate exposes a new interpretation of factor proof slack: `sigma+1` is a candidate symmetric-prime radius around the upper square root.

## 2. Centered prime radius

For an integer center `c>=2`, define the **positive centered prime radius** when it exists by

\[
\boxed{
\rho(c)=
\min\{r\ge1:c-r\text{ and }c+r\text{ are both prime}\}.
}
\]

The radius is required to be positive, so equal-prime representations at radius zero are deliberately excluded.

The set defining `rho(c)` may be empty. P018 makes no universal existence claim.

## 3. P018-T71 — Centered shell theorem

Status: `PROVED`.

Let `c>=3`, `r>=1`, and put

\[
k=c-1,
\qquad
p=c-r.
\]

Assume

\[
\boxed{
p\ge3\text{ is prime},
\qquad p>r^2.}
\]

Then

\[
\boxed{
L_p(k)\ne\varnothing
\iff
c+r\text{ is prime}.}
\]

When nonempty,

\[
\boxed{
L_p(k)=\{(c-r)(c+r)\}
=\{c^2-r^2\}.}
\]

Proof: set `s=r-1`. Then `p=k-s`, and the hypothesis `p>r^2=(s+1)^2` is exactly the Stage-8 T63 hypothesis. T63 gives the equivalence and singleton shell with right prime

\[
p+2(s+1)=c-r+2r=c+r.
\]

The product identity is the ordinary difference-of-squares factorization. ∎

So near the universal factor horizon, first-factor shells are indexed by symmetric prime radii around the upper square root.

## 4. P018-T72 — Minimal centered radius equals factor proof slack plus one

Status: `PROVED`.

Suppose `rho(c)` exists. Write

\[
r=\rho(c),
\qquad
p=c-r.
\]

Assume

\[
\boxed{p\ge3,
\qquad p>r^2.}
\]

Set `k=c-1`. Then

\[
\boxed{
\sigma(k)=r-1.}
\]

### Proof

Because `c-r` and `c+r` are prime, T71 gives a nonempty shell

\[
L_{c-r}(k)\ne\varnothing.
\]

Therefore

\[
H(k)\ge c-r.
\]

Suppose instead that `H(k)>c-r`. Since a nonempty first-factor shell is indexed by a prime, write

\[
H(k)=c-r'
\]

for some integer `r'` with

\[
1\le r'<r.
\]

Because

\[
c-r'>c-r>r^2>(r')^2,
\]

T71 applies at radius `r'`. Nonemptiness of `L_(c-r')(k)` would force both

\[
c-r',\qquad c+r'
\]

to be prime, contradicting the minimality of `r=rho(c)`.

Hence

\[
H(k)=c-r.
\]

Since `k=c-1`,

\[
\sigma(k)=k-H(k)
=(c-1)-(c-r)=r-1.
\]

∎

Thus, in the near-diagonal theorem range, the smallest symmetric prime radius is **exactly one larger than the minimal factor precision slack**.

## 5. P018-T73 — Actual factor slack gives the minimal centered radius

Status: `PROVED`.

Conversely, suppose

\[
\sigma(k)=s,
\qquad
r=s+1,
\qquad
c=k+1,
\qquad
p=c-r=k-s.
\]

Assume

\[
\boxed{p\ge3,
\qquad p>r^2.}
\]

Then

\[
\boxed{
\rho(c)=r=s+1.}
\]

Proof: Stage-8 T66 gives that `p=c-r` and `c+r` are prime, so a centered pair exists at radius `r`.

If a smaller centered prime radius `r'<r` existed, then

\[
c-r'>c-r>r^2>(r')^2.
\]

T71 would give a nonempty shell `L_(c-r')(k)` at an index strictly larger than

\[
c-r=H(k),
\]

contradicting the definition of the factor horizon. ∎

Together T72–T73 give the exact identification

\[
\boxed{
\rho(k+1)=\sigma(k)+1
}
\]

whenever either side lies in the common near-diagonal range

\[
k-\sigma(k)>(\sigma(k)+1)^2,
\]

or equivalently the minimal centered pair has left prime larger than the square of its radius.

## 6. P018-T74 — Fixed-slack first-centered-pair criterion

Status: `PROVED`.

Fix `s>=0`, put

\[
c=k+1,
\qquad
r=s+1,
\qquad
p=c-r=k-s,
\]

and assume `p>=3` is prime with `p>r^2`.

Then

\[
\boxed{
\sigma(k)=s
}
\]

if and only if:

1. `c-r` and `c+r` are both prime;
2. for every integer `1<=t<r`, at least one of `c-t`, `c+t` is composite/nonprime.

Equivalently,

\[
\boxed{
\sigma(k)=s
\iff
\rho(c)=s+1
}
\]

under the stated size hypothesis.

Proof: the forward direction is T73. The reverse direction is T72. ∎

This turns the factor-slack strata into **first centered-prime-radius strata**.

The Stage-8 special cases become immediate:

- `sigma=0` means the first centered prime pair occurs at radius `1` — the twin-prime stratum;
- `sigma=1` means the first centered prime pair occurs at radius `2` — the gap-four stratum.

## 7. P018-T75 — Radius, prime gap, square offset, and parity are one coordinate

Status: `PROVED`.

Under T73, with `r=sigma(k)+1`, the last near-diagonal composite shell has

\[
\boxed{
\begin{aligned}
p&=k+1-r,\\
q&=k+1+r,\\
q-p&=2r,\\
p+q&=2(k+1),\\
pq&=(k+1)^2-r^2.
\end{aligned}}
\]

Because `p,q>=3` are odd primes, `p` and `q` are odd. Therefore the center `k+1` and radius `r` have opposite parity, equivalently

\[
\boxed{r\equiv k\pmod2.}
\]

Since `sigma=r-1`, this is also

\[
\boxed{\sigma(k)\equiv k+1\pmod2.}
\]

whenever the factor horizon lies in this near-diagonal odd-prime range.

Thus one integer `r` simultaneously measures:

- the first symmetric-prime search radius;
- half of the forced prime gap;
- the square-root of the upper-square offset;
- one plus the factor proof slack.

This is a genuine compression of several Stage-8 coordinates into one centered finite-precision coordinate.

## 8. Proof-theoretic interpretation

Stage 7 asked how much factor precision must be accumulated before every survivor is known prime.

Stage 9 gives a geometric interpretation when that precision requirement is close to the universal cutoff:

> the proof has to move inward from the universal factor horizon until it reaches the first symmetric prime pair around `k+1`.

The amount moved inward is `sigma`; the centered radius is `sigma+1`.

This does **not** say that symmetric prime pairs are the mechanism proving a prime exists inside every square basin. The centered pair here describes the location of the **last composite first-factor obstruction**, not the prime survivor itself.

That distinction is essential: the Legendre existence target remains open.

## 9. Boundary against Goldbach-type overclaiming

The identity

\[
(c-r)+(c+r)=2c
\]

is of course a representation of the even integer `2c` as a sum of two primes whenever the centered pair exists.

P018 uses only centered pairs whose existence has already been supplied by Stage-8 factor-shell hypotheses or by an explicitly given prime pair.

It does **not** assert:

- that every `c` has a positive centered prime radius;
- that every even integer has a distinct-prime centered representation;
- any form of the Goldbach conjecture.

Universal existence of `rho(c)` is a separate hard number-theoretic question and is not required for T71–T75.

## 10. Stage-9 status

- P018-T71 centered shell theorem: `PROVED`
- P018-T72 minimal centered radius => exact factor slack: `PROVED`
- P018-T73 actual near-diagonal slack => minimal centered radius: `PROVED`
- P018-T74 fixed-slack / first-centered-pair criterion: `PROVED`
- P018-T75 unified radius/gap/square-offset/parity coordinate: `PROVED`
- universal existence of positive `rho(c)`: `NOT CLAIMED / OPEN`
- use of centered radius to prove a prime survivor in every square basin: `OPEN`
- recurrence or deterministic bound for `rho(k+1)` across neighboring basins: `OPEN`

Executable finite checks live in `src/enterprise_math/centered_prime_radius.py` and `tests/test_centered_prime_radius.py`.
