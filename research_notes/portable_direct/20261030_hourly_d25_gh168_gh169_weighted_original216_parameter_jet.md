# GH-168/GH-169 — Original weighted-216 CM first/second jets and the p²-parameter alias obstruction

2026-10-30. **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.** Author-side auxiliary arithmetic, not the native p=373 H0/B0 experiment or an admitted all-prime LIFT proof.

**Binding scope:** mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Actual Research logical ID chatgpt-research-hourly-enterprise-math-20260923; the onhour Research lane and maintenance lane remain distinct. P000 ACTIVE_LOCKED; no promotion of this auxiliary Fp model to native X6 geometry.

## Source-correct original weighted family

Let p=6m+1>=13 be prime with p mod24 in {13,19}. Work over Z_(p). The SOURCE ORIGINAL fixed-parameter sum and its explicitly auxiliary parameter deformation are

$$
a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3\,2^n}
=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},
\qquad {\cal A}_p(X)=\sum_{n=0}^{p-1}(6n+1)a_n X^n,\quad A_p={\cal A}_p(1).
$$

The original Task fixes X=1. The auxiliary X deformation must not substitute a differently tuned parameter for the frozen LIFT target.

Put

$$
b_n=\frac{(1/6)_n(1/3)_n}{(n!)^2\,2^n},\quad
f_p(X)=\sum_{n=0}^m(b_n\bmod p)X^n\in\mathbb F_p[X].
$$

The already-accepted parent source supplies CM0 and first digit, **consumed rather than reproved**:

$$
f_p(1)=0,\qquad \bar h=\sum_{n=0}^m(12n+1)b_n=12f_p'(1)\ne0\pmod p,
\qquad A_p\equiv p\pmod{p^2}.
$$

The still-open hard target is A_p≡p (mod p³), equivalently Delta_p=R_p^(original) modp under the previously verified original signed Clausen transfer. The GH-166/GH-167 signed source R and the other onhour lane's already published harmonic/reflection results are not redefined or credited as new here.

## GH-168: complete finite-polynomial identity and nonzero original weighted first jet

**Theorem** (all p in the exact target classes):

