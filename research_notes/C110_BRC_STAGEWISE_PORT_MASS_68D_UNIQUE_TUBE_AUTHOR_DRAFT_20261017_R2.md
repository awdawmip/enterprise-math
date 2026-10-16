# C110 — Stagewise port-product Bernstein bounds for the finite positive-weight BRC zero tube

Date: 2026-10-17. **AUTHOR-LEVEL DRAFT / NO CLAIM / NOT DRIVER ADMITTED.**
Global canonical input: `awdawmip/chatgpt-global-knowledge@a6bcf5c1b6ee8ac3ed81f1daebb3b311f672a3e5`.
EM canonical input: `awdawmip/enterprise-math@e13462192b274e15d7c5b3e17fa3841db8c16be4`.
Original C109 full portable research package SHA256: `d0414944f29ff4ed62e3ea17025a5254bf8b9ad7bcf20fbee78fbd5ee6f98386`.
New C110 full portable research package SHA256: `b5141665b36c3beb9ab1d4f2fa8134ed2b326841f1f94c88a0a464aa5488258d`. The full proof, reproducible code, exact 11-arc coefficient certificate and frozen parents are in the conversation portable package, **not** in this GitHub note. The uploaded package has not been published into Source.

## Scope and new theorem
Fixed 48-bit core c2=c24=1 and all other bits zero; inherited 156 integer edges, 142 GF(2) faces, 68 weak couplings, eleven parameter arcs (shared C104 arc plus five exceptional C105 pairs × two arcs); t in [0,1], u in [2/5,99/100]. All results are for the **classical finite positive-weight BRC auxiliary model**, not the native P000 6D Cell substrate. Define `F=AD-BC` and for all 68 weak faces
```
r_f(t,u,z) = eps + (1-eps)*r0_f(t,u) + z_f
eps=13/50000000 = 2.6e-7; delta=1/4000000 = 2.5e-7; |z_f|<=delta.
```
The 68 face characters may be correlated; no probabilistic independence is assumed.

**Author-level exact theorem (C110):** for every inherited arc, all t and z, all 68 weak couplings remain strictly in (0,1), `F(t,2/5,z)>98`, `F(t,99/100,z)<-27`, `partial_u F(t,u,z)<-15` throughout the closed parameter interval. Thus a unique nondegenerate root `u*(t,z)` exists in (2/5,99/100), with `|u*-u0*|<1/600`. Inherited exact four-moment junctions keep the five-branch connected zero-star under the common z perturbation; only a local relatively open smooth 67D patch is claimed, **not global connectedness**.

## New proof component: joint-port mass rather than global total mass
Let four nonnegative port masses be a,b,c,d. Walsh inversion yields
```
F=4(ad-bc)
Q0=4(ad+bc)=(A^2+D^2-B^2-C^2)/2.
```
C109 bounded `Q0<=M^2` with `M=12609529/131072`. C110 reconstructs `Q0(t,u)` **from all four exact Fourier polynomials per arc** and transforms each to rational Bernstein form. Across eleven arcs, 753 Bernstein coefficients are checked; each arc has a separate `U_s=max Bernstein(Q0)`, with `max_s U_s=3840303675216281/858993459200<4471`. The same exact polynomials reconstruct the determinant and its u-derivative (628 checked derivative Bernstein coefficients), producing per-arc `L_s=min Bernstein(-partial_u F0)>281`; matching the frozen C104/C105 four-moment certificates exactly.

## Error lemma, all rational
From C109's verified per-state weak-face support (at most 3 with r0<=99/100, at most 9 others <=9/10, 56 zeros), put
```
aH=eps+100*delta; aM=eps+10*delta; aZ=eps+delta;
S=3*aH+9*aM+56*aZ; rho=S/(1-S);
beta=3*max(2*eps+delta, 10000*delta/(1-aH)).
```
Statewise spin-factor ratios and u-score differences imply for each port `|p_z-p0|<=rho*p0` and `|p_z'-p0'|<=[300*rho+beta*(1+rho)]p0`. Expanding products **before** taking maxima gives the stagewise exact inequalities:
```
|Fz-F0| <= U_s*(2*rho+rho^2)
|Fz'-F0'| <= 2*U_s*[300*rho*(2+rho)+beta*(1+rho)^2].
```
For each of eleven arcs, exact Fraction assertions check `L_s - 2U_s[300rho(2+rho)+beta(1+rho)^2] > 15`, `U_s*(2rho+rho^2)<6/5`, and `U_s*(2rho+rho^2)/L_s<1/600`. Maximum observed rational upper values displayed in decimal are 1.1552743911 (F error), 0.00145841735 (root drift); minimum negative-derivative margin 15.8193414949. These decimals are NOT decision inputs.

## Reproducibility, lineage, next question
Independent clean extraction of C110 runs the original C109 verifier, itself rechecking C108/C105 exact GF(2) / independent rebuilt integer graph Walsh / 846 Bernstein sign coefficients, and then reconstructs the new 753 Q coefficients, 628 derivative coefficients and stagewise inequalities using standard-library Python Fractions. All tests passed locally with frozen SHA256 manifest. This is **author two-route inherited verification**, not an independent Driver judgment or original X6 physical experiment.

Radius comparisons (centers differ; not literal set inclusion): C110/C106=2500/3 (~833.33); C110/C107=25/11 (~2.27); C110/C109=125/21 (~5.95). The C107 existence-only bound is now surpassed by a separate **uniqueness + transversality** result.

Next research unit C111: improve conditional port scores and subdivided Bernstein error certificates to test delta >=3e-7, or find an exact interior multiple-root counterexample. Any native six-dimensional Cell transfer still requires a separately verified provenance-preserving native-state/readout bridge.

**Persistence/authority:** This is an author draft on an isolated branch, not main. Native task inventory was unavailable (`CONTROL_QUOTA`); authenticated execution session registration was denied (`STATIC_READONLY_SCOPE_DENIED`). No owner was verified, no CLAIM was created, no canonical Source Result published, and no Driver admission claimed.
