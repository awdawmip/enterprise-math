import Mathlib.Order.GaloisConnection.Basic
import EnterpriseMath.Order.WellFoundedStabilization

namespace EnterpriseMath.AdjointReductiveDuality

open EnterpriseMath.WellFoundedStabilization

variable {α : Type*} [PartialOrder α]

/--
If the right adjoint of a Galois connection is reductive, then the left adjoint
is extensive.  This is the order-dual motion underlying P024 boundary pullback.
-/
theorem left_extensive_of_right_reductive {l u : α → α} (gc : GaloisConnection l u)
    (hred : ∀ x, u x ≤ x) : ∀ x, x ≤ l x := by
  intro x
  have hx : x ≤ u (l x) := (gc x (l x)).mp le_rfl
  exact hx.trans (hred (l x))

/--
Under reductivity of the right adjoint, the two adjoints have exactly the same
fixed points.
-/
theorem left_fixed_iff_right_fixed {l u : α → α} (gc : GaloisConnection l u)
    (hred : ∀ x, u x ≤ x) (x : α) : l x = x ↔ u x = x := by
  have hext : x ≤ l x := left_extensive_of_right_reductive gc hred x
  constructor
  · intro hl
    have hxle : x ≤ u x := by
      apply (gc x x).mp
      rw [hl]
    exact le_antisymm (hred x) hxle
  · intro hu
    have hlx : l x ≤ x := by
      apply (gc x x).mpr
      rw [hu]
    exact le_antisymm hlx hext

variable [WellFoundedGT α]

/--
A monotone extensive endomap on an upward-well-founded partial order reaches,
after finitely many ordinary iterations, the least fixed point above the initial
state.  This is the order-dual of P020's reductive stabilization theorem.
-/
theorem exists_iterate_isLeast (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x)
    (x : α) : ∃ n : ℕ, IsLeast {y : α | L y = y ∧ x ≤ y} (L^[n] x) := by
  induction x using WellFoundedGT.induction with
  | ind x ih =>
      by_cases hfix : L x = x
      · refine ⟨0, ?_⟩
        change IsLeast {y : α | L y = y ∧ x ≤ y} x
        refine ⟨⟨hfix, le_rfl⟩, ?_⟩
        intro y hy
        exact hy.2
      · have hlt : x < L x := lt_of_le_of_ne (hext x) (Ne.symm hfix)
        obtain ⟨n, hn⟩ := ih (L x) hlt
        refine ⟨n.succ, ?_⟩
        change IsLeast {y : α | L y = y ∧ x ≤ y} (L^[n] (L x))
        refine ⟨⟨hn.1.1, (hext x).trans hn.1.2⟩, ?_⟩
        intro y hy
        apply hn.2
        refine ⟨hy.1, ?_⟩
        calc
          L x ≤ L y := hmono hy.2
          _ = y := hy.1

/-- A canonical finite iteration count reaching the least fixed point above `x`. -/
noncomputable def coStabilizationSteps (L : α → α) (hmono : Monotone L)
    (hext : ∀ x, x ≤ L x) (x : α) : ℕ :=
  Classical.choose (exists_iterate_isLeast L hmono hext x)

/-- The canonical upward-stabilized state selected by finite iteration. -/
noncomputable def coStabilize (L : α → α) (hmono : Monotone L)
    (hext : ∀ x, x ≤ L x) (x : α) : α :=
  L^[coStabilizationSteps L hmono hext x] x

/-- The selected upward finite iterate is the least fixed point above the initial state. -/
theorem coStabilize_isLeast (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x)
    (x : α) : IsLeast {y : α | L y = y ∧ x ≤ y} (coStabilize L hmono hext x) := by
  unfold coStabilize coStabilizationSteps
  exact Classical.choose_spec (exists_iterate_isLeast L hmono hext x)

/-- Upward stabilization always lands at an original fixed point. -/
theorem coStabilize_fixed (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x)
    (x : α) : L (coStabilize L hmono hext x) = coStabilize L hmono hext x :=
  (coStabilize_isLeast L hmono hext x).1.1