$$
\boxed{{\cal A}_p(X)\equiv f_p(X)^2+12Xf_p(X)f_p'(X)\pmod p\quad\text{in }\mathbb F_p[X].}\tag{J0}
$$

Consequently

$$
\boxed{{\cal A}_p'(1)=\frac{\bar h^2}{12}\ne0\pmod p.}\tag{J1}
$$

**Proof.** Apply the classical Clausen formal power-series identity with a=1/6, b=1/3 and argument X/2:

$$
{}_2F_1(1/6,1/3;1;X/2)^2={}_3F_2(1/2,1/3,2/3;1,1;X/2).
$$

See NIST DLMF §16.12.2: https://dlmf.nist.gov/16.12.E2 . All factorial denominators up to n=p-1 are p-units. For n>m the coefficient b_n is zero modp (the factor 6m+1=p first appears at n=m+1). For n>2m the coefficient a_n is zero modp (the factor 3(2m)+1=p first appears at n=2m+1). Thus the *complete* finite polynomial sum of a_n X^n reduces coefficientwise to f_p(X)^2; no hidden degree>2m part remains. The source weight 6n+1 is exactly the operator 1+6X∂_X. Applying it gives (J0). At X=1, f_p(1)=0 and \bar h=12f_p'(1) is a unit, so one derivative yields (J1). QED.

## GH-169: exact second jet, universal curvature, and p² alias failure

The same truncated f_p satisfies its hypergeometric differential equation in Fp[X]:

$$
\boxed{X(2-X)f_p''+(2-\tfrac32X)f_p'-\tfrac1{18}f_p=0.}\tag{ODE}
$$

This follows coefficientwise from b_(n+1)/b_n=(6n+1)(3n+1)/(36(n+1)²); at the top index n=m, factor 6m+1=p makes the omitted terminal coefficient vanish modulo p. There is no spurious use of a homogeneous finite p³ equation: (ODE) is only an Fp polynomial identity.

At X=1, CM0 and (ODE) imply f_p''(1)=-f_p'(1)/2. Twice differentiating (J0), at f_p(1)=0, gives

$$
{\cal A}_p''(1)=26 f_p'(1)^2+36 f_p'(1)f_p''(1)
=8 f_p'(1)^2=\bar h^2/18\pmod p.
$$

Hence the second all-target-prime theorem:

$$
\boxed{{\cal A}_p''(1)=\bar h^2/18,\qquad 3{\cal A}_p''(1)=2{\cal A}_p'(1)\pmod p.}\tag{J2}
$$

**Source-typed observer obstruction.** For any p-integral u, using integer binomial expansions modulo p³,

$$
{\cal A}_p(1+p^2u)\equiv {\cal A}_p(1)+p^2u{\cal A}_p'(1)
\equiv {\cal A}_p(1)+p^2u\bar h^2/12 \pmod{p^3}.
$$

Because A_p(1)≡p modp², normalized D_p(X)=({\cal A}_p(X)-p)/p² modp is defined on the fiber X≡1 modp². It obeys

$$
\boxed{D_p(1+p^2u)-D_p(1)=u\bar h^2/12\pmod p.}\tag{J3}
$$

Since \bar h is a unit, this maps u modp bijectively to every normalized residual in Fp. **Remembering only X modp² erases the entire future second-digit observer.** The smallest one-step repair coordinate on this fiber is (X-1)/p² modp. This is an explicit BRC COMPOSE_APPLIED sufficiency/fiber theorem: original signed rational coefficient provenance, p-adic valuation and direction/parameter must be retained before subtracting p and dividing by p². It neither proves D_p(1)=0 nor permits parameter tuning to fake the frozen target.

### Exact original weighted 216 witness at p=373

The original frozen-parameter arithmetic gives A_373(1)≡373 mod373³ (previously known finite certificate). The independently computed low-unit \bar h=171 gives A'_373(1)=292, A''_373(1)=319 modulo 373. Full original-216 recurrence at the *second* auxiliary input yields

$$
\boxed{{\cal A}_{373}(1+373^2)\equiv40\,626\,041
=373+292\cdot373^2\pmod{373^3},\qquad373^3=51\,895\,117.}
$$

Therefore X=1 and X=1+373² are identical modulo 373² yet have distinct normalized second digits 0 and 292. This is **not** a counterexample to fixed-X=1 LIFT and **not** a native H0/B0 divided-power execution.

Other exact originals (p: hbar, slope, curvature, A_p(1+p²) modulo p³):
13: 6,3,2,520;
19: 12,12,8,4351;
157: 80,10,59,246647;
373: 171,292,319,40626041.

## Executed exact validation

Companion program: research_notes/portable_direct/d25_gh168_weighted_216_cm_jet_check.py . Executed with Python standard library, modular inverses only, no floats. 166 target primes p<5000 passed original 216 mod p³ and CM0, unit, first-digit, both jets, and perturbed original weighted recurrence. For all 15 target primes p<=283, checked **every coefficient** of the full Clausen polynomial identity independently. Terminal:

PASS_GH168_ORIGINAL_WEIGHTED_216_CM_JET_TRANSVERSALITY_EXACT

Finite checks audit the independently derived proof and the indicated instances; they do NOT constitute an all-prime LIFT proof. This is author-side unreviewed, not independent Driver accepted mathematics, and no native Source checkpoint.

## Durable frontier / next scientific action

Mother D25/LIFT/JT2 remains OPEN. The mathematically open **constant term** D_p(1)=Delta_p-R_p^(original) must still be shown to vanish (or exactly refuted) for *both* target residue classes. The first and second deformation jets now have a proof, so re-deriving these jets does not solve that source-pinned constant. Pursue an independent finite telescoping/CM/Gauss-Manin identity canceling the full signed GH-166/GH-167 three-port combination while consuming the other lane's harmonic and high-tail C identities without recrediting them. Genuine native p=373 divided-power, [X]U modulo p², semilinear Frobenius/eta, signed odd Green/Hesse and κ remain for authorized original experimental owner (#1559). Control recovery (#1558) has not granted this Research lane a new CLAIM/OPEN, source-native checkpoint or formal Result. Retain old sessions/requests/staging unmodified; do not borrow the CONTROL_PLANE_MAINTENANCE identity, change frozen scientific source pins, task schedule or notification settings.
