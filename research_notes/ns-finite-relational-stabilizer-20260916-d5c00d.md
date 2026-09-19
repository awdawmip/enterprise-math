# 有限关系态作为固定精度闭合：三逻辑比特 stabilizer/GHZ 对照

Progress-Event-ID: `NS-FINITE-RELATIONAL-STABILIZER-20260916-D5C00D-18`  
Researcher-ID: `EM-DIRECT-D5C00D / TASK_RESEARCH`  
Research-Activity-ID: `RA-D5C00DF7D77F4AA2ACE0`  
Status: **TESTING — exact finite algebra and executed enumeration; external quantum-comparison assumptions, not native-force or Navier–Stokes theorem.**

## 0. Frontier

Event17 found an exact obstruction to treating raw rational amplitudes as a fixed-resolution native state under arbitrary-depth overlapping three-port reflections: three amplitudes acquire reduced denominator `3^(2n)`. That result was representation-specific, not a no-go for all finite relational encodings.

This note tests a different state carrier. Keep the project six-axis Cell ontology unchanged. Over one Cell (or over explicitly transported registers), encode three **logical** two-level systems using six internal modes, two modes per logical system. Each logical system occupies the one-excitation sector

```
|0_L> = |01>,   |1_L> = |10>.
```

The six internal modes are decorations, not the six native spatial axes. Logical stabilizer/Clifford/Born rules are additional quantum-comparison assumptions. Nothing below derives quantum mechanics, `TRIADIC_CLOSURE_E`, or a physical Hamiltonian from P000.

BRC question: can the exact future operations in a nonclassical finite subtheory be carried by a **finite relation state** rather than by arbitrarily fine amplitude coordinates, and which joint relation is unsafe to erase?

## 1. Finite signed-Pauli relation state

For three logical qubits let `P_3` be the Pauli words in `{I,X,Y,Z}^3`. A pure stabilizer state is represented by its eight-element signed commuting subgroup

```
S = { (+/-1, P) }
```

containing `+III` but not `-III`. Its density matrix is reconstructed exactly as

\[
\rho_S = \frac18\sum_{(s,P)\in S} sP.                 \tag{1.1}
\]

Every signed Pauli entry is in `{0,+/-1,+/-i}`. Therefore every real or imaginary density entry reconstructed from the relation table lies in `(1/8) Z`:

\[
\boxed{\rho_{ab}\in \tfrac18\mathbb Z[i].}            \tag{1.2}
\]

This denominator bound is independent of the depth of a Clifford circuit. It does **not** say an arbitrary quantum state has denominator 8.

For the declared gate set `H_q`, `S_q` and directed `CNOT_{c,t}`, exact conjugation sends every signed Pauli word to another signed Pauli word. Hence the update is a permutation of a finite relation carrier. No new rational denominator is generated at the relation level.

### Executed closure

Starting from `|000>` and exhausting the state graph under 12 generators (3 H, 3 S, 6 directed CNOT), the checker finds exactly

\[
\boxed{1080}
\]

distinct three-qubit stabilizer states. Every reconstructed density matrix is Hermitian, trace one, and has real/imaginary denominators at most 8. The finite count `1080` here is an exact enumeration result and regression certificate. The all-depth closure follows already from finite signed-Pauli conjugation, not from assuming that the 1080-node search approximates a continuum.

The local program derives H/S/CNOT Pauli-conjugation tables from exact matrices instead of hard-coding the stabilizer update signs.

## 2. GHZ relation and exact Mermin witness

Prepare at the logical relation level

```
|000> --H_1--> --CNOT_1,2--> --CNOT_1,3--> |GHZ+>
```

where

\[
|GHZ+\rangle=(|000\rangle+|111\rangle)/\sqrt2.
\]

The resulting relation table contains, among others,

\[
+XXX,\quad +ZZI,\quad +ZIZ,\quad -XYY,\quad -YXY,\quad -YYX.       \tag{2.1}
\]

Therefore the Mermin expression

\[
M=XXX-XYY-YXY-YYX
\]

has

\[
\boxed{\langle M\rangle=4.}                               \tag{2.2}
\]

For a deterministic local-hidden assignment to the six variables `X_1,Y_1,X_2,Y_2,X_3,Y_3 in {+/-1}`, direct finite algebra gives only

\[
X_1X_2X_3-X_1Y_2Y_3-Y_1X_2Y_3-Y_1Y_2X_3\in\{-2,2\}.       \tag{2.3}
\]

Thus the specified quantum comparator is not reproduced by merely adding denser ordinary local hidden residual data while keeping locality and setting-independent assignments. This is a constraint on any future proposed physical bridge, not a derivation of the bridge.

The exact outcome distributions contain four allowed outcomes of probability `1/4` for each of `XXX`, `XYY`, `YXY`, `YYX`; the product sign is fixed by the corresponding stabilizer eigenvalue and every one-party outcome is exactly unbiased.

## 3. BRC fiber witness: pair marginals do not contain the global relation

Compare the coherent GHZ density with the incoherent mixture

\[
\rho_{mix}=\tfrac12(|000\rangle\langle000|+|111\rangle\langle111|). \tag{3.1}
\]

They have **identical one-qubit marginals**:

\[
\rho_q=I/2,\qquad q=1,2,3,                              \tag{3.2}
\]

and identical pair-Z relations

\[
\langle ZZI\rangle=\langle ZIZ\rangle=\langle IZZ\rangle=1.      \tag{3.3}
\]

But

