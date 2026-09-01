import EnterpriseMath.PrimeFusion.Reconstruction

namespace EnterpriseMath.PrimeFusion

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

/-- The channel-labelled prime-field condition. Unlike `SquarefreeSemiprime`,
this records which fixed projection is the Gaussian `N` factor and which is the
Eisenstein `C` factor. -/
def FixedChannelPrimeFieldPair (a b : ℤ) : Prop :=
  (Nmodulus a b).Prime ∧
    (Cmodulus a b).Prime ∧
      Nmodulus a b ≠ Cmodulus a b

/-- F2-L04: a labelled dual-prime cell really has two finite field carriers,
with the fixed Gaussian/Eisenstein orders `N` and `C`; no unordered product
isomorphism is used to manufacture or swap these labels. -/
theorem fixed_channel_prime_fields_and_orders {a b : ℤ}
    (h : FixedChannelPrimeFieldPair a b) :
    Nonempty (Field (ZMod (Nmodulus a b))) ∧
      Nonempty (Field (ZMod (Cmodulus a b))) ∧
        Nat.card (ZMod (Nmodulus a b)) = Nmodulus a b ∧
          Nat.card (ZMod (Cmodulus a b)) = Cmodulus a b := by
  letI : Fact (Nat.Prime (Nmodulus a b)) := ⟨h.1⟩
  letI : Fact (Nat.Prime (Cmodulus a b)) := ⟨h.2.1⟩
  refine ⟨⟨inferInstance⟩, ⟨inferInstance⟩, ?_, ?_⟩
  · exact gaussianCarrier_card a b
  · exact eisensteinCarrier_card a b

/-- F2-L04 quotient/product form with fixed channel attachment. For a primitive
cell the already-fixed CRT projections give the exact ring product, while dual
primality upgrades each labelled factor to a finite field. -/
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

/-- Channel-labelled form of the same T8 characterization. This is the converse
bridge required by F2-L04: a fixed pair of distinct prime `ZMod` channels is
exactly the dual-prime condition, not merely an abstract unordered product. -/
theorem fixedChannelPrimeFieldPair_iff_dualPrime
    {a b : ℤ} (hne : Nmodulus a b ≠ Cmodulus a b) :
    FixedChannelPrimeFieldPair a b ↔
      ((Nmodulus a b).Prime ∧ (Cmodulus a b).Prime) := by
  simp [FixedChannelPrimeFieldPair, hne]

end EnterpriseMath.PrimeFusion
