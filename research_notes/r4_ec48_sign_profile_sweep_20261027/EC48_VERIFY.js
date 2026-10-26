"use strict";
// EM EC48: independent exact-integer sign-profile sweep and brute-force verification.
// Run: node EC48_VERIFY.js
const report = (function runAudit() {
  const check=(ok,label)=>{if(!ok)throw new Error("FAIL "+label);};
  const sum=(a)=>a.reduce((s,v)=>s+BigInt(v),0n);
  const cmp=(a,b)=>a.n*b.d<b.n*a.d?-1:a.n*b.d>b.n*a.d?1:0;
  function instantiate(H,Y,p,q) {
    check(p.length===H*Y && q.length===H*Y && p.every(x=>Number.isInteger(x)&&x>0) && q.every(x=>Number.isInteger(x)&&x>0),"positive finite input");
    const P=sum(p),Q=sum(q);
    const cells=p.map((v,i)=>({h:Math.floor(i/Y),y:i%Y,n:BigInt(v)*Q,d:BigInt(q[i])*P}));
    const sorted=[...cells].sort(cmp),groups=[];
    for(const c of sorted) {
      if(!groups.length||cmp(groups[groups.length-1],c)!==0) groups.push({n:c.n,d:c.d,cells:[c]});
      else groups[groups.length-1].cells.push(c);
    }
    return {H,Y,p,q,P,Q,cells,groups};
  }
  function thresholdD(m,i,t) {return m.cells[i].n*t.d-m.cells[i].d*t.n;}
  function rowsAt(m,t) {
    const masks=[];
    for(let h=0;h<m.H;h++){
      let v=0n;
      for(let y=0;y<m.Y;y++){
        const d=thresholdD(m,h*m.Y+y,t);
        check(d!==0n,"strict interval incorrectly sampled");
        if(d>0n)v|=1n<<BigInt(y);
      }
      masks.push(v);
    }
    return masks;
  }
  function sweep(m){
    let masks=Array(m.H).fill((1n<<BigInt(m.Y))-1n);
    const freq=new Map([[masks[0],m.H]]), intervals=[1];
    for(const g of m.groups){
      const changes=new Map();
      for(const c of g.cells)changes.set(c.h,(changes.get(c.h)||0n)^(1n<<BigInt(c.y)));
      for(const [h,xor] of changes){
        const old=masks[h], count=freq.get(old);
        check(count>0,"negative signature frequency");
        if(count===1)freq.delete(old); else freq.set(old,count-1);
        const next=old^xor; masks[h]=next;freq.set(next,(freq.get(next)||0)+1);
      }
      intervals.push(freq.size);
    }
    check(masks.every(x=>x===0n)&&freq.size===1,"end state empty");
    return {intervals,peak:Math.max(...intervals)};
  }
  function sampleInterval(m,j){
    const a=j===0?{n:0n,d:1n}:m.groups[j-1];
    if(j===m.groups.length)return {n:a.n+a.d,d:a.d};
    const b=m.groups[j];
    return {n:a.n*b.d+b.n*a.d,d:2n*a.d*b.d};
  }
  function chromaticAt(m,t){
    const adj=Array.from({length:m.H},()=>[]);
    for(let h=0;h<m.H;h++)for(let k=h+1;k<m.H;k++){
      let bad=false;
      for(let y=0;y<m.Y;y++) {
        if(thresholdD(m,h*m.Y+y,t)*thresholdD(m,k*m.Y+y,t)<0n){bad=true;break;}
      }
      if(bad){adj[h].push(k);adj[k].push(h);}
    }
    function feasible(K){
      const color=Array(m.H).fill(-1);
      function walk(i){
        if(i===m.H)return true;
        for(let c=0;c<K;c++){
          if(adj[i].some(k=>k<i&&color[k]===c))continue;
          color[i]=c;
          if(walk(i+1))return true;
        }
        color[i]=-1;return false;
      }
      return walk(0);
    }
    for(let k=1;k<=m.H;k++)if(feasible(k))return k;
    throw new Error("graph cannot color");
  }
  function optNumerator(m,t,K){
    const coeff=m.cells.map((_,i)=>thresholdD(m,i,t));
    let full=0n;
    for(const d of coeff)if(d>0n)full+=d;
    let best=null;
    const assignment=Array(m.H).fill(0);
    function walk(i){
      if(i<m.H) {for(let c=0;c<K;c++){assignment[i]=c;walk(i+1)}return;}
      const buckets=Array(K*m.Y).fill(0n);
      for(let h=0;h<m.H;h++)for(let y=0;y<m.Y;y++){
        buckets[assignment[h]*m.Y+y]+=coeff[h*m.Y+y];
      }
      let val=0n;
      for(const d of buckets)if(d>0n)val+=d;
      if(best===null||val>best)best=val;
    }
    walk(0);
    return {full,best,den:m.P*m.Q*t.d};
  }
  let seed=0xC0FFEE27>>>0;
  const rnd=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed;};
  const cases=[];
  for(let H=2;H<=4;H++)for(let Y=1;Y<=3;Y++)for(let rep=0;rep<12;rep++){
    const N=H*Y,p=Array.from({length:N},()=>1+(rnd()%9));
    const shift=1+(rnd()%(N-1)),q=p.map((_,i)=>p[(i+shift)%N]);
    cases.push({H,Y,p,q});
  }
  const positive4={H:4,Y:2,p:[4,4,4,1,1,4,1,1],q:Array(8).fill(1)};
  const positive3={H:3,Y:2,p:[3,3,3,1,1,1],q:Array(6).fill(2)};
  cases.push(positive4,positive3);
  let intervalCases=0,tieCases=0,bruteChecks=0,tieChromaticChecks=0,maxPeak=0;
  for(const [idx,input] of cases.entries()){
    const m=instantiate(input.H,input.Y,input.p,input.q), sw=sweep(m);
    maxPeak=Math.max(maxPeak,sw.peak);
    for(let j=0;j<=m.groups.length;j++){
      const t=sampleInterval(m,j),n=new Set(rowsAt(m,t)).size;
      check(n===sw.intervals[j],"profile count vs sweep case "+idx+" interval "+j);
      const yes=optNumerator(m,t,n);
      check(yes.best===yes.full,"profile colors sufficient case "+idx+" interval "+j);
      bruteChecks++;
      if(n>1){
        const no=optNumerator(m,t,n-1);
        check(no.best<no.full,"fewer memory states impossible case "+idx+" interval "+j);
        bruteChecks++;
      }
      intervalCases++;
    }
    for(let j=0;j<m.groups.length;j++){
      const t=m.groups[j],chi=chromaticAt(m,t);
      check(chi<=Math.min(sw.intervals[j],sw.intervals[j+1]),"tie cannot increase chromatic number");
      tieChromaticChecks++;
      const yes=optNumerator(m,t,chi);
      check(yes.best===yes.full,"tie graph sufficiency");
      bruteChecks++;
      if(chi>1){
        const no=optNumerator(m,t,chi-1);
        check(no.best<no.full,"tie graph minimality");
        bruteChecks++;
      }
      tieCases++;
    }
  }
  const four=instantiate(positive4.H,positive4.Y,positive4.p,positive4.q);
  const one={n:1n,d:1n}, full4=optNumerator(four,one,4),part3=optNumerator(four,one,3),
        part2=optNumerator(four,one,2),part1=optNumerator(four,one,1);
  check(full4.full===48n&&full4.den===160n&&part3.best===36n&&part2.best===24n&&part1.best===0n,"explicit four-pattern witness");
  check(sweep(four).intervals.join(",")==="1,4,1","4-pattern trace");
  check(sweep(instantiate(positive3.H,positive3.Y,positive3.p,positive3.q)).intervals.join(",")==="1,3,1","3-pattern trace");
  return {
    schema:"EM_EC48_SIGN_PROFILE_SWEEP_AUDIT_V1",
    status:"PASS",
    input_kind:"finite strictly positive integer joint source counts, independently normalized under P and Q",
    algorithm:"sort exact rational likelihood ratios; update grouped sign-bitset histories; compare generic sweep with direct sign rows and complete deterministic encoder/decoder optimization",
    seed:"0xC0FFEE27",
    generated_cases:108,
    worked_cases:2,
    total_cases:cases.length,
    generic_interval_cases:intervalCases,
    ratio_tie_cases:tieCases,
    exact_bruteforce_optimization_checks:bruteChecks,
    exact_tie_chromatic_checks:tieChromaticChecks,
    largest_peak_memory:maxPeak,
    four_profile_example:{
      P_joint_integer_counts:positive4.p,
      Q_joint_integer_counts:positive4.q,
      total_P:"20",total_Q:"8",
      sorted_thresholds:["2/5","8/5"],
      generic_profile_counts:[1,4,1],
      lambda:"1",
      full_support_numerator:"48",
      shared_denominator:"160",
      optimal_K_1_numerator:part1.best.toString(),
      optimal_K_2_numerator:part2.best.toString(),
      optimal_K_3_numerator:part3.best.toString(),
      optimal_K_4_numerator:full4.best.toString(),
      K3_loss_fraction:"3/40"
    },
    three_profile_example:{P_joint_integer_counts:positive3.p,Q_joint_integer_counts:positive3.q,profile_counts:[1,3,1]},
    verification_scope:"finite generated inputs and worked examples; universal theorem supplied by mathematical proof, not inferred from enumeration",
    exclusions:["seedless behavioral S_K=Z not decided by this audit","four-coordinate variable-depth stopping not modeled","native P000/X6 dynamics not modeled","no CAD/QE or independent Driver review executed"]
  };
})();
if (typeof console !== 'undefined') console.log(JSON.stringify(report,null,2));
