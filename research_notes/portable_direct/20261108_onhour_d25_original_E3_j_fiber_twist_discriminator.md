# D25 — Original E3: coalescing CM j-fibers, actual quadratic twist, and a sign-comparator guard

2026-11-08 Asia/Hong_Kong. **TASK_RESEARCH AUTHOR-SIDE / exact algebraic theorem / exact p=13,19 finite-field point counts / 77-prime coefficient regression / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; scientific input frozen at `enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical research lane: `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance. This note consumes the author-side original-E3 geometric Frobenius sign theorem and the later auxiliary semilinear quartic-twist obstruction; those statements are not recredited as new Source Results.

## Exact question and inputs

Can the apparent coincidence of the two CM conjugate j-values at the first diagnostic primes p=13 and p=19, or an automorphism of the *original* elliptic curve, provide the missing original-geometric interpretation of the abstract scalar `rho` used to change the auxiliary Frobenius-square sign? We inspect the *actual* curve

    E3(t): y² + x y + (t/27)y = x³,
    t=(2-s)/4, s²=2, c=t/27=(2-s)/108,

over the unique field k=F_p[s]/(s²-2)=F_(p²) for p≡13,19 (mod 24). Its j-invariant and the prior source CM theorem give

    j(E3)=2417472+1707264s,
    H_(-24)(X)=X²−4834944X+14670139392,
    original geometric q=p² Frobenius π_q=[+p].

The geometric π_q=[+p] is a **consumed prior author-side theorem** depending on classical CM, inert supersingular reduction and original 3-torsion. The new computations below independently count the two small curves but do not reprove that all-prime source.

## Theorem A — No exceptional original self-automorphisms on either target class

For every prime p≡13 or19 (mod24), p>3, the reduced original curve has j neither 0 nor 1728 in F_(p²), hence its automorphisms preserving the identity over the algebraic closure consist exactly of {+1,−1}. Proof: the exact integer factorization

    H_(-24)(0)    = 14670139392 = 2^12 * 3^6 * 17^3,
    H_(-24)(1728)= 6318342144 = 2^14 * 3^6 * 23^2

shows neither can vanish modulo a target prime, since 17 and23 are outside both residue classes. The classical char>3 elliptic automorphism classification therefore applies. In particular, a self-automorphism of the original marked elliptic curve cannot implement a nontrivial operator scalar norm −1 to convert a σ-semilinear auxiliary square −p into +p: the only identity-preserving automorphism factors are ±1 and have σ-norm +1. This exact statement concerns *self-automorphisms*, not isogenies, twists, isomorphisms between conjugate curves, or changes of the actual native Frobenius operator.

## Theorem B — Precisely two small target primes have CM conjugate-j collision

The coefficient factorization

    1707264 = 2^8 * 3^3 * 13 * 19

and (2/p)=−1 for the two target residue classes imply

    j_+ = j_- ∈ F_p  ⇔  p∈{13,19}

among **all** target primes p>3; elsewhere j is genuinely quadratic over F_p. The two small collisions produce

    p=13: j_+=j_-=5 ∈ F_13;
    p=19: j_+=j_-=7 ∈ F_19.

Their j-values remain nonexceptional: 1728 mod13=12 and mod19=18. The Hilbert polynomial has a double reduction root at each of these two primes, but this does **not** enlarge the original curve's automorphism group. It instead creates a potential confusion between a *model descending to F_p* and the actual original E3 over F_(p²).

## Theorem C — At p=13 and p=19, original E3 is the nontrivial quadratic twist over F_(p²) of an explicit F_p model

Let j=j(E3) modp in F_p for p∈{13,19}. The standard short reference model with this j is

    E_j / F_p: y²=x³+A x+B,
    A=3j/(1728−j),  B=2j/(1728−j).

Its coefficients are:

| p | original j | reference E_j/F_p | exact #E_j(F_p) | #E_j(F_(p²)) | #original E3(F_(p²)) |
|---:|---:|---|---:|---:|---:|
| 13 | 5 | y²=x³+4x+7 | 14 | 196 | 144 |
| 19 | 7 | y²=x³+14x+3 | 20 | 400 | 324 |

Both F_p point counts were obtained by exhaustive finite Legendre sums, hence a_p=0. For their base change, a_(p²)=a_p²−2p=−2p, so #E_j(F_(p²))=(p+1)². For the genuine E3, a separate **exhaustive F_(p²) point count on the original equation**, using the quadratic character of the original discriminant `(x+c)²+4x³`, gives (p−1)². These differing traces prove the original curve is the **nontrivial** quadratic twist of E_j over F_(p²), since j is equal and nonexceptional.

An explicit square-class certificate is available without solving for a coordinate isomorphism. For original E3 put

    c4=1−24c, c6=−1+36c−216c²,

and for E_j put `c4_ref=−48A`, `c6_ref=−864B`. Define

    d = (c6*c4_ref)/(c4*c6_ref) ∈ F_(p²)^×.

