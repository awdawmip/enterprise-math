# D25/LIFT — original E3 fixed-parameter formal coefficient, first-digit bridge, and second-digit typed mismatch

Date: 2026-11-11 (Asia/Hong_Kong). **AUTHOR_SIDE / exact algebraic first-digit identity + eight exact finite p³ certificates / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0 / NO_SOURCE_CHECKPOINT**.

Parent objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`; original science pin **`c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged**. The Research-onhour lane `chatgpt-research-onhour-enterprise-math-20260923` is distinct from maintenance. No private issued session, current winning CLAIM/open run, Driver admission, or native experiment is asserted.

## 1. Exact unmodified original geometric differential

Use the original d=3 curve in Chisholm–Deines–Long–Nebe–Swisher (2013), Lemma 12:

```text
E3(t): y^2+xy+(t/27)y=x^3,
t(lambda)=(1-sqrt(1-lambda))/2, lambda=1/2,
R_r=(Z/p^r Z)[T]/(T^2-2), sqrt(1-lambda)=T/2,
t0=(2-T)/4; sigma(T)=-T.
```

With the **original** local uniformizer `z=-x/y` and `w=-1/y`, direct substitution gives

```text
(1-z)w-(t/27)w^2=z^3,    w(0)=0,
omega=dx/(2y+x+t/27)=dz/[1-z-2(t/27)w]
     =sum_{n>=0} H_{3,n}(t) z^n dz.
```

The second equality follows by implicit differentiation and the curve equation. Differentiate the coefficients with respect to the original curve parameter t, at **fixed z**. This is a specified formal observer, not an unverified identification with crystalline Frobenius or a canonically normalized Gauss–Manin class.

Independently, the published exact integer formula for the same coefficient is, for n=p−1,

```text
H_{3,p-1}(t)=sum_{j=0}^{floor((p-1)/3)}
  binom(p-1-j,j) binom(p-1-2j,j) (t/27)^j.
```

Its formal t derivative is obtained by differentiating each exact term. Two independent computational routes — implicit formal-group recursion and this exact binomial polynomial — agree at all eight checked target primes through modulus p³, for both H and dH/dt.

## 2. Uniform first-digit original source-to-scalar identity (proved, p=6m+1)

For every prime p=6m+1>3, define

```text
J_m(lambda)=sum_{k=0}^m binom(m,k)binom(2m,k)lambda^k.
B_k=((1/6)_k(1/3)_k)/(2^k (k!)^2),
g=sum_{k=0}^{p-1} B_k, h=sum_{k=0}^{p-1}(12k+1)B_k.
```

Lemma 12 gives `H_{3,p-1}(t) = 2F1(1/3,2/3;1;t) mod p`. Since `1/3=-2m` and `2/3=2m+1` in F_p, the terminating expression is the Legendre polynomial `P_{2m}(1-2t)`. The classical even-degree identity

```text
P_{2m}(sqrt(1-lambda))
  = 2F1(-m,m+1/2;1;lambda)
```

becomes `J_m(lambda)` modulo p, because `m+1/2=-2m mod p`. Meanwhile the original B_k reduce to the J_m coefficients and truncate at k=m mod p. Differentiating this **polynomial identity** gives the source-typed relation

```text
g = H_{3,p-1}(t(1/2))                  (mod p),
h = H_{3,p-1}(t(1/2))
    +6*(d/dlambda) H_{3,p-1}(t(lambda))|lambda=1/2 (mod p),
dt/dlambda = T/4 at lambda=1/2.
```

This proof holds in the quadratic coefficient ring, with either split or inert type of 2. For the task's p≡13,19 (mod 24) the accepted supersingular source has H≡g≡0 mod p; the even Legendre parity forces dH/dt mod p into the **sigma-odd T-coordinate**. The original scalar h is recovered by multiplying that derivative by 6T/4. This uses the true unmodified E3 differential and its local uniformizer; it is not a second proof of the already accepted UR/JT0.

## 3. New exact p373 second-digit obstruction in the original source representation

