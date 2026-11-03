# D25: quadratic-character boundary unit and terminating fourth-order hypergeometric H2 carrier

Date: 2026-11-03 (Asia/Shanghai). Role: author-side TASK_RESEARCH of the logical lane chatgpt-research-hourly-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; frozen scientific input Enterprise Math c47e13e4aba0e006366f989d6334d443f6333ae3. Status: ALGEBRAICALLY_PROVED / FINITE_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is portable source evidence, not a native claim/checkpoint/Result.

## Selected dependency and novelty

The existing H2 boundary theorem at research_notes/portable_direct/20261103_hourly20_d25_green_boundary_source_transfer.md expresses the high-band observer through L=b_(3r)/p and a finite Green homogeneous product. The independent on-hour D25 lane's research_notes/portable_direct/20261103_onhour_d25_one_sided_primal_dual_laurent_p3.md gives a middle/high reciprocal pair and determinant-one two-carrier transport. These earlier identities are consumed as inputs, not re-proved as new results.

This note identifies L *exactly* as a quadratic character and identifies the entire high-band scalar as a terminating mod-p 4F3 polynomial solution of a fourth-order differential operator. This removes the apparently free high-band boundary unit and gives a new analytic-algebraic target for the signed second-digit cancellation.

## Theorem 1: exact universal H2 incoming unit

Let p=6r+1 >=7 be prime, b_k=(2k)!(3k)!/((k!)^5 216^k) in Z_(p), and let chi=(6/p) in {+1,-1} denote the Legendre symbol. Then

$$
\boxed{L_p:=\frac{b_{3r}}p\equiv-2\chi\pmod p,\qquad L_p^2\equiv4\pmod p.}\tag{1}
$$

In particular, on the frozen D25 target classes, L_p=+2 for p=13 (mod 24), and L_p=-2 for p=19 (mod 24).

**Proof.** Since 6r=p-1 and 9r=p+(3r-1),

$$
\frac{(9r)!}{p}\equiv-(3r-1)!,\qquad(6r)!\equiv-1\pmod p.
$$

Consequently

$$
\frac{b_{3r}}p\equiv
\frac{(3r-1)!}{(3r)!^5\,216^{3r}}
=\frac1{3r(3r)!^4\,216^{3r}}\pmod p.
$$

Writing n=3r=(p-1)/2, Wilson's relation n!^2=(-1)^{n+1} (mod p) implies n!^4=1. Also 3r=-1/2 (mod p), and by Euler's criterion

$$
216^{3r}=216^{(p-1)/2}\equiv(216/p)=(6/p)=\chi\pmod p,
$$

because 216=6^3. Thus L_p=-2/chi=-2chi. The congruence-class signs follow from the quadratic characters of 2 and 3. QED.

## Theorem 2: a finite terminating 4F3 carrier for the high signed band

Set a=3r+1=(p+1)/2 and

$$
H_2(p)=\sum_{k=3r+1}^{4r}(6k+1)b_k.
$$

For 0<=s<=r-1 define in F_p

$$
A_s=\frac{(1)_s(5/6)_s(7/6)_s}{(3/2)_s^3},\quad
F_r(x)=\sum_{s=0}^{r-1}A_s x^s,\quad
\theta=x\frac{d}{dx}.
$$

All displayed denominators are invertible modulo p. Then each *directed original high-band coefficient* and the full signed readout satisfy

$$
\boxed{
\frac{b_{a+s}}{p^2}\equiv\frac{\chi}{9}A_s2^{-s}\pmod p,\qquad
\frac{H_2(p)}{p^2}\equiv
\frac{\chi}{9}\left[(6\theta+4)F_r(x)\right]_{x=1/2}\pmod p.
}\tag{2}
$$

Further, F_r is a polynomial solution over F_p of the *homogeneous* order-four hypergeometric operator

$$
\boxed{
\left[
\theta(\theta+\tfrac12)^3
-x(\theta+1)^2(\theta+\tfrac56)(\theta+\tfrac76)
\right]F_r(x)=0\quad\text{in }\mathbb F_p[x].
}\tag{3}
$$

Equivalently F_r is the terminating reduction of 4F3(1,1,5/6,7/6;3/2,3/2,3/2;x).

**Proof.** The previously verified original coefficient ratio is

$$
\frac{b_{k+1}}{b_k}
=\frac{(2k+1)(3k+1)(3k+2)}{36(k+1)^3}.
$$

