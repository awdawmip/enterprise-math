'use strict';
// R305: exact BigInt signed defect-series recurrence versus independent six-edge origin DP.
function verify() {
  const MAX_N = 240, MAX_D = 44;
  const dTerms = [[0,0,1],[1,0,-1],[1,1,-1],[2,1,1],[3,1,-1],
    [3,2,-1],[4,2,2],[6,3,1],[8,4,-1]];
  const nTerms = [[3,0,1],[4,0,-1],[4,1,-1],[5,1,1],[6,2,-1],[8,3,1]];
  const q = new Map(nTerms.map(([n,d,c]) => [`${n},${d}`, BigInt(c)]));
  const diffs = Array.from({length:MAX_N+1}, () => Array(MAX_D+1).fill(0n));
  let series_coefficients = 0;
  for (let n=0;n<=MAX_N;n++) {
    for (let d=0;d<=MAX_D;d++) {
      let v = q.get(`${n},${d}`) || 0n;
      for (const [a,b,c] of dTerms) {
        if (a===0 && b===0) continue;
        if (n>=a && d>=b) v-=BigInt(c)*diffs[n-a][d-b];
      }
      diffs[n][d]=v; series_coefficients++;
    }
  }
  // Independent DP retains state, full affine sign/translation, and forbidden-00 provenance.
  const edges=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
  let dp=new Map([['0,1,0,2',1n]]);
  let direct_checks=0, seen_effects=0;
  for (let n=0;n<=MAX_N;n++) {
    const plus=new Map(),minus=new Map();
    for (const [key,count] of dp.entries()) {
      const [state,epsilon,k] = key.split(',').map(Number);
      if(state!==0 || n===0) continue;
      const twice=n+k-2;
      if(twice<0 || twice%2!==0) continue;
      const d=twice/2;
      const dest=epsilon===1?plus:minus;
      dest.set(d,(dest.get(d)||0n)+count);
      seen_effects++;
    }
    for(let d=0;d<=MAX_D;d++) {
      const actual=(plus.get(d)||0n)-(minus.get(d)||0n);
      if(actual!==diffs[n][d]) throw Error(`rational/DP mismatch: n=${n},d=${d}`);
      direct_checks++;
    }
    const next=new Map();
    for(const [key,count] of dp.entries()) {
      const [state,epsilon,k,prev]=key.split(',').map(Number);
      for(let bit=0;bit<=1;bit++) {
        if(prev===0 && bit===0) continue;
        const [qn,eta,c]=edges[state][bit];
        const nextKey=`${qn},${eta*epsilon},${eta*k+c},${bit}`;
        next.set(nextKey,(next.get(nextKey)||0n)+count);
      }
    }
    dp=next;
  }
  function choose(n,k) {
    if(k<0 || k>n || n<0) return 0n;
    k=Math.min(k,n-k);
    let v=1n;
    for(let j=1;j<=k;j++) v=v*BigInt(n-k+j)/BigInt(j);
    return v;
  }
  let theorem_window_checks=0, finite_stronger_window_checks=0, bound_checks=0;
  let largest_positive_defect=0;
  for(let d=2;d<=MAX_D;d++) {
    for(let n=4*d+4;n<=MAX_N;n++) {
      const diff=diffs[n][d];
      if(diff<=0n) throw Error(`linear-wedge finite counterexample n=${n},d=${d},D=${diff}`);
      finite_stronger_window_checks++;
      if(n<8*d*d) continue;
      theorem_window_checks++; largest_positive_defect=Math.max(largest_positive_defect,d);
      const A=choose(n-2*d-4,d-1);
      let U=0n;
      for(let r=1;r<=d-1;r++) {
        for(let t=1;t<=Math.min(r,d-r);t++) {
          const p=d-r+1-t;
          U+=choose(d-r,t)*choose(r-1,t-1)*choose(n,p-1);
        }
      }
      if(!(A>U)) throw Error(`positive majorant fails n=${n},d=${d}`);
      bound_checks++;
    }
  }
  return {
    schema:'EM_R305_QUADRATIC_DEFECT_EXACT_EVIDENCE_V1', status:'PASS',
    mode:'BigInt exact integer arithmetic; rational bivariate series and independent six-edge DP',
    source_equation:'F(x,z)=x^3(1-x-xz+x^2z-x^3z^2+x^5z^3)/[(1+x^2z)(1-x-xz+2x^4z^2-x^6z^3)]',
    max_length:MAX_N,max_defect:MAX_D,
    checks:{series_coefficients,direct_checks,seen_effects,theorem_window_checks,
      finite_stronger_window_checks,bound_checks},
    strongest_finite_check:'D_d(n)>0 for 2<=d<=44, 4d+4<=n<=240 (not an infinite theorem)',
    proved_window:'For all integers d>=2 and n>=8d^2, D_d(n)>0 by separate exact combinatorial upper bound',
    max_defect_with_theorem_window_in_run:largest_positive_defect,
    physical_transfer:'NOT_ESTABLISHED',independent_driver_review:'NOT_PERFORMED'
  };
}
if (require.main === module) process.stdout.write(JSON.stringify(verify(), null, 2)+'\n');
module.exports={verify};
