# P018 — Finite-Precision Proof Calculus, Supplement 07

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact relation between square-basin factor proof slack and fixed even prime gaps  
Depends on: P018 Stage 7 and P017 first-factor shells  
Discipline: twin/cousin primes and bounded prime-gap theorems are established number theory. The external bound used below is credited to D. H. J. Polymath. This note does not improve any prime-gap bound and does not prove Legendre's conjecture.

## 1. From factor horizon to factor proof slack

Stage 7 defines the minimal survivor-prime horizon

\[
H(k)=\max\{\operatorname{spf}(n): k^2<n<(k+1)^2,\ n\text{ composite}\}
\]

and the nonnegative factor proof slack

\[
\boxed{\sigma(k)=k-H(k).}
\]

To avoid confusion with the standard bounded-prime-gap notation `H_1`, this supplement will sometimes call the same horizon

\[
h_{\mathrm{fac}}(k)=H(k).
\]

The question is now: what arithmetic structure is forced when the last composite shell sits only `s` precision units below the universal cutoff `k`?

Write

\[
s=\sigma(k),
\qquad
p=k-s.
\]

Then `p=H(k)` is the least-prime-factor index of the last nonempty composite first-decision shell.

## 2. P018-T63 — Near-diagonal shell / fixed-gap theorem

Status: `PROVED`.

Let `s>=0`, let

\[
p=k-s
\]

be an odd prime, and assume

\[
\boxed{p>(s+1)^2.}
\]

Then

\[
\boxed{
L_p(k)\ne\varnothing
\iff
q:=p+2(s+1)\text{ is prime}.
}
\]

Moreover, when nonempty,

\[
\boxed{
L_p(k)=\{pq\}.
}
\]

### Step 1 — the size condition already forces a semiprime shell

Put `t=s+1`. Since `p>t^2` and `p>=3`, one has `t<=p-1` and `t^2<=p-1`. Hence

\[
2pt+t^2
\le
2p(p-1)+(p-1).
\]

Therefore

\[
\begin{aligned}
p^3-(p+t)^2
&=p^3-p^2-2pt-t^2\\
&\ge p^3-3p^2+p+1\\
&=p^2(p-3)+p+1>0.
\end{aligned}
\]

Since `k+1=p+s+1=p+t`,

\[
p^3>(k+1)^2>(k+1)^2-1.
\]

Thus Stage-7 T62 applies: every state in `L_p(k)` is a semiprime

\[
n=pq,
\qquad q>p\text{ prime}.
\]

### Step 2 — the cofactor interval contains only two integers

The basin inequalities are

\[
(p+s)^2<pq<(p+s+1)^2.
\]

Dividing by `p` gives

\[
p+2s+\frac{s^2}{p}
<q<
p+2s+2+\frac{(s+1)^2}{p}.
\]

Because `p>(s+1)^2`, both fractions lie strictly between `0` and `1` (with the left fraction equal to zero only when `s=0`). Hence an integer `q` can only be

\[
p+2s+1
\quad\text{or}\quad
p+2s+2.
\]

The first candidate is even because `p` is odd, and it is greater than `2`; it cannot be prime. Therefore

\[
q=p+2s+2=p+2(s+1).
\]

This proves necessity and uniqueness.

### Step 3 — converse

If both `p` and `q=p+2(s+1)` are prime, then

\[
pq-k^2
=2p-s^2>0
\]

because `p>(s+1)^2>s^2/2`, while

\[
(k+1)^2-pq=(s+1)^2>0.
\]

Thus `pq` lies in the open basin and has smallest prime factor `p`, proving the converse.

So the shell nearest the universal factor horizon is governed by a fixed even prime gap.

## 3. P018-T64 — Zero slack is exactly the twin-prime stratum

Status: `PROVED`.

For every `k>=3`,

\[
\boxed{
\sigma(k)=0
\iff
k\text{ and }k+2\text{ are both prime}.
}
\]

Proof: `sigma(k)=0` means `H(k)=k`, so `L_k(k)` is nonempty. Apply T63 with `s=0`: the only possible shell state is

\[
k(k+2)=(k+1)^2-1,
\]

and it exists exactly when `k` and `k+2` are prime.

Conversely, a twin-prime pair `k,k+2` puts `k(k+2)` into `L_k(k)`, so `H(k)>=k`; Stage 7 gives `H(k)<=k`, hence equality. ∎