Substituting k=a+s-1=(p-1)/2+s yields, for 1<=s<r,

$$
\frac{b_{a+s}}{b_{a+s-1}}\equiv
\frac{s(36s^2-1)}{9(2s+1)^3}
=\frac12\frac{s(s-\tfrac16)(s+\tfrac16)}{(s+\tfrac12)^3}\pmod p.
$$

The previously proved entry ratio b_a/p^2=-L_p/18, combined with Theorem 1, gives b_a/p^2=chi/9. The ratio is precisely A_s/A_(s-1) times 1/2. All high indices have valuation two, so the full first equation follows by induction. Since 6(a+s)+1=3p+4+6s, applying the original signed weight and summing proves the second equation in (2).

For (3), direct coefficient comparison gives for s>=1

$$
s(s+\tfrac12)^3 A_s
=s^2(s-\tfrac16)(s+\tfrac16)A_{s-1}.
$$

This cancels the x^s coefficient of the fourth-order operator for 1<=s<r. The x^0 coefficient vanishes because of the leading theta. The only truncation term is x^r, proportional to r^2(r-1/6)(r+1/6)A_(r-1); but 6r+1=p, so r+1/6=0 in F_p. There are no larger powers. Thus (3) holds identically as a polynomial over F_p, not merely as a finite numerical fit. QED.

## Exact verification and observer scope

The executed standard-library script research_notes/portable_direct/d25_h2_quadratic_character_hypergeometric_20261103.py has verified Git blob SHA-1 5cca21c545a8b4da81542e793c5b6cfb6d1ea4b5 and immutable first published commit 6af673a3fd110787d01b9377e037854c7d7be1e5. It independently calculates p-free factorial units for the **original** b_k, then separately checks the quadratic boundary, each reduced high-band coefficient, signed F_r(1/2) readout, and every coefficient of the homogeneous order-four differential equation. It passed all 148 primes 7<=p<=2000 with p=1 (mod 6). A further independent integer-binomial modulo-p^3 evaluation matched H2/p^2 for p=7,13,19,37,373.

Witnesses (p, chi, L, H2/p^2, (6theta+4)F_r(1/2)): (7,-1,2,5,4); (13,-1,2,10,1); (19,+1,17,9,5); (37,-1,2,20,5); (373,-1,2,266,217). These finite checks support the exact algebraic proof; no native 373 H0/B0/SpectralDNS/Lean run was executed.

**BRC information preservation:** the full source is the original signed factorial b_k with exact index a+s and valuation p^2. The proven carrier map (chi,F_r) reconstructs every high-band *leading unit* and any F_p-linear future readout of those units, including the signed H2; it is an observer-safe compression at that precise modulo-p horizon. For mod-p^2 leading-unit lifts, lower/middle second digit, or source-sensitive Frobenius ports, retain the original factorial and cutoff data. The scalar H2 alone is not declared a lossless carrier for later operations. This is arithmetic formalism under the unchanged P000/ACTIVE Heartbeat-X6 assumptions; the variable x is a scalar generating-function parameter, not a native spatial plane.

## Next discriminating scientific unit

Compare the new polynomial ODE (3) and directional readout (2) against the original low/middle Gauss–Green signed-prefix forcing, holding the actual lower/middle p-adic lifts and the on-hour lane's one-sided Laurent pair fixed. Search for a *p-dependent adjoint/WZ identity* that converts (6theta+4)F_r(1/2) into precisely the negative of the low/middle p^2 carry. Verify all endpoint terms and the signed residues at p=13,19,373. A valid uniform identity would prove the frozen W_(p-1)=p (mod p^3) target; a nonzero residual is to be preserved with its exact provenance.

## Control and delivery boundary

The task publication and canonical taskbook match their exact Source Git blob (publication 1c32f864cd34a376411567bef23d1e37913d2f98, taskbook 53a3ef039325534e3715add837f0eee332289984). The service em_status 0.6.11 on 2026-11-03 reports research_authority_granted=false, executor_binding_configured=false, UPSTREAM_CODE_REVIEW_REQUIRED and quota active_jobs=5/5. Last verified own recovery #6637 found session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94, no local pending/unopened claim/run/uploads; old continuation #6638 ended FAILED due upstream code-review requirement. Support issue #1558 is already open. Do not replay these requests, close the protected session, borrow maintenance identity, or treat neutral staging as accepted progress.

Formal CLAIM/OPEN, Source checkpoint, freeze, review and admission were not performed here. No scheduler or notification change was made.
