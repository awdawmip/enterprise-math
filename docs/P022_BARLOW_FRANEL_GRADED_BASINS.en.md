# P022 — Graded Franel p-adic Basins from Zero Digits

Status: `ACTIVE RESEARCH NOTE / PRIOR-ART VALUATION THEOREM + NEW P022 SPECIALIZATION`  
Owner: `program/p022-geometry-v2`  
Depends on: Delaygue valuation theorem for Apéry-like sequences; Franel p-Lucas zero-digit basin; half-index witness family  
Cross-route relevance: P011 collision precision; P018/P023 graded repair; P024 task-relative observation depth

## 1. Prior-art theorem now confirmed to apply to Franel numbers

Let

\[
F_N=\sum_{k=0}^{N}\binom Nk^3.
\]

For a prime `p`, define

\[
Z_p=\{1\le d\le p-1:p\mid F_d\}
\]

and let

\[
\alpha_p(F,N)
\]

be the number of base-`p` digits of `N` which belong to `Z_p`.

Eric Delaygue's Theorem 1 in *Arithmetic properties of Apéry-like numbers* proves a Kummer-type lower bound for the Apéry-like multisums to which the theorem applies.  His application table explicitly includes the Franel sequence

\[
\sum_k\binom nk^3,
\]

with factorial-ratio multisum

\[
\frac{(n_1+n_2)!^3}{n_1!^3n_2!^3},
\]

and the associated differential operator is among the type-I cases.  Consequently the theorem gives, for every prime `p` and every `N`,

\[
\boxed{
v_p(F_N)\ge \alpha_p(F,N).
}
\]

This valuation theorem is **prior art**.  P022 does not claim it.

What is new in the present route is its combination with the already derived Franel zero-digit geometry, forced midpoint family, and task-relative precision interpretation.

Reference: É. Delaygue, *Arithmetic properties of Apéry-like numbers*, Compositio Math. 154 (2018), 249--274, Theorem 1 and the application table containing Franel numbers; arXiv:1310.4131v2.

---

## 2. P022-LI20 — exact distribution of the guaranteed valuation depth

Let

\[
z_p=|Z_p|.
\]

On the complete digit block

\[
0\le N<p^L,
\]

the `L` base-`p` positions are independent combinatorial choices.  Exactly `z_p` digits are zero digits and `p-z_p` are nonzero digits.

Therefore the number of indices with

\[
\alpha_p(F,N)=j
\]

is exactly

\[
\boxed{
C_{p,L}(j)
=
\binom Lj z_p^j(p-z_p)^{L-j}.
}
\]

The profile sums to the full block:

\[
\sum_{j=0}^{L}C_{p,L}(j)=p^L.
\]

Delaygue's theorem now gives the finite certificate

\[
\boxed{
\#\{0\le N<p^L:v_p(F_N)\ge r\}
\ge
\sum_{j=r}^{L}C_{p,L}(j).
}
\]

The inequality rather than equality is essential: Franel values can have more `p`-adic divisibility than the digit lower bound predicts.

---

## 3. P022-LI21 — average guaranteed p-adic depth

Summing the exact binomial profile gives

\[
\sum_{0\le N<p^L}\alpha_p(F,N)
=
Lz_p p^{L-1}.
\]

Therefore

\[
\boxed{
\frac1{p^L}
\sum_{0\le N<p^L}v_p(F_N)
\ge
\frac{Lz_p}{p}.
}
\]

So once `Z_p` is nonempty, the average `p`-adic depth grows at least linearly in the base-`p` digit horizon `L`.

Since `L` is logarithmic in the numerical scale of the index, this is a concrete example where a finite digit-state alphabet forces increasing arithmetic precision at larger horizons.

---

## 4. P022-LI22 — counting-typical depth is linear in digit horizon

Under uniform counting on `0,...,p^L-1`, the exact lower-bound state

\[
\alpha_p(F,N)
\]

has binomial mean and variance

\[
\mathbb E\alpha
=
L\frac{z_p}{p},
\]

\[
\operatorname{Var}(\alpha)
=
L\frac{z_p}{p}
\left(1-\frac{z_p}{p}\right).
\]

Hence, for every fixed

\[
0<\varepsilon<\frac{z_p}{p},
\]

Chebyshev's inequality gives a completely explicit finite bound

\[
\frac{
\#\{N<p^L:\alpha_p(F,N)<(z_p/p-\varepsilon)L\}
}{p^L}
\le
\frac{z_p(p-z_p)}{\varepsilon^2p^2L}.
\]

Since `v_p(F_N)>=alpha_p(F,N)`, it follows that

\[
\boxed{
\frac{
\#\{N<p^L:v_p(F_N)\ge(z_p/p-\varepsilon)L\}
}{p^L}
\longrightarrow1.
}
\]

