# Weighted/Log BRC Foundation Retrofit — Old-Research Regression

Status: `RESEARCH REGRESSION / EXACT ALGEBRAIC RECHECK + BOUNDARY TEST`
Date: `2026-09-02`
Researcher-ID: `EM-STW-B9F4C2`
Foundation baseline: `main@ba9e8fb6801d30406bccc3df7f7693263b12c861`
Foundation input: `definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md`

## 0. Question

After promoting the positive Weighted/Log BRC layer into the current research Foundation, does re-running older research actually improve anything?

Four deliberately different prior routes were selected:

1. the full unsieved BRC support/thickness two-scale decomposition;
2. the width-one neighboring-arm selector-flip reduction;
3. the oriented positive-axis holonomy cocycle;
4. P001 exact integer-root multiplicativity as a deterministic negative control.

The regression criterion is not “can the new language restate the old result?” It asks whether the new Foundation removes redundant state, reveals a stronger exact identity, shortens the proof/interface, moves the true blocker to a cleaner boundary, or correctly reports no gain/non-applicability.

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

The probabilistic two-scale theorem separated the growing distinct-prime support mode from the \(O(1)\) repeated-prime thickness field.

### 1.2 Foundation retrofit

The Boolean squarefree skeleton has

\[
C_{\mathrm{bool}}(n)=2^{\omega(n)}
\]

equal-weight choices, while the full exponent-sensitive divisor family has

\[
C_{\mathrm{full}}(n)=\tau(n)=\prod_{p^e\Vert n}(e+1).
\]

Because equal \(k\)-branch recoalescence has log multiplicity surplus \(\ln k\),

\[
\Delta_{\mathrm{bool}}=\omega(n)\ln2,
\qquad
\Delta_{\mathrm{full}}=\ln\tau(n),
\]

and therefore

\[
\boxed{
\Theta(n)
=\Delta_{\mathrm{full}}-\Delta_{\mathrm{bool}}
=\ln\frac{\tau(n)}{2^{\omega(n)}}.
}
\]

The exact rational precursor is

\[
\frac{\tau(n)}{2^{\omega(n)}}
=\prod_{p^e\Vert n}\frac{e+1}{2}.
\]

Thus the old “support versus thickness” split is a nested multiplicity tower:

```text
Boolean support multiplicity 2^omega
        -> exponent-sensitive multiplicity tau
        -> relative log multiplicity Theta = ln(tau/2^omega).
```

The squarefree atom receives a direct structural meaning:

\[
\Theta(n)=0
\iff
\tau(n)=2^{\omega(n)}
\iff
n\text{ is squarefree}.
\]

So the old \(6/\pi^2\) zero-thickness atom is exactly the population where exponent enrichment adds no multiplicity beyond Boolean support.

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

Hence, when the support/thickness decomposition is not itself the observable, the exact arithmetic BRC value factors through the smaller pair

\[
\boxed{(\tau,H_1)}
\]

rather than the decomposed triple \((\omega,\Theta,\Delta_1)\).

The old coordinates remain useful because they diagonalize the asymptotic probability problem; the new Foundation clarifies that they are not the minimal exact arithmetic state.

### 1.4 What did not improve

The new Foundation does not replace the Erdős--Kac or CRT/profinite argument. The Gaussian/support-thickness independence theorem still needs the same analytic/probabilistic input.

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

while the boundary atom requires

\[
D_\Theta=-d\ln2,
\qquad
D_\Delta<-\frac d2.
\]

### 2.2 Foundation retrofit: first coordinate disappears

Since

\[
\Theta=\ln\tau-\omega\ln2,
\]

we obtain exactly

\[
D_\Theta
=\ln\frac{\tau_-}{\tau_+}-d\ln2,
\]

hence

\[
\boxed{
\rho_d
=2^d e^{D_\Theta}
=\frac{\tau_-}{\tau_+}.
}
\]