At p=373, q=p³=51,895,117, p²=139,129, in `R_3`, the two independent algorithms give

```text
H := H_{3,372}(t0)          = 46,042,747 + 33,130,606 T   (mod q)
dH/dt                      =  5,280,934 + 49,750,797 T   (mod q)
H/p                        =    123,439 +     88,822 T   (mod p²)
(dH/dt) mod p               = 57 T
g mod q                     = 24,495,656
h mod q                     =  4,236,705 (h mod p² = 62,835)
H+6*(T/4)*(dH/dt)          = 39,609,787 + 41,052,007 T  (mod q).
```

The proven first-digit bridge gives h mod373=171 on both sides. One digit further, **the raw original geometric port retains a nonzero typed correction**:

```text
[H-g]/p                 = 325 + 48T (mod 373),
[H+6 d_lambda H - h]/p  =  92 + 24T (mod 373).
```

For the second expression, before dividing by p the actual difference modulo p² is `34,316+8,952T =373(92+24T)`. The 24T term is sigma-odd. It is a genuine exact **fixed-z formal-differential vs frozen scalar-port discrepancy**, not an inconsistency of the proved mod-p identity. Scalar projection or norm is not an observer-safe replacement at the second digit without a proved comparison/gauge/twist/connection map.

## 4. Executed finite reproduction and BRC provenance

Eight primes `13,19,37,43,109,139,157,373`, both target residue classes: direct binomial and independent original formal expansion agree for H and derivative modulo p³; frozen B_n original scalar is computed separately; the all-prime mod-p bridge passes.

Typed second-digit residues `(H+6 d_lambda H-h)/p mod p` in ordered basis `(1,T)`:

| p | scalar component | T component |
|---:|---:|---:|
| 13 | 8 | 0 |
| 19 | 13 | 11 |
| 37 | 0 | 4 |
| 43 | 3 | 8 |
| 109 | 94 | 48 |
| 139 | 23 | 72 |
| 157 | 33 | 62 |
| 373 | **92** | **24** |

Reproducible Python 3, standard-library integers, no floats:
`research_notes/portable_direct/d25_e3_original_formal_derivative_second_digit_20261111.py`.
It explicitly asserts the p373 vectors, computes in `(Z/p³)[T]/(T²−2)` and checks both derivations. The quadratic ring and two coordinates are a **typed external calculation surface**, not the six-dimensional P000 native space or a complete three-dimensional slice.

## 5. Highest frontier and precise next action

**Source native H0/B0 remains NOT_RUN / PENDING_OWNER.** This finite exact certificate supplies a discriminating acceptance datum for the true frozen H0/B0 divided-power evaluator: if its actual original-class source-to-scalar map identifies the raw fixed-z derivative observer with the frozen h through p², that map must account for the measured correction `92+24T` (or demonstrate the precise source-normalization mechanism that changes the observer). Do not hard-code it into a native Frobenius; first establish actual module rank, basis, semilinear Frobenius direction and eta, raw `[X]U mod139129`, signed odd Green/Hesse kappa, and original Delta-R, with independent reproduction. The previously verified original scalar Delta=R=196 at p373 is consumed unchanged.

Existing support path: Enterprise Math Issue #1559, OPEN / PENDING_OWNER at this run's verified read. No new task, maintenance claim, execution scheduler or admissibility decision created. Research lane recovery_status returned `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; exact Source continuation `onhour11-20261111-0838-exact-cont` returned SUCCEEDED with `execution_authorized=false`. Preserve the prior source claims/continuations and frozen input separately. The faithful project artifact and program are **author-side durable evidence only**; the next formal checkpoint/Result is due only from a genuinely authorized own Researcher session and current winning claim.

Sources: [2013 paper, §4.1 Lemma 12 and original E3 family](https://www.mdpi.com/2227-7390/1/1/9); frozen Task publication `TP2-B6F4FC938FF94941C1B7`; prior accepted CM0/UR proofs and `research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md`; preserved prior Source Hesse candidate and direct scalar fixture (separate evidence class).
