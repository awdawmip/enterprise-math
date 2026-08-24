# P017 — Two-Stage Prime-Gap Recycling for Consecutive-Square P2

Status: `PROVED_WIP CONDITIONAL TRANSFER + EXACT INTEGER ENDPOINTS / NOT CANONICAL / EXTERNAL GAP INPUT NOT REPROVED`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Parent note: `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`

Scope: construct a product of two primes inside

\[
I_K=(K^2,(K+1)^2)
\]

by reusing a finite operational prime-gap statement twice. This bypasses the P017/Chen bilinear remainder for a very large finite range. It does not prove an all-`K` P2 theorem and does not reprove the external prime-gap computations.

---

## 1. Operational prime-gap input

Write

\[
\operatorname{GAP}(B,G)
\]

for the following statement:

> for every real `x` with `0<x<B`, there is a prime `r` satisfying
> \[
> x<r\le x+G.
> \]

Two potentially different inputs will be used:

- `GAP(B_p,G_p)` to select the first prime factor `p`;
- `GAP(B_q,G_q)` to select its prime cofactor `q`.

The distinction is useful because a short local certificate for the selector-prime range may have a much smaller gap constant than the global cofactor certificate.

---

## 2. P2-R06 — Two-stage gap-recycling theorem

### Theorem

Let `K>=1`, and suppose `GAP(B_p,G_p)` and `GAP(B_q,G_q)` hold. Put

\[
U_K=\frac{2K+1}{G_q}.
\]

Assume

\[
\boxed{
0<U_K-G_p<B_p
}
\]

and

\[
\boxed{
\frac{K^2}{B_q}<U_K-G_p.
}
\]

Equivalently, the second inequality is

\[
\boxed{
B_q(2K+1-G_qG_p)>G_qK^2.
}
\]

Then there are primes `p,q` such that

\[
\boxed{
K^2<pq<(K+1)^2.
}
\]

Hence the open consecutive-square interval contains an integer with exactly two prime factors counted with multiplicity.

### Proof

The strict inequality

\[
\frac{K^2}{B_q}<U_K-G_p
\]

allows one to choose a sufficiently small real `epsilon>0` such that

\[
\frac{K^2}{B_q}<U_K-G_p-\epsilon
\]

and

\[
0<U_K-G_p-\epsilon<B_p.
\]

Apply `GAP(B_p,G_p)` at

\[
x_p=U_K-G_p-\epsilon.
\]

There is a prime `p` with

\[
U_K-G_p-\epsilon<p\le U_K-\epsilon<U_K.
\]

In particular,

\[
p>\frac{K^2}{B_q},
\]

so

\[
x_q:=\frac{K^2}{p}<B_q.
\]

Apply `GAP(B_q,G_q)` at `x_q`. There is a prime `q` with

\[
\frac{K^2}{p}<q\le\frac{K^2}{p}+G_q.
\]

Multiplication by `p` gives

\[
K^2<pq\le K^2+pG_q.
\]

Since `p<U_K`,

\[
pG_q<2K+1.
\]

Therefore

\[
pq<K^2+2K+1=(K+1)^2.
\]

This proves the theorem. ∎

---

## 3. Why the construction is a P017 cofactor-window hit

For a prime `p`, the canonical P017 cofactor window is

\[
W_p(K)=
\left[
\left\lfloor\frac{K^2}{p}\right\rfloor+1,
\left\lfloor\frac{K^2+2K}{p}\right\rfloor
\right].
\]

The proof above selects `p` so that the guaranteed prime after `K^2/p` lies before the upper window endpoint. Indeed,

\[
q\le\frac{K^2}{p}+G_q
<
\frac{K^2+2K+1}{p},
\]

because `pG_q<2K+1`. Since `q` is an integer, this is exactly

\[
q\in W_p(K).
\]

Thus P2-R06 is a direct prime-in-one-P017-window construction. The first use of the gap theorem chooses a window whose width is guaranteed to dominate the second gap constant; the second use places a prime inside that window.

---

## 4. P2-R07 — Same-source recycling corollary

Assume one operational statement `GAP(B,G)` and use it in both stages. If

\[
0<\frac{2K+1}{G}-G<B
\]

and

\[
\boxed{
B(2K+1-G^2)>GK^2,
}
\]

then `I_K` contains a semiprime.

The admissible integers are exactly those lying strictly between the two real roots of

\[
GK^2-2BK+B(G^2-1)=0.
\]

When the discriminant is positive, those roots are

\[
\boxed{
K_\pm=
\frac{B\pm\sqrt{B^2-BG(G^2-1)}}{G}.
}
\]

This is an elementary finite transfer theorem. It uses no weighted sieve and no average-distribution estimate.

---

## 5. P2-R08 — Campbell `B=6.8*10^19`, `G=1724` corollary

Campbell's 2026 square-interval paper records the operational computational input

\[
\operatorname{GAP}
(68{,}000{,}000{,}000{,}000{,}000{,}000,\ 1724).
\]

Set

\[
B=68{,}000{,}000{,}000{,}000{,}000{,}000,
\qquad
G=1724.
\]

Exact integer evaluation of

\[
F(K)=B(2K+1-G^2)-GK^2
\]

gives

\[
F(1{,}486{,}087)
=-68{,}003{,}807{,}375{,}681{,}384{,}956<0,
\]

\[
F(1{,}486{,}088)
=67{,}996{,}192{,}619{,}194{,}585{,}344>0,
\]

\[
F(78{,}886{,}310{,}903{,}386{,}302)
=39{,}597{,}120{,}694{,}510{,}508{,}304>0,
\]

and

