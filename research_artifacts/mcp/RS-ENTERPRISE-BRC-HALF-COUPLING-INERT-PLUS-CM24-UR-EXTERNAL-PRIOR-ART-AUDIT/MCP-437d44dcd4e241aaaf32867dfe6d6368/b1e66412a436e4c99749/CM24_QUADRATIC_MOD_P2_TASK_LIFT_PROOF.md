# Finite Gauss–Hesse quadratic comparison at the Task rational half

Status: EXECUTED_BOUNDED_COMPARISON / AUTHOR_PROOF_AND_EXACT_REGRESSION_PASS /
DECISIVE_READONLY_REVIEW_PENDING / NO_FORMAL_MATHEMATICAL_ACCEPTANCE.

Own actual winning claim: `MCP-634560f210aa28118cb281a0`, epoch `6109143010`.
Own authorized execution: `ER-76196AE54358D3A41681`,
`RUN-725aa319e999e96ac1a99acb`, generation 1, session
`MCP-437d44dcd4e241aaaf32867dfe6d6368`. Actual execution-open succeeded
before the checker ran. The preparation snapshot is retained separately.

Prepared for one bounded continuation of
`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT`,
publication `TP2-E133E3FC788A867C5BAD`.

The direction and initial valuation hint were proposed by Root Driver
`EM-DVR-4C90FB` in a shared, nonblind context. This researcher's argument,
precision boundaries and task-local checker must receive another researcher's
decisive read-only check; a new identity does not establish clean blindness.
The result is an arithmetic comparison supporting the audit's exact-normalization
gate. It is not a proof of UR or LIFT or a period-normal identification.

## 1. Exact finite objects and the claim to be checked

For a prime \(p=6m+1\) (necessarily \(p\ge7\)), define
\[
a_n=\frac{(1/6)_n(1/3)_n}{(n!)^2},\quad
b_n=\frac{(1/3)_n(2/3)_n}{(n!)^2},\quad 0\le n<p,
\]
\[
f_p(w)=\sum_{n=0}^{p-1}a_nw^n,\qquad
L_p(x)=\sum_{n=0}^{p-1}b_nx^n,\qquad q(x)=4x(1-x).
\]
The proposed uniform comparison is
\[
f_p(q(x))\equiv L_p(x)\pmod{p^2}
\quad\text{in }\mathbf Z_{(p)}[x]. \tag{Q2}
\]
The rational Task value is exactly \(g_p=f_p(1/2)\), because
\(a_{n+1}(1/2)^{n+1}/[a_n(1/2)^n]
=(6n+1)(3n+1)/[36(n+1)^2]\), the inherited \(B_n\) recurrence.
We use \(\bar G_p=g_p/p\bmod p\) only when \(p\mid g_p\).
The stronger inherited notation \(G_p=g_p/p\bmod p^2\) carries a second
digit; (Q2) alone does not transport that second digit.

## 2. Characteristic-zero identity, proved without a truncation exchange

