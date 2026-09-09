# Independent source-exposed review of the v3 exact-map candidate

Decision: **PASS within the stated paper and code-review scope.** I found no mathematical or implementation defect that blocks the pinned full-fiber and placement argument. This is an Owner-delegated peer review, not a blind derivation, independent computational replay, formal Driver disposition, Result, or permission to close the parent problem.

The reviewed author proof has SHA256 `7c8c480af589fcd875488a8031db4e6adb1cc1a144adee2950a2e16b74866f12`; checker `58c57974e3bf74e17a9a4ff4063d3d6ab676b378521b1dba6dfba26ec38f05b6`; tests `41a805d1a57e9422b3a8bfeac8257b8c61231524157514fcf4389a761de712e6`; final certificate `bbb33d3e80274af0eb09aeef6bb6d5009745048849c6e8b93026a6410bac0e5e`; final author receipt `b02c0cc64126fab7bac3c355d24db2fc816a068e7408ca9c7c28a07744570c26`. Their repository directory is `research_artifacts/RB_CM24_SOURCE_EXPOSED_EXACT_MAP_20260909/`. The exact 40-file publication manifest is pinned by SHA256 `843bc000fd927108c72d792a86f5a77ede2e6afe16e2b3dda4f0ec0901d9cdc6`; this review does not substitute an anticipated commit for those actual bytes.

## Read and execution scope

I read the complete 23,768-byte author proof, all 822 lines of the final checker, all 13 focused tests, the final runner, the formula/source freeze, both v3 bindings, and the actual final logs. I independently derived the implications below before reading the Owner's comparison note. The prior field, full ODE, nonzero and common-base-divisor reviews are reused at their pinned scopes; no earlier arithmetic run or old classification enumeration was repeated.

For historical compatibility I read the old RR paper's field, base representatives, constant factors, divisor and differential conventions in sections 1–4, and the empty-fiber result's exact exclusion boundary. I compared the full selected old row, not the entire old enumeration. The final certificate was parsed completely for serialization integrity and selected evidence fields. I did **not** manually compare every large integer coefficient or recompute its polynomial identities.

The accompanying `collect_read_evidence.py` performs only byte hashes, JSON/AST reads, log binding and serialization checks. It imports no mathematics module and runs no checker or test. Its actual invocation passed: all 40 manifest files match content/SHA256/Git blob/size; all seven original and five placement-source pins match; final primary and archived certificates are identical; all three author command logs match their receipt; 132 nonempty polynomial lists, totaling 1,772 serialized terms including repeated evidence, have sorted, unique, strict-integer normal-form rows. All six recorded coprimality chains have nonzero constant termini and retained multipliers. The metadata receipt is `receipt.json`, SHA256 `e30709d55be0c8e88508d59439f636f15cef42fffe2ca336124c5087c7ea60d5`.

## 1. Complete fibers and exceptional points

The asserted norm factorizations, with the recorded degrees and nonzero leading coefficients, account for every finite root. For each residual Q2, Q3 or Ql, squarefreeness makes its R-roots simple. Avoidance of R=0, +/-sqrt(3), -2 and -3sqrt(3) removes the carrier ramification values, source-cover branch values and B0. Coprimality with the corresponding t coefficient prevents simultaneous vanishing on both ordinary t-sheets. Thus a double root in a norm belongs to exactly one point on C, with function order two; it is not two simple points on opposite sheets.

At B0 the simple R+3sqrt(3) norm factor and actual vanishing imply order one for D0, N-D0 and N-lambda D0. Combined with the established order one of N, this gives a finite canceled X-value outside 0, 1 and lambda. The separately recorded nonzero twice-delta D0 value justifies the derivative-ratio description. This legitimately strengthens v2's common-minimum-order statement; that earlier statement by itself did not determine the individual D0 order.

The T0/Tplus orders follow from the nonzero linear t coefficients, and the O orders from the reduced weights six and seven. Consequently the displayed complete divisors of X, X-1 and X-lambda have the claimed degree-six zero and pole fibers. Their residual selected divisors cannot overlap on C: such overlap would force N=D0=0, whose only finite possibility is the excluded B0. Coincident R-coordinates on opposite sheets are not an overlap of points.

