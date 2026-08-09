import EnterpriseMath.State.OperationCongruence
import Mathlib.Logic.Function.Basic

namespace EnterpriseMath.TransportProtocol

open Function
open EnterpriseMath.OperationCongruence

/-- An exact deterministic one-message transport protocol for one `k`-ary
operation call. The decoder knows the entire coarse input tuple and receives one
token computed from the fine input tuple. -/
structure Protocol
    {α β C : Type*} {k : ℕ}
    (O : α → β) (μ : (Fin k → α) → α) where
  encode : (Fin k → α) → C
  decode : (Fin k → β) → C → β
  correct : ∀ x : Fin k → α,
    decode (fun i ↦ O (x i)) (encode x) = O (μ x)

/-- If two fine tuples have the same coarse inputs and receive the same token,
then exact decoding forces the same coarse output. -/
theorem coarse_inputs_token_eq_forces_output_eq
    {α β C : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (P : Protocol O μ (C := C))
    {x y : Fin k → α}
    (hinputs : ∀ i : Fin k, O (x i) = O (y i))
    (htoken : P.encode x = P.encode y) :
    O (μ x) = O (μ y) := by
  have hcoarse : (fun i ↦ O (x i)) = (fun i ↦ O (y i)) := by
    funext i
    exact hinputs i
  calc
    O (μ x) = P.decode (fun i ↦ O (x i)) (P.encode x) := (P.correct x).symm
    _ = P.decode (fun i ↦ O (y i)) (P.encode y) := by rw [hcoarse, htoken]
    _ = O (μ y) := P.correct y

/-- P018-T200 lower-bound core: inside one coarse input cell, two different
coarse outputs must receive different transport tokens in every exact protocol. -/
theorem output_ne_forces_token_ne
    {α β C : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (P : Protocol O μ (C := C))
    {x y : Fin k → α}
    (hinputs : ∀ i : Fin k, O (x i) = O (y i))
    (houtput : O (μ x) ≠ O (μ y)) :
    P.encode x ≠ P.encode y := by
  intro htoken
  exact houtput (coarse_inputs_token_eq_forces_output_eq P hinputs htoken)

/-- A one-symbol token type can carry no extra distinction beyond the coarse
input tuple, so any exact protocol with a subsingleton token alphabet forces
operation congruence. -/
theorem subsingleton_protocol_compatible
    {α β C : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    [Subsingleton C]
    (P : Protocol O μ (C := C)) :
    ObservationCompatible O μ := by
  intro x y hinputs
  exact coarse_inputs_token_eq_forces_output_eq P hinputs (Subsingleton.elim _ _)

/-- Any descended coarse operation yields an exact protocol with the one-symbol
`Unit` token alphabet. -/
def unitProtocolOfDescended
    {α β : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (ν : (Fin k → β) → β)
    (hν : ∀ x : Fin k → α, O (μ x) = ν (fun i ↦ O (x i))) :
    Protocol O μ (C := Unit) where
  encode := fun _ ↦ ()
  decode := fun observed _ ↦ ν observed
  correct := fun x ↦ (hν x).symm

/-- Under a surjective observation, operation compatibility is equivalent to the
existence of an exact transport protocol whose token type has only one value.
This is the formal relation-level core of `B_E(mu)=1`. -/
theorem exists_unit_protocol_iff_compatible
    {α β : Type*} {k : ℕ}
    {O : α → β} {μ : (Fin k → α) → α}
    (hO : Surjective O) :
    Nonempty (Protocol O μ (C := Unit)) ↔ ObservationCompatible O μ := by
  constructor
  · rintro ⟨P⟩
    exact subsingleton_protocol_compatible P
  · intro hcomp
    obtain ⟨ν, hν⟩ := compatible_operationDescends hO hcomp
    exact ⟨unitProtocolOfDescended ν hν⟩

end EnterpriseMath.TransportProtocol
