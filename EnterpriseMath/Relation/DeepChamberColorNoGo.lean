import EnterpriseMath.Relation.BranchRecoalescence
import Mathlib.Tactic

namespace EnterpriseMath.DeepChamberColorNoGo

open EnterpriseMath.BranchRecoalescence

/--
A deepest degree-three cutoff state retains the unique uncut history position
and the lower arithmetic endpoint.
-/
abbrev DeepState := Fin 3 × ℕ

/-- Forgetful scalar endpoint projection. -/
def scalarEndpoint (s : DeepState) : ℕ :=
  s.2

/-- The chamber color is the unique uncut history position. -/
def chamberColor (s : DeepState) : Fin 3 :=
  s.1

/-- Full colored endpoint key. -/
def coloredEndpoint (s : DeepState) : Fin 3 × ℕ :=
  (chamberColor s, scalarEndpoint s)

/-- The colored key recovers both the endpoint and the chamber color. -/
theorem coloredEndpoint_recovers :
    Recovers coloredEndpoint
      (fun s : DeepState => (chamberColor s, scalarEndpoint s)) := by
  exact ⟨id, fun _ => rfl⟩

/-- Two deepest states may share one scalar endpoint while carrying distinct colors. -/
theorem scalarEndpoint_collision (m : ℕ) :
    scalarEndpoint ((0 : Fin 3), m) =
      scalarEndpoint ((1 : Fin 3), m) := by
  rfl

/-- The same two states have different chamber colors. -/
theorem chamberColor_collision_ne (m : ℕ) :
    chamberColor ((0 : Fin 3), m) ≠
      chamberColor ((1 : Fin 3), m) := by
  decide

/-- The scalar lower endpoint cannot recover the deepest chamber color. -/
theorem scalarEndpoint_not_recovers_chamberColor :
    ¬ Recovers scalarEndpoint chamberColor := by
  intro h
  have hsame : chamberColor ((0 : Fin 3), 0) =
      chamberColor ((1 : Fin 3), 0) :=
    noResurrection h (scalarEndpoint_collision 0)
  exact chamberColor_collision_ne 0 hsame

/-- A concrete standard-sector color observable. -/
def standardColorObservable : DeepState → ℤ
  | ⟨0, _⟩ => 1
  | ⟨1, _⟩ => -1
  | ⟨2, _⟩ => 0

/-- The scalar endpoint also cannot recover a nontrivial standard color observable. -/
theorem scalarEndpoint_not_recovers_standardColorObservable :
    ¬ Recovers scalarEndpoint standardColorObservable := by
  intro h
  have hsame : standardColorObservable ((0 : Fin 3), 0) =
      standardColorObservable ((1 : Fin 3), 0) :=
    noResurrection h (scalarEndpoint_collision 0)
  norm_num [standardColorObservable] at hsame

end EnterpriseMath.DeepChamberColorNoGo
