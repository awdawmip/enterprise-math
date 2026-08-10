import EnterpriseMath.Scale.OverlapGraph
import EnterpriseMath.Scale.PrimeSplit
import Mathlib.Tactic

namespace EnterpriseMath.Scale

/-- Gcd-block label on overlap-graph vertices. -/
def overlapVertexBlock (d e : ℕ) : Fin d ⊕ Fin e → ℕ
  | Sum.inl i => gcdBlockD d e i.1
  | Sum.inr j => gcdBlockE d e j.1

/-- Every overlap-graph edge preserves the gcd-block label. -/
theorem overlapGraph_adj_same_block {d e : ℕ} (hd : 0 < d) (he : 0 < e)
    {u v : Fin d ⊕ Fin e} (hAdj : (overlapGraph d e).Adj u v) :
    overlapVertexBlock d e u = overlapVertexBlock d e v := by
  cases u with
  | inl i =>
      cases v with
      | inl i' =>
          exfalso
          simpa [overlapGraph, overlapRel] using hAdj
      | inr j =>
          exact cellOverlap_same_gcdBlock hd he
            ((overlapGraph_adj_left_right i j).1 hAdj)
  | inr j =>
      cases v with
      | inl i =>
          exact (cellOverlap_same_gcdBlock hd he
            ((overlapGraph_adj_right_left i j).1 hAdj)).symm
      | inr j' =>
          exfalso
          simpa [overlapGraph, overlapRel] using hAdj

/-- The gcd-block label is constant along every overlap-graph walk/reachable pair. -/
theorem overlapGraph_reachable_same_block {d e : ℕ} (hd : 0 < d) (he : 0 < e)
    {u v : Fin d ⊕ Fin e} (hReach : (overlapGraph d e).Reachable u v) :
    overlapVertexBlock d e u = overlapVertexBlock d e v := by
  have hrtg : Relation.ReflTransGen (overlapGraph d e).Adj u v :=
    (SimpleGraph.reachable_iff_reflTransGen).1 hReach
  induction hrtg with
  | refl => rfl
  | tail hxy hyz ih =>
      exact ih.trans (overlapGraph_adj_same_block hd he hyz)

