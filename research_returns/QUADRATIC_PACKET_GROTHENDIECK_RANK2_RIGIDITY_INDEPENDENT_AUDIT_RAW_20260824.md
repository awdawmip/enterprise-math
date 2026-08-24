# Quadratic Packet Grothendieck Rank-Two Rigidity — Independent Audit RAW

Status: `FROZEN RAW / BLIND-FORWARD`

Date: `2026-08-24`

Task-ID:

`RS-QUADRATIC-PACKET-GROTHENDIECK-RANK2-RIGIDITY-INDEPENDENT-AUDIT`

Owner branch:

`research/quadratic-packet-rank2-rigidity-independent-audit`

Frozen audit packet:

`research_inputs/QUADRATIC_PACKET_GROTHENDIECK_RANK2_RIGIDITY_AUDIT_PACKET_20260824.md@blob:f2f64fb25419c592031ca01f467a66ac9fc61676`

Source-proof access before this freeze: `NO`

Raw verdict:

`PROVED_AT_EXACT_STRENGTH`

Packet-class verdict: `PROVED`

---

## 1. Exact theorem proved

Let `A` be a commutative unital `Z`-algebra whose underlying additive group is free of finite rank `n >= 2`. Let `e in A` be nonzero and nilpotent. Suppose that for a prime `ell`:

1. `A / (ell + e)A` is cyclic as an additive abelian group;
2. there are `k in Z` and a unit `u in A^x` such that
   `(ell + e)^2 = u (ell^2 + k e)`.

Then `n = 2`. Moreover `A / (ell + e)A` has order `ell^2`.

No hypothesis has been strengthened or reinterpreted.

---

## 2. Independent proof

Write `M` for the underlying free `Z`-module of `A`, and let

`T = m_e : M -> M`

be multiplication by `e`. Since `e` is nilpotent, `T` is nilpotent.

Let

`Q = M / (ell I + T)M = A / (ell + e)A`.

### Lemma 2.1 — the quotient is finite of order `ell^n`

For nilpotent `T`, the characteristic polynomial over `Q` is `x^n`. Hence

`det(ell I + T) = ell^n != 0`.

For an injective endomorphism of a free rank-`n` abelian group represented by an integral matrix of nonzero determinant, the cokernel is finite of order the absolute determinant; this is the standard Smith-normal-form index formula. Therefore

`|Q| = ell^n`.

Since `Q` is cyclic by premise 1,

`Q ~= Z / ell^n Z`.

In particular,

`Q / ell Q ~= F_ell`.

### Lemma 2.2 — cyclicity gives a corank-one nilpotent residue operator

Set

`V = M / ell M ~= A / ell A`

and let

`E = m_{bar e} : V -> V`

be multiplication by the image `bar e` of `e` modulo `ell`.

Reduction of the cokernel modulo `ell` gives

`Q / ell Q ~= M / ((ell I + T)M + ell M) ~= V / E V`.

Thus

`dim_Fell(V / E V) = 1`.

Since `E` is an endomorphism of the `n`-dimensional vector space `V`, rank-nullity gives

`dim ker(E) = dim coker(E) = 1`,

hence

`rank(E) = n - 1`.

Because `n >= 2`, `E != 0`. Since `e` is nilpotent, so is `E`.

### Lemma 2.3 — a nonzero nilpotent map strictly drops rank after squaring

Because `E != 0`, `im(E) != 0`. The restriction

`E | im(E) : im(E) -> im(E)`

is nilpotent, so it cannot be injective on the nonzero finite-dimensional space `im(E)`. Therefore

`im(E) intersect ker(E) != 0`.

Equivalently,

`rank(E^2) < rank(E)`.

### Lemma 2.4 — the arbitrary unit causes no gap

Reduce premise 2 modulo `ell`:

`bar e^2 = bar u * bar k * bar e`.

Let `U = m_{bar u}` on `V`. Since `u` is a unit in `A`, `bar u` is a unit in `A/ell A`, so `U` is an invertible `F_ell`-linear map. Applying multiplication operators to the residue equality gives

`E^2 = bar k * U E`.

If `bar k != 0`, then `bar k U` is invertible and therefore

`rank(E^2) = rank(E)`,

contradicting Lemma 2.3. Hence

`bar k = 0`, i.e. `ell | k`.

Therefore the same residue equality becomes

`E^2 = 0`.

Now `im(E) subset ker(E)`. Using Lemma 2.2,

`n - 1 = rank(E) <= dim ker(E) = 1`.

Thus `n <= 2`. Since the theorem assumes `n >= 2`,

`n = 2`.

Finally Lemma 2.1 gives

`|A / (ell + e)A| = ell^n = ell^2`.

This proves QP-R2 at exactly the frozen statement strength.

---

## 3. Edge-case pressure

### 3.1 `ell = 2` versus odd primes

The proof is uniform in the prime `ell`. It never divides by `2`, never assumes `2` is invertible, and never uses oddness. The only field fact used is that a nonzero scalar `bar k in F_ell` is invertible. Thus `ell = 2` and all odd primes are covered identically.

### 3.2 Possibility `e in ell A`

