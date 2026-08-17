import EnterpriseMath.Scale.OverlapReachability
import Mathlib.SetTheory.Cardinal.NatCard
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Every overlap-graph vertex has a gcd-block label strictly below the gcd. -/
theorem overlapVertexBlock_lt_gcd {d e : ℕ} (hd : 0 < d) (he : 0 < e)
    (v : Fin d ⊕ Fin e) :
    overlapVertexBlock d e v < d.gcd e := by
  let g := d.gcd e
  have hg : 0 < g := by
    dsimp [g]
    exact Nat.gcd_pos_of_pos_left e hd
  cases v with
  | inl i =>
      let w := d / g
      have hw : 0 < w := by
        dsimp [w, g]
        exact Nat.div_gcd_pos_of_pos_left e hd
      have hd_decomp : d = w * g := by
        dsimp [w, g]
        exact (Nat.div_mul_cancel (Nat.gcd_dvd_left d e)).symm
      unfold overlapVertexBlock gcdBlockD
      apply (Nat.div_lt_iff_lt_mul hw).2
      have hi : i.1 < w * g := by simpa [hd_decomp] using i.2
      simpa [Nat.mul_comm] using hi
  | inr j =>
      let w := e / g
      have hw : 0 < w := by
        have hgsymm : e.gcd d = g := by
          dsimp [g]
          rw [Nat.gcd_comm]
        dsimp [w]
        rw [← hgsymm]
        exact Nat.div_gcd_pos_of_pos_left d he
      have he_decomp : e = w * g := by
        dsimp [w, g]
        exact (Nat.div_mul_cancel (Nat.gcd_dvd_right d e)).symm
      unfold overlapVertexBlock gcdBlockE
      apply (Nat.div_lt_iff_lt_mul hw).2
      have hj : j.1 < w * g := by simpa [he_decomp] using j.2
      simpa [Nat.mul_comm] using hj

/-- Gcd-block label as an actual element of `Fin (gcd d e)`. -/
def overlapVertexBlockFin {d e : ℕ} (hd : 0 < d) (he : 0 < e)
    (v : Fin d ⊕ Fin e) : Fin (d.gcd e) :=
  ⟨overlapVertexBlock d e v, overlapVertexBlock_lt_gcd hd he v⟩

/-- The block label descends from vertices to connected components. -/
noncomputable def overlapComponentBlock {d e : ℕ} (hd : 0 < d) (he : 0 < e) :
    (overlapGraph d e).ConnectedComponent → Fin (d.gcd e) :=
  SimpleGraph.ConnectedComponent.lift (overlapVertexBlockFin hd he) (by
    intro v w p _hp
    apply Fin.ext
    exact overlapGraph_reachable_same_block hd he p.reachable)

/-- Canonical left root vertex of gcd block `k`. -/
def overlapBlockRootVertex {d e : ℕ} (hd : 0 < d) (k : Fin (d.gcd e)) :
    Fin d ⊕ Fin e := by
  let g := d.gcd e
  let w := d / g
  have hw : 0 < w := by
    dsimp [w, g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  have hd_decomp : d = w * g := by
    dsimp [w, g]
    exact (Nat.div_mul_cancel (Nat.gcd_dvd_left d e)).symm
  have hlt : k.1 * w < d := by
    rw [hd_decomp]
    have h := (Nat.mul_lt_mul_right hw).2 k.2
    simpa [Nat.mul_comm] using h
  exact Sum.inl ⟨k.1 * w, hlt⟩

/-- Canonical connected component represented by gcd block `k`. -/
def overlapBlockComponent {d e : ℕ} (hd : 0 < d) (k : Fin (d.gcd e)) :
    (overlapGraph d e).ConnectedComponent :=
  (overlapGraph d e).connectedComponentMk (overlapBlockRootVertex hd k)

@[simp]
theorem overlapVertexBlockFin_blockRoot {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) (k : Fin (d.gcd e)) :
    overlapVertexBlockFin hd he (overlapBlockRootVertex hd k) = k := by
  apply Fin.ext
  let g := d.gcd e
  let w := d / g
  have hw : 0 < w := by
    dsimp [w, g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  simp [overlapVertexBlockFin, overlapBlockRootVertex, overlapVertexBlock,
    gcdBlockD, w, g, Nat.mul_div_left k.1 hw]

@[simp]
theorem overlapComponentBlock_blockComponent {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) (k : Fin (d.gcd e)) :
    overlapComponentBlock hd he (overlapBlockComponent hd k) = k := by
  simp [overlapComponentBlock, overlapBlockComponent]

/-- Mapping a component to its block and back returns the same component. -/
theorem overlapBlockComponent_componentBlock {d e : ℕ}
    (hd : 0 < d) (he : 0 < e)
    (c : (overlapGraph d e).ConnectedComponent) :
    overlapBlockComponent hd (overlapComponentBlock hd he c) = c := by
  refine SimpleGraph.ConnectedComponent.ind ?_ c
  intro v
  obtain ⟨hs, hreach⟩ := overlapGraph_vertex_reachable_from_blockStart hd he v
  apply SimpleGraph.ConnectedComponent.sound
  have hroot : overlapBlockRootVertex hd
      (overlapComponentBlock hd he ((overlapGraph d e).connectedComponentMk v)) =
      (Sum.inl (⟨overlapVertexBlockStart d e v, hs⟩ : Fin d) : Fin d ⊕ Fin e) := by
    apply congrArg Sum.inl
    apply Fin.ext
    simp [overlapComponentBlock, overlapBlockRootVertex, overlapVertexBlockFin,
      overlapVertexBlockStart]
  simpa [overlapBlockComponent, hroot] using hreach

/-- Connected components of the two-scale overlap graph are canonically indexed by
`Fin (gcd d e)`. -/
noncomputable def overlapConnectedComponentEquivFinGcd {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) :
    (overlapGraph d e).ConnectedComponent ≃ Fin (d.gcd e) where
  toFun := overlapComponentBlock hd he
  invFun := overlapBlockComponent hd
  left_inv := overlapBlockComponent_componentBlock hd he
  right_inv := overlapComponentBlock_blockComponent hd he

/-- R007 overlap-component theorem: the exact number of connected components is the
greatest common divisor of the two scales. -/
theorem overlapGraph_connectedComponent_natCard {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) :
    Nat.card (overlapGraph d e).ConnectedComponent = d.gcd e := by
  exact Nat.card_eq_of_equiv_fin (overlapConnectedComponentEquivFinGcd hd he)

end EnterpriseMath.Scale
