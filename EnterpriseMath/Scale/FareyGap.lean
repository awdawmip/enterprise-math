import EnterpriseMath.Scale.FareyBridge
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Non-strict order of nonnegative fractions by cross multiplication. -/
def fracLe (a b c d : ℕ) : Prop :=
  a * d ≤ c * b

/-- Membership in a closed rational gap, expressed entirely by cross multiplication. -/
def fracInClosedGap (l ln u un x xn : ℕ) : Prop :=
  fracLe l ln x xn ∧ fracLe x xn u un

/-- A mediant of two fractions lying in the same closed gap remains in that gap. -/
theorem mediant_mem_closedGap {l ln u un p b q d : ℕ}
    (hp : fracInClosedGap l ln u un p b)
    (hq : fracInClosedGap l ln u un q d) :
    fracInClosedGap l ln u un (p + q) (b + d) := by
  unfold fracInClosedGap fracLe at hp hq ⊢
  rcases hp with ⟨hlp, hpu⟩
  rcases hq with ⟨hlq, hqu⟩
  constructor <;> nlinarith

/-- Between determinant-one neighbors, every strictly intermediate denominator is at
least the sum of the two endpoint denominators. -/
theorem denominator_add_le_of_between_left_det_one {a b m N x y : ℕ}
    (hdet : a * N + 1 = m * b)
    (hleft : fracLt a b x y) (hright : fracLt x y m N) :
    b + N ≤ y := by
  unfold fracLt at hleft hright
  have h₁ : a * y + 1 ≤ x * b := Nat.succ_le_iff.mpr hleft
  have h₂ : x * N + 1 ≤ m * y := Nat.succ_le_iff.mpr hright
  have h₁N := Nat.mul_le_mul_left N h₁
  have h₂b := Nat.mul_le_mul_left b h₂
  nlinarith [hdet]

/-- Right-hand version of the determinant-one denominator barrier. -/
theorem denominator_add_le_of_between_right_det_one {m N c d x y : ℕ}
    (hdet : m * d + 1 = c * N)
    (hleft : fracLt m N x y) (hright : fracLt x y c d) :
    N + d ≤ y := by
  unfold fracLt at hleft hright
  have h₁ : m * y + 1 ≤ x * N := Nat.succ_le_iff.mpr hleft
  have h₂ : x * d + 1 ≤ c * y := Nat.succ_le_iff.mpr hright
  have h₁d := Nat.mul_le_mul_left d h₁
  have h₂N := Nat.mul_le_mul_left N h₂
  nlinarith [hdet]

/-- No fraction of denominator `< N` can lie strictly between the left Farey parent
and the center fraction. -/
theorem no_small_denominator_between_left_parent {m N x y : ℕ}
    (P : FareyParentData m N) (hyN : y < N) :
    ¬ (fracLt P.a P.b x y ∧ fracLt x y m N) := by
  rintro ⟨h₁, h₂⟩
  have hden := denominator_add_le_of_between_left_det_one P.left_det h₁ h₂
  omega

/-- No fraction of denominator `< N` can lie strictly between the center fraction
and the right Farey parent. -/
theorem no_small_denominator_between_right_parent {m N x y : ℕ}
    (P : FareyParentData m N) (hyN : y < N) :
    ¬ (fracLt m N x y ∧ fracLt x y P.c P.d) := by
  rintro ⟨h₁, h₂⟩
  have hden := denominator_add_le_of_between_right_det_one P.right_det h₁ h₂
  omega

/-- An old lower endpoint below the center cannot sit to the right of the left parent;
therefore it is at or to the left of that parent. -/
theorem old_lower_le_left_parent {m N x y : ℕ}
    (P : FareyParentData m N) (hyN : y < N)
    (hcenter : fracLt x y m N) :
    fracLe x y P.a P.b := by
  unfold fracLe
  by_contra hnot
  have hparentLower : fracLt P.a P.b x y := by
    unfold fracLt
    omega
  exact no_small_denominator_between_left_parent P hyN ⟨hparentLower, hcenter⟩

/-- An old upper endpoint above the center cannot sit to the left of the right parent;
therefore the right parent is at or to the left of that endpoint. -/
theorem right_parent_le_old_upper {m N x y : ℕ}
    (P : FareyParentData m N) (hyN : y < N)
    (hcenter : fracLt m N x y) :
    fracLe P.c P.d x y := by
  unfold fracLe
  by_contra hnot
  have hparentUpper : fracLt x y P.c P.d := by
    unfold fracLt
    omega
  exact no_small_denominator_between_right_parent P hyN ⟨hcenter, hparentUpper⟩

/-- If a reduced center fraction lies in an open gap whose endpoint denominators are
both `< N`, then both Farey parents lie in the corresponding closed gap. -/
theorem fareyParents_mem_closedGap_of_center_mem {m N l ln u un : ℕ}
    (P : FareyParentData m N)
    (hln : ln < N) (hun : un < N)
    (hlc : fracLt l ln m N) (hcu : fracLt m N u un) :
    fracInClosedGap l ln u un P.a P.b ∧
      fracInClosedGap l ln u un P.c P.d := by
  have hleftLower : fracLe l ln P.a P.b := old_lower_le_left_parent P hln hlc
  have hrightUpper : fracLe P.c P.d u un := right_parent_le_old_upper P hun hcu
  have hparents := P.parents_straddle
  unfold fracInClosedGap
  constructor
  · refine ⟨hleftLower, ?_⟩
    unfold fracLe
    unfold fracLt at hparents hcu
    exact le_trans (Nat.le_of_lt hparents.1) (Nat.le_of_lt hcu)
  · refine ⟨?_, hrightUpper⟩
    unfold fracLe
    unfold fracLt at hparents hlc
    exact le_trans (Nat.le_of_lt hlc) (Nat.le_of_lt hparents.2)

/-- Contrapositive bridge core: if the center mediant is outside a closed source gap,
then the two parents cannot both lie in that source gap. -/
theorem farey_parent_escapes_of_center_outside {m N l ln u un : ℕ}
    (P : FareyParentData m N)
    (hcenterOut : ¬ fracInClosedGap l ln u un m N) :
    ¬ (fracInClosedGap l ln u un P.a P.b ∧
        fracInClosedGap l ln u un P.c P.d) := by
  rintro ⟨hleft, hright⟩
  have hmed := mediant_mem_closedGap hleft hright
  rw [P.numer_sum, P.denom_sum] at hmed
  exact hcenterOut hmed

end EnterpriseMath.Scale
