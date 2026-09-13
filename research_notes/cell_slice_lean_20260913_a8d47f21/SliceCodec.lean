import Std

/-!
Formal target: the THREE-region codec in the user-visible verify_lines.py
(SHA256 b190bf460e87c855c2e4f5b4c61b75473c0422afad70bd2b7deb1663d6ee54e7).
A fixed two-generator native slice, NOT a codec for arbitrary full X6 states.
The coordinate-reference drawing is not a vertex or an edge.
Code constructors store positive displayed entries minus one.
No new spatial axis, metric, native direction, or physical transition is added.
-/
namespace EnterpriseMath.CellAddress.ThreeRegionSlice

abbrev Point := Int × Int

/-- A = first displayed field zero; B = second zero; C = third zero.
All constructor arguments are natural offsets: the displayed active count is +1. -/
inductive Code where
  | A (b c : Nat)
  | B (a c : Nat)
  | C (a b : Nat)
  deriving DecidableEq, Repr

/-- The final six fields are nonnegative; only the first three are used here. -/
def digits : Code → List Nat
  | .A b c => [0, b + 1, c + 1, 0, 0, 0]
  | .B a c => [a + 1, 0, c + 1, 0, 0, 0]
  | .C a b => [a + 1, b + 1, 0, 0, 0, 0]

def decode : Code → Point
  | .A b c => (-(c : Int), (b : Int) - c)
  | .B a c => ((a : Int) + 1 - c, -(c : Int))
  | .C a b => ((a : Int) + 1, (b : Int) + 1)

def encode (p : Point) : Code :=
  if p.1 ≤ 0 ∧ p.1 ≤ p.2 then
    .A (p.2 - p.1).toNat (-p.1).toNat
  else if p.2 ≤ 0 ∧ p.2 + 1 ≤ p.1 then
    .B (p.1 - p.2 - 1).toNat (-p.2).toNat
  else
    .C (p.1 - 1).toNat (p.2 - 1).toNat

/-- The three original region conditions exhaust the full integer slice. -/
theorem region_exhaustive (m n : Int) :
    (m ≤ 0 ∧ m ≤ n) ∨ (n ≤ 0 ∧ n + 1 ≤ m) ∨ (1 ≤ m ∧ 1 ≤ n) := by
  omega

theorem decode_encode (p : Point) : decode (encode p) = p := by
  rcases p with ⟨m, n⟩
  unfold encode
  split
  · simp only [decode]
    apply Prod.ext <;> dsimp <;> omega
  · split
    · simp only [decode]
      apply Prod.ext <;> dsimp <;> omega
    · simp only [decode]
      apply Prod.ext <;> dsimp <;> omega

theorem encode_decode (q : Code) : encode (decode q) = q := by
  cases q with
  | A b c =>
    unfold decode encode
    split
    · congr 1 <;> omega
    · omega
  | B a c =>
    unfold decode encode
    split
    · omega
    · split
      · congr 1 <;> omega
      · omega
  | C a b =>
    unfold decode encode
    split
    · omega
    · split
      · omega
      · congr 1 <;> omega

theorem encode_injective {p q : Point} (h : encode p = encode q) : p = q := by
  have hh := congrArg decode h
  simpa only [decode_encode] using hh

theorem decode_injective {p q : Code} (h : decode p = decode q) : p = q := by
  have hh := congrArg encode h
  simpa only [encode_decode] using hh

theorem digits_injective {p q : Code} (h : digits p = digits q) : p = q := by
  cases p <;> cases q <;> simp_all [digits]

theorem digits_length (q : Code) : (digits q).length = 6 := by
  cases q <;> rfl

theorem digits_nonnegative (q : Code) (n : Nat) (_h : n ∈ digits q) : 0 ≤ n := by
  exact Nat.zero_le n

theorem zero_marker_not_a_cell (q : Code) : digits q ≠ [0, 0, 0, 0, 0, 0] := by
  cases q <;> simp [digits]

/-- Existing signed primitive moves in the retained two-coordinate slice.
These are operation labels, not extra signed output fields. -/
inductive Dir where
  | e1p | e1m | e2p | e2m
  deriving DecidableEq, Repr

def nativeStep : Dir → Point → Point
  | .e1p, (m, n) => (m + 1, n)
  | .e1m, (m, n) => (m - 1, n)
  | .e2p, (m, n) => (m, n + 1)
  | .e2m, (m, n) => (m, n - 1)

