# P022 Barlow — Common conductor-18 datum after three-section

Status: **PROVED_WIP / exact structural reduction / nonvanishing still open**  
Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-2346F5D3E731ED56DB0A`

## 1. Starting point

The current boundary obstruction is

\[
W_{3m}\equiv0\pmod q,
\qquad q=18m-1,
\]

where

\[
W_M=\sum_{j=0}^{2M-1}
\binom{2M}{j}\binom{M+j}{j}\binom{2M-1}{j}.
\]

Put `M=3m` and write

\[
w_j=\binom{6m}{j}\binom{3m+j}{j}\binom{6m-1}{j}.
\]

Then

\[
W_{3m}=\sum_{a=0}^2 W_m^{(a)},
\qquad
W_m^{(a)}=\sum_{k=0}^{2m-1}w_{3k+a}.
\]

All three residue sections have exactly `2m` terms.  There is no asymmetric
short tail.

## 2. Triplication parameters

Using

\[
w_j=\frac{(-6m)_j(1-6m)_j(3m+1)_j}{(j!)^3},
\]

and

\[
(x)_{3k}=3^{3k}(x/3)_k((x+1)/3)_k((x+2)/3)_k,
\]

each section becomes a terminating `9F8(1)` after factoring out its first
term `w_a`.

The three exact parameter sets differ by integer contiguous shifts.  At the
live prime boundary

\[
18m\equiv1\pmod q,
\]

so `m` may be replaced by `1/18` at the parameter level modulo `q`.  Reducing
all parameters modulo integers gives the **same** upper signature for all
three sections:

\[
\boxed{
\alpha_{18}=
\left\{
\frac1{18},\frac7{18},\frac{13}{18},
\frac29,\frac29,
\frac59,\frac59,
\frac89,\frac89
\right\}.
}
\]

Including the standard hypergeometric `k!` lower parameter, the common lower
signature is

\[
\boxed{
\beta_{18}=
\left\{
0,0,0,
\frac13,\frac13,\frac13,
\frac23,\frac23,\frac23
\right\}.
}
\]

Thus the three sections are not three unrelated finite sums.  They are three
contiguous realizations of one conductor-18 rank-nine cyclotomic datum.

A useful organization is

\[
\alpha_{18}
=
\left(\frac1{18}+\left\{0,\frac13,\frac23\right\}\right)
\sqcup
2\left(\frac29+\left\{0,\frac13,\frac23\right\}\right),
\]

while

\[
\beta_{18}=3\left\{0,\frac13,\frac23\right\}.
\]

So the entire signature is built from cubic orbits.

## 3. Frobenius/Dwork period

The target prime satisfies

\[
q\equiv-1\pmod{18}.
\]

For a rational parameter `a` of denominator dividing 18, Dwork dash at a prime
`q=-1 (mod 18)` acts on the fractional part by

\[
a\longmapsto1-a.
\]

Hence the conjugate upper signature is

\[
\alpha_{18}^{\vee}=
\left\{
\frac5{18},\frac{11}{18},\frac{17}{18},
\frac19,\frac19,
\frac49,\frac49,
\frac79,\frac79
\right\},
\]

and

\[
\beta_{18}^{\vee}=\beta_{18}.
\]

Applying dash twice returns the original datum:

\[
\boxed{
(\alpha_{18},\beta_{18})
\leftrightarrow
(\alpha_{18}^{\vee},\beta_{18})
}
\]

is a period-two orbit.

This upgrades the earlier informal root-of-unity observation: the special
boundary `q=18m-1` naturally raises the cyclotomic conductor from the visible
cubic section to 18, and Frobenius is complex conjugation on that conductor.

## 4. Relation with the root-of-unity filter

Let

\[
P_M(z)=\sum_{j=0}^{2M-1}w_jz^j.
\]

Over `F_(q^2)` choose `omega^2+omega+1=0`.  Then

\[
W_m^{(a)}=\frac13\sum_{t=0}^2\omega^{-at}P_M(\omega^t).
\]

Since `q=5 (mod 6)`, Frobenius exchanges `omega` and `omega^2`.  The rank-nine
period-two dash orbit above is therefore compatible with the elementary
three-section Frobenius pair rather than being a separate numerical pattern.

## 5. What this does and does not prove

It proves:

1. all three residue sections have equal length `2m`;
2. all three share one exact cyclotomic parameter signature modulo `q`;
3. that signature has conductor 18 and a period-two Dwork orbit at the target
   primes;
4. the next finite-field proof may be organized on one common motive plus
   contiguous operators, rather than three independent `9F8` sums.

It does **not** yet prove

\[
W_{3m}\not\equiv0\pmod{18m-1}.
\]

The remaining target is to compute the contiguous transfer among the three
sections inside this common period-two system and show that the sum functional
cannot annihilate the admissible Frobenius vector.  A finite census is not a
substitute for that step.
