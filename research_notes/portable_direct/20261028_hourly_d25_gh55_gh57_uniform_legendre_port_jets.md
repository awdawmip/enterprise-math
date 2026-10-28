# D25/LIFT GH-55–GH-57 — Uniform Legendre F/G transport and typed second-jet equations

2026-10-28 Asia/Hong_Kong. TASK_RESEARCH author-side proof, **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**. No native Source CLAIM, OPEN, checkpoint, Result, Driver review, or project mathematical acceptance is asserted.

Mother Objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN); Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (UNCHANGED). Stable independent Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923; not the maintenance conversation.

## Hypotheses and prior author evidence

Let \(p=8m+3\ge11\) be prime, \(m\ge1\), and \(k=\mathbb F_p\). Use original GH-22 labeled ports:
\[
 F_m(z)=\sum_{r=0}^m\frac{(-m)_r^2}{(2m+2)_r\,r!}z^r,\quad
 G_m(z)=(16\theta+5)F_m(z),\quad
 \theta=z\frac{d}{dz},\quad D_m=\binom{3m+1}{m}\in k^\times.
\]
GH-28 previously established a Legendre relationship at \(z=9\); GH-32 established a conditional-free all-target-prime F-port CM dichotomy, NOT the distinct G-port disappearance. Neither source implies a global polynomial identity without proof. The exact predecessor evidence is in GH-22/GH-23, GH-27/GH-28, GH-32/GH-33, and GH-53/GH-54 files under research_notes/portable_direct/.

## GH-55 — whole-polynomial Legendre identity (PROVED)

Set \(n=2m\). In \(\mathbb Z[1/2][z]\) introduce the explicit polynomial
\[
 \mathcal L_m(z)=z^mP_{2m}\left(\sqrt{\frac{z-1}{z}}\right)
 =\sum_{j=0}^m\binom{2m}{2j}\binom{2j}{j}
       \left(-\frac14\right)^j(z-1)^{m-j}. \tag{55.1}
\]
The formal square-root notation is only a compact expression of an EVEN polynomial; use the right-hand side at \(z=0\). All \(p\)-reductions are well-typed.

**Theorem GH-55.** Over the **entire** polynomial ring \(k[z]\),
\[
 \boxed{D_mF_m(z)=\mathcal L_m(z).} \tag{55.2}
\]