This is not an extra hypothesis; it is ruled out by the stated premises.

Indeed Lemma 2.2 gives `rank(E) = n - 1 >= 1`, so `bar e` cannot act as zero. In particular `e notin ell A`.

There is also a direct integral check. If `e = ell f`, torsion-freeness of the additive group and nilpotence of `e` imply nilpotence of `f`. Hence `1 + f` is a unit and

`(ell + e)A = ell(1 + f)A = ell A`.

Then

`A / (ell + e)A ~= A / ell A ~= (Z/ell Z)^n`,

which is not cyclic for `n >= 2`.

### 3.3 Nilpotence index greater than two

No square-zero assumption is used in the proof. Higher nilpotence index is allowed at the start and is eliminated by the premises.

After the proof gives `n = 2`, the multiplication operator `T = m_e` is a nilpotent endomorphism of a free rank-two module. Over `Q`, its characteristic polynomial is `x^2`, so Cayley-Hamilton gives `T^2 = 0`; because the module is torsion-free this equality is integral. Therefore

`e^2 = T^2(1) = 0`.

Since `e != 0`, any actual model satisfying QP-R2 has nilpotence index exactly two. Thus nilpotence index `> 2` is incompatible with the two substantive premises.

### 3.4 Arbitrary-unit associateness

No normalization of `u` is needed. The proof uses only that reduction of a unit is a unit, so multiplication by `bar u` is invertible. In particular it does not assume `u congruent 1 (mod ell)`, scalarity of `u`, or any sign/orientation condition.

A determinant-side phase fact can nevertheless be derived rather than assumed. From

`(ell I + T)^2 = m_u (ell^2 I + kT)`

we get

`ell^(2n) = det(m_u) * ell^(2n)`,

because both `T` and `kT` are nilpotent. Hence

`det(m_u) = +1`.

This phase-neutral determinant is a consequence of premise 2 and is not used to prove rank two.

### 3.5 Dependence on commutativity

The rank-two proof itself does not use commutativity. It uses only:

- a unital associative `Z`-algebra structure;
- finite free additive rank;
- left multiplication by `e`;
- nilpotence of `e`;
- the additive cyclicity of the cokernel of left multiplication by `ell + e`;
- an equality `(ell + e)^2 = u(ell^2 + ke)` with a left unit `u`.

For left multiplication, `L_{u e} = L_u L_e` holds in every associative algebra, and `L_u` is invertible for a unit `u`. Thus commutativity is redundant for the algebraic rank-rigidity conclusion, provided `(ell + e)A` is interpreted as the image of left multiplication by `ell + e`.

---

## 4. Positive rank-two model / non-vacuity

For every prime `ell`, take

`A = Z[epsilon] / (epsilon^2)`, `e = epsilon`.

Then `A` is free of rank two and `e` is nonzero nilpotent. In the quotient by `(ell + epsilon)` we have `epsilon = -ell`, and the relation `epsilon^2 = 0` becomes `ell^2 = 0`. Hence

`A / (ell + epsilon)A ~= Z / ell^2 Z`,

which is cyclic of order `ell^2`.

Also

`(ell + epsilon)^2 = ell^2 + 2ell epsilon`,

so premise 2 holds with

`u = 1`, `k = 2ell`.

This includes `ell = 2` (`k = 4`) and every odd prime.

---

## 5. Premise minimality / independence

The three named ingredients are individually necessary if deleted outright, but two of them are stronger than the local linear-algebra input actually used.

| Ingredient | Exact role in proof | Can it be weakened? | Countermodel if deleted outright | Audit status |
|---|---|---|---|---|
| Nilpotent infinitesimal phase | Makes `E = m_bar(e)` nilpotent, hence for nonzero `E`, `rank(E^2) < rank(E)` | Yes. Global integral nilpotence can be replaced by the local residue condition `rank(E^2) < rank(E)`; residue nilpotence is a convenient stronger sufficient condition | `A = Z^3`, `e = (0, 1-ell, 1-ell)`, any prime `ell`; take `u=1`, `k=ell+1`. Then `A/(ell+e)A ~= Z/ell Z` is cyclic and `(ell+e)^2 = ell^2 + ke`, but `e` is not nilpotent and rank is `3` | Necessary in some rank-drop form; original premise is not minimal |
| One-clock self-composition closure | Modulo `ell`, forces `E^2 = bar k U E`; hence `rank(E^2)` is either `0` or `rank(E)` | Yes. Only the residue relation `E^2 = c U E` with `c in F_ell` and `U` invertible is used; equivalently, the needed rank consequence is `rank(E^2) in {0, rank(E)}` | `A = Z[t]/(t^3)`, `e=t`. Then `e` is nilpotent and `A/(ell+t)A ~= Z/ell^3 Z` is cyclic, but no `k` and unit `u` satisfy the one-clock closure | Necessary in some residue rank-control form; original integral closure is stronger than needed |
| Primitive one-chain quotient | Gives `dim_Fell coker(E)=1`, hence `dim ker(E)=1` and `rank(E)=n-1` | Locally the exact input is `dim_Fell(V/EV)=1`. Under the original nilpotence premise this is equivalent to cyclicity of `A/(ell+e)A`, since that quotient is an `ell`-group of order `ell^n` | `A = Z[epsilon,eta]/(epsilon,eta)^2`, `e=epsilon`. Then `e^2=0` and closure holds with `u=1,k=2ell`, but rank is `3`; modulo `ell`, multiplication by `epsilon` has rank `1`, so the cokernel has dimension `2` and the quotient is not cyclic | Necessary; the stated global cyclicity is equivalent to the local corank-one condition in the original setting |

