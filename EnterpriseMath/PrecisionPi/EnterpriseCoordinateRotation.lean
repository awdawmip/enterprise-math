import EnterpriseMath.PrecisionPi.EnterpriseCoordinateK4

namespace EnterpriseMath.PrecisionPi.EnterpriseCoordinateRotation

open EnterpriseCoordinateIncidence EnterpriseCoordinateK4

/-- A permutation of slice charts transports an unordered slice pair. -/
def mapSlicePair (σ : Equiv.Perm SliceChart) (p : SlicePair) : SlicePair :=
  ⟨(p : Finset SliceChart).map σ.toEmbedding, by simpa using p.property⟩

/-- Transport of slice pairs is itself a permutation. -/
def slicePairPerm (σ : Equiv.Perm SliceChart) : Equiv.Perm SlicePair where
  toFun := mapSlicePair σ
  invFun := mapSlicePair σ.symm
  left_inv p := by
    apply Subtype.ext
    ext s
    simp [mapSlicePair]
  right_inv p := by
    apply Subtype.ext
    ext s
    simp [mapSlicePair]

/-- A slice permutation induces the corresponding permutation of FCC line families. -/
def lineFamilyPerm (σ : Equiv.Perm SliceChart) : Equiv.Perm LineFamily :=
  lineFamilyEquivSlicePair.trans
    ((slicePairPerm σ).trans lineFamilyEquivSlicePair.symm)

/-- The induced line permutation sends the associated pair to the transported pair. -/
theorem lineToSlicePair_lineFamilyPerm
    (σ : Equiv.Perm SliceChart) (l : LineFamily) :
    lineToSlicePair (lineFamilyPerm σ l) =
      mapSlicePair σ (lineToSlicePair l) := by
  change lineFamilyEquivSlicePair (lineFamilyPerm σ l) = _
  simp [lineFamilyPerm, slicePairPerm]

/-- Incidence is covariant under simultaneous slice and line transport. -/
theorem incidence_covariant
    (σ : Equiv.Perm SliceChart) (l : LineFamily) (s : SliceChart) :
    lineFamilyPerm σ l ∈ sliceLines (σ s) ↔ l ∈ sliceLines s := by
  rw [← mem_lineToSlicePair_iff, ← mem_lineToSlicePair_iff]
  rw [lineToSlicePair_lineFamilyPerm]
  simp [mapSlicePair]

/-- The identity slice transport induces the identity line transport. -/
theorem lineFamilyPerm_refl :
    lineFamilyPerm (Equiv.refl SliceChart) = Equiv.refl LineFamily := by
  ext l
  apply lineFamilyEquivSlicePair.injective
  simp [lineFamilyPerm, slicePairPerm, mapSlicePair]

/-- Composition of slice transports agrees with composition of induced line transports. -/
theorem lineFamilyPerm_trans
    (σ τ : Equiv.Perm SliceChart) :
    lineFamilyPerm (σ.trans τ) =
      (lineFamilyPerm σ).trans (lineFamilyPerm τ) := by
  ext l
  apply lineFamilyEquivSlicePair.injective
  simp [lineFamilyPerm, slicePairPerm, mapSlicePair]

end EnterpriseMath.PrecisionPi.EnterpriseCoordinateRotation
