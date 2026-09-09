# Complete fixed-k exclusion of the six-point branch block

Researcher: `EM-RB-1EB0B6`. Task: `RS-RB-SIX-BLOCK-COMPLETE-HALF-SECTION-OBSTRUCTION-REPAIR`; publication `TP2-8B673D783D3FBC81E124`; execution `ER-023A3343CE7FA4FA2AEE`; actual Issue 240 CLAIM `5605439472`.

Status: researcher proof and exact integer certificate, awaiting ordinary Driver review. This repairs the six-block exclusion at the frozen differential. It grants no parent closure, Working Truth, Foundation status, or period/homology/absolute-normalization conclusion. The accepted concrete map, its 80 pins, and the 4+2 / 2+2+2 results are unchanged.

## 1. Statement and exact field

Let

\[
 C:t^2=P(R)=R^3-3R,\qquad F=(R+2)t,
\]

with origin O and

\[
 B=O+T_0+T_++T_-+P_++P_-,\quad
 T_r=(r,0),\ r=0,\sqrt3,-\sqrt3,\quad
 P_\pm=(-2,\pm i\sqrt2).
\]

Keep the task's coefficient field and embedding

\[
 K=\mathbb Q(i,3^{1/4},\sqrt2),\quad
 k=-i3^{1/4}(\sqrt6-2),\quad
 \lambda=35+24\sqrt2-20\sqrt3-14\sqrt6.
\]

The symbols are named algebraic-model coordinates; this does not introduce native axes or change P000. Let L be any algebraic extension of K. The exclusion below holds even over an algebraic closure, so no extension or arithmetic constant square class can evade it.

**Theorem.** There is no rational function X of degree six on C whose pole divisor is exactly B and which satisfies the full fixed-k identity

\[
 F(\delta X)^2=\kappa(t+k)^2X(X-1)(X-\lambda),\qquad
 \delta R=t,\quad \delta t=\tfrac32(R^2-1),
 \tag{1}
\]

for a nonzero constant \(\kappa\in L\), independent of R and t. In fact the contradiction is independent of lambda. It therefore excludes every allowed six-point-block correspondence in the task, after the permitted fixed-target V4 translation sends its occupied block to infinity.

This statement uses the prescribed differential, not the erroneous smaller half-section classification. No S4, source-sign, or semilinear quotient is applied. The old raw claim under repair is not a proof premise.

## 2. Complete pole space and the four even-divisor sectors

The smooth cubic C has genus one. At O, R and t have orders -2 and -3. The six functions

\[
 1,R,t,R^2,Rt,R^3
\]

have distinct pole orders and, by \(\ell(6O)=6\), form the full space \(L(6O)\). Thus write without an ansatz restriction

\[
 G=aR^3+bR^2+cR+d+(eR+f)t.\tag{2}
\]

Here a,b,c,d,e,f are scalar coefficients, not differential or field generators. The unique order-six term is aR^3, so exact pole six means \(a\ne0\).

Since \(\operatorname{div}(R+2)=P_++P_--2O\) and \(\operatorname{div}(t)=T_0+T_++T_--3O\),

\[
 \operatorname{div}(F)=B-6O.
\]

Consequently X=G/F has exactly six simple poles B if and only if G has exact pole six at O and is nonzero at the five finite B points. These conditions prevent every numerator/denominator cancellation. They imply \(\deg(X:C\to\mathbb P^1)=6\). A corresponding map D to the elliptic target, if it existed, would also have degree six, by the two degree-two quotient maps. No actual map is constructed here.

For completeness, the allowed even-divisor classification is retained in full. For any nonzero G with even divisor, half its divisor defines a 2-torsion class in Pic^0(C). The four classes are O and \(T_r-O\), because all two-torsion points are split over K. Their representatives are

\[
 \gamma_O=1,\qquad \gamma_{T_r}=R-r,\qquad
 \operatorname{div}(R-r)=2T_r-2O.
\]

