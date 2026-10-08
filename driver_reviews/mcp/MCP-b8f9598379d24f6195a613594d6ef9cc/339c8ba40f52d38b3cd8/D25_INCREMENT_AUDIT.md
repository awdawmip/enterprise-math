# D25 checkpoint increment: independent bounded audit

Status: BOUNDED_AUDIT_COMPLETE / SOURCE_BYTES_BOUND / NO_BLOCKING_ERROR_FOUND / LIFT_OPEN.

Reviewer: Driver EM-DVR-011C81; own session MCP-b8f9598379d24f6195a613594d6ef9cc; ACTIVE DA-653026BAED7F2AA7D352 (activation request d25-audit-activate-20261008-03, GitHub bridge issue 3158). Task scope: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. No task claim, Result, RR or DR is created by this report.

## Evidence and independence

The reviewed frozen local draft is `D25_FIXED_X_BRIDGE_DRAFT.md`, SHA256 `fcb9eb4df92688ef827e9da46632369be7f9b0aee8dde0be8040385c47cedc13`. The supplied author's checker SHA256 is `bf5468725d80f9344f9b980239049beb908d381c07305df0cfadf1f55bd18024`; its regression output SHA256 is `48bd87b98a198bc520090a9e5661235f62c17bd13c32711c932e3637bf1b0235`. I read the draft before inspecting regression output. I neither imported nor executed the author's checker. Its four output rows are author-reported evidence, not my independent proof.

I was given only the audit scope and frozen filenames/hashes before reading the draft. I did not receive the Owner's derivation hints or private mathematical conversation. The draft itself discloses the Owner's fixed-x route suggestion; that disclosure was first encountered as part of the claim being reviewed. After the draft, I read the predecessor note to distinguish the inherited interface from this increment. That predecessor is not accepted here merely because it is inherited. My prior contribution list at session creation was truthfully empty. This is independent mathematical checking of a disclosed claim, not blind rediscovery or independence established solely by a new ID.

Primary external source: Chisholm–Deines–Long–Nebe–Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), DOI `10.3390/math1010009`; supplied PDF SHA256 `3adacbce06377f7690237de150f5a48a0411d004703f5219f28c5691db6989e2`, verified locally. Relevant printed pages: 18–19 (Gauss–Manin eigenclass discussion), 20–21 (formal differential), 25–26 (ordinary/divided-power quotients and Proposition 16), 27–28 (normalization, parameter and quartic twist).

I independently fetched the complete note, checkpoint, author checker and author regression from `awdawmip/enterprise-math` at immutable commit `ac6ee6c5a280c4209506a135392be09f30f35f2a` using the connected GitHub tool. All four full-content SHA256 values match the supplied frozen values. The note's Git blob is `49af9376e405156dae2c0ced5b122db751cbe6a5`; the checkpoint's Git blob is `86a1305ca21cd3c92129e4905e8e891dd94a6c89`, SHA256 `dab51c2f4cf508d6f048e7f52a7d1defd7c3d2a0a54e0418f4957f384a44675a`. The checkpoint remains `AUTHOR_REPORTED_SOURCE_BYTES_ONLY_NOT_MATHEMATICAL_ACCEPTANCE`, explicitly retains LIFT/JT2 open, and preserves inherited units. This audit adjudicates only its last two completed-unit increments and affected premises, not all prior units.

