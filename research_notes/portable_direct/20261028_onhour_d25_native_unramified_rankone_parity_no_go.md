# D25 — unramified rank-one parity obstruction for the original-class native Frobenius benchmark

Date: 2026-10-28, on-hour Research lane. **AUTHOR-SIDE / EXACT FINITE-RING CONDITIONAL NO-GO / EXECUTED p=373 CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED**.

Mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; immutable publication `TP2-B6F4FC938FF94941C1B7`; science Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**. Research logical conversation `chatgpt-research-onhour-enterprise-math-20260923`, not the maintenance lane. There is **no** asserted current Source session ownership/CLAIM/open.

## Direct question: when is the existing conditional rank-one norm comparison structurally impossible?

Consume (do not reprove) the existing D25 Hilbert-90 author-side note `research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-d6dd85529e9e45a9b5f808c1025f5918/767679018d6c936f92dd/D25_R2_HILBERT90_20261025.md`, which defines, for p ≡ 13,19 mod 24,
[
R_2=(\mathbb Z/p^2\mathbb Z)[T]/(T^2-2),\qquad
\sigma(a+bT)=a-bT,\qquad N(x)=x\sigma(x).
]
It recorded a **conditional** comparison of a potential rank-one semilinear native coefficient with the *ordinary external Hesse candidate* \(\alpha_{373}=92060+21788T\pmod{373^2}\). This candidate is not an authenticated H0/B0 output. The research question is whether an unramified, rank-one Frobenius \(F(x)=u\sigma(x)\) can reproduce a supersingular half-slope first nonzero square digit \(F^2=p\cdot U\pmod{p^2}\), with U a unit.

## Theorem — valuation-parity no-go (exact finite-ring statement)

Let p>2, let \(R_2\) be an unramified quadratic \(\mathbb Z/p^2\mathbb Z\)-algebra whose reduction is \(\mathbb F_{p^2}\), and let \(\sigma\) be its nontrivial involution. For **any** \(u\in R_2\), the rank-one \(\sigma\)-semilinear endomorphism \(F_u(x)=u\sigma(x)\) has
[
\boxed{ F_u^2=N(u)\,\mathrm{id},\qquad
N(u)\text{ is either a unit or }0\pmod{p^2}. }
\tag{1}
]
In particular, for every unit \(v\in R_2^\times\),
[
\boxed{F_u^2\not\equiv p\,v\,\mathrm{id}\pmod{p^2}.}\tag{2}
]
The same exclusion applies after **any** coefficient rescaling \(u\mapsto\eta u\), including nonunit \(\eta\in R_2\), and under a rank-one basis-gauge change. Thus the absence of a specified normalization \(\eta\) is **not** enough to save an unramified rank-one model from (2) if an authenticated native observer actually imposes \(F^2=pU\) with U invertible modulo p.

**Proof.** Since \(R_2/pR_2=\mathbb F_{p^2}\) is a field, exactly one of these alternatives holds: (i) \(u\notin pR_2\), hence u and \(\sigma(u)\) are units and N(u) is a unit; (ii) \(u=pw\), hence N(u)=p²N(w)=0 in R_2. The equality \(F_u^2(x)=u\sigma(u)\sigma^2(x)=N(u)x\) follows directly. The element pv for v a unit is nonzero modulo p², yet not a unit; neither case permits equality. Rescaling and basis changes still give an R_2 coefficient, so the same dichotomy applies. QED.

**Sharpness / scope.** This is **not** a theorem that the unknown H0/B0 module has rank two. It only excludes the conjunction of (i) a genuine free rank-one unramified R_2 \(\sigma\)-semilinear realization and (ii) a required native square with exact valuation one. The latter would hold for an appropriately normalized full supersingular H¹ F-isocrystal if its first square digit has the assumed integral unit form. Whether this identification, native rank, chosen lattice, semilinear direction, normalization or square law applies to the actual frozen H0/B0 is **UNKNOWN and must be measured**. Other coefficient rings (especially ramified ones), non-F-stable fragments, other operators, or a different readout are outside (1)–(2). Standard background: supersingular elliptic H¹ has slope 1/2, while rank-one F-isocrystals over an unramified perfect-field Witt fraction field have integral slopes. Neither background fact is a new Enterprise Math discovery.

## Actual exact p=373 port certificate and minimal compatible model

p=373≡13 mod24; (2/p)=−1. Work in R_2 with modulus 139129. Independently recomputing the **already known ordinary candidate** yields:
[
\alpha=92060+21788T,\quad N(\alpha)
=(92060)^2-2(21788)^2
\equiv122102\pmod{139129},
]
[
N(\alpha)\bmod373=131\ne0,\qquad N(\alpha)^{-1}\equiv18818\pmod{139129}.
]
Thus any `unit eta` keeps N(eta alpha) a unit; any `nonunit eta` makes N(eta alpha)=0 mod p². **Neither can equal \(373\cdot v\) for v a unit.** This is an exact falsifier for the *proposed identification under a half-slope square requirement*, not for LIFT/JT2 or the H0/B0 object itself.

