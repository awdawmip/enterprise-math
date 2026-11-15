// R195 exact reference check: binary-field affine last-occurrence action.
// Self-contained Node.js 18+, no dependencies or random sampling.
import assert from 'node:assert/strict';

function allStates(k) {
  const out = [[]];
  function visit(word, used) {
    for (let i = 0; i < k; i++) {
      if (used.has(i)) continue;
      used.add(i); word.push(i); out.push(word.slice());
      visit(word, used); word.pop(); used.delete(i);
    }
  }
  visit([], new Set());
  return out;
}
function features(k) {
  const out = [];
  for (let i = 0; i < k; i++) out.push([i]);
  for (let i = 0; i < k; i++)
    for (let j = i + 1; j < k; j++) out.push([i, j]);
  return out;
}
function star(left, right) {
  const rightSet = new Set(right);
  return left.filter((x) => !rightSet.has(x)).concat(right);
}
// 0 = identity, 1 = constant 0, 2 = constant 1 over F_2.
function action(word, featuresList) {
  return featuresList.map((U) => {
    for (let n = word.length - 1; n >= 0; n--) {
      const pos = U.indexOf(word[n]);
      if (pos >= 0) return U.length === 1 || pos === 0 ? 1 : 2;
    }
    return 0;
  });
}
function orbitAtOnes(A) {
  return A.map((state) => (state === 1 ? '0' : '1')).join('');
}
function compose(first, second) {
  return first.map((old, i) => second[i] === 0 ? old : second[i]);
}
const rows = [];
for (let k = 1; k <= 7; k++) {
  const S = allStates(k), C = features(k), encoded = S.map((w) => action(w, C));
  const actionSignatures = new Set(encoded.map((a) => a.join(',')));
  const orbitSignatures = new Set(encoded.map(orbitAtOnes));
  assert.equal(actionSignatures.size, S.length, 'action injectivity k=' + k);
  assert.equal(orbitSignatures.size, S.length, 'one-orbit injectivity k=' + k);
  let append = 0, products = 0;
  const generators = Array.from({length:k}, (_,a) => action([a], C));
  for (let i = 0; i < S.length; i++) {
    for (let a = 0; a < k; a++) {
      assert.deepEqual(compose(encoded[i], generators[a]), action(star(S[i], [a]), C),
        'generator append k=' + k + ' state=' + i + ' generator=' + a);
      append++;
    }
  }
  if (k <= 5) {
    for (let i = 0; i < S.length; i++) {
      for (let j = 0; j < S.length; j++) {
        assert.deepEqual(compose(encoded[i], encoded[j]), action(star(S[i], S[j]), C),
          'pair product k=' + k + ' left=' + i + ' right=' + j);
        products++;
      }
    }
  }
  rows.push({k, dimension:C.length, quotient_states:S.length,
    distinct_actions:actionSignatures.size, distinct_single_orbit_points:orbitSignatures.size,
    generator_appends_checked:append, ordered_pair_products_checked:products});
}
const total = (key) => rows.reduce((n,r) => n+r[key], 0);
const result = {
  schema:'ENTERPRISE_MATH_R195_EXACT_BINARY_AFFINE_CHECK_V1',
  status:'PASS', frozen_scientific_input:'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
  arithmetic:'exact F_2 bit values; exhaustive finite enumeration, no floats',
  validated:'all partial-permutation states for k=1..7; every generator append k=1..7; every ordered product k=1..5',
  rows,
  totals: {states:total('quotient_states'), generator_appends:total('generator_appends_checked'),
    ordered_pair_products:total('ordered_pair_products_checked')},
  scope:'Finite checks only; all-field lower bound relies on the algebraic proof; no native BRC integration or independent review'
};
console.log(JSON.stringify(result,null,2));
