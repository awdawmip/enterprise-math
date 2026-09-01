# R005-B — Horizon-Gap Phase Supplement 02

Status: `PROVED WIP / DRAFT OWNER SUPPLEMENT / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Consumes: R005-A T-A16/T-A22, P018 square centered-shell results  
Owner branch: `agent/r005b-prime-collapse-field`

## 1. Why this supplement exists

The first two R005-B checkpoints identified the universal factor horizon

\[
F=F_p(k)=\left\lfloor\sqrt{(k+1)^p-1}\right\rfloor
\]

and the one-large-prime normal form below the basin upper endpoint.

The remaining p=3 / p=4 full-forcing frontier is not controlled by one uniform
"next prime after A/q" rule.  Near the factor horizon, the next prime after
`A/q` can itself still be a candidate divisor and therefore cannot serve as an
exclusive cofactor.

This supplement gives the exact global e=1 cofactor rule, isolates a theorem-
safe pure horizon cap, and shows that the R005-A full-forcing exponent

\[
\lambda(p,2)=1-\frac2p
\]

has a direct factor-horizon interpretation: it is the exponent of the
right-of-horizon prime-free gap required for the upper critical cap to survive.

No prime-gap conjecture is proved here.

---

## 2. Setup

Fix `p>=2`, `k>=1`, and write

\[
A=k^p,
\qquad
U=(k+1)^p-1,
\qquad
F=\lfloor\sqrt U\rfloor.
\]

A **candidate divisor witness** is a prime `q<=F`.

An **e=1 exclusive-cofactor certificate** for q means an integer

\[
n=qr
\]

in the basin `A<n<=U`, where `r` is prime and `r>F`.

The condition `r>F` is essential: otherwise r is itself another candidate
small-prime divisor, so q does not have singleton candidate support (unless one
is studying a different pure-power route rather than the e=1 cofactor route).

Let `nextprime(t)` denote the least prime strictly larger than integer t.

---

## 3. B12.1 — global first exclusive-cofactor theorem

### Theorem

For every candidate prime `q<=F`, define

\[
\boxed{
r_*(q)=
\operatorname{nextprime}
\left(
\max\left(F,\left\lfloor\frac Aq\right\rfloor\right)
\right).
}
\]

Then q has an e=1 exclusive-cofactor certificate if and only if

\[
\boxed{q\,r_*(q)\le U.}
\]

When it exists, `q*r_*(q)` is the least such certificate.

### Proof

Any eligible cofactor prime r must satisfy two independent strict lower bounds:

1. `r>F`, so r is outside the candidate-divisor language;
2. `qr>A`, equivalently `r>A/q`.

For integer prime r these are jointly equivalent to

\[
r>
\max\left(F,\left\lfloor A/q\right\rfloor\right).
\]

The least eligible prime is therefore exactly `r_*(q)`.  If `q*r_*(q)>U`, every
later eligible prime is even larger and no e=1 certificate can fit.  If
`q*r_*(q)<=U`, strict lower-basin membership is automatic from the construction.
∎

This theorem was independently checked against literal e=1 searches in 554
bounded `(p,k,q)` cases for `p=2,3,4`, `2<=k<=15`.

---

## 4. B12.2 — exact two-regime split

The global rule has two arithmetic regimes.

### Regime I — cofactor-gap band

If

\[
qF\le A,
\]

then `A/q>=F`, so

\[
r_*(q)=
\operatorname{nextprime}
\left(\left\lfloor A/q\right\rfloor\right).
\]

This is the regime represented by R005-A T-A16: the e=1 obstruction is encoded
by the consecutive-prime gap surrounding the cofactor point `A/q`, and the
reciprocal-gap interval gives the dangerous q.

### Regime II — horizon-gap band

If

\[
qF>A,
\]

then `A/q<F`, so the factor-horizon exclusion rather than the basin lower
endpoint controls the first eligible cofactor.  Put

\[
\boxed{R=\operatorname{nextprime}(F).}
\]

Then

\[
\boxed{r_*(q)=R}
\]

for every q in this band, and the e=1 certificate condition becomes simply

\[
\boxed{qR\le U.}
\]

So all upper-band witnesses share the same first post-horizon prime.

### Scope correction to R005-A T-A16 wording

The unspecialized phrase "the next prime after A/q gives the e=1 exclusive
collision" needs the condition that this next prime is already above F, for
example `A/q>=F`.  Without that condition the next cofactor prime can remain a
candidate witness and the product need not have singleton support.

This is a **scope correction**, not a contradiction to the R005-A cubic-core or
finite least-basis results: those results deliberately operate on smaller
forced cores where the cofactor point lies on the safe side of the horizon
boundary.  The correction matters for global **full forcing**, especially the
upper candidate band.

---

## 5. Exact cubic witness for the scope boundary

Take the cubic basin `p=3`, `k=23`:

\[
A=23^3=12167,
\qquad
U=24^3-1=13823,
\qquad
F=117.
\]

Take candidate prime

\[
q=109.
\]

Then

\[
\left\lfloor\frac Aq\right\rfloor=111<F.
\]

The next prime after 111 is 113, and

\[
12167<109\cdot113=12317\le13823.
\]

But

\[
113\le F,
\]

so 113 is another candidate divisor.  The product is not an exclusive
q-certificate.

The first eligible exclusive cofactor is instead

\[
R=\operatorname{nextprime}(117)=127,
\]

and

\[
109\cdot127=13843>13823.
\]

Therefore q=109 has no e=1 exclusive-cofactor certificate.

The pure-cap theorem below shows that in this case no other singleton-support
form can rescue q, so q is genuinely non-forced.

This gives a concrete mechanism for R005-A's existing statement that p=3 full
forcing is false in general even though a much smaller cubic core can already
be sufficient for a unique least basis.

---

## 6. B13 — pure cofactor horizon-cap theorem

The global e=1 theorem is not by itself a complete forcedness theorem: a
candidate q may also obtain singleton support from `q^a` or `q^a r` with
`a>=2`.

The following exact cap excludes those alternatives.

### Definition — pure cofactor cap

A candidate prime q lies in the pure cofactor cap when

\[
\boxed{
q\le F,
\quad
q^2\le A,
\quad
q^3>U,
\quad
q^2(F+1)>U,
\quad
qF>A.
}
\]

### Theorem B13.1

For q in the pure cofactor cap, put

\[
R=\operatorname{nextprime}(F).
\]

Then q has singleton candidate-prime support somewhere in the basin if and only
if

\[
\boxed{qR\le U.}
\]

When it exists, the certificate is exactly of the form

\[
qR.
\]

Thus, consuming the R005-A singleton-support -> forced-witness theorem,

\[
\boxed{
q\text{ is forced}
\iff
qR\le U
}
\]

on this cap.

### Proof

The prior R005-B one-large-prime normal form says every integer below
`(F+1)^2` has at most one prime factor exceeding F, and such a factor occurs to
exponent one.  Since `U<(F+1)^2`, any singleton-q-support basin integer is
therefore either

\[
q^a
\]

or

\[
q^a r,
\qquad r>F\text{ prime}.
\]

The cap inequalities remove every form except `q r`:

- `q^2<=A` removes q^2 from the basin;
- `q^3>U` removes all pure powers q^a with a>=3;
- `q^2(F+1)>U` removes every q^a r with a>=2 and r>F;
- `qF>A` places the remaining e=1 route in the horizon-gap regime.

Hence q has singleton support exactly when the first prime `R>F` satisfies
`qR<=U`. ∎

A bounded independent direct-support regression checked 325 pure-cap candidates
for `p=3,4`, `3<=k<45` against literal basin multiples.

---

## 7. Cubic pure-cap failures already occur at small scales

Exact integer examples include

| cubic k | F_3(k) | first prime R>F | non-forced pure-cap q |
|---:|---:|---:|---|
| 23 | 117 | 127 | 109 |
| 64 | 524 | 541 | 509 |
| 120 | 1330 | 1361 | 1303, 1307 |
| 138 | 1638 | 1657 | 1621 |
| 1005 | 31907 | 31957 | 31859 |

These are exact certificates of **non-full-forcing**.  They do not imply a
least-basis failure: R005-A T-A18 shows that forcing the much smaller cubic core
`q<=k` is already sufficient to eliminate every residual composite.

No claim is made here that all cubic non-forced witnesses lie in the pure cap,
or that the displayed family is exhaustive/infinite.

The remaining asymptotic question for p=3 is therefore sharper:

> do horizon/cofactor-gap failures continue infinitely often, or are the known
> non-forced witnesses only a finite pre-asymptotic phenomenon?

Current BHP-scale input cannot decide that question.

---

## 8. B14 — horizon-gap threshold theorem

Put

\[
S=S_p(k)=\lfloor\sqrt A\rfloor,
\qquad
R=\operatorname{nextprime}(F).
\]

Suppose a non-forced pure-cap candidate q also satisfies `q<=S` (already part
of the cap through `q^2<=A`).  Then

\[
qR>U
\]

and `q<=S`, hence

\[
\boxed{RS>U.}
\]

Equivalently,

\[
R>\frac US.
\]

Therefore the prime-free gap immediately to the right of F must exceed

\[
\boxed{
G_p(k)=\frac{U}{S_p(k)}-F_p(k).
}
\]

The executable implementation retains the exact rational pair

\[
(U-FS,\ S)
\]

and tests the obstruction by the integer inequality `R*S>U`; no floating-point
comparison is required.

This is a necessary condition for pure-cap non-forcing.  It turns a witness
search near the horizon into one post-horizon prime-gap test plus a short q-cap
check.

---

## 9. B15 — asymptotic horizon-gap exponent

For fixed `p>=3`, as `k->infinity`,

\[
S_p(k)=k^{p/2}+O(1),
\]

\[
U=k^p+p k^{p-1}+O(k^{p-2}),
\]

and

\[
F_p(k)
=
 k^{p/2}
 +\frac p2 k^{p/2-1}
 +O(k^{p/2-2}+1).
\]

Consequently

\[
\boxed{
G_p(k)
=
\frac p2 k^{p/2-1}
+O(k^{p/2-2}+1).
}
\]

Since `F_p(k) asymp k^(p/2)`, the same threshold has horizon-scale form

\[
\boxed{
G_p(k)\asymp F_p(k)^{\,1-2/p}.
}
\]

Thus the horizon-gap exponent is

\[
\boxed{\gamma_p=1-\frac2p.}
\]

But R005-A T-A22 already obtained, from the cofactor-interval side, the
full-forcing short-prime exponent

\[
\boxed{\lambda(p,2)=1-\frac2p.}
\]

Hence

\[
\boxed{\gamma_p=\lambda(p,2).}
\]

This equality is the structural bridge of this supplement:

> the analytic exponent in the R005-A full-forcing phase diagram is exactly the
> arithmetic scale of the post-factor-horizon prime-free gap required for the
> upper pure cofactor cap to remain unresolved.

The equality does not claim novelty for classical short-interval prime theory.
It identifies what that exponent means inside the Prime Toolkit geometry.

---

## 10. The refined collapse-dimension phase

### p=2 — self-aligned / no horizon cap

Here

\[
F_2(k)=k,
\qquad
A=k^2.
\]

For every candidate `q<=F`,

\[
qF\le k^2=A.
\]

So the horizon-gap band `qF>A` is empty.

Square non-forcing therefore cannot arise from this upper cofactor cap.  Its
near-horizon behavior is instead the centered-shell / fixed-prime-gap mechanism
already owned by P018 and consumed by the previous R005-B supplement.

This is another exact sense in which p=2 is structurally exceptional.

### p=3 — cube-root horizon-gap scale

\[
G_3(k)
=
\frac32\sqrt{k}+O(1)
\asymp F^{1/3}.
\]

So a pure-cap failure requires a post-horizon prime gap on the order of
`F^(1/3)`.  Existing BHP exponent 0.525 is much larger than 1/3 and therefore
does not rule out this mechanism asymptotically.

R005-A already proves that p=3 full forcing is false at finite scales while a
smaller forced core suffices for least-basis control.  The new result explains
where the upper non-forced witnesses can live and why current short-interval
technology does not automatically make them disappear.

### p=4 — exact square-gap criticality

For p=4,

\[
S=k^2,
\qquad
F=(k+1)^2-1=k^2+2k,
\]

and the threshold is exactly

\[
\boxed{
G_4(k)
=2k+6+\frac4k.
}
\]

So the required post-horizon gap is square-root scale in F.

### p>=5 — BHP crosses the cap exponent

For fixed p>=5,

\[
1-\frac2p>0.525.
\]

Therefore the established BHP prime-gap scale is asymptotically smaller than
the pure-cap protecting gap `G_p(k)`, so BHP eventually kills this cap
mechanism.

R005-A T-A22 already supplies the stronger global conclusion: for p>=5 the
entire candidate language is eventually forced.  The present theorem should be
read as an arithmetic/geometric explanation of why the integer transition
occurs at p=5, not as a replacement proof of the global R005-A result.

---

## 11. B16 — quartic cap failure localizes directly to Legendre

The p=4 cap gives an especially sharp consequence.

Assume a pure-cap q is non-forced.  Then B14 gives

\[
Rk^2>U,
\]

so

\[
R>\frac{U}{k^2}
=k^2+4k+6+\frac4k.
\]

But

\[
(k+2)^2=k^2+4k+4.
\]

Hence

\[
\boxed{R>(k+2)^2.}
\]

On the other hand

\[
F=(k+1)^2-1,
\]

and R is the first prime strictly above F.  Therefore there is no prime in

\[
\boxed{((k+1)^2,(k+2)^2).}
\]

So:

\[
\boxed{
\text{p=4 pure horizon-cap non-forcing at basin k}
\Longrightarrow
\text{Legendre failure at square index }k+1.
}
\]

The exact arithmetic margin is

\[
U-k^2(k+2)^2=2k(k+2)>0.
\]

This is a one-way implication and proves no Legendre statement.  It sharpens
"p=4 is square-gap critical" into a local factor-horizon theorem.

R005-A T-A17 already gives a broader Legendre-to-p4 forcing transport; the
present result is the reverse diagnostic only for the explicitly declared pure
horizon cap.

---

## 12. Updated phase picture

The full-forcing frontier should now be read as follows.

| p | upper-horizon mechanism | required gap scale | current structural status |
|---:|---|---|---|
| 2 | horizon cap empty; P018 centered shell | fixed centered prime gaps | full forcing fails infinitely often |
| 3 | genuine horizon/cofactor cap | `F^(1/3)` | finite non-forced examples; eventual behavior unresolved |
| 4 | horizon cap is consecutive-square critical | `F^(1/2)` | cap failure implies Legendre failure; global full forcing remains square-gap critical |
| >=5 | horizon cap too wide for BHP-size gaps | `F^(1-2/p)` with exponent >0.525 | R005-A gives eventual global full forcing |

This makes p=5 a real arithmetic phase threshold rather than only the solution
of one exponent inequality.

---

## 13. R005-A / R005-B ownership bridge

### R005-B owns here

- exact factor-horizon boundary F;
- global first eligible exclusive cofactor `nextprime(max(F,floor(A/q)))`;
- cofactor-gap versus horizon-gap regime split;
- pure cofactor cap and its one-prime normal form;
- horizon-gap threshold `G_p(k)` and its exponent interpretation.

### R005-A remains owner of

- generic forced/exclusive witness semantics;
- forced core, residual hypergraph, least safe basis and hitting-set theory;
- T-A16 reciprocal-gap search in its valid cofactor-gap band;
- T-A22 observation-arity/collapse-dimension phase theorem;
- finite Oppermann/Legendre transports.

### P018 remains owner of

- square centered-shell / centered-prime-radius theorems.

The correct cross-route flow is therefore

\[
\text{R005-B factor horizon / eligible cofactor}
\to
\text{R005-A singleton support / forcedness}
\to
\text{R005-A residual basis theory}.
\]

No mother theorem is duplicated.

---

## 14. Prior-art boundary

Classical objects used here include:

- the least-prime-factor square-root criterion;
- the next-prime function and consecutive prime gaps;
- primes in short intervals, including the Baker-Harman-Pintz exponent already
  consumed by R005-A;
- Legendre/Oppermann consecutive-power questions;
- elementary asymptotic binomial expansion.

The project-side contribution under test is the exact coupling of those objects
to the factor-horizon split, pure-cap witness normal form, and the equality
between the R005-A full-forcing exponent and the R005-B post-horizon protecting
gap exponent.

Historical novelty remains `NOVELTY_UNVERIFIED`.

---

## 15. Executable checkpoint

Owner-local additions:

- `src/enterprise_math/prime_horizon_gap.py`;
- `tests/test_prime_horizon_gap.py`.

The regression surface includes:

- 554 exact global e=1 comparisons against literal search;
- the cubic `(k,q)=(23,109)` horizon-scope counterexample;
- selected exact cubic pure-cap non-forced examples;
- the proof-level fact that the p=2 horizon cap is empty;
- exact p=4 threshold algebra and Legendre localization;
- 325 pure-cap comparisons against independent literal singleton-support search
  on a bounded p=3/p=4 grid.

The runtime used for this research did not provide a repository checkout, so the
new committed files were not imported as a package here.  The theorem formulas
were independently exercised with exact standalone integer code.  Full-suite
validation remains a later integration boundary.

---

## 16. Next frontier

The p=3 question is now the sharpest unresolved R005-B target.

Do not ask merely whether cubic full forcing holds.  It already fails at finite
scales.  The next question is:

\[
\boxed{
\text{Are cubic horizon/cofactor non-forcing events finite or infinite?}
}
\]

A productive attack should separate:

1. the pure horizon cap, controlled by the first prime after F;
2. the lower cofactor-gap band, controlled by reciprocal prime gaps;
3. possible higher-power q-certificates outside the pure-cap hypotheses.

For p=4, the corresponding pure-cap question has already been localized to
consecutive-square prime existence; further progress without new square-gap
input should focus on exact equivalence boundaries rather than larger brute
force cutoffs.