The old exponential thickness comparison was total divisor-branch multiplicity comparison in disguised coordinates.

Therefore, on the same fixed-\(d>0\) limiting layer,

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

Because

\[
\Delta_1=H_1-\frac\omega2,
\]

we have

\[
\boxed{
\frac d2+D_\Delta
=H_{1,-}-H_{1,+}.
}
\]

Thus the old limiting reversal event becomes

\[
\boxed{
E_d
=\{\tau_-<\tau_+\}
\cup
\{\tau_-=\tau_+,\ H_{1,-}<H_{1,+}\},
\qquad d>0.
}
\]

The old cascade is therefore the direct two-coordinate rule

```text
compare total branch multiplicity tau;
if tied, compare exact secondary shape H_1.
```

### 2.4 Concrete regression witnesses

A minimal multiplicity reversal occurs at center \(n=15\):

\[
14=2\cdot7,
\qquad
16=2^4.
\]

Although

\[
\omega(14)=2>1=\omega(16),
\]

we have

\[
\tau(14)=4<5=\tau(16).
\]

Thus Boolean support favors the left arm while exponent-sensitive branch multiplicity reverses the first comparison.

A first multiplicity tie occurs at center \(n=7\):

\[
\tau(6)=\tau(8)=4,
\]

and the tie is resolved by

\[
H_1(6)=1>\frac34=H_1(8).
\]

### 2.5 True blocker remains

The old obstacle was the probability mass of fixed integer layers

\[
\omega(n-1)-\omega(n+1)=d
\]

at width one. That still requires the same marked local-limit/high-Fourier-frequency input adjacent to shifted Möbius/Chowla phenomena.

The Foundation compresses the **conditional event** but does not determine its **frequency**.

**Regression verdict:** `STRONG EXACT STATE COMPRESSION / BLOCKER CLEANER BUT UNSOLVED`.

## 3. Regression C — oriented positive-axis holonomy

### 3.1 Old signed observable

The earlier path study defined

\[
\omega(x,y)=\det(x,y,\mathbf1),
\qquad
\Omega_2(\gamma)=\sum_{i<j}\omega(D_i,D_j).
\]

For

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

The paths have the same canonical endpoint but opposite oriented holonomy.

### 3.2 Can positive Weighted BRC replace it?

Choose \(\lambda>1\) and encode an individual path by

\[
w(\gamma)=\lambda^{\Omega_2(\gamma)}.
\]

For \(\lambda=2\), the elementary pair has positive weights

\[
2,\qquad\frac12.
\]

Recoalescence gives

\[
(C,W,M)=\left(2,\frac52,2\right),
\qquad
E=\frac WM=\frac54.
\]

Global orientation reversal swaps the two positive weights, so the recoalesced CWM state is unchanged.

More generally, a pair \(+A,-A\) gives

\[
W=\lambda^A+\lambda^{-A},
\qquad
M=\lambda^{|A|},
\qquad
E=1+\lambda^{-2|A|},
\]

which depends on \(|A|\), not the sign of \(A\).

Therefore

\[
\boxed{
\text{positive CWM recoalescence cannot recover the reflection-odd sign of }\Omega_2.
}
\]

Projective/gauge scaling removes absolute positive scale but cannot recreate orientation after positive aggregation erased it.

Before recoalescence, if branch identity remains typed, log weights can still linearize the signed difference:

\[
\ln w(\gamma_+)-\ln w(\gamma_-)=2A\ln\lambda.
\]

So the new layer is useful **around** the signed carrier, not **instead of** it.

**Regression verdict:** `USEFUL LAYERING CLARIFICATION / NO SUBSTITUTION / NEGATIVE BOUNDARY CONFIRMED`.

## 4. Regression D — P001 integer-root multiplicativity negative control

P001 is an exact deterministic threshold/carry theorem. For

\[
r=R_p(a),\quad s=R_p(b),\quad
u=a-r^p,\quad v=b-s^p,
\]