Under an algebraic-closure isomorphism and a quadratic twist by parameter D, `d=u^(-2) D` for some invertible u, so d and D have the same square class. Exact evaluation yields

| p | d in F_p[s]/(s²−2) | norm d ∈ F_p | Legendre_p(norm d) |
|---:|---|---:|---:|
| 13 | 7+2s | 2 | −1 |
| 19 | 11+2s | 18 | −1 |

Since `χ_(p²)(d)=χ_p(N(d))`, both d are nonsquares in F_(p²). This independently certifies the genuine quadratic-twist distinction, including its sign-flipped Frobenius trace. Values d are **square-class witnesses**, not a measured native Frobenius coefficient or a canonical H0/B0 change-of-basis matrix.

## New discriminator for the previous abstract sign-fixing rho

The prior auxiliary scalar construction had `N(rho)=-1` modulo p for **both** residue classes, needed to change `Mσ(M)=−pI` to `+pI`. But

    χ_(p²)(rho) = χ_p(N(rho)) = (−1/p)
               = +1 for p≡13 mod24,
               = −1 for p≡19 mod24.

Thus **at p=13**, any such rho is a *square* in F_(13²), while the actual original E3/F_(13²) relative to the explicit F_13 model is a *nonsquare quadratic twist*. Therefore rho cannot simply be declared the genuine original-E3 quadratic twist parameter in the 13-class. At **p=19**, both are nonsquares and their square-classes agree, but that parity alone does not identify a concrete geometric curve isomorphism, differential pullback or native H0/B0 operator. This is a **geometric-vs-auxiliary coefficient semantic discriminator**: operator norm and elliptic quadratic-twist character are different typed observations; passing one does not imply the other. It does not refute the earlier abstract sign-correction construction.

## Exact computation and source/observer accounting

Checker: `d25_original_E3_j_twist_comparator_check_20261108.py` beside this note. Standard-library exact modular arithmetic:
- all 77 primes p≤2000 in the two target classes: direct computation of original Weierstrass j from c4³/Δ, Hilbert polynomial identity, absence of special j, and conjugate collision criterion;
- p=13,19: exhaustive **original-E3 F_(p²) points** and reference-E_j F_p points, plus exact invariant-ratio d and norm-square-class;
- p=373: original j=59+43s, still nonexceptional, with conjugates distinct.

**BRC: COMPOSE_APPLIED.** Carrier consists of original curve E3 over labelled k=F_(p²), conjugate CM j-fiber labels, actual identity-preserving self-automorphism group, explicit F_p reference model, invariant ratio's square class and its norm/Legendre readout, original geometric Frobenius, and **separately** the auxiliary σ-semilinear M/rho. The proved quotient to a square class is valid only for the quadratic-twist observer, not for differential normalization, signed odd Green/Hesse or native [X]U. The two-coordinate quadratic field is external algebra, **not** a native Enterprise X6 two-dimensional slice. P000/ACTIVE worldview unmodified.

## Actual unchanged research frontier

The formal mother target remains `Delta_p−R_p≡0 modp` for both target residue classes and equivalently `W_p≡p modp³` via previously proved author-side exact source-port alignment. **Neither is proven by this new geometric diagnostic.** The required native same-original-class H0/B0 divided-power benchmark at p=373 remains #1559, `PENDING_OWNER / NOT_EXECUTED`: real [X]U mod139129, rank, semilinear F direction and eta, signed odd κ/Green/Hesse, original Delta−R, raw reproducible evidence and independent checker, then p=19. Native comparator must identify the *actual* curve/operator/differential mapping before interpreting rho or a twist.

Site status at 2026-11-08 10:11 Asia/Hong_Kong: local gateway `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`; exact native status/old receipt both returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`. Old request `onhour11-20261106-1400-exact-research-lane-continuation` retained for later receipt/reconcile; no new mutation, session, CLAIM, run, freeze or formal Result claimed. The required safe remediation is a separate Site-bound backend client and secure user-entered credential; the benchmark itself still needs a lawful executor. Future native run should inspect E3/reference model **twist sign**, not equate an auxiliary scalar with a geometric map solely by the semilinear square.

Source notes consumed:
- `research_notes/portable_direct/20261026_onhour_d25_uniform_E3_q_frobenius_sign_CM_three_torsion.md` (author-side π_q=+p);
- `research_notes/portable_direct/20261108_onhour_d25_original_e3_quartic_sign_obstruction.md` (author-side auxiliary scalar and p19 falsifier);
- original task publication `TP2-B6F4FC938FF94941C1B7` and frozen taskbook; native support `https://github.com/awdawmip/enterprise-math/issues/1559`.

**Status:** `AUTHOR_SIDE_EXACT_PROVED / 77_PRIME_MODULAR_REGRESSION / P13_P19_EXHAUSTIVE_GEOMETRIC_COUNTS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE`.
