# D25 — Original E3 Cartier/Hasse coefficient, exact p-adic two-jet against the Hesse port

Date: 2026-11-08 (Asia/Hong_Kong). Status: **AUTHOR-SIDE ALGEBRAIC IDENTITY PROVED / INDEPENDENT EXACT FINITE CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; scientific pin **unchanged** `c47e13e4aba0e006366f989d6334d443f6333ae3`. This is a source-aligned, explicit original-Weierstrass coefficient calculation. It neither redefines nor fulfills the separate native H0/B0 divided-power `[X]U` benchmark tracked in issue #1559.

## Exact original geometric source and observer

For odd prime `p>3` use `R_3=(Z/p³Z)[T]/(T²-2)`, the explicitly chosen coefficient lift `c=(2-T)/108`, and the original cubic
[
 E_3:y²+xy+cy=x³,qquad Y=2y+x+c,qquad Y²=F(x):=4x³+(x+c)².
]
The differential is `dx/Y`. Put `n=(p-1)/2`, `m=⌊(p-1)/3⌋`, and use the *original cubic coefficient observer*
[
 H_p(c):=[x^{p-1}]F(x)^n
   =sum_{k=0}^{m}inom nkinom{p-1-2k}{k}(4c)^k.
]
Modulo `p`, this coefficient is the Hasse–Witt/Cartier coefficient for the indicated Weierstrass model, with the usual semilinear convention for Cartier. Its `p²` or `p³` **chosen integral lift** is a source-specific coefficient, not automatically a crystalline Frobenius entry.

The previous Hesse/CM finite polynomial at the *same original parameter* `u=27c=(2-T)/4` is
[
 A_p(c):=sum_{k=0}^{m}rac{(3k)!}{(k!)³}c^k
       =sum_{k=0}^{m}rac{(3k)!}{27^k(k!)³}u^k .
]
The binomial factors are integers; all rational denominators below are `p`-units because `3k≤p-1`.

## New exact source-port relation and second jet

For each `0≤k≤m` take the labelled denominator multiset
[
 {cal D}_k={1,3,ldots,2k-1}sqcup{2k+1,2k+2,ldots,3k}.
]
Define `S_1(k)=Σ_{d∈D_k}d^{-1}` and `S_2(k)=Σ_{d<e,;d,e∈D_k}(de)^{-1}` with multiset indices retained, and `a_k=(3k)!/(k!)³`.
There is an **exact rational identity in** `Z_(p)[c]`:
[
 oxed{H_p(c)=sum_{k=0}^{m}a_k c^k prod_{din{cal D}_k}(1-p/d).}	ag{1}
]
Proof: first use
[
4^kinom nk=(-1)^kinom{2k}kprod_{j=0}^{k-1}(1-p/(2j+1)),
]
and then
[
inom{p-1-2k}k=(-1)^kinom{3k}kprod_{j=2k+1}^{3k}(1-p/j).
]
The two signs cancel; `binom(2k,k)binom(3k,k)=a_k`. Each equality holds over `Z_(p)`, with no asymptotic or CM argument.

Let
[
 J_p(c)=sum_{k=0}^{m}a_k c^kS_1(k),qquad
 K_p(c)=sum_{k=0}^{m}a_k c^kS_2(k).
]
Taking the first two elementary-symmetric terms of the exact product gives, for **every prime p>3**:
[
 oxed{H_p(c)equiv A_p(c)-pJ_p(c)+p²K_p(c)pmod{p³}.}	ag{2}
]
In particular, `H_p≡A_p (mod p)` for all such primes. Whenever `p|A_p(c)` (in particular the accepted supersingular CM target classes `p≡13,19 mod24`), the quotient relation is
[
 oxed{H_p(c)/pequiv A_p(c)/p-J_p(c)+pK_p(c)pmod{p²}.}	ag{3}
]
Equation (3) is a **coefficient-lift port correction**, not an identification of either quotient with the required native H0/B0 Frobenius or a new all-prime LIFT proof.

## Exact p=373 source-class certificate

At `p=373`, `p²=139129`, `p³=51895117`, and `T²=2`, exhaustive integer modular arithmetic gives:

| Observer | Pair of coefficients in basis (1,T) |
|---|---|
| `c mod p³` | `(33635724,35077255)` |
| `H_p mod p³` | `(7225756,36025459)` |
| `H_p/p mod p²` | **`(19372,96583)`** |
| `A_p mod p³` | `(34338380,8126924)` |
| `A_p/p mod p²` | **`(92060,21788)`** |
| `J_p mod p²` | `(123789,97904)` |
| `K_p mod p` | `(137,90)` |

The previous Source author-side ordinary Hesse candidate `A_p/p=(92060,21788) mod139129` is independently reproduced, with its norm `122102 mod139129`. The **actual original cubic's chosen Hasse coefficient lift** has `H_p/p=(19372,96583) mod139129`, with norm `134077 mod139129`. In particular, the two quotients differ modulo `p`: original `(349,349)` vs Hesse `(302,154)`. The missing source-tagged term is `-J_p+pK_p`, not an optional scalar identification.

As small-fiber controls, exact direct coefficients at `p=13,19,37` also satisfy (1)–(3); the output pairs `H/p mod p²` are respectively `(119,106),(144,353),(569,532)`.

The independently executed checker uses **two coefficient constructions**: (i) binomial coefficient summation `[x^{p-1}]F^n` and (ii) direct repeated polynomial multiplication of the *actual cubic* `F(x)`, truncated at degree `p-1`; independently it computes the `a_k`, rational harmonic `J,K` and verifies each term of (1) through `p³`. All operations are exact integers modulo `p³`. No `[X]U` or native divided-power implementation was run.

## BRC and execution continuation

BRC resolution: **COMPOSE_APPLIED** as provenance-preserving port comparison. Carrier: (original E3 equation, chosen integral lift c, p, coefficient index k, finite denominator multiset D_k, Hesse A, harmonic J/K, original Cartier coefficient H, semilinear convention). The quotient `A/p` cannot replace `H/p` for a second-digit observer without carrying the displayed correction. This use does not reinterpret external two-coordinate ring notation as a native X6 plane or alter P000.

New exactly verified original-object first/second-digit diagnostic should be supplied to the true #1559 executor, who must still obtain the fixed **same-original-class H0/B0 divided-power module** and `[X]U mod139129`, determine rank, semilinear Frobenius direction/normalization `eta`, signed Green/Hesse `kappa` and original `Delta-R`, and independently reproduce the native result. If the original H0/B0 class can be compared to this Weierstrass Hasse lift, the executor must provide the comparison map and integral-lift convention explicitly; otherwise this Hasse result is only a separate source-aligned diagnostic.

Research lane label `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance `chatgpt-hourly-enterprise-math-20260921`; not an authenticated service Researcher identity. Prior continuation request `onhour11-20261106-1400-exact-research-lane-continuation` has read-only `SUCCEEDED` receipt and no research ownership. Native session/CLAIM/run: **NOT VERIFIED**. Result: **AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Highest priority unresolved original experiment: #1559, PENDING_OWNER. Do not re-credit accepted D24 UR or predecessor verified Source units.
