#!/usr/bin/env node
'use strict';
// Frozen auxiliary Walsh fiber; source K is the eight-facet R749SPR theorem.
// Integer-only exact audit of all lattice centers in nK.
const assert = require('node:assert/strict');
const facets = [
  [[-1,-1,-1],-2], [[-1,-1,1],-2], [[-1,1,-1],-2], [[-1,1,1],-2],
  [[1,-1,-1],-2], [[1,-1,1],-4], [[1,1,-1],-4], [[1,1,1],-2]
];
const vertices = [
  [-2,-1,1],[-2,1,-1],[-1,-2,1],[-1,-1,2],[-1,1,-2],[-1,2,-1],
  [0,-2,0],[0,0,-2],[0,0,2],[0,2,0],[2,0,0]
];
function dot(a,b){return a.reduce((x,y,i)=>x+y*b[i],0);}
function inside(p,n=1){return facets.every(([a,b])=>dot(a,p)>=b*n);}
function count(n,strict=false){
  let total=0;
  for(let u=-4*n;u<=4*n;u++) for(let v=-4*n;v<=4*n;v++){
    const lo=Math.max(Math.abs(u+v)-2*n, Math.abs(u-v)-4*n);
    const hi=2*n-Math.abs(u)-Math.abs(v);
    for(let h=lo+(strict?1:0);h<=hi-(strict?1:0);h++){
      if(strict && !facets.every(([a,b])=>dot(a,[h,u,v])>b*n))continue;
      assert(inside([h,u,v],n));
      total++;
    }
  }
  return total;
}
// Exhaustive finite checks of all n=0..7; only n=0..3 used in the theorem
// via the standard degree-3 integral-polytope Ehrhart theorem.
const counts=Array.from({length:8},(_,n)=>count(n));
assert.deepEqual(counts,[1,33,179,531,1181,2221,3743,5839]);
for(let n=0;n<=7;n++) assert.equal(3*counts[n],46*n**3+33*n**2+17*n+3);
const interior=count(1,true);
assert.equal(interior,9);
assert.equal(vertices.length,11);
assert(vertices.every(p=>inside(p)));
for(const [a,b] of facets){
  const points=vertices.filter(p=>dot(a,p)===b);
  assert(points.length>=3);
}
const hstar=[1,counts[1]-4,counts[2]-4*counts[1]+6,interior];
assert.deepEqual(hstar,[1,29,53,9]);
assert.equal(hstar.reduce((x,y)=>x+y,0),92);
const result={status:'PASS',unit:'R749SPS',model:'auxiliary Walsh 16-atom source fiber',
  frozen_pin:'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
  predecessor:'R749SPR: 8 facets / 11 integer vertices / rho_cal=9/20',
  count_formula:'L_K(n)=(46*n^3+33*n^2+17*n+3)/3 for integer n>=0',
  input_counts_n0_to_3:counts.slice(0,4),extra_audit_counts_n4_to_7:counts.slice(4),
  h_star:hstar,normalized_volume:92,euclidean_volume:'46/3',
  boundary_n1:counts[1]-interior,interior_n1:interior,
  status_of_prior_theorem:'AUTHOR_EXACT_NOT_REVIEWED',
  verification:'Integer loops exact; Ehrhart-degree theorem applies because prior 11 vertices integral and full dimension.'};
console.log(JSON.stringify(result,null,2));
