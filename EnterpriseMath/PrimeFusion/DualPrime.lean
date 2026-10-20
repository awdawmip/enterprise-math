import Mathlib.Algebra.CharP.Lemmas
import Mathlib.Algebra.Field.IsField
import EnterpriseMath.PrimeFusion.Reconstruction

namespace EnterpriseMath.PrimeFusion

-- These proposition-valued structures are intentionally installed with `letI`
-- below because the fixed `ZMod` API consumes them through typeclass synthesis.
set_option linter.style.haveILetI false

/-- An unordered square-free semiprime is a product of two distinct natural primes.
This deliberately forgets channel attachment; the fixed-channel predicate below
retains the Gaussian/Eisenstein labels. -/
def SquarefreeSemiprime (h : ℕ) : Prop :=
  ∃ p q : ℕ, p.Prime ∧ q.Prime ∧ p ≠ q ∧ h = p * q

/-- F2-L03 arithmetic core. For two fixed nontrivial distinct factors, being
prime in both factors is equivalent to their product being a square-free
semiprime. The reverse direction is exact: no coprimality assumption is needed. -/
theorem dualPrime_iff_squarefreeSemiprime_mul {n c : ℕ}
    (hn1 : 1 < n) (hc1 : 1 < c) (hne : n ≠ c) :
    (n.Prime ∧ c.Prime) ↔ SquarefreeSemiprime (n * c) := by
  constructor
  · rintro ⟨hn, hc⟩
    exact ⟨n, c, hn, hc, hne, rfl⟩
  · rintro ⟨p, q, hp, hq, _hpq, hprod⟩
    have hpdiv : p ∣ n * c := ⟨q, hprod⟩
    rcases (hp.dvd_mul.mp hpdiv) with hpN | hpC
    · rcases hpN with ⟨k, hk⟩
      have heq : p * (k * c) = p * q := by
        calc
          p * (k * c) = n * c := by rw [hk]; simp [Nat.mul_assoc]
          _ = p * q := hprod
      have hkcq : k * c = q := Nat.mul_left_cancel hp.pos heq
      have hcq : c ∣ q := ⟨k, by simpa [Nat.mul_comm] using hkcq.symm⟩
      have hcEq : c = q :=
        (hq.eq_one_or_self_of_dvd c hcq).resolve_left (Nat.ne_of_gt hc1)
      have hkEq : k = 1 := by
        have hkq : k * q = 1 * q := by simpa [hcEq] using hkcq
        exact Nat.mul_right_cancel hq.pos hkq
      have hnEq : n = p := by simpa [hkEq] using hk
      exact ⟨by simpa [hnEq] using hp, by simpa [hcEq] using hq⟩
    · rcases hpC with ⟨k, hk⟩
      have heq : p * (n * k) = p * q := by
        calc
          p * (n * k) = n * c := by
            rw [hk]
            simp [Nat.mul_left_comm]
          _ = p * q := hprod
      have hnkq : n * k = q := Nat.mul_left_cancel hp.pos heq
      have hnq : n ∣ q := ⟨k, hnkq.symm⟩
      have hnEq : n = q :=
        (hq.eq_one_or_self_of_dvd n hnq).resolve_left (Nat.ne_of_gt hn1)
      have hkEq : k = 1 := by
        have hqk : q * k = q * 1 := by simpa [hnEq] using hnkq
        exact Nat.mul_left_cancel hq.pos hqk
      have hcEq : c = p := by simpa [hkEq] using hk
      exact ⟨by simpa [hnEq] using hq, by simpa [hcEq] using hp⟩

/-- A prime modulus makes the *existing* quotient ring `ZMod n` a field.
The primality proof is used only in this forward construction. -/
theorem zmod_isField_of_prime {n : ℕ} (hn : n.Prime) : IsField (ZMod n) := by
  letI : Fact (Nat.Prime n) := ⟨hn⟩
  exact Field.toIsField (ZMod n)

/-- Converse field-to-prime bridge for a nontrivial positive modulus.

Crucially, the hypothesis is `IsField (ZMod n)`, a property of the already-fixed
`ZMod n` ring operations; it does not store or assume `n.Prime`. Since `ZMod n`
has characteristic `n`, fieldness supplies an integral-domain structure and,
for `1 < n`, the carrier is finite. The characteristic of a finite nontrivial
domain is prime, hence `n.Prime`. -/
theorem zmod_prime_of_isField {n : ℕ} (hn1 : 1 < n)
    (hfield : IsField (ZMod n)) : n.Prime := by
  letI : Nontrivial (ZMod n) := hfield.nontrivial
  letI : IsDomain (ZMod n) := hfield.isDomain
  letI : NeZero n := ⟨Nat.ne_of_gt (Nat.zero_lt_of_lt hn1)⟩
  letI : Finite (ZMod n) := inferInstance
  exact CharP.char_is_prime (ZMod n) n

/-- The channel-labelled quotient-field condition.

Unlike the rejected first F2 encoding, this definition contains **no primality
fields**. It asserts directly that the two already-fixed Gaussian/Eisenstein
`ZMod` quotient rings are fields and remembers that their moduli are distinct. -/
def FixedChannelPrimeFieldPair (a b : ℤ) : Prop :=
  IsField (ZMod (Nmodulus a b)) ∧
    IsField (ZMod (Cmodulus a b)) ∧
      Nmodulus a b ≠ Cmodulus a b

