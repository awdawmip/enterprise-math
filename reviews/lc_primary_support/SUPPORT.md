# CM24 LC primary-source review support

Reviewer: EM-LCPRIMARYSUPPORT-20261015 / TASK_RESEARCH. Activity: RA-76FF3730A695FEB52604FCA5.

This is a read-only mathematical support handoff to the decisive reviewer, not an additional Native review vote, formal Result, Driver review, or independent-blindness claim. I did not contact the import author or modify the fixed author package. My new identity supplies execution provenance only. The bounded assignment is complete.

## Finding and exact scope

No mathematical must-fix found in the frozen primary-source applicability audit. Its conclusion `NOT_APPLICABLE_DIRECT_HYODO_KATO_5_1` is justified for the stated two-parameter formal family. This is an obstruction to that direct theorem application, not a counterexample to LC and not a proof that a composite relative import cannot discharge LC.

The fixed report, current-base geometry paper, previous geometry review, and full primary PDF were each byte-hashed and matched their declared pins; details are embedded below. I independently ran `pdftotext -layout` on the pinned complete PDF and visually read PDF page 43 (printed p. 262), and PDF pages 20–22 (printed pp. 239–241). The extraction SHA-256 is 07202df784b3bf5a35b41e00d3e545a560450d2e041250c98a834fe52da6551a, identical to the author's derivative. This establishes that the supplied complete PDF was actually readable. No additional literature, numerical experiment, prime scan, or scientific computation was used.

## Theorem 5.1: what the original says

Hyodo–Kato, Astérisque 223 (1994), Exposé V, pp. 221–268. Official complete source: https://www.numdam.org/item/AST_1994__223__221_0.pdf . It has 49 PDF pages including its cover, 1,867,725 bytes, SHA-256 220873e91f89094d14f1a82631c6887a40ec362139990928236ca0525b1050cf. Printed page n corresponds to PDF page n-219 in this file.

Printed p. 262 / PDF p. 43, Theorem 5.1 opens:

> “Let A be a complete discrete valuation ring with field of fractions K and with perfect residue field k such that char(K) = 0 and char(k) = p > 0”.

The remaining inputs there are the canonical log structure N on Spec(A), a scheme X with fine log structure M and a log-smooth map f:(X,M)→(Spec(A),N), X proper over A, and the induced log special fibre (Y,M-bar)→(Spec(k),L) of Cartier type. Here Y=X⊗_A k and M-bar,L are the inverse-image log structures. The theorem fixes m∈Z and defines D as rationalized inverse-limit log-crystalline cohomology of this special log fibre over W_n(k) with its indicated log structure.

Printed p. 263 / PDF p. 44 concludes that each prime element π of A determines a canonical K-isomorphism K⊗_{K_0}D→H^m_dR(X_K/K), where K_0=Frac(W(k)); it also records dependence on changing the prime element via monodromy. Thus this is a special-fibre/generic-fibre comparison for that mixed-characteristic trait. It is not stated as a theorem directly constructing the entire relative logarithmic F-module over an arbitrary two-dimensional formal base.

The canonical log structure is important: §2.13.1, printed p. 232 / PDF p. 13, defines it from the closed point of the DVR as a reduced normal-crossings divisor. The base in the target LC statement instead has the horizontal divisor t=0 on Z_p[[t]]. One must not silently replace the former by an arbitrary chosen divisor on a higher-dimensional ring.

## Match against the pinned current base

The fixed geometry paper, SHA-256 6f3e40db8efe1dbefa7da9542e4ffe569eb5c9592435cfb7529e8637e53c5033, explicitly fixes:

- Lines 35–46: E_s with s=4r^3-3r, t=r-1, θ(t)=t^p; descent to Z_p with identity coefficient Frobenius, followed by scalar extension.
- Lines 95–107: the semistable smoothing and divisorial log structures t=0 on the base and its semistable divisor on the curve.
- Lines 111–130: LC for a proper semistable genus-one curve over Spf Z_p[[t]], relative log-crystalline/log-de Rham realization after passage to Q_p[[t]], horizontal regular θ-Frobenius with cup multiplier p, and the normalization/graph-compatible specialisation.

The previous geometry review, SHA-256 36899b4f55d21fb70ff3ce68874fcda8d7d6d98c7a53b93b257babc9f98a93f0, states this same base and completion requirement in A, same geometric generic comparison in B, same θ/coefficient/cup conditions in C, and graph/residue-kernel compatibility in D. The import audit accurately preserves that interface.

For R=Z_p[[t]], the maximal ideal m=(p,t) has dim_{F_p}(m/m²)=2; a DVR would have principal maximal ideal and dimension one here. Thus R is not the required DVR. The source's geometric semistability does not repair this independent base-ring failure. Moreover the theorem is stated for schemes over Spec(A); passage to a formal family, completion, and the relative connection cannot be assumed merely from its title.

Both one-dimensional replacements in the report are also correctly excluded from the displayed theorem:

