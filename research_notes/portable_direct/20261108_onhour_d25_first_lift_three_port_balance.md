# D25 — First Gauss lift as Hasse quotient + local deformation + zero-crossing tail

Date: 2026-11-08 (Asia/Hong_Kong). Classification: **TASK_RESEARCH, author-side exact lemma PROVED / finite cross-model conjectural tests CHECKED / UNREVIEWED / NOT_ADMITTED**. Mother Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical lane `chatgpt-research-onhour-enterprise-math-20260923`; **not** the maintenance lane. This is external finite-field mathematics; no native X6/H0/B0 execution is claimed.

## Why this is the smallest new unfinished part

The prior CM derivative result `20261107_onhour_d25_cm_frobenius_first_digit_bridge.md` reduces the open A-model first digit to `C_p=0`, with B's unit already proved from Guo–Zudilin. The prior three-stratum/Clausen calculations do not themselves supply an inter-model first-lift identity. Here we isolate the *exact first-order p-adic Gauss-parameter shift* into three independently typed observable ports, and show at p=373 that all three genuinely contribute. This determines what a successful Cartier/Fricke transport must cancel, without claiming the conjectural cancellation has been proved.

## General exact first-lift lemma (proved)

Let p be a prime, `0<=u<v<p`, and `lambda,mu,z in Z_(p)`. Define the p-term Gauss polynomial
[
F_{<p}(a,b;z)=sum_{n=0}^{p-1}rac{(a)_n(b)_n}{(n!)^2}z^n,qquad
P_{u,v}(z)=sum_{n=0}^{u}inom{u}{n}inom{v}{n}z^n.
]
Set `a=-u+lambda*p`, `b=-v+mu*p`. In `Z_(p)[z]` coefficientwise modulo p²,
[
oxed{F_{<p}(a,b;z)=P_{u,v}(z)+p{L_{u,v}(z)+T_{u,v}(z)}pmod{p^2}}
]
where the low-index harmonic variation is
[
L_{u,v}(z)=sum_{n=0}^{u}inom{u}{n}inom{v}{n}z^n
left(lambdasum_{j=0}^{n-1}rac1{j-u}+
      musum_{j=0}^{n-1}rac1{j-v}ight)
]
and the *single-zero crossing tail* is
[
T_{u,v}(z)=lambdasum_{n=u+1}^{v}
rac{(-1)^{u+n}u!,(n-u-1)!,v!}
     {(v-n)!,(n!)^2},z^n.
]
All displayed denominators are p-units. **Proof:** every summand is a polynomial in a,b over `Z_(p)`; Taylor expansion at `(-u,-v)` to first order is exact mod p². For `n<=u` both Pochhammer factors are nonzero and logarithmic differentiation gives the two harmonic sums. For `u<n<=v`, exactly the a-factor vanishes and only its derivative survives, with
(partial_a(a)_n|_{a=-u}=(-1)^u u!(n-u-1)!).
For `v<n<p` both base Pochhammer factors vanish, so both first derivatives are zero. The above is a full proof for arbitrary specified u,v and coefficients, not a numerical fit.

## Specialization to the frozen 216 and 2304 input

For `p≡13,19 mod24`, let `m=(p-1)/6`; `epsilon=1` for 13, 0 for 19; `k=(p-(5 if epsilon else 3))/8`.

* A input: `(a,b,z)=(1/6,1/3,1/2)` equals `(-m+p/6,-2m+p/3,1/2)`. Let `Q_A=P_{m,2m}(1/2)`, and `L_A,T_A` use `(lambda,mu)=(1/6,1/3)`.
* B input: `(a,b,z)=((3+2epsilon)/8,(1+6epsilon)/8,1/9)` equals `(-k+p/8,-(3k+1)+3p/8,1/9)`. Let `Q_B=P_{k,3k+1}(1/9)`, and `L_B,T_B` use `(lambda,mu)=(1/8,3/8)`. Both Euler branches stay distinct, although these first-order parameter shifts are uniform.

