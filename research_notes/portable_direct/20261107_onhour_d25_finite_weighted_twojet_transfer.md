# D25 — Exact finite weighted Fricke transfer as a two-jet condition

Date 2026-11-07. Author-side TASK_RESEARCH unit. `AUTHOR_SIDE_PROVED / FINITE_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED`. Immutable D25 task/publication/science `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, `TP2-B6F4FC938FF94941C1B7`, `c47e13e4aba0e006366f989d6334d443f6333ae3`. Continue from Fricke source/Hasse frontier `19e0e0bfb6fdb21da55b62b082a96f3a5d6ee3cd`, with analytic maps and pullback fixed at `9924d627da2b8bec897405ab8d7ef9ecbb6aeccc`.

## Exact theorem for every cutoff (not an asymptotic argument)

Let `U_<n(z)=sum_(k=0)^(n-1) C_k z^k` and `B_<n(w)=sum_(k=0)^(n-1) D_k w^k` with coefficients and Fricke maps `z(t),w(t),H(t)` as in the frozen previous proof. Put
[
E_n(t)=U_{<n}(z(t))-H(t)B_{<n}(w(t)),qquad t_ε=ε6sqrt2quad (ε=pm1).
]
Define the two **weighted** truncated objects at the *original* 216 and 2304 arguments:
[
W_n=(1+6zpartial_z)U_{<n}(z)|_{z=1/2},quad
V_n=(1+8wpartial_w)B_{<n}(w)|_{w=1/9}.
]
For every integer n≥1 the following identity holds **exactly over Q(s), s²=2**:
[
oxed{qquad W_n-rac32V_n=
E_n(t_ε)+(24+18εs) E'_n(t_ε).qquad} 	ag{1}
]
The right side lies in Q and agrees for both ε. This is an exact finite counterpart of the analytic weighted period identity, retaining the first *homogeneous initial-value jet* of the cutoff defect.

**Proof:** From the exact maps at tε,
[
z=1/2, w=1/9, H=ε3s/4,quad z'=-1+ε3s/4,
]
[
H'=(-7+ε5s)/8,quad w'=4/9-ε8s/27,quad
6z/z'=3/z'=24+18εs.
]
The two exact coefficient identities
[
H+6z H'/z'=3/2,qquad 6zHw'/z'=(3/2),8w=4/3
]
follow by multiplication in Q(s). Substitute `U_<n=E_n+H B_<n` into `(1+6z∂_z)U_<n` and apply the chain rule. The B_<n and ∂_w B_<n terms become `(3/2)(1+8w∂_w)B_<n`, leaving exactly (1). No use of a conjectured supercongruence occurs.

For every prime p>3, write χ_p=(−3/p). The previously observed fourth-digit transfer
[
2V_p-W_p-pχ_pequiv0pmod{p^4}
]
is **equivalent**, without loss of p-adic precision, to the **two-jet target**
[
oxed{qquad E_p(t_ε)+(24+18εs)E_p'(t_ε)
equivrac12V_p-pχ_ppmod{p^4}.qquad} 	ag{2}
]
The equivalence is valid for both conjugate ports. Equation (2) fixes the missing type of information for the next Frobenius/Dwork step: two initial-value constants for the cutoff defect, not merely the Picard–Fuchs forcing. The exact nonzero inhomogeneous p-th Hasse source from `19e0e0b` coexists with (2); it does not determine E_p or E'_p alone.

## Exact finite witnesses and observer typing

`d25_weighted_finite_twojet_check_20261107.py` independently evaluates integer binomial sums and their k-weighted moments modulo p⁴, then reconstructs `(E_p(t_+),E'_p(t_+))` as pairs of scalar and s-coefficient. All six p=5,7,11,13,19,373 checks passed. The conjectured fourth-digit residual additionally happens to vanish for these six tested primes, a finite observation.

At p=19 (mod 130321):
- `E_p(t_+)=(126350,10108)` and `E'_p(t_+)=(51927,14934)` in `(Z/p⁴)[s]/(s²−2)`.
- `E+(24+18s)E'=85728` with s-coefficient exactly 0; `(W,V)=(82327,41173)` and `V/2−19=85728`.

At p=373 (mod 19356878641):
- `E_p(t_+)=(10804062495,6686261482)` and `E'_p(t_+)=(15402948464,15591439165)`.
- `E+(24+18s)E'=12636460803` with s-coefficient exactly 0; `(W,V)=(11832087049,5916043711)` and `V/2−373=12636460803`.

These are original 216/2304 finite arithmetic observations; **not** the same-original-class native H0/B0 [X]U experiment at p373 requested by #1559.

## Applied BRC interface and next exact action

`COMPOSE_APPLIED`: the carrier retains independent C and D coefficient streams, both conjugate Fricke ports, the value E, its first derivative and the Hasse p-th coefficient; operations are rational Fricke pullback, weighted logarithmic derivative, branch-conjugate combination and mod p⁴ readout. This is the first explicit all-n exact linear functional matching the mother-weighted readout to the finite Fricke difference without hiding the source.

Next: compute **native-normalized** Frobenius values of `E_p(t_ε)` and `E'_p(t_ε)` from the fixed CM class and prove the two-jet target (2) uniformly for p≡13,19 (mod24). Keep issue #1559's fixed native experiment separate. Current Source gateway lacks verified execution authority; original request `onhour11-20261106-1400-exact-research-lane-continuation` remains unresent, session/claim/run unverified. 
