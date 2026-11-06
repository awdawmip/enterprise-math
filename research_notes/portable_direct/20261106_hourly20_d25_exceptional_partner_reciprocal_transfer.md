# D25 — Exact reciprocal transfer at the exceptional weighted coordinate

Date: 2026-11-06. Scope: portable author-side mathematical research, UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific input pin: c47e13e4aba0e006366f989d6334d443f6333ae3.

This unit extends the earlier proved all-order Clausen multiplier reflection and its naive pairing's third-order noncancellation. Neither predecessor proof is recredited. All claims here concern the algebraic shadow/source pair, not the mother LIFT acceptance criterion.

## Exact source definitions

Let p=6m+1 be a prime with m>=1, and let F=F_p. Put a=2m, b=3m, c=4m, and for 0<=j<p define in F[[t]]

\[
M_j(t)=\left(-\frac12\right)^j\frac{j!}{(1-3t)_j}
  \prod_{s\in\{2m,3m,4m\}}\binom{s+t}{j}.
\]

All factorial denominators have indices less than p and are units in F. The exceptional D25 observer at j=m has zero scalar weight (6m+1)=p; its complementary source index is j'=p-1-m=5m.

Set u=M_m(0) and v=[t^3]M_{5m}(t).

## Theorem 1: exceptional regular/triple-carry reciprocal duality

For **every** prime p=6m+1>=7,

\[
\boxed{u=\left(-\frac12\right)^m\frac{(4m)!}{(m!)^4}
  \ne 0,\qquad v=\frac{1}{m^2u}\ne0\pmod p.}
\]

In particular the earlier third-order noncancellation coefficient 4v is exactly 4/(m^2u), with no independently unknown triple-carry constant.

**Proof.** At j=m, the three binomial coefficients telescope:
\(\binom{2m}{m}\binom{3m}{m}\binom{4m}{m}=(4m)!/(m!)^4\).
At j=5m each numerator binomial has one simple t-zero, and its first coefficient for s<5m is
\[
[t]\binom{s+t}{5m}
=(-1)^{5m-s-1}\frac{s!(5m-s-1)!}{(5m)!}.
\]
Introduce A=(m)!, B=(2m)!, C=(3m)!, D=(4m)!, E=(5m)!.
Their product yields
\[
v=\left(-\frac12\right)^{5m}
  \frac{-A B^2 C^2 D}{6m^3E^3}.
\]
Wilson's factorial complements in F are
\(BD=-1,\;C^2=(-1)^{m+1},\;AE=(-1)^{m+1}\).
Substituting gives \(v=(-1/2)^{5m}A^4B/(6m^3)\), while
\(u=(-1/2)^m(-1)/(BA^4)\).
Fermat's little theorem supplies \((-1/2)^{6m}=1\);
finally 6m=-1 in F, giving \(uv=-1/(6m^3)=1/m^2\).
All displayed divisors are nonzero mod p.

## Theorem 2: exact all-order source reconstruction

Define the explicitly known unit rational series
\[
K_m(t)=
\frac{\displaystyle\prod_{s\in\{2m,3m,4m\}}
  \left[\prod_{h=1}^{s}\left(1+\frac th\right)
  \prod_{h=1}^{5m-s-1}\left(1-\frac th\right)\right]}
{\displaystyle\prod_{h=1}^{5m}\left(1-\frac{3t}{h}\right)}
\in 1+tF[[t]].
\]
Then the following is an **identity of formal power series**, not just a finite-order congruence:
\[
\boxed{M_{5m}(t)=\frac{t^3}{m^2u}K_m(t).}
\]
**Proof.** Factor the single zero t from each of the three binomial polynomials in the definition of \(M_{5m}\). The remaining positive and negative numerator factors normalize to the displayed products in K. The factor \(j!/(1-3t)_j\) normalizes to the denominator product. The constant multiplier is exactly v from Theorem 1.

For any 1<=n<p, logarithmic coefficients of K can be recovered with the source-labelled formula
\[
[t^n]\log K_m(t)=\frac1n
\left(3^nH_{5m}^{(n)}+
 (-1)^{n+1}\sum_{s=2m,3m,4m}H_s^{(n)}
 -\sum_{s=2m,3m,4m}H_{5m-s-1}^{(n)}\right),
\]
where \(H_r^{(n)}=\sum_{h=1}^{r}h^{-n}\pmod p\). This yields an explicit triangular recurrence for each jet of the lost complementary source. Only n<p is claimed for the characteristic-p logarithmic coefficient formula, and the exact rational unit formula above needs no such restriction.

## Corollary: four-jet signed repair coefficient

Put \(\alpha_m=2H_m+H_{2m}+11/(6m)\) in F. Wilson/harmonic complement \(H_{p-1-k}=H_k\pmod p\) gives
\(K_m(t)=1+\alpha_m t+O(t^2)\). Hence
\[
[t^4]M_{5m}(t)=\frac{\alpha_m}{m^2u}.
\]
In the **specific two-index signed observer**,
\[
(6m+1)M_m(t)+(30m+1)M_{5m}(-t)
=\frac4{m^2u}t^3-\frac{4\alpha_m}{m^2u}t^4+O(t^5).
\]
Thus the two lost pair-jets through order four are reconstructed exactly from the regular-source scalar u and known p,m; the source labels, regular/triple-carry distinction and true signed weights remain explicit. This is a local observer transfer, not the full Theta_p telescope.

