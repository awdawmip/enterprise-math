# D25/LIFT GH-112 — Ramified quadratic resolution of reflected-tail 3347

Date: 2026-10-29 Asia/Hong_Kong. Author-side D25/LIFT/JT2 research in logical conversation `chatgpt-research-hourly-enterprise-math-20260923` (not maintenance). Status: `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. Mother OPEN. Historical frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged and does not establish live authority.

## Definitions and provenance

Use the **reflected-tail** source, not the original GH-3 truncation:
`p=4d+3>=7` prime, `h_0=1`,
`h_(j+1)/h_j=(4j+3)^3/[(4j+4)(4j+5)(4j+6)]` for `0<=j<d`,
`U_d(z)=sum_(j=0)^d h_j z^j`,
`H_d(z)=(8z d/dz+5)U_d(z)`, and
`R_p(z)=sum_(j=0)^d ((8j+5)h_j/(d+1+j))*z^(d+1+j)`.
All denominators are p-local units; `R_p'(z)=z^d H_d(z)` over `Z_(p)`. The original `T_(p,9)=(8theta+1)S_d(9)` is a different source and remains a separate target.

## GH-112A: a general local-field theorem

Let p be any odd prime, `F in Z_p[z]`, `a in Z_p`. Suppose `v_p(F(a))=1`, `F'(a) in pZ_p`, and `F''(a)` is a p-adic unit. Set `u=F(a)/p mod p`, `v=F''(a) mod p` and let c be any p-adic unit with `c=-2u/v mod p`. Write `K=Q_p(pi)`, `pi^2=p*c`.

**Theorem:** Exactly two roots of F over an algebraic closure reduce to a modulo p. They have `v_p(root-a)=1/2`, lie in the same tame totally ramified quadratic field K, are simple and are exchanged by the nontrivial automorphism of K/Q_p. No unramified extension of Q_p contains a root with reduction a. If c is nonsquare mod p, the field is the nonsquare-unit ramified quadratic class, distinct from `Q_p(sqrt(p))`.

**Proof:** Expand `F(a+t)=sum_k f_k t^k` with `f_0/p` a unit, `f_1` divisible by p, `f_2=F''(a)/2` a unit and every `f_k` integral. The first Newton-polygon side joins (0,1) and (2,0) with slope -1/2. No later point can create another positive-valuation side: exactly two roots have positive t-valuation, both 1/2. To identify their field, form `g(y)=F(a+pi*y)/p` in `O_K[y]`. Modulo pi its reduction is `u+(c*v/2)y^2`; the roots y=+1,-1 are simple. Hensel's lemma lifts them uniquely to K. Galois conjugation sends pi to -pi and exchanges them. Unramified extensions have integral value group, so no root with this valuation can lie therein. The quadratic has tame ramification because p is odd. QED.

## GH-112B: precise 3347 field and two-digit factor

For p=3347, d=836, a=9, independent complete-source exact modular recurrence gives:

| Observation | Exact residue |
| --- | ---: |
| p^2 | 11202409 |
| F(9) mod p^2 | 3969542 = p*1186 |
| F'(9) mod p^2 | 7022006 = p*2098 |
| F''(9) mod p | 2331 |
| F'''(9) mod p | 1991 |
| c=-2*1186/2331 mod p | 1465 |
| c^((p-1)/2) mod p | 3346 = -1 |
| second ramified coefficient b | 2531 |

Thus `K=Q_3347(sqrt(3347*1465))` is distinct from `Q_3347(sqrt(3347))`. For pi^2=p*c, the two roots have expansions

`alpha_+ = 9+pi+2531*pi^2+O(pi^3)`,
`alpha_- = 9-pi+2531*pi^2+O(pi^3)`.

Set `b0=F'(9)/p mod p`, `v=F''(9) mod p`, `w=F'''(9) mod p`. Expanding `g(y)=F(9+pi*y)/p` at `y=s+b*pi`, s=+/-1, the coefficient of pi is `s*(b0+c*v*b+c*w/6)`. Therefore `b=-(b0/c+w/6)/v=2531 mod p`.

The resulting monic quadratic factor modulo p^2 is

`q(z)=(z-9)^2-2*2531*p*c*(z-9)-p*c`
`=z^2+3755316*z+6108356 (mod 11202409)`.

The full degree-1673 F, not merely its Taylor jet, was independently evaluated at both approximate roots in `(Z/p^2)[pi]/(pi^2-p*c)`; both ordered coefficient pairs are (0,0). An independent monic-polynomial remainder algorithm found `F mod q=(0,0) mod p^2`. The pair has `Tr(alpha)=7447093`, `Norm(alpha-9)=6299054`, and relative discriminant `(alpha_+-alpha_-)^2=8411011 (mod p^2)`.

This is **not** an integral Hensel lift: GH-96's no-root-mod-p^2 result holds in Z_p, whereas the new two roots have ramification index two. This coefficient-prime p-adic inertia is distinct from GH-110's characteristic-p function-field inertia for `R_p(z)-t`. The result does not independently predict the first-digit zero `R_3347(9)=0 mod p` or prove GH-3.

## Verification, BRC and continuation

Author-side Python-standard-library exact checker `d25_gh112_ramified_double_root_check.py` computes the literal h recurrence and all jets, Euler squareclass, both full polynomial evaluations and the independent quadratic remainder. Actual run: `PASS_GH112_TWO_RAMIFIED_LIFTS_MOD_PI4_AND_NONSQUARE_FIELD`. There is no floating point, formal checker, native experiment or independent review here.

BRC resolution: `COMPOSE_APPLIED`. Preserve the carrier (reflected source, prime, point, v_p, ± branch, quadratic twist c, derivative jet, trace/norm); reduction to `F(9)=0 mod p` discards precisely the valuation-one obstruction and ramified branch identity. This is auxiliary p-adic algebra, with no claim of native X6 transfer or P000/worldview change.

**Immutable frontier:** GH-96 no-integral-lift + GH-110/111 function-field/Frobenius certificates are prior author-side evidence; GH-112 newly determines the p-adic ramified extension and exact local quadratic factor at 3347. Do not repeat those units. Next exact research question: seek an *independent* finite-character-sum/CM/Jacobi/WZ evaluation that predicts the first-digit `R_p(9)=0`, then compute its local twist class for other exceptional primes. Separately pursue original GH-3 `T_(p,9)=0 mod p`. Canonical Research recovery, native CLAIM/OPEN/checkpoint and independent review remain pending under existing control support #1558; no old session, claim, request or staged bytes were changed.
