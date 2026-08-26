# P017 — Residual-Energy Fixed-Power Obstruction and Constant Pivot

Status: `PROVED_WIP FIXED-POWER OBSTRUCTION + ROOT-EDGE WEIGHT TRANSFER + EXPLICIT CONSTANT PIVOT / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_COLLISION_PACKET_COMPRESSION_20260824.md`;
- `docs/P017_P2_TERMINAL_PRIME_CORE_COLLAPSE_20260824.md`;
- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`;
- `docs/P017_P2_EXPLICIT_RECIPROCAL_SUM_LEMMA_20260825.md`;
- H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31 (1981), especially the weights on pp. 38–39 and Lemmas 2 and 4.

Purpose: settle the current route-selection question. We first ask whether the exact P017 square geometry can force a **uniform fixed-power saving** in the support size or positive quadratic energy of the residual distinct-prime sector. The answer is negative: an explicit moving-small-core family survives all exact reductions and has critical-scale support along an infinite sequence of square shells. We then pivot, as prescribed, to finite constant reduction and derive two exact assets: a root-edge packet-weight transfer and a dyadic `rho=2` reciprocal-sum package for the current `a=6,d=5/9` root-edge parameters.

This note does **not** say that signed Chen/Iwaniec bilinear cancellation is impossible. It says that a coefficient-uniform argument based only on shrinking the residual support or on bounding a positive quadratic energy by `K^(1-delta)` cannot be the missing step.

---

## 1. Frozen a6 root-edge data

Write

\[
X=K^2,
\qquad
\theta=\frac{4999}{10000},
\qquad
D=X^{5/9},
\]

and

\[
a=6,
\qquad
b=\frac{22}{5},
\qquad
c=\frac{27}{5}.
\]

Then

\[
D^{1/a}=X^{5/54}=K^{5/27},
\]

\[
D^{b/a}=X^{11/27}=K^{22/27},
\]

and

\[
D^{c/a}=X^{1/2}=K.
\]

The source denominator satisfies the special root-edge identity

\[
\boxed{2c-b-1=c=\frac{27}{5}.}
\]

Hence the last source weight on

\[
D^{b/a}\le p<D^{c/a}=K
\]

normalizes exactly to

\[
\boxed{
\gamma_K(p)
=\frac{c-a\log p/\log D}{2c-b-1}
=1-\frac{\log p}{\log K}.
}
\tag{1.1}
\]

The `W_1/W_2` split occurs at

\[
y=X^\theta=K^{2\theta}=K^{4999/5000}.
\]

Therefore

\[
D^{b/a}\le p<y
\quad\Longrightarrow\quad
\boxed{\frac1{5000}<\gamma_K(p)\le\frac5{27}},
\tag{1.2}
\]

while the special two-dimensional Selberg tail

\[
y\le p<K
\]

has

\[
\boxed{0\le\gamma_K(p)\le\frac1{5000}.}
\tag{1.3}
\]

The upper bound in (1.3) is exactly the terminal weight printed by Iwaniec–Laborde,

\[
1-\frac{\log p}{\log w},
\qquad w=K.
\]

---

## 2. P2-R20 — A fixed-core collision slice with no exact Möbius cancellation

Start with the simplest prime small core

\[
d_1=d_2=5,
\qquad
\ell=5,
\qquad
t=3.
\]

Then

\[
1<t<(d_1,d_2)=5,
\]

and every pair of distinct odd primes `p_1,p_2` satisfying

\[
K^2<15p_1p_2<(K+1)^2
\tag{2.1}
\]

and

\[
\frac{K+1}{5}<p_i<\frac{K+1}{3}
\tag{2.2}
\]

produces a legitimate distinct-prime super-root collision with

\[
m_i=5p_i,
\qquad
n=15p_1p_2.
\]

For this packet

\[
R_i=\frac{K+1}{p_i}<5.
\]

Since the only divisor of `ell=5` strictly below `R_i` that can occur in the exact cover formula is `1`, two such small divisors cannot have lcm `5`. The correction term in P2-R16 is empty. Thus

\[
\boxed{
\mathcal C_5^{p_1,p_2}(K)=-\mu(5)=1.
}
\tag{2.3}
\]

So this slice is not removed by exact Möbius core collapse.

A convenient narrower band is

\[
\frac K4<p_i<\frac{4K}{15}.
\tag{2.4}
\]

For all sufficiently large `K`, (2.4) implies (2.2). On a realized collision the super-root carry is `1`, hence its centered value is

\[
O_{5p_i}(K)-\frac{K}{5p_i}
=1-\frac{K}{5p_i}.
\]

The band (2.4) gives the strict bounds

\[
\boxed{
\frac15
<1-\frac{K}{5p_i}
<\frac14.
}
\tag{2.5}
\]

Therefore neither exact Möbius summation nor centering kills this sector.

This fixed-core example is already a useful finite diagnostic. The next theorem strengthens it into a genuine asymptotic obstruction inside the actual `W_1` sector.

---

## 3. P2-R21 — Moving-small-core W1 obstruction

The preceding fixed core eventually moves into `W_2` because `p_i` is a fixed positive fraction of `K`. To test the actual `W_1` residual, let the common small prime grow extremely slowly.

Fix any sufficiently small constant relative box width `0<eps_0<1/100`, and let `R` tend to infinity. Put

\[
Q_R=R^{1/2000}.
\]

Choose

\[
q\in[Q_R,(1+\varepsilon_0)Q_R]
\]

prime, and choose distinct primes

\[
p_1,p_2\in[R,(1+\varepsilon_0)R].
\]

Set

\[
d_1=d_2=q,
\qquad
\ell=q,
\qquad
t=3,
\]

and

\[
n=3qp_1p_2,
\qquad
K=\lfloor\sqrt n\rfloor.
\tag{3.1}
\]

Because `n` is not a square for all sufficiently large choices, it lies in the unique square shell

\[
K^2<n<(K+1)^2.
\]

Moreover

\[
K\asymp R^{1+1/4000}.
\]

Consequently

\[
\frac{\log p_i}{\log K}
\longrightarrow
\frac{1}{1+1/4000}
=\boxed{\frac{4000}{4001}},
\tag{3.2}
\]

and

\[
\frac{\log q}{\log K}
\longrightarrow
\frac{1/2000}{1+1/4000}
=\boxed{\frac2{4001}}.
\tag{3.3}
\]

These limiting exponents satisfy

\[
\frac{22}{27}
<
\frac{4000}{4001}
<
\frac{4999}{5000},
\tag{3.4}
\]

and

\[
\frac2{4001}<\frac5{27}.
\tag{3.5}
\]

Therefore, for all sufficiently large `R`, every tuple in the box has

\[
q<z=K^{5/27},
\]

and

\[
D^{b/a}=K^{22/27}<p_i<y=K^{4999/5000}.
\]

Thus the outer primes lie in the **actual `W_1` part of the root-edge T4 weight**, not in the Selberg `W_2` tail.

Also

\[
\frac{qp_i}{K}\asymp R^{1/4000}\to\infty.
\]

Hence the two factors `m_i=qp_i` are super-root, and eventually

\[
1-\frac{K}{qp_i}>\frac12.
\tag{3.6}
\]

Likewise

\[
\frac{K+1}{p_i}<q
\]

for large `R`. Since `ell=q` is prime, the exact P2-R16 small-divisor cover correction is again empty, so

\[
\boxed{
\mathcal C_q^{p_1,p_2}(K)=-\mu(q)=1.
}
\tag{3.7}
\]

Finally, because `p_i<y`, (1.2) gives

\[
\boxed{\gamma_K(p_i)>\frac1{5000}.}
\tag{3.8}
\]

Thus this moving-small-core family survives all of the exact reductions that were being considered as a possible source of a fixed power: super-root complement localization, collision packet compression, exact Möbius core collapse, and centered carry subtraction.

---

## 4. P2-R22 — PNT pigeonhole lower bound along infinitely many square shells

Let

\[
\mathcal Q_R
=
\{q\text{ prime}:R^{1/2000}\le q\le(1+\varepsilon_0)R^{1/2000}\},
\]

and

\[
\mathcal P_R
=
\{p\text{ prime}:R\le p\le(1+\varepsilon_0)R\}.
\]

By the prime number theorem in fixed relative intervals,

\[
|\mathcal Q_R|\asymp\frac{R^{1/2000}}{\log R},
\qquad
|\mathcal P_R|\asymp\frac R{\log R}.
\]

Hence the number of distinct unordered tuples

\[
(q,\{p_1,p_2\}),
\qquad
q\in\mathcal Q_R,
\quad
p_1,p_2\in\mathcal P_R,
\quad p_1\ne p_2,
\]

is

\[
\asymp
\frac{R^{2+1/2000}}{(\log R)^3}.
\tag{4.1}
\]

Unique factorization makes the corresponding integers

\[
n=3qp_1p_2
\]

distinct once `R` is large enough that the `q`-box and `p`-box are disjoint.

All these `n` lie in one fixed relative interval

\[
3R^{2+1/2000}
\le n\le
3(1+\varepsilon_0)^3R^{2+1/2000}.
\]

Therefore their square-shell indices `K=floor(sqrt(n))` occupy only

\[
O\!\left(R^{1+1/4000}\right)=O(K)
\]

possible values. Pigeonholing (4.1) among these shells yields an infinite sequence `K_j -> infinity` for which

\[
\boxed{
\#\{\text{moving-small-core W1 collision tuples in }I_{K_j}\}
\gg
\frac{K_j}{(\log K_j)^3}.
}
\tag{4.2}
\]

On every such tuple, (3.6), (3.7), and (3.8) show that the positive weighted centered collision contribution is bounded below by an absolute positive constant:

\[
\gamma_K(p_1)\gamma_K(p_2)
\left(1-\frac K{qp_1}\right)
\left(1-\frac K{qp_2}\right)
>
\frac1{4\cdot5000^2}.
\]

Hence along the same infinite sequence,

\[
\boxed{
\mathcal E_{W_1,+}(K_j)
\gg
\frac{K_j}{(\log K_j)^3}.
}
\tag{4.3}
\]

### Fixed-power obstruction

For every fixed `delta>0`,

\[
\frac{K/(\log K)^3}{K^{1-\delta}}
=
\frac{K^\delta}{(\log K)^3}
\longrightarrow\infty.
\]

Therefore no uniform bound of either form

\[
\#\operatorname{supp}(\text{W1 residual})
\ll K^{1-\delta}
\]

or

\[
\mathcal E_{W_1,+}(K)
\ll K^{1-\delta}
\]

can hold for any `delta>0`.

This is the promised route-selection result:

\[
\boxed{
\text{EXISTING-RESIDUAL SUPPORT/positive-energy FIXED-POWER SAVING IS OBSTRUCTED.}
}
\]

It does not obstruct signed bilinear cancellation. The correct fallback is constant extraction plus the existing Chen/Iwaniec oscillatory machinery.

---

## 5. P2-R23 — Exact root-edge packet-weight transfer

Now exploit the same T4 weight rather than discarding it by the generic bound `|beta|<=1`.

Consider a T4 x T4 distinct-prime collision. Put

\[
P=p_1p_2,
\qquad
Q=\operatorname{lcm}(d_1,d_2)t,
\qquad
n=PQ\in I_K.
\]

Since `p_i<K`, the root-edge weights

\[
\gamma_i=1-\frac{\log p_i}{\log K}
\]

are nonnegative. Their sum is

\[
\begin{aligned}
\gamma_1+\gamma_2
&=2-\frac{\log P}{\log K}\\
&=2-\frac{\log n-\log Q}{\log K}\\
&=\frac{\log Q}{\log K}
+2-\frac{\log n}{\log K}.
\end{aligned}
\]

Because `n>K^2`,

\[
2-\frac{\log n}{\log K}<0.
\]

Therefore

\[
\boxed{
\gamma_1+\gamma_2
<\frac{\log Q}{\log K}.
}
\tag{5.1}
\]

By AM-GM,

\[
\boxed{
\gamma_1\gamma_2
\le
\frac{(\log Q)^2}{4(\log K)^2}.
}
\tag{5.2}
\]

This is an exact transfer of the two outer-prime endpoint weights to the **small-core packet**. It is stronger than treating the two weights independently.

Since T4 begins at

\[
p_i\ge K^{22/27},
\]

one also has

\[
P\ge K^{44/27}.
\]

Thus

\[
\boxed{
Q
<
\frac{(K+1)^2}{K^{44/27}}
=K^{10/27}\left(1+\frac1K\right)^2.
}
\tag{5.3}
\]

Asymptotically, (5.2) and (5.3) recover the uniform T4 x T4 bound

\[
\gamma_1\gamma_2
\le
\frac{25}{729}+o(1),
\]

but small `Q` packets receive much stronger logarithmic suppression.

---

## 6. Finite conservative-splice consequence

Use the current Tier-A conservative splice

\[
K_*=116{,}009{,}280{,}740{,}973{,}308,
\]

so

\[
X_*=K_*^2
=13{,}458{,}153{,}218{,}037{,}960{,}469{,}637{,}923{,}168{,}462{,}864.
\]

Let

\[
p_{\min}
=
\left\lceil K_*^{22/27}\right\rceil.
\]

Exact integer arithmetic gives

\[
\boxed{p_{\min}=80{,}241{,}952{,}393{,}051.}
\]

Consequently every T4 x T4 packet satisfies

\[
Q\le
\left\lfloor
\frac{(K_*+1)^2-1}{p_{\min}^2}
\right\rfloor
=
\boxed{2{,}090{,}174<2^{21}.}
\tag{6.1}
\]

This is a useful finite fact: at the analytic splice, the entire T4 x T4 small-core packet lives below about `2.1e6`.

For a deliberately coefficient-uniform upper ledger, ignore the requirement that `P` be a distinct semiprime and count every odd integer `P` with

\[
K_*^2<PQ<(K_*+1)^2.
\]

For each packet pair use the already-proved internal multiplicity envelope

\[
2\cdot4^{\omega(Q)}.
\]

The companion checker performs the resulting exact finite sum for all odd

\[
Q\le2{,}090{,}174.
\]

For the logarithmic weight it uses only the exact inequalities

\[
K_*^3>2^{170},
\qquad
Q<2^{j+1}
\Longrightarrow
\frac{\log Q}{\log K_*}
<\frac{3(j+1)}{170}.
\]

Thus (5.2) is replaced by a rational dyadic upper bound in every packet bin.

The same crude all-odd-P / `2*4^omega(Q)` skeleton has unweighted ledger

\[
<427K_*.
\]

After applying the exact root-edge weight transfer bin by bin, the checker proves

\[
\boxed{
\mathcal L_{T4\times T4}^{\rm weighted}(K_*)
<8.83K_*.
}
\tag{6.2}
\]

So the packet-weight transfer alone cuts this deliberately crude finite collision ledger by more than a factor `48` before:

- imposing that `P` actually be a product of two distinct primes;
- imposing the individual T4 prime ranges;
- using exact Möbius core cancellation;
- using Rosser/well-factorable structure;
- using any oscillatory cancellation.

Equation (6.2) is therefore an **upper-envelope engineering result**, not a final normalized P2 error constant.

---

## 7. P2-R24 — Dyadic reciprocal block `rho=2`

The earlier explicit reciprocal lemma fixed

\[
\rho=\frac65
\]

and obtained local constant `15`. For the current a6 package the lower-frequency margin is much wider, so the same proof can be replayed directly on a full dyadic block.

Let

\[
S(M,t)=\sum_{M<m\le2M}e(t/m).
\]

Assume

\[
\boxed{
2^{4/3}M^{5/3}\le t\le\frac12M^3.
}
\tag{7.1}
\]

Then the low-frequency Kuzmin-Landau half of the old proof is unchanged.

For the high-frequency half, write

\[
r=\frac t{M^2},
\qquad
\frac12<r\le\frac M2.
\]

After dividing Patel's explicit second-derivative bound by `sqrt(t/M)=sqrt(rM)`, the curvature part is at most

\[
4\left(2+\frac2r\right)
\sqrt{\frac4\pi}.
\]

Using `r>=1/2` and `pi>3`, this is less than

\[
\frac{48}{\sqrt3}<28.
\]

The remaining part is

\[
4\sqrt{\frac rM}+\frac4{\sqrt{rM}}.
\]

Since `r<=M/2`, `rM>=1`, and `1/sqrt(2)<5/7`, it is less than

\[
\frac{48}{7}.
\]

Therefore

\[
28+\frac{48}{7}<35,
\]

and we obtain the clean dyadic lemma

\[
\boxed{
|S(M,t)|\le35\sqrt{\frac tM}.
}
\tag{7.2}
\]

### a6 lower frequency edge

With

\[
M=X^{31/72},
\qquad
N=X^{1/8},
\]

the lower edge is governed by

\[
1-2\nu-\frac53\mu
=1-\frac14-\frac53\frac{31}{72}
=\boxed{\frac7{216}}.
\]

For `rho=2`, (7.1) is guaranteed once

\[
X^{7/216}\ge2^{10/3},
\]

or

\[
\boxed{X\ge2^{720/7}.}
\tag{7.3}
\]

Exact integer comparison gives

\[
2^{720}<10^{217},
\]

so

\[
\boxed{2^{720/7}<10^{31}.}
\]

Thus the dyadic reciprocal lower edge is already legal below the current finite splice.

---

## 8. One explicit a6 B-spline companion

A convenient balanced explicit smoothing choice for the a6 package is

\[
\boxed{p=6,\qquad\eta=\frac{13}{900}.}
\]

For the order-six B-spline,

\[
C_6=\frac{2\,6^6}{\pi^6\,5}
<\frac{128}{5}
\]

using only `pi>3`.

With the same exponent bookkeeping as the frozen explicit B-spline package, the diagonal square exponent is

\[
\frac{31}{72}-\theta+\eta
=-\frac{549}{10000},
\]

so

\[
\boxed{\delta_{\rm diag}=\frac{549}{20000}=0.02745.}
\]

The trivial off-diagonal square exponent is

\[
2(d-\theta)+\frac{1-\theta}{2}+\frac52\eta-\frac{31}{72}
=-\frac{397}{12000},
\]

hence

\[
\boxed{\delta_{\rm off}=\frac{397}{24000}\approx0.0165417.}
\]

The Fourier-tail saving relative to the interval scale is

\[
(p-1)\eta-(d-\theta)
=\boxed{\frac{497}{30000}\approx0.0165667.}
\]

The reciprocal upper-frequency exponent margin is

\[
3\mu-(d+1+\eta-\theta-\nu)
=\boxed{\frac{10397}{30000}}
>\frac13,
\]

so the upper edge is overwhelmingly legal whenever `X>=10^31`.

Therefore the combined explicit package

\[
\boxed{
(a,d,p,\eta,\rho)
=\left(6,\frac59,6,\frac{13}{900},2\right)
}
\]

retains a minimum structural saving

\[
\boxed{
\min(\delta_{\rm diag},\delta_{\rm off},\delta_{\rm tail})
=\frac{397}{24000}
\approx0.0165417.
}
\]

This package is not claimed optimal. Its purpose is to provide a clean dyadic constant baseline after the fixed-power residual route has been ruled out.

---

## 9. Route decision

The research priority is now frozen as follows.

### Retired target

Do **not** attempt to prove a coefficient-uniform residual support or positive-energy bound

\[
K^{1-\delta}
\]

for any fixed `delta>0`. P2-R22 gives an explicit W1 family contradicting such a uniform theorem.

### Live target

Continue with finite constant extraction:

1. keep the T4 outer-prime weights instead of replacing them by `1`;
2. transfer the paired T4 weights to the small-core packet by (5.2);
3. exploit the finite splice fact `Q<=2,090,174` before any worst-case `K^o(1)` replacement;
4. use the dyadic `rho=2` reciprocal lemma to avoid unnecessary `6/5` sub-block proliferation;
5. only then charge Rosser/well-factorable coefficient defects and the remaining Lemma-4 constants;
6. keep `W_2` separate: its source weight is already at most `1/5000` in the present near-half packet.

The next hard frontier is therefore a **fully normalized W1 T4 packet constant ledger**, not another support-exponent theorem.

No all-K consecutive-square P2 theorem is claimed here.
