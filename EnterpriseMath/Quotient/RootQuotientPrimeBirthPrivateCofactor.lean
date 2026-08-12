import EnterpriseMath.Quotient.RootQuotientMinimumMacroPrivateTarget
import EnterpriseMath.Quotient.RootQuotientMultiSpareReachability
import Mathlib.Tactic

namespace EnterpriseMath.Quotient

/-- A literal word over a singleton alphabet has the expected pure-power
product. -/
theorem rootQuotientWordProduct_eq_pow_of_wordOver_singleton
    {g : ℕ} {w : List ℕ}
    (hw : RootQuotientWordOver ({g} : Set ℕ) w) :
    rootQuotientWordProduct w = g ^ w.length := by
  induction w with
  | nil => simp [rootQuotientWordProduct]
  | cons a w ih =>
      have ha : a = g := by
        have := hw a (by simp)
        simpa using this
      subst a
      have hwTail : RootQuotientWordOver ({g} : Set ℕ) w := by
        intro x hx
        exact hw x (by simp [hx])
      rw [rootQuotientWordProduct, ih hwTail]
      simp [pow_succ']

/-- Re-adjoining a deleted stored type recovers the original prime-plus-macro
presentation. -/
theorem prime_union_sdiff_union_singleton_eq
    {N g : ℕ} {S : Set ℕ}
    (hgS : g ∈ S) :
    (RootQuotientPrimeBasis N ∪ (S \ {g})) ∪ ({g} : Set ℕ) =
      RootQuotientPrimeBasis N ∪ S := by
  ext a
  constructor
  · intro ha
    rcases ha with haBase | haG
    · rcases haBase with haPrime | haRest
      · exact Or.inl haPrime
      · exact Or.inr haRest.1
    · have haEq : a = g := by simpa using haG
      subst a
      exact Or.inr hgS
  · intro ha
    rcases ha with haPrime | haS
    · exact Or.inl (Or.inl haPrime)
    · by_cases hag : a = g
      · subst a
        exact Or.inr (by simp)
      · exact Or.inl (Or.inr ⟨haS, by simpa [hag]⟩)

/-- **Private-target cofactor decomposition.**

If `g` is genuinely necessary for a target at horizon `h`, then every successful
presentation using `g` can be regrouped into a positive number `j` of copies of
`g` times a residual cofactor reachable from the dictionary with `g` deleted in
only `h-j` steps.

This is the recursive action-level certificate behind exact macro
preinvestment. -/
theorem private_target_decomposes_into_macro_power_and_residual
    {N h g t : ℕ} {S : Set ℕ}
    (hgS : g ∈ S)
    (hReach : RootQuotientProductReachableWithin h
      (RootQuotientPrimeBasis N ∪ S) t)
    (hNoReach : ¬RootQuotientProductReachableWithin h
      (RootQuotientPrimeBasis N ∪ (S \ {g})) t) :
    ∃ j b : ℕ,
      1 ≤ j ∧ j ≤ h ∧
      RootQuotientProductReachableWithin (h - j)
        (RootQuotientPrimeBasis N ∪ (S \ {g})) b ∧
      g ^ j * b = t := by
  let G : Set ℕ := RootQuotientPrimeBasis N ∪ (S \ {g})
  have hEq : G ∪ ({g} : Set ℕ) = RootQuotientPrimeBasis N ∪ S := by
    dsimp [G]
    exact prime_union_sdiff_union_singleton_eq hgS
  have hReach' : RootQuotientProductReachableWithin h (G ∪ ({g} : Set ℕ)) t := by
    rw [hEq]
    exact hReach
  obtain ⟨u, b, huLen, huG, hbReach, hFactor⟩ :=
    (rootQuotientProductReachableWithin_union_iff_exists_spareWord_residual
      (G := G) (S := ({g} : Set ℕ)) (t := t) (h := h)).1 hReach'
  have hProdU : rootQuotientWordProduct u = g ^ u.length :=
    rootQuotientWordProduct_eq_pow_of_wordOver_singleton huG
  have huPos : 1 ≤ u.length := by
    by_contra hNot
    have huZero : u.length = 0 := by omega
    have huNil : u = [] := List.length_eq_zero.mp huZero
    subst u
    simp [rootQuotientWordProduct] at hFactor
    subst b
    exact hNoReach (by simpa [G] using hbReach)
  refine ⟨u.length, b, huPos, huLen, ?_, ?_⟩
  · simpa [G] using hbReach
  · rw [← hProdU]
    exact hFactor

/-- Any nontrivial one-step reachable positive denominator is itself a literal
instruction of the alphabet. -/
theorem mem_generators_of_reachableWithin_one_of_two_le
    {G : Set ℕ} {b : ℕ}
    (hb : 2 ≤ b)
    (hReach : RootQuotientProductReachableWithin 1 G b) :
    b ∈ G := by
  obtain ⟨w, hwLen, hwG, hProd⟩ := hReach
  cases w with
  | nil =>
      simp [rootQuotientWordProduct] at hProd
      omega
  | cons a w =>
      have hwNil : w = [] := by
        cases w with
        | nil => rfl
        | cons x xs => simp at hwLen
      subst w
      have haG : a ∈ G := hwG a (by simp)
      simp [rootQuotientWordProduct] at hProd
      simpa [hProd] using haG

/-- **Recursive private-axis slice at a future prime birth.**

If an old exact optimum has preinvested in `p^e`, then that macro owns a private
old hard target

`t = p^(e*j) * b`

with `1≤j`, `e*j≤h`, and residual cofactor `b` reachable from the same optimum
with the future-axis macro deleted in only `h-j` steps. -/
theorem exactPrimeDirectionPreinvestment_has_private_cofactor_slice
    {r N h p : ℕ}
    (hr : 2 ≤ r)
    (hh : 1 ≤ h)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ (h + 1))
    (hPre : RootQuotientExactPrimeDirectionPreinvestment r N h p) :
    ∃ S : Set ℕ, ∃ e j t b : ℕ,
      RootQuotientCompositeMacroPresentation r N h S ∧
      S.ncard = rootQuotientMinimumCompositeMacroCount r N h ∧
      2 ≤ e ∧ e ≤ h ∧ p ^ e ∈ S ∧
      t ∈ RootQuotientPrimeHardSemanticTargetFinset r N h ∧
      1 ≤ j ∧ e * j ≤ h ∧
      RootQuotientProductReachableWithin (h - j)
        (RootQuotientPrimeBasis N ∪ (S \ {p ^ e})) b ∧
      p ^ (e * j) * b = t := by
  obtain ⟨S, hS, hSCard, e, heTwo, heLe, heMem⟩ := hPre
  obtain ⟨t, htHard, htReach, htNoReach, _htDvd⟩ :=
    exists_private_primeHard_target_of_mem_minimumCompositeMacroPresentation
      hr hh hS hSCard heMem
  obtain ⟨j, b, hjPos, hjLe, hbReach, hFactor⟩ :=
    private_target_decomposes_into_macro_power_and_residual
      (N := N) (h := h) (g := p ^ e) (t := t) (S := S)
      heMem htReach htNoReach
  have htMem := (mem_primeHardSemanticTargetFinset_iff).1 htHard
  have hPowDvd : p ^ (e * j) ∣ t := by
    refine ⟨b, ?_⟩
    calc
      p ^ (e * j) * b = (p ^ e) ^ j * b := by rw [pow_mul]
      _ = t := hFactor
  have hPowLeT : p ^ (e * j) ≤ t :=
    Nat.le_of_dvd (by omega) hPowDvd
  have hejLe : e * j ≤ h := by
    by_contra hNot
    have hPowerLe : p ^ (h + 1) ≤ p ^ (e * j) :=
      pow_le_pow_right' hp.one_le (by omega)
    have : N + 1 ≤ N := by
      rw [hBirth]
      exact hPowerLe.trans (hPowLeT.trans htMem.1.2.1)
    omega
  refine ⟨S, e, j, t, b, hS, hSCard, heTwo, heLe, heMem,
    htHard, hjPos, hejLe, hbReach, ?_⟩
  calc
    p ^ (e * j) * b = (p ^ e) ^ j * b := by rw [pow_mul]
    _ = t := hFactor

