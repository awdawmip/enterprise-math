# D25 — Quartic Gauss Jacobi first jet and exclusive-factor lemma

Date: 2026-11-04. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Provenance: author-side portable derivation in the hourly20 research lane, not a native CLAIM, Source checkpoint, review or mathematical admission. Status: **GENERAL EXACT SCOPED LEMMAS + FINITE EXACT TESTS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.

## Exact first-jet theorem (proved)

Let `p=8q+5>=5` be prime, `L=5q+3`, `M=7q+4`, and for `0<=k<p` let

[
v_k=\frac{(1/8)_k(3/8)_k}{(k!)^2 9^k},\qquad
j_k=\binom Lk\binom Mk9^{-k}\quad(0\le k\le L).
]

Write `H_n=sum_{m=1}^n 1/m`, `H_0=0`, and

[
h_k=\tfrac58(H_L-H_{L-k})+\tfrac78(H_M-H_{M-k}),\qquad 0\le k\le L.
]

All denominators are `p`-units in these ranges. Then, **coefficient by coefficient** in `Z_(p)/p²`,

[
\boxed{v_k\equiv j_k(1-p h_k)\pmod{p^2}\qquad(0\le k\le L).}\tag{A}
]

Proof: The exact parameter equalities `1/8=-L+5p/8`, `3/8=-M+7p/8` give

[
(1/8)_k=(-L)_k\prod_{j=0}^{k-1}
\left(1+\frac{5p}{8(-L+j)}\right),
]
and the analogous formula with `M,7`. Expanding both finite products modulo `p²`, using `sum_{j<k}(-L+j)^{-1}=-(H_L-H_{L-k})` and `(-L)_k(-M)_k/(k!)²=binom(L,k)binom(M,k)`, yields (A) exactly.

Define the source-separated polynomials `J(z)=sum_{k=0}^L j_k z^k`, `K(z)=sum_{k=0}^L j_k h_k z^k`. Reuse the already proved single-boundary carry from `20261104_hourly20_d25_quartic_gauss_second_digit_tail_injection.md`:

[
R(z)=\sigma z^{L+1}\sum_{s=0}^{2q}
\frac{(1)_s(5/4)_s}{(15/8)_s^2}(z/9)^s,
\qquad \sigma=\tfrac{10}{441}\bar v_L\in\mathbb F_p.
]

For the exceptional prime `p=5`, `sigma=0`; this formula still applies. The complete `p`-term Gauss polynomial satisfies

[
\boxed{\sum_{k=0}^{p-1}v_kz^k\equiv J(z)+p(R(z)-K(z))\pmod{p^2}.}\tag{B}
]

Thus for `S=sum_{k<p}v_k`, `D=sum_{k<p}k v_k`, `Y=S+16D`, and `theta=z d/dz`,

[
\boxed{S\equiv J(1)+p(R-K)(1),\quad
Y\equiv[(1+16\theta)J](1)+p[(1+16\theta)(R-K)](1)\pmod{p^2}.}\tag{C}
]

This is a new explicit **Jacobi-binomial / harmonic jet / Frobenius tail** decomposition of the unit source and the carry source. The previous Gauss-band theorem gave `U+pR`; (A) replaces the otherwise opaque unit band `U` with explicit integer-binomial coefficients and first-order harmonic corrections.

## Exclusive first-factor zero (proved for all specified primes)

Reduce `J(z)` modulo `p`: it is the terminating solution of the Gauss differential equation

[
\mathcal D J=0,\qquad
\mathcal D=\theta^2-\frac z9
(\theta+\tfrac18)(\theta+\tfrac38).
\tag{D}
]

Indeed the coefficient recurrence holds for every `k<=L`, and its first omitted numerator contains `8L+1=5p`. Here `deg(J)=L<p` and `J(0)=1`. At `z=1`, the leading coefficient of `d²/dz²` is `z²(1-z/9)=8/9`, a nonzero element of `F_p`. If `J(1)=J'(1)=0`, expand about `z=1`. The Taylor coefficient recursion forces all coefficients of degrees `0..L` to vanish because `n(n-1)` is invertible for `2<=n<=L<p`. This contradicts `J(0)=1`.

