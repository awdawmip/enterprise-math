# EC49BC — exact η=11/25 causal optimum of the positive auxiliary BRC observer

**2026-10-30; AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_SYMPY_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.** This is a **new single parameter point** beyond EC49BB's proven interval [21/50,43/100]. The result is conditional on the EC49AV author-side sparse-to-edge representative lemma pending independent review. No native signed/phase BRC, X6, native three-dimensional slice, Heartbeat World or external physics assertion.

For the exact 18+18 positive auxiliary P/Q causal observer of EC49BB, hidden w∈{0,1,2} uniform, costs C1=43/48, C2=13/16, coefficient k=177/172, and *observation-only* purchase and terminal acceptance, the global real-policy optimum at η=11/25 is

[
\boxed{H_{\max}=\frac{405889}{3233600}-\frac{3\sqrt{21}}{3760}\approx0.12186601766050653.}
]

An attaining policy uses the previous exceptional edge row family
`x[0,:]=((11−8t)/16,0,t/4,0,(5+4t)/16)`,
`x[1,:]=(0,1,0,0,0)`, `x[2,:]=(1,0,0,0,0)`, at
[
t_*=\frac{565}{376}-\frac{15\sqrt{21}}{94},\qquad
p(0,1)=\frac{22}{47}+\frac{15\sqrt{21}}{188}.
]
Buy every other positive-mass paid observable fiber fully; accept only the purchased events `(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)`. Direct exact algebra verifies t*∈(3/4,4/5), p∈(0,1), exact C1 and C2, β=13/48, α=Hmax+177β/172, and no dependence on hidden w during purchasing or acceptance.

**Full upper-bound certificate.** Reuse the EC49AV sparse-edge lemma; the executed `Fraction` checker enumerates 168 first-stage vertices, 924 edges, 720 purchase-infeasible edges, **196 ordinary edges and 8 signature-isomorphic exceptions**. For each ordinary edge it finds a nonnegative rational λ shared by the two clipped edge endpoints, giving the strict uniform rational bound
[
H\le \frac{60933}{500000}=0.121866.
]
This bound is **strictly below** the attainable radical H*: putting `r=7389439/1612500`, exact computation gives `r²−21=527484721/2600156250000>0`; elementary rearrangement reduces H*>60933/500000 to √21<r. There is no float-based comparison.

The remaining 8 edges have the same algebraic signatures, score signs and fiber-density ordering as the EC49BB exceptional-edge proof, now checked at η=11/25 for all real t∈[0,1]. Their exact purchase-optimized objective is
[
H_{\rm best}(t,\eta)=h(\eta)-\frac{344(1-4\eta^2)t^2+(2436\eta^2+1568\eta-1201)t+(2060\eta^2-5096\eta+1769)}{2064(27-10\eta-(8+16\eta)t)}.
]
The only partially purchased fiber is observable (c,u)=(0,1), with withheld mass (1−t)/12. Differentiating this quotient gives numerator `N(t)=−aft²+2adt+bd+fc`; its derivative `N'(t)=2a(d−ft)>0`, and exact signs `N(3/4)<0<N(4/5)` ensure a unique interior optimum at the specified radical t*. At η=11/25 all 24 atomic score signs are fixed along the edge and the five positive-fiber density cross-product factors are nonnegative; see EC49BB proof and the actual checker. Hence the best of the 8 exceptional edges equals H*, exceeding the cap on the other 196. The inherited full-policy sparse representative lemma completes the stated conditional global theorem.

**Reproduction.** Actual Python 3 `fractions.Fraction` and SymPy 1.14.0 program `VERIFY_EC49BC.py` was run twice with byte-identical `EXACT_REPORT_EC49BC.json`, and enumerates all 196 rational dual multipliers and exact algebraic checks. Published losslessly as `VERIFY_EC49BC.py.gz.b64` and `EXACT_REPORT_EC49BC.json.gz.b64`. Decode both by base64 and gzip, and decode sibling `VERIFY_EC49BB.py.gz.b64` into the same directory; run `python VERIFY_EC49BC.py > EXACT_REPORT_EC49BC.json`. Exact raw source SHA256 `f05eba28f38dcb76863a78ee323370ba0d04445cdf431c25b7b9d02ba119bf70`, exact JSON SHA256 `c7aa71647e3146e66df6563daa9d98280ee304e1fea091663ad385a96aac478d`. The computation is finite exact checking plus closed-form rational/algebraic inequalities, not finite grid extrapolation.

**Next EC49BD:** obtain a nonzero real η right neighborhood from 11/25 through per-edge dual and density certificates, or find a lawful changing-strategy counterexample; independently audit EC49AV. Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 `main@ae95db422329f57935973df82b6b5a08e2c9d59a`, Enterprise Math `main@4f75ce4f2301660419479a6dfdca6748bb41c10a`. P000 and ACTIVE worldview untouched. Native service reported `research_authority_granted=false`, `CONTROL_QUOTA`, and `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`; no Source-native researcher session, CLAIM, Result or independent Driver review.
