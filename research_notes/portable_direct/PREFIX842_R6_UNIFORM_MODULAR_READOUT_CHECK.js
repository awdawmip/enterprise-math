'use strict';
// PREFIX-842 exact modular observer with a uniformly bounded mass register.
function assert(b,s){if(!b)throw Error(s);}
function gcd(a,b){while(b){let t=a%b;a=b;b=t;}return a;}
function primes(n){let p=[];for(let d=2n;d*d<=n;d++){if(n%d===0n){p.push(d);while(n%d===0n)n/=d;}}if(n>1n)p.push(n);return p;}
function radical(n){return primes(n).reduce((a,p)=>a*p,1n);}
function freePart(m,ps){let x=m;for(const p of ps)while(x%p===0n)x/=p;return x;}
function c(t,a,b){return a**BigInt(Math.floor(t/2))*b**BigInt(Math.floor((t-1)/2));}
function leastCoprime(N,C){let m=N;while(gcd(m,C)!==1n)m++;return m;}
const stats={parameterFamilies:0,finiteHorizons:0,finiteMinimumCandidates:0,uniformModuli:0,saturationChecks:0,fullResidueComparisons:0,modularDynamicConfigurations:0,modularDynamicFrames:0,modularWeightDecodes:0};
const examples=[];
for(let p=1;p<=4;p++)for(let W=2;W<=4;W++)for(let an=1;an<=4;an++)for(let bn=1;bn<=4;bn++){
  const N=BigInt(W)**BigInt(p),a=BigInt(an),b=BigInt(bn),C=a*b,ps=primes(C),rad=radical(C),star=leastCoprime(N,C);
  stats.parameterFamilies++;
  assert(star>=N&&star<=N+rad-1n,'radical candidate upper bound');
  assert(gcd(star,C)===1n,'minimum coprime');
  for(let m=N;m<star;m++){assert(gcd(m,C)!==1n,'coprime minimum');}
  let prev=0n;
  for(let T=1;T<=12;T++){
    const ct=c(T,a,b);let candidate=1n;
    while(candidate/gcd(candidate,ct)<N){candidate++;stats.finiteMinimumCandidates++;}
    assert(candidate<=star,'finite cannot exceed uniform');
    assert(candidate>=prev,'finite minimum monotonic');
    prev=candidate;stats.finiteHorizons++;
    if(p===2&&W===2&&an===2&&bn===1)examples.push({p,W,a:an,b:bn,T,leastModulus:candidate.toString()});
    if(p===2&&W===3&&an===2&&bn===3)examples.push({p,W,a:an,b:bn,T,leastModulus:candidate.toString()});
  }
  const late=c(100,a,b);
  for(let m=1n;m<=star+7n;m++){
    const good=freePart(m,ps);
    assert(m/gcd(m,late)===good,'primary-part saturation by time 100');
    const uniform=good>=N;
    assert(uniform===(m/gcd(m,late)>=N),'uniform criterion');
    if(m<star)assert(!uniform,'no smaller universally injective modulus');
    stats.uniformModuli++;stats.saturationChecks++;
  }
  if(p<=2&&W<=3&&an<=3&&bn<=3){
    for(let T=1;T<=5;T++){
      const ct=c(T,a,b);for(let m=1n;m<=star+3n;m++){
        let values=new Set(),unique=true;const S=(N-1n)/BigInt(W-1);
        for(let u=0n;u<N;u++){
          const v=(ct*(S+u))%m, key=v.toString();stats.fullResidueComparisons++;
          if(values.has(key)){unique=false;break;}values.add(key);
        }
        assert(unique===(m/gcd(m,ct)>=N),'full residue observer iff');
      }
    }
  }
}
function popcount(mask){let n=0;while(mask){mask&=mask-1;n++;}return n;}
function invMod(n,m){let [r,rr]=[m,((n%m)+m)%m],[s,ss]=[0n,1n];while(rr){const q=r/rr;[r,rr]=[rr,r-q*rr];[s,ss]=[ss,s-q*ss];}assert(r===1n,'inverse only for units');return ((s%m)+m)%m;}
for(let p=1;p<=3;p++)for(let W=2;W<=3;W++)for(let wcode=0;wcode<W**p;wcode++)for(let an=1;an<=3;an++)for(let bn=1;bn<=3;bn++){
  const a=BigInt(an),b=BigInt(bn),N=BigInt(W)**BigInt(p),m=leastCoprime(N,a*b);
  const w=[];let x=wcode;for(let i=0;i<p;i++){w.push(BigInt(1+x%W));x=Math.floor(x/W);}
  const all=(1<<p)-1;let state=new Map([[all*2,1n]]);
  let sum=0n,ordinal=0n,pow=1n;for(let i=0;i<p;i++){sum+=pow;ordinal+=pow*(w[i]-1n);pow*=BigInt(W);}
  stats.modularDynamicConfigurations++;
  for(let t=1;t<=6;t++){
    const next=new Map();
    function add(k,weight,mass){next.set(k,((next.get(k)||0n)+weight*mass)%m);}
    for(const [key,mass] of state){
      const mask=Math.floor(key/2),marked=key&1,occ=popcount(mask)+marked;
      for(let i=0;i<p;i++)if(mask&(1<<i))add((mask^(1<<i))*2+marked,w[i],mass);
      if(marked)add(mask*2,b,mass);
      if(!marked&&occ<p)add(mask*2+1,a,mass);
    }
    state=next;
    const marker=t%2===0?1:0;
    let z=0n,power=1n;
    for(let i=0;i<p;i++){
      const D=state.get((all^(1<<i))*2+marker)||0n;
      z=(z+power*D)%m;power*=BigInt(W);
    }
    const ct=c(t,a,b),inverse=invMod(ct,m);
    const decoded=((z*inverse-sum)%m+m)%m;
    assert(decoded===ordinal,'complete modular DP exact named readout');
    let cur=decoded;
    for(let i=0;i<p;i++){assert(cur%BigInt(W)===w[i]-1n,'uniform readout digit');cur/=BigInt(W);stats.modularWeightDecodes++;}
    assert(cur===0n,'uniform digits exhausted');
    stats.modularDynamicFrames++;
  }
}
const result={schema:'PREFIX842_UNIFORM_MODULAR_PROVENANCE_V1',frozen_scientific_input:'f42f2906d77f24085c123f3ccfe9667d41caa96d',
  theorems:['For all t>=1, Z_W(t) mod m is label-injective iff the factor of m coprime to ab is >=W^p.',
    'The least uniform modulus is min{m>=W^p:gcd(m,ab)=1}, at most W^p+rad(ab)-1.',
    'For finite 1<=t<=T, injectivity iff m/gcd(m,c_T)>=W^p; finite optimum is nondecreasing and stabilizes at the least uniform modulus.'],
  checked:{p:[1,4],W:[2,4],a:[1,4],b:[1,4],horizons:[1,12],late_saturation_t:100,stats,result:'ALL_EXACT_ASSERTIONS_PASSED'},
  examples};
if(typeof console!=='undefined')console.log(JSON.stringify(result,null,2));
JSON.stringify(result,null,2);
