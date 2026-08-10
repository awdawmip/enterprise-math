import Mathlib
import EnterpriseMath.R009.ScaleNaturalLiftTargets

namespace EnterpriseMath.R009

/-- Compatible inverse-limit endpoint coordinates.

The frozen R009 endpoint is indexed only by positive scales. The total-Nat
representation used for Lean therefore fixes the unused coordinate `a 0` to
zero. This is a representation normalization, not an extra mathematical
hypothesis at any positive scale. -/
def Endpoint (a : ℕ → ℕ) : Prop :=
  a 0 = 0 ∧
  (∀ d, 0 < d → a d < d) ∧
  (∀ d r, 0 < d → 0 < r → a (d * r) / r = a d)

def LevelMonotone (P : ScaleFamily) : Prop :=
  ∀ d s t, 0 < d → s < d → t < d → s ≤ t → P d s ≤ P d t

def LevelReductive (P : ScaleFamily) : Prop :=
  ∀ d s, 0 < d → s < d → P d s ≤ s

def LevelIdempotent (P : ScaleFamily) : Prop :=
  ∀ d s, 0 < d → s < d → P d (P d s) = P d s

def T17Statement : Prop :=
  ∀ P : ScaleFamily, GridEndomorphism P → LevelMonotone P →
    LevelReductive P → LevelIdempotent P →
    ∃! a : ℕ → ℕ, Endpoint a ∧
      ∀ d s, 0 < d → s < d → P d s = min s (a d)

def ScaleDownward (F : ScaleFamily) : Prop :=
  ∀ d m, 0 < d → F d m ≤ m

def ScaleIdempotent (F : ScaleFamily) : Prop :=
  ∀ d m, 0 < d → F d (F d m) = F d m

def ScaleMonotone (F : ScaleFamily) : Prop :=
  ∀ d, 0 < d → Monotone (F d)

def T18Statement : Prop :=
  ∀ p : ℕ, 1 ≤ p → ∀ F : ScaleFamily,
    F 1 = collapse p →
    (ScaleNatural F ∧ ScaleDownward F ∧ ScaleIdempotent F ∧ ScaleMonotone F ↔
      ∃ a : ℕ → ℕ → ℕ,
        (∀ k, Endpoint (a k)) ∧
        ∀ d q s, 0 < d → s < d →
          let k := Nat.nthRoot p q
          F d (d * q + s) =
            d * collapse p q +
              (if q = k ^ p then min s (a k d) else a k d))

end EnterpriseMath.R009
