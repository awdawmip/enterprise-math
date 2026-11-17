# R749STE — Exact optimal five-read discrimination for cutoff pair (602,604)

**2026-11-17 · AUTHOR_EXACT_NOT_REVIEWED · Portable research.** Researcher EM-DIRECT-D83D31, session MCP-228ce0eba9504ed792987c922fc539d7, Activity RA-E81BE9E8D01D96A68D0753DE. Frozen five-labeled-source auxiliary scalar model: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This file is independent scientific evidence, not a formal X6/BRC Result or a shared CLAIM.

## Theorem

Take five **separately labeled** nonnegative integer sources with weights (1,1,2,3,6), marking the first unit-weight source. For n≥6 set

\[
\Omega_n=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le n-1\},\quad C_n=|\Omega_n|,\quad T_n=\sum_{k\in\Omega_n}k_1.
\]

Let \(S(n)=18n^4+54n^3-345n^2+2070n-16315\), and

\[
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108},\qquad
\mathcal O_n^{(m)}(e,d)=(Y_{n+6j}(e,d))_{j=0}^{m-1}.
\]

Each candidate maintains the same pair of real error parameters across its reads; both candidates' error parameters belong to \([-2,2]^2\). Then

\[
\boxed{\mathcal O_{602}^{(5)}(e,d)\ne\mathcal O_{604}^{(5)}(E,D)
\quad\text{for all }e,d,E,D\in[-2,2].}
\]

The previously certified R749STD exact four-read collision for the same pair (Draft PR #2619, commit 749399f2ced6038e5941706e3d144880260708d2) together with this result shows that the **optimal uniform exact discrimination horizon for this particular cutoff pair is exactly five**. The global bound remains \(5\le m_*\le11\).

## Proof — exact elimination

For j=0,…,4, let \(a_j=602+6j\), \(b_j=604+6j\), and define

\[
t_j=C_{a_j}+d,\quad\alpha_j=a_j^3/b_j^3,\quad
\beta_j=(S(b_j)-S(a_j))/(108b_j^3),
\]
\[
u_j=\alpha_j(T_{a_j}+e)+\beta_jt_j,\qquad
w_j=C_{b_j}u_j-T_{b_j}t_j.
\]

Equality of the j-th read is equivalent to \(E-(u_j/t_j)D=w_j/t_j\), where \(t_j>0\) for allowed d. Let \(A=w_0t_1-w_1t_0\) and \(B=u_1t_0-u_0t_1\). The first two equalities imply \(A=BD\), including the case B=0. Thus all five equalities necessarily imply \(P_2=P_3=P_4=0\), where

\[
P_j(e,d)=\frac{A(u_jt_0-u_0t_j)-(w_0t_j-w_jt_0)B}{t_0},
\qquad j=2,3,4.
\]

Exact polynomial division has zero remainder. After primitive integer normalization each \(P_j\) has total degree at most three. Form two pairwise resultants with respect to e:

\[
R_{23}(d)=\operatorname{primitive}\operatorname{Res}_e(P_2,P_3),\qquad
R_{24}(d)=\operatorname{primitive}\operatorname{Res}_e(P_2,P_4).
\]

Both are degree-eight integer polynomials. Exact Euclidean calculation gives

\[
\boxed{
\gcd(R_{23},R_{24})=
(d+19230175073)(d+20197991618)
(423323687089090985675d-894099074786485299705326337578).
}
\]

The first two roots are \(-C_{602}\) and \(-C_{608}\), far below −2. The third is greater than 2 since
\(894099074786485299705326337578>2(423323687089090985675)\).
A common zero of all three \(P_j\) would make both resultants vanish, so its d-coordinate would be a root of their GCD. Hence no such zero has \(d\in[-2,2]\). In particular no five-read coincidence exists for admissible parameters.

A separate exact elimination of d produces

\[
\gcd(\operatorname{primitive}\operatorname{Res}_d(P_2,P_3),
\operatorname{primitive}\operatorname{Res}_d(P_2,P_4))
=(e+1938941614326)(e+2056723726251)
(16278056426515699712159090150e-
10813151975078948797440159426145393125049).
\]

Its three roots also lie outside \([-2,2]\). These independently computed eliminations cross-check the obstruction.

## Reproducibility and provenance

Run Python 3 with SymPy: **python R749STE_FIVE_READ_PAIR_SEPARATION_CERT.py**. The companion script reconstructs the labeled-source counts via integer generating-function convolution, checks C602=19230175073, C608=20197991618, T602=1938941614326, T608=2056723726251, verifies polynomial divisions exactly, calculates all four rational/integer resultants and both GCD factorizations, proves all candidate roots excluded by integer inequalities, and generates a machine-readable JSON result. There is no floating-point assumption or sampling step. The evidence is author-side exact checking, not independent review.

The historical four-read existence certificate is [R749STD@749399f2](https://github.com/awdawmip/enterprise-math/blob/749399f2ced6038e5941706e3d144880260708d2/research_notes/portable_direct/2026-11-17_R749STD_FOUR_READ_EXACT_COLLISION.md). This result establishes a minimal future-observer distinction for the auxiliary pair: four readouts may alias, while five separate the two cutoff classes. Transferring that statement to native X6 Cell/Link/Port semantics requires its own source-preserving embedding and future-operation argument under P000.

**Next scientific problems:** seek five-read collision witnesses for other cutoff pairs (which would improve the global lower bound); lower the global eleven-read upper bound; quantify a robust five-read separation margin for (602,604) under measurement noise; design the smallest BRC repair coordinate preserving labeled source and future-observation distinctions.
