# Weighted/Log BRC Foundation Retrofit — Old-Research Regression

Status: `RESEARCH REGRESSION / EXACT ALGEBRAIC RECHECK + BOUNDARY TEST`
Date: `2026-09-02`
Researcher-ID: `EM-STW-B9F4C2`
Foundation baseline: `main@ba9e8fb6801d30406bccc3df7f7693263b12c861`
Foundation input: `definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md`

## 0. Question

After promoting the positive Weighted/Log BRC layer into the current research Foundation, does re-running older research actually improve anything?

Three deliberately different prior routes were selected:

1. the full unsieved BRC support/thickness two-scale decomposition;
2. the width-one neighboring-arm selector-flip reduction;
3. the oriented positive-axis holonomy cocycle.

The regression criterion is not “can the new language restate the old result?” It asks whether the new Foundation:

- removes redundant state;
- reveals a stronger exact identity;
- shortens the proof/interface;
- moves the true blocker to a cleaner boundary; or
- correctly reports no gain / non-applicability.

## 1. Regression A — support/thickness two-scale BRC

### 1.1 Old state

The previous route used

\[
\omega(n),\qquad
\Theta(n)=\sum_{p^e\Vert n,\ e\ge2}\ln\frac{e+1}{2},
\]

and

\[
\Delta_1(n)=H_1(n)-\frac{\omega(n)}2,
\qquad
H_1(n)=\sum_{p^e\Vert n}\frac e{e+1}.
\]

Its exact factorization was

\[
\operatorname{BRC}(n)
=1+2^{\omega(n)}e^{\Theta(n)}
\left(\frac{\omega(n)}2-1+\Delta_1(n)\right).
\]

The probabilistic two-scale theorem then separated the growing distinct-prime support mode from the \(O(1)\) repeated-prime thickness field.

### 1.2 Foundation retrofit

The new Foundation says an equal-weight \(k\)-branch family has log multiplicity surplus \(\ln k\). Apply this twice to the divisor-choice structure.

The Boolean squarefree skeleton has exactly

\[
C_{\mathrm{bool}}(n)=2^{\omega(n)}
\]

choices: for every distinct prime, absent/present.

The full exponent-sensitive divisor family has

\[
C_{\mathrm{full}}(n)=\tau(n)=\prod_{p^e\Vert n}(e+1)
\]

choices.

Therefore

\[
\Delta_{\mathrm{bool}}=\omega(n)\ln2,
\qquad
\Delta_{\mathrm{full}}=\ln\tau(n),
\]

and the old thickness coordinate is exactly

\[
\boxed{
\Theta(n)
=\Delta_{\mathrm{full}}-\Delta_{\mathrm{bool}}
=\ln\frac{\tau(n)}{2^{\omega(n)}}.
}
\]

No analytic approximation is used in this identity. Its exact rational precursor is

\[
\frac{\tau(n)}{2^{\omega(n)}}
=\prod_{p^e\Vert n}\frac{e+1}{2}.
\]

Hence the old “support versus thickness” split is not two unrelated coordinates. It is a nested multiplicity tower:

```text
Boolean support multiplicity      2^omega
        -> exponent-sensitive multiplicity tau
        -> logarithmic surplus Theta = ln(tau/2^omega).
```

The squarefree atom receives a direct structural meaning:

\[
\Theta(n)=0
\iff
\tau(n)=2^{\omega(n)}
\iff
n\text{ is squarefree}.
\]

So the old \(6/\pi^2\) zero-thickness atom is exactly the population where exponent enrichment adds **no multiplicity beyond Boolean support**.

### 1.3 Exact BRC state compression

Substituting

\[
2^{\omega}e^\Theta=\tau,
\qquad
\frac\omega2-1+\Delta_1=H_1-1
\]

gives

\[
\boxed{
\operatorname{BRC}(n)=1+\tau(n)\bigl(H_1(n)-1\bigr).
}
\]

Thus the exact arithmetic observable itself needs only the pair

\[
\boxed{(\tau,H_1)}
\]

rather than the decomposed triple \((\omega,\Theta,\Delta_1)\), once the support/thickness decomposition is not itself the object being studied.

This is a real state reduction. The old coordinates remain useful because they diagonalize the asymptotic probability problem, but they are no longer mistaken for the minimal exact arithmetic state.

### 1.4 What did *not* improve

The new Foundation does not replace the Erdős--Kac or CRT/profinite argument.

The theorem that the growing support mode is asymptotically Gaussian and independent of the finite repeated-prime field still needs the same analytic/probabilistic input. The gain is semantic and algebraic:

- one common multiplicity language now generates both scales;
- the exact BRC state is smaller;
- the squarefree residual atom gets a precise forgetful-layer meaning.

