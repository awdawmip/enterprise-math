# Frobenius collapse of p-adic primitive spectral levels

Status: `FREE_RESEARCH / EXACT MOD-p FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- prime phase polynomial congruence `R_p(u)=u^p mod p`;
- primitive pullback semigroup.

## 1. Prime phase map becomes Frobenius

For every prime `p`, the integer phase-multiplication polynomial satisfies

\[
\boxed{R_p(u)\equiv u^p\pmod p.}
\tag{FCL-1}

By composition,

\[
\boxed{R_{p^a}(u)\equiv u^{p^a}\pmod p.}
\tag{FCL-2}

Thus finite phase multiplication reduces to ordinary Frobenius on the spectral coordinate in characteristic `p`.

## 2. New-prime first step

Assume `p\nmid m`.  The primitive pullback identity is

\[
\operatorname{Monic}(\Psi_m(R_p))=\Psi_m\Psi_{mp}.
\]

Modulo `p`,

\[
\Psi_m(R_p(u))
\equiv\Psi_m(u^p)
\equiv\Psi_m(u)^p.
\]

Cancel `Psi_m` in the polynomial domain `F_p[u]`:

\[
\boxed{
\Psi_{mp}(u)
\equiv\Psi_m(u)^{p-1}\pmod p.
}
\tag{FCL-3}

## 3. Deeper levels when p was initially absent

After the first step, `p` divides the denominator.  Apply the present-prime pullback recursively.  Induction gives

\[
\boxed{
\Psi_{mp^a}(u)
\equiv
\Psi_m(u)^{p^{a-1}(p-1)}\pmod p,
\qquad p\nmid m,\ a\ge1.
}
\tag{FCL-4}

The degree identity

\[
\varphi(mp^a)=p^{a-1}(p-1)\varphi(m)
\]

shows that (FCL-4) accounts for the full polynomial degree.

## 4. Deeper levels when p is already present

If `p|m`, the prime pullback has only the deeper channel:

\[
\operatorname{Monic}(\Psi_m(R_p))=\Psi_{mp}.
\]

Modulo `p`, this gives

\[
\Psi_{mp}(u)\equiv\pm\Psi_m(u)^p.
\]

Iterating,

\[
\boxed{
\Psi_{mp^a}(u)
\equiv
\pm\Psi_m(u)^{p^a}\pmod p,
\qquad p\mid m.
}
\tag{FCL-5}

The sign only reflects the monic convention when the phase polynomial has leading coefficient `-1`; it does not affect support or p-divisibility.

Again

\[
\varphi(mp^a)=p^a\varphi(m).
\]

## 5. Support collapse versus multiplicity depth

Equations (FCL-4)--(FCL-5) imply that all primitive factors on one `p`-adic denominator ray have the same reduced polynomial support modulo `p`; deeper levels differ only through Frobenius multiplicity.

Schematically,

```text
characteristic zero:
Psi_m, Psi_(mp), Psi_(mp^2), ...
    = distinct primitive spectral levels

mod p:
Psi_m,
Psi_m^(...),
Psi_m^(...), ...
    = one support with increasing Frobenius thickness
```

Thus

\[
\boxed{
\text{P-ADIC DEPTH}
\xrightarrow{\bmod p}
\text{FROBENIUS MULTIPLICITY, NOT NEW SUPPORT}.
}
\tag{FCL-6}

## 6. Resultant criterion becomes mod-p support collision

For distinct primitive factors, the native resultant law says a prime `p` divides

\[
\operatorname{Res}(\Psi_m,\Psi_n)
\]

exactly when the two denominator indices lie on the same `p`-adic ray:

\[
\boxed{
 p\mid\operatorname{Res}(\Psi_m,\Psi_n)
\iff
\frac{\max(m,n)}{\min(m,n)}=p^a
}
\tag{FCL-7}

for an integer prime-power ratio.

The forward direction is equivalently the statement that the reductions of `Psi_m` and `Psi_n` have a common root/support modulo `p`.  Along a prime-power ray, (FCL-4)--(FCL-5) strengthen this to exact Frobenius-power coincidence.

Hence the prime-power resultant law is the characteristic-zero determinant shadow of a mod-`p` support recoalescence.

## 7. Why the resultant is depth-blind

Suppose `n=mp^a`.  In characteristic zero the level `a` is real scale provenance.  Modulo `p`, however, every level has already collapsed onto the same base support; the exponent `a` only changes Frobenius multiplicity.

The integral quotient-algebra theorem then shows

\[
\Psi_{mp^a}(\bar u)=p\cdot\text{unit}
\]

in `A_m`, independently of `a`.

Thus the two previously observed facts are one structure:

\[
\boxed{
\text{FROBENIUS SUPPORT COLLAPSE}
\Longrightarrow
\text{ONE p-TORSION LAYER}
\Longrightarrow
\text{DEPTH-BLIND NORMALIZED RESULTANT MASS}.
}
\tag{FCL-8}

## 8. Typing consequence

Before reduction, distinct p-adic levels are distinct finite spectral carriers.  Mod-p reduction deliberately erases that support distinction and retains it only as nilpotent/multiplicity thickness.

Therefore

`MOD_P_SUPPORT != CHARACTERISTIC_ZERO_DENOMINATOR_PROVENANCE`.

Freeze:

`R_p MOD p = FROBENIUS`.

`P_ADIC_PRIMITIVE_LEVELS MOD p = FROBENIUS_THICKENINGS_OF_ONE_SUPPORT`.

`PRIME_POWER_RESULTANT = SUPPORT_COLLISION_SHADOW`.