Removing the representative makes the half-divisor principal. Over L, a principal rational divisor can be represented by an L-rational function: equivalently apply Galois descent/Hilbert 90 to a function with that divisor. A nonzero constant remains. Hence every sector is exactly

\[
 \alpha_O L(3O)^2\quad\hbox{or}\quad
 \alpha_r(R-r)L(2O+T_r)^2,\qquad \alpha_j\in L^*.
\tag{3}
\]

Constants are not silently absorbed unless the declared field contains the required roots. The bases are

\[
 L(3O)=\langle1,R,t\rangle,\qquad
 L(2O+T_r)=\langle1,R,t/(R-r)\rangle.
\]

Indeed \(t/(R-r)\) has a simple pole at T_r and O, and no other poles; the three displayed sections are independent and the space has dimension three. Conversely, regularity of \((R-r)h^2\) off O and pole bound six are precisely \(\operatorname{ord}_{T_r}h\ge-1\), \(\operatorname{ord}_O h\ge-2\), and nonnegative orders elsewhere. Thus the compensated T_r poles are mandatory members of the classification.

Use scalar parameters A,u,v,z in a single sector, and put

\[
 Q_r=R^2+rR+r^2-3,\quad P=(R-r)Q_r.
\]

The complete expansions are

\[
 \begin{aligned}
 H_O(A,u,v,z)&=A(u+vR+zt)^2,\\
 H_r(A,u,v,z)&=A\{(R-r)(u+vR)^2+2z(u+vR)t+z^2Q_r\}.
 \end{aligned}\tag{4}
\]

In the coefficient order \((R^3,R^2,R,1,Rt,t)\), their vectors are

\[
 \begin{aligned}
 V_O&=A(z^2,v^2,2uv-3z^2,u^2,2vz,2uz),\\
 V_r&=A(v^2,2uv-rv^2+z^2,u^2-2ruv+rz^2,
          -ru^2+(r^2-3)z^2,2vz,2uz).
 \end{aligned}\tag{5}
\]

The exact-pole conditions are A nonzero and z nonzero for O, or A nonzero and v nonzero for T_r. Nonvanishing at the finite B points is imposed, not inferred from evenness. In particular

\[
 H_r(T_r)=Az^2P'(r),\qquad P'(r)=3(r^2-1)\ne0,
\]

so z must also be nonzero in a nontrivial sector. For s different from r, \(H_r(T_s)=A(s-r)(u+vs)^2\). At \(P_\pm\), the half-section value is \(u-2v+z(\pm i\sqrt2)/(-2-r)\); its nonvanishing is required. Here \(-2-r\ne0\), so no artificial pole has been introduced. In the trivial sector require \(u+vr\ne0\) at every T_r and \(u-2v\pm i\sqrt2 z\ne0\) at P_±. These are the exact finite basepoint exclusions.

## 3. Full ordered triple, cover constants, and differential gate

For j=0,1,lambda retain independent sector labels \(\tau_j\), scalar factors \(\alpha_j\ne0\), and half-section parameters. The complete ordered coefficient equations are

\[
 V_{\tau_j}(\alpha_j,u_j,v_j,z_j)
   =(a,b,c,d,e-j,f-2j),\qquad j=0,1,\lambda.\tag{6}
\]

Thus the three members are exactly G, G-F, G-lambda F, with the same leading coefficient a. Formula (6) is a complete equation set for the even-divisor pencil, subject to the pole/nonvanishing conditions above. Its target-special labels remain ordered.

The source double cover additionally requires

\[
 \tau_0+\tau_1+\tau_\lambda=O.\tag{7}
\]

This retains all 16 compatible ordered triples: all O; O and two equal nonzero labels in any position; or the three distinct nonzero labels in any order. The classification is algebraic, not an assignment search. Product representatives are respectively 1, \(\gamma_T^2\), or \(\gamma_{T_0}\gamma_{T_+}\gamma_{T_-}=t^2\). Let h_j be the relevant rational half-section and write \(G(G-F)(G-\lambda F)=\alpha_0\alpha_1\alpha_\lambda H_0^2\), with H_0 the product of the h_j times 1, gamma_T, or t as appropriate.