**Regression verdict:** `STRONG STRUCTURAL GAIN / NO ANALYTIC BLOCKER REMOVAL`.

## 2. Regression B — width-one selector flips

### 2.1 Old reduction

For neighboring arms write

\[
R_-=\omega(n-1),\qquad R_+=\omega(n+1),\qquad d=R_--R_+.
\]

The old route introduced

\[
D_\Theta=\Theta_- -\Theta_+,
\qquad
D_\Delta=\Delta_{1,-}-\Delta_{1,+},
\]

and

\[
\rho_d=2^d e^{D_\Theta}.
\]

For fixed positive \(d\) and large common support scale, the support-predicted left arm is reversed when

\[
D_\Theta<-d\ln2,
\]

while the boundary atom

\[
D_\Theta=-d\ln2
\]

requires the secondary test

\[
D_\Delta<-\frac d2.
\]

### 2.2 Foundation retrofit: first coordinate disappears

Using

\[
\Theta=\ln\tau-\omega\ln2,
\]

we obtain exactly

\[
D_\Theta
=\ln\frac{\tau_-}{\tau_+}-d\ln2.
\]

Therefore

\[
\boxed{
\rho_d
=2^d e^{D_\Theta}
=\frac{\tau_-}{\tau_+}.
}
\]

The old exponential thickness comparison was simply total divisor-branch multiplicity comparison in disguised coordinates.

Consequently, on the same fixed-\(d>0\) limiting layer,

\[
D_\Theta<-d\ln2
\iff
\boxed{\tau_-<\tau_+},
\]

and

\[
D_\Theta=-d\ln2
\iff
\boxed{\tau_-=\tau_+}.
\]

### 2.3 Boundary coordinate also simplifies

Since

\[
\Delta_1=H_1-\frac\omega2,
\]

we have

\[
\frac d2+D_\Delta
=H_{1,-}-H_{1,+}.
\]

Hence the entire old limiting reversal event becomes

\[
\boxed{
E_d
=\{\tau_-<\tau_+\}
\cup
\{\tau_-=\tau_+,\ H_{1,-}<H_{1,+}\},
\qquad d>0.
}
\]

The previous `thickness exponential -> boundary thickness moment` cascade is therefore a direct two-coordinate comparison:

```text
first compare total branch multiplicity tau;
if tied, compare the exact secondary shape coordinate H_1.
```

This is a sharper result than merely renaming \(D_\Theta\). It removes one exponential/logarithmic intermediate variable and exposes the exact arithmetic meaning of the boundary atom.

### 2.4 Exact finite regression

The checker verifies over centers below 20,000 that

\[
2^d\frac{\tau_-/2^{R_-}}{\tau_+/2^{R_+}}
=\frac{\tau_-}{\tau_+}
\]

for every center, and checks the boundary identity

\[
\frac d2+D_\Delta=H_{1,-}-H_{1,+}
\]

whenever \(d>0\) and \(\tau_-=\tau_+\).

A minimal concrete multiplicity reversal is the center \(n=15\):

\[
n-1=14=2\cdot7,
\qquad
n+1=16=2^4.
\]

Then

\[
\omega(14)=2>1=\omega(16),
\]

so support count favors the left arm, but

\[
\tau(14)=4<5=\tau(16),
\]

so the first Weighted-BRC multiplicity correction reverses that ordering.

A first tie occurs at center \(n=7\):

\[
\tau(6)=\tau(8)=4,
\]

and the tie is resolved by

\[
H_1(6)=1>\frac34=H_1(8).
\]

### 2.5 True blocker remains

This compression does **not** prove the unconditional width-one flip constant.

The old obstacle was the probability mass of fixed integer layers

\[
\omega(n-1)-\omega(n+1)=d,
\]

at width one. That still requires the same marked local-limit / high-Fourier-frequency input adjacent to shifted Möbius/Chowla phenomena.

The new Foundation improves the **conditional event** dramatically but leaves the difficult **frequency of the event** unchanged.

**Regression verdict:** `STRONG EXACT STATE COMPRESSION / BLOCKER CLEANER BUT UNSOLVED`.

## 3. Regression C — oriented positive-axis holonomy

### 3.1 Old signed observable

The earlier path study defined

\[
\omega(x,y)=\det(x,y,\mathbf1),
\qquad
\Omega_2(\gamma)=\sum_{i<j}\omega(D_i,D_j).
\]

For the elementary positive-axis paths

\[
\gamma_+=(e_1,e_2,e_3),
\qquad
\gamma_-=(e_3,e_2,e_1),
\]

one has

\[
\Omega_2(\gamma_+)=+1,
\qquad
\Omega_2(\gamma_-)=-1.
\]

