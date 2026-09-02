# R005-A — Prime-Gap Obstruction Scale for Least-Basis Failure

Status: `PROVED R005 NECESSARY CONDITION + PRIOR-ART COMPARISON / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-12`

## 1. The phase exponent is not merely sufficient

For the p-power basin

\[
A=k^p,\qquad U=(k+1)^p-1,\qquad W=U-A,
\]

the earlier cube-root-core theorem says:

\[
\text{no least safe witness basis}
\Longrightarrow
\exists q\le U^{1/3}
\text{ prime and non-forced}.
\]

Let

\[
x=A/q.
\]

Let \(P^-(x)\le x<P^+(x)\) be the consecutive primes surrounding x, with the
obvious convention that \(P^-(x)=x\) if x itself is prime.

Because q is non-forced, the e=1 cofactor interval

\[
(x,U/q]
\]

contains no prime. Therefore

\[
P^+(x)-x>\frac Wq.
\]

Hence the full consecutive prime gap g containing x satisfies

\[
\boxed{g>\frac Wq}.
\]

This immediately converts witness-language failure into a prime-gap lower
bound.

---

## 2. T-A46 — exact obstruction exponent

Define

\[
\boxed{
\lambda_p
=
1-\frac{3}{2p}.
}
\]

Since

\[
x=\frac{k^p}{q},
\]

we have

\[
x^{\lambda_p}
=
k^{p-3/2}q^{-1+3/(2p)}.
\]

Therefore

\[
\frac{W/q}{x^{\lambda_p}}
=
W\,k^{3/2-p}q^{-3/(2p)}.
\]

Using

\[
q^3\le U,
\]

we get

\[
q^{3/(2p)}
\le
U^{1/(2p)}.
\]

Thus

\[
\boxed{
g
>
c_{p,k}\,x^{\lambda_p},
}
\]

where

\[
\boxed{
c_{p,k}
=
\frac{W\,k^{3/2-p}}{U^{1/(2p)}}.
}
\]

Because the left prime \(P^-(x)\le x\),

\[
\boxed{
g
>
c_{p,k}\,P^-(x)^{\lambda_p}.
}
\]

Finally,

\[
W\sim p\,k^{p-1},
\qquad
U^{1/(2p)}\sim k^{1/2},
\]

so

\[
\boxed{
c_{p,k}\longrightarrow p.
}
\]

Hence:

> **If no-least p-power basins occur for arbitrarily large k, then**
>
> \[
> \boxed{
> \limsup_{n\to\infty}
> \frac{p_{n+1}-p_n}{p_n^{\,1-3/(2p)}}
> \ge p.
> }
> \]

This is a necessary condition for infinite least-basis failure.

---

## 3. Square-basin specialization

For \(p=2\),

\[
\lambda_2=\frac14.
\]

Here

\[
A=k^2,\qquad U=k^2+2k.
\]

The exact constant simplifies to

\[
c_{2,k}
=
2\left(\frac{k}{k+2}\right)^{1/4}.
\]

Thus any no-least square basin forces a consecutive prime gap satisfying

\[
\boxed{
g
>
2\left(\frac{k}{k+2}\right)^{1/4}
x^{1/4}.
}
\]

Consequently:

\[
\boxed{
\text{infinitely many no-least square basins}
\Longrightarrow
\limsup
\frac{p_{n+1}-p_n}{p_n^{1/4}}
\ge2.
}
\]

This is the **quarter-power barrier** for infinite p=2 least-basis failure.

---

## 4. A converse sufficient gap condition

The contrapositive gives an immediate transfer principle.

If

\[
\boxed{
\limsup_{n\to\infty}
\frac{p_{n+1}-p_n}{p_n^{\lambda_p}}
<p,
}
\]

then only finitely many p-power basins can lack a least safe divisor-witness
basis.

A stronger but simpler sufficient condition is

\[
p_{n+1}-p_n
=
o\!\left(p_n^{\lambda_p}\right).
\]