its core criterion is

\[
R_p(ab)=rs
\iff
s^p\nu+r^p v+\nu v<\Delta_p(rs).
\]

There is one deterministic result path, not a family of positive alternative branches whose recoalescence is part of the theorem.

If that unique evaluation path is assigned unit positive weight, its CWM state is simply

\[
(C,W,M)=(1,1,1),
\]

so

\[
E=\frac WM=1,
\qquad
\Delta=\ln E=0.
\]

Therefore the new Foundation contributes **no new mathematical state** to P001 and should not be inserted into its proof. The exact carry load, basin width and floor/root Galois structure remain the correct sufficient coordinates.

The regression checker re-verifies the P001 no-carry equivalence on 10,000 small \((p,a,b)\) cases and simultaneously confirms the Weighted-BRC surplus is identically zero for the unique path.

This is a successful negative control: the new Foundation does not become a universal wrapper around every Enterprise Math problem.

**Regression verdict:** `NO GAIN EXPECTED / TYPE SYSTEM CORRECTLY DEACTIVATES WEIGHTED LAYER`.

## 5. Comparative result

| Old research route | New-Foundation effect | What became smaller/clearer | What did not improve |
|---|---|---|---|
| one-arm support/thickness | strong | `Theta` becomes relative log multiplicity; exact BRC state compresses to `(tau,H_1)` | Erdős--Kac/CRT proof burden |
| width-one selector flip | very strong | `rho_d` becomes `tau_-/tau_+`; boundary becomes direct `H_1` comparison | fixed-difference local-limit/Chowla frontier |
| oriented holonomy | boundary result | gauge separates absolute positive scale; signed information is confirmed as separate | positive recoalescence cannot preserve orientation sign |
| P001 integer root | deliberately none | typed applicability is clearer | the exact carry theorem is unchanged, as it should be |

The mixed result is the desired outcome. The Foundation is effective when the old problem is fundamentally about **branch multiplicity/positive mass**, and it correctly switches off or stops at a boundary when the essential datum is **signed orientation** or **single-valued deterministic carry**.

This is evidence that the extension is narrow enough to be a research foundation rather than a universal metaphor.

## 6. Next research targets suggested by the regression

The strongest new lead is the arithmetic selector hierarchy

\[
\boxed{
2^{\omega(n)}\longrightarrow\tau(n)\longrightarrow H_1(n)\longrightarrow\operatorname{BRC}(n).
}
\]

The first arrow is exactly the Boolean-to-weighted multiplicity enrichment measured by \(\Theta\); the second coordinate resolves multiplicity ties relevant to the old width-one route.

A natural next question is whether the fixed-difference local-limit problem becomes more tractable when stratified first by the exact integer multiplicity pair \((\tau_-,\tau_+)\) rather than by the real variable \(D_\Theta\). No such theorem is claimed here.

A second independent target is to combine the positive gauge coordinate with the existing signed holonomy carrier **before** recoalescence, keeping the type product explicit rather than attempting to encode sign into positive mass.

## 7. Exact checker

`experiments/brc_foundation_retrofit_check.py` verifies:

- exact divisor multiplicity/thickness factorization through `n<=10000`;
- squarefree iff no multiplicity enrichment beyond the Boolean skeleton in that range;
- exact collapse of the old BRC factorization to `1+tau(H_1-1)`;
- exact `rho_d=tau_-/tau_+` over centers below 20,000;
- exact boundary reduction `d/2+D_Delta=H_{1,-}-H_{1,+}` on multiplicity-tie layers;
- the elementary `Omega_2=+1/-1` oriented paths;
- exact positive CWM orientation erasure and projective `E=W/M` invariance;
- P001 no-carry equivalence over degrees `1..4` and inputs `1..50`, together with the single-path `E=1` negative control.

All checks use integers and `Fraction`; no floating logarithm is used as evidence.
