# PREFIX-692-R6 — 严格嵌套的BRC方差符号域与两条有序极端交叉前沿

Date: 2026-11-11 (Asia/Shanghai). Mode: independent TASK_RESEARCH author derivation.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Status: `AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Precise object and upstream evidence

For the frozen 189-level joint-clock BRC stopping-time observer retain the two separately labelled readouts `(z,z)` and `(0,z)`. Define their mean/variance differences
[
A(z)=\mathrm{Var}(Y(z,z))-\mathrm{Var}(Y(0,z)),\qquad
B(z)=E[Y(z,z)]-E[Y(0,z)],\qquad
F_q(z)=qA(z)-B(z).
]
The sampled-variance difference equals `q F_q(z)` for `q>0`, so `F_q=0` is precisely its crossover equation. Keep the branch labels, joint-clock and moment observer; no physical native-orbit transfer is inferred.

The spatial bridge and continuous parameter interval are
[
L=0.0528706,\quad R=0.0530659,\quad
q_-={63055771\over5256000},\quad
q_+={660614143\over27500000}.
]
PREFIX-690 (`e1394a13ec0627a579db9414242a3633b773304e`, paper and `PREFIX690_R6_AFFINE_BRIDGE_CERTIFICATE.py`) establishes the **strict** endpoint signs `F_q(L)>0>F_q(R)` for every real `q\in[q_-,q_+]`. PREFIX-680 (`2c91711f60aa74d93880780929f532da24140ec0`) gives at `b=53/1000` the half-open exact rational derivative intervals
[
\frac{J_j}{10^8}\le B^{(j)}(b)<\frac{J_j+1}{10^8}\quad(j=0,1,2),
\qquad(J_0,J_1,J_2)=(789752024,12845959424,-99127959112),
]
and the certified global bound `|B'''|≤69527880576` on this bridge. This note proves consequences of these frozen prior certificates; it does not rerun the 189-level recurrence.

## 692.1 Exact certified positivity on the whole bridge

**Theorem.** For every `z\in[L,R]`,
[
\boxed{7.85<B(z)<7.95.}
]
For every `q\in[q_-,q_+]` and every `z\in[L,R]` with `F_q(z)=0`,
[
\boxed{A(z)=B(z)/q>{215875000\over660614143}>0.326.}
]

**Proof.** Put
[
T=\max(|L-b|,|R-b|)=647/5000000.
]
Taylor's theorem, the integer derivative floors, and `|B'''|\le M_3=69527880576` give the following rational enclosure even when `z-b<0`:
[
B(z)>\frac{789752024}{10^8}
-\frac{12845959425}{10^8}T
-\frac{99127959112}{10^8}\frac{T^2}{2}
-M_3\frac{T^3}{6}
=\frac{4909863349354430849559}{625000000000000000000}>7.85,
]
[
B(z)<\frac{789752025}{10^8}
+\frac{12845959425}{10^8}T
+\frac{99127959112}{10^8}\frac{T^2}{2}
+M_3\frac{T^3}{6}
=\frac{4962036956895569150441}{625000000000000000000}<7.95.
]
At any root, `qA(z)=B(z)>0`. Since `q\le q_+`, `A(z)>7.85/q_+=215875000/660614143`.

## 692.2 One-way sign change: nested positivity sets

For `q\in[q_-,q_+]` define the closed sign region `S_q=\{z\in[L,R]:F_q(z)\ge0\}`.

**Theorem.** For any `q_-\le q_1<q_2\le q_+`,
[
\boxed{S_{q_1}\subseteq\{z:F_{q_2}(z)>0\}\subseteq S_{q_2}.}
]

**Proof.** From `F_{q_1}(z)=q_1A(z)-B(z)\ge0` and `B(z)>0` one obtains `A(z)\ge B(z)/q_1>0`. Consequently
[
F_{q_2}(z)=F_{q_1}(z)+(q_2-q_1)A(z)>F_{q_1}(z)\ge0.
]
In particular at each fixed `z` the sign can cross from negative to nonnegative at most once as positive `q` increases; its positive-`q` crossing, if any, has the unique parameter `q=B(z)/A(z)`.

## 692.3 Ordered leftmost/rightmost roots without assuming uniqueness

Since `F_q(L)>0>F_q(R)`, each `F_q` has at least one root in `(L,R)`. The frozen finite observer makes `F_q` a polynomial; since endpoint signs are opposite it is not identically zero, and thus it has finitely many roots. Define
[
Z(q)=\{z\in(L,R):F_q(z)=0\},\qquad
\ell(q)=\min Z(q),\qquad r(q)=\max Z(q).
]

**Theorem.** For every `q_-\le q_1<q_2\le q_+`,
[
\boxed{\ell(q_1)<\ell(q_2),\qquad r(q_1)<r(q_2).}
]
The least-root function `\ell` is left-continuous on `(q_-,q_+]`; the greatest-root function `r` is right-continuous on `[q_-,q_+)`.

**Proof for the first root.** `F_{q_1}>0` on `[L,\ell(q_1))`, because there is no earlier root and `F_{q_1}(L)>0`. The nesting theorem gives `F_{q_2}>0` throughout this interval, and `F_{q_2}(\ell(q_1))=(q_2-q_1)A(\ell(q_1))>0`. The first root of `F_{q_2}` must therefore be strictly to the right.

**Proof for the last root.** At `r(q_1)`, `F_{q_2}(r(q_1))=(q_2-q_1)A(r(q_1))>0`; at `R`, `F_{q_2}(R)<0`. Thus there is a `q_2` root to the right of `r(q_1)`, giving strict order.

**One-sided continuity.** For `q_n\uparrow q`, `\ell(q_n)` increases to some `u\le\ell(q)`. Continuity of the polynomial in `(q,z)` gives `F_q(u)=0`; the endpoint signs exclude `u=L` or `u=R`. Minimality of `\ell(q)` forces `u=\ell(q)`. Analogously for `q_n\downarrow q`, `r(q_n)` decreases to a root `u\ge r(q)`, and maximality forces `u=r(q)`.

## 692.4 An explicit positive separation coefficient

Define the finite positive derivative envelope
[
M=\max_{q\in[q_-,q_+],\,z\in[L,R]}|\partial_zF_q(z)|.
]
For either `x=\ell` or `x=r` and any `q_1<q_2`, the root equations, the mean value theorem and theorem 692.1 imply
[
\boxed{x(q_2)-x(q_1)\ge
\frac{215875000}{660614143}\frac{q_2-q_1}{M}>0.}
]
For `\ell`: `F_{q_1}(\ell(q_2))=-(q_2-q_1)A(\ell(q_2))` and `F_{q_1}(\ell(q_1))=0`. For `r`: `F_{q_2}(r(q_1))=(q_2-q_1)A(r(q_1))` and `F_{q_2}(r(q_2))=0`. A future exact Bernstein derivative envelope would make `M` numerically sharp.

## Verification and continuation

The companion `PREFIX692_R6_ORDERED_EXTREMAL_FRONTIERS.py` uses only Python integers/`Fraction` and checks the full-range rational Taylor enclosure, inherited affine endpoint margins for the whole parameter band, and the exact root-`A` lower bound. Local equivalent rational replay returned `ALL_CHECKS_PASS PREFIX692-R6`; exact outputs are in `PREFIX692_R6_RESULTS.json`. The statements about ordered extrema and one-sided continuity are mathematical deductions proved above.

**BRC reuse resolution:** `REUSE_APPLIED` — retained the frozen joint-clock labelled moment/variance observer; the signed comparison is formed only after preserving its positive branch structure and two population labels. No new mechanism is claimed.

**Next discriminating unit:** decide whether `\ell(q)=r(q)` for `12\le q\le24` by a signed Bernstein derivative certificate `F'_q<0` on the full bridge or exact Sturm root count. Then integrate the result with PREFIX-675's boundary-versus-interior sampled-variance maximum objective.