For p=2:

\[
\boxed{
g_n=o(p_n^{1/4})
\Longrightarrow
\text{all sufficiently large square basins have a unique least basis}.
}
\]

This implication is about R005 witness semantics; it is not a claim that the
stated prime-gap bound has been proved.

---

## 5. The observation-arity phase law becomes an obstruction law

Earlier R005 derived

\[
\lambda_{\rm least}(p)
=
1-\frac{3}{2p}
\]

as the short-prime exponent sufficient to force the cube-root observation core.

T-A46 shows the same exponent from the opposite direction:

\[
\boxed{
\text{least-basis failure}
\Longrightarrow
\text{prime gap of scale }x^{\lambda_{\rm least}(p)}.
}
\]

Therefore \(\lambda_{\rm least}(p)\) is not merely a limitation of the proof
method.

It is the natural prime-gap obstruction scale of the witness language.

The current phase table is:

| p | obstruction exponent | asymptotic failure requires |
|---:|---:|---|
| 2 | \(1/4\) | gap ratio limsup at least 2 |
| 3 | \(1/2\) | gap ratio limsup at least 3 |
| 4 | \(5/8\) | gap ratio limsup at least 4 |
| 5 | \(7/10\) | gap ratio limsup at least 5 |
| 6 | \(3/4\) | gap ratio limsup at least 6 |

---

## 6. Comparison with established short-interval theory

Baker–Harman–Pintz proved that, for all sufficiently large x,

\[
[x,x+x^{0.525}]
\]

contains a prime.

Thus established theory rules out the obstruction for every fixed integer

\[
p\ge4,
\]

because

\[
1-\frac{3}{2p}>0.525.
\]

This recovers the earlier asymptotic least-basis phase boundary, now as a
direct comparison with the **necessary** obstruction exponent.

For p=3:

\[
\lambda_3=\frac12,
\]

so the 0.525 theorem does not reach the required square-root scale.

For p=2:

\[
\lambda_2=\frac14,
\]

and the gap is much larger still.

---

## 7. Newer 0.52 preprint does not change the integer phase boundary

Runbo Li's current preprint claims existence of primes in intervals of length

\[
x^{0.52}
\]

for all sufficiently large x, improving the 0.525 Baker–Harman–Pintz
exponent.

This is newer preprint evidence, not treated here as a replacement for the
published BHP theorem.

Even if accepted as stated, it does not change the R005 integer phase split:

- p=3 still requires exponent 1/2 and remains below 0.52;
- p=4 already has exponent 5/8 and was already controlled;
- all p>=4 remain controlled.

So the important R005 transition remains between p=3 and p=4.

---

## 8. Current large-gap constructions are on the wrong scale

Ford–Maynard–Tao prove that fixed-length chains of consecutive large prime
gaps occur infinitely often.

The proven lower-bound scale is essentially polylogarithmic in the prime
location.

Likewise the Ford–Green–Konyagin–Maynard–Tao large-gap results construct
prime-free intervals of polylogarithmic scale.

For every fixed \(\varepsilon>0\),

\[
(\log x)^C=o(x^\varepsilon).
\]

Therefore even the known theorems producing **several simultaneous large
gaps** are far below the p=2 obstruction scale

\[
x^{1/4}.
\]

So the existence of chains of large prime gaps does not currently supply a
route to infinitely many R005 no-least square basins.

This is a scale mismatch, not a proof that such basins are finite.

---

## 9. Probabilistic prime-gap models

Banks–Ford–Tao's 2023 random-sieve model rigorously predicts largest-gap
behavior on a scale derived from roughly \(\log^2 x\), modified by slowly
varying factors.

In particular the model's largest gaps are subpolynomial:

\[
G_{\rm model}(x)=x^{o(1)}.
\]

Therefore, applying T-A46 to that model:

\[
\boxed{
G_{\rm model}(x)=o(x^{1/4})
}
\]