The precise source branch assignment is therefore `(0,infinity,infinity,0,0,0)` in the fixed order `(O,T0,Tplus,Tminus,Pplus,Pminus)`. Empty blocks for 1 and lambda mean no **source-cover branch points** there, not empty degree-six fibers.

The section 4 differential argument includes all exceptional loci. At t=0, R=-2 and O the normalized local orders cancel every possible pole of phi. The checked exclusions k!=0 and k^2!=+/-2 make t=-k an ordinary three-point divisor avoiding the six cover branch points; it has two lifts per point and exactly six simple zeros. The unsquared equality is first an equality of rational differentials, with the original Y sign retained, and extends globally. The proper-target extension argument does not replace the independent basepoint and degree arguments.

## 2. Half-point and the three retained scalar/function pairs

The explicit Q lies in L. Its tangent norm, tQ!=0 and xQ+sqrt(3)!=0 give divisor `2[Q]+[Tminus]-3[O]`; equivalently 2Q=Tminus. Hence g=t/ell has divisor `[T0]+[Tplus]-2[Q]`. This fixes the half-point convention rather than hiding a change of geometric twist labels.

For h=n/d with Norm(h)=H^2, the identity `(h+H)^2=h(Tr(h)+2H)` is valid in the proved quadratic function field. Write the trace expression as U/V. The checked identities

`M U = removed Q3 B`, `256 V = c removed Q3^3`, `K B = J S^2`

give `r=256 J S^2/(M c K Q3^2)` and

`h=(M c K/256) (Q3(h+H)/S)^2/J`.

The actual nonzero factors exclude the degenerate r=0 case. For h0, J=R(R+s)=t^2/(R-s) and c=-lambda^5, producing exactly the stated alpha0 and u0. For h1, J=R and c=1, producing alpha1 and u1. Thus the class labels follow from full square reconstructions, not only branch parity.

The full ODE and G0 G1 Gl=F imply `h0 h1 hl=Hprod^2/C4`. With `(R-s)R(R+s)=t^2`, the displayed alphal and ul reconstruct the third class. The program separately clears and checks all three x' identities and nonzero numerator/denominator/scalar factors. Constants remain in L; none is silently declared a square or removed by extending constants. The resulting triple is `(Tplus,T0,Tminus)` relative to the specified Q. In particular R-s is geometrically nonsquare: a putative square would make `[Tplus]-[O]` principal on this elliptic curve.

## 3. Two V4 transformations, descent, RR data and sign

Both transformations preserve fixed lambda and the twist C=C4/4:

`x'=(X-lambda)/(X-1)`, `Y'=(lambda-1)Y/(X-1)^2`;

`z=lambda/x'`, `Yz=-lambda Y'/x'^2`.

Their derivative ratios are one, so neither changes fixed k or the differential direction. The composed formula is `z=lambda(X-1)/(X-lambda)`, with `Yz=lambda(1-lambda)Y/(X-lambda)^2` and `Wz=lambda(1-lambda)W`.

The original representative and the lexicographically chosen empty-infinity representative are distinct. The latter is `(1,2,2,1,1,1)`, not the intermediate x' assignment. The code's frozen row 42 is byte/object-consistent with the old certificate and has dimensions `(3,1,2)` and transport `(1,0,3,2)`.

The three canonical scalar/function formulas follow exactly from `z=lambda/x'`, `z-1=-(x'-lambda)/x'` and `z-lambda=-lambda(x'-1)/x'`, using

`(R+s)/(R-s)=R(t/(R(R-s)))^2`,

`R/(R-s)=(R+s)(t/((R-s)(R+s)))^2`.

These give the stated a0,a1,al and v0,v1,vl without an additional constant square root. The map and this displayed representation descend to **L=Q(alpha,beta,i)**. No smaller or minimal field is established; removing i from the original erroneous real-field declaration is not justified.

The actual pole half-divisor is El, defined by the full Ql/Al equations, so it is an L-defined divisor even if individual cubic points are not L-rational. Its Picard parameter is S=sum(El), and `div(Al)=[B0]+2El-7[O]` gives `2S=-B0`. Because B0 is not O, S is not O. The relation alone would not select a unique half of -B0; the pinned divisor El supplies that selection. It has not been replaced with 3O.

