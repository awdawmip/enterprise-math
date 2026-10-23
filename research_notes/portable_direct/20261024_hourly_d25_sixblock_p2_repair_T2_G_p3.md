# D25/LIFT — A second-digit six-block harmonic repair and a third-digit seam normalization

2026-10-24 | TASK_RESEARCH | exact author-side algebra | **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. This is not a Source CLAIM, authorized run, independent review, native CM comparison, benchmark, freeze or final LIFT proof.

**Parent**: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific source pin**: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged. Logical author lane: chatgpt-research-hourly-enterprise-math-20260923, separate from CONTROL_PLANE_MAINTENANCE and from the onhour research lane. The latter's already published six-way Lerch identity and strict mod-p² counterexample, and this lane's already published exact seam-to-target product, are **inputs**, not claimed as new results. Global knowledge checked at canonical main e29d16ce5d2abb0f99684e96ec41a8a8ba4e106f; P000 ACTIVE_LOCKED. Current research work is external finite rational arithmetic, not an assertion about native X6 coordinates.

## Fixed variables and unchanged research obligation

Let \(p=6m+1\ge7\) be prime. Write \(H_r=\sum_{k=1}^r1/k\), \(Q_r=H_r^{(2)}=\sum_{k=1}^r1/k^2\), \(H_0=Q_0=0\), with all fractions interpreted in \(\mathbb Z_{(p)}\). For brevity put \(\mathsf H_j=H_{jm}\) and \(\mathsf Q_j=Q_{jm}\) for \(1\le j\le6\). The exact inherited quantities are

\[
q_p(a)=\frac{a^{p-1}-1}{p},\qquad
T_2=\frac{R_{2m}}p,\qquad
G_m=(-1)^m\frac{((2m)!)^3}{((3m)!)^2}.
\]

The prior onhour proof gave \(\mathsf H_1-\mathsf H_2-\mathsf H_3\equiv0\pmod p\) and a strict counterexample to silently lifting that equality modulo \(p^2\). The prior hourly proof gave the exact all-\(m\) finite product for \(T_2/G_m\), but only its first-order \(p^2\)-precision expansion. The present two units resolve precisely these finer-observer deficits. The original D25 finite LIFT obstruction modulo \(p\) and the Source-specific CM divided-power comparison are **still open**.

## Theorem 1 — exact universal \(p^2\) repair of the six-block harmonic seam

For every prime \(p=6m+1\ge7\),

\[
\boxed{H_m-H_{2m}-H_{3m}
\equiv \frac p6\bigl(2H_{2m}^{(2)}-H_m^{(2)}\bigr)\pmod{p^2}.}\tag{SB2}
\]

Thus the residue deleted by the previous mod-\(p\) compression is a fully explicit quadratic reciprocal observer. It is generally nonzero; the result **does not** state the uncorrected equality modulo \(p^2\).

### Proof from a second-order finite residue permutation

For \(a\in\{2,3,6\}\), set \(b_{a,k}=\lfloor ak/p\rfloor\) for \(1\le k<p\). Since \(a<p\) and multiplication by \(a\) permutes nonzero residues, the integers \(r_{a,k}=ak-pb_{a,k}\) permute \(1,\ldots,p-1\), yielding the **exact rational product**

\[
1=\prod_{k=1}^{p-1}\frac{r_{a,k}}k
=(1+pq_p(a))\prod_{k=1}^{p-1}\left(1-\frac{p\,b_{a,k}}{ak}\right).
\]

Put \(S_1(a)=\sum b_{a,k}/k\) and \(S_2(a)=\sum b_{a,k}^2/k^2\). Expanding the finite product through \(p^3\), reducing first modulo \(p\), then substituting that first digit into the second, gives

\[
\boxed{a q_p(a)\equiv S_1(a)+p C_a\pmod{p^2},\quad
C_a=\tfrac12\left(aq_p(a)^2+\frac{S_2(a)}a\right).}\tag{L2}
\]

No logarithm, numerical interpolation or unlicensed division by \(p\) is involved. Splitting the \(p-1=6m\) residue indices into the six blocks of length \(m\) evaluates the two sums **exactly**:

| \(a\) | \(S_1(a)\) | \(S_2(a)\) |
| --- | --- | --- |
| 2 | \(\mathsf H_6-\mathsf H_3\) | \(\mathsf Q_6-\mathsf Q_3\) |
| 3 | \(2\mathsf H_6-\mathsf H_4-\mathsf H_2\) | \(4\mathsf Q_6-3\mathsf Q_4-\mathsf Q_2\) |
| 6 | \(5\mathsf H_6-\sum_{j=1}^5\mathsf H_j\) | \(25\mathsf Q_6-\mathsf Q_1-3\mathsf Q_2-5\mathsf Q_3-7\mathsf Q_4-9\mathsf Q_5\) |

