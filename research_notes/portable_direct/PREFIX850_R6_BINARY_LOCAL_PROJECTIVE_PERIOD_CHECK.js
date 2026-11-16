#!/usr/bin/env node
"use strict";
/* PREFIX-850: exact binary named-source local-update modular observer.
 * No floating point is used in the number-theory or injectivity tests.
 * This is an auxiliary Q-only BRC scalar observer, not an X6-native event.
 */
function projectivePeriod(q) {
  if (q <= 1n || q % 2n === 0n) throw Error("q must be odd and >1");
  let a = 2n % q;
  for (let d = 1n; d <= q; d++) {
    if (a === 1n || a === q - 1n) return Number(d);
    a = (a * 2n) % q;
  }
  throw Error("Unreachable: finite multiplicative group");
}
function minimalModulus(p) {
  if (!Number.isInteger(p) || p < 1) throw Error("p must be positive integer");
  for (let q = 3; q < 9 * p + 3; q += 2) {
    if (projectivePeriod(BigInt(q)) >= p) return q;
  }
  throw Error("The explicit 3-power upper bound was violated");
}
function threePowerConstruction(p) {
  let q = 3;
  let span = 1;
  while (span < p) { q *= 3; span *= 3; }
  return q;
}
function bruteAllKnownPredecessors(p, q) {
  if (p > 9) throw Error("brute scope deliberately capped at p<=9");
  for (let x = 0; x < 2 ** p; x++) {
    const residues = new Set([x % q]);
    for (let i = 0; i < p; i++) {
      const next = (x ^ (1 << i)) % q;
      if (residues.has(next)) return false;
      residues.add(next);
    }
  }
  return true;
}
function exactBitWidth(q) { return BigInt(q - 1).toString(2).length; }
function verify() {
  const exact = [];
  for (let p = 1; p <= 64; p++) {
    const q = minimalModulus(p);
    const upper = threePowerConstruction(p);
    if (!(q >= 2 * p + 1 && q <= upper && upper < 9 * p))
      throw Error("Asymptotic bound failed, p=" + p);
    if (projectivePeriod(BigInt(upper)) < p)
      throw Error("3-power construction failed, p=" + p);
    exact.push({
      p, minimal_odd_modulus: q, exact_port_bits: exactBitWidth(q),
      projective_period: projectivePeriod(BigInt(q)),
      explicit_three_power_modulus: upper
    });
  }
  let exhaustive = 0;
  for (let p = 1; p <= 9; p++) {
    const top = Math.max(45, minimalModulus(p) + 4);
    for (let q = 3; q <= top; q += 2) {
      const predicted = projectivePeriod(BigInt(q)) >= p;
      const actual = bruteAllKnownPredecessors(p, q);
      if (predicted !== actual)
        throw Error("Signed-power/neighbor mismatch p=" + p + ", q=" + q);
      exhaustive++;
    }
  }
  for (let k = 1; k <= 8; k++) {
    const q = 3 ** k;
    if (projectivePeriod(BigInt(q)) !== 3 ** (k - 1))
      throw Error("3-adic projective period failed, k=" + k);
  }
  return {
    schema: "PREFIX850_R6_BINARY_LOCAL_PROJECTIVE_PERIOD_RESULTS_V1",
    status: "ALL_EXACT_ASSERTIONS_PASSED",
    scientific_input_pin: "f42f2906d77f24085c123f3ccfe9667d41caa96d",
    exact_minima_p_range: [1, 64],
    exact_minima_count: exact.length,
    independently_enumerated_neighbor_cases: exhaustive,
    exhaustive_binary_predecessor_range: [1, 9],
    verified_three_power_exponents: [1, 8],
    data: exact,
    scope_note: "Auxiliary named positive-integer Q-only BRC scalar observer; known previous source state; no native X6 authorization or model validation"
  };
}
const result = verify();
process.stdout.write(JSON.stringify(result, null, 2) + "\n");