For z the even zero parts are E1, [Z], Einf and the base divisors are `(0,3[O]-[Q],[Q])`. Direct divisor comparison gives `div(v_a)=E_a-El+B'_a`, with `B'_a=B_a+[O]-[T_a]`. The corresponding line bundles have positive degrees `(3,1,2)`, hence those exact genus-one RR dimensions. The two section equations follow from the displayed function identities with the actual pole data; this does not posit an evaluated RR basis.

Finally, the displayed product satisfies `t v0 v1 vl=alpha0^2 Hprod/x'^2`, whereas `2 delta(z)/(t+k)=-lambda Hprod/x'^2`. Thus `eta=-lambda/alpha0^2` has the stated **unsquared** sign and `eta^2=C4 a0 a1 al`. The remaining factor 1/2 in delta(z) agrees with the code's integer derivation D=2delta. This sign does not come from choosing a root of the squared ODE.

## 4. What the program and actual receipts establish

The final program directly checks the full original ODE; geometric identities and exact nonzero witnesses; three complete norm factorizations; six pseudo-remainder coprimality witnesses; actual Y sign/normalization counterchecks; the explicit tangent; norm and square reconstructions for all three **x'** classes; the composed z full ODE and Wz multiplier; and matching to the exact old classification row. Pseudo-quotient and pseudo-remainder routines retain their multipliers and verify reconstruction and degree decrease. They do not invert a scalar or discard integer content.

The canonical z three-pair transport, the local-divisor interpretation of polynomial facts, the Picard/RR conclusions and the explicit eta identity are **paper deductions** reviewed above. The code does not independently execute a separate check for each such conclusion. Its degree and branch/component labels combine checked polynomial premises with this proof; they are not software root counts or a generic geometric solver. This distinction should remain explicit in the return.

The verified author receipt records a fresh final certificate command (exit 0; 0.797 seconds measured by its outer runner), 13 focused tests (0.880 seconds reported by unittest; 2.906 seconds outer duration), and selected static checking of two files (exit 0). The tests include fixed-k sign, one-coefficient mutation, wrong C4, actual Y sign and missing factor two, repeated-root rejection, integer/symbol-carrier rejection and nonmonic pseudo-quotient content preservation. The common-multiplier test correctly demonstrates why the ODE alone is not a degree certificate. I read these tests and their bound logs; I did not execute them again.

The recorded final certificate has 533,112 bytes, 376 as its largest normalized support and 583 as its largest observed coefficient bit length. Its API counters are 789 add, 5,757 multiply, 341 section differences, 102 scale and 10 twice-delta calls. These are source/log-bound author observations, not a new independent performance measurement. They count calls at the shown wrappers into the frozen legacy integer API, not every internal integer operation. The current code contains no scalar division/root evaluation; the recorded BRC evaluation count is zero. This is not a transitive certification of unrelated legacy tools.

Each mathematical child applies the 4,096 MiB Windows Job process-memory cap; no measured peak is reported. The actual stored final runner supplies `subprocess.run(..., timeout=600)`. Child deadline checks at normalization boundaries are cooperative and do not alone interrupt a multiplication or JSON serialization. The outer runner and source archives are correctly distinguished from the earlier v1 inline runner. Existing final certificates are replayed in a fresh process at the canonical module path; archived `.py.frozen` is an archive, not a standalone alternative package.

## Acceptance boundary

The reviewed evidence supports the finite source-exposed exact-map certificate for this one formula: complete ODE/target/differential, cancellation and degree, all four fibers, actual V4 component with L-rational scalar data, and its non-O RR pole class. It places one map in a surviving 4+2 component; it does not solve or enumerate the other 1,980 parameter families, prove period or homology normalization, restore blindness, certify novelty, or promote Working Truth/Foundation status.

The source status `INCOMPLETE` and formal review/return boundaries are preserved. A gate-by-gate durable return and Root's formal Driver procedure remain distinct actions. This review supplies the additional disclosed paper/code checking requested for that return; it creates no DR/RR/claim and does not close the research parent.

Reviewer: Owner-delegated `integration_admission_check`, shared-context source-exposed peer.

Global knowledge context: existing canonical `main@3ad395d666b488e89f4e1cef56ec8fbdf9732a18` lease, valid through 2026-09-09T05:10:38Z; no new startup or authority was inferred from this review.