## Exact independent finite-field checks

An independently recurred polynomial computation of M_j(t) in F_p[t]/(t^5) compared the reciprocal, harmonic and signed coefficient formulas for **all 207 primes p<=3000 with p=1 (mod 6): 207/207 PASS**. The recurrence used was

\[
M_{j+1}(t)=M_j(t)
 \frac{-\prod_{s=2m,3m,4m}(s+t-j)}
 {2(j+1)^2(j+1-3t)}.
\]
A standalone Python standard-library verifier was actually executed. Sample exact finite-field data (p,m,u,v,[t^4]M,alpha,4v):

- (7,1,2,4,5,3,2)
- (13,2,6,6,10,6,11)
- (19,3,8,14,7,10,18)
- (373,62,122,251,194,243,258)
- (1009,168,184,66,821,945,264)

Proof and finite checks have distinct roles: the algebraic argument covers every p=1 (mod 6) prime, and finite checks audit the implementation and signs. No native original-class experiment has been substituted.

## Frontier and project linkage

Mother target remains the frozen second-digit LIFT certificate \(\Delta_p-R_p=0\pmod p\) for p=13,19 (mod 24). The original H0/B0, [X]U mod p², Frobenius eta/kappa and independent review obligations remain. In BRC terms the carrier is a labelled signed (regular, triple-carry) pair with its jet observer; K is an exact source-preserving transfer for this pair/horizon, rather than positive-mass collapse.

Next smallest scientific unit: attempt an **actual full-sum finite telescope** using the exact K transfer across all labelled complement pairs, beginning with p=13,19,373 and computing the source-weighted residual through the required p-adic precision. If this pair-only transfer does not close Theta_p, retain the remaining labelled shell(s), rather than promoting a scalar zero to the native LIFT. Keep formal execution/Source result publication separate until a real winning Researcher claim/open is verified.

Research lane configured logical ID: chatgpt-research-hourly-enterprise-math-20260923. Role-bound original session/staging ownership remains unverified in this execution; no new session, claim, open, native checkpoint, Result or review is asserted.


## Follow-on theorem 3: fifth jet and a harmonic-square observer

The exact unit K above yields one additional nontrivial coefficient without constructing any new signed source.

For p=6m+1>=7, put
\[
\beta_m=
\frac{\alpha_m^2}{2}
-5H_m^{(2)}
-\frac{H_{2m}^{(2)}}2+\frac{49}{72m^2}
\quad\text{in }\mathbb F_p.
\]
Then
\[
\boxed{[t^5]M_{5m}(t)=\frac{\beta_m}{m^2u}.}
\]
The exceptional weighted pair has the sharpened five-jet reconstruction
\[
\boxed{
(6m+1)M_m(t)+(30m+1)M_{5m}(-t)
=\frac4{m^2u}\bigl(t^3-\alpha_mt^4+\beta_mt^5\bigr)+O(t^6).
}
\]

**Proof.** The coefficient of t² in log K is exactly
\[
\frac12\left(9H_{5m}^{(2)}-\sum_{s}H_s^{(2)}
-\sum_s H_{5m-s-1}^{(2)}\right).
\]
The involution h→p-h gives
\(H_{p-1-k}^{(2)}=-H_k^{(2)}\), hence
\(H_{5m}^{(2)}=-H_m^{(2)}\),
\(H_{4m}^{(2)}=-H_{2m}^{(2)}\),
and \(H_{3m}^{(2)}=0\).
Using \(H_{r-1}^{(2)}=H_r^{(2)}-r^{-2}\) collapses the coefficient to
\[
-5H_m^{(2)}-\frac{H_{2m}^{(2)}}2+\frac{49}{72m^2}.
\]
Since K=exp(log K) with constant 1 and linear coefficient alpha, its quadratic coefficient is the last expression plus alpha²/2, precisely beta. The signed index j'=5m changes t to -t, and its observer weight is -4 modulo p. This proves the displayed five-jet formula.

**Independent verification extension.** The standalone source verifier was extended to F_p[t]/(t^6) and rerun for all 207 primes p=1 (mod 6) through 3000: **207/207 PASS** for the new fifth-order formula, in addition to the prior third/fourth-order formulas. Exact examples (p, [t³]M, [t⁴]M, [t⁵]M, alpha, beta):
(7,4,5,6,3,5), (13,6,10,12,6,2), (19,14,7,5,10,18),
(373,251,194,158,243,121), (1009,66,821,468,945,374).

This extension is a second substantive scientific unit after the exact reciprocal transfer. The retained source-labelled regular scalar, triple-carry order and harmonic-square data determine the signed partner's first three nonzero jets. The full LIFT certificate and native Source admission remain separate tasks.
