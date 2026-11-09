# D25 — finite-log carry reconstruction of every original Gauss-overflow coefficient mod p²

Date 2026-11-10. TASK_RESEARCH, same logical onhour Research lane `chatgpt-research-onhour-enterprise-math-20260923`; NOT the maintenance lane. AUTHOR-PROVED CONDITIONAL ON PRIOR AUTHOR-SIDE REFLECTION / FIVE EXACT POLYNOMIAL CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. Parent Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`.

## 1. Direct target and original definitions

Fix any prime `p≡13 (mod24)`; work in `Z_(p)[X]`. Keep the original truncated series

```
F_p(z)=sum_{k=0}^{p-1} (1/8)_k(3/8)_k/(k!)² * z^k
G_p(X)=sum_{k=0}^{p-1} (1/4)_k(3/4)_k/(k!)² * X^k.
```

Their exact finite quadratic transform (preceding author-side derivation) defines `E_p` of degree at most `p-2` by

```
F_p(4X(1-X))=G_p(X)+X^p E_p(X).
```

The **load-bearing declared dependency** is the prior all-prime second-digit anti-reflection `G_p(1-X)=-G_p(X) (mod p²)`, previously author-proved using terminating Legendre polynomials (not independently admitted). This run independently checked its exact coefficient consequences for five selected primes.

## 2. New all-prime finite-log first-jet reconstruction

Define the universal integral binomial-carry polynomial

```
C_p(X)=((1-X)^p-1+X^p)/p.
```

It has degree `p-1`, vanishes at `X=0`, and modulo p satisfies

```
C_p(X) = -sum_{j=1}^{p-1} X^j/j.
```

Let `L_p(X)=sum_{j=1}^{p-1} X^j/j` in `F_p[X]`, and let the truncation `[P(X)]_<p` retain exactly degrees 0 to p-1. Set

```
A_p(X)=[ L_p(X) * (G_p(X) mod p) ]_<p .
```

**Theorem (conditional only on the above explicit anti-reflection):** in `(Z/p²Z)[X]`, coefficientwise for all indices,

```
             E_p(X) = -2 G_p(X) + 2p A_p(1-X)  (mod p²).
```

The formula reconstructs the entire original, signed, high-degree Gauss-transform overflow from the low-degree finite Gauss polynomial and a single explicit finite-log carry operator. It is a polynomial congruence, not merely a special-value identity. It retains the `p²` digit needed by the current CM overflow target.

**Proof.** The exact `F_p(4X(1-X))` is symmetric under `X→1-X`; with the declared anti-reflection,

```
2G_p(X)=(1-X)^p E_p(1-X)-X^pE_p(X)   (mod p²).
```

Reduce mod p and use `(1-X)^p=1-X^p`. Since `deg E_p≤p-2`, comparing degrees less than p gives `E_p(1-X)=2G_p(X)` modulo p and hence `E_p(X)=-2G_p(X)` modulo p. The coefficientwise quotient `H_p=(E_p+2G_p)/p` is therefore integral mod p. Substitute `E_p=-2G_p+pH_p` into the symmetric identity, divide by p and use the exact binomial carry:

```
X^p(H_p(X)+H_p(1-X))-H_p(1-X) = 2 C_p(X) G_p(X)  (mod p).
```

The first term has no coefficient of degree less than p; therefore

```
H_p(1-X)=-2[C_p(X)*(G_p(X) mod p)]_<p
          = 2 A_p(X)  (mod p).
```

Substitute `X→1-X`. The displayed theorem follows. The high-degree part of the same identity imposes a consistency relation (not an extra assumption). No formal logarithm beyond the finite polynomial `L_p` is used.

## 3. New scalar target without double-overflow convolution

Take the same auxiliary quadratic ring and original observer as the preceding author-side overflow study:

```
s=(3-2√2)/6,  σ(s)=1-s,  Tr(z)=z+σ(z),
G_p(s)=p*g_p*√2 (mod p²),
S_p=Tr(E_p(s)).
```

Anti-reflection implies `Tr(G_p(s))=0 (mod p²)`. Apply the full-polynomial theorem and trace:

```
       S_p/p = 2 Tr(A_p(s))  (mod p).
```

The original still-open target `S_p=48p*g_p (mod p²)` is therefore **equivalent** to one finite-log/Hasse trace condition

```
              Tr(A_p(s)) = 24*g_p  (mod p).
```

This keeps the odd-coordinate `g_p`, all original signs, and the exact p² carry. Compared with the preceding signed coefficient double-sum, it gives a direct O(p²) field-polynomial reconstruction, and makes the next proof obligation a *single explicit finite-log/Hasse pairing* rather than another unsigned norm or repeated prime survey. As before, this does not execute or replace the native original H0/B0 experiment.

## 4. Actual independent checks

The accompanying standard-library Python code independently constructs original `f_k`, original overflow coefficients by their raw binomial `k,j` sum, the separate Gauss recurrence `g_k`, verifies **every** coefficient of `G(1-X)+G(X)` mod p², reconstructs **every** `E_p` coefficient using the truncated finite-log product and binomial substitution, and checks the scalar trace.

| p | E coefficients checked | S_p/p | Tr(A_p(s)) |
|---:|---:|---:|---:|
|13|13|1|7|
|37|37|1|19|
|61|61|16|8|
|109|109|54|27|
|373|373|298|149|

All checks PASS. At `p=373`, `S_p=111154 mod139129` and `Tr(A_p(s))=149=24*115 mod373`, matching the pre-existing `g_373=115`. This is a new independent path to the pre-existing `u_373=149`, not a new native H0/B0 observation.

## 5. BRC and next scientific obligation

BRC COMPOSE_APPLIED: the signed original overflow carrier and sigma-even / sigma-odd observers are preserved; the finite-log map is an exact reconstructive observer through modulus p², not a mere total-only summary. Polynomial equality certifies preservation for subsequent polynomial evaluations in this stated ring/precision. The quadratic auxiliary coordinates are not the native six-axis space.

**Next direct step:** prove `Tr(A_p(s))=24g_p` for every target prime using the explicit `L_p(X) G_p(X)` truncated product and CM Hasse polynomial, or produce a valid counterexample; do not redo already-proven raw-band and finite-reflection identities. The original AF4/Delta−R LIFT remains OPEN. Separately the original same-class H0/B0 native p373 `[X]U mod139129`, Frobenius direction/eta, rank, κ, Delta−R and independent reproduction remain OPEN under Issue #1559, with no verified executor.

This is source-preserving author-side mathematics, not a Source Result, checkpoint, accepted theorem or claim. Predecessors: `20261110_onhour_d25_CM_overflow_scalar_trace_reflection.md` (reflection/trace), `20261110_onhour_d25_CM_overflow_valuation_band_firstjet.md` (new exact p-adic coefficient bands). Source-native durable frontier remains `b58330b74576153cdadde5d80a3d92df3a819a0e`.
