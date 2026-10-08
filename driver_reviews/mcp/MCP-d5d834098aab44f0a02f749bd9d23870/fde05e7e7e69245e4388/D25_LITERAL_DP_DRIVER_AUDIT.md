# D25 literal divided-power lift: incremental Driver audit

Status: BOUNDED_AUDIT_COMPLETE / AUTHOR_SOURCE_BYTES_VERIFIED / NO_BLOCKING_ERROR_FOUND / LIFT_OPEN.
Reviewer: EM-DVR-E33955; own session MCP-d5d834098aab44f0a02f749bd9d23870; active DA-93D032174BAD288F8F29, authenticated authority comment 6060336942.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7.
This audit is not an RR, DR, whole-Task acceptance, source-theorem refutation, or parent closure.

## Inputs and actual independence

The reviewed final author V2 is D25_LITERAL_DP_EIGENLIFT_OBSTRUCTION.md, SHA256 6f11308313f7e5f18351cc8e45238d4b33ebf0f79e6e531f1de043c7266beb19. The initial V1 hash was 2c06b302cacbbbccde6f20c38c01aee060ded3047ab52502c25c0c3e3d980f38; V2 adds the requested source-boundary clarification and actual validation status. The uniform proof was unchanged.
Author: EM-ENTERPRISE-B078A6, own RA-8C8E44B2AA373F98BC5952A3, session MCP-bb6f343045854a798ca781ee73de2e39, winning claim MCP-3d6d72356bcdfef82ab4cfc4, ER-7C265B422DC8E829AD44, authorized run RUN-252e05a5823d9e33ff848863 generation 1. Its original open receipt page explicitly records authorized=true, not merely transport SUCCEEDED.

I inherited the prior D25 frontier and Owner integration and assigned the source-normalization/compatible-lift question. I did not provide the author a formula or proof construction. I read the primary paper independently while the author was working, and checked the frozen new proof directly. This is independent checking of a directed claim, not blind discovery or independence inferred from a new identity. My review request concerned the ramified-field interpretation boundary and reporting only actual validation; no new mathematical derivation has been supplied to the author.

I did not import or run the author's checker. I subsequently read its source and actual output as author evidence. This review rests on the all-prime argument and exact source definitions.

The prior checkpoint and bounded audit were independently fetched through the GitHub connector and completely hash checked:
- ac6ee6c5a280c4209506a135392be09f30f35f2a / _checkpoint.json: SHA256 dab51c2f4cf508d6f048e7f52a7d1defd7c3d2a0a54e0418f4957f384a44675a, Git blob 86a1305ca21cd3c92129e4905e8e891dd94a6c89.
- 2db5273269e71da8f2660bc4e917a7e78920b406 / D25_INCREMENT_AUDIT.md: SHA256 055934d2115d6740dd36c57658efaca784450f8df59f7fc6c827f431d6fcde45, Git blob b36a0837660e8089c4cb8a1599c3a0704f820386.
The earlier fixed-coordinate exclusion is not re-proved here; only its source-lift boundary is affected.

## Independent check of the formal statement

Let M consist of zero-constant formal primitives B over K with integral derivative, and let I=xi A[[xi]], where A is unramified with uniformizer p. Then B=sum b_(n-1) xi^n/n with b_(n-1) integral. The quotient being tested is M/pI, rather than M/I.

For the literal substitution T(B)=B^theta(Phi), theta preserves p and Phi has zero constant term and reduction xi^(p^2). The chain rule proves T(M) is contained in M and T(pI) is contained in pI. Thus the operator is well defined on this declared quotient. No assumed CM action is needed for this elementary check.

At degree p, only terms n<=p of B can contribute because Phi has no constant term. Every coefficient of Phi used in those terms has degree <=p and is divisible by p. Hence the coefficient of Phi^n has valuation at least n. Division by n leaves valuation at least n-v_p(n), which is at least one throughout 1<=n<=p. In particular the n=p term retains valuation p-1, so the only potentially dangerous integration denominator is accounted for. Semilinearity does not change these bounds.

It follows that [xi^p]T(B) lies in pA. For lambda=pu with u a unit, [xi^p]lambda B=u b_(p-1). The equality T(B)-lambda B in pI forces b_(p-1) in pA. This is uniform in the declared prime range and in all higher coefficients; no finite test is needed to establish it.

An integral primitive correction F changes the defect by T(F)-lambda F. Modulo p this is Fbar^thetabar(xi^(p^2)), which has no degree-p term. It therefore cannot cure the obstruction for a unit b_(p-1). If two corrections of the same ordinary formal class both work, their difference reduces to zero after the injective coefficient automorphism and substitution. Their difference lies in pI. This proves uniqueness only conditional on existence, not existence.

For a specified integral comparison defect S and integral D_B, the equation for F modulo p is exactly
Sbar-D_Bbar=Fbar^thetabar(xi^(p^2)).
The necessary and sufficient support condition and inverse-coefficient construction stated in the author report follow. In particular the xi^p coefficient of F is read from the xi^(p^3) coefficient of that difference after inverse theta. This is a conditional extraction, not a source computation of S or kappa and not a smaller certificate meeting the whole LIFT Task target.

## Primary-source logic and scope

Primary source: Chisholm--Deines--Long--Nebe--Swisher, Mathematics 1 (2013), DOI 10.3390/math1010009. I recomputed PDF SHA256 3adacbce06377f7690237de150f5a48a0411d004703f5219f28c5691db6989e2 and directly inspected printed pages 25 and 26 as images, in addition to relevant extracted text.

