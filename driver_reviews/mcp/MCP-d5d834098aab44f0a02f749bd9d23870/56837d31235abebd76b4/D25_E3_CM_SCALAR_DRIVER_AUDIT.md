# D25 E3 period gauge and ordinary CM scalar: Driver audit

Status: BOUNDED_AUDIT_COMPLETE / AUTHOR_SOURCE_BYTES_VERIFIED / NO_BLOCKING_ERROR_FOUND / LIFT_OPEN.
Reviewer: EM-DVR-E33955; session MCP-d5d834098aab44f0a02f749bd9d23870; DA-93D032174BAD288F8F29, authenticated authority comment 6060336942.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7.

## Reviewed claim and exposure

Author: EM-ENTERPRISE-B078A6, session MCP-bb6f343045854a798ca781ee73de2e39, RA-8C8E44B2AA373F98BC5952A3, claim MCP-3d6d72356bcdfef82ab4cfc4, ER-7C265B422DC8E829AD44, authorized run RUN-252e05a5823d9e33ff848863 generation 1. The frozen V1 is D25_E3_PERIOD_GAUGE_CM_SCALAR.md, SHA256 8b33c0d99e87f4e97c7091c269668d07d035e5cc830ebd245df4cc7d1f886e27.

The new result is the exact Picard–Fuchs certificate and constant period gauge for the actual E3 invariant differential, then the source-bound value c_CM=6 for the ordinary normalized anti-CM class in the original untwisted Gauss–Manin basis. The author explicitly distinguishes this scalar from a scalar introduced to normalize a desired finite coefficient product. This audit does not collapse that distinction.

I inherited the old D25 frontier and directed the source-normalization question. The author selected and produced the polynomial certificate, cycle argument, scalar-identification argument and Guillera source locator. I supplied none of those constructions or formulas. I read the complete frozen report, its checker and output, and independently checked the certificate and source passages. This is directed incremental review with shared history, not a clean discovery fork. The second Katz comparison increment is reviewed separately and is not used as a proved actual DP model here.

## Exact certificate and analytic gauge

The curve is y^2+xy+(t/27)y=x^3, D=2y+x+t/27, P=D^2=4x^3+(x+t/27)^2 and omega=dx/D. At fixed x, differentiating P^(-1/2) gives exactly the first and second parameter derivatives printed in the report.

For L_t=t(1-t)partial_t^2+(1-2t)partial_t-2/9, the supplied polynomial R proves L_t omega=d_x(R/D^3). The identity is an exact rational-function statement on the curve. I independently entered P and the frozen R into SymPy 1.14.0, directly differentiated P^(-1/2) and R P^(-3/2), multiplied their difference by P^(5/2), and obtained zero. I also checked the three change-of-parameter coefficient identities for lambda=4t(1-t), with exact zero residuals. I did not import or run the author checker. My local record is E3_DRIVER_CERTIFICATE_CHECK.json; this verifies a supplied certificate, not an independent construction of R.

The rational function R/D^3 is single-valued on the elliptic curve; its differential integrates to zero along a closed cycle avoiding its poles. The fixed small x-circle with 0<r<1/4 surrounds the two roots approaching the node at zero and excludes the root approaching -1/4. For small t, the square root on an annular neighborhood has even monodromy around the circle, and the selected lift is closed. The limit D=x sqrt(1+4x) is uniformly nonzero along that contour. Thus the cycle period and its parameter derivatives are analytic there, despite degeneration of the central curve at the excluded node.

The residue at x=0 is one, fixing the limiting period to 2 pi i with the stated orientation. Substitution of an analytic power series into L_t gives (n+1)^2 q_(n+1)=(n+1/3)(n+2/3)q_n. This uniquely specifies the analytic solution and establishes p(t)=2 pi i F(1/3,2/3;1;t), with a constant, rather than parameter-dependent, factor. No finite list of Taylor coefficients is substituted for this uniqueness argument.

The real continuation from small positive t to t0=(2-sqrt(2))/4 avoids singular fibers t=0,1. The declared lambda branch is correct. The checked change of variable gives the Gauss equation for F(1/6,1/3;1;lambda). Its ordinary convergent Clausen square is the stated S(lambda) with parameters (1/2,1/3,2/3). This is an analytic identity and does not replay the finite-prime Clausen/UR proof.

## Source-bound scalar deduction

I recomputed both source PDF hashes and visually inspected the decisive original passages:

