# D25 fixed-x lift: exact coordinate bridge and vanishing of its divided-layer correction

Status: LOCAL_ALGEBRAIC_INCREMENT / AUTHOR_PROOF / NOT_YET_REVIEWED / LIFT_OPEN.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7.
Author: EM-ENTERPRISE-1C7646. Session MCP-078376aa00ee4999935d36d5b9766cd6; RA-5F93C76E1A4CA9FBAB96B655; claim MCP-ca0c9c185e519dde136fee48; ER-B895F9046546FFCD3131; open cm24d25-open-20261008-r1; run RUN-080b5da0bfb40a62a7aa38a5 generation 1.

## Scope and provenance

The predecessor D25 note is consumed at Source 1bc8516493d29356676b8bd0f223dae617a9d1dd, path research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-70a0fec6896849ac81484f0e00b3f0dd/252cb7c4f5df0ea1472d/d25_gauss_manin_representative_gauge_20260924.md, SHA256 24a0df3b881495d2f70e1546043c375288273b1ac1b71238e77274e64d43cab1. Own artifact request cm24d25-artifact-d25-20261008-r1 (#3146) verified complete bytes. This is inherited author-reported material, not newly accepted mathematics. Its highest checkpoint SHA256 is d8d5f568c80a6901789346f4938e6cfe67c30bf1990c4b8e6817cfb28fd0b077.

The fixed-x versus fixed-xi candidate route and the instruction to audit the full divided-power/Frobenius premise were proposed by Owner through the line Driver. That guidance is disclosed as source exposure and contribution, not independent review. The present derivation and checker are this Researcher's work. No previous contributor identity is adopted; the predecessor authors remain EM-DIRECT-A71FA7, EM-DIRECT-B9BCE8, EM-DIRECT-C4D02C, EM-DIRECT-E267A2.

External source: Chisholm, Deines, Long, Nebe, Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), DOI 10.3390/math1010009. Publisher PDF https://www.mdpi.com/2227-7390/1/1/9/pdf was fetched on 2026-10-08; SHA256 3adacbce06377f7690237de150f5a48a0411d004703f5219f28c5691db6989e2. Relevant text is Section 3.4 (pp.17–19), Lemma 12 (pp.20–21), the two formal cohomology quotients (p.25), Proposition 16 (pp.25–26), and the proof of Theorems 1–2 (pp.27–28). The PDF does not explicitly state that its de Rham symbol partial_lambda selects the fixed-x rational representative below.

P000 binding: native space remains the full six-dimensional discrete Cell torsor X6, with no native plane. Time is separately typed and is unnecessary for this static calculation. The elliptic curve here is an external algebraic observer, not native spatial ontology. The readout bridge takes a declared X6 relational state together with its retained arithmetic labels (prime, residue class, branch t,s, valuation, local-coordinate choice, companion normalization and provenance) to this elliptic observer's coefficient data. Only the coefficient readouts and operations explicitly declared below are studied; no full-X6 dynamics or lossless reconstruction is claimed. Unspecified native coordinates and joint relations are not erased.

## 1. Fixed-x lift and exact coordinate change

Work over an unramified p-adic coefficient ring A containing s with s^2=2, p>3. At the target lambda=1/2 put t=(2-s)/4 and a=t/27. Use

    E: y^2+xy+ay=x^3, D=2y+x+a, omega=dx/D, xi=-x/y.

All differentiations first occur in the smooth family with a=t/27; evaluation at the target occurs afterward. Since lambda=4t(1-t), dt/dlambda=s/4 at this branch. The fixed-x lift of partial_t is

    delta_x x=0, delta_x y=-y/(27D).

It gives the explicit rational differential

    G_x := partial_lambda omega |_x = -s(x+a) dx/(108 D^3).                (1)

This is an actual algebraic representative of the Gauss–Manin derivative class. It is only a candidate for the particular representative used in the source's normalized companion; no such source identification is asserted.

From implicit differentiation on E,

    (partial_t xi)|x = xi/(27D),
    (partial_x xi)|t = (y+x+2a)/(Dy),
    (partial_t x)|xi = x/[27(y+x+2a)].

The difference between the fixed-xi and fixed-x horizontal lifts is a vertical derivation V. Its contraction with omega is x/[27D(y+x+2a)]. Cartan's formula for the relative one-form therefore yields

    G_xi = G_x + d_rel Q_lambda,
    Q_lambda = s x/[108 D(y+x+2a)].                                    (2)

