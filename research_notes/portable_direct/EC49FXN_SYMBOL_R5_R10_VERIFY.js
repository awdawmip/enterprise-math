'use strict';
// EC49FXN exact integer verifier; frozen BRC16943 auxiliary Farey-CRT two-channel observer.
// Usage: node EC49FXN_SYMBOL_R5_R10_VERIFY.js [output.json]
// Distances are whole-activation SYMBOL distances, not separate channel-bit distances.
const fs = require('node:fs');
const assert = require('node:assert/strict');
const mod = (a,n) => ((a%n)+n)%n;
const witness = {
  5: {
    2: [59,65,68,69,70,71,73,74,82,85,89,90,93,98,99,105,108],
    4: [58,60,61,69,70,73,75,76,79,81,85,86,88,89,90,93,102,103,104,106,109]
  },
  6: {
    2: [56,58,59,63,64,65,68,69,78,80,84,85,89,90,92,93,94,100,105,108],
    4: [58,59,60,63,64,65,67,69,70,73,76,78,80,81,85,86,88,91,94,95,96,103,104,106,109]
  }
};
function safeResidues(i,k) {
  return Array.from({length:55},(_,x)=>x)
    .filter(x=>x%5===i && (2*x)%55>=k);
}
function claimed(r,k) {
  if (k<5) {
    assert.ok(r===5 || r===6);
    return k<=2?3*r+2:4*r+1;
  }
  return 5*r+Math.max(0,Math.min(5,k-55+5*Math.ceil(r/2)));
}
function sites(r,k) {
  if (k<5) return witness[r][k<=2?2:4].slice();
  const S=[], h=Math.ceil(r/2);
  for(let i=0;i<5;i++) {
    const safe=safeResidues(i,k);
    if(safe.length>=h) {
      for(let z=0;z<r;z++) {
        const x=safe[Math.floor(z/2)];
        S.push(x+(z%2)*55);
      }
    } else {
      for(let z=0;z<=r;z++) S.push(i+5*z);
    }
  }
  return S.sort((a,b)=>a-b);
}
function symbolDifference(S,d,i,j) {
  let v=0;
  for(const t of S) {
    const left=t%5===i && t%11!==j;
    const right=mod(d-t,5)===i && mod(d-t,11)!==j;
    if(left||right) v++;
  }
  return v;
}
const profiles=[];
let count=0;
for(let r=4;r<=10;r++) {
  const results=[];
  for(let k=1;k<=55;k++) {
    if(k<5 && r!==5 && r!==6) continue;
    const S=sites(r,k);
    assert.equal(S.length,claimed(r,k));
    assert.equal(new Set(S).size,S.length);
    assert.ok(S.every(t=>Number.isInteger(t) && t>=0 && t<110));
    let min=Infinity;
    for(let d=0;d<k;d++)
      for(let i=0;i<5;i++)
        for(let j=0;j<11;j++) {
          const value=symbolDifference(S,d,i,j);
          assert.ok(value>=r,'row failed r='+r+', k='+k+', d='+d+', i='+i+', j='+j);
          min=Math.min(min,value);
          count++;
        }
    assert.equal(min,r);
    const heavy=[0,1,2,3,4].filter(i=>safeResidues(i,k).length<Math.ceil(r/2)).length;
    if(k>=5) assert.equal(S.length,5*r+heavy);
    results.push({k,n:S.length,min_distance:min});
  }
  profiles.push({r,k_range:[results[0].k,55],results});
}
assert.equal(count,590150);
const out={
  schema:'EC49FXN_EXACT_INTEGER_VERIFY_V1',
  scientific_input:'BRC16943',
  model:'Farey-CRT auxiliary 110-cycle, two Boolean channels per physical activation',
  general_theorem:'4<=r<=10, 5<=k<=55: N=5*r+min(5,max(0,k-55+5*ceil(r/2)))',
  small_k_theorem:'r=5,6: N=3*r+2 for k=1,2; N=4*r+1 for k=3,4',
  exactly_checked_rows:count,failed_rows:0,
  small_k_witnesses:witness,profiles
};
const json=JSON.stringify(out,null,2)+'\n';
if(process.argv[2]) fs.writeFileSync(process.argv[2],json,'utf8');
else process.stdout.write(json);
console.error('PASS: '+count+' exact integer rows, 0 failures');