/-- Upward stabilization never moves downward. -/
theorem le_coStabilize (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x)
    (x : α) : x ≤ coStabilize L hmono hext x :=
  (coStabilize_isLeast L hmono hext x).1.2

/-- Every original fixed point above `x` lies above the upward-stabilized state. -/
theorem coStabilize_le_fixed (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x)
    {x y : α} (hyfix : L y = y) (hxy : x ≤ y) : coStabilize L hmono hext x ≤ y :=
  (coStabilize_isLeast L hmono hext x).2 ⟨hyfix, hxy⟩

/-- An original fixed point is unchanged by upward stabilization. -/
theorem coStabilize_eq_of_fixed (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x)
    {x : α} (hfix : L x = x) : coStabilize L hmono hext x = x := by
  apply le_antisymm
  · exact coStabilize_le_fixed L hmono hext hfix le_rfl
  · exact le_coStabilize L hmono hext x

/-- Upward stabilization is idempotent. -/
theorem coStabilize_idempotent (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x)
    (x : α) :
    coStabilize L hmono hext (coStabilize L hmono hext x) = coStabilize L hmono hext x := by
  exact coStabilize_eq_of_fixed L hmono hext (coStabilize_fixed L hmono hext x)

/-- Upward stabilization preserves monotonicity. -/
theorem coStabilize_mono (L : α → α) (hmono : Monotone L) (hext : ∀ x, x ≤ L x) :
    Monotone (coStabilize L hmono hext) := by
  intro x y hxy
  apply coStabilize_le_fixed L hmono hext (coStabilize_fixed L hmono hext y)
  exact hxy.trans (le_coStabilize L hmono hext y)

variable [WellFoundedLT α]

/--
If `l ⊣ u` and the right adjoint `u` is reductive, then finite upward
stabilization of `l` remains left adjoint to P020 finite downward stabilization
of `u`.  The two stabilized maps select the least/greatest common fixed states
above/below their inputs.
-/
theorem coStabilize_stabilize_gc {l u : α → α} (gc : GaloisConnection l u)
    (hred : ∀ x, u x ≤ x) :
    GaloisConnection
      (coStabilize l gc.monotone_l (left_extensive_of_right_reductive gc hred))
      (stabilize u gc.monotone_u hred) := by
  let hext : ∀ x, x ≤ l x := left_extensive_of_right_reductive gc hred
  intro x y
  constructor
  · intro hxy
    have hlfixed : l (coStabilize l gc.monotone_l hext x) = coStabilize l gc.monotone_l hext x :=
      coStabilize_fixed l gc.monotone_l hext x
    have hufixed : u (coStabilize l gc.monotone_l hext x) = coStabilize l gc.monotone_l hext x :=
      (left_fixed_iff_right_fixed gc hred (coStabilize l gc.monotone_l hext x)).mp hlfixed
    have hfixed_le : coStabilize l gc.monotone_l hext x ≤ stabilize u gc.monotone_u hred y :=
      fixed_le_stabilize u gc.monotone_u hred hufixed hxy
    exact (le_coStabilize l gc.monotone_l hext x).trans hfixed_le
  · intro hxy
    have hufixed : u (stabilize u gc.monotone_u hred y) = stabilize u gc.monotone_u hred y :=
      stabilize_fixed u gc.monotone_u hred y
    have hlfixed : l (stabilize u gc.monotone_u hred y) = stabilize u gc.monotone_u hred y :=
      (left_fixed_iff_right_fixed gc hred (stabilize u gc.monotone_u hred y)).mpr hufixed
    have hco : coStabilize l gc.monotone_l hext x ≤ stabilize u gc.monotone_u hred y :=
      coStabilize_le_fixed l gc.monotone_l hext hlfixed hxy
    exact hco.trans (stabilize_le u gc.monotone_u hred y)

end EnterpriseMath.AdjointReductiveDuality
