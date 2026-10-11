# Hesse / full-level-3 normalization: independent readcheck

Status: **PASS for the base-coordinate formulas, with explicit full-level marking.** Betina–Lecouturier's (H) is not the naked Hesse parameter. Their paper does not state the proposed Hesse (j)-formula. A precise coordinate bridge is nevertheless available from the primary formulas below. This is a base-curve coordinate result, not an identification of the divided normal digit (G_p), a period pairing, or the UR-FRICKE normalization.

Work is local/read-only except downloading exact, already identified primary URLs. Provider queries: 0. No identity, claim, open, native mutation, Source mutation, or GK write. No historical Clausen/Sun/Shvets/77-prime/CM0/SIMPLE/JT2 unit was repeated. Algebraic geometry here is an external typed observer; no claim about native low-dimensional ontology is made.

## 1. Primary formulas and the marking that must be retained

[Betina–Lecouturier, arXiv:1611.01044v3, Appendix 7.2.1, equation (7), PDF p. 20](https://arxiv.org/html/1611.01044v3#S7.SS2.SSS1) defines

\[
w=\frac{z}{1-z},\qquad H(z)=\left(\frac{\eta(w/3)}{\eta(3w)}\right)^3.
\]

It identifies (H) as a Hauptmodul on the base full-level-3 curve. The complete original TeX, lines 620–662, was read; no Hesse equation or explicit rational (j(H)) is supplied there. The source's higher-curve period assertion at the end of 7.2 is therefore not a source statement of the candidate Hesse (j)-formula.

[Maier, arXiv:math/0611041v4, §4, equations (4.4)–(4.5)](https://arxiv.org/html/math/0611041v4#S4.E4) uses the Hesse–Dixon equation (x^3+y^3+1-(\gamma+3)xy=0) and the marking

\[
\gamma(w)=t_9(w/3)=27\frac{\eta(3w)^3}{\eta(w/3)^3}=\frac{27}{H(z)}.
\]

Thus Maier's particular Hesse parameter is (h_M=(\gamma+3)/3=1+9/H). The candidate convention is the different marking

\[
h_B=\frac{H+3}{3},\qquad h_M=\frac{h_B+2}{h_B-1}.
\]

The last equation is a nontrivial Möbius transformation of the Hesse base. Both markings have the same (j); they must not be substituted for one another in a quotient or derivative without transporting the selected 3-torsion basis/cyclic subgroup. Also (w=z/(1-z)) is a modular argument change. Although (j(w)=j(z)), this alone does not identify the chosen (Γ_0(3)) coordinate at (w) with the coordinate at (z).

## 2. Exact Hesse (j) and source comparison

For (x^3+y^3+z^3-3hxyz=0), characteristic different from 2 and 3, choose the flex (O=(1:-1:0)). Set (u=z, v=x-y, w_0=x+y+hz). The cubic becomes

\[
3w_0v^2+w_0^3-6hu w_0^2+9h^2u^2w_0+4(1-h^3)u^3=0.
\]

On (w_0=1), scale (X_0=4(h^3-1)u/3, Y_0=4(h^3-1)v/3). This is a Weierstrass model with

\[
a_2=-3h^2,\quad a_4=\frac{8h(h^3-1)}3,\quad
a_6=-\frac{16(h^3-1)^2}{27}.
\]

Exact invariant calculation gives

\[
c_4=16h(h^3+8),\quad c_6=-64(h^6-20h^3-8),\quad
\Delta=\frac{4096}{27}(h^3-1)^3,
\]

and consequently

\[
j(h)=\frac{27h^3(h^3+8)^3}{(h^3-1)^3}.
\]

This matches [Artebani–Dolgachev, arXiv:math/0611590v3, §2, equations (2), (6)–(8)](https://arxiv.org/html/math/0611590v3#S2), after (λ=-3h, u_0=1, u_1=-h/2), and the standard factor 1728 in the affine (j)-invariant. That source presents its projective (j)-map up to a scalar; this factor must not be dropped. The script checks the comparison exactly.

Define

\[
R(H)=\frac{(H+3)^3\big((H+3)^3+216\big)^3}{\big((H+3)^3-27\big)^3}.
\]

Maier's first formula in (4.5) is exactly (R(\gamma)), using the factorizations ((\gamma+3)^3+216=(\gamma+9)(\gamma^2+27)) and ((\gamma+3)^3-27=\gamma(\gamma^2+9\gamma+27)). Direct rational simplification gives (R(27/H)=R(H)). Therefore the source formulas prove (j(z)=j(w)=R(H(z))=j(h_B)), as well as (j(h_M)=j(h_B)). This is the source-based proof; it does not depend on numerical coincidence.

## 3. The eta coordinate and the proposed Fricke quotient

Maier's **small** canonical coordinate is (t_3(w)=729(\eta(3w)/\eta(w))^{12}), not the candidate's reciprocal eta coordinate. His Table 6, row (NM=9, M=3), second covering, applied at (w/3), gives (t_3(w)=\gamma^3/(\gamma^2+9\gamma+27)). Substitute (γ=27/H):

\[
t_3(w)=\frac{729}{H(H^2+9H+27)},\qquad
T:=\left(\frac{\eta(w)}{\eta(3w)}\right)^{12}
=H(H^2+9H+27)=27(h_B^3-1).
\]

Table 2 and §3.1 give (t_3|W_3=729/t_3), so (T|W_3=729/T). For the **candidate normalization** (X=T+54+729/T), exact algebra yields

\[
X=\frac{27h_B^6}{h_B^3-1}
=\frac{(H+3)^6}{(H+3)^3-27},\qquad
\frac{dX}{dh_B}=\frac{81h_B^5(h_B^3-2)}{(h_B^3-1)^2}.
\]

This verifies Fricke invariance and the stated rational formula. The additive constant 54 is the chosen candidate normalization; it is not presented here as a separate formula quoted from Maier. Identifying this (X) with a previously frozen Sakai coordinate must keep that earlier normalization/provenance.

At (X=216), (h_B^3=4\pm2\sqrt2). The two values are exchanged by (v\mapsto v/(v-1)), (v=h_B^3). The full degree-6 fibre in (H) is

\[
(H+3)^6-216((H+3)^3-27)=0,
\]

with discriminant (2^{21}3^{36}). Thus all six geometric lifts are distinct for every prime (p\ge5), and the quotient is unramified there; the derivative is nonzero on every such lift. This retains six full-level branches rather than erasing them into one first-normal value. The derivative relative to (H) has the additional factor (dh_B/dH=1/3).

## 4. Additional exact series/divisor certificate and its conditions

The script also expands (r=e^{2\pi iw/3}), (H=r^{-1}\prod_{n\ge1}(1-r^n)^3/(1-r^{9n})^3), in integers through (r^{72}). After clearing Laurent denominators, all 73 coefficients of the candidate (j) minus (E_4^3/\Delta) vanish. By itself this is only a finite check.

The global certificate uses explicit additional facts: (H) is a coordinate on the compact connected base (X(3)\cong\mathbf P^1); ([\mathrm{PSL}_2(\mathbf Z):\overline{\Gamma(3)}]=|\mathrm{PSL}_2(\mathbf F_3)|=12); hence the modular (j) has total pole degree 12. The candidate (R(H)) also has degree 12. Their difference has total pole degree at most 24. The exact series check proves a zero of order at least 70 at the (r)-cusp. A nonzero meromorphic function on the compact base cannot have such a zero with total pole degree at most 24. Therefore equality is global. This independently certifies the source-based equality; it is not a new finite-prime regression.

The eta (T) series also agrees exactly through this order. Its global equality is already supplied by Maier's Table 2/Table 6 covering formulas above, so no unstated all-orders inference from the finite series is used.

## 5. Limits for the first-normal continuation

Betina's original TeX says the base (H) has a simple pole at the level-3 cusp (line 635), but separately says its pullback to (\Gamma_0(p)\cap\Gamma(3)) has a double pole at (c') (line 642; PDF p. 20). These occur on different curves. No cusp ramification reconciliation or period normalization is inferred here. The base-coordinate calculation does not use the second pole-order claim.

The completed unit supplies a marked, unramified base-coordinate quotient at (X=216). It leaves unresolved the exact relation of the level-3 pairing/divided normal coordinate to (G_p=g_p/p), including the operation, selected level structure, normal parameter, and multiplier in UR-FRICKE. Parent mathematical completion is not claimed.

## 6. Complete-byte primary evidence

All three Betina URLs were exact-version, direct reads with HTTP 200; no search query was used. The source endpoint is a gzip-compressed single TeX file, not a tar archive. Its decompressed bytes and the PDF rendering agree on equation (7).

| Source | Complete bytes | SHA-256 |
| --- | ---: | --- |
| Betina v3 HTML | 636796 | `fa59f385dc981094a5bfa4c7f547fff05d2dec0cf5f4a72390ca8b6c2594cc83` |
| Betina v3 PDF | 258570 | `03117b4ce827afdbd61c21464c9a40b693f330a79e687590d6f4ec26ad1705fe` |
| Betina v3 compressed source | 17939 | `56262f3e181e7332261ecf39a3928a90270eb55e8c2d7a3013a26a179b4e8b58` |
| Betina v3 decompressed TeX | 63224 | `81835e700f2cec78a89cd9e4b81b155f7b086035521f2efe2cdba19d75a0242b` |
| Maier v4 HTML, independently read from parent's exact download | 2498309 | `a8e2141a2786658147e79d0034544902d17049d2e586281473099d6ff88853cf` |
| Artebani–Dolgachev v3 HTML, independently read from parent's exact download | 775460 | `4bb4d4bb247aa21dfc079756999d77022cbb0159bf47072b9eed6f0444eab3f7` |

Machine-readable claims, source byte pins, and boundaries: `HESSE_EXACT_CHECK_RESULT.json`. Reproducer: `check_hesse_normalization.py`, using exact integer truncated series and symbolic rational identities. Verification: **PASS**. These local paths are recorded in the evidence manifest; no native Result or publication is implied.