\[
F(78{,}886{,}310{,}903{,}386{,}303)
=-96{,}402{,}879{,}300{,}365{,}462{,}716<0.
\]

The selector-origin condition also holds throughout this interval. At the lower endpoint,

\[
\frac{2K+1}{G}-G=\frac1{1724}>0,
\]

while at the upper endpoint it is less than

\[
91{,}515{,}441{,}881{,}555
\ll B.
\]

Therefore, under Campbell's declared operational gap input,

\[
\boxed{
1{,}486{,}088
\le K\le
78{,}886{,}310{,}903{,}386{,}302
}
\]

implies that `(K^2,(K+1)^2)` contains a semiprime.

Campbell also consumes the Sorenson–Webster finite verification that the interval contains a prime for every

\[
K\le7.05\times10^{13}.
\]

Those ranges overlap. Hence, under the same declared external computational inputs,

\[
\boxed{
\forall\,1\le K\le
78{,}886{,}310{,}903{,}386{,}302,
\quad
(K^2,(K+1)^2)
\text{ contains a prime or semiprime.}
}
\]

This is a conditional finite theorem: the transfer proof and endpoints are exact, while the large prime-gap and finite Legendre/Oppermann statements remain external computational premises.

---

## 6. Quantitative extension over Campbell's direct finite P2 lemma

Campbell's direct finite P2 lemma covers `K^2<=10^31`, whose largest integer root is

\[
K_C=3{,}162{,}277{,}660{,}168{,}379.
\]

The recycled-gap endpoint is larger by the factor

\[
\frac{78{,}886{,}310{,}903{,}386{,}302}{K_C}
=24.9460\ldots.
\]

At the level of the square parameter, the new endpoint satisfies

\[
K^2
=6{,}223{,}050{,}047{,}945{,}724{,}554{,}758{,}050{,}641{,}235{,}204,
\]

which is about

\[
622.305
\]

times `10^31`.

No stronger external prime-gap theorem has been inserted. The gain comes solely from using the same finite gap information first on the selector scale and then on the cofactor scale.

---

## 7. P2-R09 — Near-optimality inside the one-global-gap construction

Suppose the only cofactor information available is `GAP(B,G)`, and one wants to certify a product by choosing a prime `p` and then taking the first guaranteed prime after `K^2/p`.

Two inequalities are structurally necessary for that construction:

1. the cofactor query must remain below the verified range:
   \[
   p>\frac{K^2}{B};
   \]
2. the guaranteed gap must fit inside the square window:
   \[
   p<\frac{2K+1}{G}.
   \]

Thus the feasible selector window is

\[
\boxed{
\frac{K^2}{B}<p<\frac{2K+1}{G}.
}
\]

It can be nonempty only if

\[
\boxed{
B(2K+1)>GK^2.
}
\]

For the Campbell constants, the largest integer satisfying this necessary feasibility inequality is

\[
\boxed{
K_{\mathrm{feas}}
=78{,}886{,}310{,}904{,}872{,}390.
}
\]

The uniform two-stage theorem stops at

\[
K_{\mathrm{uniform}}
=78{,}886{,}310{,}903{,}386{,}302,
\]

only

\[
K_{\mathrm{feas}}-K_{\mathrm{uniform}}
=1{,}486{,}088
\]

below this method-specific ceiling.

This is not an impossibility theorem for P2 itself. It says the recycled single global gap constant is already nearly saturated; further progress from the same finite data should target the very short selector-prime range near

\[
p\asymp9.1515\times10^{13}
\]

with a sharper local selector-gap certificate.

---

## 8. P2-R10 — Local-selector sharpening interface

P2-R06 already isolates the exact improvement mechanism. Keep the global cofactor data

\[
(B_q,G_q)=(6.8\times10^{19},1724),
\]

but replace the selector constant `G_p=1724` by a certified local value `G_p^*` on the relevant selector-origin interval. The sufficient inequality becomes

\[
\boxed{
B_q(2K+1-1724G_p^*)>1724K^2.
}
\]

Every unit saved in `G_p^*` moves the upper root toward the feasibility ceiling. This reduces the remaining finite task to a narrow, ordinary prime-gap certificate around the selector scale; it does not require another sieve theorem.

A discovery scan suggests that this local gap may be far smaller than 1724, but no large local selector certificate is promoted in this note. It must be independently generated and checked before changing the proved endpoint.

---

## 9. Executable evidence boundary

The companion experiment

`experiments/p017_p2_two_stage_gap_recycling.py`

performs three tasks:

1. verifies all large integer endpoint inequalities exactly;
2. proves a self-contained small operational gap input by an exact sieve through `B_s=5,000,000`, obtaining `G_s=154`;
3. constructs the two primes for every integer
   \[
   15{,}611\le K\le49{,}324
   \]
   in that small model and checks
   \[
   K^2<pq<(K+1)^2.
   \]

The small computation validates the complete mechanism but is not evidence for the large external gap premise.

---

## 10. Current route consequence

The P017 P2 line now splits cleanly:

- **finite range:** the same explicit prime-gap input can be recycled twice, yielding a much larger exact conditional finite P2 theorem without bilinear remainder analysis;
- **beyond the finite gap ceiling:** P2-R03 still identifies the asymptotic carry remainder with the classical Chen floor remainder;
- **near the finite ceiling:** only a narrow selector-prime gap certificate is needed to approach the method-specific maximum.

The highest-value next step is therefore finite and concrete: certify the local selector gap near `9.1515*10^13`, then replay P2-R06 with separate `G_p` and `G_q`. The generic Chen bilinear problem remains relevant only after this finite route is exhausted.
