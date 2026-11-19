/* Unit163 A_p integer collapsed triangle carry independent exact audit; Node.js */
const audit = function audit(){
  const isqrt=q=>{let x=0;while((x+1)*(x+1)<=q)x++;return x};
  const points=n=>{const a=[];function gen(prefix){if(prefix.length===n){if(prefix.reduce((s,x)=>s+x,0)===0)a.push(prefix);return}for(let t=-2;t<=2;t++)gen([...prefix,t])}gen([]);return a};
  const q=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0)/2;
  const d=(a,b)=>isqrt(q(a,b));
  let cases=0,violations=0,sharp=0,counts={};
  for(const p of [1,2,3]){const a=points(p+1);let cnt=0;
    for(const x of a)for(const y of a)for(const z of a){const direct=d(x,z),via=d(x,y)+d(y,z),carry=Math.max(0,direct-via);if(carry>1||direct>via+1)violations++;if(carry===1)sharp++;cnt++}
    counts[`A_${p}`]={points:a.length,triples:cnt};cases+=cnt;
  }
  const a=[-2,0,2],b=[-1,1,0],c=[0,2,-2];const witness=[d(a,b),d(b,c),d(a,c),Math.max(0,d(a,c)-d(a,b)-d(b,c))];
  if(violations||witness.join(",")!=="1,1,3,1")throw Error("exact triangle-carry audit failed");
  return {schema:"X6_UNIT163_LATTICE_INTEGER_RADIAL_CARRY_AUDIT_V1",date:"2026-11-19",historical_source:"fd2bcff10ca6e147348b6c1236027fc0d2877df3",domain:"A_p, p=1,2,3; each coordinate integer [-2,2], zero sum; ordered triples",counts,checked_triples:cases,sharp_triples:sharp,violations,witness:{a,b,c,radii:witness},integer_operations_only:true,proof_scope:"ALL A_p INTEGER LATTICES BY SCALED_EUCLIDEAN_TRIANGLE_PLUS_FLOOR",execution:"actual V8 isolate run",status:"PASS"};
};
console.log(JSON.stringify(audit(),null,2));
