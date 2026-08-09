import Mathlib.Data.Set.Basic

namespace EnterpriseMath.CompositionSafeCollapse

variable {X Q R S : Type*}

/-- `h` is constant on every fiber of `q`; equivalently, `h` may be observed
without choosing a fine representative inside a `q`-class. -/
def FiberConstant (q : X → Q) (h : X → R) : Prop :=
  ∀ ⦃x y : X⦄, q x = q y → h x = h y

/--
A map on fine states factors uniquely through the represented range of a coarse
map exactly when it is constant on every coarse fiber.
-/
theorem exists_range_factor_iff_fiberConstant (q : X → Q) (h : X → R) :
    (∃ bar : Set.range q → R,
        ∀ x : X, bar ⟨q x, ⟨x, rfl⟩⟩ = h x) ↔ FiberConstant q h := by
  constructor
  · rintro ⟨bar, hbar⟩ x y hxy
    have hsub :
        (⟨q x, ⟨x, rfl⟩⟩ : Set.range q) =
          ⟨q y, ⟨y, rfl⟩⟩ := by
      exact Subtype.ext hxy
    calc
      h x = bar ⟨q x, ⟨x, rfl⟩⟩ := (hbar x).symm
      _ = bar ⟨q y, ⟨y, rfl⟩⟩ := congrArg bar hsub
      _ = h y := hbar y
  · intro hconst
    classical
    let preimage : Set.range q → X := fun z => Classical.choose z.property
    refine ⟨fun z => h (preimage z), ?_⟩
    intro x
    apply hconst
    simpa [preimage] using
      (Classical.choose_spec (⟨q x, ⟨x, rfl⟩⟩ : Set.range q).property)

/-- The canonical one-step repair remembers the old coarse label and exactly
one failed future observable. -/
def repair (q : X → Q) (h : X → R) : X → Q × R :=
  fun x => (q x, h x)

/-- The repair never merges states that were already distinct at coarse level. -/
theorem repair_refines_coarse (q : X → Q) (h : X → R) :
    FiberConstant (repair q h) q := by
  intro x y hxy
  exact congrArg Prod.fst hxy

/-- The failed observable always descends through the repaired state. -/
theorem observable_descends_through_repair (q : X → Q) (h : X → R) :
    FiberConstant (repair q h) h := by
  intro x y hxy
  exact congrArg Prod.snd hxy

/--
Coarsest-repair theorem: any state map `s` that already refines `q` and makes
`h` fiber-constant must itself refine the pair repair `(q,h)`.
-/
theorem repair_coarsest (q : X → Q) (h : X → R) (s : X → S)
    (hsq : FiberConstant s q) (hsh : FiberConstant s h) :
    FiberConstant s (repair q h) := by
  intro x y hxy
  exact Prod.ext (hsq hxy) (hsh hxy)

/-- A quotient is transition-compatible when the transition induces a
well-defined endomap on quotient classes. -/
def TransitionCompatible (T : X → X) (q : X → Q) : Prop :=
  FiberConstant q (fun x => q (T x))

/--
For an idempotent transition, the one-step repair `(q, q ∘ T)` is already fully
transition-compatible. No second future-refinement round is needed.
-/
theorem repair_transitionCompatible_of_idempotent (T : X → X) (q : X → Q)
    (hT : Function.Idempotent T) :
    TransitionCompatible T (repair q (fun x => q (T x))) := by
  intro x y hxy
  have hnext : q (T x) = q (T y) := congrArg Prod.snd hxy
  apply Prod.ext
  · exact hnext
  · calc
      q (T (T x)) = q (T x) := congrArg q (hT x)
      _ = q (T y) := hnext
      _ = q (T (T y)) := (congrArg q (hT y)).symm

/--
Any quotient `s` that already refines `q` and supports `T` must refine the
canonical pair repair `(q, q ∘ T)`. Combined with idempotence, this makes the
pair repair the full coarsest `T`-compatible refinement of `q`.
-/
theorem repair_coarsest_transitionCompatible (T : X → X) (q : X → Q) (s : X → S)
    (hsq : FiberConstant s q) (hsT : TransitionCompatible T s) :
    FiberConstant s (repair q (fun x => q (T x))) := by
  apply repair_coarsest
  · exact hsq
  · intro x y hxy
    exact hsq (hsT hxy)

end EnterpriseMath.CompositionSafeCollapse
