import EnterpriseMath.Scale.FareyGap
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- A closed rational gap contains a grid point of denominator/scale `h`. -/
def gapHasGridPoint (l ln u un h : ℕ) : Prop :=
  ∃ k, fracInClosedGap l ln u un k h

/-- Grid points at scales `b` and `d` in the same closed gap produce a grid point at
scale `b+d` by the mediant construction. -/
theorem gapHasGridPoint_add {l ln u un b d : ℕ}
    (hb : gapHasGridPoint l ln u un b)
    (hd : gapHasGridPoint l ln u un d) :
    gapHasGridPoint l ln u un (b + d) := by
  rcases hb with ⟨p, hp⟩
  rcases hd with ⟨q, hq⟩
  exact ⟨p + q, mediant_mem_closedGap hp hq⟩

/-- If a source gap contains no `(b+d)`-grid point, it cannot simultaneously contain
both a `b`-grid point and a `d`-grid point. -/
theorem gapNoGridPoint_add_split {l ln u un b d : ℕ}
    (hno : ¬ gapHasGridPoint l ln u un (b + d)) :
    ¬ gapHasGridPoint l ln u un b ∨
      ¬ gapHasGridPoint l ln u un d := by
  by_contra h
  push_neg at h
  exact hno (gapHasGridPoint_add h.1 h.2)

/-- Primitive Farey bridge descent.

Suppose `m/N` is a reduced proper `N`-grid point lying strictly inside a target gap,
whose endpoint denominators are already `< N`. If a source gap contains no `N`-grid
point, then some strictly smaller scale `h<N` already separates the two gaps:
the target contains an `h`-grid point while the source contains none.

This is the number-theoretic core of R007's one-step natural-extension theorem. -/
theorem primitive_grid_bridge_descend
    {m N sl sln su sun tl tln tu tun : ℕ}
    (hm : 0 < m) (hmN : m < N) (hcop : m.Coprime N)
    (htln : tln < N) (htun : tun < N)
    (htargetLeft : fracLt tl tln m N)
    (htargetRight : fracLt m N tu tun)
    (hsourceNoN : ¬ gapHasGridPoint sl sln su sun N) :
    ∃ h,
      0 < h ∧ h < N ∧
        gapHasGridPoint tl tln tu tun h ∧
        ¬ gapHasGridPoint sl sln su sun h := by
  let P : FareyParentData m N := Classical.choice (exists_fareyParentData hm hmN hcop)
  have htargetParents := fareyParents_mem_closedGap_of_center_mem
    P htln htun htargetLeft htargetRight
  have htargetB : gapHasGridPoint tl tln tu tun P.b :=
    ⟨P.a, htargetParents.1⟩
  have htargetD : gapHasGridPoint tl tln tu tun P.d :=
    ⟨P.c, htargetParents.2⟩
  have hsourceSplit :
      ¬ gapHasGridPoint sl sln su sun P.b ∨
        ¬ gapHasGridPoint sl sln su sun P.d := by
    apply gapNoGridPoint_add_split
    simpa [P.denom_sum] using hsourceNoN
  rcases hsourceSplit with hnoB | hnoD
  · exact ⟨P.b, P.b_pos, P.b_lt, htargetB, hnoB⟩
  · exact ⟨P.d, P.d_pos, P.d_lt, htargetD, hnoD⟩

end EnterpriseMath.Scale
