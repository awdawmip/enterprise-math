# EBP6JT continuation — Chisholm CM closure of JT0/UR and height-2 LIFT frontier

Status: `DIRECT_TASK_RESEARCH_CONTINUATION / JT0+UR_PROVED_BY_PRIOR_ART / LIFT_OPEN`

Date: `2026-09-08`

Researcher-ID: `EM-UR24-7C91A0`

Parent task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE`

Parent publication: `TP2-A19C97A703AF47D1CBEC`

Parent strict-reduction frontiers: PR #1375 (`RR-82F6383FB6634F72B457`) and independent audit PR #1379 (`RR-BDF69EEDA87C8D22F3BC`).

Control boundary: no new immutable-V2 UR successor publication was found at the start of this continuation. This file is a durable research continuation artifact, not a fabricated task publication, claim, Driver review, Working Truth promotion, or Foundation admission.

## 1. Frozen parent interface

For

\[
p=6m+1,\qquad p\equiv13,19\pmod{24},
\]

the accepted strict reduction defines

\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2 2^k},\qquad
 g=\sum_{k=0}^{p-1}B_k,\qquad
 h=\sum_{k=0}^{p-1}(12k+1)B_k,
\]

with \(p\mid g\), and

\[
G_p=\frac gp.
\]

The Legendre transport writes

\[
P_{2m}(T)=Q_m(T^2),\qquad H_m(z)=Q_m(1-z),
\]

and the parent proof establishes

\[
Q_m(1/2)\equiv0\pmod p,\qquad Q'_m(1/2)\not\equiv0\pmod p.
\]

The first digit is exactly

\[
(JT0)\iff (UR):\qquad
G_p\bigl(-6Q'_m(1/2)\bigr)\equiv1\pmod p. \tag{UR}
\]

After UR, the remaining second digit is

\[
\Delta_p:=\frac{G_ph-1}{p}\pmod p,
\qquad
(LIFT):\quad \Delta_p\equiv R_p\pmod p. \tag{LIFT}
\]

The full certificate remains

\[
(JT2)\iff (UR)+(LIFT).
\]

## 2. Weighted Ramanujan sum attached to JT0

Let

\[
W_p:=\sum_{k=0}^{p-1}(6k+1)
\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k}.
\]

Using

\[
\frac{(1/2)_k}{k!}=\frac{\binom{2k}{k}}{4^k},
\]

and

\[
\frac{(1/3)_k(2/3)_k}{(k!)^2}
=\frac{\binom{3k}{k}\binom{2k}{k}}{27^k},
\]

we obtain the exact hypergeometric form

\[
W_p=\sum_{k=0}^{p-1}
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}
(6k+1)\left(\frac12\right)^k. \tag{W}
\]

The frozen predecessor bridge identifies

\[
(JT0)\iff W_p\equiv p\pmod{p^2}. \tag{BRIDGE-1}
\]

The stronger full plus target is

\[
W_p\equiv p\pmod{p^3}, \tag{W3}
\]

with the frozen reflected tail scalar \(R_p\) carrying the second-digit correction; equivalently this is the parent JT2 target.

## 3. Chisholm–Deines–Long–Nebe–Swisher Theorem 1 closes JT0

Source:

Sarah Chisholm, Alyson Deines, Ling Long, Gabriele Nebe, Holly Swisher,
“p-Adic Analogues of Ramanujan Type Formulas for 1/π”, *Mathematics* 1 (2013), 9–30/31, DOI `10.3390/math1010009`.

Their Theorem 1 treats the CM Ramanujan-type family

\[
\sum_{k=0}^{p-1}
\frac{(1/2)_k(1/d)_k((d-1)/d)_k}{(k!)^3}
(ak+1)\lambda_d^k
\]

for \(d\in\{2,3,4,6\}\). In the supersingular branch it gives

\[
\sum_{k=0}^{p-1}\cdots
\equiv
-\left(\frac{1-\lambda_d}{p}\right)p
\pmod{p^2}, \tag{CDLNS}
\]

under the stated good-reduction/unramified/unit hypotheses. (The ordinary branch has the opposite sign.)

Our series is the exact specialization

\[
d=3,\qquad \lambda_3=\frac12,\qquad a=6.
\]

The project’s already-proved Hesse/Legendre CM identification gives discriminant \(-24\), CM field

\[
K=\mathbf Q(\sqrt{-6}),
\]

and singular \(j\)-values

\[
2417472\pm1707264\sqrt2.
\]

For every target prime \(p\equiv13,19\pmod{24}\):

1. \(p>3\), so all fixed denominators in the specialization are \(p\)-units;
2. \(p\) is unramified in \(\mathbf Q(\sqrt2)\) and the specialized CM curve has good reduction at these target primes;
3. \(\left(\frac{-6}{p}\right)=-1\), so the CM reduction is supersingular;
4. \(p\equiv3,5\pmod8\), hence
   \[
   \left(\frac{1/2}{p}\right)=\left(\frac2p\right)=-1.
   \]

Therefore the two negative signs in `(CDLNS)` cancel and

\[
\boxed{W_p\equiv p\pmod{p^2}} \tag{W2-PROVED}
\]

uniformly for both target residue classes.

Combining `(W2-PROVED)` with the already-frozen equivalence `(BRIDGE-1)` yields

\[
\boxed{JT0\ \text{is proved for all target primes}.}
\]

Combining further with the already-proved parent equivalence `JT0 iff UR` yields

\[
\boxed{
G_p\bigl(-6Q'_m(1/2)\bigr)\equiv1\pmod p
}
\]

for all target primes. Thus

`UR = PROVED_BY_EXISTING_CM_RAMANUJAN_CONGRUENCE`.

This is a prior-art closure of the first digit, not a new theorem-priority claim. It corrects the prior project state in which UR was left as an open successor certificate after only finite regression.

## 4. What the 2013 proof says about the second digit

The same paper’s supersingular proof works through de Rham/Atkin–Swinnerton-Dyer coefficient recurrences and a degree-\(p^2\) Frobenius endomorphism (equivalently the relevant CM multiplication-by-\(-p\) map after the specialization/twist).

At the key supersingular step, the Frobenius matrix has trace zero and off-diagonal divisibility/unit behavior that implies the required product congruence modulo \(p^2\). The proof only retains the Frobenius coefficient comparison to the precision needed for the final mod-\(p^2\) weighted congruence.

Consequently, the next required information for `(W3)` / `(LIFT)` is not another proof of CM supersingularity, Hasse vanishing, or simple-root transversality. It is the **next p-adic digit of the height-2 Frobenius/de Rham coefficient comparison**, together with the already-frozen truncation/Clausen-tail correction represented by \(R_p\).

This gives a sharper structural frontier:

\[
\boxed{
LIFT=\text{height-2 supersingular Frobenius next digit matched to the frozen }R_p\text{ correction}.
}
\]

No equality between an unnamed Frobenius-matrix coefficient and \(R_p\) is asserted here without a separate derivation; the claim is a localization of the missing information, not a completed p³ formula.

## 5. Two route exclusions / boundaries

### 5.1 Coster–van Hamme split-CM ASD supercongruence does not apply

Coster–van Hamme, “Supercongruences of Atkin and Swinnerton-Dyer Type for Legendre Polynomials”, JNT 38 (1991), assumes the relevant CM prime splits (their theorem is in the \(({-d}/p)=1\) regime).

Our lane has

\[
\left(\frac{-6}{p}\right)=-1.
\]

Therefore the attractive higher-precision split-CM Legendre/ASD theorem is not directly instantiable. This confirms the parent project’s earlier ordinary/split-CM no-go rather than overcoming it.

### 5.2 Ordinary unit-root Hasse–Witt formulas are the wrong local rank

Standard unit-root Dwork/Hasse–Witt formulas require invertibility of the first Hasse–Witt matrix (or equivalent ordinary locus condition). Here the selected point is exactly supersingular and the Hasse invariant vanishes.

Recent “beyond the unit-root part” / higher Hasse–Witt / whole-de-Rham Cartier-matrix frameworks are conceptually relevant, but no theorem located in this continuation directly supplies the exact second digit `(LIFT)` at this discriminant-\(-24\) supersingular point.

Beukers–Vlasenko’s Dwork-crystals work is especially informative as a boundary: excellent Frobenius lifts can strengthen certain Cartier congruences, but their desired generic enhancement of the truncation-ratio congruence to twice the p-adic precision is explicitly left conjectural in the cited setting. Thus invoking “excellent Frobenius” by name is not a proof of `(LIFT)`.

## 6. BRC information audit

`BRC_REUSE_RESOLUTION = REUSE_APPLIED + COMPOSE_APPLIED`.

Population: target primes \(p\equiv13,19\pmod{24}\), kept as labeled branches.

Exact carrier retained from the parent:

\[
(B_k;\ g,h,G_p\bmod p^2,R_p;\ Q_m(1/2),Q'_m(1/2)).
\]

New external theorem observer: the weighted scalar \(W_p\bmod p^2\), which is adequate for the first digit because the predecessor has already proved `(BRIDGE-1)`.

Loss guard: the theorem `(W2-PROVED)` may close `UR`, but it must not be used to collapse \(G_p\bmod p^2\), \(h\bmod p^2\), or \(R_p\); those coordinates remain necessary for `(LIFT)`.

Precision horizon:

- `CM0/SIMPLE/UR/JT0`: mod \(p\) / weighted mod \(p^2\), now theorem-level closed;
- `LIFT/JT2`: requires the next digit / weighted mod \(p^3\), still open.

This is precisely the BRC repair-coordinate principle: the first-digit observer can be safely quotient-collapsed after theorem factorization, while the second-digit carrier cannot.

## 7. Literature boundary checked in this continuation

Targeted searches did not locate a direct proof of

\[
W_p\equiv p\pmod{p^3}
\]

for the present inert/supersingular discriminant-\(-24\) lane.

The 2013 Chisholm–Deines–Long–Nebe–Swisher paper explicitly distinguishes its proved mod-\(p^2\) Ramanujan-type congruence from the stronger mod-\(p^3\) phenomenon conjectured by Zudilin. Subsequent Dwork-crystal literature supplies powerful higher-precision mechanisms but does not, in the material checked here, instantiate the exact target automatically.

This is a bounded prior-art audit, not a universal nonexistence claim.

## 8. Updated freeze

`CM_HASSE_ZERO = PROVED` (parent).

`SIMPLE_ROOT_TRANSVERSALITY = PROVED` (parent).

`WEIGHTED_W2 = PROVED_BY_CHISHOLM_DEINES_LONG_NEBE_SWISHER_THEOREM_1`.

`JT0 = PROVED`.

`UR = PROVED`.

`LIFT = OPEN`.

`JT2 = EQUIVALENT_TO_LIFT_GIVEN_PROVED_UR / OPEN`.

`WEIGHTED_W3 = OPEN_IN_THIS_EXECUTION`.

`SPLIT_CM_COSTER_VAN_HAMME_ROUTE = NOT_APPLICABLE_TO_INERT_LANE`.

`ORDINARY_UNIT_ROOT_ROUTE = NOT_APPLICABLE_AT_SUPERSINGULAR_HASSE_ZERO`.

`HEIGHT2_FROBENIUS_NEXT_DIGIT = CURRENT_SHARPEST_LIVE_INTERFACE`.

`FINITE_PRIME_SCAN = REGRESSION_ONLY / NO_LONGER_EVIDENCE_SOURCE_FOR_UR_THEOREM_STATUS`.

`WORKING_TRUTH_PROMOTION = NONE`.

`FOUNDATION_PROMOTION = NONE`.

`OFFICIAL_SUCCESSOR_TASK_PUBLICATION = NONE_CREATED_BY_THIS_ARTIFACT`.

## 9. Smallest next executable mathematical action

Do not reopen CM0, SIMPLE, the five harmonic arrays, or the parent Clausen decomposition.

Work directly in the supersingular height-2 de Rham/Frobenius interface used by Proposition 16 of Chisholm–Deines–Long–Nebe–Swisher:

1. retain one additional p-adic digit in the degree-\(p^2\) Frobenius matrix/coefficient comparison;
2. express the resulting scalar correction in the same normalization as the parent \(G_ph\) product;
3. subtract the frozen reflected tail coordinate \(R_p\);
4. prove that the residual scalar is zero mod \(p\), or produce an exact counterexample.

The target is now one second-digit scalar only:

\[
\boxed{
\frac{G_ph-1}{p}-R_p\equiv0\pmod p.
}
\]

That is the smallest unresolved unit after the current continuation.