The obstruction is **rank-specific**, not an impossibility for semilinear Frobenius. Over the same ring define on a free rank-two module:
[
F(\mathbf x)=A\sigma(\mathbf x),\qquad
A=\begin{pmatrix}0&p\\1&0\end{pmatrix}.
]
Because \(\sigma(A)=A\), this toy model satisfies \(F^2=A\sigma(A)=pI_2\pmod{p^2}\), with determinant \(-p\). It is an *external algebraic witness*, **not** a reconstructed native H0/B0 Frobenius.

Actual Python 3 standard-library modular operations checked the norm, inverse, three representative eta rescalings and the rank-two matrix square. Output:
```text
eta (1, 0) F2 scalar norm 122102 class unit
eta (373, 0) F2 scalar norm 0 class zero-mod-p2
eta (123, 45) F2 scalar norm 16791 class unit
rank2 F^2 ((373, 0), (0, 373))
PASS_D25_UNRAMIFIED_RANK_ONE_ODD_VALUATION_OBSTRUCTION_P373
```
Reproduction core (no native execution):
```python
p=373; modulus=p*p
a,b=92060,21788
norm=(a*a-2*b*b)%modulus
assert (norm,norm%p,pow(norm,-1,modulus))==(122102,131,18818)
A=((0,p),(1,0))
A2=tuple(tuple(sum(A[i][k]*A[k][j] for k in (0,1))%modulus
               for j in (0,1)) for i in (0,1))
assert A2==((p,0),(0,p))
```
The categorical no-go (1)–(2) is proved algebraically; the numeric check is one p373 instance, not evidence that the native half-slope condition holds.

## BRC / Enterprise coordinate and source audit

**BRC COMPOSE_APPLIED:** carrier = (original CM class, p=373, coefficient ring R_2, exact rank, semilinear \(\sigma\), coefficient u, \(v_p\), future \(F^2\), ordered signed odd Green/Hesse provenance, actual native-vs-external source). Observer = \(F^2\bmod p^2\), then only conditionally its scalar norm. The valuation partition `unit / p·unit / zero mod p²` is preserved before comparing norm. Rank and Frobenius direction cannot be compressed into one unsigned norm until the required factorization and observer lease are proved. This is **external arithmetic** only, not a claimed native X6 plane, force relation, or P000 modification.

### Native acceptance decision sharpened, **not satisfied**

Issue `awdawmip/enterprise-math#1559` remains the existing support path: original p373 H0/B0 divided-power [X]U mod139129, measured module rank, actual σ-semilinear direction and eta, same-definition signed odd Green/Hesse, original kappa and Delta_p−R_p, and raw reproducible source/normalization. The **additional discriminating question** for its real executor is: does the authenticated H0/B0 F² observer satisfy \(F²\equiv pU\pmod{p²}\) with U invertible? If **yes**, no unramified free rank-one σ-model can represent that very observer, independent of unit/denominator-free eta; record actual rank/matrix instead of forcing comparison to 122102. If **no or unknown**, no rank rejection follows from this note; keep original benchmark unchanged. No executor assignment, experimental run, Source claim or Result is asserted.

**Highest validated frontier:** existing author-side Hilbert-90 rank-one norm conditional + this new valuation-parity no-go. **Do not repeat:** accepted D24 UR/CM0; previously published Hesse/Hilbert-90 norm, original 216 third-digit finite scans or scalar source-port derivations. **Precise next mathematical action:** derive a *source-authenticated* bridge (or falsification) from original native H0/B0's actual operator to its Frobenius-square valuation and integral lattice, retaining rank and odd signed observer. If unavailable, retain the conditional no-go and prioritize #1559's real native execution; do not replace it by this toy matrix. Formal D25/LIFT/JT2 is still **OPEN**.

Research Source site status at 2026-10-28 15:05 +08:00: research_authority_granted=false, write_relay_enabled=false, native active jobs quota 5/5, upstream code review required. Original ordinary-control #6575 is read-only historical recovery pointer; #6576 final FAILED / TimeoutExpired. This GitHub note is an **author-only noncanonical scientific artifact**, not a native session, activity registration, Source checkpoint, review or admission.

External background for source checking: mathlib WittVector Isocrystal rank-one slope classification at https://math.iisc.ac.in/~gadgil/PfsProgs25doc/Mathlib/RingTheory/WittVector/Isocrystal.html ; standard supersingular H¹ slope semantics is classical (see https://en.wikipedia.org/wiki/Supersingular_variety ). The proof of (1)–(2) is self-contained and independent of external slope classification.