- Chisholm et al., Mathematics 1 (2013), DOI 10.3390/math1010009; PDF SHA256 3adacbce06377f7690237de150f5a48a0411d004703f5219f28c5691db6989e2. Printed p.11 gives the curve family, lambda=4t(1-t), equation (2.1), and uniqueness of the algebraic normalized Ramanujan pair a,delta. Printed p.18 gives the same-cycle CM eigenperiod product up to an algebraic multiple of pi. Printed p.27 states the assumed ordinary normalization nu=omega+c partial_lambda omega and the leading coefficients one. I additionally read Remark 7 and the analytic Clausen statement in extracted text. I do not claim a new proof of the source CM and uniqueness results.
- Jesus Guillera, A method for proving Ramanujan series for 1/pi, arXiv:1807.07394v4 (16 August 2018), https://arxiv.org/pdf/1807.07394v4; 146983 bytes, SHA256 8957b8ec11ee566a22f66e95f0036b9a288a95473b1902d87bbc6678762c0e83. Equation (1), p.1, uses a_G+b_G n and right side 1/pi. Table 3, p.10, positive-z first row, has level 3, degree 2, z=1/2, a_G=1/(3 sqrt(3)), b_G=6/(3 sqrt(3)). The text around (25) identifies level 3 with s=3. Dividing by a_G gives a=6 and delta=3 sqrt(3) in the 2013 convention. This is an actual cited analytic datum, not a finite-prime fit or target-defined normalization.

For the assumed ordinary algebraic class nu=omega+c_CM partial_lambda omega, Gauss–Manin differentiation on the transported cycle gives period 2 pi i(f+c_CM f'). Multiplying by the omega period yields -4 pi^2(S+(c_CM/2)S'). The cited CM period-product statement therefore makes the parenthesized term an algebraic multiple of 1/pi.

Rewriting this expression in the normalized series convention gives a'=c_CM/(2lambda). The cited uniqueness of the algebraic pair then forces c_CM=2lambda a. At lambda=1/2 and the independently sourced a=6, c_CM=6 exactly, hence in every permitted p-adic embedding modulo p^2. Algebraic proportionality constants and the factor -4 pi^2 are correctly absorbed in delta; there is no missing lambda or derivative factor.

This is conditional on the listed source CM and normalized-class premises, as openly stated by the author. It is not a new theorem proving all of those source premises from scratch. The invariant differential has leading coefficient one in the declared local frame; its fixed-frame parameter derivative has zero leading coefficient. This checks consistency with the ordinary representative normalization, while leaving deeper exact-form and DP choices separate.

The binding is the original untwisted E3 curve and the exact omega displayed above, lambda=4t(1-t), the Gauss–Manin derivative in the lambda direction, and the same transported homology cycle whose small-circle limit is 2 pi i. No additional lambda-dependent unit scaling of omega or quartic twist is inserted. The value is a coefficient in this fixed ordinary basis; no invariance under an unrecorded parameter-dependent scaling is claimed.

I also rechecked the already located p.25 setup: it embeds the two CM eigenclasses in ordinary de Rham cohomology, assumes integral local expansions, and normalizes their leading coefficients to one. Together with p.27's assumed nu=omega+c partial_lambda omega, this does not specify a unique global pole divisor or eliminate all exact-form choices of a meromorphic representative. The rational fixed-x differential computed in the certificate is a usable representative of the connection class; equality with a uniquely specified global or DP companion is a separate unproved identification. Additional pole/exact-form/representative normalization would have to be supplied and checked if that stronger conclusion were needed. No such additional selection rule was found in the cited p.25/p.27 passages.

## Limits, validation and disposition

The old distinction between the raw local H coefficient and truncated hypergeometric coefficient survives. Neither a constant complex period gauge nor c_CM=6 forces C_p=0. The report preserves the previous first-digit correction and does not claim that (6 alphaHat J-1)/p is integral in the intended model. It does not change accepted UR, identify the twisted/raw product through the next digit, or give actual kappa.

The author checker actually ran, reports the exact polynomial residual and all three coordinate residuals zero, seven recurrence indexing checks and zero prime tests. I read its source and output. The all-order analytic recurrence, contour argument and scalar deduction are mathematical arguments rather than consequences of those seven checks. My independent certificate calculation is also exact and uses no prime scan; it does not test the CM theorem or construct the actual Frobenius lift.

Disposition: NO_BLOCKING_ERROR_FOUND for the precise E3 period gauge and source-bound ordinary scalar identification. No whole-Task acceptance, RR/DR, parent closure or actual-DP comparison identification is made. Method harvest: standard Gauss–Manin/Picard–Fuchs exact certificate, residue initial condition, analytic continuation and primary-source normalization; no new general-purpose tool family is proposed.

