# Prime-power spectral Eisenstein factors and Frobenius congruences

Status: `FREE_RESEARCH / EXACT FINITE p-ADIC SPECTRAL THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- projective primitive factors `Omega_d`;
- prime Frobenius congruence `R_p(v) congruent v^p mod p`;
- projective denominator-Frobenius recursion;
- primitive mass law.

## 1. Prime projective factor from a critical-value fiber

Let `p` be an odd prime.  The odd-length critical-value factorization gives

\[
\boxed{
R_p(v)=v\,\Omega_p(v)^2.
}
\tag{PE-1}

Indeed the nonzero roots in the zero-critical-value fiber are exactly the complement-paired primitive denominator-`p` roots, each with critical multiplicity two.

Modulo `p`,

\[
R_p(v)\equiv v^p.
\]

Therefore

\[
v\Omega_p(v)^2
\equiv v^p\pmod p,
\]

and cancellation in `F_p[v]` gives

\[
\Omega_p(v)^2
\equiv v^{p-1}\pmod p.
\]

Since `Omega_p` is monic of degree `(p-1)/2`,

\[
\boxed{
\Omega_p(v)
\equiv v^{(p-1)/2}\pmod p.
}
\tag{PE-2}

Thus every nonleading coefficient is divisible by `p`.

The primitive mass law gives

\[
|\Omega_p(0)|=p,
\]

so the constant coefficient is divisible by `p` but not by `p^2`.

Hence

\[
\boxed{
\Omega_p\text{ is }p\text{-Eisenstein}.
}
\tag{PE-3}

---

## 2. Odd prime powers

Let `a>=2`.  Because `p|p^(a-1)`, the projective Frobenius law has only one denominator preimage:

\[
\widehat\Omega_{p^{a-1}}(R_p(v))
=
\widehat\Omega_{p^a}(v).
\]

For monic normalization and odd `p`, `R_p` is itself monic, and both primitive factors have constant magnitude `p`.  Therefore the normalized identity lifts to the exact monic recursion

\[
\boxed{
\Omega_{p^a}(v)
=
\Omega_{p^{a-1}}(R_p(v)).
}
\tag{PE-4}

Iterating,

\[
\boxed{
\Omega_{p^a}(v)
=
\Omega_p(R_p^{\circ(a-1)}(v)).
}
\tag{PE-5}

Reduce (PE-4) modulo `p`.  Using `R_p(v) congruent v^p` and the induction hypothesis,

\[
\begin{aligned}
\Omega_{p^a}(v)
&\equiv
\left(v^p\right)^{\varphi(p^{a-1})/2}\\
&=v^{\varphi(p^a)/2}
\pmod p.
\end{aligned}
\]

Thus

\[
\boxed{
\Omega_{p^a}(v)
\equiv v^{\varphi(p^a)/2}\pmod p.
}
\tag{PE-6}

Again the constant coefficient has magnitude exactly `p`, so

\[
\boxed{
\Omega_{p^a}\text{ is }p\text{-Eisenstein}
\qquad(p\text{ odd prime}).
}
\tag{PE-7}

---

## 3. Powers of two

The first nontrivial projective factor is

\[
\Omega_4(v)=v-2,
\]

which is `2`-Eisenstein.

For `a>=3`, the same denominator recursion uses `R_2(v)=v(4-v)`, whose leading sign is negative but whose reduction is

\[
R_2(v)\equiv v^2\pmod2.
\]

After the monic sign normalization one gets inductively

\[
\boxed{
\Omega_{2^a}(v)
\equiv v^{2^{a-2}}\pmod2,
}
\tag{PE-8}

while

\[
|\Omega_{2^a}(0)|=2.
\]

Hence

\[
\boxed{
\Omega_{2^a}\text{ is }2\text{-Eisenstein}
\qquad(a\ge2).
}
\tag{PE-9}

---

## 4. Unified prime-power theorem

For every prime power `q=p^a>2`,

\[
\boxed{
\Omega_q(v)
\equiv v^{\varphi(q)/2}\pmod p,
}
\tag{PE-10}

and

\[
\boxed{
|\Omega_q(0)|=p.
}
\tag{PE-11}

Therefore

\[
\boxed{
\Omega_{p^a}\text{ is }p\text{-Eisenstein for every }p^a>2.
}
\tag{PE-12}

This supplies a direct `p`-adic irreducibility proof in the prime-power sector, independent of the general discriminant/Frobenius transitivity proof.

---

## 5. General prime-extension congruence

For `d>2` and a prime `p` with `p \nmid d`, the projective Frobenius law is

\[
\widehat\Omega_d(R_p(v))
=
\widehat\Omega_d(v)\widehat\Omega_{pd}(v).
\]

Modulo `p`, `R_p(v) congruent v^p`.  Whenever the constant normalization of `Omega_d` is a `p`-adic unit, the identity gives the residue-field congruence

\[
\boxed{
\widehat\Omega_{pd}(v)
\equiv
\widehat\Omega_d(v)^{p-1}
\pmod p.
}
\tag{PE-13}

When `p|d`, the single-preimage law gives instead the Frobenius-type congruence

\[
\boxed{
\widehat\Omega_{pd}(v)
\equiv
\widehat\Omega_d(v)^p
\pmod p
}
\tag{PE-14}

in any normalization where reduction is defined.

These are spectral analogues of the familiar prime-extension congruences for cyclotomic-type factors, obtained here from finite denominator decimation.

---

## 6. Local ramification meaning

The Eisenstein theorem implies that for `q=p^a>2`, adjoining one projective primitive root `alpha_q` of `Omega_q` gives a totally ramified extension at `p` of degree

\[
\boxed{\varphi(q)/2}
\]

at the local field level after choosing a prime above `p`.

This matches the projective root-block degree exactly.

The statement is a standard consequence of Eisenstein once the polynomial theorem is known; no broader claim about the complete global Galois group is made here.

---

## 7. Research consequence

The prime-power spectral sector now carries an explicit arithmetic package:

```text
prime decimation R_p
  -> R_p(v) = v^p mod p
  -> projective primitive recursion
  -> Omega_(p^a)(v) = pure top monomial mod p
  -> constant term exactly p
  -> p-Eisenstein
  -> total local ramification
```

This gives a concrete entry point for the open question raised by the spectral Riccati sequence: whether `p`-adic information in the finite primitive factors can constrain the valuations/numerators of the universal completion coefficients `beta_n` without importing Bernoulli theory first.

Freeze:

`PRIME_POWER_PROJECTIVE_SPECTRAL_FACTOR = p-EISENSTEIN`.

`PRIME_DECIMATION_FROBENIUS_CONGRUENCE -> LOCAL_SPECTRAL_RAMIFICATION`.
