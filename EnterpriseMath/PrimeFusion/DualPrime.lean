import EnterpriseMath.PrimeFusion.PointedRecovery

namespace EnterpriseMath.PrimeFusion

/-- F2-L03: dual-prime data with the Gaussian channel first and the Eisenstein
channel second. Distinctness is explicit because the target is the square-free
semiprime family. -/
def DualPrimeChannels (a b : ℤ) : Prop :=
  (Nmodulus a b).Prime ∧
    (Cmodulus a b).Prime ∧
    Nmodulus a b ≠ Cmodulus a b

/-- Unordered arithmetic content of “square-free semiprime”: a product of two
distinct primes. This intentionally forgets which factor is Gaussian/Eisenstein. -/
def SquarefreeSemiprime (H : ℕ) : Prop :=
  ∃ p q : ℕ, p.Prime ∧ q.Prime ∧ p ≠ q ∧ H = p * q

/-- Channel-labelled square-free semiprime data. Unlike `SquarefreeSemiprime`, this
remembers that `n` is the first (Gaussian) factor and `c` the second (Eisenstein)
factor. -/
def ChannelledSquarefreeSemiprime (n c H : ℕ) : Prop :=
  n.Prime ∧ c.Prime ∧ n ≠ c ∧ H = n * c

/-- F2-L03 / T8 exact arithmetic equivalence at the fixed channel attachment. -/
theorem dualPrime_iff_channelled_squarefree_semiprime (a b : ℤ) :
    DualPrimeChannels a b ↔
      ChannelledSquarefreeSemiprime
        (Nmodulus a b) (Cmodulus a b) (Hmodulus a b) := by
  simp [DualPrimeChannels, ChannelledSquarefreeSemiprime, Hmodulus_eq_mul]

/-- Forgetting channel labels recovers the usual unordered distinct-prime product. -/
theorem channelled_squarefree_semiprime_forget
    {n c H : ℕ} (h : ChannelledSquarefreeSemiprime n c H) :
    SquarefreeSemiprime H := by
  rcases h with ⟨hn, hc, hne, hH⟩
  exact ⟨n, c, hn, hc, hne, hH⟩

/-- Negative control for T8 channel attachment: the same unordered semiprime admits
both factor orders. Therefore the abstract product alone cannot identify the
Gaussian versus Eisenstein channel. -/
theorem unordered_semiprime_has_both_channel_orders
    {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hne : p ≠ q) :
    ChannelledSquarefreeSemiprime p q (p * q) ∧
      ChannelledSquarefreeSemiprime q p (p * q) := by
  constructor
  · exact ⟨hp, hq, hne, rfl⟩
  · exact ⟨hq, hp, Ne.symm hne, by simp [mul_comm]⟩

/-- F2-L04 certificate for the fixed product quotient. The first component is the
Gaussian `ZMod N` carrier and the second the Eisenstein `ZMod C` carrier; the
prime and distinctness fields are exactly what makes them distinct prime fields. -/
structure FixedChannelPrimeFieldCertificate (a b : ℤ) : Prop where
  gaussianPrime : (Nmodulus a b).Prime
  eisensteinPrime : (Cmodulus a b).Prime
  distinct : Nmodulus a b ≠ Cmodulus a b
  fusedOrder : Hmodulus a b = Nmodulus a b * Cmodulus a b

/-- F2-L04 converse included: the fixed channel quotient certificate is equivalent
to dual-prime arithmetic. This is deliberately label-preserving. -/
theorem dualPrime_iff_fixed_channel_prime_field_certificate (a b : ℤ) :
    DualPrimeChannels a b ↔ FixedChannelPrimeFieldCertificate a b := by
  constructor
  · rintro ⟨hN, hC, hne⟩
    exact ⟨hN, hC, hne, Hmodulus_eq_mul a b⟩
  · intro h
    exact ⟨h.gaussianPrime, h.eisensteinPrime, h.distinct⟩

/-- Prime channel moduli equip the two fixed `ZMod` carriers with their canonical
field structures. The instances are supplied explicitly so the statement carries
no ambient instance-ordering ambiguity. -/
theorem dualPrime_fixed_zmod_fields
    {a b : ℤ} (h : DualPrimeChannels a b) :
    Nonempty (Field (ZMod (Nmodulus a b))) ∧
      Nonempty (Field (ZMod (Cmodulus a b))) := by
  exact
    ⟨⟨@ZMod.instField (Nmodulus a b) ⟨h.1⟩⟩,
      ⟨@ZMod.instField (Cmodulus a b) ⟨h.2.1⟩⟩⟩

/-- F2-L04: under primitive input the already-fixed CRT projection is exactly a
product of the two labelled prime-field carriers, with the expected orders. The
field structures are returned together with the fixed equivalence so the theorem
does not collapse to a bare unordered CRT slogan. -/
theorem dualPrime_pointedCRT_prime_field_orders
    {a b : ℤ} (hab : IsCoprime a b) (h : DualPrimeChannels a b) :
    Nonempty (Field (ZMod (Nmodulus a b))) ∧
      Nonempty (Field (ZMod (Cmodulus a b))) ∧
      ∃ e : ZMod (Hmodulus a b) ≃+*
          ZMod (Nmodulus a b) × ZMod (Cmodulus a b),
        e = pointedCRT a b hab ∧
        Nat.card (ZMod (Nmodulus a b)) = Nmodulus a b ∧
        Nat.card (ZMod (Cmodulus a b)) = Cmodulus a b := by
  rcases dualPrime_fixed_zmod_fields h with ⟨hNField, hCField⟩
  exact
    ⟨hNField, hCField,
      ⟨pointedCRT a b hab, rfl, gaussianCarrier_card a b, eisensteinCarrier_card a b⟩⟩

/-- The fixed prime-field certificate also yields the channel-labelled semiprime
statement, hence its unordered consequence, without dropping the attachment. -/
theorem fixed_channel_prime_fields_imply_squarefree_semiprime
    {a b : ℤ} (h : FixedChannelPrimeFieldCertificate a b) :
    SquarefreeSemiprime (Hmodulus a b) := by
  apply channelled_squarefree_semiprime_forget
  exact ⟨h.gaussianPrime, h.eisensteinPrime, h.distinct, h.fusedOrder⟩

end EnterpriseMath.PrimeFusion
