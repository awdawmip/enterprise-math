namespace EnterpriseMath.ReductiveWord

variable {α : Type*} [PartialOrder α]

/-- Apply a finite word of endomaps from left to right. -/
def applyWord : List (α → α) → α → α
  | [], x => x
  | f :: fs, x => applyWord fs (f x)

/-- A finite word of reductive maps is itself reductive. -/
theorem applyWord_le (fs : List (α → α))
    (hred : ∀ f ∈ fs, ∀ x, f x ≤ x) (x : α) :
    applyWord fs x ≤ x := by
  induction fs generalizing x with
  | nil =>
      exact le_rfl
  | cons f fs ih =>
      have hf : ∀ y, f y ≤ y := hred f (by simp)
      have htail : ∀ g ∈ fs, ∀ y, g y ≤ y := by
        intro g hg
        exact hred g (by simp [hg])
      exact le_trans (ih htail (f x)) (hf x)

/-- P004-T01: the fixed points of a finite reductive word are exactly the common fixed points. -/
theorem applyWord_eq_self_iff (fs : List (α → α))
    (hred : ∀ f ∈ fs, ∀ x, f x ≤ x) (x : α) :
    applyWord fs x = x ↔ ∀ f ∈ fs, f x = x := by
  induction fs generalizing x with
  | nil =>
      simp [applyWord]
  | cons f fs ih =>
      have hf : ∀ y, f y ≤ y := hred f (by simp)
      have htail : ∀ g ∈ fs, ∀ y, g y ≤ y := by
        intro g hg
        exact hred g (by simp [hg])
      constructor
      · intro hword
        have htail_le : applyWord fs (f x) ≤ f x :=
          applyWord_le fs htail (f x)
        have hx_le_fx : x ≤ f x := by
          rw [← hword]
          exact htail_le
        have hfx : f x = x := le_antisymm (hf x) hx_le_fx
        have htail_fix : applyWord fs x = x := by
          simpa [applyWord, hfx] using hword
        intro g hg
        rcases List.mem_cons.mp hg with rfl | hg
        · exact hfx
        · exact (ih htail x).1 htail_fix g hg
      · intro hall
        have hfx : f x = x := hall f (by simp)
        have htail_all : ∀ g ∈ fs, g x = x := by
          intro g hg
          exact hall g (by simp [hg])
        have htail_fix : applyWord fs x = x :=
          (ih htail x).2 htail_all
        simpa [applyWord, hfx] using htail_fix

end EnterpriseMath.ReductiveWord