and the p=2 R005 least-basis failures are almost surely finite in the model.

This is a **model transfer**, not a theorem about the actual primes.

It does show that infinitely many R005 p=2 failures would represent a very
different large-gap regime from the one predicted by modern probabilistic
prime models.

---

## 10. Empirical normalization of the 49 certified failures

The current exact p=2 certificate family was also normalized by the
quarter-power scale.

For every non-forced cube-root witness q participating in the 49 no-least
basins, the corresponding cofactor gap satisfies the T-A46 lower bound.

Among the current exact witnesses, the smallest observed normalized ratio

\[
\frac{g}{p^{1/4}}
\]

is approximately

\[
\boxed{2.2515},
\]

at

\[
k=5833,\qquad q=281,
\]

using the consecutive cofactor primes

\[
121081<121123
\]

with gap 42.

The theoretical asymptotic obstruction constant is 2.

This numerical proximity is suggestive but is not evidence that the constant
2 is sharp for actual residual formation.

---

## 11. R005 last-failure conjecture

The exact finite classification proved earlier gives:

\[
k=35901
\]

as the last no-least basin through the certified endpoint

\[
11661903789.
\]

T-A46 plus standard prime-gap probabilistic models strongly suggest eventual
unique least-basis behavior.

This motivates the explicit R005 conjecture:

> **R005 square last-failure conjecture**
>
> \[
> \boxed{
> k=35901
> }
> \]
> is the largest square-basin index whose divisor-witness language lacks a
> least safe basis.

Status:

`CONJECTURAL / EXACTLY VERIFIED THROUGH 11,661,903,789 / MODEL-SUPPORTED`.

This should not be promoted as a classical prime conjecture; it is a statement
about the R005 witness language.

---

## 12. Next infinite frontier

A future counterexample beyond the certified range must do more than contain
a "large gap".

It must generate:

1. a quarter-power-scale cofactor prime gap;
2. a prime q in the reciprocal gap strip;
3. at least two compatible non-forced witness coordinates;
4. a successful multiplicative pair closure.

For \(\tau\ge2\), several such closed residual blocks must additionally form
either disjoint blocks or a Berge-triangle obstruction.

Thus the infinite hierarchy is now:

\[
\boxed{
x^{1/4}\text{-scale gap}
\to
\text{reciprocal NF strip}
\to
\text{strip overlap}
\to
\text{pair closure}
\to
\text{repair obstruction}.
}
\]

The first arrow alone already lies well beyond the scale of known large-gap
lower-bound constructions and far above standard probabilistic predictions.

---

## 13. External primary references

1. R. C. Baker, G. Harman, J. Pintz, **The Difference Between Consecutive Primes, II**, Proceedings of the London Mathematical Society 83 (2001), 532–562. DOI: `10.1112/plms/83.3.532`. Established input used here: sufficiently large intervals of length \(x^{0.525}\) contain a prime.

2. Runbo Li, **The number of primes in short intervals and numerical calculations for Harman's sieve**, arXiv:`2308.04458`, current preprint version. Preprint claim used only as a status comparison: sufficiently large intervals of length \(x^{0.52}\) contain primes. It is not substituted for the published BHP theorem in the proved-status classification.

3. Kevin Ford, James Maynard, Terence Tao, **Chains of large gaps between primes**, arXiv:`1511.04468`. Used only to compare known simultaneous-large-gap constructions with the much larger polynomial R005 obstruction scale.

4. William Banks, Kevin Ford, Terence Tao, **Large prime gaps and probabilistic models**, Inventiones Mathematicae 233 (2023), 1471–1518. DOI: `10.1007/s00222-023-01199-0`. Used only for model/heuristic transfer: the analyzed random-sieve largest-gap scale is subpolynomial and therefore lies below the R005 quarter-power obstruction.

All four inputs remain external prior mathematics. T-A46 is the R005 translation from least-basis failure to a required prime-gap scale.