For a target twist \(Y^2=A_E X(X-1)(X-\lambda)\), arithmetic descent further requires \(A_E\alpha_0\alpha_1\alpha_\lambda=c_H^2\) in the declared field. Then the prospective lift is \(Y=c_H H_0w/F^2\). This arithmetic square condition is separate from (7). It is not asserted merely because the geometric divisor parity works.

The prescribed *unsquared* differential would require

\[
 \frac{dX}{Y}=c_\phi\frac{(t+k)dR}{wt},\quad
 N=2c_\phi c_H(t+k)H_0,\quad \kappa=A_Ec_\phi^2\ne0,
\tag{8}
\]

where

\[
 D=2\delta,\quad DR=2t,\quad Dt=3(R^2-1),\quad
 N=F DG-G DF.
\]

In particular every valid lift must satisfy the full squared identity

\[
 N^2=4\kappa(t+k)^2G(G-F)(G-\lambda F).\tag{9}
\]

The factor four comes from D=2delta and is retained. Clearing F^3 is legitimate in the function field since F is a nonzero function; (9) is then an equality of regular affine functions modulo \(t^2-P\). Neither the cover condition alone nor a solution of (6) is a correspondence without the differential gate. The proof below excludes even the larger full space (2) under necessary consequences of (9); hence it covers every sector and every constant in (3)–(8).

## 4. Necessary equations from O and the three finite two-torsion points

The order-twelve leading term of N is aR^6. The order-twenty-four leading terms of the two sides of (9) are respectively \(a^2R^{12}\) and \(4\kappa a^3R^{12}\). Lower terms involving F, k, or lambda cannot reach that order. Since a is nonzero,

\[
 4\kappa a=1.\tag{10}
\]

Write \(p(R)=aR^3+bR^2+cR+d\). At every T_r, F=0 and \(G(T_r)=p(r)\ne0\). Also

\[
 DF=2P+(R+2)P',\qquad N(T_r)=-p(r)(r+2)P'(r).
\]

Evaluating (9), cancelling the nonzero \(p(r)^2\), and using (10) gives

\[
 k^2p(r)=a(r+2)^2P'(r)^2.\tag{11}
\]

No half-section value is assumed regular before its compensated square is formed. The cancellation here is of the actual nonzero G(T_r), guaranteed by the six simple poles of X.

The exact polynomial remainder is

\[
 (R+2)^2P'(R)^2
 =P(R)(9R^3+36R^2+45R+36)+72R^2+144R+36.
\tag{12}
\]

Since the three roots of P are distinct, (11) and the leading coefficient of p yield the necessary scalar equations

\[
 L_b=k^2b-72a=0,\quad
 L_c=k^2c+(3k^2-144)a=0,\quad
 L_d=k^2d-36a=0.\tag{13}
\]

These equations arise from all G in the complete L(6O), irrespective of square class.

## 5. A necessary coefficient at the three prescribed critical points

Put q=k^2. The three prescribed points are \(Q=(R,-k)\) with \(R^3-3R-q=0\). They are distinct for the frozen k; the exact check is in section 6. At each of them, (9) implies N(Q)^2=0 and hence N(Q)=0. This consequence includes both ordinary target values and all special-target cases with the higher local degree four. No target label or pole case is discarded by assuming it ordinary.

Substitute t=-k into the polynomial N and reduce by the monic cubic \(R^3-3R-k^2\). Its remainder has degree at most two. Since it vanishes at three distinct roots, each coefficient vanishes. In particular its R^2 coefficient is

\[
 C_2=(6k^2-18)a-(k^2+12)b-6c-6d=0.\tag{14}
\]

The existing integer ring independently computes N and this remainder from the full six-coefficient G. The coefficients e and f do contribute to other remainder terms, but do not occur in C_2. They have not been fixed or discarded.

The decisive integer identity is