For any prime \(p\ge5\), \(\sum_{k=1}^{p-1}k^{-2}=0\bmod p\), since inversion permutes the nonzero residues and the quadratic power sum is zero. Pairing \(k\leftrightarrow p-k\) then gives \(\mathsf H_6\equiv0\bmod p^2\). The same reflection at the block boundaries yields

\[
\mathsf H_5\equiv\mathsf H_1+p\mathsf Q_1,\quad
\mathsf H_4\equiv\mathsf H_2+p\mathsf Q_2\pmod{p^2},
\]
\[
\mathsf Q_6\equiv\mathsf Q_3\equiv0,\quad
\mathsf Q_5\equiv-\mathsf Q_1,\quad
\mathsf Q_4\equiv-\mathsf Q_2\pmod p.
\]

The exact integer identity \(6^{p-1}=2^{p-1}3^{p-1}\) implies
\(q_p(6)=q_p(2)+q_p(3)+p q_p(2)q_p(3)\).
Subtract \(3\) times (L2) for \(a=2\) and \(2\) times (L2) for \(a=3\) from (L2) for \(a=6\). The first-order combination is

\[
S_1(6)-3S_1(2)-2S_1(3)
\equiv -2D+p(\mathsf Q_2-\mathsf Q_1)\pmod{p^2},
\quad D:=\mathsf H_1-\mathsf H_2-\mathsf H_3.
\]

The second-order coefficient obeys, by the displayed table and reflections,

\[
C_6-3C_2-2C_3
\equiv6q_p(2)q_p(3)+\frac{2\mathsf Q_1-\mathsf Q_2}{3}\pmod p.
\]

Consequently

\[
6p q_p(2)q_p(3)
\equiv-2D+p\left[\mathsf Q_2-\mathsf Q_1
+6q_p(2)q_p(3)+\frac{2\mathsf Q_1-\mathsf Q_2}{3}\right]\pmod{p^2},
\]

and cancellation of the *same retained mixed term* proves (SB2). QED.

## Theorem 2 — all-target harmonic formula for the second digit of \(q_p(6)\)

Put \(h_m=(3H_m+H_{2m})/6\). In the same p-local ring,

\[
\boxed{q_p(6)\equiv
-h_m+p\left(\frac{h_m^2}{2}
-\frac{3H_m^{(2)}+2H_{2m}^{(2)}}{36}\right)
\pmod{p^2}.}\tag{Q6-2}
\]

**Proof.** Specialize (L2) at \(a=6\) and use the same table and reflected blocks:

\[
6q_p(6)\equiv
-2\mathsf H_1-2\mathsf H_2-\mathsf H_3
+p\left(3q_p(6)^2-\frac{\mathsf Q_1+2\mathsf Q_2}{3}\right)\pmod{p^2}.
\]

By (SB2), \(\mathsf H_3\equiv\mathsf H_1-\mathsf H_2-p(2\mathsf Q_2-\mathsf Q_1)/6\bmod p^2\). Substitution gives
\(6q_p(6)\equiv-3\mathsf H_1-\mathsf H_2+
p(3q_p(6)^2-(3\mathsf Q_1+2\mathsf Q_2)/6)\).
The first digit is \(q_p(6)\equiv-h_m\bmod p\); replace the square inside the already p-multiplied correction by \(h_m^2\). Divide by the p-unit \(6\), proving (Q6-2). QED.

## Theorem 3 — a full \(p^3\) seam-to-target normalization

Set
\[
X_m=4+\frac32H_m-\frac{11}{6}H_{2m},\qquad
Y_m=8+\frac12X_m^2+\frac14H_m^{(2)}-\frac{16}{9}H_{2m}^{(2)}.
\]

Then for **all target primes**, including \(p=7\),

\[
\boxed{\frac{T_2}{G_m}\equiv-3\bigl(1+pX_m+p^2Y_m\bigr)\pmod{p^3}.}\tag{TG3}
\]

All displayed rational denominators are p-units; \(T_2/G_m\) is well-defined in \(\mathbb Z_{(p)}\). This supplies the *third digit of the first seam relative to the exact target*, one order beyond the preceding (NORM-p2) lemma.

**Proof.** Start **without modular simplification** from the already proved all-\(m\) product

