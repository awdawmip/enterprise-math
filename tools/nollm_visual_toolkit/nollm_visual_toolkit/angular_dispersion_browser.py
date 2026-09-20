"""Offline BigInt port of the existing angular observer and BRC division law.

This extends angular_dispersion.py; it is not an independent numeric family.
Domain: non-negative histogram counts and positive scale. The exported record
matches AngularDispersion.as_record. Its trace is locally computed, not a claim
that Python BRC ran inside the browser. Cross-language tests compare all fields.
JavaScript source is embedded in Python to retain the toolkit's wheel layout.
"""

SCRIPT = r'''
// NOLLM_ANGULAR_BIGINT_BRC_PORT_V1: exact histogram observer, not geometry.
const NollmAngularExact = (() => {
  'use strict';
  function natural(value, name) {
    let result;
    if (typeof value === 'bigint') result = value;
    else if (typeof value === 'string' && /^(0|[1-9][0-9]*)$/.test(value)) result = BigInt(value);
    else if (typeof value === 'number' && Number.isSafeInteger(value) && !Object.is(value, -0)) result = BigInt(value);
    else throw new TypeError(name + ' must be an exact non-negative integer or canonical decimal string');
    if (result < 0n) throw new RangeError(name + ' must be non-negative');
    return result;
  }
  function positive(value, name) {
    const result = natural(value, name);
    if (result === 0n) throw new RangeError(name + ' must be positive');
    return result;
  }
  function source(counts) {
    if (!Array.isArray(counts) || counts.length < 1) throw new TypeError('at least one ordered bin required');
    const ordered = [];
    let total = 0n, squares = 0n;
    for (let i = 0; i < counts.length; i++) {
      const count = natural(counts[i], 'bin count');
      ordered.push(count); total += count; squares += count * count;
    }
    if (total === 0n) throw new RangeError('CV squared is undefined for zero population');
    const bins = BigInt(ordered.length), denominator = total * total;
    const numerator = bins * squares - denominator;
    if (numerator < 0n) throw new Error('negative histogram dispersion');
    return {ordered, bins, total, squares, numerator, denominator};
  }
  // Port of brc_evaluate_division, natural domain only. All quotient/remainder
  // materialization is confined here, including phase-bin address readout.
  function divisionTrace(numerator, denominator) {
    const quotient = numerator / denominator, remainder = numerator % denominator;
    const collapsed = denominator * quotient;
    if (collapsed + remainder !== numerator || remainder < 0n || remainder >= denominator)
      throw new Error('BRC division reconstruction failed');
    return {quotient, remainder, collapsed};
  }
  // Port of brc_scaled_evaluate; caller supplies a validated histogram ratio.
  function brcReadout(numerator, denominator, scale) {
    const s = positive(scale, 'scale'), scaled = s * numerator;
    const {quotient, remainder, collapsed} = divisionTrace(scaled, denominator);
    return {
      kind: 'INTEGER_PLUS_RATIONAL_RESIDUAL_OF_CV_SQUARED', scale: String(s),
      integer: String(quotient), residual_numerator: String(remainder),
      residual_denominator: String(denominator * s),
      trace: {evaluation_kind: 'BRC_DIVISION_EVALUATION', numerator: String(scaled),
        denominator: String(denominator), quotient: String(quotient),
        remainder: String(remainder), collapsed_numerator: String(collapsed)}
    };
  }
  function fromCounts(counts, scale = null) {
    const a = source(counts);
    return {
      schema: 'NOLLM_ANGULAR_CV_SQUARED_V1',
      scope: 'ORDERED_HISTOGRAM_OBSERVER_NOT_NATIVE_GEOMETRY', integer_encoding: 'DECIMAL_STRING',
      counts: a.ordered.map(String), bins: String(a.bins), population: String(a.total),
      sum_squares: String(a.squares), numerator: String(a.numerator), denominator: String(a.denominator),
      definition: '(bins*sum_squares-population*population)/(population*population)',
      readout: scale === null ? null : brcReadout(a.numerator, a.denominator, scale)
    };
  }
  function signDifference(left, right) { return left < right ? -1 : left > right ? 1 : 0; }
  function compareCounts(left, right) {
    const a = source(left), b = source(right);
    return signDifference(a.numerator * b.denominator, b.numerator * a.denominator);
  }
  function compareRatio(counts, numerator, denominator) {
    const a = source(counts), n = natural(numerator, 'threshold numerator'), d = positive(denominator, 'threshold denominator');
    return signDifference(a.numerator * d, n * a.denominator);
  }
  function phaseBin(tick, modulus, bins) {
    const t = natural(tick, 'phase tick'), m = positive(modulus, 'phase modulus'), b = positive(bins, 'bins');
    if (b < 2n || b > 256n || t >= m) throw new RangeError('phase or bins outside declared domain');
    // A bounded array-index conversion only: result is in 0..255 exactly.
    return Number(divisionTrace(t * b, m).quotient);
  }
  // Shared natural-domain BRC boundary used by the certified-cell port.
  function evaluateDivision(numerator, denominator) {
    return divisionTrace(natural(numerator, 'numerator'), positive(denominator, 'denominator'));
  }
  return Object.freeze({fromCounts, compareCounts, compareRatio, phaseBin, evaluateDivision});
})();
'''