Let \(F(w)={}_2F_1(1/6,1/3;1;w)\) and
\(L(x)={}_2F_1(1/3,2/3;1;x)\) as formal series in characteristic zero.
The Gauss differential operator is
\[
\mathcal D_G F=w(1-w)F''+(1-3w/2)F'-F/18.
\]
The Hesse operator is
\[
\mathcal D_HY=x(1-x)Y''+(1-2x)Y'-2Y/9.
\]
For \(Y(x)=F(q(x))\), direct polynomial identities give
\[
x(1-x)(q')^2=4q(1-q),\qquad
x(1-x)q''+(1-2x)q'=4-6q,
\]
so \(\mathcal D_H(F\circ q)=4(\mathcal D_GF)\circ q=0\).
The coefficients of a solution with constant term 1 satisfy
\[
(n+1)^2c_{n+1}=(n+1/3)(n+2/3)c_n.
\]
Every \((n+1)^2\) is invertible in \(\mathbf Q\), proving uniqueness and
therefore \(F(q(x))=L(x)\) in \(\mathbf Q[[x]]\). No assertion about the
integrality of the infinite tails at indices \(n\ge p\) is used.

## 3. Exact valuation cutoffs and every coefficient of (Q2)

For \(0\le n<p\), \(n!\), 3 and 6 are units at \(p\). In the Gauss
numerators the unique factors divisible by \(p\) are
\(6m+1=p\) at \(j=m\), and \(3(2m)+1=p\) at \(j=2m\).
They each occur once and have valuation exactly one. Thus
\[
v_p(a_n)=\mathbf1_{n>m}+\mathbf1_{n>2m}.
\]
For Hesse the unique divisible factors are
\(3(2m)+1=p\) and \(3(4m)+2=2p\), giving
\[
v_p(b_n)=\mathbf1_{n>2m}+\mathbf1_{n>4m}.
\]
The possible numerator factors lie below \(6p\) or \(3p\); the relevant
residue classes exclude additional multiples of \(p\), and the displayed
factors \(p,2p\) have no extra \(p\)-power. These formulas cover the
boundary indices themselves: the new factor enters at \(n=j+1\).

Consequently \(f_p\) modulo \(p^2\) has degree at most \(2m\), and
\(L_p\) modulo \(p^2\) has degree at most \(4m\). The composed Gauss
polynomial has effective degree at most \(4m<p\). For every coefficient
\(x^k\) with \(k<p\), the characteristic-zero identity only involves
Gauss indices \(n\le k<p\), since \(q\) has order one at zero. Hence
these coefficients of the *finite* polynomials are exactly equal over
\(\mathbf Q\). For \(k\ge p\), both effective polynomials have zero
coefficient modulo \(p^2\). This proves (Q2) coefficientwise over the
entire degree range \(0\le k\le2p-2\).

The proof is stronger than a pointwise identity at a CM zero and does not
use a supersingular hypothesis. It applies to every prime \(p\equiv1\pmod6\),
including the ordinary residue classes. A prime such as 5 is outside this
statement; treating \(m=(p-1)/6\) as an integer there is invalid.

## 4. Exact algebraic lift and the first divided digit

Work in the finite étale algebra
\[
\mathcal O=\mathbf Z_{(p)}[s]/(s^2-2),\qquad
x_\pm=(2\pm s)/4=1/(4\mp2s).
\]
Since the discriminant 8 is a unit, the reduction and division-by-\(p\)
arguments are unramified. For the Task classes \(p\equiv13,19\pmod{24}\),
2 is a nonsquare, so this is the unramified quadratic local extension.
Exactly, rather than just modulo \(p\),
\[
x_- =1-x_+,\qquad q(x_+)=q(x_-)=1/2.
\]
(Q2) therefore gives
\[
L_p(x_\pm)\equiv g_p\pmod{p^2\mathcal O}. \tag{V2}
\]
The inherited CM0 supplies \(p\mid g_p\) for the two Task classes; this
unit does not re-prove CM0. Thus \(L_p(x_\pm)\in p\mathcal O\), and
\[
\frac{L_p(x_\pm)}p\equiv\frac{g_p}p=\bar G_p
\pmod{p\mathcal O}. \tag{DIGIT}
\]
This division is well-defined from a mod-\(p^2\) value in the ideal
\(p\mathcal O/p^2\mathcal O\). Changing a representative by \(p^2a\)
changes its quotient by \(pa\), which vanishes modulo \(p\).
The implication is bidirectional at this precision: a proposed value
\(d\) satisfies \(L_p(x_\pm)=pd\bmod p^2\) exactly when
\(g_p=pd\bmod p^2\). No extra period scale is chosen.

## 5. Frobenius branches, derivative orientation and the UR comparison

The exact automorphism \(\sigma(s)=-s\) exchanges \(x_+,x_-\).
On the Task reduction it is the \(p\)-power Frobenius. On
\(\mathcal O/p^2\mathcal O\), \(\sigma\) is the lifted Frobenius
automorphism; the literal operation \(a\mapsto a^p\) need not equal it
and is not an additive ring endomorphism. The exact algebraic lifts above
must not be silently replaced by Teichmüller lifts.

Differentiating the coefficientwise congruence gives
\[
L'_p(x_\pm)\equiv q'(x_\pm)f'_p(1/2)\pmod{p^2},\qquad
q'(x_\pm)=\mp2s.
\]
Therefore the branch derivatives are conjugate and opposite, while the
branch values and divided digits are the same. This does **not** lose the
signed scalar \(\bar G_p\). It does mean that the scalar value alone is
not an observer of the Hesse branch orientation. Retain the marked branch
and its Jacobian before a future comparison to an oriented period.

Using the inherited \(f'_p(1/2)=-Q'_m(1/2)\bmod p\), the Task UR
certificate can now be compared in this coordinate as
\[
\bar G_p(-6Q'_m(1/2))=1
\iff
\frac{L_p(x_\pm)}p\frac{6}{q'(x_\pm)}L'_p(x_\pm)=1\pmod p.
\tag{UR-COMPARE}
\]
Here \(6/q'(x_\pm)=\mp3/s\) is an independently fixed coordinate
Jacobian, not a scalar selected from the desired UR answer. SIMPLE ensures
the inherited Gauss derivative is a unit. This is an equivalent target,
**not a proof that either side equals 1**, and the Hesse derivative is not
identified here with the fixed source's period-normal scalar.

## 6. Lift sensitivity: why a mod-p marked point is insufficient

For \(\delta\in\mathcal O\), the finite polynomial Taylor formula gives
\[
\frac{f_p(1/2+p\delta)}p
\equiv\bar G_p+\delta f'_p(1/2)
=\bar G_p-\delta Q'_m(1/2)\pmod p.
\]
For a branch lift \(x_\pm+p\epsilon\),
\[
q(x_\pm+p\epsilon)=1/2+p q'(x_\pm)\epsilon\pmod{p^2},
\]
\[
\frac{L_p(x_\pm+p\epsilon)}p
\equiv\bar G_p+\epsilon L'_p(x_\pm)\pmod p.
\]
All second Taylor terms vanish at this stated precision. On the Task
classes both derivatives are units. Consequently nonzero shifts can change
the divided digit while retaining the same residue-field point. The exact
algebraic lift fixes this ambiguity for the present arithmetic bridge; it
does not prove that a separately defined modular period uses this lift.

## 7. Sharp precision boundary

The coefficient of \(x^{2p-2}\) in
\(f_p(q(x))-L_p(x)\) is \((-4)^{p-1}a_{p-1}\), with valuation exactly
two. Thus the uniform *polynomial* comparison is false modulo \(p^3\) for
every prime in the statement. Pointwise cancellations at a particular lift
would need separate proof; they cannot be inferred from (Q2).

In particular this unit transports \(g_p\bmod p^2\) and
\(g_p/p\bmod p\). It does not transport \(g_p/p\bmod p^2\), prove
the inherited LIFT target, or license removal of cutoff-dependent second
digits. The full coefficients and exact lifts remain available for future
work at a stronger precision.

## 8. Observer certificate and semantic boundary

The retained arithmetic population is the exact finite coefficient arrays,
Task rational half, both marked algebraic lifts, conjugation, signed values,
derivatives, Jacobians and precision. The permitted observers for this
bridge are polynomial evaluation/differentiation, reduction modulo \(p^2\),
and division of a \(p\)-divisible value followed by reduction modulo \(p\).
These operations are certified by (Q2), (DIGIT) and the differentiated map.
The branch value may be compressed to \(g_p\) for its divided-value
observer only; that certificate excludes an oriented Hesse derivative or
future period/normal observer. We retain the branch tags and Jacobians.
Neither the zero reduction \(L_p(x)\bmod p\) nor a norm substitutes for
the signed divided digit.

P000, the Heartbeat World X6/time contract, residual fidelity, and joint
relation observer preservation were loaded before preparation. This is a
static *external arithmetic readout*, not a standalone lower-dimensional
native spatial model, a native Cell-address codec, a propagation theorem,
or a change to the native six-dimensional ontology. No native-state
embedding is established by an algebraic hypergeometric coordinate map.
Time records execution provenance separately; this static identity does not
require time as another spatial coordinate.

## 9. Reuse, bounded regression and remaining gate

The current toolbox/method inventory was checked at fixed Source. BRC
branch/provenance preservation and operation-safe quotient discipline are
reused; the existing finite integer precision projection/detail/recomposition
functions are composed with canonical residue representatives. The exact
Source functions are retained and executed unchanged by AST extraction.
This is a task-local checker, with no new general-purpose tool family or
method-novelty claim. The lexical scale/valuation calculus does not replace
the elementary prime-adic factor count above.

The executed exact regression uses ten representative primes, including both
target residue classes, the smallest admissible prime 7, ordinary classes,
all factor-entry boundaries, a negative excluded prime 5, explicit shifts,
and mod-\(p^3\) polynomial negative checks. It does not repeat the prior
77-prime CM0/UR/LIFT audit. All ten coefficientwise mod-p² and derivative/
reflection checks passed; six Task-class cases passed the divided-digit and
shift checks. All ten highest coefficients give the expected mod-p³ failure.
The excluded prime 5 has coefficient failures at degrees 5–8 modulo 25.
The exact values at the smallest two Task primes are
\(\bar G_{13}=11\), \(\bar G_{19}=8\).
At 13, shifting the rational half by 13 changes the digit from 11 to 12.
Also \(x_+^{13}-\sigma(x_+)=13+78s\bmod169\), so literal powering
does not implement the lifted Frobenius. The checker records the resulting
shifted Hesse digit separately. A pointwise precision-extension counterexample
is
\[
L_{13}(x_+)-f_{13}(1/2)=507+1690s
=13^2(3+10s)\pmod{13^3},
\]
nonzero in the unramified quadratic algebra. The uniform proof supplies
all-prime (Q2); these finite checks are regression and sharp-boundary evidence,
not an all-prime proof of UR or LIFT. A separate decisive review remains
required and must be bound to final exact bytes before publication.

The remaining interface is the independently calibrated oriented raw
period/normal on the marked source curve: identify its actual polynomial,
local parameter, Fourier/sign gauge and lift, and prove a source-level
bidirectional comparison with this finite Hesse divided value. No constant
is selected from UR, and no source-wide absence, literature exhaustion,
novelty, Working Truth, Foundation or mathematical parent completion follows.

Researcher-ID: EM-ENTERPRISE-A1D9B5 / RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-CM24-UR-EXTERNAL-PRIOR-ART-AUDIT