1. Q_p[[t]] is a complete t-adic DVR, but its residue field is Q_p of characteristic zero, failing char(k)=p>0.
2. R_(p) is a mixed-characteristic DVR. Its residue field is Frac(F_p[[t]])=F_p((t)), and p-adic completion does not change this residue field. It is imperfect: t cannot be a p-th power because its t-adic valuation is 1, while v_t(z^p)=p v_t(z). Its canonical DVR log divisor is additionally the p-adic closed point, not the original t=0 boundary, since t is invertible after this localization.

Perfecting that residue field or specializing t changes the base/object and leaves new descent or relative-comparison obligations. It does not by itself establish LC over the saved formal family. Also R[1/p] and Q_p[[t]] are distinct rings; the earlier A-interface explicitly retains the completion passage rather than assuming their equality.

## Relative propositions: exact interfaces and limits

Proposition 2.20, printed p. 238 / PDF p. 19, assumes the situation of Definition 2.19: the log-PD base conventions of §2.14 (including a structure sheaf killed by a nonzero integer), X locally of finite type over the base, a chosen embedding system, and a crystal F. The embedding system (§2.18, pp. 236–237) has an étale hypercover X^•→X with induced log structures, smooth log ambient objects Z^i over the base, and closed immersions X^i→Z^i. The crystalline complex uses their log-PD envelopes and ambient logarithmic differentials. The conclusion is the canonical comparison Ru^log_{X/S,*}F≅Rθ_*C_{X/S,F}. The report accurately calls this an ingredient for A, without claiming local freeness, formal completion, or the full LC realization.

Proposition 2.23, printed pp. 239–240 / PDF pp. 20–21, uses the displayed two-square diagram of fine log schemes. Precisely, f:(X,M)→(S-bar,L-bar) is smooth integral; the upper square is cartesian; the lower vertical arrows S-bar→S and S-bar'→S' are exact closed immersions cut out by PD-subideals of I and I'; the reduced-base map S-bar'→S-bar is radicial; and F is a flat crystal. The conclusion is the displayed base-change isomorphism for Ru^log after the indicated scalar extension and restriction to X'. “Radicial base map” in the report is accurate when understood as this S-bar'→S-bar map, rather than an assertion about an arbitrary map of PD thickenings. Its application to the specific formal tower has not been supplied and is not claimed.

Proposition 2.24, printed pp. 240–241 / PDF pp. 21–22, assumes f is smooth of Cartier type between fine log schemes over F_p. In §2.12 (pp. 231–232), Cartier type includes integrality and exactness of the relative-Frobenius map in its defining cartesian diagram. There is an exact closed-immersion tower (S,L)→(T_1,L_1)→(T_2,L_2)→… with PD structures on the ideals of S, PD-compatible transition maps, T_n flat over Z/p^nZ and T_n≅T_{n+1}⊗Z/p^nZ, and bounded log-differential rank. If r is the maximum such rank, the relative-Frobenius map φ of derived crystalline sheaf projective systems has ψ with φψ=ψφ=p^r. This is the precise p-isogeny statement. The printed text introduces “(i)–(iv)” but visibly lists only (i)–(iii) before the conclusion; no missing fourth condition should be invented from OCR. The report does not reproduce that typographical issue and correctly lists the actual mathematical hypotheses.

In particular these propositions do not themselves state the required normalization/dual-graph identification with the residue-kernel line and actual split-branch Frobenius. They are relative ingredients located in the same source, not an already instantiated proof of LC A–D. No must-fix arises from the audit's restrained description.

## Evidence pins and method boundary

All SHA-256 values below were recomputed from the local exact bytes before this support handoff:

| Input | Bytes | SHA-256 |
|---|---:|---|
| research_notes/owner_goal_20261015/cm24_lc_import/PRIMARY_IMPORT_AUDIT.md | 8233 | a1ce7e44e447a355bc533e1b70c9f92e5b6c4b2ee0d0e31a01d148e6f9a3be78 |
| research_notes/owner_goal_20261015/cm24_geometry/CM24_SPLIT_NODE_LOG_COMPARISON_AND_POSITIVE_SIGN.md | 14416 | 6f3e40db8efe1dbefa7da9542e4ffe569eb5c9592435cfb7529e8637e53c5033 |
| reviews/cm24_geometry_nonauthor/REVIEW.md | 10953 | 36899b4f55d21fb70ff3ce68874fcda8d7d6d98c7a53b93b257babc9f98a93f0 |
| research_notes/owner_goal_20261015/cm24_lc_import/sources/hyodo_kato_1994_retry.pdf | 1867725 | 220873e91f89094d14f1a82631c6887a40ec362139990928236ca0525b1050cf |

The existing external-import coverage resolution is reused solely for scope: native signed-circuit/carry/quotient/BRC lexical matches do not implement the external relative log-crystalline theorem interface. No new mechanism or capability-gap claim is made. The P000, Heartbeat X6, residual-fidelity, and joint-preservation contracts were loaded. This audit treats the cohomology family as an external typed module; t is the arithmetic boundary coordinate, not physical time or a native spatial dimension. No native quotient or erased branch information is introduced.

Retain LC OPEN, the preceding conditional geometry acceptance, all actual-c/extension/integral/dagger/global obligations, and the original mathematical parents. The decisive disposition belongs to the parent reviewer.

Researcher-ID: EM-LCPRIMARYSUPPORT-20261015 / TASK_RESEARCH
