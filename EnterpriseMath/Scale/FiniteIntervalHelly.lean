import Mathlib.Data.Finset.Max
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Finite one-dimensional Helly lemma for integer intervals.

If a nonempty finite family of closed integer intervals is pairwise intersecting,
then all intervals have a common integer point. Choosing the largest lower endpoint
is already sufficient. -/
theorem finite_natInterval_helly
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (hs : s.Nonempty)
    (lo hi : ι → ℕ)
    (hpair : ∀ i ∈ s, ∀ j ∈ s, lo i ≤ hi j ∧ lo j ≤ hi i) :
    ∃ x : ℕ, ∀ i ∈ s, lo i ≤ x ∧ x ≤ hi i := by
  obtain ⟨i₀, hi₀s, hmax⟩ := Finset.exists_max_image s lo hs
  refine ⟨lo i₀, ?_⟩
  intro i his
  have hlow : lo i ≤ lo i₀ := hmax i his
  have hupp : lo i₀ ≤ hi i := (hpair i₀ hi₀s i his).1
  exact ⟨hlow, hupp⟩

/-- Equivalent interval-overlap formulation: if each pair of intervals has a common
integer point, then the whole finite family has one. -/
theorem finite_natInterval_helly_of_pairwise_witness
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (hs : s.Nonempty)
    (lo hi : ι → ℕ)
    (hpair : ∀ i ∈ s, ∀ j ∈ s,
      ∃ x : ℕ,
        lo i ≤ x ∧ x ≤ hi i ∧
        lo j ≤ x ∧ x ≤ hi j) :
    ∃ x : ℕ, ∀ i ∈ s, lo i ≤ x ∧ x ≤ hi i := by
  apply finite_natInterval_helly s hs lo hi
  intro i his j hjs
  obtain ⟨x, hli, hui, hlj, huj⟩ := hpair i his j hjs
  exact ⟨le_trans hli huj, le_trans hlj hui⟩

end EnterpriseMath.Scale
