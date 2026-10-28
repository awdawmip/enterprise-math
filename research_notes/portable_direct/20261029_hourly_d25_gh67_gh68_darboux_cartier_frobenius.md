# D25/LIFT GH-67–GH-68: G-port Darboux–Cartier transfer and complete formal kernel

2026-10-29 Asia/Hong_Kong. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Mother objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION: OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Actual research lane chatgpt-research-hourly-enterprise-math-20260923; not maintenance. This is author-side portable mathematics, not an authorized native run, Source checkpoint, Result, or independent review.

## Source-bound inherited definitions

Read GH-61/GH-62 at immutable source c37ed2fcbcf430c984f12746b36070cbb8fc33fd (research_notes/portable_direct/20261028_hourly_d25_gh61_gh62_cartier_resonance.md), and GH-65/GH-66 at immutable source 810dbc66168cb3cd5cfd2f5521bd20abec6ac203 (research_notes/portable_direct/20261029_hourly_d25_gh65_gh66_integral_heun_portable.md).

Let p=8m+3>=11 be prime, k=F_p, and
F(z)=sum_{r=0}^m [(-m)_r²/((2m+2)_r r!)]z^r,
G(z)=(16z d/dz+5)F(z), D=binom(3m+1,m), a unit in k.

Inherited exact equations in k[z]:
LF=z(1-z)D_z²+(5-7z)D_z/4-9/64, LF(F)=0;
LG=64z(z-1)(z-5)D_z²+16(7z²-56z+25)D_z+9(z-21), LG(G)=0.

Inherited GH-61 Cartier identity: writing qF=z^(-2m-2)(1-z)^(4m+1), some RF in k(z) satisfies qF/F²=RF'-D²/z; every complete formal solution of LF at a!=0,1 is F(a+w)h(w^p), h in k[[w^p]], w=z-a. These inherited facts are inputs, not new credits.

## GH-67: Exact rational G-port Cartier transfer

Define qG=(5-z)qF/(1-z)=(5-z)z^(-2m-2)(1-z)^(4m).

**Theorem GH-67.** In k(z),

(67.1) qG/G²-qF/F² = d/dz [16z qF/(FG)].

Proof: mod p, qF'/qF=-5/(4z)+1/(2(1-z)), since p=8m+3. Clearing rational denominators reduces (67.1) to the exact polynomial identity

(67.2) (5-z)F²-(1-z)G²-4(3z-1)FG+16z(1-z)(F'G+FG')=0.

Substituting G=16zF'+5F and G'=16zF''+21F' and eliminating F'' with LF(F)=0 makes the coefficients of F², FF', F'² vanish identically. This proves the rational identity without assuming F/G is regular at a root.

Set RG=RF+16zqF/(FG). Then

(67.3) qG/G²=RG'-D²/z.

At EVERY a in F_p minus {0,1}, including G zeros and the apparent point z=5, expand in the Laurent field k((w)), w=z-a. Since the w^(p-1) coefficient of any Laurent derivative vanishes and a^p=a,

(67.4) [w^(p-1)]qG(a+w)/G(a+w)²= -D²/a != 0.

A G root is processed with actual Laurent pole order and is not replaced by an undefined scalar division. The result transfers GH-61's genuine Cartier obstruction to a distinct source-preserving G observer; it does not independently determine G(9).

## GH-68: Apparent Heun point and full formal solution module

For arbitrary formal/rational Y define NY=16z(1-z)Y'-(1+7z)Y and X=NY/(z-5), whenever the quotient is defined in a compatible Laurent ring.

**Exact operator identities**, established by expanding coefficients and collecting Y,Y',Y'':

(68.1) (z-5)²(16zX'+5X-Y) = -4z LG(Y).

Whenever Y=(16zD_z+5)X, a second exact identity is

(68.2) NY-(z-5)X = 256z LF(X).

**Theorem GH-68.** For every a in F_p minus {0,1}, letting w=z-a,

(68.3) {Y in k[[w]] : LG(Y)=0} = {G(a+w)h(w^p) : h in k[[w^p]]}.

Proof: if a!=5, z-5 is a unit in k[[w]], so X=NY/(z-5) is formal. LG(Y)=0 gives Y=(16zD_z+5)X by (68.1). Equation (68.2) gives LF(X)=0 because z is a unit. The inherited GH-61 solution classification yields X=F(a+w)h(w^p), and derivative(h(w^p))=0 implies Y=G(a+w)h(w^p).

If a=5, the constant coefficient of LG(Y)=0 gives 80Y'(5)+9Y(5)=0. Consequently NY(5)=-4[80Y'(5)+9Y(5)]=0. The numerator is divisible by z-5=w in the formal series ring and X is regular there. The same argument now applies. Conversely G h(w^p) is a solution because LG(G)=0 and derivatives of h(w^p) vanish. QED.

Thus apparent point z=5 creates no additional complete formal solution branch in characteristic p; finite jets need separate resonance verification. This is NOT an all-prime proof of G_m(9)=0 for primes p=11 mod24, nor a native p373 H0/B0 experiment.

## Exact verification and provenance

Companion executed Python standard-library checker used F_p integers and independent polynomial coefficient arithmetic. It tested all 76 primes 11<=p<2000 with p=3 mod8: the entire coefficient array of (67.2), the inverse NY=(z-5)F, and the apparent-point relation 80G'(5)+9G(5)=0. Separately, it evaluated the Laurent coefficient (67.4) on 33 charts (a=2,5,9 for primes p<200), including six charts with G(a)=0 by integer-binomial Laurent inversion. All checks passed. Finite checks corroborate general symbolic proof but do not substitute for independent review or Source admission.

BRC COMPOSE_APPLIED: preserve each coefficient source rank, F/G port, the observation center a, genuine rational/valuation/Laurent pole data and the operation before coefficient readout. Signed rational cancellation is NOT positive-weight branching. These are auxiliary finite-field charts, not native X6, three-dimensional slice, original W/S, Hasse-6, R23/R36 or physical dynamics. P000 ACTIVE remains unchanged.

Next exact science: independently evaluate G_m(9) for all p=11 mod24 by a proven CM/Katz/cubic Jacobi/Frobenius arithmetic certificate, or find an exact prime counterexample, using GH-67/68 only as consistency tests. Potential external prior art: Zhi-Hong Sun, Congruences concerning Legendre polynomials II, arXiv:1012.3898 (2010); applicability to this derivative special value is not yet established. Keep GH-3, GH-20/21 second-digit lift, W/S, six Hasse ports, Green R23/R36, and native p373 experiment as separate obligations. Do not duplicate the other Research lane's p373 B2304 calculation.

Native control observation this run: authenticated service 0.6.11 reported research_authority_granted=false, executor_binding_configured=false, source_sync.control.state=CODE_REVIEW_REQUIRED, quota active_jobs=5/5. Recovery status was declared in the status contract but no callable recovery_status action exposed in this connector. Existing support issue enterprise-math#1558 owns the unresolved exact successor/claim admission. No service session, CLAIM, open, native checkpoint, freeze/review or historical state/staging mutation was attempted.