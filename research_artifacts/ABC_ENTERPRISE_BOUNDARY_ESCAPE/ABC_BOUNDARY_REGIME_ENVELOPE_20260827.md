# ABC Enterprise Boundary-Escape Regime — Exact Obstruction and Unconditional Envelope

Status: `FROZEN / EXACT_OBSTRUCTION / AWAITING DRIVER REVIEW`

Task: `RS-ABC-ENTERPRISE-BOUNDARY-ESCAPE`  
Publication: `TP2-CD1E2741D7E41F56418B`  
Claim: `chatgpt-abc3-20260827-1634`

## 0. Verdict

The requested boundary analysis has a normalization-independent rigorous core, but the frozen publication does **not** make the parent coordinate \(\beta\) reproducible: the taskbook asks to use an “exact beta definition from the parent analysis”, while its only pinned `source_ref`, `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md@c7a5a1c...`, contains the Enterprise-plane ontology but no definition of \(\beta\).

Accordingly the exact numerical map
\[
\beta\longleftrightarrow \frac{\min(a,b)}c
\]
cannot be certified without inventing a normalization. This is a source-contract obstruction and is kept explicit below.

Independently of that missing adapter, the arithmetic boundary regime can be classified exactly in the intrinsic coordinate
\[
m:=\min(a,b),\qquad x:=\frac{m}{c}\in(0,\tfrac12].
\]

The main result is:

> **Fixed geometric boundary depth is not enough.** For every fixed \(\delta>0\), the band \(x\le\delta\) contains primitive infinite families with \(m\asymp c\), so it does not imply any power-small-addend hypothesis \(m\le c^{1-\eta}\). To activate the strongest currently available unconditional small-addend theorem one needs the shrinking band \(x\le c^{-\eta}\), equivalently boundary depth growing like \(\eta\log c\) in any logarithmic small-addend coordinate. Even the ultra-thin family \((1,n,n+1)\) remains a nontrivial consecutive-radical problem for near-abc quality.

Thus the clean boundary split is **scale-sensitive**, not a fixed-\(\beta\)-constant cutoff.

## 1. Source-contract audit: why no beta formula is inserted

The immutable taskbook records only:

- “the exact beta definition and boundary-payment inequality from the parent analysis”;
- the inherited inequality \(D_{\rm sup}\le 2\beta+\log 16\);
- one pinned source file for the Enterprise plane.

Neither the taskbook nor that pinned source supplies the actual formula for \(\beta(a,b,c)\). Therefore two or more inequivalent normalizations with the same qualitative behavior “high beta = one addend small” cannot be distinguished from the durable inputs.

The only safe adapter statement is abstract. If the restored parent definition has
\[
\beta=B(x),\qquad x=m/c,
\]
with \(B\) strictly decreasing, then
\[
\beta\ge T\iff x\le B^{-1}(T).
\]
The function \(B\) itself must be restored from a durable parent artifact before a numerical \(\beta\)-threshold is canonical.

This does **not** invalidate the intrinsic \(x\)-classification below.

## 2. Exact boundary coordinate and two universal families

Let \(a,b,c\in\mathbb Z_{>0}\), \(a+b=c\), \(\gcd(a,b)=1\), and \(m=\min(a,b)\).

### Lemma 2.1 — consecutive family reaches every boundary band

For every \(n\ge1\),
\[
(a,b,c)=(1,n,n+1)
\]
is primitive and
\[
x=\frac1{n+1}\to0.
\]

Hence every fixed band
\[
\mathcal B_\delta:=\{(a,b,c):m/c\le\delta\},\qquad \delta>0,
\]
contains all sufficiently large members of this family.

### Lemma 2.2 — a fixed boundary band does not force a power-small addend

Fix \(0<\delta<1/2\), choose an integer
\[
M\ge \max(3,\lceil 1/\delta\rceil),
\]
and for \(t\ge1\) define
\[
a=t,\qquad b=(M-1)t+1,\qquad c=Mt+1.
\]

