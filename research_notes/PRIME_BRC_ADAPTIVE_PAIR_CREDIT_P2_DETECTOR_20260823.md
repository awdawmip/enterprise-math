# Prime-BRC Adaptive Pair-Credit P2 Detector

Status: `L3 OWNER-LOCAL / PROVED FINITE FACTOR-PATTERN THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Setup

Let

\[
I_K=\{n\in\mathbb N:K^2<n<(K+1)^2\},
\qquad X=(K+1)^2-1.
\]

Use Campbell's square-interval Richert parameters

\[
k_2=3.17,\qquad \lambda=4-k_2=0.83,
\]

with

\[
z=X^{1/8},\qquad y=X^{1/k_2}.
\]

For a prime \(p\ge z\), define the ordinary Richert single-prime charge

\[
g(p)=
\begin{cases}
1-\dfrac{\log p}{\log y},&p<y,\\
0,&p\ge y.
\end{cases}
\]

For a \(z\)-rough state \(n\in I_K\), write

\[
w_R(n)=\lambda-\sum_{p\mid n}g(p),
\]

where the sum is over distinct prime divisors.

Every composite \(n\in I_K\) has a prime divisor \(\le K\), and at most one prime divisor can exceed \(K\).

## 2. Adaptive pair credits

For distinct visible primes \(p<q\le K\), define

\[
c_{\rm low}(p,q)
=
[\lambda-g(p)-g(q)]_+
\qquad (pq\le K),
\]

and

\[
c_{\rm high}(p,q)
=
\left[
\frac{\lambda}{3}-\frac{g(p)+g(q)}2
\right]_+
\qquad (pq>K),
\]

where \([x]_+=\max(x,0)\).

For a repeated visible prime define

\[
c_{\rm rep}(p)=[\lambda-g(p)]_+.
\]

Define the Prime-BRC adaptive weight

\[
\boxed{
\begin{aligned}
w^\dagger(n)=w_R(n)
&-\sum_{\substack{p<q\le K\\pq\le K\\pq\mid n}}c_{\rm low}(p,q)\\
&-\sum_{\substack{p<q\le K\\pq>K\\pq\mid n}}c_{\rm high}(p,q)\\
&-\sum_{\substack{p\le K\\p^2\mid n}}c_{\rm rep}(p).
\end{aligned}}
\]

All added credits are nonnegative.

## 3. Main theorem

### Theorem — positive adaptive weight is a P2 certificate

For every \(z\)-rough \(n\in I_K\),

\[
\boxed{\Omega(n)\ge3\Longrightarrow w^\dagger(n)\le0.}
\]

Equivalently,

\[
\boxed{w^\dagger(n)>0\Longrightarrow \Omega(n)\le2.}
\]

No square-factor deletion set \(\mathcal A'\) is needed.

## 4. Proof

### 4.1 Any repeated prime

Assume \(p^2\mid n\) for some visible prime \(p\le K\). If \(w_R(n)\le0\) there is nothing to prove. Otherwise

\[
w_R(n)
=\lambda-\sum_{q\mid n}g(q)
\le\lambda-g(p)
=c_{\rm rep}(p).
\]

Hence the repeat credit alone makes \(w^\dagger(n)\le0\).

Thus it remains only to treat squarefree states.

### 4.2 Squarefree states with four or more prime factors

Let \(m=\Omega(n)\ge4\), and let \(t\) of the prime factors be below \(y\). Since every other prime factor is at least \(y=X^{1/k_2}\),

\[
\prod_{p<y,\,p\mid n}p
\le
\frac{X}{y^{m-t}}.
\]

Therefore

\[
\sum_{p<y,\,p\mid n}\frac{\log p}{\log y}
\le k_2-(m-t).
\]

Hence

\[
\begin{aligned}
w_R(n)
&=\lambda-t+
\sum_{p<y,\,p\mid n}\frac{\log p}{\log y}\\
&\le\lambda+k_2-m\\
&=4-m\le0.
\end{aligned}
\]

The extra Prime-BRC credits are nonnegative, so \(w^\dagger(n)\le0\).

### 4.3 Squarefree triprime with one large tail — A type

Write

\[
n=pqr,\qquad p<q\le K<r.
\]

Since \(r\ge K+1>\sqrt n\),

\[
pq=\frac nr<\sqrt n<K+1,
\]

so the integer product satisfies

\[
\boxed{pq\le K.}
\]

Also \(r> K>y\), hence \(g(r)=0\). Thus

\[
w_R(n)=\lambda-g(p)-g(q).
\]

The unique visible pair \((p,q)\) is a low pair, and its credit is exactly

\[
c_{\rm low}(p,q)=[w_R(n)]_+.
\]

Therefore \(w^\dagger(n)\le0\).

### 4.4 Squarefree fully-smooth triprime — B type

Write

\[
n=pqr,\qquad p<q<r\le K.
\]

For every pair, e.g. \(pq\),

\[
pq=\frac nr>\frac{K^2}{K}=K,
\]

and similarly

\[
pr>K,\qquad qr>K.
\]

Thus all three visible pairs are high pairs.

Before taking positive parts, their three symmetric pair credits sum to

\[
\begin{aligned}
&\left(\frac\lambda3-\frac{g(p)+g(q)}2\right)
+\left(\frac\lambda3-\frac{g(p)+g(r)}2\right)
+\left(\frac\lambda3-\frac{g(q)+g(r)}2\right)\\
&=\lambda-g(p)-g(q)-g(r)\\
&=w_R(n).
\end{aligned}
\]

Replacing any negative summand by zero can only increase the total credit. Hence the three high-pair credits are at least \(w_R(n)\) whenever \(w_R(n)>0\), and again

\[
w^\dagger(n)\le0.
\]

This completes the proof.

## 5. Exact semantic gain over ordinary Richert weighting

The new carrier distinguishes two missing pieces that the ordinary distinct-prime Richert weight does not retain:

1. **pair interaction:** whether two visible prime branches coexist, and whether their product lies below or above the square-root threshold \(K\);
2. **repeat event:** whether one visible branch occurs with exponent at least two.

Prime and semiprime states in an open square basin incur no added penalty:

- prime: no visible pair and no repeated branch;
- semiprime: necessarily \(n=pq\) with \(p\le K<q\), so there is only one visible branch and no square factor because there are no integer squares strictly between consecutive squares.

Thus the added state is exactly targeted at \(\Omega\ge3\).

## 6. Aggregate analytic form

Summing over the \(z\)-rough basin gives

\[
\sum_n w^\dagger(n)
=W_R
-T_{\rm low}
-T_{\rm high}
-T_{\rm rep},
\]

where

\[
T_{\rm low}
=\sum_{\substack{z\le p<q\le K\\pq\le K}}
 c_{\rm low}(p,q)\,S(\mathcal A_{pq},\mathcal P,z),
\]

\[
T_{\rm high}
=\sum_{\substack{z\le p<q\le K\\pq>K}}
 c_{\rm high}(p,q)\,S(\mathcal A_{pq},\mathcal P,z),
\]

and

\[
T_{\rm rep}
=\sum_{z\le p\le K}c_{\rm rep}(p)\,S(\mathcal A_{p^2},\mathcal P,z).
\]

This is the exact remaining analytic problem for an explicit P2 theorem.

The new terms are pair/square upper-bound terms. No lower-bound detection of primes is introduced at this layer.

## 7. BRC interpretation

The theorem realizes the following information flow:

```text
ordinary Richert scalar credit
        +
visible pair interaction (low/high relative to K)
        +
repeat-event bit
        ↓
P2-safe signed credit
```

The A/B triprime distinction is not an externally imposed class label: it is exactly the square-basin divisor-frontier distinction

\[
pq\le K \quad\text{versus}\quad pq>K.
\]

The three B-type pair credits form a symmetric interaction decomposition whose untruncated sum is exactly the original Richert residual credit.

## 8. Boundaries

This theorem does **not** prove an explicit P2 result by itself. It reduces P2 to upper bounds for the three aggregate switching terms above.

It also does not address the final P2 -> P1 parity barrier. Semiprime states deliberately pay no additional pair/repeat penalty.

Freeze:

`PRIME_BRC_ADAPTIVE_PAIR_REPEAT_WEIGHT_IS_P2_SOUND = true`.

`P2_ANALYTIC_SWITCHING_TERMS_REMAIN_OPEN = true`.

`P2_TO_P1_NOT_SOLVED = true`.