\[
\frac{T_2}{G_m}=
\frac{1}{2m\,6^{p-1}}\;
\frac{\prod_{j=1}^{2m-1}(1+p/j)\,\prod_{k=1}^{2m}(1-p/k)}
{\prod_{k=2m+1}^{3m}(1-p/k)}.\tag{P}
\]

Put \(A=H_{3m}-H_{2m}-1/(2m)\) and \(B=H_{3m}^{(2)}-3H_{2m}^{(2)}+1/(2m)^2\). Expanding the finite products in (P), still keeping all seam factors, gives

\[
\frac{\prod(1+p/j)\prod(1-p/k)}{\prod(1-p/k)}
\equiv 1+pA+\frac{p^2}{2}(A^2+B)\pmod{p^3}.
\]

Because \(2m=(p-1)/3\),
\[
\frac1{2m}\equiv-3(1+p+p^2)\pmod{p^3},
\qquad 6^{-(p-1)}=(1+pq_p(6))^{-1}
\equiv1-pq_p(6)+p^2q_p(6)^2\pmod{p^3}.
\]

Combining gives \(-3[1+p(1+A-q_p(6))
+p^2(1+A+(A^2+B)/2-q_p(6)(1+A)+q_p(6)^2)]\).
Apply (SB2) and (Q6-2), use \(H_{3m}^{(2)}\equiv0\bmod p\), and collect coefficients. The first bracket becomes \(X_m\); the second becomes

\[
8+\tfrac12X_m^2+\tfrac14H_m^{(2)}-\tfrac{16}{9}H_{2m}^{(2)}=Y_m.
\]

This calculation is valid term by term modulo \(p^3\) because only the p-multiplied factor needs a second digit, and only the p²-multiplied factor needs a first digit. It makes no assumption about the still-open forcing sum. QED.

## Executed author verification and witnesses

The author executed integer modular-inverse and exact rational factorial calculations, without floating point or a native Source experiment. (SB2) passed for **all 148 primes \(p<2000\) with \(p\equiv1\bmod6\)**. (Q6-2) passed for **all 121 such primes \(p<1600\)**. (TG3) was checked by a *separately reconstructed* exact factorial \(T_2=(8m)!/[p6^{p-1}((4m)!)^2]\) and \(G_m\) for **21 target primes** with \(1\le m\le34\); the product expansion did not serve as its own verifier. All finite tests passed.

| p | \((H_m-H_{2m}-H_{3m})\bmod p^2\) | \(q_p(6)\bmod p^2\) | \((T_2/G_m)\bmod p^3\) |
| ---: | ---: | ---: | ---: |
| 7 | 14 | 1 | 123 |
| 13 | 104 | 102 | 374 |
| 19 | 209 | 211 | 1574 |
| 31 | 217 | 54 | 24053 |
| 37 | 148 | 167 | 39957 |
| 61 | 3233 | 781 | 127609 |

The derivations above, not this finite evidence, support their quantified statements. None of the checks is independent Driver validation, a Source-native run or a completed D25/CM task.

## BRC observer/provenance and next research unit

**Applied structural BRC gate, not a positive-mass cancellation theorem.** The pre-subtraction carrier retains the six labeled residue blocks, the original \(k\) and floor \(b_{a,k}\), positive rational reciprocal/squared-reciprocal weights, and the signed algebraic combination of three such labeled finite sums. The future observers are the first/second \(p\)-adic digit and the fixed \(T_2/G_m\) scalar through \(p^3\). The previous projection \(q_p(6)\mapsto\) harmonic first digit is proved non-faithful at the next observer; (SB2) and (Q6-2) give explicit repair coordinates, and (P) preserves exact factor provenance. Signed cancellation in (L2) is **external rational algebra**, not a claim of cancellation in a positive-weight-only BRC semiring. No Heartbeat physical/native spatial interpretation is asserted.

**Durable status:** portable author-side note only, with Source task/publication and frozen science pin preserved; **UNREVIEWED / NOT_ADMITTED**. No new native Source execution authority, checkpoint, Result or independent acceptance was acquired. The original Source D25 continuation remained in parked/needs-new-owner posture pending concrete source-specific divided-power representative, leading normalization and same-class comparison; this arithmetic note does not supply that missing CM choice.

**Next exact scientific action:** use the inherited exact \(T_4/T_2\) product and the new (TG3) to obtain the *two-seam* scalar transport through \(p^3\), retaining \(2m\) and \(4m\) seam labels. Then test whether the third-digit observer eliminates an independent high-sector defect without claiming the still-open all-prime finite obstruction or replacing the required Source CM normalization. Carry the same task/parent/proof-strength/pin and avoid rerunning previously audited mod-\(p\) Lerch, mod-\(p^2\) first-seam, or finite-zero scans.
