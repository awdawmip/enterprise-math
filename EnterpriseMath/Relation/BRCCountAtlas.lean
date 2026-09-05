import EnterpriseMath.Relation.BRCFrameSymmetry
import Mathlib.Data.Finset.Lattice.Fold
import Mathlib.Tactic

namespace EnterpriseMath.BranchRecoalescence

/-- A finite count atlas indexed by a declared axis type.  The six-axis model is
the specialization `ι = Fin 6`; the generic form keeps the formal layer reusable
for other finite atlases. -/
abbrev CountAtlas (ι : Type*) := ι → ℕ

/-- A coordinate action is a pure reindexing action when every frame acts on the
atlas by a permutation of coordinate axes.  No metric or native-geometric claim
is built into this predicate. -/
def CoordinateReindexing {G ι : Type*} [Monoid G]
    (ρ : CoordinateAction G (CountAtlas ι)) : Prop :=
  ∀ g, ∃ e : Equiv.Perm ι, ∀ n i, ρ.act g n i = n (e i)

/-- Common atlas depth: the largest scalar depth removable from every coordinate
simultaneously. -/
def commonDepth {ι : Type*} [Fintype ι] [Nonempty ι] (n : CountAtlas ι) : ℕ :=
  Finset.univ.inf' Finset.univ_nonempty n

/-- Common depth is below every coordinate. -/
theorem commonDepth_le {ι : Type*} [Fintype ι] [Nonempty ι]
    (n : CountAtlas ι) (i : ι) :
    commonDepth n ≤ n i := by
  exact Finset.inf'_le _ (Finset.mem_univ i)

