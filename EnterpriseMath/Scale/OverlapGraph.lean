import EnterpriseMath.Scale.OverlapConnectivity
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Oriented generating relation for the bipartite overlap graph. `fromRel` below
symmetrizes it and removes loops. -/
def overlapRel (d e : ℕ) : (Fin d ⊕ Fin e) → (Fin d ⊕ Fin e) → Prop
  | Sum.inl i, Sum.inr j => cellOverlap d i.1 e j.1
  | _, _ => False

/-- Bipartite graph whose vertices are the scale-`d` and scale-`e` cells, with an edge
exactly when the corresponding half-open cells overlap in positive length. -/
def overlapGraph (d e : ℕ) : SimpleGraph (Fin d ⊕ Fin e) :=
  SimpleGraph.fromRel (overlapRel d e)

@[simp]
theorem overlapGraph_adj_left_right {d e : ℕ} (i : Fin d) (j : Fin e) :
    (overlapGraph d e).Adj (Sum.inl i) (Sum.inr j) ↔ cellOverlap d i.1 e j.1 := by
  simp [overlapGraph, overlapRel]

@[simp]
theorem overlapGraph_adj_right_left {d e : ℕ} (i : Fin d) (j : Fin e) :
    (overlapGraph d e).Adj (Sum.inr j) (Sum.inl i) ↔ cellOverlap d i.1 e j.1 := by
  rw [SimpleGraph.adj_comm]
  exact overlapGraph_adj_left_right i j

/-- Consecutive left-side cells are reachable through the explicit bridge cell from
`boundaryBridgeCell_certificate`. -/
theorem overlapGraph_left_succ_reachable {d e i : ℕ}
    (hcop : d.Coprime e) (hd : 0 < d) (he : 0 < e) (hi : i + 1 < d) :
    (overlapGraph d e).Reachable
      (Sum.inl (⟨i, by omega⟩ : Fin d))
      (Sum.inl (⟨i + 1, hi⟩ : Fin d)) := by
  obtain ⟨hj, hov₁, hov₂⟩ := boundaryBridgeCell_certificate hcop hd he hi
  let j : Fin e := ⟨boundaryBridgeCell d e i, hj⟩
  have hAdj₁ : (overlapGraph d e).Adj
      (Sum.inl (⟨i, by omega⟩ : Fin d)) (Sum.inr j) := by
    exact (overlapGraph_adj_left_right _ _).2 hov₁
  have hAdj₂ : (overlapGraph d e).Adj
      (Sum.inl (⟨i + 1, hi⟩ : Fin d)) (Sum.inr j) := by
    exact (overlapGraph_adj_left_right _ _).2 hov₂
  exact hAdj₁.reachable.trans hAdj₂.symm.reachable

/-- In the coprime graph, the leftmost left vertex reaches every left vertex by the
bridge chain. -/
theorem coprime_overlapGraph_left_reachable {d e : ℕ}
    (hcop : d.Coprime e) (hd : 0 < d) (he : 0 < e) (i : Fin d) :
    (overlapGraph d e).Reachable
      (Sum.inl (⟨0, hd⟩ : Fin d)) (Sum.inl i) := by
  have aux : ∀ n : ℕ, ∀ hn : n < d,
      (overlapGraph d e).Reachable
        (Sum.inl (⟨0, hd⟩ : Fin d))
        (Sum.inl (⟨n, hn⟩ : Fin d)) := by
    intro n
    induction n with
    | zero =>
        intro hn
        exact SimpleGraph.Reachable.refl
    | succ n ih =>
        intro hn
        have hprev : n < d := by omega
        have hstep : n + 1 < d := by simpa using hn
        have hreachPrev := ih hprev
        have hreachStep := overlapGraph_left_succ_reachable hcop hd he hstep
        exact hreachPrev.trans hreachStep
  simpa using aux i.1 i.2

/-- In the coprime graph, the leftmost left vertex reaches every right vertex by first
reaching an attached left cell. -/
theorem coprime_overlapGraph_right_reachable {d e : ℕ}
    (hcop : d.Coprime e) (hd : 0 < d) (he : 0 < e) (j : Fin e) :
    (overlapGraph d e).Reachable
      (Sum.inl (⟨0, hd⟩ : Fin d)) (Sum.inr j) := by
  obtain ⟨hi, hov⟩ := attachmentCell_certificate hd he j.2
  let i : Fin d := ⟨attachmentCell d e j.1, hi⟩
  have hleft := coprime_overlapGraph_left_reachable hcop hd he i
  have hAdj : (overlapGraph d e).Adj (Sum.inl i) (Sum.inr j) := by
    exact (overlapGraph_adj_left_right _ _).2 hov
  exact hleft.trans hAdj.reachable

/-- Every overlap graph of coprime positive scales is connected. -/
theorem coprime_overlapGraph_connected {d e : ℕ}
    (hcop : d.Coprime e) (hd : 0 < d) (he : 0 < e) :
    (overlapGraph d e).Connected := by
  rw [SimpleGraph.connected_iff_exists_forall_reachable]
  refine ⟨Sum.inl (⟨0, hd⟩ : Fin d), ?_⟩
  intro v
  cases v with
  | inl i => exact coprime_overlapGraph_left_reachable hcop hd he i
  | inr j => exact coprime_overlapGraph_right_reachable hcop hd he j

end EnterpriseMath.Scale