/-- If the gcd is nontrivial, vertices in the first two gcd blocks cannot be connected. -/
theorem overlapGraph_not_connected_of_one_lt_gcd {d e : ℕ}
    (hd : 0 < d) (he : 0 < e) (hg : 1 < d.gcd e) :
    ¬ (overlapGraph d e).Connected := by
  let g := d.gcd e
  let d' := d / g
  have hd' : 0 < d' := by
    dsimp [d', g]
    exact Nat.div_gcd_pos_of_pos_left e hd
  have hd_decomp : d = d' * g := by
    dsimp [d', g]
    exact (Nat.div_mul_cancel (Nat.gcd_dvd_left d e)).symm
  have hd'_lt : d' < d := by
    rw [hd_decomp]
    have hmul : d' * 1 < d' * g :=
      (Nat.mul_lt_mul_left hd').2 (by simpa [g] using hg)
    simpa using hmul
  let u₀ : Fin d ⊕ Fin e := Sum.inl ⟨0, hd⟩
  let u₁ : Fin d ⊕ Fin e := Sum.inl ⟨d', hd'_lt⟩
  have hb₀ : overlapVertexBlock d e u₀ = 0 := by
    simp [u₀, overlapVertexBlock, gcdBlockD]
  have hb₁ : overlapVertexBlock d e u₁ = 1 := by
    simp [u₁, overlapVertexBlock, gcdBlockD, d', g, Nat.div_self hd']
  intro hconn
  have hreach : (overlapGraph d e).Reachable u₀ u₁ := hconn u₀ u₁
  have hblock := overlapGraph_reachable_same_block hd he hreach
  rw [hb₀, hb₁] at hblock
  omega

/-- Positive two-scale overlap graphs are connected exactly in the coprime case. -/
theorem overlapGraph_connected_iff_gcd_eq_one {d e : ℕ} (hd : 0 < d) (he : 0 < e) :
    (overlapGraph d e).Connected ↔ d.gcd e = 1 := by
  constructor
  · intro hconn
    by_contra hne
    have hgpos : 0 < d.gcd e := Nat.gcd_pos_of_pos_left e hd
    have hg : 1 < d.gcd e := by omega
    exact (overlapGraph_not_connected_of_one_lt_gcd hd he hg) hconn
  · intro hg
    have hcop : d.Coprime e := (Nat.coprime_iff_gcd_eq_one).2 hg
    exact coprime_overlapGraph_connected hcop hd he

/-- Topological form of the arithmetic split predicate: for positive scales, graph
disconnection is exactly `gcd > 1`. -/
theorem overlapGraph_not_connected_iff_arithmeticSplit {n d : ℕ}
    (hn : 0 < n) (hd : 0 < d) :
    ¬ (overlapGraph n d).Connected ↔ arithmeticSplit n d := by
  rw [overlapGraph_connected_iff_gcd_eq_one hn hd]
  unfold arithmeticSplit
  have hgpos : 0 < n.gcd d := Nat.gcd_pos_of_pos_left d hn
  omega

/-- At a prime scale, overlap disconnection is exactly divisibility by that prime. -/
theorem overlapGraph_prime_not_connected_iff_dvd {n p : ℕ}
    (hn : 0 < n) (hp : p.Prime) :
    ¬ (overlapGraph n p).Connected ↔ p ∣ n := by
  rw [overlapGraph_not_connected_iff_arithmeticSplit hn hp.pos]
  exact arithmeticSplit_prime_iff hp

/-- The smallest prime factor is itself a disconnecting overlap scale. -/
theorem overlapGraph_minFac_not_connected {n : ℕ} (hn : 2 ≤ n) :
    ¬ (overlapGraph n n.minFac).Connected := by
  apply (overlapGraph_not_connected_iff_arithmeticSplit (by omega)
    (Nat.minFac_prime (by omega : n ≠ 1)).pos).2
  exact arithmeticSplit_minFac (by omega)

/-- R007/R005 bridge: `minFac n` is the first positive scale whose overlap graph with
scale `n` disconnects. -/
theorem minFac_is_first_overlap_disconnect {n : ℕ} (hn : 2 ≤ n) :
    ¬ (overlapGraph n n.minFac).Connected ∧
      ∀ d, 0 < d → ¬ (overlapGraph n d).Connected → n.minFac ≤ d := by
  refine ⟨overlapGraph_minFac_not_connected hn, ?_⟩
  intro d hd hdisc
  apply minFac_le_of_arithmeticSplit hd
  exact (overlapGraph_not_connected_iff_arithmeticSplit (by omega) hd).1 hdisc

/-- Primality characterization: `n>=2` is prime exactly when every smaller positive
nontrivial scale remains connected to scale `n`. -/
theorem prime_iff_all_lower_overlap_connected {n : ℕ} (hn : 2 ≤ n) :
    n.Prime ↔ ∀ d, 2 ≤ d → d < n → (overlapGraph n d).Connected := by
  constructor
  · intro hp d hd2 hdn
    apply (overlapGraph_connected_iff_gcd_eq_one (by omega) (by omega)).2
    have hnotdvd : ¬ n ∣ d := by
      intro hdiv
      have hle : n ≤ d := Nat.le_of_dvd (by omega) hdiv
      omega
    have hcop : n.Coprime d := hp.coprime_iff_not_dvd.mpr hnotdvd
    exact hcop.gcd_eq_one
  · intro hall
    have hmin : n.minFac.Prime := Nat.minFac_prime (by omega : n ≠ 1)
    have hle : n.minFac ≤ n := Nat.minFac_le (by omega)
    have hmin2 : 2 ≤ n.minFac := hmin.two_le
    by_cases heq : n.minFac = n
    · exact (Nat.prime_def_minFac).2 ⟨hn, heq⟩
    · have hlt : n.minFac < n := lt_of_le_of_ne hle heq
      have hconn := hall n.minFac hmin2 hlt
      exact False.elim ((overlapGraph_minFac_not_connected hn) hconn)

end EnterpriseMath.Scale
