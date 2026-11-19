# EC49FTU Supplement — Complete two-parameter sharp phase diagram

**Status:** AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.
**Date:** 2026-11-19. Extends the first EC49FTU theorem on the same Draft PR; no changes to frozen native scientific inputs.

## 1. Statement

Continue to use the exact inherited BRC16943 *external high-gap price observation* from EC49FTS and the fixed native Bellman scientific pin \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. The high-gap conditioning interval is
\[
I=(m_2,m_3)=(1469/64,187/8),\quad
t=m_3-m\in(0,27/64),\quad U=3/4.
\]
The price domain is \`3/4<=a<=49/64\`, \`7/16<=b<=57/128\`, and the clipping curve is \`a_c(b)=(77+6b)/105\`. The full inherited coordinate map, Jacobian and continuous/clip mass definitions are in \`EC49FTU_JOINT_PRIOR_THEOREM.md\`.

For a *two-parameter* family \`0<=theta<=1\`, \`lambda>=0\`, define
\[
h_\theta(a,b)=(1+a+b)[1+\theta(a-a_c(b))],\qquad
m(b)=47-54b,\quad t(b)=m_3-m(b),
\]
\[
\delta(b)=49/64-a_c(b)>0,\quad
f_{\theta,\lambda}(b)=\frac{54\lambda\,t(b)A_\theta(t(b))}{\delta(b)},
\]
\[
\boxed{h_{\theta,\lambda}(a,b)=
h_\theta(a,b)+f_{\theta,\lambda}(b)
\psi\left(\frac{a-a_c(b)}{\delta(b)}\right)}
\]
where \`psi(s)=0\` for \`s<=0\` and \`psi(s)=exp(-1/s^2)/J\` otherwise, with \`J=int_0^1 exp(-1/s^2)ds>0\`. The density is normalized by its finite positive integral on the fixed price box. It is strictly positive and \`C^\infty\` there.

**Sharp two-parameter phase theorem.** For every \`theta in [0,1]\`, every \`lambda>=0\`, and all real \`m<m'\` in \`I\`,
\[
Z\mid M=m\preceq_{\rm st}Z\mid M=m'
\quad\text{for all such pairs}
\quad\Longleftrightarrow\quad
\boxed{0\le\lambda\le\Lambda(\theta),}
\]
where the *explicit exact rational function* is
\[
\boxed{
\Lambda(\theta)=
\frac{3500\bigl(862686243742176000
-2239375169798320\theta-18989094173841\theta^2\bigr)}
{6561(413340200-1327113\theta)^2}.
}
\]
Furthermore \`\Lambda\` is **strictly increasing** on \`[0,1]\`, with exactly
\[
\Lambda(0)=\frac{171167905504400}{63545784776721},
\qquad
\Lambda(1)=\frac{3011497578173713436500}{1113761136900667642209}.
\]
The first endpoint recovers EC49FTT, while the second recovers the new EC49FTU fixed-\`theta=1\` theorem. This is a complete continuous interpolation, not finite sampling.

## 2. Baseline continuous and clipped fibers

On a nonclipped fiber,
\[
a(m,z)-a_c(b(m,z))=\frac{8(4z-3)}{35}.
\]
Thus
\[
K_\theta(m,z)=\frac{16}{945}[1+a(m,z)+b(m,z)]
\left[1+\theta\,\frac{8(4z-3)}{35}\right].
\]
The bracket is positive for \`theta in [0,1]\` on \`z<=3/4\`, because its minimum is at \`theta=1\` and is \`>=11/35\`. The price prior itself remains positive: \`1+a-a_c(b)>=6661/6720>0\`.

The bracket depends only on \`z\`. Hence the strict TP2 log-cross derivative is independent of \`theta\`:
\[
\partial_m\partial_z \log K_\theta=
\frac{(37/1890)(94/45)}
{[1+a(m,z)+b(m,z)]^2}>0.
\]
As \`L(m)=(8m+173)/480\` increases with \`m\`, the normalized continuous conditional laws are stochastically increasing.

Exact rational integration of the continuous fiber and the clipped \`a\`-interval gives
\[
\boxed{A_\theta(t)=\frac{tQ_\theta(t)}{421954312500},
\quad
Q_\theta(t)=3296t^2\theta-1992060t\theta+258300t+261457875,}
\]
\[
\boxed{
B_\theta(t)=
\frac{(64t-441)
(109568t^2\theta+12022416t\theta-209018880t
-88044327\theta-24135965280)}
{35838544379904000}.
}
\]
The integrals are positive, as is the original price prior. The smooth flat bump vanishes identically on the continuous region, and its clipped integral is exactly \`\lambda t A_\theta(t)\`. Therefore
\[
r_{\theta,\lambda}(m)=\frac{B_\theta(t)}{A_\theta(t)}+\lambda t
=:r_\theta(m)+\lambda(m_3-m).
\]

## 3. Universal strict convexity in m on the entire (t,theta)-rectangle

Write \`P(t,theta)=P0(t)+theta*P1(t)+theta^2*P2(t)+theta^3*P3(t)\`. Exact rational differentiation gives
\[
\boxed{
\frac{\partial^2 r_\theta(m)}{\partial m^2}
=\frac{875P(t,\theta)}
{589824\,t^3 Q_\theta(t)^3}.
}
\]
For reproducibility the **full integer polynomial** has the following ascending-degree coefficients (each row is \`[t^0,t^1,...]\`):

\`P0\`:
\`\`\`text
[11549579342670997976722500000,
 34230252321280268694000000,
 33816821063762923200000,
 12801796518963916800000]
\`\`\`

\`P1\`:
\`\`\`text
[42131107190529170303765625,
 -263865518225915450565262500,
 -84690274701240897570000,
 -59022641298932077536000,
 490066449785192448000]
\`\`\`

\`P2\`:
\`\`\`text
[0, -962996735783523892657500,
 2011045926875081504688000,
 -94073316394194182707200,
 435121386935995791360,
 -1039174690028912640,
 -2401505839677440]
\`\`\`

\`P3\`:
\`\`\`text
[0, 0, 7337117986922086801200,
 -721265226914893489920,
 3459632021600477184,
 -5657731060875264,
 855171863150592]
\`\`\`

**Uniform sign proof (all real parameters).** Since \`0<t<27/64<1\` and \`0<=theta<=1\`, each positive-coefficient monomial is nonnegative, while the absolute value of every negative monomial is bounded by its coefficient magnitude. Summing **all** negative-coefficient magnitudes of \`P\` gives
\[
265067023506554183438688464,
\]
strictly smaller than the positive constant monomial
\[
11549579342670997976722500000.
\]
Thus \`P(t,theta)>0\` on the *entire rectangle*. Also
\[
Q_\theta(t)\ge261457875-1992060=259465815>0,
\]
because all its other terms are nonnegative. Therefore
\[
\partial_m^2r_\theta(m)>0
\quad\forall\,0<t<27/64,\ 0\le\theta\le1.
\]
This is an analytic uniform proof, not an assertion extrapolated from samples.

## 4. Exact moving sharp threshold and monotonicity in theta

Strict convexity means \`\partial_m r_\theta\` is strictly increasing in \`m\`; its infimum on \`I\` occurs at the *left limit* \`m\downarrow1469/64\`, or \`t\uparrow27/64\`. Exact evaluation gives the rational function \`\Lambda(\theta)\` displayed above. The top-atom criterion from EC49FTR applies because the continuous law is stochastically increasing and the top endpoint is fixed; hence the full conditional family has first-order stochastic increase **iff** \`r_{\theta,\lambda}\` is nondecreasing. Its derivative is
\[
r'_{\theta,\lambda}(m)=r'_\theta(m)-\lambda.
\]
The uniform strict convexity therefore proves the stated exact half-closed region \`0<=lambda<=Lambda(theta)\`; at the threshold the derivative is strictly positive at every interior \`m\`. For \`lambda>Lambda(theta)\` it becomes negative on an interior left neighborhood, giving an exact upper-atom-order obstruction.

Finally differentiate the explicit threshold:
\[
\boxed{
\Lambda'(\theta)=
\frac{2240000(2131469495973983261425
-29171587292164226979\theta)}
{6561(413340200-1327113\theta)^3}>0,
\quad 0\le\theta\le1.
}
\]
Both numerator and denominator are positive throughout the stated interval, proving strict growth of the sharp allowable atom slope as the continuous prior tilts.

## 5. Validation and open directions

The companion \`EC49FTU_TWO_PARAMETER_VERIFY.py\` uses only Python's \`fractions.Fraction\`, implements sparse exact bivariate polynomial arithmetic, checks the universal identity for \`r_{\theta}''\` by polynomial cross multiplication, the exact all-\`theta\` rational formula for the endpoint derivative, both endpoint thresholds, and 217 independent rational integrations across seven values of \`theta\` and 31 interior values of \`t\`. It does not run native BRC or independently review the inherited optimizer. The universal theorem is analytic as proved above.

**Next:** determine maximal admissible \`theta\` ranges outside \`[0,1]\` under price-prior positivity, then seek more general non-affine continuous-kernel changes and sharp atom compatibility criteria. The native \`z<11/16\` Bellman phase is a separate open problem. The native 228-observer result remains PARENT_DEPENDENT/NOT_REVIEWED; no Source CLAIM, Activity association, formal Result or mathematical Review is acquired by a file publication.