Here G_xi=(s/4)(partial_t H(xi,t)) dxi, where omega=H dxi. The sign in (2) is fixed by the displayed chain rule, not by convention.

For a direct integral expansion set w=-1/y=xi^3 V(xi), where

    V=1+xi V+a xi^3 V^2, V(0)=1,
    S=1-xi-2a xi^3 V, S^2=(1-xi)^2-4a xi^3,
    H=1/S,
    U=xi-2+a xi^3 V, W=xi-1+2a xi^3 V.

Then

    Q_lambda = s xi^4 V/(108 U W)
             = s xi^4/[27 S(1-xi+S)(3-xi+S)].                          (3)

The formal branch has S(0)=1. All three denominators are units for p>3, so Q_lambda belongs to A[[xi]], with Q_lambda=s xi^4/216+O(xi^5). Both derivative representatives have zero leading constant coefficient. Direct substitution also gives

    G_x/dxi = -s xi^4 V(1+a xi^2 V)/(108 S U^2).                        (4)

Define J_x=[xi^(p-1)]G_x/dxi, J_xi=[xi^(p-1)]G_xi/dxi and q_p=[xi^p]Q_lambda. Equation (2) is the exact identity

    J_x = J_xi - p q_p.                                                (5)

## 2. The coordinate correction vanishes at the D25 observer

**Lemma.** For every prime p>3 at which this family has good reduction, q_p is in pA. Consequently J_x=J_xi modulo p^2. In particular this holds for all target primes p=13 or 19 modulo 24.

**Proof.** Reduce the identities modulo p and write

    f=xi^(-1)=-y/x, P(x)=D^2=4x^3+(x+a)^2.

Since H dxi=dx/D and Q_lambda=-(s/108) xi H/D, coefficient extraction is the algebraic residue

    q_p=-(s/108) Res_O(f^p dx/P(x)) in A/pA.                           (6)

Let iota be elliptic inversion, iota(x,y)=(x,-x-a-y). It fixes O, preserves x and dx/P, and satisfies

    f+iota^*f=1+a/x.

Residue is invariant under this local automorphism. In characteristic p the Frobenius identity is exact, hence

    2 Res_O(f^p dx/P)
      =Res_O((f^p+(iota^*f)^p)dx/P)
      =Res_O((1+a^p/x^p)dx/P).                                        (7)

The last differential is the pullback from the x projective line. At x=infinity it is O(x^(-3))dx, so its residue there is zero. The map x:E->P^1 has ramification degree 2 at O; equivalently x=xi^(-2)(1+O(xi)). Pullback therefore multiplies this zero residue by 2, still zero. Because p is odd, (7) gives zero for (6). This proves q_p=0 modulo p and then (5) proves the assertion. No finite regression enters the proof.

For the target branch the discriminant is a^3(1-27a)=t^3(1-t)/27^3; t(1-t)=1/8. Thus for p>3 all factors needed for smoothness are units. The proof applies in both residue classes, over the unramified quadratic coefficient ring when needed. It preserves the chosen s branch; no collapse of s or residue identity is used. QED.

The residue proof concerns a change between two coordinate lifts. It is not an ASD/Katz recurrence, an evaluation-adjoint/SBP replay, or a new theorem about the actual normalized CM companion.

## 3. Consequence for the saved scalar interface

Keep exactly the same p-adic unit c_p, including its required lift modulo p^2, in both candidate companions. No normalization is defined by forcing the desired product. The saved alphaHat formula is consumed, not re-derived:

    alphaHat_p = GThat_p-D_p-E_p+p M_p modulo p^2.

Whenever the chosen normalization makes c_p alphaHat_p J_xi=1 modulo p, define the candidate divided scalars at precision p^2 by

    L_xi=(c_p alphaHat_p J_xi-1)/p modulo p,
    L_x =(c_p alphaHat_p J_x -1)/p modulo p.

Then (5) gives L_x-L_xi=-c_0 alpha_0 q_p=0 modulo p by the lemma. Thus replacing the fixed-xi derivative by the natural fixed-x rational derivative cannot supply the missing D25 digit. Substituting alphaHat leaves the same scalar

    ((c_p (GThat_p-D_p-E_p+p M_p) J_xi)-1)/p modulo p.

This is an equality of the two candidate observers, not an evaluation of that scalar. In the inherited TRAW=alpha_0^2+Lcomp and K=tau_p-alpha_0^2-Lcomp interfaces, the coordinate change supplies zero additional term. Exact c_p, the quartic factor tau_p=(2^((p-1)/2)+1)/p, and C_p=beta_p-alpha_p remain unresolved/preserved as before. The predecessor first-digit identity 6 beta_p J_p^F=1 is consumed; neither c_p=6 nor C_p=0 is asserted.

