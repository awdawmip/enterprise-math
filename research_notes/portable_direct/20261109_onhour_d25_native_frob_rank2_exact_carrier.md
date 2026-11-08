# D25 / LIFT — exact integral rank-two Frobenius carrier for the original-E3 comparison gate

Date: 2026-11-09 (Asia/Hong_Kong). Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication: TP2-B6F4FC938FF94941C1B7; scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Research source: on-hour TASK_RESEARCH author side, provenance label \`chatgpt-research-onhour-enterprise-math-20260923\`. Does not use maintenance conversation identity.

Status: **AUTHOR-SIDE PROVED ALGEBRAIC CARRIER / EXECUTED SYNTHETIC EXACT TEST / UNREVIEWED / NOT_ADMITTED / NATIVE H0/B0 NOT_RUN**. This unit builds a *positive* minimal two-port semilinear structure and a measurable signature of an authentic full-geometric comparison. It is not an alternative definition of the frozen native experiment.

## 1. A new small discriminating mathematical unit

The actual pending experiment (#1559) must report native original-class p=373 H0/B0 divided-power \`[X]U mod 139129\`, rank, semilinearity, normalization η, odd Green/Hesse κ, frozen Δ−R and an independent reproducer. Author-side original-E3 point counts from an earlier unit supply \(\operatorname{Fr}_{373^2}=[+373]\); the previously proved direct unramified rank-one obstruction says no operator \(a\sigma\) on a free rank-one \(R\) can have square \(+p\) when \(v_p(a)\in\mathbb Z\).

Here we determine **the minimal integral module that *can* realize that exact Frobenius square** and an immediately testable mod-p rank signature. This is a *conditional comparison theorem*: it applies to a native module only once a specific, invertible original-geometry comparison identifies that module with the full integral Frobenius lattice carrying \(F^2=\epsilon p I\). An unnamed Hesse polynomial or an arbitrarily chosen scalar is not such a comparison.

## 2. General theorem and proof (all odd inert primes)

Let \(p\) be an odd prime with \((2/p)=-1\), let \(O=\mathbb Z_p[T]/(T^2-2)\) be the unramified quadratic DVR, with \(\sigma(T)=-T\), and let \(M\) be a finite free \(O\)-module of rank \(n\). Suppose an \(O\)-integral \(\sigma\)-semilinear automorphism after inverting \(p\),
\[
 F:M\to M,\qquad F(a v)=\sigma(a)F(v),
\]
satisfies \(F^2=\epsilon p\,\mathrm{id}_M\), where \(\epsilon\in\{+1,-1\}\). Then:

**(i) Exact residual complex.** For \(\overline M=M/pM\) and induced semilinear \(\overline F\), one has
\[
 \operatorname{im}\overline F=\ker\overline F,\qquad
 \operatorname{rank}_{\mathbb F_{p^2}}\overline F=n/2.
\]
In particular \(n\) must be even.

**(ii) Integer-coordinate Smith signature.** The \(O\)-linear matrix \(A\) of \(F\) in a chosen basis has Smith elementary-divisor valuations exactly \(n/2\) zeros and \(n/2\) ones. In rank two, \(\overline A\) has rank one and \(v_p(\det A)=1\). Neither the sign nor basis choice changes these valuations.

**(iii) Constructive rank-two realization.** The explicit matrix
\[
 A_\epsilon=\begin{pmatrix}0&\epsilon p\\1&0\end{pmatrix}
\]
defines a \(\sigma\)-semilinear \(F_\epsilon(v)=A_\epsilon\sigma(v)\) with \(A_\epsilon\sigma(A_\epsilon)=\epsilon pI_2\), and satisfies the signatures (i)–(ii). Thus the full-geometric sign \(+p\) is algebraically *realizable* over the unramified coefficient ring in rank two. It does not require a ramified scalar coefficient or a rank-one identification.

**Proof.** Since \(\overline F^2=0\), \(\operatorname{im}\overline F\subseteq\ker\overline F\). Conversely, given \(\overline x\in\ker\overline F\), lift \(x\in M\); \(F(x)=p y\) for some \(y\in M\). Then
\[
 \epsilon p x=F^2(x)=F(p y)=pF(y),
\]
and \(M\) is \(p\)-torsion-free, so \(x=\epsilon F(y)\). This gives the reverse inclusion and rank-nullity yields (i). As \(pM=\epsilon F^2(M)\subseteq F(M)\), every Smith exponent of \(A\) is at most one; its reduction has rank \(n/2\), hence precisely that many zero exponents and the rest one. Part (iii) follows by direct multiplication. QED.

A verified change of integral basis \(U\in\mathrm{GL}_n(O)\) acts by
\[
 A\longmapsto A'=U^{-1}A\sigma(U),\qquad
 A'\sigma(A')=U^{-1}\bigl(A\sigma(A)\bigr)U=\epsilon p I.
\]
The rank and Smith signature are therefore invariant under the allowed gauge. The original elliptic cohomology and the native H0/B0 module are still separately tagged until a comparison map is actually supplied.

## 3. Exact original-sign and negative-control interface

At \(p=373\), \(p^2=139129\) and \(\epsilon=+1\) is the independently established *original-E3 geometric* sign. The explicit positive example \(A_{+}=\bigl(\begin{smallmatrix}0&373\\1&0\end{smallmatrix}\bigr)\) has \(\overline A_+\) rank one and determinant \(-373\), so its square gives \(+373I\) (mod \(373^2\)).

For a nontrivial \(\sigma\)-twisted integral gauge, set
\[
 U=\begin{pmatrix}1&T\\1+T&2\end{pmatrix},\quad \det U=-T,\quad N(\det U)=-2.
\]
The gauge determinant is a unit for every odd inert target prime. The executed checker forms \(A'=U^{-1}A_{\epsilon}\sigma(U)\) at \(p=13,19,373\) and verifies all six exact matrix squares modulo \(p^2\), the mod-p rank-one signature and determinant valuation one. Negative-sign inputs \(\epsilon=-1\) are tested separately and never relabeled as the positive geometric sign.

As a source-typed negative control, the prior **ordinary Hesse candidate** \(\alpha=92060+21788T\) modulo 139129 has \(N(\alpha)=122102\) and \(N(\alpha)\bmod373=131\). A rank-one operator \(\alpha\sigma\) is therefore not the whole original geometric \(F\). This computation is reused as a previous result, not credited as a new benchmark.

## 4. Test evidence and interpretation

Tool: Python 3 standard library, exact ordered pairs \((a,b)\) representing \(a+bT\), arithmetic modulo \(p^2\); no floating-point operations or delegated native assumptions. Test invocation:
\`python d25_native_frob_rank2_acceptance_20261109.py\`.

**Actual result:** PASS for \(p=13,19,373\), both signs, a nontrivial invertible \(\sigma\)-gauge, mod-p rank and Smith signature; PASS for previous p=373 ordinary-Hesse negative control. These are algebraic synthetic matrices **not obtained by running a native H0/B0 divided-power evaluator**. The script prints all full \(2\times2\) coordinate matrices and exact observations as JSON.

**Native acceptance interpretation.** When/if the genuine p=373 native H0/B0 operator is delivered, first preserve its actual rank, ring and orientation. If an independently justified comparison identifies its *full free integral lattice* with original \(E_3\) geometric Frobenius, then testing \(F^2=+373I\) requires mod-373 rank half and all elementary-divisor valuations \(0,1\) in equal number; rank two gives one of each. If the native object is a subquotient or a different normalized operator, use that documented structure and its own typed comparisons. Signed \(\kappa\) and frozen \(\Delta-R\) remain independent named observations.

BRC/coordinate bookkeeping: this result keeps \((p,\epsilon,\sigma,\text{module rank},\text{basis},\eta,\text{comparison map})\) as distinct carrier fields. The smaller mod-p rank/Smith signature is a proved projection from an authenticated square identity, never a reconstruction of the raw \([X]U\) coefficient or signed Green branch.

## 5. Exact continuation and source boundary

Mother objective remains \(\Delta_p-R_p\equiv0\pmod p\) for every \(p\equiv13,19\pmod{24}\), equivalent under the frozen source-port bridge to the original 216 sum \(W_p\equiv p\pmod{p^3}\). No universal proof or exact counterexample arose from this conditional rank-two result. In particular this unit does not reopen the accepted D24 UR/JT0, redo the earlier original-E3 point counts, or count a synthetic Frobenius as native execution.

Original native benchmark support: Issue #1559 OPEN, no named assignee on the present read. It still requires the authentic original H0/B0 \([X]U\bmod139129\), module rank, semilinear direction, normalization \(\eta\), odd Hesse/Green signed \(\kappa\), exact \(\Delta-R\), reproducible raw evidence and independent replication. Native Source execution was not authorized in this run: previously successful historical Researcher session \`MCP-ecbfd1c046864bb3bff1a2e04c87d207\` lacks its private capability (\`SESSION_CAPABILITY_REQUIRED\`); no own winning CLAIM or open run is established. Do not borrow maintenance credentials or other owners.

**Next precise scientific action:** authorized native executor produces the unaltered \([X]U\) p=373 data under the frozen pin. Record actual full operator and its compared module as-is; only if full-geometric correspondence is authenticated, apply the new half-rank and Smith signature along with positive \(+373\) square. Then check original \(\kappa\) and \(\Delta-R\) with independent replication. This is an actual pending experiment, not a completed one.

Source dependencies: frozen taskbook \`research_tasks/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT_610cb297.md\`; Source checkpoint \`research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/latest_checkpoint.json\`; previous original-E3 point-count and rank-one obstruction author records from 2026-11-08. 
