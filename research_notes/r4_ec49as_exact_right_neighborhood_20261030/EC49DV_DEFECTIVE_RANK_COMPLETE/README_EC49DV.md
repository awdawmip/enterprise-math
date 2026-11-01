# EC49DV — Exact defective ranks and sharp 12-step repair of the joint-neutral BRC observer

**2026-11-02 | AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**

## Scope, provenance and scientific pins

Continuation of EC49DU at immutable research commit 6040d0bba5a32096aff1bcdbb963a26051957043 (Draft PR #1730). Preserve frozen scientific inputs GLOBAL_KNOWLEDGE_V1 773d538180bfb49e24cffeb35c3ee75eb0628e2e and Enterprise Math fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Separately, the verified 2026-11-02 current normative snapshots are GLOBAL_KNOWLEDGE_V1 main@462e56c5ad43a2c69ed13fa4d4f60542cf29fc21 and Enterprise Math main@4c87adb75df284f7b13c36a3250d2b2b87fb5f0c. Protected P000 and ACTIVE worldview have not changed.

Old histories are ordered **native signed X6 primitive-step words** with full displacement D=−2E₁, preserving all six spatial axes and path order. At length n=10 there are four positive primitives, with multiplicities p∈N⁶, |p|=4, and six negatives with multiplicities p+2E₁. Flags A/B record adjacent (+E₁,+E₂)/(+E₂,+E₁), including the old/future seam; L is 1 for old final +E₁, 2 for +E₂, 0 otherwise. BRC uses X_p=∏x_i^{p_i}, Y_p=∏y_i^{p_i}, negative steps unit-weight, and an unweighted count channel; x_i,y_i are arbitrary strictly positive real numbers. We study EC49DU's diagnostic future alphabet a,b,c,d,e,f,g and the eight old features z=(z00,z01,z10,z11,pA,pB,q,r).

The n=10 historical instrument-feature matrix H₈ has rows (X_p z | Y_p z | z), with 24 columns. Define C₁₁ as the three positive-count patterns (p₁,p₂)=(1,3),(2,2),(3,1) with zero other positives, and the eight patterns (1,2,+E_j),(2,1,+E_j) with j∈{3,4,5,6}. G_C is the 11×3 matrix with rows v_p=(X_p,Y_p,1), p∈C₁₁.

## Theorem A — all-parameter exact rank classification at n=10

For **every** x,y∈(0,∞)⁶, the rank of H₈ is one of exactly four values: **8, 16, 23, 24**.

1. rank(G_C)=3 implies rank(H₈)=24 (the EC49DU full-rank criterion).
2. rank(G_C)=1 is equivalent to x₁=⋯=x₆ and y₁=⋯=y₆; then rank(H₈)=8.
3. With rank(G_C)=2, if one of the global conditions holds — all x_i equal, all y_i equal, or y_i=λx_i for a common λ>0 — then rank(H₈)=16.
4. Every remaining rank(G_C)=2 instance has x₁=x₂=u, y₁=y₂=U and all five weight points (u,U),(x₃,y₃),…,(x₆,y₆) on one oblique affine line that is neither horizontal, vertical nor through the origin. Then rank(H₈)=23.

In particular the tempting formula rank(H₈)=8 rank(G_C) is **false**, even for all-positive integer weights. This theorem classifies the historical observer exactly. Under the author-side EC49DU future-operator factorization, the same ranks hold for each finite exact returning horizon h≥2 and cumulative horizon 1..h for that specific a–g language. The future transfer is a reused author-side theorem awaiting independent Driver review; no physical-model or arbitrary-new-operation transfer is asserted.

### Proof of exact historical ranks

Let W_p⊂R⁸ be the linear span of eight-feature rows produced by genuine ordered native signed histories having positive-count vector p, and v_p=(X_p,Y_p,1). The complete historical row space is exactly Σ_p (span(v_p)⊗W_p). The exact native-path witness (encoded execution report) verifies W_p=R⁸ for each of the eleven p∈C₁₁. For p outside C₁₁, the two flags cannot both occur: their coexistence requires the positive subsequence 121 or 212, exhausting exactly the C₁₁ possibilities when only four positives are available. Thus W_p lies in the seven-dimensional coordinate hyperplane K={z:z11=0} for every p∉C₁₁.

Write V=span{v_p:p∈C₁₁}, r=dim V. The C₁₁ row space is V⊗R⁸, with dimension 8r. At r=2, the quotient by that core lies in (R³/V)⊗K, which has dimension 7. Therefore 16≤rank(H₈)≤23. This upper bound uses the declared history population, not a floating-point calculation.

If r=1, two distinct pure-core count patterns force x₁=x₂=u, y₁=y₂=U (strict positivity makes the relevant geometric powers injective). Each single-external C₁₁ count pattern then forces x_j=u,y_j=U for all j≥3. Every v_p is identical, and eleven full W_p give rank eight.

For r=2 put u=x₁, v=x₂, U=y₁, V=y₂. The pure-core three-row determinant factors, up to a nonzero positive monomial, as (u/v−1)(U/V−1)(u/v−U/V). If u≠v and U=V, the eight external C₁₁ rows on the same line force every y_j=U. If u=v and U≠V, they force every x_j=u. If u≠v,U≠V and uV=vU, they force y_j=(U/u)x_j for all j≥3. In each case all v_p for |p|=4 lie in an instrument two-plane: Y constant, X constant, or Y=λ⁴X respectively. Thus rank H₈=16, from the full core.

The remaining r=2 case necessarily has u=v and U=V. The external C₁₁ rows are (u³x_j,U³y_j,1); their collinearity with (u⁴,U⁴,1) means all points (u,U),(x_j,y_j) lie on one affine line. Excluding horizontal, vertical and origin-passing lines yields an index j≥3 with t=x_j≠u, s=y_j≠U and us≠Ut. Choose p₀=(1,3), p₁=(1,2,+E_j), p₂=(1,1,+2E_j), with zeros in the other axes. Their instrument/count vectors are

- v₀=(u⁴,U⁴,1);
- v₁=(u³t,U³s,1);
- v₂=(u²t²,U²s²,1).

Let α=t/u and β=s/U. Direct factorization gives

**det[v₀;v₁;v₂] = −u⁴U⁴(α−1)(α−β)(β−1) ≠ 0.**

Both p₀ and p₁ belong to C₁₁, so they supply independent full eight-dimensional features, spanning 16 dimensions. At p₂ genuine signed histories span exactly K: the report contains seven independent native path feature rows, while z11=0 for every such history. Because v₂ lies outside span(v₀,v₁), p₂ contributes seven new quotient dimensions, giving rank H₈≥23 and therefore **rank H₈=23**. All cases are exhausted.

## Theorem B — first full-24 saturation at n=12 on the oblique defective stratum

For **every** parameter in case A(4), the earliest n with rank H₈=24 is **n=12**. At n=10 rank is 23, and the EC49DU positive-step counting argument excludes full 24 for n≤8. All native histories reaching D=−2E₁ have even n.

At n=12 there are five positive steps. For the same external axis j with t≠u,s≠U,us≠Ut, choose count patterns P₀=(1,4), P₁=(1,3,+E_j), P₂=(1,2,+2E_j). The independently regenerated native-path witnesses contain eight independent old z rows for *each* of these patterns. Their 3×3 instrument/count matrix has

**det G₁₂=−u⁵U⁵(α−1)(α−β)(β−1)≠0**.

The resulting 24×24 Kronecker construction has nonzero determinant, proving rank 24 at length 12. This is sharp. For the globally constant/proportional instrument cases in A(3), all v_p lie in a two-plane at each fixed history length (since |p| is fixed), so full rank 24 remains impossible at every even length.

## Concrete exact counterexample, finite coverage and reproduction

Take strictly positive weights

x=(2,2,1,2,3,4),   y=(3,3,1,3,5,7).

All six weight points lie on y=2x−1. Exact finite computation gives rank G_C=2 but **rank H₈(n=10)=23**, so rank H₈≠8 rank G_C. With j=3, v₀=(16,81,1), v₁=(8,27,1), v₂=(4,9,1); the two-row X/Y minor is −216 and det[v₀;v₁;v₂]=−72. The attached executed verifier constructs **23 real signed native six-axis words** in these three count patterns, drops the z11 column in the count block (zero-based column 19), and computes exactly:

**det M₂₃ = 2166612408926208 = 216·72⁷ ≠ 0**.

At n=12, the three patterns give det G₁₂=−432 and 24 actual native paths yield **det M₂₄ = −1213025622610333925376 = −432⁸ ≠0**.

The Python standard-library verifier exactly enumerated all 126 positive-count vectors at n=10, with 357 reachable (count,A,B,L) states. W_p rank histogram: 35 patterns of rank 1, 70 of rank 2, 10 of rank 7, and 11 of rank 8. Six reference integer-weight families yielded (rank G_C, rank H₈) of (1,8), (2,16), (2,16), (2,16), (2,23), (3,24), all using exact Fraction linear algebra. The 23×23 and 24×24 determinants use fraction-free integer Bareiss elimination. The finite computation certifies the enumerated witnesses and reference ranks; universal parameter quantifiers come from the analytic proof above.

Published source is losslessly stored as VERIFY_EC49DV.py.gz.b64 and its executed JSON as EC49DV_EXECUTED.json.gz.b64. Reproduce by base64-decoding each file and gzip-decompressing, then run the resulting Python program. Decoded source SHA256: 0c24a4d786508c2697b23e53a16b64bfd5c1b62d45f5e30a43a8a67a2b8b661a. Decoded executed report SHA256: 63256621aef1e34918d2416b308e0322379520f4fc7a1b27fe5dbd9c3f5cc829. The full signed witness path lists for 23 and 24 are included in the report.

## Permission, review and next question

Authenticated GitHub identity: awdawmip. Native Enterprise Math service 0.6.11 returned research_authority_granted=false; active-owner read returned CONTROL_QUOTA; this execution's own RESEARCHER session_start returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. This research manuscript therefore remains an author-side Draft. No native Research Activity, CLAIM, Result, independent Driver review or Foundation admission has been obtained.

**Next EC49DW:** Determine the sharp first saturation length for the original a–e, f-only and f+g future languages across these parameter strata, and test whether a further native zero-displacement future operation creates a ninth independent historical residual. Any proposed new observer must retain the complete six-axis return, A/B seam and specific future-operation grammar.