- [Reviewed immutable note](https://github.com/awdawmip/enterprise-math/blob/ac6ee6c5a280c4209506a135392be09f30f35f2a/research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-078376aa00ee4999935d36d5b9766cd6/455dda816873d7acb044/D25_FIXED_X_BRIDGE_DRAFT.md)
- [Immutable checkpoint](https://github.com/awdawmip/enterprise-math/blob/ac6ee6c5a280c4209506a135392be09f30f35f2a/research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-078376aa00ee4999935d36d5b9766cd6/455dda816873d7acb044/_checkpoint.json)

## Verified local algebra

Put `F=y^2+xy+ay-x^3`, `a=t/27`, `D=F_y=2y+x+a`. Differentiation with x fixed gives `y_t=-y/(27D)` and `D_t=(x+a)/(27D)`. Thus `partial_t(dx/D)=-(x+a)dx/(27D^3)`. At the target, `lambda_t=4(1-2t)=2s` and `t_lambda=1/(2s)=s/4`, yielding the stated `G_x=-s(x+a)dx/(108D^3)`. This factor is evaluated after differentiating the family; no derivative of the target relation `s^2=2` is imposed on the family parameter.

Direct differentiation of `xi=-x/y`, using `F=0`, gives `xi_t|x=xi/(27D)` and `xi_x|t=(y+x+2a)/(Dy)`. Therefore `x_t|xi=x/[27(y+x+2a)]`. The vertical difference of the two lifts contracts with `omega=dx/D` to `x/[27D(y+x+2a)]`. Cartan's formula in relative degree one gives the plus sign `G_xi-G_x=d_rel Q_lambda`. Consequently coefficient differentiation gives the exact, unreduced identity `J_x=J_xi-p q_p`. The sign is verified independently of the author's checker.

Writing `w=-1/y=xi^3 V` gives `x=xi^-2/V`, `y=-xi^-3/V`, `V=1+xi V+a xi^3 V^2`. With the branch `S(0)=1`, the relations are `W=-S`, `U=-(3-xi+S)/2`, `V=2/(1-xi+S)`. These prove both displayed forms of Q and the displayed G_x/dxi formula. They also give `Q=s xi^4/216+O(xi^5)` and zero constant terms in both derivative coefficients.

All constant denominators introduced here involve only 2 and 3. The series denominators in the closed form of Q have constant terms 1, 2 and 4. Thus `Q in A[[xi]]` for every p>3, not merely for the four regressed target primes.

## Independent all-prime residue check

Let `f=xi^-1=-y/x`, `P(x)=D^2=4x^3+(x+a)^2`. Since `Q=-(s/108)xi H/D` and `H dxi=dx/D`, reduction modulo p gives

`q_p=-(s/108) Res_O(f^p dx/P)`.

Elliptic inversion fixes O and x and sends y to `-x-a-y`. Hence `f+iota^*f=1+a/x`, and invariance of residue under this local automorphism implies

`2 Res_O(f^p dx/P)=Res_O((1+a^p/x^p)dx/P)`

in characteristic p. This uses the characteristic-p binomial identity, not a Frobenius lift or the CM action. In particular it does not assume `s^p=s`; target p=13 or 19 modulo 24 has the nontrivial quadratic residue-field Frobenius.

For an explicit check of the last residue, set `u=1/x`. The differential on the right is

`-(1+a^p u^p) u/(4+u+2a u^2+a^2 u^3) du`.

It is regular at u=0 for p>3. Its pullback to O is regular and therefore has zero residue. Since 2 is invertible, the original residue is zero. Thus `q_p in pA` and `J_x=J_xi mod p^2`. This supplies a proof for the full declared prime range; finite series tests are only regression.

The discriminant of the supplied Weierstrass model is `a^3(1-27a)=t^3(1-t)/27^3`. At the target, `t(1-t)=1/8`, so t and 1-t are units at every p>3 and all target primes have good reduction. The coefficient ring can be the integers in an unramified extension containing s; for split primes s may already lie in Z_p, and for the target inert quadratic primes the ring is W(F_(p^2)). The branch is retained throughout. No global native-X6 assertion follows from this external algebraic observer calculation.

## Precision and normalization boundary

Using the same actual unit c_p, with the same lift modulo p^2, is essential when comparing the two divided scalars. The exact difference is `L_x-L_xi=-c_0 alpha_0 q_p mod p`, hence zero by the lemma. J modulo p^2 and alphaHat modulo p^2 are the needed input precision; division by p loses one digit only after the numerator is known divisible by p. Changing c_p modulo p^2 can change the divided scalar and is not covered by this zero-correction result.

The report correctly treats the saved alphaHat/raw-H and first-digit interfaces as inherited premises. I have not repeated their proof or the 166-prime predecessor scan. The conclusion of this increment is equality of two candidate observers conditional on those interfaces; it does not evaluate either observer, prove a source normalization, set c_p=6, set C_p=0, or absorb the quartic factor tau_p.

For a fixed normalization and the same ordinary formal class, let the actual companion differ from the candidate by `dF`, where `F in A[[xi]]` and `F(0)=0`. Then `delta b(p-1)=p[xi^p]F`, and with `a(p-1)=p alphaHat` the product shift modulo p^3 is `p^2 alpha_0 [xi^p]F`. Thus kappa is precisely the missing image at this one observer. Calling it necessary and sufficient is valid only under the draft's stated fixed-c_p/fixed-class/unit-alpha_0 conditions. It does not claim that an arbitrary kappa extends to a genuine compatible CM/Frobenius lift.

## Proposition 16 boundary

The source on printed p.25 explicitly divides formal primitives by A[[xi]] in the ordinary quotient and by pA[[xi]] in the divided-power quotient, with zero constant term understood. An integral primitive F can therefore leave the former unchanged while changing the latter. The source treats omega and nu as R-eigenclasses and assumes a degree-p Frobenius lift in the ordinary case, respectively degree-p^2 in the supersingular case, commuting with R on the divided-power space under the chosen uniformizer. Its coefficient action is sigma-semilinear. Pages 27–28 also change uniformizer using the quartic twist when applying that proposition.

Accordingly, preservation of an ordinary de Rham class, leading coefficient and low-precision coefficient product does not prove preservation of the full Proposition-16 setup. In fact Q has the p-unit coefficient s/216 at xi^4, so for a unit c_p the entire class [c_p Q] in A[[xi]]/pA[[xi]] is nonzero, even though its xi^p coefficient is zero. Equality at this one observer must not be relabeled equality of divided-power classes. The new draft correctly retracts any stronger reading of the inherited exact-form gauge argument: it is an insufficiency result for weaker retained data, not a no-go once compatible lifted CM/Frobenius data are supplied. Nor does the quoted source text explicitly identify partial_lambda with the particular fixed-x rational representative. The audit finds no evidence justifying such an identification at the missing digit.

The coordinate comparison of this increment does not require Proposition 16. Its vanishing correction is proved directly. The source's theorem and Frobenius-lift existence arguments have not been independently re-proved in this bounded audit; only the premises invoked by this draft and the claimed implication boundary have been checked.

## Independent finite verification and disposition

`independent_series_check.py` was written after the hand derivation and imports no author code. It obtains V and H from Catalan/binomial coefficient expansions over QQ[a], inverts `T=2-xi-a xi^3V`, and checks the exact polynomial identity `H_(n-1)'(a)-Gx_scaled[n-1]=n Q_scaled[n]` for n=1 through 43. It separately checks that every coefficient of Q_scaled[p] is p-divisible with p-unit denominator for p=5,7,11,13,17,19,23,29,31,37,41,43. All assertions passed. This includes non-target prime classes and the first allowed primes. These tests supplement, and do not replace, the residue proof.

Verdict: no blocking mathematical error found in the bounded increment. Verified: the fixed-x representative, exact lift-change primitive and sign, integrality and target good reduction, and zero correction to the declared divided digit for the same normalization. Verified as source interpretation: full divided-power/Frobenius premises must not be discarded.

Remaining uncertainty: actual normalized CM companion, c_p modulo p^2, its compatible divided-power lift and kappa, the value of Lcomp, the endpoint/cutoff R_p bridge, and LIFT/JT2. This report neither accepts the whole Task nor closes the parent objective. The no-repeat consequence is limited to this particular fixed-x/fixed-xi coordinate-change route; it is not a no-go for other compatible source lifts.

Driver-ID: EM-DVR-011C81 / CONTROL_PLANE
Global-Knowledge-Sync: main@9c0c7038e6b6e4036a52d148c800b9759173b8ed / GLOBAL_KNOWLEDGE_V1