/-- Pure axis relabeling preserves common depth exactly. -/
theorem commonDepth_act {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (hρ : CoordinateReindexing ρ) (g : G) (n : CountAtlas ι) :
    commonDepth (ρ.act g n) = commonDepth n := by
  rcases hρ g with ⟨e, he⟩
  apply le_antisymm
  · refine Finset.le_inf' _ _ ?_
    intro i _hi
    have hle := commonDepth_le (ρ.act g n) (e.symm i)
    rw [he n (e.symm i)] at hle
    simpa using hle
  · refine Finset.le_inf' _ _ ?_
    intro i _hi
    rw [he n i]
    exact commonDepth_le n (e i)

/-- The common depth of a serially added atlas is at least the sum of the two
individual common depths, even when the second atlas is first frame-reindexed. -/
theorem commonDepth_add_act {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (hρ : CoordinateReindexing ρ)
    (n m : CountAtlas ι) (g : G) :
    commonDepth n + commonDepth m ≤ commonDepth (n + ρ.act g m) := by
  rcases hρ g with ⟨e, he⟩
  refine Finset.le_inf' _ _ ?_
  intro i _hi
  change commonDepth n + commonDepth m ≤ n i + ρ.act g m i
  rw [he m i]
  exact Nat.add_le_add (commonDepth_le n i) (commonDepth_le m (e i))

/-- Integer-valued common depth is invariant under a reindexing frame action. -/
theorem commonDepth_coordinateInvariant {G ι : Type*}
    [Group G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (hρ : CoordinateReindexing ρ) :
    CoordinateInvariant ρ (fun n => (commonDepth n : Int)) := by
  intro g n
  change (commonDepth (ρ.act g n) : Int) = (commonDepth n : Int)
  exact_mod_cast commonDepth_act ρ hρ g n

/-- Integer-valued common depth is superadditive for framed serial composition. -/
theorem commonDepth_coordinateSuperadditive {G ι : Type*}
    [Monoid G] [Fintype ι] [Nonempty ι]
    (ρ : CoordinateAction G (CountAtlas ι))
    (hρ : CoordinateReindexing ρ) :
    CoordinateSuperadditive ρ (fun n => (commonDepth n : Int)) := by
  intro n m g
  change (commonDepth n : Int) + (commonDepth m : Int) ≤
    (commonDepth (n + ρ.act g m) : Int)
  exact_mod_cast commonDepth_add_act ρ hρ n m g

/-- The BRC carry induced by removing common atlas depth after serial framed
composition.  This is deliberately distinct from any other compression
potential, such as a K4 optimal-extraction potential; the shared structure is the
two-coboundary law, not equality of the potentials. -/
def commonDepthCarry {W G ι : Type*}
    [Monoid W] [Monoid G] [Fintype ι] [Nonempty ι]
    {ρ : CoordinateAction G (CountAtlas ι)}
    (a b : FramedPath W G (CountAtlas ι) ρ) : Int :=
  coordinateCarry (fun n => (commonDepth n : Int)) a b

@[simp] theorem commonDepthCarry_eq {W G ι : Type*}
    [Monoid W] [Monoid G] [Fintype ι] [Nonempty ι]
    {ρ : CoordinateAction G (CountAtlas ι)}
    (a b : FramedPath W G (CountAtlas ι) ρ) :
    commonDepthCarry a b =
      (commonDepth (a.coord + ρ.act a.frame b.coord) : Int) -
        commonDepth a.coord - commonDepth b.coord := by
  rfl

/-- A normalized atlas has no removable common depth. -/
def CountAtlasNormalized {ι : Type*} [Fintype ι] [Nonempty ι]
    (n : CountAtlas ι) : Prop :=
  commonDepth n = 0

/-- For normalized inputs, the carry is exactly the common depth that appears
after framed composition.  This is the direct formal version of the six-axis
formula `c = min(r + g·s)`. -/
theorem commonDepthCarry_of_normalized {W G ι : Type*}
    [Monoid W] [Monoid G] [Fintype ι] [Nonempty ι]
    {ρ : CoordinateAction G (CountAtlas ι)}
    (a b : FramedPath W G (CountAtlas ι) ρ)
    (ha : CountAtlasNormalized a.coord)
    (hb : CountAtlasNormalized b.coord) :
    commonDepthCarry a b =
      (commonDepth (a.coord + ρ.act a.frame b.coord) : Int) := by
  rw [commonDepthCarry_eq, ha, hb]
  simp

/-- Reindexing actions make the common-depth carry nonnegative. -/
theorem commonDepthCarry_nonneg {W G ι : Type*}
    [Monoid W] [Monoid G] [Fintype ι] [Nonempty ι]
    {ρ : CoordinateAction G (CountAtlas ι)}
    (hρ : CoordinateReindexing ρ)
    (a b : FramedPath W G (CountAtlas ι) ρ) :
    0 ≤ commonDepthCarry a b := by
  exact coordinateCarry_nonneg _ (commonDepth_coordinateSuperadditive ρ hρ) a b

/-- Common-depth carry obeys exact parenthesization independence because it is a
two-coboundary. -/
theorem commonDepthCarry_cocycle {W G ι : Type*}
    [Monoid W] [Monoid G] [Fintype ι] [Nonempty ι]
    {ρ : CoordinateAction G (CountAtlas ι)}
    (a b c : FramedPath W G (CountAtlas ι) ρ) :
    commonDepthCarry a b + commonDepthCarry (a * b) c =
      commonDepthCarry b c + commonDepthCarry a (b * c) := by
  exact coordinateCarry_cocycle (fun n => (commonDepth n : Int)) a b c

/-- Under a reindexing group action, global frame relabeling leaves the
common-depth carry unchanged. -/
theorem commonDepthCarry_relabel {W G ι : Type*}
    [Monoid W] [Group G] [Fintype ι] [Nonempty ι]
    {ρ : CoordinateAction G (CountAtlas ι)}
    (hρ : CoordinateReindexing ρ)
    (s : G) (a b : FramedPath W G (CountAtlas ι) ρ) :
    commonDepthCarry (FramedPath.relabel ρ s a) (FramedPath.relabel ρ s b) =
      commonDepthCarry a b := by
  exact coordinateCarry_relabel _ (commonDepth_coordinateInvariant ρ hρ) s a b

end EnterpriseMath.BranchRecoalescence