No new bridge from this scalar to the cutoff/endpoint R_p has been proved. LIFT/JT2 remains open.

## 4. What Source must still identify: the divided-power lift

The source's p.25 distinguishes the ordinary formal quotient, whose denominator consists of integral primitives A[[xi]], from its divided-power quotient, whose denominator is pA[[xi]] (primitives have zero constant term). An exact derivative dF with F integral is invisible to the former but need not be invisible to the latter. In particular F=eta xi^p changes J by p eta, but F is generally not in pA[[xi]]. Keeping ordinary de Rham class and leading coefficient therefore does **not** establish that the same divided-power class, CM eigenlift, or full Frobenius/commutation premise of Proposition 16 is preserved.

The source's Proposition 16 assumes a Frobenius lift under the chosen uniformizer commuting with R on the divided-power cohomology; the companion classes and their R-eigenfunction status also belong to that setup. This note does not verify that arbitrary exact perturbations continue to satisfy all of those premises. The inherited gauge argument remains only its explicitly weaker information boundary, never a no-go after adding full lifted CM/Frobenius data.

There is a precise source datum to request rather than another unspecified representative search. Once an exact source normalization c_p and a normalized candidate primitive B_x for omega+c_p G_x are fixed, an actual normalized companion with the same ordinary integral class differs by dF, with F in A[[xi]], F(0)=0. Its lift to the divided-power quotient differs by

    [F] in A[[xi]]/pA[[xi]].

For the present observer, the only needed image of this lift difference is

    kappa_p=[xi^p]F modulo p.                                          (8)

Indeed b_actual(p-1)-b_x(p-1)=p kappa_p modulo p^2, hence the divided coefficient-product digit changes by alpha_0 kappa_p. This follows by coefficient differentiation and a(p-1)=p alphaHat_p, not by imposing a target congruence. Since alpha_0 is a unit at the inherited normalization, (8) is necessary and sufficient **for this observer once c_p and the ordinary class are fixed**. Other coefficients of F may still be required to satisfy the full lifted CM/Frobenius conditions; the observer quotient grants no permission to erase those conditions.

This identifies the missing data as a specific coefficient of the *integral divided-power lift difference*, subject to actual CM/Frobenius compatibility, not an arbitrary ordinary exact-form gauge. The fixed-x/fixed-xi difference computed here has F=c_p Q_lambda and kappa_p=0, so that tempting candidate supplies none of the required data. The actual source c_p modulo p^2 and the actual compatible lift have not been identified in the cited paragraphs. Specifying only a de Rham eigenline, only a residue c_0, or enforcing c_p alphaHat_p J_p=1 modulo p^2 would not repair this gap.

## 5. Verification and disposition

The accompanying checker uses the predecessor Q2 exact modular arithmetic class (source hash 29e111f86909af821114d33a1c80f7a93d7b55ab5c9d3bd7cd2fedfd0e9d5f19). It checks four curve/chain-rule identities symbolically and independently computes the formal series of (3) and (4) for p=13,19,37,43. It confirms (5), the leading coefficient s/216, and q_p=0 modulo p. The four computations are regression only; the lemma's all-prime scope comes from (6)–(7). No old 166-prime main or raw-H p^3 proof is rerun.

New completed unit: explicit fixed-x representative, exact primitive connecting it to fixed-xi, and an all-target zero effect on the D25 divided product observer; precise distinction between ordinary and divided-power lift premises.

Not completed: actual normalized CM companion and exact c_p identification, compatible divided-power lift coefficient kappa_p, evaluation of Lcomp_p, its cutoff/endpoint R_p bridge, and LIFT/JT2. This is not a Result, not SATISFIED, not independent review, and not Task or parent closure.

Do not repeat: the fixed-x versus fixed-xi coordinate-lift route as a source of a nonzero D25 correction; its correction is exactly p-divisible and its effect is zero. Preserve the prior no-repeat list, raw-H/alphaHat frontier, C_p, tau_p, source authors, and the full lifted cohomology premise.

Recommended return: checkpoint this bounded increment and release for Driver integration. A later step requires an explicitly source-bound normalized divided-power CM lift or its coefficient (8), together with exact c_p, before claiming a representative identification; this report does not publish or dispatch a new task.
