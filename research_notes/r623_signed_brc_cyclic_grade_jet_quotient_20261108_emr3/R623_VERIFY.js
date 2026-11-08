#!/usr/bin/env node
"use strict";
/* R623 frozen signed BRC exact verifier. Node.js BigInt; no external dependencies.
 * Source: R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f,
 * K blob 7fa7a762f758b30c6090468ac43487daa34abad8.
 * Usage: node R623_VERIFY.js > R623_EVIDENCE.json
 */
function verifyR623() {
  "use strict";
  const assert = (condition, message) => { if (!condition) throw new Error(message); };
  const C = (n, k) => {
    if (k < 0 || k > n) return 0;
    let a = 1;
    for (let j = 1; j <= k; j++) a = a * (n - j + 1) / j;
    return Math.round(a);
  };
  const gcd = (a, b) => { while (b) [a, b] = [b, a % b]; return a; };
  const factorial = n => { let v = 1; for (let j = 2; j <= n; j++) v *= j; return v; };
  const frozenK = i => {
    const ds = [-C(4, i) + C(2, i - 1),
      C(5, i - 1) - C(5, i - 2),
      C(7, i - 2), -C(9, i - 3)];
    const a = Array(i + 12).fill(0n);
    for (let r = 1; r <= 4; r++) {
      const n = i + 1 - r;
      if (n < 0) continue;
      for (let j = 0; j <= n; j++)
        a[i - 1 + j] -= BigInt(ds[r - 1] * C(n, j));
    }
    while (a.length > 1 && a[a.length - 1] === 0n) a.pop();
    return a;
  };
  const K = Array.from({length:12}, (_,i) => frozenK(i + 1));
  const lead = K.map(k => k.find(x => x !== 0n)?.toString());
  assert(lead.join(",") === "2,-1,-8,-11,6,53,106,119,83,36,9,1", "Frozen K lead coefficients mismatch");
  const order = K.map(k => k.findIndex(x=>x!==0n));
  assert(order.every((v,i) => v===i), "Frozen BRC valuations mismatch");
  assert(K[0].join(",")==="2,3" && K[1].join(",")==="0,-1,4,4", "K1/K2 frozen examples mismatch");
  const perms = [];
  const permute = (prefix, remaining) => {
    if (!remaining.length) { perms.push(prefix); return; }
    for (let j=0; j<remaining.length; j++)
      permute(prefix.concat(remaining[j]), remaining.filter((_,i)=>i!==j));
  };
  permute([], [0,1,2,3,4,5]);
  assert(perms.length===720, "S6 enumeration error");
  const jet = (p,d) => Array.from({length:d+1},(_,k)=> (p[k]??0n).toString()).join(",");
  const polyProductJet = (p,q,d) => {
    const out=Array(d+1).fill(0n);
    for(let a=0;a<=d;a++)for(let b=0;b<=d-a;b++)
      out[a]+=(p[a]??0n)*(q[b]??0n);
    return out.map(x=>x.toString()).join(",");
  };
  const rows=[];
  let orbitComparisons=0;
  let distinctClassSum=0;
  let twoStepChecks=0;
  let matchedFiberWitnesses=0;
  const witnessPairs = new Set(["0/1","0/2","0/3","0/4","0/5","2/3","2/4","4/3","4/4","6/3","8/1"]);
  for(let d=0;d<=11;d++){
    for(let m=1;m<=20;m++){
      const profiles=Array.from({length:6},(_,j)=>
        `${jet(K[2*j],d)};${jet(K[2*j+1],d)};${(2*j+1)%m};${(2*j+2)%m}`);
      const seen=new Map();
      let pair=null;
      for(const p of perms){
        const label=p.map(j=>profiles[j]).join("|");
        const first=seen.get(label);
        if(first===undefined) seen.set(label,p);
        else if(pair===null) pair=[first,p];
      }
      const k=Math.min(6,Math.floor(d/2)+1);
      const L=m/gcd(m,2);
      const multiplicities=Array.from({length:L},(_,r)=>
        Array.from({length:6-k},(_,a)=>a+k+1).filter(j=>j%L===r).length);
      const denom=multiplicities.reduce((a,v)=>a*factorial(v),1);
      const expected=720/denom;
      assert(Number.isInteger(expected)&&expected===seen.size,
        `orbit failure at d=${d},m=${m}, got=${seen.size}, expected=${expected}`);
      assert((seen.size===720)===(L>=6-k), `full resolution threshold at d=${d},m=${m}`);
      orbitComparisons+=perms.length;
      distinctClassSum+=seen.size;
      if(witnessPairs.has(`${d}/${m}`) && pair!==null){
        matchedFiberWitnesses++;
        for(let ax=0;ax<6;ax++)for(let sx=0;sx<2;sx++)
          for(let bx=0;bx<6;bx++)for(let sb=0;sb<2;sb++){
            const qA=2*pair[0][ax]+1+sx, qB=2*pair[0][bx]+1+sb;
            const qC=2*pair[1][ax]+1+sx, qD=2*pair[1][bx]+1+sb;
            assert((qA+qB)%m===(qC+qD)%m, "two-step cyclic grade not preserved");
            assert(polyProductJet(K[qA-1],K[qB-1],d)===
                   polyProductJet(K[qC-1],K[qD-1],d), "two-step signed jet not preserved");
            twoStepChecks++;
          }
      }
      rows.push({d,m,k,L,stabilizer:denom,orbit:seen.size,bits:Math.ceil(Math.log2(seen.size)),
                 full_orientation:seen.size===720});
    }
  }
  const read=(d,m)=>rows.find(r=>r.d===d&&r.m===m).orbit;
  assert(read(0,3)===180 && read(0,4)===60 && read(0,5)===720,
    "non-monotone grade-modulus witness failed");
  assert(read(2,1)===30 && read(2,3)===360 && read(4,3)===720 && read(6,4)===720,
    "jet/grade cross-checks failed");
  for(let d=0;d<=11;d++){
    for(let a=1;a<=20;a++)for(let b=a+1;b<=20;b++)
      if(b%a===0)
        assert(read(d,b)>=read(d,a), "divisibility refinement failed");
  }
  return {
    schema:"EM_R623_SIGNED_BRC_CYCLIC_GRADE_JET_ORBIT_EVIDENCE_V1",
    status:"AUTHOR_SIDE_EXACT_FINITE_CHECK",
    science:{commit:"18783e01e3646c72b7aab3b16d3f565e83e6446f",
      original_K_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",
      theta:"0",branch_count:12,orders:order,leading_coefficients:lead},
    model:"Formal S6 orientation; exact signed K coefficient jets degree d and step grade increments modulo m",
    coverage:{jet_degrees:"0..11",grade_moduli:"1..20",orientations:720,
      observer_pairs:rows.length,orientation_profile_evaluations:orbitComparisons,
      distinct_profile_classes_sum:distinctClassSum,representative_two_step_checks:twoStepChecks,
      nontrivial_fiber_cases_checked:matchedFiberWitnesses},
    formula:"N(d,m)=720/prod_r multiplicity({j>k_d:j modulo (m/gcd(m,2))=r})!, k_d=min(6,floor(d/2)+1)",
    validation:"R623_CYCLIC_GRADE_JET_QUOTIENT_EXACT_PASS",
    special:{d0_m1:read(0,1),d0_m3:read(0,3),d0_m4:read(0,4),
      d0_m5:read(0,5),d2_m3:read(2,3),d4_m3:read(4,3),
      d6_m4:read(6,4),d8_m1:read(8,1)},
    rows
  };
}
process.stdout.write(JSON.stringify(verifyR623(),null,2)+"\n");