Therefore the Twin Prime Conjecture is equivalent to the statement that

\[
\boxed{
\sigma(k)=0
\text{ for infinitely many }k.
}
\]

This is an equivalence of formulations, not progress on the twin-prime conjecture.

## 4. P018-T65 — Slack one is exactly the gap-four stratum

Status: `PROVED`.

For every `k>=4`,

\[
\boxed{
\sigma(k)=1
\iff
k-1\text{ and }k+3\text{ are both prime}.
}
\]

For `k=4`, this is the direct basin calculation `H(4)=3` and the prime pair `3,7`.

For larger `k`, if `sigma(k)=1`, then `p=H(k)=k-1` is prime. For `k>=6`, `p>4=(s+1)^2`, so T63 with `s=1` forces `p+4=k+3` prime.

Conversely, if `k-1` and `k+3` are prime, the product

\[
(k-1)(k+3)=(k+1)^2-4
\]

lies in `L_(k-1)(k)`. For `k>4`, primality of `k-1` forces `k` to be even, hence nonprime, so no shell can occur at index `k`. Thus `H(k)=k-1`. ∎

So infinitely many gap-four prime pairs are equivalent to infinitely many `k` with `sigma(k)=1`.

## 5. P018-T66 — Actual bounded slack forces a fixed even prime gap

Status: `PROVED`.

Suppose

\[
\sigma(k)=s,
\qquad
p=k-s\ge3,
\qquad
p>(s+1)^2.
\]

Because `p=H(k)`, the shell `L_p(k)` is nonempty. T63 therefore gives

\[
\boxed{
p\text{ and }p+2(s+1)\text{ are prime}.}
\]

Thus an actual small factor proof slack is not merely a statement about composite-factor cutoffs: sufficiently far out, it forces a prime pair whose even gap is exactly

\[
\boxed{2(s+1).}
\]

## 6. P018-T67 — A fixed prime gap creates a bounded-slack square basin

Status: `PROVED`.

Let

\[
p,\quad q=p+2m
\]

be primes with `m>=1`, and suppose

\[
\boxed{p>m^2.}
\]

Set

\[
s=m-1,
\qquad
k=p+s=p+m-1.
\]

Then `p=k-s`, and T63 gives

\[
pq\in L_p(k).
\]

Therefore

\[
H(k)\ge p=k-s,
\]

so

\[
\boxed{
\sigma(k)=k-H(k)\le s=m-1.
}
\]

Thus every sufficiently large prime pair of fixed gap `2m` produces a square basin whose factor proof slack is at most `m-1`.

The actual slack may be smaller if a later first-factor shell is also nonempty.

## 7. P018-T68 — Bounded factor slack and a repeated fixed prime gap are equivalent at infinity

Status: `PROVED`.

The following two statements are equivalent:

1. there exists an integer `S>=0` for which `sigma(k)<=S` for infinitely many `k`;
2. there exists an integer `m>=1` for which prime pairs `p,p+2m` occur infinitely often.

### 1 => 2

Among infinitely many `k` with `sigma(k)<=S`, one exact slack value

\[
s\in\{0,1,\ldots,S\}
\]

occurs infinitely often by the finite pigeonhole principle.

For all sufficiently large such `k`, `p=k-s>(s+1)^2`. T66 then gives prime pairs

\[
p,\ p+2(s+1)
\]

infinitely often. Take `m=s+1`.

### 2 => 1

If `p,p+2m` occur infinitely often, then eventually `p>m^2`. T67 maps every such sufficiently large pair to

\[
k=p+m-1
\]

with

\[
\sigma(k)\le m-1.
\]

Thus bounded factor proof slack occurs infinitely often. ∎

So the question “is `liminf sigma(k)` finite?” is exactly another finite-precision formulation of the existence of some fixed even prime gap occurring infinitely often.

## 8. P018-T69 — Established bounded prime gaps imply an unconditional slack bound

Status: `PROVED COROLLARY OF ESTABLISHED PRIOR ART`.

D. H. J. Polymath proved the unconditional bounded-gap result

\[
H_1^{\mathrm{gap}}
:=
\liminf_{n\to\infty}(p_{n+1}-p_n)
\le246.
\]

[SRC-POLYMATH-2014-BOUNDED-GAPS]

Hence infinitely many consecutive prime pairs have gap at most `246`.

For all sufficiently large primes such gaps are positive even integers, so among the finite set

