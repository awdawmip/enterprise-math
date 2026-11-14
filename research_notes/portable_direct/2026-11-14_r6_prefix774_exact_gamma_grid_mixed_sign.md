# PREFIX-774 / R6 — Exact mixed-difference phase in a rational 1/768 Gamma square

Date: 2026-11-14 (Asia/Shanghai). Scientific input frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_EXACT_INTEGER_GRID_WITNESS / UNREVIEWED / NOT_ADMITTED`.
Scope: independent two-Gamma-clock killed-Pascal auxiliary; this is a mixed-difference witness in the auxiliary parameter square, **not** an original BRC-comparison-cell exclusion, a native X6 theorem, or a claim that this cell was previously unknown in every record.

## 1. Model and exact moment identities

Use the 189-layer frozen first-stop recurrence, `T_x <= 189`, with survivor polynomial `S_i(x)=Pr(T_x>i)` for `0<=i<189`. Conditioned on `T_x=m`, let `C_x ~ Gamma(m,1)`; take the two clocks independently. Set `Y(p,z)=max(C_p,C_z)`, `mu=E[Y]`, `W=Var(Y)`, and `V_q=q^2 W-q mu`.

Let `s(x)=(S_0(x),...,S_188(x))`, and define rational matrices
[
K_{ij}={inom{i+j}{i}over 2^{i+j+1}},
qquad L_{ij}=(i+j+1)K_{ij}.
]
Integrating the exact survival identity
[
Pr(Y>t)=H_p(t)+H_z(t)-H_p(t)H_z(t),qquad
H_x(t)=e^{-t}sum_{i=0}^{188}S_i(x)t^i/i!,
]
shows
[
mu=sum_i s_i(p)+sum_i s_i(z)-s(p)^T K s(z),
]
[
M_2=2sum_i(i+1)s_i(p)+2sum_i(i+1)s_i(z)-s(p)^T L s(z),
quad W=M_2-mu^2.
]
The factor in the mixed product of `M_2` is exactly `L`, since `2 int_0^infty t e^{-2t}t^{i+j}/(i!j!)dt=(i+j+1)K_ij`.

## 2. Exact 1/768 cell and finite theorem

Let `a=38/768`, `b=39/768`, and for any `F` write
[
Delta F=F(b,b)-F(a,b)-F(b,a)+F(a,a).
]
The attached pure-Python integer certificate reconstructs the 189 survivor rows with the original killed-Pascal width predicate. Its nonzero row-position count is exactly **9,529** and row 189 is empty. It computes `mu`, `M_2` and `W` at the three symmetry-distinct corners by rational integer numerators at one common positive denominator. In particular, it proves
[
oxed{Deltamu<0,qquadDelta W<0.}
]
Define the exact positive rational switch
[
q_R={Deltamuover Delta W}.
]
Integer cross-multiplication, not floating point, proves the narrow rational enclosure
[
oxed{rac{2852034258349}{10^{14}}<q_R<
rac{2852034258350}{10^{14}}.}
]
Since `Delta V_q=q*(q Delta W - Delta mu)`, and `Delta W<0`, it follows **for all real `q>0`** that
[
oxed{
0<q<q_RRightarrowDelta V_q>0,quad
q=q_RRightarrowDelta V_q=0,quad
q>q_RRightarrowDelta V_q<0.
}
]
In particular the exact comparison establishes `Delta V_2<0`.

Display-only decimals from the exact ratios are:
[
Deltamuapprox -0.00493294208071696916,quad
Delta Wapprox -0.17296223095063648041,
]
[
q_Rapprox0.02852034258349057518,quad
Delta V_2approx-0.68198303964111198330.
]

## 3. Proof obligations and reproducibility

The row predicate is the frozen integer check `40(n+1) binom(n,k)x^k(2^18-x)^(n-k)>(2^18)^n`, with the source's quartile-width test. All comparisons use integer arithmetic. A common survivor denominator `E=768^188` and kernel denominator `T=2^377` yield moment denominator `H=E^2 T`. Thus `mu_num`, `M2_num` are integers over `H`; `W_num=M2_num*H-mu_num^2` is over `H^2`. The checker tests the three-corner integer differences, both negative signs, positive variances, the strict `q_R` bracket and the strict `q=2` sign.

The exact finite proof concerns this one auxiliary cell. No claim is made about the previously recorded historical `1/768` comparator coverage tally. The earlier local diagonal minimizer near `u=0.05029714515369` lies inside this square, while this square's switching ratio is larger than the PREFIX-773 diagonal local minimum. This is consistent with the strict local minimum and gives a reproducible **finite** sign certificate instead of another infinitesimal phase-point refinement.

Run `python3 research_notes/portable_direct/PREFIX774_R6_EXACT_GAMMA_GRID_WITNESS.py` with Python 3 standard library. Local run produced the companion JSON and satisfied all assertions. Scientific follow-up: certify a larger region using exact matrix/interval bounds, and determine whether the two-dimensional global phase minimum equals the PREFIX-773 diagonal local minimum. Preserve source and role verification before any shared Task CLAIM or formal Result.
