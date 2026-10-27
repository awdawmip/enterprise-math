# D25 / original weighted 216: E.2 prior-art transfer fails at the first missing p-adic band

**2026-10-27 / research-onhour / AUTHOR-SIDE / ALL-PRIME TERM-VALUATION NO-GO PROVED / TEN EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_EXECUTED / REGISTER_PENDING.**

Research task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; unchanged frozen science Source c47e13e4aba0e006366f989d6334d443f6333ae3. Logical lane chatgpt-research-onhour-enterprise-math-20260923 only; NOT a Source CLAIM, activity, run, checkpoint, or Result.

## Source, theorem, and frozen target

Guo and Schlosser, *Results in Mathematics* **78** (2023), article 105, DOI https://doi.org/10.1007/s00025-023-01885-8 , introduction equation (1.2), present the proved Van Hamme E.2 supercongruence (attributing its prior proof to Swisher):

\[
E_p=\sum_{n=0}^{(p-1)/3}(-1)^n(6n+1)\frac{(1/3)_n^3}{(n!)^3}\equiv p\pmod{p^3}
\quad(p\equiv1\bmod3).
\]

The *original frozen D25* weighted 216 object differs in parameters, argument and truncation:

\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
=\sum_{n=0}^{p-1}(6n+1)\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3\,2^n}.
\]

LIFT/JT2 still asks to prove or refute \(W_p\equiv p\pmod{p^3}\) for *both* frozen classes \(p\equiv13,19\pmod{24}\), equivalently \(\Delta_p-R_p\equiv0\bmod p\) under previously proved Source alignment. Two right-hand sides equal to p do not identify the two series' p-adic intermediate observers.

## New all-prime sharp valuation mismatch

For any prime \(p=6m+1>3\), let \(n_0=2m+1=(p+2)/3\) and denote the true signed/weighted summands of the external E.2 and original W by \(e_n,w_n\).

In E.2, \((1/3)_{n_0}\) contains \(p/3\), with all its other factors p-units. Since \(n_0<p\) and \(6n_0+1=2p+5\) is a p-unit (p>=7), \(v_p(e_{n_0})=3\). For every \(n_0\le n<p\), \(e_n\equiv0\bmod p^3\). Thus E.2's published short cutoff extends to \(p-1\) modulo p³, *but it remains E.2, not W*.

For the original W at this **same index** \(n_0\), \(2n_0=4m+2<p\) whereas \(3n_0=p+2<2p\). Thus the factorial expression \(\binom{2n_0}{n_0}^2\binom{3n_0}{n_0}\) has valuation exactly one. Neither \(216\) nor the weight \(6n_0+1=2p+5\) contributes p. Therefore

\[
\boxed{v_p(w_{n_0})=1,\qquad v_p(e_{n_0})=3
\quad\text{for every prime }p\equiv1\pmod6,\ p>3.}
\]

An index-preserving p-integral **unit** identification \(w_n=u_ne_n\), including ordinary unit gauge or simple termwise transport, is **impossible** modulo the required p³ at the exact entry of the original *middle p-adic band*. The mismatch is a proved information-loss witness; it does not exclude index mixing, a nonlinear pullback, a nonunit factor with a separately proved boundary correction, or the truth of W's target theorem.

A second exact narrow falsifier rules out constant rescaling of the two formal coefficient sequences: W's first three weighted terms at the fixed original argument are \(1,7/18,65/432\); E.2's are \(1,-7/27,104/729\). Their constant terms force prefactor 1, linear terms force argument scale \(-3/2\), while quadratic terms require its square \(135/128\ne9/4\). This is **NO_SIMPLE_ARGUMENT_RESCALE**, not **NO_NONLINEAR_TRANSFORMATION**.

## Executed evidence and use of BRC

The companion script d25_van_hamme_e2_transfer_scope_20261027.py performs exact modular-integer recurrence checks with no floating point, at ten selected primes 7,13,19,31,37,43,61,67,211,373. All assertions passed, including external E.2 modulo-p³, original W finite regression, exact E.2 cutoff, nonzero original middle-band p-digit and formal coefficient test. At p=13,19,373 the retained original single summand has \(w_{n_0}/p\bmod p=10,13,108\) respectively, while the same-index external summand is 0 modulo p³. The finite W checks are not an all-prime proof.

**BRC interface actually applied:** carrier = indexed source-tagged E.2/W weighted terms; observers = signed finite total, degree cutoff and p-adic valuation (not total alone); allowed operations = indexed unit scaling or bounded finite summation at p³. An index-erasing scalar quotient loses the witnessed p-adic band. No P000/X6-native geometric transfer is asserted; this is typed external hypergeometric mathematics only.

**Scientific increment:** A proven all-prime *prior-art transfer obstruction* precisely at the frozen D25 middle band and a separate exact formal no-simple-rescaling proof. It is not a new H0/B0 experiment and does not establish LIFT. Consume existing CM0/UR, reflection source R, four-port reduction, p⁴-sharpness and prior finite regressions without counting them again.

## Highest frontier / continuation

Issue https://github.com/awdawmip/enterprise-math/issues/1559 remains the already-existing native-capability support intake: OPEN / PENDING_OWNER / NOT_EXECUTED at the 2026-10-27 read. The fixed original-class p=373 H0/B0 divided-power calculation still needs real \([X]U\bmod139129\), actual rank and base, genuine semilinear Frobenius direction and eta, signed odd Green/Hesse, kappa, Delta-R, version-pinned inputs and independent checking. The responsible path is the actual Source Task owner / authorized native executor or designated implementation maintainer; **no native executor or Source run is represented by this note**.

The first next scientific action is authenticated native execution via #1559. If canonically authorized to pursue an external prior-art bridge separately, demand an explicit nonlinear/index-mixing transformation **with retained cutoff and p-adic digit corrections**, rather than a scalar similarity claim. This is not a fresh dispatched Task.

Last exact successful Source continuation request onhour-20261027T1705-D25-exact-continuation read back as execution_authorized=false. The current onhour-20261027T2203-D25-exact-continuation returned CONTROL_QUOTA; current Sites identity is read-only, research_authority_granted=false. Historical GitHub bridge requests are out of scope for this native control_result. No legitimate own Source CLAIM/open/run/Result exists for this turn; no other lane's session or owner adopted. This standalone GitHub note is **not** a canonical Source publish_checkpoint. D25/LIFT/JT2 OPEN; notification/scheduler settings unchanged.