The two paths have the same canonical endpoint but opposite oriented holonomy.

### 3.2 Stress test: can positive Weighted BRC replace the signed observable?

Choose a positive scale \(\lambda>1\) and encode an individual path by

\[
w(\gamma)=\lambda^{\Omega_2(\gamma)}.
\]

For \(\lambda=2\), the two elementary paths have weights

\[
2,\qquad \frac12.
\]

Positive recoalescence gives

\[
(C,W,M)=\left(2,\frac52,2\right),
\qquad
E=\frac WM=\frac54.
\]

But globally reversing orientation simply swaps the two positive weights. The recoalesced CWM state is unchanged.

More generally for a pair \(+A,-A\),

\[
W=\lambda^A+\lambda^{-A},
\qquad
M=\lambda^{|A|},
\]

so

\[
E=1+\lambda^{-2|A|}
\]

depends on \(|A|\), not the sign of \(A\).

Therefore

\[
\boxed{
\text{positive CWM recoalescence cannot recover the reflection-odd sign of }\Omega_2.
}
\]

Projective/gauge scaling does not fix this. Multiplying both \(W\) and \(M\) by a common positive \(\mu\) leaves \(E=W/M\) unchanged, so it cleanly removes absolute scale but cannot recreate branch orientation after positive recoalescence erased it.

### 3.3 Where the new Foundation *does* help

Before recoalescence, if the two branch identities remain typed separately, log weights linearize the signed difference:

\[
\ln w(\gamma_+)-\ln w(\gamma_-)=2A\ln\lambda.
\]

Thus the new log/gauge layer can serve as a **scale transport coordinate around an already-retained oriented path carrier**.

It cannot replace that carrier after forgetful positive aggregation.

This pressure test therefore validates the Foundation hard boundary

```text
POSITIVE_WEIGHTED_BRC != SIGNED_AMPLITUDE_CANCELLATION
```

and shows that the older oriented holonomy result remains genuinely independent information.

**Regression verdict:** `USEFUL LAYERING CLARIFICATION / NO SUBSTITUTION / NEGATIVE BOUNDARY CONFIRMED`.

## 4. Comparative result

| Old research route | New-Foundation effect | What became smaller/clearer | What did not improve |
|---|---|---|---|
| one-arm support/thickness | strong | `Theta` becomes relative log multiplicity; exact BRC state compresses to `(tau,H_1)` | Erdős--Kac/CRT proof burden |
| width-one selector flip | very strong | `rho_d` becomes `tau_-/tau_+`; boundary becomes direct `H_1` comparison | fixed-difference local-limit/Chowla frontier |
| oriented holonomy | boundary result | gauge separates absolute positive scale; confirms signed information is a separate carrier | positive recoalescence cannot preserve orientation sign |

The important outcome is mixed rather than uniformly positive. The new Foundation is effective when the old problem is fundamentally about **branch multiplicity / positive mass**, and it correctly refuses to absorb a problem whose essential datum is **signed orientation**.

This is evidence that the new layer is typed narrowly enough to be useful without becoming a universal metaphor.

## 5. Next research target suggested by the regression

The strongest new lead is the arithmetic selector hierarchy

\[
\boxed{
2^{\omega(n)}\longrightarrow\tau(n)\longrightarrow H_1(n)\longrightarrow\operatorname{BRC}(n).
}
\]

The first arrow is exactly the Boolean-to-weighted multiplicity enrichment measured by \(\Theta\). The second coordinate resolves multiplicity ties relevant to the old width-one problem.

A natural next question is whether the fixed-difference local-limit problem becomes more tractable when stratified first by the exact integer multiplicity pair \((\tau_-,\tau_+)\) rather than by the real thickness variable \(D_\Theta\). No such local theorem is claimed here.

A second independent target is to combine the positive gauge coordinate with the existing signed holonomy carrier **before** recoalescence, keeping the type product explicit rather than attempting to encode sign into positive mass.

## 6. Exact checker

`experiments/brc_foundation_retrofit_check.py` verifies:

- exact divisor multiplicity/thickness factorization through `n<=10000`;
- squarefree iff no multiplicity enrichment beyond the Boolean skeleton in that range;
- exact collapse of the old BRC factorization to `1+tau(H_1-1)`;
- exact `rho_d=tau_-/tau_+` over centers below 20,000;
- exact boundary reduction `d/2+D_Delta=H_{1,-}-H_{1,+}` on multiplicity-tie layers;
- the elementary `Omega_2=+1/-1` oriented paths;
- exact positive CWM orientation erasure and projective `E=W/M` invariance.

All checks use integers and `Fraction`; no floating logarithm is used as evidence.
