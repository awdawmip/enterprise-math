// X6 R100 author-side exact integer crosscheck.
// Conditional positive-count BRC histogram, not native X6 dynamics.
// Columns: [Port q, U, V, H, K]. All values are exact integers.
const C = [
  [1,1,3,7,4], [4,1,1,12,11], [6,1,3,6,8],
  [7,0,0,12,12], [10,0,3,6,3], [11,1,1,1,1],
  [16,1,6,1,5], [17,0,3,6,9], [21,1,4,6,2],
  [27,0,6,0,6]
];
const result = [];
let cases = 0;
for (let p = 11; p <= 40; ++p) {
  let maxTies = 0;
  let locations = [];
  for (let S = 1; S <= 40; ++S) {
    for (let T = 1; T <= 40; ++T) {
      // Multiplier divisible by every score denominator.
      const D = 2*(S+1)*(T+1)*(S+T);
      const scores = C.filter(a => a[0] <= p).map(a =>
        Math.max(a[1]*D/2, a[2]*D/(S+1),
                 a[3]*D/(T+1), a[4]*D/(S+T)));
      const best = Math.min(...scores);
      const ties = scores.filter(x => x === best).length;
      if (ties > maxTies) { maxTies = ties; locations = [[S,T]]; }
      else if (ties === maxTies) locations.push([S,T]);
      ++cases;
    }
  }
  const expectedMax = p <= 16 ? 6 : 7;
  const expectedLocations = p <= 26 ? [[5,23]] : [[5,23],[11,11]];
  if (maxTies !== expectedMax ||
      JSON.stringify(locations) !== JSON.stringify(expectedLocations)) {
    throw new Error(JSON.stringify({p,maxTies,locations,expectedMax,expectedLocations}));
  }
  result.push({p,maxTies,locations});
}
console.log(JSON.stringify({
  status:"PASS", parameter_domain:"integer S,T in 1..40",
  port_domain:"all integer p in 11..40",
  cases, budgets:result.length, maximum_at_p11:result[0],
  maximum_at_p17:result[6], maximum_at_p27:result[16],
  universal_argument:"R100 symbolic region and strict inequality proof"
},null,2));
