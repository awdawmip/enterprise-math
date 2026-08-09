import EnterpriseMath.Order.WellFoundedStabilization

namespace EnterpriseMath.Coalescence

open Function
open EnterpriseMath.WellFoundedStabilization

/-- Two states have coalesced by common deterministic time `n` exactly when the
same `n`-fold iterate sends them to one state. -/
def CoalescedBy {α : Type*} (F : α → α) (n : ℕ) (x y : α) : Prop :=
  F^[n] x = F^[n] y

/-- Eventual coalescence is witnessed by one finite common iterate. -/
def EventuallyCoalesce {α : Type*} (F : α → α) (x y : α) : Prop :=
  ∃ n : ℕ, CoalescedBy F n x y

@[simp] theorem coalescedBy_zero_iff {α : Type*} (F : α → α) (x y : α) :
    CoalescedBy F 0 x y ↔ x = y := by
  rfl

/-- Once a pair has entered the diagonal, every later common iterate keeps it
there. This is the subtraction-free kernel-filtration monotonicity law. -/
theorem coalescedBy_mono {α : Type*} {F : α → α} {n m : ℕ} {x y : α}
    (hnm : n ≤ m) (hxy : CoalescedBy F n x y) : CoalescedBy F m x y := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hnm
  unfold CoalescedBy at hxy ⊢
  rw [Nat.add_comm, Function.iterate_add_apply F k n x,
    Function.iterate_add_apply F k n y, hxy]

/-- Two finite coalescence witnesses can always be transported to their common
maximum time. This is the relation-level precursor of the merger-time
ultrametric inequality. -/
theorem coalescedBy_max {α : Type*} {F : α → α} {a b : ℕ} {x y z : α}
    (hxy : CoalescedBy F a x y) (hyz : CoalescedBy F b y z) :
    CoalescedBy F (max a b) x z := by
  exact (coalescedBy_mono (Nat.le_max_left _ _) hxy).trans
    (coalescedBy_mono (Nat.le_max_right _ _) hyz)

theorem eventuallyCoalesce_refl {α : Type*} (F : α → α) (x : α) :
    EventuallyCoalesce F x x := by
  exact ⟨0, rfl⟩

theorem eventuallyCoalesce_symm {α : Type*} {F : α → α} {x y : α}
    (h : EventuallyCoalesce F x y) : EventuallyCoalesce F y x := by
  obtain ⟨n, hn⟩ := h
  exact ⟨n, hn.symm⟩

theorem eventuallyCoalesce_trans {α : Type*} {F : α → α} {x y z : α}
    (hxy : EventuallyCoalesce F x y) (hyz : EventuallyCoalesce F y z) :
    EventuallyCoalesce F x z := by
  obtain ⟨a, ha⟩ := hxy
  obtain ⟨b, hb⟩ := hyz
  exact ⟨max a b, coalescedBy_max ha hb⟩

/-- Stabilizing after one ordinary step gives the same canonical fixed point. -/
theorem stabilize_step_invariant
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) (x : α) :
    stabilize F hmono hred (F x) = stabilize F hmono hred x := by
  apply le_antisymm
  · exact fixed_le_stabilize F hmono hred
      (stabilize_fixed F hmono hred (F x))
      ((stabilize_le F hmono hred (F x)).trans (hred x))
  · apply fixed_le_stabilize F hmono hred (stabilize_fixed F hmono hred x)
    calc
      stabilize F hmono hred x = F (stabilize F hmono hred x) :=
        (stabilize_fixed F hmono hred x).symm
      _ ≤ F x := hmono (stabilize_le F hmono hred x)

/-- Stabilization is invariant under every finite prefix of the same dynamics. -/
theorem stabilize_iterate_invariant
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) :
    ∀ n x, stabilize F hmono hred (F^[n] x) = stabilize F hmono hred x := by
  intro n
  induction n with
  | zero =>
      intro x
      rfl
  | succ n ih =>
      intro x
      rw [Function.iterate_succ_apply]
      calc
        stabilize F hmono hred (F^[n] (F x)) = stabilize F hmono hred (F x) := ih (F x)
        _ = stabilize F hmono hred x := stabilize_step_invariant F hmono hred x