/-- **Horizon-two literal-cofactor specialization.**

At a cubic prime birth `N+1=p^3`, any exact preinvestment is necessarily the
square `p^2`, used exactly once on a private old hard target

`t = p^2 * b`,

where `2≤b<p` and `b` is itself a literal instruction of the dictionary after
`p^2` is deleted. -/
theorem exactPrimeDirectionPreinvestment_horizonTwo_has_literal_cofactor
    {r N p : ℕ}
    (hr : 2 ≤ r)
    (hp : p.Prime)
    (hBirth : N + 1 = p ^ 3)
    (hPre : RootQuotientExactPrimeDirectionPreinvestment r N 2 p) :
    ∃ S : Set ℕ, ∃ t b : ℕ,
      RootQuotientCompositeMacroPresentation r N 2 S ∧
      S.ncard = rootQuotientMinimumCompositeMacroCount r N 2 ∧
      p ^ 2 ∈ S ∧
      t ∈ RootQuotientPrimeHardSemanticTargetFinset r N 2 ∧
      2 ≤ b ∧ b < p ∧
      b ∈ RootQuotientPrimeBasis N ∪ (S \ {p ^ 2}) ∧
      p ^ 2 * b = t := by
  obtain ⟨S, e, j, t, b, hS, hSCard, heTwo, heLe, heMem,
      htHard, hjPos, hejLe, hbReach, hFactor⟩ :=
    exactPrimeDirectionPreinvestment_has_private_cofactor_slice
      (r := r) (N := N) (h := 2) (p := p)
      hr (by omega) hp (by simpa using hBirth) hPre
  have heEq : e = 2 := by omega
  subst e
  have hjEq : j = 1 := by omega
  subst j
  have htMem := (mem_primeHardSemanticTargetFinset_iff).1 htHard
  have hbPos : 1 ≤ b := by
    by_contra hbZero
    have hbEq : b = 0 := by omega
    rw [hbEq] at hFactor
    simp at hFactor
    omega
  have hbNotOne : b ≠ 1 := by
    intro hbOne
    subst b
    have hpCount : rootQuotientPrimeFactorCount p = 1 := by
      rw [rootQuotientPrimeFactorCount,
        Nat.primeFactorsList_prime hp]
      simp
    have hCount : rootQuotientPrimeFactorCount t = 2 := by
      rw [← hFactor]
      simp [rootQuotientPrimeFactorCount_pow hp.one_le, hpCount]
    omega
  have hbTwo : 2 ≤ b := by omega
  have hPowPos : 0 < p ^ 2 := Nat.pow_pos hp.pos
  have htLtBirth : t < p ^ 3 := by
    rw [← hBirth]
    omega
  have hbLt : b < p := by
    have hMulLt : p ^ 2 * b < p ^ 2 * p := by
      rw [hFactor]
      simpa [pow_succ] using htLtBirth
    exact (Nat.mul_lt_mul_left hPowPos).1 hMulLt
  have hbLiteral : b ∈ RootQuotientPrimeBasis N ∪ (S \ {p ^ 2}) :=
    mem_generators_of_reachableWithin_one_of_two_le hbTwo
      (by simpa using hbReach)
  exact ⟨S, t, b, hS, hSCard, heMem, htHard,
    hbTwo, hbLt, hbLiteral, hFactor⟩

end EnterpriseMath.Quotient