\[
 k^2C_2+(k^2+12)L_b+6L_c+6L_d
     =6a\,(k^4-12k^2-324).\tag{15}
\]

Equations (13) and (14), characteristic zero, and a nonzero therefore force

\[
 k^4-12k^2-324=0.\tag{16}
\]

Only necessary consequences of the full ODE were used. Finding one inconsistent subset of its mandatory equations is enough to exclude the complete system; no finite parameter sample, smaller ansatz, unresolved saturation, or auxiliary triple is being substituted for an exclusion proof.

## 6. Exact frozen-field contradiction and distinctness

Write u=sqrt(2), s=sqrt(3), so \(u^2=2\), \(s^2=3\). The actual frozen value obeys

\[
 q=k^2=12u-10s,\qquad
 q^2-12q-324=24h,\quad h=11-6u+5s-10us.
\]

There is an integer identity, already reduced only by \(s^2=3\),

\[
 \prod_{\epsilon,\eta\in\{1,-1\}}
 (11-6\epsilon u+5\eta s-10\epsilon\eta us)
 =175876+(u^2-2)(69696u^2+86880).\tag{17}
\]

Thus h is nonzero in every characteristic-zero extension with the frozen relations. The product for the unreduced factor 24h is

\[
 24^4\cdot175876=58351435776\ne0.
\]

This is an exact polynomial norm certificate, without floating approximation or an assumed numerical embedding. It contradicts (16).

For the distinctness used above, \(q(12u+10s)=-12\ne0\). Also

\[
 4-q^2=240us-584,\qquad
 (240us-584)(-240us-584)=-4544\ne0.
\tag{18}
\]

The critical cubic has discriminant \(27(4-q^2)\ne0\), proving its three roots distinct. This also gives q different from ±2 and hence no Q with R=-2; k is nonzero, so the Q avoid the other finite B points. These facts are exact field identities, not positivity approximations.

The contradiction proves the theorem. In particular there is no solution over the algebraic closure, so questions of descending a positive map, choosing its twist/embedding, or verifying its unsquared differential cannot leave an exceptional case. The exact frozen lambda was retained throughout (6), (8), and (9); the inconsistent necessary subset happens not to depend on its value.

## 7. Evidence, checks, and retained scope

`check_complete_obstruction.py` imports the unchanged integer add/multiply/curve-rewrite/2delta/critical-restriction primitives from the task's pinned `check_squareclass_rr.py`. It extends only the formal variable alphabet; it neither executes that checker's main nor replays any assignment enumeration. The scalar extension relation u^2=2 is handled with the explicit ideal certificates in (17)–(18), without an additional reduction engine.

The certificate verifies the full leading-pole identities, complete sector expansions including all three compensated torsion poles, the product of the three nontrivial square-class representatives, the torsion remainder, the critical R^2 coefficient, the integer elimination identity, the frozen-field contradiction and distinctness. Meaningful tamper cases omit each sector's compensating term, change the torsion remainder constant, reverse the critical coefficient's d sign, and falsely set the obstruction norm to zero. Exact nonzero residuals are retained.

The existing BRC natural-division facade normalizes the four unsigned coefficient magnitudes 264,144,120,240 by 24, recording quotient, remainder, and reconstruction traces. Signs, sector labels, poles, and field generators remain separate exact data. Positive branch mass is not used to justify cancellation or field descent. SymPy was used only for exploratory symbolic discovery; the final integer checker needs no SymPy.

The paper's Riemann–Roch/divisor and local-to-global implications justify why the computed identities are necessary for every candidate. The finite checker is not advertised as a proof kernel, a new tool family, or a replacement for Driver review. Source and actual execution pins are in `source-bindings.json`, `runtime/`, and the handoff manifest.

The six-block exclusion is now established for this frozen k, with all four half-section sectors retained. It does not solve any of the remaining 1980 components in the separate 4+2 and 2+2+2 strata, alter the accepted map, or discharge the parent period integer, homology index, or independent absolute-normalization obligations.