/-- Canonical prime-field structure on the fixed Gaussian channel, used in the
forward dual-prime-to-field direction. -/
@[instance_reducible]
noncomputable def gaussianChannelField (a b : ℤ) (hN : (Nmodulus a b).Prime) :
    Field (ZMod (Nmodulus a b)) := by
  letI : Fact (Nat.Prime (Nmodulus a b)) := ⟨hN⟩
  infer_instance

/-- Canonical prime-field structure on the fixed Eisenstein channel, used in the
forward dual-prime-to-field direction. -/
@[instance_reducible]
noncomputable def eisensteinChannelField (a b : ℤ) (hC : (Cmodulus a b).Prime) :
    Field (ZMod (Cmodulus a b)) := by
  letI : Fact (Nat.Prime (Cmodulus a b)) := ⟨hC⟩
  infer_instance

/-- F2-L04: structural fieldness of the fixed channels yields actual finite-field
data on exactly those quotient ring operations, together with the exact orders. -/
theorem fixed_channel_prime_fields_and_orders {a b : ℤ}
    (h : FixedChannelPrimeFieldPair a b) :
    Nonempty (Field (ZMod (Nmodulus a b))) ∧
      Nonempty (Field (ZMod (Cmodulus a b))) ∧
        Nat.card (ZMod (Nmodulus a b)) = Nmodulus a b ∧
          Nat.card (ZMod (Cmodulus a b)) = Cmodulus a b := by
  refine ⟨⟨h.1.toField⟩, ⟨h.2.1.toField⟩, ?_, ?_⟩
  · exact gaussianCarrier_card a b
  · exact eisensteinCarrier_card a b

/-- F2-L04 quotient/product form with fixed channel attachment. For a primitive
cell the already-fixed CRT projections give the exact ring product, while the
structural field hypotheses upgrade each labelled factor to a finite field. -/
theorem fixed_channel_prime_field_product {a b : ℤ}
    (hab : IsCoprime a b)
    (h : FixedChannelPrimeFieldPair a b) :
    Nonempty (Field (ZMod (Nmodulus a b))) ∧
      Nonempty (Field (ZMod (Cmodulus a b))) ∧
        Nonempty
          (ZMod (Hmodulus a b) ≃+*
            ZMod (Nmodulus a b) × ZMod (Cmodulus a b)) := by
  have hfields := fixed_channel_prime_fields_and_orders h
  exact ⟨hfields.1, hfields.2.1, ⟨pointedCRT a b hab⟩⟩

/-- F2-L03/L04 cell specialization: on the fixed channel projections, dual
primality is equivalent to square-free-semiprime total modulus. The hypotheses
make the nonzero/distinct family explicit; the theorem keeps channel order in
its left-hand side while the right-hand side intentionally forgets it. -/
theorem fixed_channels_dualPrime_iff_squarefreeSemiprime
    {a b : ℤ}
    (hN1 : 1 < Nmodulus a b)
    (hC1 : 1 < Cmodulus a b)
    (hne : Nmodulus a b ≠ Cmodulus a b) :
    ((Nmodulus a b).Prime ∧ (Cmodulus a b).Prime) ↔
      SquarefreeSemiprime (Hmodulus a b) := by
  rw [Hmodulus_eq_mul]
  exact dualPrime_iff_squarefreeSemiprime_mul hN1 hC1 hne

/-- The load-bearing F2-L04 converse: actual fieldness of the two fixed quotient
rings forces primality of the two channel moduli. The `1 <` hypotheses are the
explicit edge conditions needed to exclude the characteristic-zero/degenerate
modulus boundary when converting finite-domain characteristic to primality. -/
theorem fixedChannelPrimeFieldPair_dualPrime
    {a b : ℤ}
    (hN1 : 1 < Nmodulus a b)
    (hC1 : 1 < Cmodulus a b)
    (h : FixedChannelPrimeFieldPair a b) :
    (Nmodulus a b).Prime ∧ (Cmodulus a b).Prime := by
  exact ⟨zmod_prime_of_isField hN1 h.1, zmod_prime_of_isField hC1 h.2.1⟩

/-- Channel-labelled T8 characterization at the fixed quotient interface.

The forward direction constructs fieldness from dual primality; the reverse
direction proves primality from structural `IsField` hypotheses on the existing
`ZMod` quotients. Distinctness is retained as channel data rather than erased by
an unordered product isomorphism. -/
theorem fixedChannelPrimeFieldPair_iff_dualPrime
    {a b : ℤ}
    (hN1 : 1 < Nmodulus a b)
    (hC1 : 1 < Cmodulus a b)
    (hne : Nmodulus a b ≠ Cmodulus a b) :
    FixedChannelPrimeFieldPair a b ↔
      ((Nmodulus a b).Prime ∧ (Cmodulus a b).Prime) := by
  constructor
  · intro h
    exact fixedChannelPrimeFieldPair_dualPrime hN1 hC1 h
  · rintro ⟨hN, hC⟩
    exact ⟨zmod_isField_of_prime hN, zmod_isField_of_prime hC, hne⟩

end EnterpriseMath.PrimeFusion