\[
\begin{array}{c|cc}
& \rho_{GHZ} & \rho_{mix}\\ \hline
\langle XXX\rangle&1&0\\
\langle XYY\rangle&-1&0\\
\langle YXY\rangle&-1&0\\
\langle YYX\rangle&-1&0\\
\langle M\rangle&4&0
\end{array}                                                     \tag{3.4}
\]

Hence the observer that keeps all one-party marginals and these pair-Z relations but deletes the global phase relation is **not safe** for future Mermin measurements:

\[
\boxed{\text{same local + pair readout} \not\Rightarrow \text{same future joint readout}.} \tag{3.5}
\]

This is a concrete BRC non-descent certificate. It does not prove that the symbol `XXX` is a native physical force; it proves only that this declared quantum subtheory has a genuinely joint state coordinate that its chosen future operation needs.

## 4. Number-conserving dual-rail embedding

Encode the three logical qubits into six internal two-level modes, pair `q` carrying the code subspace `span{|01>,|10>}`. Define the pair number operator

\[
N_q=n_{2q}+n_{2q+1}.                                    \tag{4.1}
\]

The checker constructs exact 64x64 matrices for:

- logical H acting inside one code pair and identity outside;
- logical CNOT on two encoded pairs and identity when either pair is outside its code sector;
- logical X and Y acting within one pair-number-one sector.

For all these declared code operations,

\[
[U,N_q]=0                                                \tag{4.2}
\]

for every relevant pair. The GHZ preparation stays in

\[
N_1=N_2=N_3=1,\qquad N_{tot}=3.                         \tag{4.3}
\]

Thus within this comparator, the Mermin X/Y measurements need not mix different local excitation sectors. The logical six-mode implementation remains an internal-state model; it is not six new spatial dimensions and it is not a complete device energy account.

## 5. Native spatial transport is separate and finite

A party/register relation can be relabeled under a logical SWAP without changing the stabilizer semantics. Spatially, the already-locked P000 primitive movement remains exactly one of the twelve signed native steps `+/-e_i`.

The checker validates all 12 signed step metadata and separately checks a party-2/party-3 relabeling of the GHZ relation table. This only establishes compatibility of **transport bookkeeping**:

\[
\text{relation state at Cell }z \to \text{same relation state at adjacent Cell }z\pm e_i. \tag{5.1}
\]

It does not certify a primitive force mechanism that performs the transport, and it does not permit an off-axis spatial move to become primitive.

## 6. What event17’s precision obstruction does and does not imply

We now have two exact statements that must not be conflated:

1. The repeated overlapping rational reflections of event17 generate amplitude denominators `3^(2n)`, so **those amplitude coordinates** do not live on one fixed rational grid for arbitrary depth.
2. The stabilizer/Clifford/Pauli subtheory above evolves exactly on a **finite relation state set**, and every reconstructed density matrix has denominator at most 8.

Therefore the event17 obstruction is not a proof that exact nonclassical finite-depth or all-depth relational evolution is impossible. It says a candidate native model should not automatically choose raw amplitudes as the primitive state if it also claims a fixed finite-resolution state alphabet.

Conversely, event18 does not solve universal quantum dynamics. Clifford plus Pauli measurement is a restricted subtheory; arbitrary non-Clifford gates, arbitrary rational measurement axes from event17, and generic states are outside this closure. A native theory that aims to recover more than the stabilizer sector must say how the larger relation population is represented without silently restoring infinite precision.

## 7. Executed exact checks

Command:

```text
python check_stabilizer_relation.py --output results_18.json
```

The checker uses SymPy exact matrices and integers only. It performs:

- BFS over the 3-qubit stabilizer orbit: 1080 states;
- exact H/S/CNOT conjugation maps derived from matrices;
- density reconstruction and denominator audit for every orbit state;
- GHZ stabilizer and density reconstruction;
- one-qubit partial traces and three pair-Z comparisons against the incoherent mixture;
- all 64 deterministic assignments entering the Mermin local-hidden bound;
- exact eight-outcome tables for four Mermin settings;
- a 64-dimensional dual-rail embedding with exact number-commutator checks;
- logical X/Y number-sector checks;
- 12 signed native spatial-step records and a party-relabel relation check.

The clean rerun in a fresh temporary directory produced byte-identical `results_18.json`.

Checker SHA256:

`6ff48da0bbd6a041f580696f464353216696bd21a27d0ac411b0e2dafe4202a4`

Result SHA256:

`c7c74c381dab29b5465f67c432803d68edc257f66bd45c2ee4594b2007afbbed`

## 8. Current conclusion and next unit

This event supplies a positive answer to a narrow question:

\[
\boxed{\text{finite exact joint relation state can carry nonclassical future information without arbitrary denominator growth}} \tag{8.1}
\]

for the three-logical-qubit stabilizer/Clifford/Pauli sector.

It also supplies a negative information result:

\[
\boxed{\text{local marginals + pair relations are insufficient; the global relation is operationally necessary}.} \tag{8.2}
\]

The next native obligation is stronger: construct or constrain a **finite-resolution, local, autonomous relation update on the X6 decorated Cell state** whose legal primitive events generate/transport an analogue of the retained joint coordinate and whose classical readout respects no-signalling/Bell constraints. The stabilizer table is a target interface and a falsifier for information-erasing proposals, not yet the native dynamics itself.

No P000 or worldview file is modified, no Foundation/theorem admission is claimed, and no Navier--Stokes conclusion follows from this event.