/-- Direct piecewise table, independent of encode/decode. This mirrors the
actual Python code_step table, with positive fields represented as Nat+1. -/
def step : Dir → Code → Code
  | .e1p, .A 0 c => .B 0 c
  | .e1p, .A (b + 1) 0 => .C 0 b
  | .e1p, .A (b + 1) (c + 1) => .A b c
  | .e1p, .B a c => .B (a + 1) c
  | .e1p, .C a b => .C (a + 1) b
  | .e1m, .A b c => .A (b + 1) (c + 1)
  | .e1m, .B 0 c => .A 0 c
  | .e1m, .B (a + 1) c => .B a c
  | .e1m, .C 0 b => .A (b + 1) 0
  | .e1m, .C (a + 1) b => .C a b
  | .e2p, .A b c => .A (b + 1) c
  | .e2p, .B a 0 => .C a 0
  | .e2p, .B 0 (c + 1) => .A 0 c
  | .e2p, .B (a + 1) (c + 1) => .B a c
  | .e2p, .C a b => .C a (b + 1)
  | .e2m, .A 0 c => .B 0 (c + 1)
  | .e2m, .A (b + 1) c => .A b c
  | .e2m, .B a c => .B (a + 1) (c + 1)
  | .e2m, .C a 0 => .B a 0
  | .e2m, .C a (b + 1) => .C a b

theorem decode_step (d : Dir) (q : Code) :
    decode (step d q) = nativeStep d (decode q) := by
  cases d <;> cases q <;> rename_i a b <;> cases a <;> cases b <;>
    simp [step, decode, nativeStep] <;> omega

theorem step_encode (d : Dir) (p : Point) :
    step d (encode p) = encode (nativeStep d p) := by
  apply decode_injective
  simp only [decode_step, decode_encode]

def opposite : Dir → Dir
  | .e1p => .e1m
  | .e1m => .e1p
  | .e2p => .e2m
  | .e2m => .e2p

theorem native_reverse (d : Dir) (p : Point) :
    nativeStep (opposite d) (nativeStep d p) = p := by
  rcases p with ⟨m,n⟩
  cases d <;> simp [opposite, nativeStep] <;> omega

theorem step_reverse (d : Dir) (q : Code) : step (opposite d) (step d q) = q := by
  apply decode_injective
  rw [decode_step, decode_step, native_reverse]

/-- The exact user-suggested equal-value switch holds for an infinite family. -/
theorem equal_crossing_AB (k : Nat) :
    digits (.A 0 k) = [0, 1, k + 1, 0, 0, 0] ∧
    digits (step .e1p (.A 0 k)) = [1, 0, k + 1, 0, 0, 0] := by
  constructor <;> rfl

theorem equal_crossing_BC (k : Nat) :
    digits (.B k 0) = [k + 1, 0, 1, 0, 0, 0] ∧
    digits (step .e2p (.B k 0)) = [k + 1, 1, 0, 0, 0, 0] := by
  constructor <;> rfl

/-- A different boundary adjusts a count; equal-value transfer is not universal. -/
theorem adjusted_crossing_AC (k : Nat) :
    digits (.A (k + 1) 0) = [0, k + 2, 1, 0, 0, 0] ∧
    digits (step .e1p (.A (k + 1) 0)) = [1, k + 1, 0, 0, 0, 0] := by
  constructor <;> rfl

/-- Concrete witnesses from the user-visible L1 and L3 lines. -/
theorem L1_boundary : digits (step .e1p (.A 0 3)) = [1,0,4,0,0,0] := by rfl

theorem L3_boundary : digits (step .e1p (.A 4 0)) = [1,4,0,0,0,0] := by rfl

theorem not_always_increment :
    (digits (step .e1p (.A 0 3))).sum = (digits (.A 0 3)).sum := by decide

theorem not_always_pure_permutation :
    (digits (step .e1p (.A 4 0))).sum ≠ (digits (.A 4 0)).sum := by decide

/-- Same ordered primitive labels, evaluated in each representation. -/
def nativeWalk : Point → List Dir → Point
  | p, [] => p
  | p, d :: ds => nativeWalk (nativeStep d p) ds

def codeWalk : Code → List Dir → Code
  | q, [] => q
  | q, d :: ds => codeWalk (step d q) ds

