# D25 AF4 — two terminating Jacobi ports and a second spectral p-adic jet

2026-11-09 | TASK_RESEARCH author-side mathematical proof | **UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`, not the maintenance lane. This note does not claim a native Source execution session or winning CLAIM.

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; immutable task science pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; last native durable frontier `b58330b74576153cdadde5d80a3d92df3a819a0e`. Predecessor author note: `20261109_onhour_d25_CM_quadratic_overflow_trace.md`, which leaves the all-prime signed CM overflow zero open. Preserve all earlier authors and source provenance.

## Theorem A: all-prime two-Jacobi interpolation (mod p²)

Let `p>3` be prime with `p ≡ 5 (mod 8)`; `a=(5p-1)/8`, `b=(7p-3)/8`. Both are integers in `0<=a<b<p`. All polynomial congruences are coefficientwise in `Z_(p)[z]`.

Set
[
F_p(z)=sum_{k=0}^{p-1}rac{(1/8)_k(3/8)_k}{(k!)^2}z^k,qquad
J_n(z)=sum_{k=0}^{n}rac{(-n)_k(n+1/2)_k}{(k!)^2}z^k.
]
Then
[
oxed{12F_p(z)equiv7J_a(z)+5J_b(z)pmod{p^2}.}	ag{A}
]
More precisely, introduce
[
U_p(lambda,z)=sum_{k=0}^{p-1}rac{z^k}{(k!)^2}
prod_{i=0}^{k-1}left((i+1/8)(i+3/8)+lambdaight).
]
For `delta` replace the two upper parameters by `1/8+delta,3/8-delta`. Their product at `i` is `r_i+delta/4-delta^2`. For `delta_A=-5p/8` the shifted parameters are `-a,a+1/2`, so `J_a=U_p(lambda_A,z)` exactly, with
[
lambda_A=-5p/32-25p^2/64.
]
For `delta_B=7p/8` the shifted parameters are `b+1/2,-b`, hence `J_b=U_p(lambda_B,z)`, with
[
lambda_B=7p/32-49p^2/64.
]
Both spectral nodes are divisible by p. Their first-order interpolation weights reduce modulo p to 7/12 and 5/12, canceling the linear displacement; this proves (A), including all coefficients up to k=p-1 and the terminating tails.

## Theorem B: a **mod p³** curvature certificate with no singular-denominator division

Define the integral coefficient
[
K_p(z)=[lambda^2]U_p(lambda,z)=
sum_{k=2}^{p-1}rac{z^k}{(k!)^2}
sum_{0le i<j<k}prod_{substack{0le h<k\h
otin{i,j}}}r_h.
]
No inverse of any `r_i` is used; only k! denominators with k<p are inverted. Define exact weights in `Z_(p)`
[
w_A=rac{7(2-7p)}{24(1-p)},quad
w_B=rac{5(2+5p)}{24(1-p)}.
]
They obey `w_A+w_B=1` and `w_A lambda_A+w_B lambda_B=0` **exactly**. The finite polynomial Taylor expansion gives
[
 w_AU_p(lambda_A,z)+w_BU_p(lambda_B,z)
 equiv U_p(0,z)-lambda_Alambda_B K_p(z)pmod{p^3}.
]
Since `lambda_A lambda_B ≡ -35p²/1024 (mod p³)`, obtain the new all-prime coefficientwise identity
[
oxed{
F_p(z)equiv
rac{7(2-7p)J_a(z)+5(2+5p)J_b(z)}{24(1-p)}
-rac{35p^2}{1024}K_p(z)pmod{p^3}.
}	ag{B}
]
This retains the first nontrivial spectral curvature in the fourth-digit comparison. It is an algebraic identity for **every** p ≡ 5 mod8 (p>3), with no assumption about supersingularity or the all-prime CM zero conjecture.

## Exact reduction to an ordinary Legendre/Jacobi pair

The classical finite quadratic identity, provable by the Legendre differential equation and the value at z=0, is
[
J_n(4x(1-x))=P_{2n}(1-2x).
]
Indeed `P_{2n}(t)` is even, so the right side is polynomial in `z=1-t²`, solves
`z(1-z)J''+(1-3z/2)J'+n(n+1/2)J=0`, and equals 1 at z=0, uniquely identifying `J_n`.

At `s=(3-2 sqrt(2))/6`, `4s(1-s)=1/9` and `1-2s=2sqrt(2)/3`. Therefore Theorem A reads
[
12F_p(1/9)equiv
7P_{(5p-1)/4}(2sqrt2/3)+
5P_{(7p-3)/4}(2sqrt2/3)pmod{p^2}.
]
Each Legendre degree is even, hence both values lie in the base ring despite the displayed square root.