**Proof.** The Legendre differential equation
\((1-t^2)P_n''-2tP_n'+n(n+1)P_n=0\),
the rational change \(t^2=1-z^{-1}\), and gauge \(z^m\) give the exact transformed equation
\[
 z(1-z)\mathcal L_m''+
 \left[\frac12-2m-(1-2m)z\right]\mathcal L_m'-m^2\mathcal L_m=0. \tag{55.3}
\]
This follows by the chain rule over \(\mathbb Q(z,t)\) and, after clearing the apparent chart singularity, is a polynomial identity. Since \(8m+3=p\), one has \(\frac12-2m=2m+2\) in \(k\). Thus (55.3) is the Gauss equation for the hypergeometric polynomial \(F_m\):
\[
 z(1-z)F_m''+[2m+2-(1-2m)z]F_m'-m^2F_m=0.
\]
The coefficient recurrence for degrees \(0\le r<m\) has denominator \((r+1)(r+2m+2)\), which is a unit modulo \(p\). Hence polynomial solutions of degree \(\le m\) are unique up to their constant coefficient. Both displayed solutions are **monic** after multiplying \(F_m\) by \(D_m\): the leading coefficient of \(F_m\) is \(D_m^{-1}\), whereas the leading coefficient of \(\mathcal L_m\) is \(P_{2m}(1)=1\). They coincide. QED.

Let \(t\) be any quadratic-extension element satisfying \(t^2=8/9\). Differentiating the GLOBAL identity, not merely GH-28's special-value equality, gives
\[
 (16\theta+5)\mathcal L_m(z)
 =z^m\left[(16m+5)P_{2m}(t)
             +\frac8{tz}P_{2m}'(t)\right]
 \quad(t^2=1-z^{-1}).
\]
At \(z=9\), use \(16m+5=2p-1=-1\) and \(8/(9t)=t\):
\[
 \boxed{D_mF_m(9)=9^mP_n(t),\qquad
        D_mG_m(9)=9^m[tP_n'(t)-P_n(t)].} \tag{55.4}
\]
Both right-hand expressions lie in \(k\), since \(n\) is even and \(tP_n'(t)\) is even. **The open class \(p\equiv11\bmod24\) G-port vanishing problem is reduced to the exact derivative condition \(tP_n'(t)=P_n(t)\), not thereby proved for all primes.**

## GH-56 — first Gauss/Picard–Fuchs jet (PROVED)

With \(m=-3/8\pmod p\), the Gauss equation becomes
\[
 z(1-z)F_m''+(5/4-7z/4)F_m'-9F_m/64=0.
\]
At \(z=9\), whose \(z(1-z)=-72\) is a \(p\)-unit, this gives
\[
 F_m''(9)=-\frac{29}{144}F_m'(9)-\frac1{512}F_m(9).
\]
Differentiate \(G_m=16zF_m'+5F_m\) to obtain
\[
 G_m'(9)=-\frac1{18}G_m(9)-\frac1{288}F_m(9),\qquad
 \boxed{288G_m'(9)+16G_m(9)+F_m(9)=0.} \tag{56.1}
\]
This is **unconditional for all stated primes**. The two restricted formulas are \(G'=-G/18\) on the F-zero locus and \(G'=-F/288\) on the G-zero locus.

## GH-57 — discriminating second Laurent-obstruction jets (PROVED conditionally)

Define the GH-17/GH-33 Laurent obstruction \(\mathcal H_m(z)=F_m(z)G_m(z)\), not the elliptic Hasse invariant. Differentiating the Gauss equation once more gives
\[
 F_m'''(9)=-\frac7{16}F_m''(9)-\frac{121}{4608}F_m'(9),
 \qquad G_m''(9)=-26F_m''(9)-\frac{121}{32}F_m'(9).
\]
If \(F_m(9)=0\), then \(F'=G/144\), \(F''=-29F'/144\), \(G'=-G/18\); the product rule yields
\[
 \boxed{16\mathcal H_m''(9)+5\mathcal H_m'(9)=0.} \tag{57.F}
\]
For all primes \(p\equiv19\bmod24\), GH-32 provides \(F_m(9)=0\) and GH-18 coprimality \(G_m(9)\ne0\), so (57.F) holds unconditionally on that exact subfamily, with \(\mathcal H'_m(9)\ne0\).

If \(G_m(9)=0\), with \(F_m(9)\ne0\), then \(F'=-5F/144\), \(F''=209F/41472\), \(G'=-F/288\), and \(G''=11F/41472\). Hence
\[
 \boxed{48\mathcal H_m''(9)+7\mathcal H_m'(9)=0,\qquad
              \mathcal H'_m(9)\ne0.} \tag{57.G}
\]
**The G-branch conclusion has a premise \(G_m(9)=0\)**; the theorem does NOT establish that premise uniformly in the class \(p\equiv11\bmod24\). The two second-jet ratios \(-5/16\) and \(-7/48\) distinguish the F/G source-typed degeneracies.

## Executed exact checking and limits

The companion **byte-pinned Python standard-library checker** independently constructs the Legendre polynomial via its binomial expansion and verifies every coefficient of (55.2) at all **76 primes** \(11\le p<2000,\ p\equiv3\bmod8\). Independent F/G and Legendre special-value formulas, (56.1), and all applicable (57.F)/(57.G) were checked for **310 primes** \(11\le p<10000,\ p\equiv3\bmod8\). All checks passed. Additional class observations: **155/155** primes in class 11 had \(G_m(9)=0\); **155/155** in class 19 had \(F_m(9)=0\). These are **FINITE OBSERVATIONS ONLY**, not a uniform G-port proof or independent GH-3 proof. Samples: \(p=11:(F,G,G')=(6,0,8)\), \(19:(0,5,5)\), \(43:(0,6,14)\), \(59:(21,0,3)\), \(67:(0,33,54)\). All arithmetic uses exact modular inverses and integers; no floating-point approximation.

**BRC COMPOSE_APPLIED:** preserve original rank, signed \(\mathbb F_p\) coefficients, labeled F/G source ports, first/second derivative jets, the original observation \(z=9\), quadratic-even Legendre coordinate, and future allowed differentiation/evaluation. The \(t\)-coordinate is an auxiliary scalar extension representation, not an X6 native position, a three-dimensional research slice, or a safe quotient of the original W/S, six Hasse, Green R23/R36, \(\eta/\kappa\), and full provenance. Keep the ACTIVE P000 and scientific Source pin fixed.

**Next proof obligation:** independently establish or refute \(tP'_{(p-3)/4}(t)=P_{(p-3)/4}(t)\) at \(t^2=8/9\) for **all** \(p\equiv11\bmod24\), e.g. via actual CM/finite-field Gauss–Manin or prime-dependent WZ evidence; do not use the defining G sum as circular proof. Separately obtain an arithmetic proof of original GH-3 \(T_d(9)=0\), not a restatement of its reverse/convolution sum. Compare typed jets to GH-20/21 second-digit source only under actual observer-preserving maps.

**Control status at ~2026-10-28 21:19 Asia/Hong_Kong:** backend 0.6.11, research_authority_granted=false, write_relay_enabled=false, active native jobs 5/5, Source control CODE_REVIEW_REQUIRED. One exact typed continuation attempt failed INVALID_ARGUMENT / CONTROL_QUOTA; the callable recovery_status operation was not exposed to this client. No service session, CLAIM, OPEN, native publish, or handoff was fabricated. Historical session/staging and request identity are preserved. The existing control support path is Enterprise Math issue #1558. GH-55–GH-57 are author-side portable evidence, **UNREVIEWED / NOT_ADMITTED**, not a durable native Source checkpoint.
