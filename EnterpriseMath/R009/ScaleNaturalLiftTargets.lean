import Mathlib

/-!
R011/R009 freeze formalization staging.

IMPORTANT: this module was authored against the canonical dependency snapshot
enterprise-math@9fec0e9b270c00b6cd6b364d153d6e480cbc076d,
Lean v4.33.0-rc2, mathlib@87adeaebd370a3b6a41ac4f044fddd4bf81803ad.
The current runtime contains no `lean`/`lake` binary, so this file is NOT BUILD VALIDATED.
Definitions below encode the frozen theorem propositions without `sorry` or `axiom`.
No proposition is `LEAN_CHECKED` until the taskbook build command succeeds.
-/

namespace EnterpriseMath.R009

abbrev ScaleFamily := ℕ → ℕ → ℕ

/-- Strict divisibility-scale naturality for the edge `d*r → d`. -/
def ScaleNatural (F : ScaleFamily) : Prop :=
  ∀ d r m : ℕ, 0 < d → 0 < r → F (d * r) m / r = F d (m / r)

def zeroResidueLift (H : ℕ → ℕ) : ScaleFamily :=
  fun d m => d * H (m / d)

def upperResidueLift (H : ℕ → ℕ) : ScaleFamily :=
  fun d m => d * H (m / d) + (d - 1)

/-- T01 frozen proposition. -/
def T01Statement : Prop :=
  ∀ H : ℕ → ℕ, ScaleNatural (zeroResidueLift H)

/-- A residue presentation used only to state T02/T03 without inventing a new theorem. -/
def ResidueNormalForm (F : ScaleFamily) (H : ℕ → ℕ) (ρ : ScaleFamily) : Prop :=
  ∀ d m : ℕ, 0 < d → ρ d m < d ∧ F d m = d * H (m / d) + ρ d m

/-- T02 frozen proposition. -/
def T02Statement : Prop :=
  ∀ (F : ScaleFamily) (H : ℕ → ℕ), ScaleNatural F → F 1 = H →
    ∀ d m : ℕ, 0 < d → ∃! ρ : ℕ, ρ < d ∧ F d m = d * H (m / d) + ρ

def ResidueCoherent (ρ : ScaleFamily) : Prop :=
  ∀ d r m : ℕ, 0 < d → 0 < r → ρ (d * r) m / r = ρ d (m / r)

/-- T03 frozen proposition, under the T02 normal form. -/
def T03Statement : Prop :=
  ∀ (F ρ : ScaleFamily) (H : ℕ → ℕ), ResidueNormalForm F H ρ →
    (ScaleNatural F ↔ ResidueCoherent ρ)

/-- Coherent finite-grid endomorphism predicate used to state T09. -/
def GridEndomorphism (φ : ScaleFamily) : Prop :=
  (∀ d s : ℕ, 0 < d → s < d → φ d s < d) ∧
  (∀ d r t : ℕ, 0 < d → 0 < r → t < d * r →
    φ (d * r) t / r = φ d (t / r))

/-- T09: adjacent output indices differ by at most one. -/
def T09Statement : Prop :=
  ∀ φ : ScaleFamily, GridEndomorphism φ →
    ∀ d s : ℕ, 0 < d → s + 1 < d →
      φ d (s + 1) ≤ φ d s + 1 ∧ φ d s ≤ φ d (s + 1) + 1

/-- Mathlib-native floor nth-root collapse. -/
def collapse (p q : ℕ) : ℕ := (Nat.nthRoot p q) ^ p

/-- T12 frozen proposition in quotient-block form. -/
def T12Statement : Prop :=
  ∀ p d q s φ : ℕ, 0 < p → 0 < d → s < d → φ < d →
    (d * collapse p q + φ ≤ d * q + s ↔ φ ≤ d * (q - collapse p q) + s)

/-- T14 algebraic equation, stated at the weaker assumption boundary found by R011. -/
def T14Statement : Prop :=
  ∀ (C : ℕ → ℕ) (φ : ℕ → ℕ → ℕ → ℕ),
    (∀ q, C (C q) = C q) →
    ∀ d q s, 0 < d → s < d → φ q d s < d →
      let F : ℕ → ℕ := fun m =>
        d * C (m / d) + φ (m / d) d (m % d)
      (F (F (d * q + s)) = F (d * q + s) ↔
        φ (C q) d (φ q d s) = φ q d s)

/-- Every output is a bare p-th power. -/
def BarePerfectPowerOutputs (p : ℕ) (F : ScaleFamily) : Prop :=
  ∀ d m : ℕ, 0 < d → ∃ k : ℕ, F d m = k ^ p

/-- T22 frozen proposition. -/
def T22Statement : Prop :=
  ∀ p : ℕ, 2 ≤ p → ¬ ∃ F : ScaleFamily,
    ScaleNatural F ∧ F 1 = collapse p ∧ BarePerfectPowerOutputs p F

/-- Pointwise order on ordinary functions. -/
def EndLE (H K : ℕ → ℕ) : Prop := ∀ n, H n ≤ K n
/-- Pointwise order on positive scales. -/
def ScaleLE (F G : ScaleFamily) : Prop := ∀ d m, 0 < d → F d m ≤ G d m

/-- T23, written as the two adjunction equivalences before subtype packaging. -/
def T23Statement : Prop :=
  (∀ (H : ℕ → ℕ) (F : ScaleFamily), ScaleNatural F →
      (ScaleLE (zeroResidueLift H) F ↔ EndLE H (F 1))) ∧
  (∀ (H : ℕ → ℕ) (F : ScaleFamily), ScaleNatural F →
      (ScaleLE F (upperResidueLift H) ↔ EndLE (F 1) H))

end EnterpriseMath.R009