For p≡13 mod24, the **previous author-side CM(-24) Hasse root statement** gives `F_p(1/9)≡0 (mod p)`, and Theorem A together with the earlier CM argument identifies `J_a(1/9)`, `J_b(1/9)` as p-divisible in the checked range. Whenever both are divisible by p, define `A_p=J_a(1/9)/p mod p`, `B_p=J_b(1/9)/p mod p`. Then
[
oxed{F_p(1/9)/p equiv (7A_p+5B_p)/12pmod p.}	ag{C}
]
Combining the predecessor's finite signed trace `F_p(1/9)/p=(3u_p+4v_p)/6` gives an exact p-integral observer bridge
[
oxed{7A_p+5B_pequiv2(3u_p+4v_p)pmod p.}
]
Thus the previously OPEN all-prime trace cancellation is equivalent to an explicit two-Legendre/Jacobi divisibility problem, subject to the declared CM p-divisibilities. Neither this reduction nor (B) proves that residual zero for all primes.

## Exact executed arithmetic and p373 fourth-digit curvature

The attached standard-library checker evaluates (A), (B) at `z=1/9` in `Z/p³`, using direct independent rising-factorial/Jacobi recurrences and a *division-free* coefficient recursion for `K_p`. At five selected primes, an independent binomial expression for `P_{2a}(2sqrt2/3)` and `P_{2b}(2sqrt2/3)` in the quadratic ring verifies the transformed ports.

Ten selected p≡5 mod8 primes **5,13,29,37,53,61,109,157,181,373** passed both exact relations; five **13,37,61,109,373** passed the independent quadratic Legendre check. These are finite executions, whereas (A) and (B) have separate full-domain proofs.

At p=373, `p²=139129, p³=51895117`, `a=233,b=326`:
[
J_a(1/9)equiv 92131=247ppmod{p^2},quad
J_b(1/9)equiv93623=251ppmod{p^2}.
]
Thus `7*247+5*251=2984=8p` and the old signed overflow residual also vanishes on this diagnostic p. At fourth digit:
[
K_{373}(1/9)equiv300pmod{373},
]
[
w_AJ_a+w_BJ_bequiv49112537=353p^2pmod{p^3},
]
[
(35/1024)K_{373}equiv341pmod{373},
]
[
oxed{F_{373}(1/9)equiv(353-341)p^2=12p^2=1669548pmod{p^3}.}
]
This isolates a **nonzero, indispensable curvature carry 341** in an original Gauss truncation coefficient, preserving p-adic residues and labels. It is not the native original-class H0/B0 divided-power coefficient [X]U.

Negative controls: p=5,29,53 also satisfy (A),(B) while F(1/9) is NOT divisible by p², showing why a residue-class-specific CM input is needed for a universal p² zero claim.

## Exact remaining fronts and provenance

**Open mathematical unit:** prove for all p≡13 mod24 that `7A_p+5B_p=0 (mod p)` using a CM/Jacobi index-transfer or a signed pairing, preserving parity and p-adic carry; combine with (B) if needed for fourth-digit AF4. Full original AF4 W/V remains open.

**Unexecuted native hard target:** same-original-class p=373 fixed H0/B0 divided-power `[X]U mod139129`, module rank, semilinear Frobenius direction and eta, signed odd Hesse/Green κ, original Delta-R and independent repetition. Existing #1559 support request remains OPEN/PENDING_OWNER, no verified native executor. Portable Jacobi/curvature is NOT a substitute.

Source canonical continuation `onhour11-20261109-2341-continuation`: read receipt SUCCEEDED 2026-11-09T15:39:19Z, action register-new-session-and-claim, no ownership granted. Old named session recovery returned `SESSION_CAPABILITY_REQUIRED`; no own verified winning CLAIM/open run, no formal Source checkpoint. This is a GitHub author-side contribution, not a native Result/freeze/acceptance.

Next action: seek exact finite Jacobi index reciprocity at p-dependent degrees p+q and 2p-q-1 (q=(p-1)/4); on the native path, only actual authorized owner executes the fixed original p373 benchmark, delivers a reproducible raw operator/observer receipt, then independent review.

References: predecessor `research_notes/portable_direct/20261109_onhour_d25_CM_quadratic_overflow_trace.md`; task source continuation, published author CM24 root result, and standard classical Legendre/Jacobi hypergeometric identities.