Then
\[
a+b=c,\qquad \gcd(a,b)=1,
\]
and, because \(M\ge3\), \(m=a=t\). Also
\[
\frac mc=\frac{t}{Mt+1}<\frac1M\le\delta.
\]

For every fixed \(\eta>0\),
\[
\frac{m}{c^{1-\eta}}
=\frac{t}{(Mt+1)^{1-\eta}}
\sim M^{-(1-\eta)}t^\eta\to\infty.
\]
Therefore all sufficiently large \(t\) violate
\[
m\le c^{1-\eta}.
\]

So there is no implication
\[
m/c\le\delta\quad\Longrightarrow\quad m\le c^{1-\eta}
\]
for any pair of fixed constants \(\delta>0,\eta>0\).

This is the first exact obstruction to treating a fixed high-boundary coordinate as a small-addend theorem trigger.

## 3. The correct scale parameter for small-addend theorems

For \(c>1\), define
\[
\eta_*(a,b,c):=\frac{\log(c/m)}{\log c}.
\]
Then exactly
\[
m=c^{1-\eta_*}.
\]

Thus, for a fixed \(\eta_0>0\),
\[
m\le c^{1-\eta_0}
\iff
\frac mc\le c^{-\eta_0}
\iff
\eta_*\ge\eta_0.
\]

This is the normalization-independent conversion the arithmetic actually needs.

Consequences:

1. a fixed ratio band \(m/c\le\delta\) has only
   \[
   \eta_*\ge\frac{\log(1/\delta)}{\log c},
   \]
   which tends to \(0\) as \(c\to\infty\);
2. a genuine power-small band requires the boundary ratio itself to shrink polynomially with \(c\);
3. if the missing parent \(\beta\) is logarithmic in the small-addend ratio, then the relevant threshold must grow on the order of \(\log c\), not remain constant. The exact coefficient cannot be stated until \(B(x)\) is restored.

## 4. Best unconditional arithmetic envelopes by intrinsic boundary band

Write
\[
R=\operatorname{rad}(abc).
\]

### Band A — no quantitative boundary input

For arbitrary primitive \(a+b=c\), the Stewart–Yu bound quoted in Pasten's paper is
\[
\log c\le \kappa\,R^{1/3}(\log R)^3
\]
for an absolute constant \(\kappa\).

This is the unconditional fallback envelope.

### Band B — fixed geometric boundary \(m/c\le\delta\)

A fixed \(\delta>0\) alone does **not** improve the hypothesis class to \(m\le c^{1-\eta_0}\) for any fixed \(\eta_0>0\), by Lemma 2.2.

Therefore the boundary ratio alone does not activate the power-small-addend theorem uniformly. With no additional arithmetic restriction, the rigorously imported uniform envelope remains the generic Stewart–Yu one above.

This is a statement about what follows from the boundary hypothesis alone; it does not say no other special arithmetic theorem can improve individual subfamilies.

### Band C — power-small boundary \(m/c\le c^{-\eta_0}\)

Pasten, Theorem 1.4(1) in arXiv:2312.03566v1, proves unconditionally that there is an absolute constant \(\kappa>0\) such that, whenever
\[
m\le c^{1-\eta_0},\qquad \eta_0>0,
\]
one has
\[
\boxed{
\log c\le
\eta_0^{-1}
\exp\!\left(\kappa\sqrt{(\log R)\log_2R}\right)
}.
\]

Because the equation is symmetric in \(a,b\), the smaller addend may be relabeled as the theorem's \(a\).

This is genuinely subexponential in \(R\) and is the strongest imported boundary-specific envelope used in this return.

### Band D — ultra-thin edge \(m=1\)

Here one may take \(\eta_0=1\), obtaining
\[
\log c\le
\exp\!\left(\kappa\sqrt{(\log R)\log_2R}\right).
\]