/-- Under the P020 hypotheses, eventual finite coalescence forces equality of
canonical stabilized states. -/
theorem eventuallyCoalesce_stabilize_eq
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) {x y : α}
    (h : EventuallyCoalesce F x y) :
    stabilize F hmono hred x = stabilize F hmono hred y := by
  obtain ⟨n, hn⟩ := h
  calc
    stabilize F hmono hred x = stabilize F hmono hred (F^[n] x) :=
      (stabilize_iterate_invariant F hmono hred n x).symm
    _ = stabilize F hmono hred (F^[n] y) := congrArg (stabilize F hmono hred) hn
    _ = stabilize F hmono hred y := stabilize_iterate_invariant F hmono hred n y

/-- Each state is coalesced with its canonical stabilized state by the selected
finite P020 stabilization witness. -/
theorem coalescedBy_stabilizationSteps
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) (x : α) :
    CoalescedBy F (stabilizationSteps F hmono hred x) x
      (stabilize F hmono hred x) := by
  unfold CoalescedBy
  calc
    F^[stabilizationSteps F hmono hred x] x = stabilize F hmono hred x :=
      (stabilize_eq_iterate F hmono hred x).symm
    _ = F^[stabilizationSteps F hmono hred x] (stabilize F hmono hred x) :=
      (Function.iterate_fixed (stabilize_fixed F hmono hred x)
        (stabilizationSteps F hmono hred x)).symm

/-- P018-T133 formalized without introducing a minimum-time operator: if two
states have the same stabilized state, the maximum of their selected finite
P020 stabilization witnesses is already a common coalescence time. -/
theorem stabilize_eq_coalescedBy_max
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) {x y : α}
    (hstab : stabilize F hmono hred x = stabilize F hmono hred y) :
    CoalescedBy F
      (max (stabilizationSteps F hmono hred x) (stabilizationSteps F hmono hred y))
      x y := by
  let m := max (stabilizationSteps F hmono hred x) (stabilizationSteps F hmono hred y)
  have hx : CoalescedBy F m x (stabilize F hmono hred x) :=
    coalescedBy_mono (Nat.le_max_left _ _)
      (coalescedBy_stabilizationSteps F hmono hred x)
  have hy : CoalescedBy F m y (stabilize F hmono hred y) :=
    coalescedBy_mono (Nat.le_max_right _ _)
      (coalescedBy_stabilizationSteps F hmono hred y)
  unfold CoalescedBy at hx hy ⊢
  calc
    F^[m] x = F^[m] (stabilize F hmono hred x) := hx
    _ = F^[m] (stabilize F hmono hred y) := congrArg (F^[m]) hstab
    _ = F^[m] y := hy.symm

/-- Equality of P020 stabilized states therefore implies finite eventual
coalescence, witnessed at the explicit max time above. -/
theorem stabilize_eq_eventuallyCoalesce
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) {x y : α}
    (hstab : stabilize F hmono hred x = stabilize F hmono hred y) :
    EventuallyCoalesce F x y := by
  exact ⟨_, stabilize_eq_coalescedBy_max F hmono hred hstab⟩

/-- P018-T132 formalized: under P020's well-founded monotone reductive
hypotheses, two states coalesce in finite common time iff their canonical
stabilized states agree. -/
theorem eventuallyCoalesce_iff_stabilize_eq
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) (x y : α) :
    EventuallyCoalesce F x y ↔
      stabilize F hmono hred x = stabilize F hmono hred y := by
  constructor
  · exact eventuallyCoalesce_stabilize_eq F hmono hred
  · exact stabilize_eq_eventuallyCoalesce F hmono hred

end EnterpriseMath.Coalescence