Thus the density-one divisibility basin is actually **graded**: counting-typical Franel indices carry a `p`-adic valuation lower bound proportional to digit depth.

No claim is made that the true valuation divided by `L` converges to `z_p/p`; this is a lower-bound statement.

---

## 5. P022-LI23 — repeated midpoint digits produce an exact valuation tower

Assume

\[
p\equiv5,7\pmod8.
\]

The half-index theorem proves that

\[
m=\frac{p-1}{2}\in Z_p.
\]

For `L>=1`, define

\[
N_L
=
m(1+p+\cdots+p^{L-1}).
\]

Since

\[
m=\frac{p-1}{2},
\]

we obtain the closed form

\[
\boxed{
N_L=\frac{p^L-1}{2}.
}
\]

Its base-`p` expansion consists of `L` copies of the zero digit `m`, so

\[
\alpha_p(F,N_L)=L.
\]

Delaygue's theorem therefore gives the infinite tower

\[
\boxed{
v_p\!\left(F_{(p^L-1)/2}\right)\ge L
\qquad(L\ge1).}
\]

Equivalently,

\[
\boxed{
p^L\mid F_{(p^L-1)/2}.}
\]

This is stronger than repeating a mod-`p` Lucas congruence: the guaranteed valuation increases by one for every repeated zero digit.

---

## 6. P022-LI24 — an infinite graded tower inside the composite A-boundary regime

Now take

\[
p>5,
\qquad
p\equiv5\ \text{or}\ 23\pmod{24}.
\]

For every **odd** `L>=1`, let

\[
N_L=\frac{p^L-1}{2}.
\]

The corresponding A-boundary is

\[
2N_L-1=p^L-2.
\]

Because

\[
p\equiv-1\pmod3
\]

and `L` is odd,

\[
p^L-2\equiv-1-2\equiv0\pmod3.
\]

For `p>5` this boundary exceeds `3`, hence is composite.  Therefore the forced half-index family lifts to an infinite **graded composite-boundary tower**:

\[
\boxed{
2N_L-1\text{ composite},
\qquad
v_p(F_{N_L})\ge L
\quad(L\text{ odd}).}
\]

This does not yet determine the pure defect valuation `v_p(D_(N_L))`, because the canonical A-elimination at the large index may itself involve older Franel factors divisible by `p`.

That distinction is the same support-cancellation boundary already isolated at level `L=1`.

---

## 7. Precision interpretation

The p-Lucas theorem gave a Boolean finite-state language:

\[
\text{does a base-p word contain a zero digit?}
\]

Delaygue's valuation theorem upgrades it to a graded language:

\[
\boxed{
\text{how many zero digits does the word contain?}
}
\]

Each zero digit guarantees one additional unit of `p`-adic depth.

Thus the finite sufficient state for the lower-bound future language is not the full integer `F_N`, but the count of visits to a finite zero-digit alphabet.

This is structurally parallel to the event-driven Barlow repair theorem:

- wall encounters accumulate repair dimension;
- zero-digit encounters accumulate guaranteed `p`-adic valuation.

Both are examples of **event-counted precision rather than clock-counted precision**.

The generic abstraction, if promoted, belongs to A2/P023/P024.  P022 owns only this Franel/geometry specialization.

---

## 8. Boundary with the half-defect conjecture

The graded theorem does **not** prove the current one-unit half-defect conjecture

\[
v_p(D_{(p-1)/2})=1.
\]

At one digit it gives only

\[
v_p(F_{(p-1)/2})\ge1.
\]

The exact defect still requires two independent ingredients already isolated by P022:

1. the canonical A-elimination support must avoid earlier Franel zero digits;
2. the midpoint zero must be simple modulo `p^2`.

Delaygue resolves neither upper bound automatically.

So LI20--LI24 substantially strengthen the infinite arithmetic side without erasing the genuine Franel--Wieferich/support-avoidance frontier.

---

## 9. Prior-art / novelty boundary

Prior art:

- Delaygue's Kummer-type valuation lower bound for the Franel sequence;
- p-Lucas structure and standard binomial counting/probability identities.

P022-specific consequences:

- exact guaranteed valuation-depth distribution over complete base-`p` blocks;
- average and density-one graded-depth interpretation;
- the repeated-half-index tower `N_L=(p^L-1)/2`;
- its odd-level specialization to the composite A-boundary family `p=5,23 mod 24`;
- the precision-language interpretation connecting zero-digit events to graded repair depth.

Historical novelty of these consequences as packaged here remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_graded_basin.py`;
- `tests/test_p022_barlow_franel_graded_basin.py`.

The code computes the exact `alpha` profile, guaranteed valuation tails, average lower bound, repeated midpoint indices, and odd-level composite-boundary tower entirely with integer arithmetic.  Short-horizon tests compare Delaygue's lower bound against exact Franel integers.