\[
2,4,\ldots,246
\]

one fixed even gap `2m` occurs infinitely often. Necessarily

\[
m\le123.
\]

Apply T67 to that fixed gap. For infinitely many resulting square basins,

\[
\sigma(k)\le m-1\le122.
\]

Therefore

\[
\boxed{
\liminf_{k\to\infty}\sigma(k)\le122.
}
\]

This does **not** improve the Polymath prime-gap theorem. It is a new project-side translation of that established theorem into P018 factor-precision language.

A future external improvement from a bound `H_1^gap<=2M` would automatically translate through the same argument to

\[
\liminf\sigma(k)\le M-1.
\]

## 9. P018-T70 — Last precision obstruction sits at a square offset below the upper square

Status: `PROVED`.

Under the hypotheses of T66, the last nonempty composite shell has the unique state

\[
n=p[p+2(s+1)].
\]

Using `p=k-s`,

\[
\boxed{
n=(k-s)(k+s+2).}
\]

Expanding around the upper basin anchor gives

\[
\boxed{
n=(k+1)^2-(s+1)^2.}
\]

Thus the factor precision slack simultaneously determines three quantities:

\[
\boxed{
\begin{aligned}
\text{factor slack} &= s,\\
\text{forced prime gap} &= 2(s+1),\\
\text{upper-square offset} &= (s+1)^2.
\end{aligned}}
\]

This is the most direct Stage-8 realization of the original P018 thesis that **precision change is itself mathematical structure**: one finite proof-precision distance becomes both a prime-pair distance and a square-basin geometric offset.

## 10. What these results do and do not solve

Stage 8 produces exact equivalences and an unconditional corollary, but it does not prove Legendre's conjecture.

In particular:

- bounded `sigma` only tells us that the final composite obstruction lies near the universal factor cutoff;
- the existence of prime survivors is still the Legendre target;
- `sigma=0` infinitely often is exactly the twin-prime conjecture, not a proof of it;
- T69 imports an established bounded-prime-gap theorem and translates it; it does not sharpen that theorem.

The gain is structural: a P018 precision observable that originated as an internal proof-effort quantity now has a precise external number-theoretic meaning.

## 11. Prior-art boundary

Twin primes, cousin primes (gap four), fixed even prime-gap problems, and bounded gaps between primes are established number theory.

The unconditional input used here is D. H. J. Polymath, *Variants of the Selberg sieve, and bounded intervals containing many primes*, Research in the Mathematical Sciences 1 (2014), Article 12, DOI `10.1186/s40687-014-0012-7`. [SRC-POLYMATH-2014-BOUNDED-GAPS]

Enterprise Math does not claim the bound `246`, the Selberg/Maynard-Tao sieve machinery behind it, or fixed-gap conjectures as project inventions.

The project-specific research result under test is the exact change of variables

\[
\text{factor proof slack}
\longleftrightarrow
\text{near-diagonal first-factor shell}
\longleftrightarrow
\text{fixed even prime gap}
\longleftrightarrow
\text{square offset below }(k+1)^2,
\]

plus the resulting translation of an established bounded-gap theorem into an unconditional bound on `liminf sigma(k)`.

Historical novelty of this translation remains `NOVELTY_UNVERIFIED`.

## 12. Stage-8 status

- P018-T63 near-diagonal shell / fixed-gap theorem: `PROVED`
- P018-T64 `sigma=0` iff twin-prime pair: `PROVED`
- P018-T65 `sigma=1` iff gap-four prime pair: `PROVED`
- P018-T66 actual bounded slack forces fixed prime gap: `PROVED`
- P018-T67 fixed prime pair creates bounded slack: `PROVED`
- P018-T68 bounded-slack / fixed-gap infinitude equivalence: `PROVED`
- P018-T69 Polymath `246` => `liminf sigma<=122`: `PROVED COROLLARY OF PRIOR ART`
- P018-T70 square-offset localization: `PROVED`
- `sigma=0` infinitely often / Twin Prime Conjecture: `OPEN, EQUIVALENT FORMULATION`
- independent universal bound `sigma(k)<=S` for all sufficiently large `k`: `OPEN`
- use of bounded slack to prove a prime survivor in every square basin: `OPEN`

Executable finite checks live in `src/enterprise_math/prime_gap_slack.py` and `tests/test_prime_gap_slack.py`.
