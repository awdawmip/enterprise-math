# P025 Supplement 05 — Closed Prime-Support Formula for the Absorption Floor

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplement 04, Pasten arithmetic derivatives, elementary prime valuations  
Hard block: `NONE`

## 1. Goal

Supplement 04 identified the exact minimum Wronskian absorption redundancy

\[
\eta_{\min}
=
\frac{\operatorname{cont}(\widehat\alpha\wedge\beta_{\rm raw})}
{M},
\qquad
M=\frac{abc}{\operatorname{rad}(abc)},
\]

where `alpha_hat` is the primitive additive-relation row and `beta_raw` is the canonically scaled arithmetic-Wronskian row.

That formula is exact, but it is still written in lattice/exterior language. The present supplement removes that layer entirely and expresses the same invariant directly from the prime-support partition and valuation exponents of `a,b,c`.

No abc-conjecture assumption is used.

## 2. Raw additive row and its content

Let

\[
a+b=c,\qquad \gcd(a,b)=1,
\]

and write

\[
e_p=v_p(abc).
\]

Because `a,b,c` are pairwise coprime, every prime belongs to exactly one of the three support blocks

\[
S_a,\quad S_b,\quad S_c.
\]

The raw additive row from Pasten's condition

\[
d(a)+d(b)=d(c)
\]

has coordinates

\[
\alpha^{(0)}_p=
\begin{cases}
 a\,v_p(a)/p,&p\in S_a,\\
 b\,v_p(b)/p,&p\in S_b,\\
 -c\,v_p(c)/p,&p\in S_c.
\end{cases}
\]

Let

\[
\boxed{
g=\gcd_{p\mid abc}|\alpha^{(0)}_p|.}
\]

Then

\[
\widehat\alpha=\alpha^{(0)}/g.
\]

Let

\[
R=\operatorname{rad}(abc).
\]

## 3. P025-T15 — closed cross-support formula

For primes `p,q` belonging to **different** support blocks among `S_a,S_b,S_c`, define

\[
\boxed{
K_{p,q}
=
\frac{R\,e_p e_q}{g\,p q}.
}
\]

Then every `K_(p,q)` is a positive integer and

\[
\boxed{
\eta_{\min}(a,b,c)
=
\gcd_{
\substack{p,q\mid abc\\
\text{different support blocks}}}
K_{p,q}.
}
\]

Thus the minimum possible Wronskian absorption redundancy is computable from finite factorization data alone; no witness enumeration and no lattice reduction are required.

### Proof

The canonically scaled Wronskian row is

\[
(\beta_{\rm raw})_p=
\begin{cases}
-b\,\alpha^{(0)}_p,&p\in S_a,\\
 a\,\alpha^{(0)}_p,&p\in S_b,\\
0,&p\in S_c.
\end{cases}
\]

Consider a `2x2` minor of the two-row matrix

\[
[\widehat\alpha;\beta_{\rm raw}].
\]

If `p,q` belong to the same support block, the two column restrictions are proportional, so the minor is zero.

If they belong to different support blocks, direct substitution gives, up to sign,

\[
\left|
\widehat\alpha_p\beta_q
-
\widehat\alpha_q\beta_p
\right|
=
\frac{abc\,e_p e_q}{g\,p q}.
\]

Supplement 04 proved that the content of all these minors is exactly the positive generator of the Wronskian image on the additive witness lattice. Since

\[
M=abc/R,
\]

dividing each non-zero minor by `M` gives exactly

\[
K_{p,q}
=
\frac{R e_p e_q}{g p q}.
\]

P025-T11 ensures `M` divides every Wronskian value and hence every image generator/minor content, so these normalized terms are integers. Taking their gcd gives `eta_min`. ∎

## 4. Exact classification of perfect absorption

P025-T15 immediately yields

\[
\boxed{
\eta_{\min}=1
\iff
\gcd_{\text{cross-block }p,q}
\frac{R e_p e_q}{g p q}=1.
}
\]

This is a complete finite arithmetic criterion for the existence of a witness with

\[
|W|=M.
\]

It is not yet a simple one-line structural classification for all abc triples, but it removes all witness variables from the question.

## 5. P025-T16 — squarefree primitive triples have perfect absorption

Assume at least two of the three support blocks are non-empty and every one of `a,b,c` is squarefree (with `1` allowed as the empty squarefree support). Then

\[
\boxed{
\eta_{\min}(a,b,c)=1.
}
\]

### Proof

All valuation exponents are one.

First, `g=1`. Indeed, for any non-unit squarefree support block with integer `n`, its raw-row coefficients are, up to sign,

\[
\{n/p:p\mid n\}.
\]

Their gcd is one: for every prime `r|n`, the coefficient `n/r` is not divisible by `r`. Hence the gcd of the entire additive row is one.

P025-T15 therefore reduces to

\[
K_{p,q}=R/(pq)
\]

for cross-block pairs.

Every prime `r|R` lies in some non-empty block. Because another support block is non-empty, choose a cross pair containing `r`; the corresponding `R/(rq)` is not divisible by `r`. Thus no prime dividing `R` divides all cross terms. Since every cross term divides `R`, their gcd is one. ∎

### Interpretation

Squarefree support carries no repeated prime multiplicity, but this theorem is stronger than the tautology `M=1`: it says the relation-adapted Wronskian lattice actually attains its smallest possible non-zero arithmetic scale.

## 6. P025-T17 — one plus squarefree equals a prime power

Let

\[
1+b=p^m,
\]

