import EnterpriseMath.Order.WellFoundedStabilization

namespace EnterpriseMath.ReductiveCompositionStabilization

open EnterpriseMath.WellFoundedStabilization

variable {α : Type*} [PartialOrder α]

/--
For two reductive endomaps, a fixed point of their composition is exactly a
common fixed point. No commutation assumption is needed.
-/
theorem comp_fixed_iff_common (F G : α → α)
    (hFred : ∀ x, F x ≤ x) (hGred : ∀ x, G x ≤ x) (x : α) :
    G (F x) = x ↔ F x = x ∧ G x = x := by
  constructor
  · intro hcomp
    have hxF : x ≤ F x := by
      calc
        x = G (F x) := hcomp.symm
        _ ≤ F x := hGred (F x)
    have hF : F x = x := le_antisymm (hFred x) hxF
    refine ⟨hF, ?_⟩
    calc
      G x = G (F x) := by rw [hF]
      _ = x := hcomp
  · rintro ⟨hF, hG⟩
    rw [hF, hG]

/-- Composition preserves monotonicity. -/
theorem comp_monotone (F G : α → α) (hFmono : Monotone F) (hGmono : Monotone G) :
    Monotone (fun x => G (F x)) := by
  intro x y hxy
  exact hGmono (hFmono hxy)

/-- Composition preserves reductivity. -/
theorem comp_reductive (F G : α → α)
    (hFred : ∀ x, F x ≤ x) (hGred : ∀ x, G x ≤ x) :
    ∀ x, G (F x) ≤ x := by
  intro x
  exact (hGred (F x)).trans (hFred x)

variable [WellFoundedLT α]

/--
Repeated composition stabilizes at the greatest common fixed point below the
initial state.
-/
theorem stabilize_comp_isGreatest_common (F G : α → α)
    (hFmono : Monotone F) (hGmono : Monotone G)
    (hFred : ∀ x, F x ≤ x) (hGred : ∀ x, G x ≤ x) (x : α) :
    IsGreatest {y : α | F y = y ∧ G y = y ∧ y ≤ x}
      (stabilize (fun z => G (F z))
        (comp_monotone F G hFmono hGmono)
        (comp_reductive F G hFred hGred) x) := by
  let H : α → α := fun z => G (F z)
  have hHmono : Monotone H := comp_monotone F G hFmono hGmono
  have hHred : ∀ z, H z ≤ z := comp_reductive F G hFred hGred
  have hgreat := stabilize_isGreatest H hHmono hHred x
  refine ⟨?_, ?_⟩
  · have hHfix : H (stabilize H hHmono hHred x) = stabilize H hHmono hHred x :=
      hgreat.1.1
    have hcommon :
        F (stabilize H hHmono hHred x) = stabilize H hHmono hHred x ∧
          G (stabilize H hHmono hHred x) = stabilize H hHmono hHred x := by
      apply (comp_fixed_iff_common F G hFred hGred
        (stabilize H hHmono hHred x)).mp
      simpa [H] using hHfix
    exact ⟨hcommon.1, hcommon.2, hgreat.1.2⟩
  · intro y hy
    apply hgreat.2
    refine ⟨?_, hy.2.2⟩
    change G (F y) = y
    exact (comp_fixed_iff_common F G hFred hGred y).mpr ⟨hy.1, hy.2.1⟩

/--
The stabilized output of the two-letter reductive word is independent of the
order of the letters, even when the one-step compositions do not commute.
-/
theorem stabilize_comp_order_independent (F G : α → α)
    (hFmono : Monotone F) (hGmono : Monotone G)
    (hFred : ∀ x, F x ≤ x) (hGred : ∀ x, G x ≤ x) (x : α) :
    stabilize (fun z => G (F z))
        (comp_monotone F G hFmono hGmono)
        (comp_reductive F G hFred hGred) x =
      stabilize (fun z => F (G z))
        (comp_monotone G F hGmono hFmono)
        (comp_reductive G F hGred hFred) x := by
  have hFG := stabilize_comp_isGreatest_common F G hFmono hGmono hFred hGred x
  have hGF := stabilize_comp_isGreatest_common G F hGmono hFmono hGred hFred x
  apply le_antisymm
  · exact hGF.2 ⟨hFG.1.2.1, hFG.1.1, hFG.1.2.2⟩
  · exact hFG.2 ⟨hGF.1.2.1, hGF.1.1, hGF.1.2.2⟩

end EnterpriseMath.ReductiveCompositionStabilization
