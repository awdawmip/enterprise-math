// D25 neutral author-side finite precision certificate, 2026-11-04.
// BigInt only; exact arithmetic in (Z/p^e) for p >= 5.
// Not a universal prime theorem, native X6 benchmark, or Source Result.
function mod(x, n) { return ((x % n) + n) % n; }
function inv(a, n) {
  let b = n, x = 1n, y = 0n;
  a = mod(a, n);
  while (b !== 0n) {
    const q = a / b;
    [a, b] = [b, a - q * b];
    [x, y] = [y, x - q * y];
  }
  if (a !== 1n) throw Error("Nonunit denominator");
  return mod(x, n);
}
function primesUpTo(limit) {
  const prime = Array(limit + 1).fill(true);
  prime[0] = prime[1] = false;
  for (let i = 2; i * i <= limit; i++)
    if (prime[i]) for (let j = i * i; j <= limit; j += i) prime[j] = false;
  return prime.flatMap((yes, i) => yes && i >= 5 ? [i] : []);
}
function coefficientsAndSums(p, e) {
  const P = BigInt(p), m = P ** BigInt(e);
  let a = 1n, b = 1n, W = 1n, V = 1n, Vhalf = 1n;
  for (let k = 1; k < p; k++) {
    const j = BigInt(k - 1), K = BigInt(k), den = K ** 3n;
    a = a * (2n*j+1n) * (3n*j+1n) * (3n*j+2n)
        * inv(36n * den, m) % m;
    b = b * (4n*j+1n) * (4n*j+2n) * (4n*j+3n)
        * inv(576n * den, m) % m;
    W = (W + (6n*K+1n)*a) % m;
    V = (V + (8n*K+1n)*b) % m;
    if (k <= (p - 1) / 2) Vhalf = (Vhalf + (8n*K+1n)*b) % m;
  }
  return { W, V, Vhalf, modulus: m };
}
function factorialReconstruction(p, e) {
  const P = BigInt(p), m = P ** BigInt(e);
  const f = [1n];
  for (let j = 1; j <= 4*(p-1); j++) f.push(f[j-1]*BigInt(j));
  const C = (n,k) => f[n]/(f[k]*f[n-k]);
  let W = 0n, V = 0n;
  for (let k = 0; k < p; k++) {
    const K = BigInt(k), central = C(2*k,k)**2n;
    const a = central*C(3*k,k)%m*inv(216n**K,m)%m;
    const b = central*C(4*k,2*k)%m*inv(2304n**K,m)%m;
    W = (W+(6n*K+1n)*a)%m;
    V = (V+(8n*K+1n)*b)%m;
  }
  return { W, V };
}
function verify() {
  const ps = primesUpTo(2000);
  const sourceCases = new Set([5,7,11,13,19,23,97,373]);
  const sharpCases = [11,13,19,373];
  let exact = 0, nonzeroComparison = 0, nonzeroHalfTail = 0;
  const comparisonZeros = [], halfTailZeros = [];
  const examples = [];
  for (const p of ps) {
    const P = BigInt(p), p3 = P**3n;
    const z = coefficientsAndSums(p, 4);
    const chi = p%3===1 ? 1n : -1n; // (-3/p)
    const conjectured = mod(z.W-2n*z.V+chi*P, z.modulus);
    if (conjectured !== 0n) throw Error("Fourth-digit failure at p="+p);
    const delta = mod(z.W-z.V,z.modulus);
    const tail = mod(z.V-z.Vhalf,z.modulus);
    if (delta%p3 !== 0n || tail%p3 !== 0n)
      throw Error("Earlier third-digit invariant failure at p="+p);
    if (delta) nonzeroComparison++; else comparisonZeros.push(p);
    if (tail) nonzeroHalfTail++; else halfTailZeros.push(p);
    if (sourceCases.has(p)) {
      const check = factorialReconstruction(p,4);
      if (check.W !== z.W || check.V !== z.V)
        throw Error("Independent binomial mismatch at p="+p);
      examples.push({
        p, W_mod_p4: z.W.toString(), V_mod_p4: z.V.toString(),
        W_minus_V_over_p3_mod_p: (delta/p3).toString(),
        V_full_minus_half_over_p3_mod_p: (tail/p3).toString()
      });
    }
    exact++;
  }
  const sharp = sharpCases.map(p=>{
    const P=BigInt(p), z=coefficientsAndSums(p,5);
    const direct=factorialReconstruction(p,5);
    if (direct.W!==z.W || direct.V!==z.V)
      throw Error("Precision-five independent reconstruction mismatch p="+p);
    const chi=p%3===1?1n:-1n, residual=mod(z.W-2n*z.V+chi*P,z.modulus);
    if (residual%(P**4n)!==0n) throw Error("Precision-five carry mismatch p="+p);
    return {p, residue_mod_p5:residual.toString(), fourth_digit:(residual/(P**4n)).toString()};
  });
  return {
    schema:"D25_SIGNED_FOURTH_DIGIT_EXACT_FINITE_V1",
    domain:"all primes 5 <= p <= 2000", tested_primes:exact,
    modulus:"p^4", finite_candidate:"W_p-2*V_p+p*(-3/p) == 0 mod p^4",
    errors:0, nonzero_W_minus_V_mod_p4:nonzeroComparison,
    W_minus_V_zero_p:comparisonZeros,
    nonzero_quartic_full_minus_half_mod_p4:nonzeroHalfTail,
    full_minus_half_zero_p:halfTailZeros,
    independent_factorial_examples:examples,
    p5_falsifying_higher_precision:sharp,
    global_proof:"NOT_ESTABLISHED", native_benchmark:"NOT_EXECUTED"
  };
}
const result = verify();
if (typeof process !== "undefined" && process.stdout) process.stdout.write(JSON.stringify(result,null,2)+"\n");
result;