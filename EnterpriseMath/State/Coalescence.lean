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
there.  This is the subtraction-free kernel-filtration monotonicity law. -/
theorem coalescedBy_mono {α : Type*} {F : α → α} {n m : ℕ} {x y : α}
    (hnm : n ≤ m) (hxy : CoalescedBy F n x y) : CoalescedBy F m x y := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hnm
  unfold CoalescedBy at hxy ⊢
  rw [Nat.add_comm, Function.iterate_add_apply F k n x,
    Function.iterate_add_apply F k n y, hxy]

/-- Two finite coalescence witnesses can always be transported to their common
maximum time. -/
theorem coalescedBy_max {α : Type*} {F : α → α} {a b : ℕ} {x y z : α}
    (hxy : CoalescedBy F a x y) (hyz : CoalescedBy F b y z) :
    CoalescedBy F (max a b) x z := by
  exact (coalescedBy_mono (Nat.le_max_left _ _) hxy).trans
    (coalescedBy_mono (Nat.le_max_right _ _) hyz)

@[refl] theorem eventuallyCoalesce_refl {α : Type*} (F : α → α) (x : α) :
    EventuallyCoalesce F x x := by
  exact ⟨0, rfl⟩

@[symm] theorem eventuallyCoalesce_symm {α : Type*} {F : α → α} {x y : α}
    (h : EventuallyCoalesce F x y) : EventuallyCoalesce F y x := by
  obtain ⟨n, hn⟩ := h
  exact ⟨n, hn.symm⟩

@[trans] theorem eventuallyCoalesce_trans {α : Type*} {F : α → α} {x y z : α}
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

/-- If two states have the same P020 stabilized state, the sum of their selected
finite stabilization witnesses is already a common finite coalescence time. -/
theorem stabilize_eq_eventuallyCoalesce
    {α : Type*} [PartialOrder α] [WellFoundedLT α]
    (F : α → α) (hmono : Monotone F) (hred : ∀ x, F x ≤ x) {x y : α}
    (hstab : stabilize F hmono hred x = stabilize F hmono hred y) :
    EventuallyCoalesce F x y := by
  let sx := stabilizationSteps F hmono hred x
  let sy := stabilizationSteps F hmono hred y
  refine ⟨sx + sy, ?_⟩
  unfold CoalescedBy
  calc
    F^[sx + sy] x = F^[sy + sx] x := by rw [Nat.add_comm]
    _ = F^[sy] (F^[sx] x) := Function.iterate_add_apply F sy sx x
    _ = F^[sy] (stabilize F hmono hred x) := by
      rw [stabilize_eq_iterate F hmono hred x]
    _ = stabilize F hmono hred x :=
      Function.iterate_fixed (stabilize_fixed F hmono hred x) sy
    _ = stabilize F hmono hred y := hstab
    _ = F^[sx] (stabilize F hmono hred y) :=
      (Function.iterate_fixed (stabilize_fixed F hmono hred y) sx).symm
    _ = F^[sx] (F^[sy] y) := by
      rw [← stabilize_eq_iterate F hmono hred y]
    _ = F^[sx + sy] y := (Function.iterate_add_apply F sx sy y).symm

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