Previous CM/Hasse-zero theorem gives `p|Q_A`, `p|Q_B`; hence the *integer-unit* Hasse quotients `q_A=Q_A/p modp`, `q_B=Q_B/p modp` exist. The two Gauss first lifts are now **rigorously**:
[
g_A=q_A+L_A+T_A,qquad g_B=q_B+L_B+T_Bquad(mod p).
]
This identity cannot identify the naive Hasse lift `Q/p` with the actual Gauss lift `G/p` unless the two deformation ports are accounted for.

Let `J_A=(zQ_A'(z))|_{z=1/2}`, `J_B=(zQ_B'(z))|_{z=1/9}` (both nonzero mod p by prior exact proof). Set scalar coefficients in Fp:
[
(t_p,r_p)=
egin{cases}
(J_A/(6J_B),,2/9),&pequiv19pmod{24},\
(-J_A/(8J_B),,-4/27),&pequiv13pmod{24}.
end{cases}
]
The previously defined signed CM residual is `C_p=s^epsilon(t_p*g_A-r_p*g_B)` in `Fp[s]/(s²-2)`. It decomposes with **no loss of provenance**:
[
oxed{ C_p/s^epsilon = R_Q+R_L+R_T inmathbb F_p, }
]
[
R_Q=t_pq_A-r_pq_B,quad
R_L=t_pL_A-r_pL_B,quad
R_T=t_pT_A-r_pT_B.
]
The notation `C_p/s^epsilon` means the uniquely declared scalar coordinate in the basis `1,s`; it does not erase the odd 13-class Frobenius eigencharacter. This equation is an exact general consequence of the lemma. **The further statement `R_Q+R_L+R_T=0` for all target primes remains unproved** and is equivalent to the A first-digit question under prior results.

## Discriminating exact witnesses (integer reductions)

Independent p² Gauss recurrence versus explicit p-parameter derivative formulas, and source-typed scalar-coordinate calculation:

| p | epsilon | R_Q | R_L | R_T | total mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 1 | 10 | 10 | 6 | 0 |
| 19 | 0 | 13 | 17 | 8 | 0 |
| 43 | 0 | 26 | 17 | 0 | 0 |
| 67 | 0 | 24 | 4 | 39 | 0 |
| 373 | 1 | 4 | 322 | 47 | 0 |

At **p=373**, the raw independent ports are:
[
(q_A,L_A,T_A)=(340,352,78),quad (q_B,L_B,T_B)=(326,41,365).
]
[
(g_A,g_B)=(24,359),quad(J_A,J_B)=(294,41),quad(t_p,r_p)=(106,138).
]
Thus `R_Q+R_L+R_T=4+322+47=373≡0 mod373`, with **each port separately nonzero**. An argument identifying just the unperturbed Hasse quotients gives residual 4, not zero. Even adjoining only the harmonic low port leaves residual `326 mod373`, so the single-zero tail is essential here. The signed coordinate is `C_373=s*0`, not its norm or a zero assigned to an unobserved component.

The accompanying independent-arithmetic script runs both Gauss p² streams, both binomial Hasse evaluations and explicit derivative/zero-crossing formulae for **all 77 primes <=2000 in the two target classes**; the universally proved individual Taylor congruences pass, and the **conjectural** cross-model three-port sum is observed zero for those 77 primes. Neither the finite range nor the tautological equality between different definitions is called a universal proof.

## Research decision and required next work

A putative Fricke–Cartier isomorphism proof must transport the *combined* Hasse-quotient and two p-adic deformation ports with the epsilon odd/even signed scalar coordinate. The next exact target is a Frobenius-compatible, source-preserving formula for `R_Q+R_L=-R_T`, ideally using an original-model or elliptic-isogeny p-adic lift rather than another finite scan. The p373 original-class native H0/B0 `[X]U mod p²`, rank, Frobenius eta, signed Hesse kappa and independent run at [support #1559](https://github.com/awdawmip/enterprise-math/issues/1559) remain **PENDING**, not replaced by these external hypergeometric port numbers.

Native Source: old continuation request `onhour11-20261106-1400-exact-research-lane-continuation` remains independently tracked; as-of 2026-11-08 this run observed a read-only receipt `RUNNING / REVALIDATING`, no native Researcher authority and no verified native CLAIM/run. No native mutating operation was sent. **No change to task schedule or notification policy.**
