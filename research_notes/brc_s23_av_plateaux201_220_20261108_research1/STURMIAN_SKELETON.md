# Sturmian candidate-staircase theorem for the S23/AV auxiliary observer

Date: 2026-11-08 (Asia/Shanghai). Status: **proved algebraic/combinatorial lemma** and exact-rational implementation checks; independent review pending. The claims about the *candidate sequences* below hold for every integer index, while equality of the candidate `M_i` with the actual observation capacity `N(h)` has a **separately certified finite range** (through i=220 as documented in `PROOF.md`).

## Definitions

Use the frozen two-point auxiliary model at source pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`, and put

```
r = log(7)/log(10/7)
eps = 79*r - 431
d = 2074774 - 380295*r
alpha = d/eps
a_i = floor(i*alpha) for integers i>=0, a_0=0
e_i = a_i-a_(i-1) for integers i>=1
V_i = 380295*i + 79*a_i
K_i = 2074774*i + 431*a_i
H_i = V_i + 510
M_i = K_i + V_i - (V_(i-1)+1) for i>=1
```

Here `H_i,M_i` are the **candidate** endpoint and required capacity values. No theorem about `N(H_i)=M_i` for arbitrary i is assumed.

## Theorem (global candidate-plateau combinatorics)

(1) `alpha` is irrational and `1/2<alpha<2/3`. The increments `e_i` are 0 or 1, with **no consecutive 00** and **no consecutive 111**. The sequence of `e_i` is not eventually periodic.

(2) For every `i>=1`:

```
H_i = 380295*i + 79*a_i + 510
M_i = 2074774*i + 380294 + 431*a_i + 79*e_i
```

Thus the candidate interval width `H_i-H_(i-1)` is `380295` or `380374` for `i>=2`. For `i>=2` the jump `M_i-M_(i-1)` is **exactly one of**

```
2,074,695 for (e_(i-1),e_i)=(1,0)
2,075,284 for (e_(i-1),e_i)=(0,1)
2,075,205 for (e_(i-1),e_i)=(1,1)
```

(The impossible pair is (0,0).)

(3) The asymptotic frequencies of candidate short/long intervals are `1-alpha` and `alpha`, respectively. For consecutive candidate capacity jumps, the asymptotic frequencies of the above three values are `1-alpha`, `1-alpha`, and `2*alpha-1`, respectively.

(4) There is an **exact two-strip identity** for every `i>=1`:

```
M_i - r*H_i = 380294 - 510*r + 79*e_i + eps*{i*alpha},
```

where braces denote fractional part. In particular, the candidate endpoints have the asymptotic slope

```
lim_(i->infinity) M_i/H_i
 = (2074774+431*alpha)/(380295+79*alpha) = r.
```

## Proof

The strict 45-term atanh rational bounds inherited from `VERIFY_PLATEAUX20_200.py` certify `LO/Q<r<(LO+1)/Q`, with `Q=10^26`, `LO=545569623581288298975349314`. Consequently the following integer bounds are certified:

```
Q*eps lies strictly between
  EL=262921775619052595806 and EU=262921775619052595885
Q*d lies strictly between
  DL=153966341169532252075 and DU=153966341169532632370
2*DL>EU, 3*DU<2*EL, 0<EL<EU, 0<DL<DU.
```

They imply `1/2<d/eps<2/3` with strict rational arithmetic. Were `r=p/q>0` rational, `7^q=(10/7)^p` would imply `7^(p+q)=10^p`, violating unique prime factorization. If `alpha` were rational, `r=(2074774+431*alpha)/(380295+79*alpha)` would also be rational. Hence alpha is irrational.

Since `0<alpha<1`, `e_i` belongs to {0,1}. For every real x, `floor(x+2*alpha)-floor(x)>=1` because `2*alpha>1`, excluding 00 in consecutive increments. Similarly `floor(x+3*alpha)-floor(x)<=2` because `3*alpha<2`, excluding 111. An eventually periodic binary increment sequence would give a rational limit for `a_i/i`, contradicting `a_i/i -> alpha`.

Substitute the definitions to obtain `V_i-V_(i-1)=380295+79*e_i` and the asserted formula for M_i. Subtraction gives `M_i-M_(i-1)=2074774+431*e_i+79*(e_i-e_(i-1))`, and the three allowed pairs give exactly the three stated numbers.

The empirical frequency of ones is `a_n/n -> alpha`, since `a_n=floor(n alpha)`. Zeros have frequency `1-alpha`. Since 00 is excluded, zeros (up to endpoint effects of O(1)) correspond bijectively to (0,1) and (1,0) transitions; their frequencies are each `1-alpha`. Remaining pairs are (1,1), with frequency `2alpha-1`.

Finally `2074774*79 - 431*380295 = 1`, so the algebraic identity `2074774+431*alpha = r*(380295+79*alpha)` follows directly from `alpha=(2074774-380295*r)/(79*r-431)`. Using `a_i=i alpha-{i alpha}`, direct subtraction yields the exact two-strip identity. The fractional term is bounded `0<=eps*{i alpha}<eps`, and all non-leading terms are O(1), proving the slope claim.

## Verified tests, application, and next question

`VERIFY_SKELETON.py` checks the four strict integer inequalities on certified log bounds; all candidate index identities and forbidden increment patterns for `i=1,...,10000`; representative strict residual strips for i=1,2,20,201,220,10000; and the special i=201 and i=220 endpoints. Actual output is `RUN_SKELETON.txt`.

For the already **independently finite-certified** indices `201<=i<=220`, the candidate M_i is indeed `N(h)` on the corresponding observation interval, so this lemma gives a proved description of the lengths and jump patterns inside that finite block.

Open: prove the endpoint coverage proposition uniformly for an infinite family of i, or locate its first counterexample. Efficient random access to a_i must certify `floor(i alpha)` at the requested bit precision; a fixed-width numerical approximation is not enough for arbitrary i. Preserve the distinct mother six-source lawful-observation bridge task and P000 native X6 assumptions.