where `p` is prime, `m>=1`, and `b>1` is squarefree. Then

\[
\boxed{
\eta_{\min}(1,b,p^m)=m.
}
\]

### Proof

The squarefree `b`-block already forces additive-row content `g=1`.

Let

\[
B=\operatorname{rad}(b)=b.
\]

Then

\[
R=pB.
\]

Every non-zero cross term pairs `p` with a prime `q|b`, and P025-T15 gives

\[
K_{q,p}
=
\frac{pB\cdot1\cdot m}{q p}
=m\frac{B}{q}.
\]

The gcd of the integers `B/q` over `q|B` is one. Hence the gcd of all `K_(q,p)` is exactly `m`. ∎

### Examples

\[
1+3=4\quad\Rightarrow\quad\eta_{\min}=2,
\]

\[
1+7=8\quad\Rightarrow\quad\eta_{\min}=3,
\]

\[
1+15=16\quad\Rightarrow\quad\eta_{\min}=4,
\]

\[
1+31=32\quad\Rightarrow\quad\eta_{\min}=5.
\]

Thus repeated multiplicity on one support block can create an **irreducible Wronskian absorption overhead** even though the opposite non-unit term is entirely squarefree.

This is not an existence theorem asserting infinitely many squarefree values `p^m-1`; it is a conditional exact formula for every triple satisfying the stated hypotheses.

## 7. P025-T18 — two prime-power support blocks

Suppose an actual primitive relation has the form

\[
1+p^m=q^n,
\]

with distinct primes `p,q` and positive integers `m,n`.

There are only two prime coordinates. The raw additive row is

\[
\left(
 m p^{m-1},
 -n q^{n-1}
\right),
\]

so let

\[
g=\gcd\left(m p^{m-1},n q^{n-1}\right).
\]

P025-T15 gives the exact formula

\[
\boxed{
\eta_{\min}
=
\frac{mn}{g}.
}
\]

Consequently

\[
\boxed{
\eta_{\min}=1
\iff
n\mid p^{m-1}
\quad\text{and}\quad
m\mid q^{n-1}.
}
\]

The forward implication follows because `eta_min=1` means `g=mn`; the reverse follows because the two divisibilities make both raw coefficients divisible by `mn`, while the exact integer formula forces `g|mn`.

### Catalan/Mihăilescu working example

For

\[
1+2^3=3^2,
\]

we have

\[
g=\gcd(12,6)=6=mn,
\]

so

\[
\eta_{\min}=1.
\]

The use of this classical numerical identity here is only as a structural sample; P025 makes no new statement about Catalan's theorem.

## 8. What this says about radical collapse

Supplement 04 separated witness search radius from absorption redundancy. P025-T15 now shows that the second axis is not mysterious hidden lattice information: it is already encoded by

\[
\boxed{
\text{support partition}
+
\text{valuation exponents}
+
\text{additive-row content}.
}
\]

So there are now three distinct compression levels:

1. **radical support only** — remembers which primes occur;
2. **support + valuation structure** — enough to compute the exact absorption floor `eta_min`;
3. **full normed witness generator** — needed for the search-radius / Pareto tradeoff structure.

This is a concrete refinement of the slogan “multiplicity matters”: not all multiplicity information has to be retained equally for every future certificate query.

## 9. High-quality examples do not collapse the new axis

The following previously used high-quality examples all happen to have perfect absorption:

\[
1+8=9,
\]

\[
1+4374=4375,
\]

\[
2+3^{10}\cdot109=23^5.
\]

For each, P025-T15 gives

\[
\eta_{\min}=1.
\]

This is a finite structural observation only. It does **not** show that high abc quality implies perfect absorption, and no such conjecture is adopted here without a separate search for counterexamples and asymptotic evidence.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_absorption_formula.py`
  - raw additive relation row and content;
  - exact cross-block normalized minor list;
  - closed support formula for `eta_min`;
  - squarefree perfect-absorption verifier;
  - `1 + squarefree = prime power` specialization;
  - two-prime-power-block formula and perfect-absorption criterion.
- `tests/test_abc_absorption_formula.py`
  - exact worked examples;
  - exhaustive agreement of support formula and exterior/determinantal formula for every primitive triple with `c<100`;
  - squarefree family samples;
  - prime-power family samples;
  - previously used high-quality triples.

The `c<100` exhaustive check validates the implementation. The proofs above establish the formulas for all triples in the stated domains.

## 11. Prior-art boundary

Pasten explicitly supplies the arithmetic derivative, the selected additive relation and the arithmetic Wronskian formula [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]. Determinantal divisors and primitive integer kernels are standard algebra.

The focused source search performed during this stage did not establish historical priority for the normalized invariant `eta_min`, the support formula above, or these particular family classifications. Therefore all of them remain

`NOVELTY_UNVERIFIED`.

Absence from this focused search is not evidence of originality.

## 12. Next frontier

There is no hard block. Continue with:

1. derive the `l`-adic valuation formula for `eta_min`, converting the gcd criterion into local prime-by-prime obstruction data;
2. classify which multiplicity patterns force `eta_min>1` and which allow `eta_min=1`;
3. search explicitly for high-quality triples with `eta_min>1`, because one counterexample would kill any naive quality/perfect-absorption implication;
4. compare `eta_min` with the full Pareto frontier and isolate when absorption obstruction, rather than search radius, is the active certificate bottleneck;
5. reread Pasten's Geometry-of-Numbers argument against the new local obstruction coordinates before making any novelty claim.
