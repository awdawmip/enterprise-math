import EnterpriseMath.CellAddress.ThreeRegionSlice

/-! Public address contract. No arbitrary full-X6 codec is asserted here. -/
namespace EnterpriseMath.CellAddress.Contract
open EnterpriseMath.CellAddress.ThreeRegionSlice

abbrev WireFields := { xs : List Nat // xs.length = 6 }
def pack (q : Code) : WireFields := ⟨digits q, digits_length q⟩

theorem pack_injective {p q : Code} (h : pack p = pack q) : p = q := by
  apply digits_injective
  exact congrArg Subtype.val h

theorem pack_fields_nonnegative (q : Code) (n : Nat)
    (_h : n ∈ (pack q).val) : 0 ≤ n := Nat.zero_le n

theorem pack_not_zero (q : Code) : (pack q).val ≠ [0,0,0,0,0,0] :=
  zero_marker_not_a_cell q

theorem public_step_compatible (d : Dir) (q : Code) :
    decode (step d q) = nativeStep d (decode q) := decode_step d q

#print axioms pack_injective
#print axioms pack_fields_nonnegative
#print axioms pack_not_zero
#print axioms public_step_compatible
end EnterpriseMath.CellAddress.Contract
