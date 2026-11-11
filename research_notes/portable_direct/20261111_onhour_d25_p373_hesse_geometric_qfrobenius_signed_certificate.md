# D25/LIFT — p=373 原始 Hesse 曲线几何 Frobenius 符号精确证书

**2026-11-11 / TASK_RESEARCH / AUTHOR_SIDE / EXECUTED EXACT FINITE-FIELD GEOMETRIC CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NATIVE_H0B0_[X]U_NOT_RUN.**

Mother objective: \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`; Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication: \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source: \`awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3\` (not rebased). Declared on-hour Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`, never the maintenance lane. No authenticated own native CLAIM/open run/checkpoint.

## 1. Exactly which original object was computed

Consume the frozen CM0/JT2 Hesse port of \`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md\` (immutable blob \`cf36004694dc2c8c9134e2e1e989c076b88e4c03\`): \`t²=1/2\`, \`u=(1-t)/2\`, and the **actual Hesse cubic** \`E_lambda: X³+Y³+Z³−3 lambda XYZ=0\` with \`lambda^(-3)=u\`. The accepted CM calculation identifies its \(j\)-roots with discriminant \(-24\). This unit studies **that exact Hesse family and parameter**, not a generic unrelated curve and not the still-missing H0/B0 divided-power module.

At \(p=373\), work in the field \(K=\mathbb F_{373}[T]/(T^2-2)\), \(|K|=q=139129\). Since \((2/373)=-1\), this is \(\mathbb F_{373^2}\). Choose \(t=T/2\) and hence
\[
u=(2-T)/4=187+93T,\qquad \lambda=56+19T,\qquad
\lambda^3=4+2T,\qquad \lambda^3u=1.
\]
The denominator and curve discriminant are nonzero. The second tagged source port is the conjugate \(T\mapsto -T\), \(\bar\lambda=56-19T\). All equalities in this section were checked as integer residue pairs.

The actual Hesse \(j\)-invariant,
\[
j(\lambda)=\frac{27\lambda^3(\lambda^3+8)^3}{(\lambda^3-1)^3}
=59-43T\in K,
\]
is one of the two reductions of \(2417472\pm1707264\sqrt 2\) from the frozen CM source. It satisfies
\[
j^2-4834944j+14670139392=0\quad\text{in }K.
\]
Thus the geometric point count below is on a **source-aligned original Hesse curve**. It still does not identify an H0/B0 cohomology basis, \(\eta\), or the original divided-power \([X]U\).

## 2. Exact projective change and complete point counting

Make the invertible projective change
\[
[U:V:W]=[Z:X-Y:X+Y+\lambda Z],
\]
whose matrix has determinant \(2\neq0\) in \(K\). The old flex \([1:-1:0]\) becomes the unique point at infinity \([0:1:0]\) of the new cubic. With \(x=U/W\), \(y=V/W\), direct expansion of the Hesse equation gives **exactly**
\[
3y^2=-1+6\lambda x-9\lambda^2x^2+4(\lambda^3-1)x^3.
\tag{H}
\]
For \(\lambda=56+19T\), the right-hand side after dividing by 3 has the explicit coefficients
\[
\boxed{y^2=(4+127T)x^3+(362+330T)x^2+(112+38T)x+124.}
\]
As a local transformation witness, the original Hesse point \([1:0:-1]\) maps to \(x=173+103T,\ y=200+270T\) and satisfies (H).

For a field element \(v=a+bT\), the **actual quadratic character** in \(K\) is
\[
\chi_K(v)=\chi_{373}(N_{K/\mathbb F_{373}}(v)),
\qquad N(v)=a^2-2b^2,
\]
with \(\chi_K(0)=0\). The point count is
\[
\#E_\lambda(K)=q+1+\sum_{x\in K}\chi_K(f_\lambda(x)).
\]
This is an exact exhaustive sum over all \(q=139129\) field elements, not a random-prime regression.

The executed modular-integer program obtained
\[
\begin{array}{c|rrr|r|r}
\text{Hesse branch / twist}&\#\{\chi=-1\}&\#\{\chi=0\}&\#\{\chi=1\}&\#E(K)&t_q=q+1-\#E\\
\hline
\lambda=56+19T&69936&3&69190&138384&+746\\
\sigma(\lambda)=56-19T&69936&3&69190&138384&+746\\
\text{quadratic twist by }T&69190&3&69936&139876&-746
\end{array}
\]
Each histogram sums to 139129. Two logically different exact counting procedures agreed in **all three cases**: (i) norm followed by prime-field Legendre character, and (ii) independent enumeration of all \(y^2\) fibers to count solutions of \(y^2=f(x)\). The \(y^2\) fiber histogram itself is \(69564\) zeros, \(1\) singleton, and \(69564\) doubletons. No floating point, probabilistic primality test, fitted parameter, or unrelated curve substitution is used.

Since \(\chi_K(T)=-1\), multiplying the right side of (H) by \(T\) produces a genuine quadratic twist with the **same \(j\)**, but its character sum has the opposite sign. In particular,
\[
\boxed{\#E_\lambda(\mathbb F_{373^2})=(373-1)^2=138384,}
\quad
\boxed{\#E_\lambda^{(T)}(\mathbb F_{373^2})=(373+1)^2=139876.}
\]
For the geometric \(q=373^2\) Frobenius of the specified Hesse cubic, the characteristic polynomial is
\[
X^2-746X+139129=(X-373)^2,
\]
while the quadratic twist has \(X^2+746X+139129=(X+373)^2\). This **determines the sign at the original Hesse curve level for this specified \(p\), branch and model**, and constructs an exact signed negative control with identical \(j\) and opposite geometric Frobenius trace.

## 3. BRC observer preservation and significance for D25

**Exact new information:** \(j\)-invariant or the CM \(-24\) class **alone does not recover the signed \(q\)-Frobenius trace**. Two geometrically isomorphic-over-closure Hesse-related curves with the same \(j\) have traces \(+746\) and \(-746\) after a concrete quadratic twist. This is an explicit finite-field *observer-fiber counterexample* to any \(j\)-only signed Frobenius readout, not a counterexample to LIFT.

Preserved carrier: \(p\), \(K\), ordered \(u,\sigma(u)\), \(\lambda,\sigma(\lambda)\), Hesse equation, twist \(d=T\), projective coordinate map, complete character histograms, and signed \(t_q\). Future operation: mapping true original H0/B0 semilinear Frobenius, its \(\eta\)/basis, and odd Green/Hesse \(\kappa\) to a signed scalar. The exact pair \(t_q=\pm746\) requires a twist/normalization port; replacing it by \(j\) or \(|t_q|\) would erase a required sign. This is an external finite-field arithmetic calculation in the fixed source Hesse family, **not** a new native two-dimensional spatial plane under P000/X6.

The rank-two *auxiliary* model from earlier author notes happened to test \(F\sigma(F)=+373I\). The present measured geometric sign is \(+373\) on its specified Hesse curve, but **no identification of that auxiliary matrix with the actual divided-power H0/B0 Frobenius follows**. Even its semilinear direction, normalization \(\eta\), original \(\kappa\), and true module rank remain unmeasured. The original \(\Delta_{373}=R_{373}=196\) is an already-persisted separate scalar interface; it is neither newly recredited nor deduced from the present point count.

## 4. Evidence, limitation, and next *real* native action

Reproducible executed checker: \`research_notes/portable_direct/d25_p373_hesse_geometric_trace_verify_20261111.py\` (Python standard library; two complete point-count routes and hard assertions for original/conjugate/twist). The finite-field sum is an exact complete certificate for the named \(p=373\) and exact Hesse models. Its derivation uses ordinary projective algebra and the standard elliptic-curve point-count trace formula; there is no all-target-prime Frobenius theorem or native p-adic H0/B0 claim here.

The original highest-priority **unexecuted** native benchmark remains exactly
\[
\boxed{[X]U\bmod373^2=139129}
\]
for the fixed *same-original-class* H0/B0 divided-power representative, with actual native module rank, the real semilinear Frobenius direction, basis/filtration and \(\eta\), signed odd Green/Hesse \(\kappa\), original \(\Delta_p-R_p\) and independent reproduction. It must authenticate the specific Hesse/CM **model and twist correspondence** before using this geometric \(+373\) as its sign cross-check. A twist disagreement is a typed model/normalization difference, not a fabricated LIFT counterexample.

Actual responsible intake remains \`awdawmip/enterprise-math\` Issue **#1559 OPEN / PENDING_OWNER**. Next action belongs to a lawfully authorized owner/native evaluator: read frozen H0/B0 operator source and execute original \([X]U\) with code/coefficients/normalization, then compare the geometric sign only after an explicit source-port map and route a fresh native artifact through authenticated Research/Driver. No native evaluator is claimed in this author note.

Source readback (existing Research lane): \`onhour11-20261111-0807-exact-cont\` and \`onhour11-20261111-0807-task\` both \`SUCCEEDED\` against \`4c95884f9871ad6db9adecee4d14f443ffc17dc8\`; exact route \`PREPARE_TYPED_CONTINUATION_WITH_EXACT_PREDECESSOR_AND_FRONTIER\`, \`execution_authorized=false\`, Source task state \`actor=null, claim_id=null\`. Own \`recovery_status\` returned \`SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED\`. No private Researcher capability, no winning CLAIM, open run, native checkpoint/Result/independent review. Existing D24 UR/CM0, earlier scalar fixtures, Hesse norm/gauge lemmas and unrelated owners are consumed, not recredited.

**Status:** \`EXACT_SOURCE_ALIGNED_HESSE_P373_GEOMETRIC_TRACE_CERTIFICATE / DUAL_EXHAUSTIVE_CHECKS / SIGNED_TWIST_DISCRIMINATOR / AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED / NATIVE_H0B0_PENDING\`.
