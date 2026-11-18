// Run with node inert_check.js. Fixed test domain: target primes below 1000.
// Products are reduced after every multiplication; all Number intermediates
// are exact integers below 2^53 throughout this domain.
"use strict";

function mod(a, m) {
  return ((a % m) + m) % m;
}

function inverse(a, m) {
  let dividend = a;
  let divisor = m;
  let first = 1;
  let second = 0;
  while (divisor !== 0) {
    const quotient = Math.floor(dividend / divisor);
    [dividend, divisor] = [divisor, dividend - quotient * divisor];
    [first, second] = [second, first - quotient * second];
  }
  if (dividend !== 1) throw Error("Expected a unit");
  return mod(first, m);
}

function product(factors, m) {
  return factors.reduce((value, factor) => value * factor % m, 1);
}

function check(p) {
  const m2 = p * p;
  const inv36 = inverse(36, m2);
  let b = 1, c = 1, g = 0, h = 0, weighted = 0;
  for (let k = 0; k < p; k++) {
    g = (g + b) % m2;
    h = (h + (12*k + 1) * b) % p;
    weighted = (weighted + (6*k + 1) * c) % m2;
    if (k + 1 === p) break;
    const inv = inverse(k + 1, m2);
    b = product([b, 6*k + 1, 3*k + 1, inv, inv, inv36], m2);
    c = product([c, 2*k + 1, 3*k + 1, 3*k + 2, inv, inv, inv, inv36], m2);
  }
  // P_r(t) = coefficients[r] * t^(r mod 2), t^2 = 1/2.
  const n = (p - 1) / 3;
  const coefficients = [1, 1];
  const half = inverse(2, p);
  for (let r = 1; r < n; r++) {
    const tFactor = r % 2 ? half : 1;
    const first = product([2*r + 1, tFactor, coefficients[r]], p);
    const delta = mod(first - r * coefficients[r-1], p);
    coefficients.push(delta * inverse(r + 1, p) % p);
  }
  let sum = 0;
  for (let j = 1; j <= n; j++) {
    sum += product([coefficients[j-1], coefficients[n-j], inverse(j, p)], p);
  }
  const companionDigit = mod(-sum * inverse(12, p), p);
  if (weighted !== p || g % p || coefficients[n] !== 0 ||
      g / p * h % p !== 1 || g / p !== companionDigit) {
    throw Error("Failed at p=" + p);
  }
  return [p, weighted, g, h, g / p, companionDigit];
}

function prime(n) {
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return false;
  return n > 1;
}

const rows = [];
for (let p = 2; p < 1000; p++) {
  if ([13, 19].includes(p % 24) && prime(p)) rows.push(check(p));
}
console.log(JSON.stringify({count: rows.length, examples: rows.slice(0, 4), last: rows.at(-1)}));
