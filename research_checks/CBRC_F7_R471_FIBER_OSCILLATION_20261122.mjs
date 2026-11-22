// Exact fiber-swap evaluation for the frozen F7 r469 quarter-valued witness.
// Run: node research_checks/CBRC_F7_R471_FIBER_OSCILLATION_20261122.mjs
import { readFileSync } from "node:fs";

const rows = JSON.parse(readFileSync(
  new URL("../research_artifacts/F7_R469_B14_Exact_Quarter_Witness_20261122.json", import.meta.url),
  "utf8",
));
const table = new Map(rows.map(([x, y, n]) => [`${x},${y}`, n]));
const fibers = new Map();
const representatives = new Set([0]);

for (const [x, y, n] of rows) {
  for (const sx of new Set([x, -x])) {
    const r = sx - y;
    const t = sx - 2 * y;
    representatives.add(r);
    representatives.add(t);
    if (!fibers.has(r)) fibers.set(r, new Map());
    fibers.get(r).set(t, 2 + n);
  }
}
const specialCount = representatives.size;
const outside1 = Math.max(...representatives) + 1000;
const outside2 = outside1 + 1000;
representatives.add(outside1);
representatives.add(outside2);

function h(r, t) {
  if (r === 0 && t === 0) return 0;
  if (r === t) return 4;
  return fibers.get(r)?.get(t) ?? 2;
}

function finite(B) {
  const ranges = [];
  for (let r = -2 * B; r <= 2 * B; r++) {
    const lo = Math.max(2 * r - B, r - B);
    const hi = Math.min(2 * r + B, r + B);
    if (lo <= hi) ranges.push({ r, lo, hi });
  }
  let max = 0;
  let evaluations = 0;
  let witness = null;
  for (const R of ranges) {
    for (const U of ranges) {
      let minR = Infinity, maxR = -Infinity, argminR = 0, argmaxR = 0;
      let minU = Infinity, maxU = -Infinity, argminU = 0, argmaxU = 0;
      for (let t = R.lo; t <= R.hi; t++) {
        const value = h(R.r, t) - h(U.r, t);
        if (value < minR) { minR = value; argminR = t; }
        if (value > maxR) { maxR = value; argmaxR = t; }
        evaluations++;
      }
      for (let s = U.lo; s <= U.hi; s++) {
        const value = h(R.r, s) - h(U.r, s);
        if (value < minU) { minU = value; argminU = s; }
        if (value > maxU) { maxU = value; argmaxU = s; }
        evaluations++;
      }
      for (const [v, t, s, sign] of [
        [maxU - minR, argminR, argmaxU, 1],
        [maxR - minU, argmaxR, argminU, -1],
      ]) {
        if (v > max) {
          max = v;
          witness = {
            z: [2 * R.r - t, R.r - t, 2 * U.r - s, U.r - s],
            numerator4D: sign * v,
          };
        }
      }
    }
  }
  return { B, max4D: max, evaluations, witness };
}

function global() {
  let max = 0, witness = null, pairs = 0;
  for (const r of representatives) {
    for (const u of representatives) {
      pairs++;
      const critical = new Set([0, r, u, 10000000]);
      for (const t of fibers.get(r)?.keys() ?? []) critical.add(t);
      for (const t of fibers.get(u)?.keys() ?? []) critical.add(t);
      let low = Infinity, high = -Infinity, tLow = 0, tHigh = 0;
      for (const t of critical) {
        const value = h(r, t) - h(u, t);
        if (value < low) { low = value; tLow = t; }
        if (value > high) { high = value; tHigh = t; }
      }
      if (high - low > max) {
        max = high - low;
        witness = { z: [2*r-tLow, r-tLow, 2*u-tHigh, u-tHigh], numerator4D: max };
      }
    }
  }
  return { specialCount, representativeCount: representatives.size, pairs, max4D: max, witness };
}

const a14 = finite(14), a15 = finite(15), a32 = finite(32), full = global();
if (rows.length !== 1190 || a14.max4D !== 2 ||
    a15.max4D !== 4 || a32.max4D !== 4 ||
    full.specialCount !== 276 || full.representativeCount !== 278 ||
    full.pairs !== 77284 || full.max4D !== 4) {
  throw new Error("Frozen r469 quarter-witness result mismatch");
}
console.log(JSON.stringify({ sourceRows: rows.length, finite: [a14, a15, a32], global: full }, null, 2));
