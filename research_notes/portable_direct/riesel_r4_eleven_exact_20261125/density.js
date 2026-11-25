
const assert=(v,m)=>{if(!v)throw Error(m);};
const groupMap={"7":[63,126,252],"9":[81,162,324],"12":[432],"14":[504],"15":[135,270,540],"16":[192,576],"18":[648],"20":[80,240,720],"21":[189,378,756],"24":[864],"28":[112,336,1008],"30":[1080],"32":[128,384,1152],"35":[315,630,1260],"36":[1296],"40":[160,480,1440],"48":[1728],"60":[2160],"70":[280,840,2520],"80":[320,960,2880],"140":[560,1680,5040]};
const known={"63":["92737","649657"],"80":["4278255361"],"81":["2593","71119","97685839"],"112":["5153","54410972897"],"126":["77158673929"],"128":["274177"],"135":["271","348031","49971617830801"],"160":["414721","44479210368001"],"162":["163","135433","272010961"],"189":["1560007"],"192":["18446744069414584321"],"240":["394783681","46908728641"],"252":["40388473189","118750098349"],"270":["811","15121","385838642647891"],"280":["84179842077657862011867889681"],"315":["983431","870031","29728307155963706810228435378401"],"320":["3602561"],"324":["3618757","106979941","168410989","4977454861"],"336":["2017","25629623713","1538595959564161"],"378":["379","119827","127391413339","56202143607667"],"384":["769"],"432":["209924353","4261383649","24929060818265360451708193"],"480":["23041"],"504":["1009","21169","2627857","269389009","1475204679190128571777"],"540":["541","166242935471754241","165041853060421","30241","49681"],"560":["4481","557761","736961"],"576":["3457","816769","1562985901350085709953","1422346738975853644793916289"],"630":["1765891","11247702599676505481447137991664348691"],"648":["1297","3889","30433969","1164777409","3718266498433","134921168163073","1174029487714513"],"720":["8369281","750016890283777055704738227247474485366338380663681"],"756":["757","456376431053626339473533320957","304832756195865229284807891468769"],"840":["127681","1130641","755667361","54169520413224311136354324156824071681"],"864":["68016300334849"],"960":["26881","4855681","610548481","137603804161"],"1008":["34273"],"1080":["2161","21601","201519653761","1117180440577441"],"1152":["17047297","628582818817"],"1260":["2521","1711081","430839361","15169173997557864184867895400813639018421","17369459529909057773233442461"],"1296":["10369","259201","1824045366145909775041","524833094849624730914401"],"1440":["37441","170251201","322029272318997936286081"],"1680":["13441","4841172001","1586308510081"],"1728":["1718990209","8148919324033","672915391135935402269916482777538049"],"2160":["6281281","148759201","4518776161","30263419164953868175425499201"],"2520":["1325521","1626833408812908876721","164861463278712334259867127702044401","517496882214135484318298195143896326867475066317761"],"2880":["252581761","40056698881","35884034243486024947201"],"5040":[]};
const sourceCofactorDigits={"128":14,"189":27,"320":32,"384":36,"480":35,"560":43,"864":73,"960":47,"1008":83,"1080":53,"1152":97,"1296":76,"1440":80,"1680":90,"1728":116,"2160":121,"2520":61,"2880":190};
const fixedPrimes=["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const trial=n=>{for(let d=2;d*d<=n;d++)if(n%d===0)return false;return n>1;};
const gcd=(a,b)=>b?gcd(b,a%b):a;
const product=x=>x.reduce((a,b)=>a*b,1n);
function powmod(a,n,m){let r=1n;for(let e=BigInt(n);e;e>>=1n,a=a*a%m)if(e&1n)r=r*a%m;return r;}
function strip(a,b){let d;while((d=gcd(a,b))>1n)a/=d;return a;}
const rowsByOrder={};
for(const [h,ds] of Object.entries(groupMap))for(const d of ds){
 const r=Array.from({length:d},(_,i)=>i+1).filter(p=>!(d%p)&&trial(p));
 let carrier=(1n<<BigInt(d))-1n;
 for(const p of r)carrier=strip(carrier,(1n<<BigInt(d/p))-1n);
 for(const q of fixedPrimes)carrier=strip(carrier,q);
 const factors=known[d].map(BigInt), quotient=carrier/product(factors);
 if(sourceCofactorDigits[d]){
  assert(String(quotient).length===sourceCofactorDigits[d],'table cofactor '+d);
  factors.push(quotient);
 }
 const remaining=carrier/product(factors);
 assert(product(factors)*remaining===carrier&&(d===5040||remaining===1n),'exact product '+d);
 for(const q of factors)assert(q%BigInt(d)===1n&&powmod(2n,d,q)===1n&&r.every(p=>powmod(2n,d/p,q)!==1n),'exact order verification '+d);
 rowsByOrder[d]={h:Number(h),d,carrier,factors,remaining};
}
const support=Object.values(rowsByOrder).flatMap(({h,d,factors})=>factors.map(q=>({h,d,q})));
assert(support.length===142&&new Set(support.map(x=>x.q)).size===142,'142 identified primes');
const unresolved=rowsByOrder[5040].remaining;

const templates=require('./templates.json');

const groupOrder=[12,20,7,14,9,15,18,36,30,60,16,24,32,48,40,80,21,28,35,70,140];
const groups={},offset={},names=[];
for(const h of groupOrder){
 offset[h]=names.length;
 groups[h]=[...new Set(templates.flat().filter(s=>s.startsWith(h+':')))].sort();
 names.push(...groups[h]);
}
const variable=new Map(names.map((x,i)=>[x,i]));
const nodes=[null,null], ids=new Map;
function decision(k,a,b){
 if(a===b)return a;
 const key=k+','+a+','+b;
 let id=ids.get(key);
 if(id===undefined){id=nodes.length;nodes.push([k,a,b]);ids.set(key,id);}
 return id;
}
const unionCache=new Map;
function union(a,b){
 if(a===1||b===1)return 1;
 if(a===0||a===b)return b;
 if(b===0)return a;
 if(a>b)[a,b]=[b,a];
 const key=a+','+b;
 let c=unionCache.get(key);
 if(c!==undefined)return c;
 const [ka,al,ah]=nodes[a], [kb,bl,bh]=nodes[b];
 if(ka===kb)c=decision(ka,union(al,bl),union(ah,bh));
 else if(ka<kb)c=decision(ka,union(al,b),union(ah,b));
 else c=decision(kb,union(bl,a),union(bh,a));
 unionCache.set(key,c);
 return c;
}
let root=0;
for(const t of templates){
 const ordered=t.map(x=>variable.get(x)).sort((a,b)=>b-a);
 root=union(root,ordered.reduce((r,k)=>decision(k,0,r),1));
}
ids.clear();
unionCache.clear();
const pop=n=>n?n%2+pop(n>>1):0;
function maskWeights(list,k){
 const M=1<<k;
 let weights=Array(M).fill(0n);weights[0]=1n;
 for(const q of list){
   const next=Array(M).fill(0n);
   for(let m=0;m<M;m++)if(weights[m]){
     next[m]+=weights[m]*(q-2n*BigInt(k));
     for(let j=0;j<k;j++)next[m|1<<j]+=2n*weights[m];
   }
   weights=next;
 }
 const independent=Array.from({length:M},(_,m)=>product(list.map(q=>q-2n*BigInt(k-pop(m)))));
 for(let j=0;j<k;j++)for(let m=0;m<M;m++)if(m>>j&1)independent[m]-=independent[m^1<<j];
 assert(weights.every((x,i)=>x===independent[i]),'occupancy replay');
 return weights;
}
const lists={};for(const {h,q} of support)(lists[h]??=[]).push(q);
function step(id,mask,start,k){
 while(id>1&&nodes[id][0]<start+k){
  const [j,l,r]=nodes[id]; id=(mask>>(j-start)&1)?r:l;
 }
 return id;
}
const factors=[];
let weightsByNode=new Map([[root,1n]]),denominator=1n;
const sizes=[];
for(const h of groupOrder.slice(0,-1)){
 const start=offset[h],k=groups[h].length,probs=maskWeights(lists[h],k),den=product(lists[h]);
 denominator*=den;
 const next=new Map;
 for(const [id,weight] of weightsByNode){
  if(id<2||nodes[id][0]>=start+k){
   next.set(id,(next.get(id)??0n)+weight*den);continue;
  }
  const aggregate=new Map;
  for(let mask=0;mask<probs.length;mask++)if(probs[mask]){
   const target=step(id,mask,start,k);
   aggregate.set(target,(aggregate.get(target)??0n)+probs[mask]);
  }
  for(const [target,value] of aggregate)next.set(target,(next.get(target)??0n)+weight*value);
 }
 weightsByNode=next;sizes.push(next.size);
}
const conditional=Array.from({length:8},(_,mask)=>{
 let result=0n;
 for(const [id,weight] of weightsByNode)if(step(id,mask,offset[140],3)===1)result+=weight;
 return result;
});
const y=[conditional[0],conditional[1],conditional[3],conditional[7]];
assert(conditional.every((x,i)=>x===y[pop(i)]),'conditional symmetry');
const provenance={
 nodes:nodes.length,sizes,conditional,denominator,
 known140:lists[140],
 symbolicCoefficients:[y[3],3n*(y[2]-y[3]),3n*(y[1]-2n*y[2]+y[3]),y[0]-3n*y[1]+3n*y[2]-y[3]]
};

const lowerPrime=100000000000n, order=5040n;
let scanned=0;
for(let q=order+1n;q<=lowerPrime;q+=order){
 assert(unresolved%q!==0n,'new factor '+q);
 scanned++;
}
let maxFactors=0, minProduct=1n;
const firstAbove=1n+order*((lowerPrime-1n)/order+1n);
while(minProduct*firstAbove<=unresolved){minProduct*=firstAbove;maxFactors++;}
let odd=unresolved-1n,twoPower=0;
while(!(odd&1n)){odd>>=1n;twoPower++;}
let u=powmod(3n,odd,unresolved),passes=u===1n||u===unresolved-1n;
for(let j=1;j<twoPower;j++){u=u*u%unresolved;passes||=u===unresolved-1n;}
assert(!passes,'base-3 strong compositeness witness');
for(let p=2;p<=maxFactors;p++)if(trial(p)){
 let low=1n,high=1n<<BigInt(Math.ceil(unresolved.toString(2).length/p));
 while(low<high){
  const mid=(low+high)>>1n;
  if(mid**BigInt(p)<unresolved)low=mid+1n;else high=mid;
 }
 assert(low**BigInt(p)!==unresolved,'perfect power');
}
function exactWith(extra){
 const list=[...lists[140],...extra], counts=maskWeights(list,3);
 const a=counts.reduce((n,v,i)=>n+v*conditional[i],0n), b=product(list)*denominator;
 const tN=BigInt("173824996471925526523603604877392898312773304909756301273102280081164283417262458415093313440431367006717203641925542017556721983780042462423521329493960383319354293534079707079760464978363874328970609801025182294249028040102379962400257739557283240553561796364337499419798156079132522544533785450488895897622528182613665491566917541393945719141457955870603322843212508526993561066043234902094334645556850437197908504880454037694432450635338070866680886658704408847182376191453027613224336272342562794879539771100872766954442214360304181650001190558531809137843069176409625182838490896670670793290463715205632033689212845793494730157415553262639649009136745504573201143178044933100559794596238735575591169855336"),tD=BigInt("19434597027744866287388042084654112295755392478677904090236180827865141881070427721314071636810299027562702703771964778353142174176574152130185705853520382865796877629873053125587959373285392712490933277649647100749597662194506124474900851259609345288047228677809012823291497763388882377488982670143320602920818231550592209780585851403315071287077106935936947970248472128756128437214051737513915070091144490731749914203669250790310906141461659505340096188351853141613695212415547479691723351269507640666008997050872916009936080852888071006362446732149388854734165428359828705124921768471359793744139949993557690623660583605329643901824709182159335466557815379967082758161010500146158314328229040927179930942328466975440957870081");
 const n=a*tD-tN*b,d=b*tD,g=gcd(n,d);
 return {n:n/g,d:d/g};
}
const lower=exactWith([]), upper=exactWith(Array(maxFactors).fill(firstAbove));
const d=gcd(lower.d,upper.d);
const width={n:upper.n*(lower.d/d)-lower.n*(upper.d/d),d:upper.d*(lower.d/d)};
function dec(f,k=73){
 const x=String(f.n*10n**BigInt(k)/f.d).padStart(k+1,'0');
 return x.slice(0,-k)+'.'+x.slice(-k);
}
const finalReport={...provenance,lower,upper,width,decLower:dec(lower),decUpper:dec(upper),decWidth:dec(width),primeInterval:[144,142+maxFactors],scanned,firstAbove,remaining:String(unresolved),inventory:rowsByOrder};

console.log(JSON.stringify(finalReport,(_,v)=>typeof v==='bigint'?String(v):v,2));
