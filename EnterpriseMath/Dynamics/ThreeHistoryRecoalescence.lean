import EnterpriseMath.Dynamics.HistoryMerge
import Mathlib.Data.Bool.Basic

namespace EnterpriseMath.ThreeHistoryRecoalescence

/-- The six ordering-provenance labels for three named operations. -/
inductive Order3 where
  | abc | acb | bac | bca | cab | cba
  deriving DecidableEq, Fintype

/-- The provenance carrier has exactly `3! = 6` labels. -/
theorem order3_card : Fintype.card Order3 = 6 := by
  native_decide

/-- Execute one of the six orderings of three named deterministic maps. -/
def runOrder3 {X : Type*} (f g h : X → X) : Order3 → X → X
  | .abc, x => h (g (f x))
  | .acb, x => g (h (f x))
  | .bac, x => h (f (g x))
  | .bca, x => f (h (g x))
  | .cab, x => g (f (h x))
  | .cba, x => f (g (h x))

/-- Pairwise commuting deterministic maps erase the ordering from the endpoint. -/
theorem runOrder3_eq_canonical {X : Type*} (f g h : X → X)
    (hfg : Function.Commute f g) (hfh : Function.Commute f h)
    (hgh : Function.Commute g h) (w : Order3) (x : X) :
    runOrder3 f g h w x = h (g (f x)) := by
  cases w with
  | abc => rfl
  | acb => exact hgh (f x)
  | bac => exact congrArg h (hfg x)
  | bca =>
      calc
        f (h (g x)) = h (f (g x)) := hfh (g x)
        _ = h (g (f x)) := congrArg h (hfg x)
  | cab =>
      calc
        g (f (h x)) = g (h (f x)) := congrArg g (hfh x)
        _ = h (g (f x)) := hgh (f x)
  | cba =>
      calc
        f (g (h x)) = g (f (h x)) := hfg (h x)
        _ = g (h (f x)) := congrArg g (hfh x)
        _ = h (g (f x)) := hgh (f x)

/-- Endpoint map from ordering provenance to the merged deterministic state. -/
def endpoint {X : Type*} (f g h : X → X) (x : X) : Order3 → X :=
  fun w => runOrder3 f g h w x

/-- Under pairwise commutation, every ordering label has the same endpoint. -/
theorem endpoint_eq {X : Type*} (f g h : X → X)
    (hfg : Function.Commute f g) (hfh : Function.Commute f h)
    (hgh : Function.Commute g h) (x : X) (u v : Order3) :
    endpoint f g h x u = endpoint f g h x v := by
  rw [endpoint, endpoint, runOrder3_eq_canonical f g h hfg hfh hgh u x,
    runOrder3_eq_canonical f g h hfg hfh hgh v x]

/--
Every merged endpoint has a six-element history fiber.  This is the literal
finite `S₃` provenance multiplicity before endpoint-only recoalescence.
-/
theorem endpoint_fiber_card_six {X : Type*} [DecidableEq X]
    (f g h : X → X) (hfg : Function.Commute f g)
    (hfh : Function.Commute f h) (hgh : Function.Commute g h)
    (x : X) (w : Order3) :
    (HistoryMerge.fiberFinset (endpoint f g h x) w).card = 6 := by
  classical
  have hall :
      HistoryMerge.fiberFinset (endpoint f g h x) w = Finset.univ := by
    ext u
    simp [HistoryMerge.fiberFinset,
      endpoint_eq f g h hfg hfh hgh x u w]
  rw [hall, Finset.card_univ, order3_card]

/-- A finite Hamming vertex is a Boolean coordinate assignment. -/
abbrev HammingVertex (m : ℕ) := Fin m → Bool

/-- Toggle one Hamming coordinate. -/
def hammingFlip {m : ℕ} (i : Fin m) (v : HammingVertex m) : HammingVertex m :=
  fun j => if j = i then Bool.not (v j) else v j

/-- Hamming coordinate flips commute exactly. -/
theorem hammingFlip_commute {m : ℕ} (i j : Fin m) :
    Function.Commute (hammingFlip i) (hammingFlip j) := by
  classical
  intro v
  funext k
  by_cases hki : k = i <;> by_cases hkj : k = j <;>
    simp [hammingFlip, hki, hkj]

/--
Any three named Hamming coordinate flips therefore have a literal six-label
ordering-provenance fiber over their common endpoint.
-/
theorem hamming_three_flip_fiber_card_six {m : ℕ} (i j k : Fin m)
    (v : HammingVertex m) (w : Order3) :
    (HistoryMerge.fiberFinset
      (endpoint (hammingFlip i) (hammingFlip j) (hammingFlip k) v) w).card = 6 := by
  exact endpoint_fiber_card_six
    (hammingFlip i) (hammingFlip j) (hammingFlip k)
    (hammingFlip_commute i j) (hammingFlip_commute i k)
    (hammingFlip_commute j k) v w

end EnterpriseMath.ThreeHistoryRecoalescence
