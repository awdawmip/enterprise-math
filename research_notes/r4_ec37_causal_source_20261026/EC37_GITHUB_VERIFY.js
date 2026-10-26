/* EC37 independent BigInt check for finite positive-source label kernels.
 * This is an auxiliary BRC observer certificate, NOT native X6 dynamics.
 * Execute: node EC37_GITHUB_VERIFY.js
 */
function assert(ok, message) { if (!ok) throw Error(message); }
function histogram(K, start, n) {
  let d = new Map([[JSON.stringify([start, '']), 1n]]);
  for (let t=0; t<n; t++) {
    const next=new Map();
    for (const [key, mult] of d) {
      const [state, word]=JSON.parse(key);
      for (const [label, successor, weight] of K[state]) {
        const k=JSON.stringify([successor, word+label]);
        next.set(k,(next.get(k)||0n)+mult*BigInt(weight));
      }
    }
    d=next;
  }
  const result=new Map();
  for (const [key, val] of d) {
    const word=JSON.parse(key)[1];
    result.set(word,(result.get(word)||0n)+val);
  }
  return result;
}
function l1(a,b) {
  const keys=new Set([...a.keys(),...b.keys()]);
  let sum=0n;
  for (const k of keys) {
    const x=a.get(k)||0n, y=b.get(k)||0n;
    sum += x>=y ? x-y : y-x;
  }
  return sum;
}
function labelsAndStates(row) {
  const L={},S={};
  for (const [lab,state,w] of row) {
    L[lab]=(L[lab]||0)+w;
    S[state]=(S[state]||0)+w;
  }
  return JSON.stringify([Object.entries(L).sort(),Object.entries(S).sort()]);
}
function verify() {
  const checks={sharp_cases:0,sharp_depths:0,correlation_depths:0,random_pairs:0,random_tv_bounds:0,strict_inequalities:0};
  for (let M=2;M<=8;M++) for (let a=1;a<=M;a++) {
    const T={s:[['R','s',M]]}, Q={s:[['B','s',a]]};
    if(M>a) Q.s.push(['R','s',M-a]);
    for(let n=0;n<=10;n++) {
      const x=histogram(T,'s',n), y=histogram(Q,'s',n);
      assert(l1(x,y)===2n*(BigInt(M)**BigInt(n)-BigInt(M-a)**BigInt(n)), 'sharp exact L1');
      checks.sharp_depths++;
    }
    checks.sharp_cases++;
  }
  const stable={U:[['R','U',2]],V:[['B','V',2]]};
  const A={O:[['R','U',1],['B','V',1]], ...stable};
  const B={O:[['R','V',1],['B','U',1]], ...stable};
  assert(labelsAndStates(A.O)===labelsAndStates(B.O),'one-step marginals');
  for(let n=0;n<=8;n++) {
    const x=histogram(A,'O',n), y=histogram(B,'O',n);
    const expect=n<=1?0n:2n*(2n**BigInt(n));
    assert(l1(x,y)===expect,'two-step joint-correlation no-go');
    checks.correlation_depths++;
  }
  let seed=3701;
  function rnd(k) {seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;seed>>>=0;return seed%k;}
  const events=[['R','0'],['R','1'],['B','0'],['B','1']];
  function kernel() {
    const K={};
    for(const state of ['0','1']) {
      const w=new Array(4).fill(0);
      for(let j=0;j<6;j++)w[rnd(4)]++;
      K[state]=w.flatMap((v,i)=>v?[[...events[i],v]]:[]);
    }
    return K;
  }
  function overlapCount(a,b,state) {
    const key=(r)=>r[0]+':'+r[1];
    const v=new Map(a[state].map(r=>[key(r),r[2]]));
    return b[state].reduce((sum,r)=>sum+Math.min(v.get(key(r))||0,r[2]),0);
  }
  for(let j=0;j<140;j++) {
    const A=kernel(), B=kernel();
    const k=Math.min(overlapCount(A,B,'0'),overlapCount(A,B,'1'));
    for(let n=1;n<=7;n++) {
      const dist=l1(histogram(A,'0',n),histogram(B,'0',n));
      const bound=2n*(6n**BigInt(n)-BigInt(k)**BigInt(n));
      assert(dist<=bound,'exact product coupling bound');
      checks.random_tv_bounds++;
      if(dist<bound)checks.strict_inequalities++;
    }
    checks.random_pairs++;
  }
  return {schema:'EM_R4_EC37_GITHUB_BIGINT_VERIFY_V1',status:'PASS',
    scope:'auxiliary finite constant-M positive-source BRC kernels',
    method:'exact BigInt word counts, source-label correlations, diagonal relation overlap',
    checks, native_X6_verified:false, independent_Driver_review:false};
}
console.log(JSON.stringify(verify(),null,2));