Hence `J(1)` and `theta J(1)` cannot vanish simultaneously modulo `p`. Since `S=J(1)`, `D=theta J(1)` modulo `p` and 16 is a unit,

[
\boxed{\neg(S\equiv0\pmod p\ \land\ Y\equiv0\pmod p).}\tag{E}
]

Now consume the established first-digit product congruence `S Y=V_p+T_v=0 mod p`: `V_p=0 modp` follows from the proved Guo–Zudilin quartic result, while `T_v=0 modp` follows from the prior quartic Frobenius boundary polynomial and its first-digit consequence. Combining with (E) yields:

[
\boxed{\text{Exactly one of }S,Y\text{ vanishes modulo }p.}\tag{F}
]

Therefore `v_p(SY)>=2` is equivalent to `v_p` of that uniquely selected factor being at least 2. This sharpens the remaining second-digit obligation from a two-source product to **one selected p-adic zero** and permits a focused Jacobi/Hasse lift without losing the `J,K,R` sources.

## Exact finite evidence and discriminating outputs

The independently reconstructed modular Gauss recurrence and binomial/harmonic first-jet equations were checked by executing the standard-library Python file `d25_quartic_jacobi_firstjet_factorwise_20261104.py`. Domain: all **168** primes `5<=p<=5000` with `p mod8=5`; **238,897** unit-band coefficient checks; complete `S,D,Y` reconstruction modulo `p²`; all modular exclusive-factor assertions passed.

An empirically stronger **class selector** held for all these primes, and is still awaiting a universal proof:

[
\begin{cases}
S\equiv0\pmod{p^2},&p\equiv13\pmod{24}\quad(83\text{ checked primes}),\\
S+16D\equiv0\pmod{p^2},&p\equiv5\pmod{24}\quad(85\text{ checked primes}).
\end{cases}\tag{G: finite evidence}
]

For the selected vanishing factor, tests modulo `p³` showed exactly `v_p=2` for the **167** checked primes other than `p=5`; `p=5` had `S+16D=0 mod125`. This is a finite exceptional pattern, not a general classification.

| p | class | Jacobi sum J(1) mod p² | harmonic K(1) mod p | tail R(1) mod p | S mod p² | Y mod p² |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 13 | 104 | 7 | 12 | 0 | 137 |
| 29 | 5 | 403 | 21 | 17 | 287 | 0 |
| 37 | 13 | 555 | 3 | 25 | 0 | 227 |
| 53 | 5 | 2467 | 10 | 30 | 718 | 0 |
| 373 | 13 | 27975 | 307 | 232 | 0 | 110861 |

Each table entry is an independent retained residue source. The checker reconstructs the original `v_k` separately from `J,K,R` rather than generating both sides from one expected answer.

## Next scientific unit and status

Prove the class selector (G) via a finite CM/Jacobi first-jet or WZ identity, starting with the first-digit factor assignment (the `p=13,37,373` branch versus `p=29,53` branch). The first-digit CM theorem for the separate 216 family is already present in the other, on-hour research lane: `20261104_onhour_d25_hesse_cm_inert_first_digit_proof.md`; do not re-prove it or equate the two Gauss families without a transformation. Then use (C) to derive a uniform lifted cancellation for the quartic triangular observer before returning to the original signed 216–2304 Green comparison.

Mother objective: `W216(p-1)-V2304(p-1)=0 mod p³` for `p mod24 in {13,19}`; frozen D24 `Delta_p-R_p=0 modp`; independently required native p=373 H0/B0. The author's research lane is `chatgpt-research-hourly-enterprise-math-20260923` as requested by the task prompt; this note is not evidence of a service-issued session, winning CLAIM or run. No maintenance-lane identity is used. Pending native continuation receipt: `research-hourly20-20261104-1716-continuation-read` (QUEUED/COLLECTING when last polled); preserve its original request ID and reconcile.

**BRC observer resolution:** `COMPOSE_APPLIED` for exact prime/valuation, signed source `(J,K,R)`, full sum and first-derivative ports, and explicitly stated future operations through the `p²` observer; no projection erases the harmonic or carry input. No new native X6 experiment, Review, Result, Foundation promotion, or Source checkpoint is claimed.
