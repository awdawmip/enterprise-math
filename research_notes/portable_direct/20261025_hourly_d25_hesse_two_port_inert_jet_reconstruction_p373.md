# D25/LIFT — two-port Hesse reflection jet and regular local reconstruction

2026-10-25 · TASK_RESEARCH · **portable author theorem / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. Parent task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Research conversation chatgpt-research-hourly-enterprise-math-20260923 remains distinct from maintenance. No native CLAIM, OPEN, Source checkpoint, Result, Driver approval or CM experiment is asserted here.

## Exact inherited mathematical inputs (not re-credited)

For a prime p=6m+1>=13 let n=2m, c_k=(3k)!/(27^k(k!)^3), and A_p(X)=sum_{k=0}^n c_k X^k. The previously proved [source reflection](https://github.com/awdawmip/enterprise-math/blob/238626c2bb75a51b843c3cb3e1af56c60a30e530/research_notes/portable_direct/20261024_hourly_d25_hesse_polynomial_reflection_defect_first_digit_bridge.md) and [half-rank theorem](https://github.com/awdawmip/enterprise-math/blob/b1e773f528ecec65959c46881e698c27331190ab/research_notes/portable_direct/20261024_hourly_d25_hesse_reflection_defect_half_rank_observer_safe_quotient.md) give the exact p-integral identity

$$D_p(X):=\frac{A_p(X)-A_p(1-X)}p=(1-2X)\Phi_p(X(1-X)),$$

with deg(Phi_p)<=m-1 and

$$\mathcal M\Phi_p=C_pF_{2m-1}(Y),\quad \mathcal M=Y(1-4Y)\partial_Y^2+(1-10Y)\partial_Y-\frac{20}{9},$$

where C_p=(p+1)c_{2m}/9; F_0=F_1=1, F_r=F_{r-1}-YF_{r-2}. The [prior global Green inverse](https://github.com/awdawmip/enterprise-math/blob/dadc43f8206cde74c09a760e2990193fce25d673/research_notes/portable_direct/20261024_hourly_d25_hesse_terminal_green_inverse_p373_exception.md) proved the ordinary polynomial even-derivative observer E_p=-Phi_p(1/8)+Phi_p'(1/8)/4 and E_373=0. Those sources did not provide native divided-power [X]U or kappa.

## Theorem 1: exact two-port and unimodular source-jet chart

Work in R=Z_(p)[T]/(T^2-2), sigma(T)=-T and u=(2-T)/4. Exact identities: sigma(u)=1-u; 1-2u=T/2; u(1-u)=1/8. In the ordered free basis (1,T), expand the **original source polynomial**

$$A_p(u)=a_p+b_pT,\qquad A'_p(u)=e_p+d_pT.$$

Then b_p and e_p are divisible by p in Z_(p); define the separate source ports v_p=b_p/p and w_p=e_p/p. Put Phi_0=Phi_p(1/8), Phi_1=Phi'_p(1/8). The following equalities hold **exactly over Z_(p)**, not only in a finite-prime sample:

$$v_p=\Phi_0/4,\qquad w_p=-\Phi_0+\Phi_1/4.$$

The two-port map has matrix

$$\binom{v_p}{w_p}=\begin{pmatrix}1/4&0\\-1&1/4\end{pmatrix}\binom{\Phi_0}{\Phi_1},\qquad\det=1/16\in\mathbf Z_{(p)}^\times.$$

It has the **division-safe inverse**

$$\boxed{\Phi_0=4v_p,\qquad \Phi_1=16v_p+4w_p.}$$

*Proof.* Evaluation of D_p at u gives 2b_pT/p=(T/2)Phi_0, so b_p=pPhi_0/4 by coefficient extraction. Exact differentiation of pD_p=A_p(X)-A_p(1-X) gives pD'_p(u)=A'_p(u)+A'_p(1-u)=2e_p. The factored expression gives D'_p(u)=-2Phi_0+(1-2u)^2Phi_1=-2Phi_0+Phi_1/2. Hence e_p=p(-Phi_0+Phi_1/4). The determinant is a p-unit for p>=13. QED.

Notice that this does not divide by w_p and does not substitute coefficient conjugation for a crystalline Frobenius.

## Theorem 2: full regular local jet from the two ports

Write Y=1/8+z, Phi_p(1/8+z)=sum_{r=0}^{m-1} a_r z^r, and F_{2m-1}(1/8+z)=sum_{r=0}^{m-1}g_r z^r, where explicitly

$$g_r=\sum_{\ell=r}^{m-1}(-1)^\ell\binom{2m-1-\ell}{\ell}\binom{\ell}{r}8^{-(\ell-r)}.$$

The differential operator has exact shifted coefficients

$$Y(1-4Y)=1/16-4z^2,\qquad1-10Y=-1/4-10z.$$

Coefficient comparison, with a_j=0 for j>=m, gives

$$\boxed{\frac{(r+1)(r+2)}{16}a_{r+2}-\frac{r+1}{4}a_{r+1}-\frac{(6r+4)(6r+5)}9a_r=C_pg_r.}$$

Starting with a_0=4v_p and a_1=16v_p+4w_p, this gives, for 0<=r<=m-3,

$$a_{r+2}=\frac{16}{(r+1)(r+2)}\left[C_pg_r+\frac{r+1}4a_{r+1}+\frac{(6r+4)(6r+5)}9a_r\right].$$

Every denominator (r+1)(r+2) is a p-unit in this degree range. This proves, without an inverse of either source port, that **(v_p,w_p), the known exact forcing (C_p,F), and the bounded degree determine the entire ordinary reflected-polynomial local jet modulo p**. The recurrence is an exact polynomial identity before reduction. QED.

The local jet is a typed ordinary source-polynomial carrier; the missing same-class CM/divided-power H0/B0, semilinear Frobenius and [X]U mod p^2 are not thereby constructed.

## New p=373 branch-odd certificate

Directly from original factorial coefficients in (Z/139129Z)[T]/(T^2-2), with u=(2-T)/4, the checker obtains

$$A_{373}(u)\equiv112646+57442T\pmod{139129},$$
$$A'_{373}(u)\equiv0+130607T\pmod{139129}.$$

Consequently v_373=57442/373=154 mod 373, whereas w_373=0. The two-port inverse gives Phi_373(1/8)=243 and Phi'_373(1/8)=226 mod 373; the new local recurrence yields a_2=350. The inherited C_373=40, and the odd derivative B_373=130607 mod373=57, so the first-digit ordinary scalar 3B_373=171 remains nonzero.

**Thus the previously known even second-digit port w_373 vanishes while a *different original source-provenance first-lift port* v_373 is nonzero.** Collapsing both to w loses actual information; the unimodular pair restores the regular local jet. This is a concrete scalar-observer nonfaithfulness witness, **not** a LIFT counterexample or a native CM map. No all-prime nonvanishing statement for v is asserted.

## Exact checks and scientific status

Companion script: [two-port checker](20261025_hourly_d25_hesse_two_port_inert_jet_reconstruction_check.py). It independently rebuilds A_p(u), A'_p(u) mod p^2 from factorials, constructs the global Green coefficients and the new forward local jet, verifies all coefficient recurrences, and checks p=373's raw residue pair. Eight bounded author cases p=13,19,37,43,61,67,211,373 passed; author tests are not independent Driver review, Lean proof or native CM benchmark. The general statements depend on the displayed exact algebra and inherited proved identities, not on extrapolating eight cases.

**BRC/Enterprise-coordinates resolution: COMPOSE_APPLIED.** The two ordered (1,T) branch ports, valuation p, observer direction (value versus derivative), and future differential operation are retained. The single w quotient loses nonzero branch information at p=373; the two-port chart is sufficient only for the declared ordinary polynomial jet, not for unknown native crystalline state. No positive-weight BRC mass is invented and no frozen science pin is changed.

**Next exact task:** obtain Source-authenticated same-class H0/B0/divided-power representative, directed semilinear Frobenius, normalized [X]U mod p^2 and kappa; test a prospective comparison on both (v_p,w_p) and odd derivative d_p, notably at p=373 where division by w is invalid, and then compare to the frozen Delta_p-R_p hard target. Prior native 19-unit checkpoint and contributor history must be preserved; do not repeat the global Green inverse, p<10000 E-zero classification or WZ scans. Parent D25/LIFT OPEN; this GitHub note is portable **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT** evidence.
