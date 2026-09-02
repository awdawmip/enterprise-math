import EnterpriseMath.Geometry.TetrahedralResidualClassification

namespace EnterpriseMath.TetrahedralResidual

/-- Two integers have the same parity when their difference is even. -/
def SameParity (a b : ℤ) : Prop := Even (a - b)

/-- Same parity is reflexive. -/
theorem sameParity_refl (a : ℤ) : SameParity a a := by
  refine ⟨0, ?_⟩
  simp [SameParity]

/-- Same parity is symmetric. -/
theorem sameParity_symm {a b : ℤ} (h : SameParity a b) : SameParity b a := by
  rcases h with ⟨t, ht⟩
  refine ⟨-t, ?_⟩
  simp [SameParity] at ht ⊢
  linarith

/-- Same parity is transitive. -/
theorem sameParity_trans {a b c : ℤ}
    (hab : SameParity a b) (hbc : SameParity b c) : SameParity a c := by
  rcases hab with ⟨s, hs⟩
  rcases hbc with ⟨t, ht⟩
  refine ⟨s + t, ?_⟩
  simp [SameParity] at hs ht ⊢
  linarith

/-- The intrinsic parity quotient, without choosing representatives `0,1`. -/
def paritySetoid : Setoid ℤ where
  r := SameParity
  iseqv := ⟨sameParity_refl, sameParity_symm, sameParity_trans⟩

/-- The two-valued parity coordinate as an abstract quotient. -/
abbrev Parity := Quotient paritySetoid

/-- Parity class of an integer. -/
def parityClass (a : ℤ) : Parity := Quotient.mk' a

/-- The parity coordinate of a six-line configuration. -/
def edgeParity (x : Edge6) : Parity :=
  parityClass (x 0 + x 1 + x 2)

/-- The complete residual observable: three opposite-pair sums together with
one parity class. -/
def residualInvariant (x : Edge6) : (Fin 3 → ℤ) × Parity :=
  (matchingSums x, edgeParity x)

/-- Equality of the abstract parity coordinates is equivalent to an even
difference of the three distinguished edge coordinates. -/
theorem edgeParity_eq_iff_even_sub (x y : Edge6) :
    edgeParity x = edgeParity y ↔
      Even (subEdge x y 0 + subEdge x y 1 + subEdge x y 2) := by
  constructor
  · intro h
    have hrel : SameParity (x 0 + x 1 + x 2) (y 0 + y 1 + y 2) :=
      Quotient.exact h
    rcases hrel with ⟨t, ht⟩
    refine ⟨t, ?_⟩
    simp [SameParity, subEdge] at ht ⊢
    linarith
  · rintro ⟨t, ht⟩
    apply Quotient.sound
    refine ⟨t, ?_⟩
    simp [SameParity, subEdge] at ht ⊢
    linarith

/-- The three `A₂`-type matching coordinates plus the parity coordinate are
complete invariants for the integer slice-potential relation. -/
theorem deltaEquivalent_iff_residualInvariant_eq (x y : Edge6) :
    DeltaEquivalent x y ↔ residualInvariant x = residualInvariant y := by
  rw [deltaEquivalent_iff_matchingSums_eq_and_even,
    residualInvariant, Prod.mk.injEq, edgeParity_eq_iff_even_sub]

/-- Equivalent configurations have identical complete residual observable. -/
theorem residualInvariant_eq_of_deltaEquivalent {x y : Edge6}
    (h : DeltaEquivalent x y) : residualInvariant x = residualInvariant y :=
  (deltaEquivalent_iff_residualInvariant_eq x y).1 h

/-- Equality of the complete residual observable reconstructs an integral
zero-sum slice potential. -/
theorem deltaEquivalent_of_residualInvariant_eq {x y : Edge6}
    (h : residualInvariant x = residualInvariant y) : DeltaEquivalent x y :=
  (deltaEquivalent_iff_residualInvariant_eq x y).2 h

end EnterpriseMath.TetrahedralResidual