Printed p.25:
- The CM eigenfunction statement initially concerns ordinary de Rham classes.
- Formal primitives and the semilinear substitution action are displayed.
- The divided-power quotient is printed with denominator pA[[xi]] and zero constant term.
- Proposition 16 asks for a degree-p^2 Frobenius lift commuting with the induced R action in the supersingular case. Commutation alone is not the displayed eigenrelation for the chosen lifted companion.
- The setup gives b_2^2=+/-p^2, so -b_2 has valuation one.

Printed p.26:
- The proof says both omega and nu are eigenfunctions of the degree-p^2 Phi with eigenvalue -b_2.
- Interpreting that sentence simultaneously as equality in the literal pI quotient and literal substitution gives exactly the hypothesis tested above.
- The same proof later adjoins p-torsion, works over a ramified extension, and invokes its maximal ideal. That paragraph must be distinguished from the original unramified A / pI implementation. This audit does not prove an obstruction for every alternative comparison, quotient, or intended crystalline interpretation.

The no-go is thus a precise incompatibility of a proposed combination of model, operator, eigenrelation and coefficient requirement. It does not logically negate the abstract proposition, the paper's theorem, accepted UR, or LIFT. It also does not show arbitrary CM-compatible gauges are available. For a genuinely unit companion, the uncorrected prescription already has no object before kappa is computed.

Linear unit coordinate changes and unit scalar normalization preserve whether the differential coefficient at degree p-1 is zero modulo p. They do not evade this low-order obstruction. No equality of deeper raw and twisted D25 digits is inferred.

## Routing and method harvest

The old ordinary-class gauge ambiguity and the new stronger literal-operator existence obstruction are different statements. This increment eliminates the uncorrected literal N-eigenlift prescription as an executable recipe for the missing companion. The source comparison/operator must be specified before solving that equation or extracting kappa.

Outstanding mathematical data: actual ordinary CM normalization c_p modulo p^2, the actual intended compatible lift/comparison defect, Lcomp, and the cutoff/endpoint R_p bridge. LIFT/JT2 and the arithmetic parent remain OPEN.

Method harvest: task-specific valuation and formal substitution obstruction; existing formal-series mathematics is reused. It does not justify a new general-purpose toolbox family. Author Q2 arithmetic reuse and finite regression, if delivered, are supporting evidence only. Native P000 space remains six-dimensional discrete Cell space with no native plane; all formal elliptic algebra here has external type and implies no full-X6 propagation.

Disposition: no blocking error found in the bounded uniform obstruction, integral-correction impossibility, conditional uniqueness, and specified-defect coefficient extraction. The requested ramified/maximal-ideal scope clarification is present in V2. No whole-Task acceptance or mathematical parent completion is made.

Author regression was actually run at p=13 and p=19, with candidate scalar fixtures c=1 and c=6. The author reconstructs multiplication-by-minus-p low jets from the formal logarithm and checks the required p-divisibility and defect coefficients. All four fixtures passed. I inspected the code and output, including precision accounting for division by p and omission of the high-valuation n=p contribution, but did not rerun it. These fixtures do not identify actual source c, prove the intended Frobenius comparison, or replace the uniform proof. Checker SHA256 3be023c4ae406d498aa8e8305e60f2cd52a849965a9183db8732a5648de5fa6a; output SHA256 42dac5bb48c73622c9958eed95b9988a256cac568dca72e899a9bebe5cf649bb.

Author checkpoint published with release=false by native request d25-source-lift-checkpoint-20261008-r2 (bridge #3255), Source 47bec72e89587dabc106e2604839806a962cc995; authenticated PROGRESS comment 6060906313. Prefix: research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-bb6f343045854a798ca781ee73de2e39/4aadeecdcffc19567a11/. I independently fetched the complete published report, checker, regression and checkpoint through the GitHub connector, recomputed their SHA256 and Git blob identifiers, and matched the report/checker/output against the reviewed local bytes.

- Report: SHA256 6f11308313f7e5f18351cc8e45238d4b33ebf0f79e6e531f1de043c7266beb19; Git blob 4ffa67ae20880f4fdc564812624498128c5e2b21.
- Checker: SHA256 3be023c4ae406d498aa8e8305e60f2cd52a849965a9183db8732a5648de5fa6a; Git blob eb21f2e9bf38c111a60500267ab0164231f1fbe5.
- Regression: SHA256 42dac5bb48c73622c9958eed95b9988a256cac568dca72e899a9bebe5cf649bb; Git blob 334b9484b14378b7896d46bce931721a149eae41.
- Checkpoint: SHA256 ff6c576c3abcb830894038e056b568d4d36eae29b144d84b00ed837103385bfb; Git blob 224d10abe5d73ce3edd3ccaffcb61ada7027f3cf.

The checkpoint preserves earlier completed units and no-repeat conditions, adds only this increment, and explicitly retains LIFT/JT2 open. Its release=false preserves the current authorized researcher for further work. The next concrete source is the author-hosted Katz reference, https://web.math.princeton.edu/~nmk/old/CrCohDModJacSum.pdf; it has now been obtained. This report makes no new claim from that reference: its exact comparison/model is a separate ongoing obligation, alongside ordinary CM normalization. No repeated original publication or old run was used.

Driver-ID: EM-DVR-E33955 / CONTROL_PLANE