theorem decode_walk (q : Code) (w : List Dir) :
    decode (codeWalk q w) = nativeWalk (decode q) w := by
  induction w generalizing q with
  | nil => rfl
  | cons d ds ih =>
    simp only [codeWalk, nativeWalk, ih, decode_step]

theorem walk_encode (p : Point) (w : List Dir) :
    codeWalk (encode p) w = encode (nativeWalk p w) := by
  apply decode_injective
  simp only [decode_walk, decode_encode]

/-- No ordered path words are added, removed, or conflated by encoding. -/
theorem word_fiber_iff (a b : Code) (w : List Dir) :
    codeWalk a w = b ↔ nativeWalk (decode a) w = decode b := by
  constructor
  · intro h
    have hh := congrArg decode h
    simpa only [decode_walk] using hh
  · intro h
    apply decode_injective
    simpa only [decode_walk] using h

def NativeReachAt (p q : Point) (k : Nat) : Prop :=
  ∃ w : List Dir, w.length = k ∧ nativeWalk p w = q

def CodeReachAt (a b : Code) (k : Nat) : Prop :=
  ∃ w : List Dir, w.length = k ∧ codeWalk a w = b

theorem reachAt_iff (a b : Code) (k : Nat) :
    CodeReachAt a b k ↔ NativeReachAt (decode a) (decode b) k := by
  constructor
  · intro ⟨w, hlen, hw⟩
    exact ⟨w, hlen, (word_fiber_iff a b w).mp hw⟩
  · intro ⟨w, hlen, hw⟩
    exact ⟨w, hlen, (word_fiber_iff a b w).mpr hw⟩

def NativeShortest (p q : Point) (k : Nat) : Prop :=
  NativeReachAt p q k ∧ ∀ j, NativeReachAt p q j → k ≤ j

def CodeShortest (a b : Code) (k : Nat) : Prop :=
  CodeReachAt a b k ∧ ∀ j, CodeReachAt a b j → k ≤ j

theorem shortest_iff (a b : Code) (k : Nat) :
    CodeShortest a b k ↔ NativeShortest (decode a) (decode b) k := by
  simp only [CodeShortest, NativeShortest, reachAt_iff]

/-- Count an arbitrary finite population of candidate words with multiplicity. -/
def nativeAccepted (p q : Point) : List (List Dir) → Nat
  | [] => 0
  | w :: ws => (if nativeWalk p w = q then 1 else 0) + nativeAccepted p q ws

def codeAccepted (a b : Code) : List (List Dir) → Nat
  | [] => 0
  | w :: ws => (if codeWalk a w = b then 1 else 0) + codeAccepted a b ws

theorem brc_count_preserved (a b : Code) (ws : List (List Dir)) :
    codeAccepted a b ws = nativeAccepted (decode a) (decode b) ws := by
  induction ws with
  | nil => rfl
  | cons w ws ih =>
    simp only [codeAccepted, nativeAccepted, word_fiber_iff, ih]

/-- Re-encoding cannot change any old scalar observer on the decoded endpoints. -/
theorem observer_preserved {α : Type} (f : Point → Point → α) (p q : Point) :
    f (decode (encode p)) (decode (encode q)) = f p q := by
  simp only [decode_encode]

def nativeSquared (p q : Point) : Int :=
  (q.1 - p.1)^2 + (q.2 - p.2)^2

def codeSquared (a b : Code) : Int := nativeSquared (decode a) (decode b)

theorem metric_preserved (p q : Point) :
    codeSquared (encode p) (encode q) = nativeSquared p q := by
  exact observer_preserved nativeSquared p q

/-- Only a fixed two-generator section is asserted: no hidden-coordinate quotient. -/
def embed (p : Point) : List Int := [p.1, p.2, 0, 0, 0, 0]

theorem embed_injective {p q : Point} (h : embed p = embed q) : p = q := by
  rcases p with ⟨m,n⟩
  rcases q with ⟨u,v⟩
  simp [embed] at h
  exact Prod.ext h.1 h.2

#print axioms decode_encode
#print axioms encode_decode
#print axioms digits_injective
#print axioms decode_step
#print axioms step_reverse
#print axioms equal_crossing_AB
#print axioms adjusted_crossing_AC
#print axioms decode_walk
#print axioms word_fiber_iff
#print axioms shortest_iff
#print axioms brc_count_preserved
#print axioms metric_preserved

end EnterpriseMath.CellAddress.ThreeRegionSlice