But the family
\[
(1,n,n+1)
\]
has
\[
R=\operatorname{rad}(n(n+1)).
\]
For the usual abc quality
\[
q(a,b,c):=\frac{\log c}{\log R},
\]
the statement
\[
q(1,n,n+1)\le 1+\varepsilon
\]
is **equivalent** to
\[
\operatorname{rad}(n(n+1))
\ge (n+1)^{1/(1+\varepsilon)}.
\]

Thus even an arbitrarily deep geometric escape region contains a concrete consecutive-integer radical problem not closed by the imported unconditional estimates. Boundary geometry by itself does not produce a near-abc \(q\)-bound.

## 5. Boundary-band table

| Intrinsic band | Exact hypothesis | Uniform unconditional envelope used here | What it does **not** give |
|---|---|---|---|
| A: unrestricted | \(0<x\le1/2\) | \(\log c\le\kappa R^{1/3}(\log R)^3\) | near-abc quality |
| B: fixed boundary | \(x\le\delta\), fixed \(\delta>0\) | same generic envelope from boundary data alone | any fixed \(\eta_0>0\) with \(m\le c^{1-\eta_0}\) |
| C: power-small | \(x\le c^{-\eta_0}\) | \(\log c\le\eta_0^{-1}e^{\kappa\sqrt{(\log R)\log_2R}}\) | \(q\le1+\varepsilon\) |
| D: edge | \(m=1\) | C with \(\eta_0=1\) | consecutive-radical near-abc bound |

External source for Bands A/C: Hector Pasten, *The largest prime factor of \(n^2+1\) and improvements on subexponential ABC*, arXiv:2312.03566v1, introduction and Theorem 1.4.

## 6. Interaction with the inherited geometric payment inequality

The taskbook preserves the parent statement
\[
D_{\rm sup}\le2\beta+\log16.
\]

Without the missing \(\beta=B(x)\) normalization, this inequality cannot be converted into a numerical \(x\)-band. More importantly, even after that adapter is restored, a **fixed** cap on or threshold for \(\beta\) can only yield a fixed geometric ratio band unless \(B\) itself incorporates \(\log c\). Lemma 2.2 then shows why a scale-free cutoff cannot by itself invoke the power-small-addend arithmetic theorem.

The interior/boundary decomposition should therefore be parameterized by a scale-dependent threshold corresponding to
\[
x=c^{-\eta_0}
\]
if the goal is to discharge the escaped part using current small-addend technology.

## 7. Exact uncovered gap

Two independent gaps are frozen.

### Gap G1 — durable normalization gap

The canonical parent formula for \(\beta\) is absent from the immutable publication's frozen source material. Therefore an “explicit beta-to-small-addend conversion” cannot be reproduced exactly in this task without an unauthorized guess.

**Repair:** publish or attach the parent \(\beta=B(m/c)\) definition (or equivalent exact formula) as a pinned durable source, then substitute \(x=B^{-1}(\beta)\) into the bands above.

### Gap G2 — arithmetic radical gap survives at the edge

After G1 is repaired, no fixed boundary band alone yields near-abc quality. The family \((1,n,n+1)\) survives arbitrarily deep into the boundary and reduces such a conclusion to the explicit radical lower bound
\[
\operatorname{rad}(n(n+1))
\ge(n+1)^{1/(1+\varepsilon)}.
\]

The current imported unconditional small-addend theorem gives a strong subexponential envelope but not this power-strength radical bound.

## 8. Frozen control-plane conclusion

Verdict:
\[
\boxed{\texttt{EXACT\_OBSTRUCTION}}
\]

What is frozen:

- exact intrinsic small-addend coordinate \(x=m/c\);
- proof that fixed boundary ratio does not imply a fixed power-small exponent;
- exact power-small conversion \(x\le c^{-\eta_0}\);
- generic Stewart–Yu envelope for unrestricted/fixed-ratio bands;
- Pasten subexponential envelope for power-small bands;
- consecutive-radical obstruction in the ultra-thin edge;
- exact identification of the missing durable \(\beta\) adapter.

No abc conjecture is invoked as an input, no desired radical bound is assumed, and conjectural and unconditional statements are not mixed.
