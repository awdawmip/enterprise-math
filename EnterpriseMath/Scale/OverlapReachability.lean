import EnterpriseMath.Scale.OverlapBlockConnectivity
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Canonical left-side root index of the gcd block containing a graph vertex. -/
def overlapVertexBlockStart (d e : ℕ) (v : Fin d ⊕ Fin e) : ℕ :=
  overlapVertexBlock d e v * (d / d.gcd e)

/-- Every overlap-graph vertex is reachable from the canonical left root of its gcd
block. -/
theorem overlapGraph_vertex_reachable_from_blockStart {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) (v : Fin d ⊕ Fin e) :
    ∃ hs : overlapVertexBlockStart d e v < d,
      (overlapGraph d e).Reachable
        (Sum.inl (⟨overlapVertexBlockStart d e v, hs⟩ : Fin d)) v := by
  cases v with
  | inl i =>
      obtain ⟨hs, hreach⟩ := overlapGraph_left_reachable_from_blockStart hd he i
      refine ⟨?_, ?_⟩
      · simpa [overlapVertexBlockStart, leftBlockStart, overlapVertexBlock] using hs
      · simpa [overlapVertexBlockStart, leftBlockStart, overlapVertexBlock] using hreach
  | inr j =>
      obtain ⟨i, hblock, hir⟩ := overlapGraph_right_reachable_from_blockStart hd he j
      obtain ⟨hs, hrooti⟩ := overlapGraph_left_reachable_from_blockStart hd he i
      have hstart : leftBlockStart d e i.1 = overlapVertexBlockStart d e (Sum.inr j) := by
        unfold leftBlockStart overlapVertexBlockStart
        rw [← hblock]
        rfl
      have hs' : overlapVertexBlockStart d e (Sum.inr j) < d := by
        simpa [hstart] using hs
      refine ⟨hs', ?_⟩
      have hrooti' : (overlapGraph d e).Reachable
          (Sum.inl (⟨overlapVertexBlockStart d e (Sum.inr j), hs'⟩ : Fin d))
          (Sum.inl i) := by
        convert hrooti using 1 <;> apply congrArg Sum.inl <;> apply Fin.ext <;>
          simpa [hstart]
      exact hrooti'.trans hir

/-- Equality of gcd-block labels is sufficient for reachability. -/
theorem overlapGraph_reachable_of_same_block {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) {u v : Fin d ⊕ Fin e}
    (hblock : overlapVertexBlock d e u = overlapVertexBlock d e v) :
    (overlapGraph d e).Reachable u v := by
  obtain ⟨hsu, hu⟩ := overlapGraph_vertex_reachable_from_blockStart hd he u
  obtain ⟨hsv, hv⟩ := overlapGraph_vertex_reachable_from_blockStart hd he v
  have hstart : overlapVertexBlockStart d e u = overlapVertexBlockStart d e v := by
    unfold overlapVertexBlockStart
    rw [hblock]
  have hroot :
      (Sum.inl (⟨overlapVertexBlockStart d e u, hsu⟩ : Fin d) : Fin d ⊕ Fin e) =
      Sum.inl (⟨overlapVertexBlockStart d e v, hsv⟩ : Fin d) := by
    apply congrArg Sum.inl
    apply Fin.ext
    exact hstart
  have hv' : (overlapGraph d e).Reachable
      (Sum.inl (⟨overlapVertexBlockStart d e u, hsu⟩ : Fin d)) v := by
    simpa [hroot] using hv
  exact hu.symm.trans hv'

/-- Exact reachability classification: two vertices are in the same connected component
iff they have the same gcd-block label. -/
theorem overlapGraph_reachable_iff_same_block {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) {u v : Fin d ⊕ Fin e} :
    (overlapGraph d e).Reachable u v ↔
      overlapVertexBlock d e u = overlapVertexBlock d e v := by
  constructor
  · exact overlapGraph_reachable_same_block hd he
  · exact overlapGraph_reachable_of_same_block hd he

end EnterpriseMath.Scale