### 5.1 Verification of the nilpotence-deleted countermodel

Take

`A = Z^3`, `e = (0, 1-ell, 1-ell)`.

Then

`ell + e = (ell,1,1)`,

so

`A/(ell+e)A ~= Z/ell Z`.

With `k = ell+1`,

`ell^2 + k e = (ell^2, ell^2 + (ell+1)(1-ell), ell^2 + (ell+1)(1-ell)) = (ell^2,1,1)`.

But `(ell+e)^2 = (ell^2,1,1)`, so self-composition holds with `u=1`. Since `1-ell != 0`, `e` is not nilpotent in the reduced ring `Z^3`. This is a rank-three countermodel after deleting nilpotence.

### 5.2 Verification of the self-composition-deleted countermodel

Take

`A = Z[t]/(t^3)`, `e=t`.

The quotient by `(ell+t)` imposes `t=-ell` and then `t^3=0` imposes `ell^3=0`, so the quotient is cyclic of order `ell^3`.

Suppose for contradiction that

`(ell+t)^2 = u(ell^2 + kt)`

for a unit `u`. Every unit of `Z[t]/(t^3)` has the form

`u = s + a t + b t^2`, with `s = +/-1`.

Comparing constant coefficients gives `s=1`. Comparing `t` coefficients gives

`k + a ell^2 = 2ell`,

so `ell | k`. Comparing `t^2` coefficients gives

`a k + b ell^2 = 1`,

whose left side is divisible by `ell`, impossible. Thus the closure premise fails genuinely.

### 5.3 Verification of the cyclicity-deleted countermodel

Take

`A = Z[epsilon,eta]/(epsilon,eta)^2`, `e=epsilon`.

Then `e^2=0`, so

`(ell+e)^2 = ell^2 + 2ell e`

with `u=1`, `k=2ell`. The additive rank is three. Modulo `ell`, multiplication by `epsilon` sends `1` to `epsilon` and kills both `epsilon` and `eta`, so it has rank one and cokernel dimension two. Therefore `A/(ell+e)A` is not cyclic.

---

## 6. Stronger local linear-algebra form actually established

The proof factors through the following more minimal statement.

Let `V` be an `n`-dimensional vector space over `F_ell`, `n >= 2`, and let `E in End(V)`. Assume:

1. `dim coker(E) = 1`;
2. `rank(E^2) < rank(E)`;
3. `E^2 = c U E` for some `c in F_ell` and some invertible `U`.

Then `n=2`.

Proof: if `c != 0`, condition 3 gives `rank(E^2)=rank(E)`, contradicting condition 2. Hence `c=0`, so `E^2=0`. Condition 1 gives `dim ker(E)=1` and `rank(E)=n-1`. Since `im(E) subset ker(E)`, `n-1 <= 1`, hence `n<=2`; with `n>=2`, `n=2`.

QP-R2 is an integral algebraic lifting of this local rank lemma:

- cyclic quotient + nilpotence imply condition 1;
- nilpotence implies condition 2;
- one-clock associateness implies condition 3 after reduction modulo `ell`.

This identifies the exact rigidity mechanism without altering the frozen theorem.

---

## 7. Lemmas used but not reproved from first principles

Only the following standard facts are used; their application is explicit above.

1. **Smith index formula.** An integral `n x n` matrix of nonzero determinant has finite cokernel of order `|det|`.
2. **Nilpotent characteristic polynomial.** A nilpotent endomorphism of an `n`-dimensional vector space has characteristic polynomial `x^n`.
3. **Rank-nullity.** For an endomorphism of a finite-dimensional vector space, `dim coker(E)=dim ker(E)`.
4. **Unit reduction.** A ring unit remains a unit after passing to a quotient.
5. **Cayley-Hamilton in rank two.** A nilpotent endomorphism of a two-dimensional vector space has square zero.

No classification theorem for finite-dimensional algebras, no Grothendieck/Cartier theorem, and no Foundation axiom is used.

---

## 8. Blind-forward conclusion

`PROVED_AT_EXACT_STRENGTH`.

The exact QP-R2 claim is true. The proof also shows:

- `e notin ell A` is derived, not assumed;
- `ell | k` is derived;
- arbitrary-unit associateness is sufficient with no normalization of `u`;
- the determinant phase `det(m_u)=+1` is derived and unnecessary to the rank argument;
- nilpotence index `>2` is excluded rather than silently assumed away;
- commutativity is not needed for the rank-rigidity mechanism;
- global nilpotence and integral one-clock closure are stronger than the local conditions actually needed.

The raw argument is frozen here before any access to the withheld source proof.