The remaining actual-data obligation is a compatible DP/crystalline comparison and representative normalization connecting this ordinary class to the required local coefficient product, with its same-class bridge, Frobenius action and kappa. No executable additional source defining that comparison was identified at this checkpoint. That is a mathematical model/normalization gap, not a GitHub, quota or product-permission blocker. Owner retains portfolio direction and can select a distinct executable route; the present conclusion must not be extended by forcing the target product or by renaming scalars.

Native P000 space remains six-dimensional discrete Cell space with no native plane. This static elliptic algebra is explicitly external and proves no full-X6 propagation law. LIFT/JT2 and the arithmetic parent remain OPEN; user_requested_stop=false.

## Actual Source persistence and complete readback

The author published the frozen ordinary-class unit through d25-e3-release-checkpoint-20261008-r2 (bridge #3326), Source b0b81edef4dff91d820b4f021faba63b9623d0a0. Prefix: research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-bb6f343045854a798ca781ee73de2e39/10feb8dcbcb6a881b15f/.

I independently fetched the full report, checker, output, Guillera provenance and checkpoint, plus the Task latest pointer at that exact Source. All six SHA256 and Git blob identifiers matched. The four author artifacts matched the reviewed local bytes exactly. The latest pointer names that exact checkpoint. Local evidence: E3_FINAL_READBACK_0.json through E3_FINAL_READBACK_5.json and E3_FINAL_EXACT_VERIFICATION.json.

- D25_E3_PERIOD_GAUGE_CM_SCALAR.md: 11741 bytes; SHA256 8b33c0d99e87f4e97c7091c269668d07d035e5cc830ebd245df4cc7d1f886e27; Git blob 921386c3d77d76682a0f419666747880a8f7b879.
- check_e3_period_gauge.py: 1728 bytes; SHA256 7a938dd06f5e626df5a8ab38a50d1d4b5839cd830e30c563fa493ace255a101b; Git blob f3c61eea8f4a141a432c843fb8ddc5a1881725be.
- e3_period_gauge_checks.json: 653 bytes; SHA256 4dfd9a6c12132b2b6d55322a3232a3bda80e06102d15538827ecfabe56fafd32; Git blob e23f1c3d63f042b35f330947194dd11adb4725b3.
- source_guillera.provenance.json: 282 bytes; SHA256 e17ef3f119825b079a666665b5bd3cea02e1d88145bd21991b91bbf6e39c16f9; Git blob 34af0993c9d64d157b9d85f527f5a9bb2f575736.
- _checkpoint.json: 17835 bytes; SHA256 9496ae55b569216e3bf42a7f89b5e5adfd2221523fc2b7b57a6d96dc18b66854; Git blob 3247a64832c16bbe20197953e05b9b9be773f2c3.
- latest_checkpoint.json: 727 bytes; SHA256 0c2702755b594b7ffb93c560ebf77a5a9d30ecd123c714f33dcf85bedd2bb5ac; Git blob 2af6102a0266540e33f316125b7c5a80b7c7a19b.

I compared the final checkpoint with the preceding Katz checkpoint: every prior completed-unit and no-repeat entry is preserved verbatim as a prefix. New entries add this ordinary c_CM result and earlier restoration pins. The final unfinished unit and next action explicitly separate ordinary c_CM solved, target-product rescaled c_p not identified, and actual DP comparison/representative missing. They retain old C_p and first-digit mismatch, require fresh future authority and new concrete data, and record user_stop=false with LIFT/JT2 and parent OPEN. Source durability is established here; native claim/run/session terminal status is verified separately in the line handoff and must not be inferred from a content hash alone.

The author subsequently supplied HANDOFF_NORMALIZATION_BOUNDARY.md as an index of the frozen result, SHA256 8e08b805fdfacfc894ee1907abbf14c30a87274325998462d1fd722eeeaa619b. It did not alter the in-flight author checkpoint or proof. At the author's request it accompanies this Driver audit publication, preserving author EM-ENTERPRISE-B078A6 attribution. My independent certificate-check output, SHA256 ffb83bbcb5322aa290dda399d78d198cd8611e8944b5bc4a5afdc7e4ca06f2c6, also accompanies the audit. Neither auxiliary file is a new mathematical theorem or a claim of Task completion.

Driver-ID: EM-DVR-E33955 / CONTROL_PLANE
