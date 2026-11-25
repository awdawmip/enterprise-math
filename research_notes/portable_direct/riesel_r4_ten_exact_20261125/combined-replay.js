
const fixedPrimes = ["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const B=[0,3,5,8,10,15,21,23,26,28,30,31,33];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const weight=n=>{let w=0;for(let p=2;p<=n;p++)for(;n%p===0;n/=p)w+=p-1;return w;};
const h0=Array.from({length:1120},(_,i)=>i+1).filter(h=>weight(h/gcd(h,35))<=5);
const eligible=h0.filter(h=>h>=9&&h!==10);
const fixed=[[2,1],[3,1],[4,2]];
const rows=[0,1,2,3,5];
const bits=(mask,arr)=>arr.filter((_,i)=>(mask>>i)&1);
const assert=(test,message)=>{if(!test)throw Error(message);};
const surviving=new Map;
const branches=[];
for(let f=0;f<8;f++)for(let r=0;r<32;r++){
  const F=bits(f,fixed), R=bits(r,rows);
  const k=6-F.length-R.length;
  if(k<1)continue;
  const L=F.reduce((n,[m])=>lcm(n,m),35);
  const D=Array.from({length:L},(_,i)=>i).filter(x=>B.includes(x%35)&&!R.includes(x%7)&&!F.some(([m,b])=>x%m===b));
  if(D.length===0)continue;
  const candidate=new Map;
  for(const h of eligible){
    const g=gcd(h,L),m=h/g;
    if(weight(m)>k-1)continue;
    const incidence=Array(g).fill(0);
    for(const x of D)incidence[x%g]++;
    assert(1440%m===0,'mass scale');
    const mass=Math.max(...incidence)*(1440/m);
    if(mass)candidate.set(h,mass);
  }
  const best=Math.max(0,...candidate.values()), survivors=[];
  for(const [h,mass] of candidate){
    
    let m=h/gcd(h,L), cap=mass+(k-1-weight(m))*best;
    for(let p=2;p<=m;p++){
      for(let power=p;m%p===0;power*=p,m/=p){
        const constrained=Math.max(0,...Array.from(candidate).filter(([v])=>v/gcd(v,L)%power===0).map(([,value])=>value));
        cap+=(p-1)*constrained;
      }
    }
    if(cap<D.length*1440)continue;
    survivors.push(h);
    if(!surviving.has(h))surviving.set(h,[]);
    surviving.get(h).push({F,R,k,L});
  }
  branches.push({F,R,k,L,remain:D.length,survivors});
}


function enumerate(reverse){
const all=[];
let branchCount=0, visited=0, shapesCount=0, maxL=0;
for(const {F,R,k,L,survivors} of (reverse ? branches.slice().reverse() : branches)){
  if(!survivors.length)continue;
  branchCount++;
  const P=survivors.reduce(lcm,L);
  maxL=Math.max(maxL,P);
  const D=Array.from({length:P},(_,x)=>x).filter(x=>B.includes(x%35)&&!R.includes(x%7)&&!F.some(([m,b])=>x%m===b));
  const n=D.length, full=(1n<<BigInt(n))-1n;
  const bit=Array.from({length:n},(_,i)=>1n<<BigInt(i));
  const options=(reverse ? survivors.slice().reverse() : survivors).flatMap(h=>{
    const set=Array(h).fill(0n);
    for(let i=0;i<n;i++)set[D[i]%h]|=bit[i];
    return set.flatMap((mask,b)=>mask?[{h,b,mask}]:[]);
  });
  const at=bit.map(b=>options.flatMap((o,i)=>(o.mask&b)?[i]:[]));
  const priority=bit.map((b,i)=>i).sort((i,j)=>at[i].length-at[j].length || (reverse ? j-i : i-j));
  const chosen=[], blocked=new Uint8Array(options.length);
  const dfs=now=>{
    visited++;
    if(now===full){
      if(chosen.some(i=>{let covered=0n;for(const j of chosen)if(j!==i)covered|=options[j].mask;return (options[i].mask&~covered)===0n;}))return;
      all.push({F,R,classes:chosen.map(j=>[options[j].h,options[j].b])}); shapesCount++; return;
    }
    if(chosen.length===k)return;
    const pivot=priority.find(i=>!(now&bit[i]));
    const used=[];
    for(const j of at[pivot]){
      if(blocked[j])continue;
      chosen.push(j);
      dfs(now|options[j].mask);
      chosen.pop();
      blocked[j]=1;
      used.push(j);
    }
    for(const j of used)blocked[j]=0;
  };
  dfs(0n);
}
all.push({F:[],R:rows,classes:[]});
const assignments=new Map;
for(const {F,R,classes} of all){
 const a=[...R.map(b=>[7,b]),...classes].sort(([h,b],[j,c])=>h-j||b-c).map(([h,b])=>h+":"+b);
 assignments.set(a.join(","),a);
}
const order=[...assignments.values()].sort((a,b)=>a.length-b.length);
const minimal=[];
for(const a of order)if(!minimal.some(b=>b.every(x=>a.includes(x)))) minimal.push(a);

return {branchCount,visited,shapesCount,maxL, unique: order.length, minimal};
}
const normal=enumerate(false), reverse=enumerate(true);
const canonical=sets=>JSON.stringify(sets.map(s=>s.join(',')).sort());
assert(canonical(normal.minimal)===canonical(reverse.minimal),'search orders disagree');
const compact=[
 ['12:0','12:8'],
 ['20:0','20:8','20:16'],
 ['12:0','24:8','24:20'],
 ['12:8','24:0','24:12'],
 ['16:0','16:4','16:8','16:12'],
 ['20:0','20:8','40:16','40:36'],
 ['20:0','20:16','40:8','40:28'],
 ['20:8','20:16','40:0','40:20'],
 ['7:0','7:1','7:3','7:5','35:23','35:30'],
 ['7:0','7:2','7:3','7:5','35:8','35:15']
];
for(let mask=0;mask<32;mask++){
 const assignment=rows.map((b,i)=>mask>>i&1?'14:'+(b+(b%2)*7):'7:'+b);
 compact.push(assignment.sort((a,b)=>{
   const [h,x]=a.split(':').map(Number),[j,y]=b.split(':').map(Number);
   return h-j||x-y;
 }));
}
assert(canonical(normal.minimal)===canonical(compact),'compact formula disagrees');
assert(normal.minimal.length===42,'template count');
const bigGcd=(a,b)=>b?bigGcd(b,a%b):a;
function remove(n, bad){
 let common;
 while((common=bigGcd(n,bad))>1n)n/=common;
 return n;
}
function divisors(n){
 return Array.from({length:n},(_,i)=>i+1).filter(p=>n%p===0);
}
function trialPrime(n){
 if(n<2)return false;
 for(let p=2;p*p<=n;p++)if(n%p===0)return false;
 return true;
}
function primitive(d){
 let value=(1n<<BigInt(d))-1n;
 for(const p of divisors(d).filter(trialPrime))value=remove(value,(1n<<BigInt(d/p))-1n);
 for(const q of fixedPrimes)value=remove(value,q);
 return value;
}
function powmod(a,e,q){
 let m=BigInt(e),v=1n;
 for(;m;m>>=1n,a=a*a%q)if(m&1n)v=v*a%q;
 return v;
}
const periods=[7,12,14,16,20,24,35,40];
const inventory=Object.fromEntries(periods.map(h=>[h,divisors(36).map(g=>h*g).filter(d=>d/gcd(d,36)===h).map(d=>[d,primitive(d)]).filter(([,n])=>n>1n)]));
assert(new Set(fixedPrimes).size===74,'fixed fiber');
const order1440=inventory[40].find(([d])=>d===1440)[1];
for(const q of [37441,170251201]){
 assert(trialPrime(q),'order 1440 prime');
 assert(order1440%BigInt(q)===0n,'order 1440 carrier');
 assert(powmod(2n,1440,BigInt(q))===1n&&[2,3,5].every(p=>powmod(2n,1440/p,BigInt(q))!==1n),'order 1440 check');
}
const c576=primitive(576), c192=primitive(192);
const first=3457n,second=816769n;
assert(trialPrime(Number(first))&&trialPrime(Number(second))&&c576%(first*second)===0n,'order 576 primes');
assert(remove(remove(c576,first),second)>1n&&c192>1n,'four distinct period 16 primes');
const witness=[[20,0],[20,8],[40,36],[40,16]];
const higher=[[80,16],[80,56]];
function missing(cover){
 const all=[...fixed,...cover];
 const period=all.reduce((acc,[h])=>lcm(acc,h),35);
 return Array.from({length:period},(_,w)=>w).filter(w=>B.includes(w%35)&&!all.some(([h,b])=>w%h===b));
}
assert(missing(witness).length===0,'true witness');
assert(missing(witness.slice(0,-1)).length>0,'false witness');
assert(missing(witness.slice(0,-1).concat(higher)).length===0,'finite 11-cover');
const chosen=witness.slice(0,-1).map(([h,b])=>h+':'+b);
assert(!normal.minimal.some(a=>a.every(x=>chosen.includes(x))),'false exact cost');

const sourceFactors={"63":["92737","649657"],"80":["4278255361"],"126":["77158673929"],"192":["18446744069414584321"],"240":["394783681","46908728641"],"252":["40388473189","118750098349"],"315":["983431","870031","29728307155963706810228435378401"],"432":["209924353","4261383649","24929060818265360451708193"],"576":["3457","816769","1562985901350085709953","1422346738975853644793916289"],"630":["1765891","11247702599676505481447137991664348691"],"720":["8369281","750016890283777055704738227247474485366338380663681"],"1260":["2521","1711081","430839361","15169173997557864184867895400813639018421","17369459529909057773233442461"]};
Object.assign(sourceFactors,{
  160:["414721","44479210368001"],
  480:["23041"],
  504:["1009","21169","2627857","269389009","1475204679190128571777"],
  864:["68016300334849"],
  1440:["37441","170251201","322029272318997936286081"]
});
const tableQuotients={480:35,864:73,1440:80};
const factors={};
const product=xs=>xs.reduce((a,b)=>a*b,1n);
const support=[];
for(const h of periods){
 factors[h]=[];
 for(const [d,carrier] of inventory[h]){
   const primes=sourceFactors[d].map(BigInt);
   if(tableQuotients[d]){
     const factor=carrier/product(primes);
     assert(String(factor).length===tableQuotients[d],'Cunningham quotient length for '+d);
     primes.push(factor);
   }
   assert(product(primes)===carrier,'exact carrier product for '+d);
   for(const q of primes){
     assert(q%BigInt(d)===1n&&powmod(2n,d,q)===1n&&divisors(d).filter(trialPrime).every(p=>powmod(2n,d/p,q)!==1n),'exact order '+d);
     support.push({h,d,q});
     factors[h].push(q);
   }
 }
}
assert(new Set(support.map(row=>row.q)).size===43,'coordinate count and distinctness');
const bitLength=n=>n.toString(2).length;
const modulus=product(support.map(row=>row.q));
const colors={};
for(const h of periods){
 colors[h]=[...new Set(normal.minimal.flatMap(template=>template.map(s=>s.split(':').map(Number)).filter(([i])=>i===h).map(([,b])=>b)))].sort((a,b)=>a-b);
}
function byConvolution(primes,k){
 let value=Array(1<<k).fill(0n);
 value[0]=1n;
 for(const q of primes){
   const next=Array(1<<k).fill(0n);
   for(let mask=0;mask<value.length;mask++){
     next[mask]+=value[mask]*(q-2n*BigInt(k));
     for(let j=0;j<k;j++)next[mask|1<<j]+=2n*value[mask];
   }
   value=next;
 }
 return value;
}
const bitCount=n=>n?n%2+bitCount(n>>1):0;
function byMobius(primes,k){
 const cumulative=Array.from({length:1<<k},(_,m)=>product(primes.map(q=>q-2n*BigInt(k-bitCount(m)))));
 for(let j=0;j<k;j++)for(let s=0;s<cumulative.length;s++)if(s>>j&1)cumulative[s]-=cumulative[s^1<<j];
 return cumulative;
}
const nine=[["7:0","7:1","7:2","7:3","7:5"],["12:0","12:8"],["20:0","20:8","20:16"]];
const sectors=[[7,14,35],[12,24],[16],[20,40]];
function componentCounts(selected, budget, alternate){
 const list=budget===9?nine:normal.minimal;
 const colorWeights={};
 for(const h of periods){
   const primes=selected.filter(x=>x.h===h).map(x=>x.q);
   const count=colors[h].length;
   colorWeights[h]=(alternate?byMobius:byConvolution)(primes,count);
   assert(colorWeights[h].reduce((a,b)=>a+b,0n)===product(primes),'mask total');
 }
 const outcomes=[];
 for(const hs of sectors){
   const eligible=list.filter(term=>term.every(s=>hs.includes(Number(s.split(':')[0]))));
   const conditions=eligible.map(term=>term.map(s=>s.split(':').map(Number)).map(([h,b])=>[h,1<<colors[h].indexOf(b)]));
   const assignment={}, total=product(selected.filter(x=>hs.includes(x.h)).map(x=>x.q));
   let hit=0n;
   function visit(i,weight){
     if(i===hs.length){
       if(conditions.some(term=>term.every(([h,b])=>assignment[h]&b)))hit+=weight;
       return;
     }
     const h=hs[i];
     for(let m=0;m<colorWeights[h].length;m++)if(colorWeights[h][m]){
        assignment[h]=m;
        visit(i+1,weight*colorWeights[h][m]);
     }
   }
   visit(0,1n);
   outcomes.push({total,hit});
 }
 return {
  numerator:product(outcomes.map(x=>x.total))-product(outcomes.map(x=>x.total-x.hit)),
  denominator:product(outcomes.map(x=>x.total)),
  outcomes
 };
}
function subtract(a,b){
 const denominator=a.denominator*b.denominator;
 const numerator=a.numerator*b.denominator-b.numerator*a.denominator;
 const g=bigGcd(numerator,denominator);
 return {numerator:numerator/g,denominator:denominator/g};
}
const den9=componentCounts(support,9,false),den10=componentCounts(support,10,false);
const no1440=componentCounts(support.filter(x=>x.d<1440),10,false);
for(const [start,b] of [[den9,9],[den10,10]]){
 const other=componentCounts(support,b,true);
 assert(start.numerator===other.numerator&&start.denominator===other.denominator,'two counts agree');
}
const exact=subtract(den10,den9),sharp=subtract(den10,no1440);
const decimal=(n,d,digits=70)=>{
 const radix=10n**BigInt(digits);
 const a=String(n*radix/d).padStart(digits+1,'0');
 return a.slice(0,-digits)+'.'+a.slice(-digits);
};
const describe=f=>({numerator:String(f.numerator),denominator:String(f.denominator),decimal:decimal(f.numerator,f.denominator)});

const r3a=BigInt("191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163");
const r3s=BigInt("398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390");
const fixedZero=["29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const modulo=(a,m)=>(a%m+m)%m;
const inverse=(a,p)=>powmod(modulo(a,p),p-2n,p);
let a4=r3a,s4=r3s;
for(const p of fixedZero){
 const k=modulo(-a4*inverse(s4,p),p);
 a4+=s4*k;
 s4*=p;
}
assert(a4>0n&&a4<s4&&a4%r3s===r3a&&fixedZero.every(p=>a4%p===0n),'R4 base');
const options={};
for(const h of periods)for(const b of colors[h]){
 const key=h+':'+b;
 options[key]=support.filter(x=>x.h===h).map(({q,d})=>{
  const inverseSquareRoot=powmod(2n,(-16-18*b)%d+d,q);
  const inv=inverse(s4,q), a=modulo((inverseSquareRoot-a4)*inv,q), z=modulo((-inverseSquareRoot-a4)*inv,q);
  assert(a!==z,'two distinct root residues');
  return {q, values:[a,z],b,h};
 });
}
const isNineIndex=j=>nine.some(t=>t.every(key=>options[key].some(({q,values})=>values.includes(j%q))));
const nonNine=normal.minimal.filter(term=>!nine.some(n=>n.join(',')===term.join(',')));
function findMinimum(reverse) {
 const terms=reverse?nonNine.slice().reverse():nonNine;
 let best=null,bestSlots=null,bestClasses=0,leaves=0,pruned=0;
 const chosen=[];
 for(const template of terms){
  const order=reverse?template.slice().reverse():template;
  const remaining=new Set;
  const search=(depth,j,m)=>{
   if(depth===order.length){
    leaves++;
    for(let candidate=j;best===null||candidate<best;candidate+=m){
     if(isNineIndex(candidate))continue;
     best=candidate;
     bestSlots=chosen.map(x=>({...x}));
     bestClasses++;
     break;
    }
    return;
   }
   if(best!==null&&j>=best){pruned++;return;}
   for(const option of options[order[depth]]){
    const {q,values,b,h}=option;
    if(remaining.has(q))continue;
    remaining.add(q);
    const inv=inverse(m,q);
    for(const residue of values){
     const offset=modulo((residue-j)*inv,q);
     const next=j+m*offset;
     chosen.push({h,b,q:String(q),jResidue:String(residue)});
     search(depth+1,next,m*q);
     chosen.pop();
    }
    remaining.delete(q);
   }
  };
  search(0,0n,1n);
 }
 return {best,bestSlots,bestClasses,leaves,pruned};
}
const forwardMinimum=findMinimum(false), reverseMinimum=findMinimum(true);
assert(forwardMinimum.best===reverseMinimum.best,'two minimum searches');
const jMinimum=forwardMinimum.best;
const rootMinimum=a4+s4*jMinimum;
assert(!isNineIndex(jMinimum),'exact cost ten at minimum');
const matching=forwardMinimum.bestSlots.map(x=>[x.h,x.b]);
assert(normal.minimal.some(t=>t.every(s=>matching.map(([h,b])=>h+':'+b).includes(s))),'cover term at minimum');
for(const {h,b,q} of forwardMinimum.bestSlots){
 const p=BigInt(q);
 assert((rootMinimum%p)**2n*powmod(2n,32+36*b,p)%p===1n,'root phase at minimum');
}
const minReceipt={
  base:a4.toString(),step:s4.toString(),
  minIndex:String(jMinimum),minRoot:String(rootMinimum),minDigits:String(rootMinimum).length,
  minimumSlots:forwardMinimum.bestSlots,
  forward:{visits:forwardMinimum.leaves,improvements:forwardMinimum.bestClasses,pruned:forwardMinimum.pruned},
  reverse:{visits:reverseMinimum.leaves,improvements:reverseMinimum.bestClasses,pruned:reverseMinimum.pruned}
};
const receipt={
 support:support.map(({h,d,q})=>({h,d,q:String(q)})),
 counts:Object.fromEntries(periods.map(h=>[h,factors[h].length])),
 modulus:{bits:bitLength(modulus),digits:String(modulus).length},
 atMostNine:describe(den9),
 atMostTen:describe(den10),
 exactTen:describe(exact),
 needs1440:describe(sharp),
 inverseExactTen:decimal(exact.denominator,exact.numerator,20),
 fractionOfExactTenNeeding1440:decimal(sharp.numerator*exact.denominator,sharp.denominator*exact.numerator,36),
 sectors:den10.outcomes.map(x=>describe({numerator:x.hit,denominator:x.total}))
};

const appendix={"480":"14768784307009061644318236958041601","864":"7311824282729722035859309520826138827918372038863677678267962656996811009","1440":"19194878188585855612908061936944281464039294965346491767953330250249208842371201"};
for(const [d,q] of Object.entries(appendix)){
 assert(support.some(x=>x.d===Number(d)&&String(x.q)===q),'exact Appendix A factor at order '+d);
}
const coverDictionary=[7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417,5,13,19,73,38737,649657,92737,21169,2627857,1009];
const fullOrder=p=>{
 let residue=2,d=1;
 while(residue!==1){residue=residue*2%p;d++;}
 return d;
};
const coverPeriod=coverDictionary.map(fullOrder).reduce(lcm);
const phase=coverDictionary.map(q=>Number(rootMinimum%BigInt(q))**2%q);
for(let n=1;n<=coverPeriod;n++){
 let hits=0;
 for(let i=0;i<phase.length;i++){
   phase[i]=phase[i]*2%coverDictionary[i];
   if(phase[i]===1)hits++;
 }
 assert(hits>0,'direct cover gap at exponent '+n);
}
const witnesses=[{"q":21169,"n":1112},{"q":1009,"n":1472},{"q":29191,"n":593},{"q":113,"n":413},{"q":2627857,"n":2912},{"q":1321,"n":377},{"q":92737,"n":320},{"q":71,"n":293},{"q":337,"n":752},{"q":673,"n":237},{"q":281,"n":233},{"q":641,"n":207},{"q":19,"n":152},{"q":38737,"n":140},{"q":41,"n":125},{"q":97,"n":117},{"q":127,"n":113},{"q":6700417,"n":111},{"q":31,"n":89},{"q":257,"n":135},{"q":65537,"n":255},{"q":14449,"n":53},{"q":151,"n":41},{"q":241,"n":33},{"q":649657,"n":2048},{"q":73,"n":20},{"q":7,"n":16},{"q":13,"n":12},{"q":5,"n":6},{"q":17,"n":3}];
const witnessTerms=witnesses.map(({q,n})=>{
 const term=(rootMinimum*rootMinimum<<BigInt(n))-1n;
 assert(term>BigInt(q)&&term%BigInt(q)===0n,'proper private divisor');
 assert(coverDictionary.filter(p=>term%BigInt(p)===0n).length===1,'unique cover channel');
 return term;
});
for(let j=0;j<witnessTerms.length;j++)for(let k=0;k<j;k++){
 assert(bigGcd(witnessTerms[j],witnessTerms[k])===1n,'unrestricted coprimality pair');
}
const totalCost={coverPeriod,witnesses,pairChecks:435,maximumExponent:Math.max(...witnesses.map(x=>x.n)),unrestrictedMinimum:30};
const result={density:receipt,minimum:minReceipt,totalCost};
if(typeof text==='function'){store('run2result',result);text({support:receipt.counts,density:receipt.exactTen.decimal,j:minReceipt.minIndex,digits:minReceipt.minDigits,total:totalCost.unrestrictedMinimum});}
else console.log(JSON.stringify(result,null,2));
