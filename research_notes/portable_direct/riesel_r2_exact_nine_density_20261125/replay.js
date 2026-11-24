"use strict";
// Exact weighted Riesel R2 ninth-cost density. Standard Node.js.
const lowOrders=[{"d":14,"f":7,"carrier":"43","primeFactors":["43"]},{"d":27,"f":9,"carrier":"262657","primeFactors":["262657"]},{"d":28,"f":7,"carrier":"29","primeFactors":["29"]},{"d":35,"f":35,"carrier":"122921","primeFactors":["122921"]},{"d":40,"f":10,"carrier":"61681","primeFactors":["61681"]},{"d":42,"f":7,"carrier":"5419","primeFactors":["5419"]},{"d":45,"f":15,"carrier":"14709241","primeFactors":["631","23311"]},{"d":54,"f":9,"carrier":"87211","primeFactors":["87211"]},{"d":56,"f":14,"carrier":"15790321","primeFactors":["15790321"]},{"d":63,"f":21,"carrier":"60247241209","primeFactors":["92737","649657"]},{"d":70,"f":35,"carrier":"86171","primeFactors":["86171"]},{"d":80,"f":20,"carrier":"4278255361","primeFactors":["4278255361"]},{"d":81,"f":27,"carrier":"18014398643699713","primeFactors":["2593","71119","97685839"]},{"d":84,"f":7,"carrier":"1429","primeFactors":["1429"]},{"d":90,"f":15,"carrier":"18837001","primeFactors":["18837001"]},{"d":96,"f":8,"carrier":"4294901761","primeFactors":["193","22253377"]},{"d":105,"f":35,"carrier":"16219885921","primeFactors":["106681","152041"]},{"d":108,"f":9,"carrier":"68719214593","primeFactors":["246241","279073"]},{"d":112,"f":28,"carrier":"280379743338241","primeFactors":["5153","54410972897"]},{"d":120,"f":10,"carrier":"4562284561","primeFactors":["4562284561"]},{"d":126,"f":21,"carrier":"77158673929","primeFactors":["77158673929"]},{"d":135,"f":45,"carrier":"4713143145948577267201","primeFactors":["271","348031","49971617830801"]},{"d":140,"f":35,"carrier":"351479006145541","primeFactors":["7416361","47392381"]},{"d":144,"f":12,"carrier":"281474959933441","primeFactors":["577","487824887233"]},{"d":162,"f":27,"carrier":"6004799458421419","primeFactors":["163","135433","272010961"]},{"d":168,"f":14,"carrier":"298994165018641","primeFactors":["3361","88959882481"]},{"d":180,"f":15,"carrier":"285871932440641","primeFactors":["181","54001","29247661"]},{"d":192,"f":16,"carrier":"18446744069414584321","primeFactors":["18446744069414584321"]},{"d":210,"f":35,"carrier":"219397309247971","primeFactors":["211","664441","1564921"]},{"d":216,"f":18,"carrier":"4722366482800925736961","primeFactors":["33975937","138991501037953"]},{"d":240,"f":20,"carrier":"18518800563924107521","primeFactors":["394783681","46908728641"]},{"d":252,"f":21,"carrier":"4796135163359699664961","primeFactors":["40388473189","118750098349"]},{"d":270,"f":45,"carrier":"4731589819653274206721","primeFactors":["811","15121","385838642647891"]},{"d":280,"f":70,"carrier":"84179842077657862011867889681","primeFactors":["84179842077657862011867889681"]},{"d":288,"f":24,"carrier":"79228162514264056118567239681","primeFactors":["1153","6337","38941695937","278452876033"]},{"d":315,"f":105,"carrier":"25435999094089869005186806358949569337458761","primeFactors":["983431","870031","29728307155963706810228435378401"]},{"d":324,"f":27,"carrier":"324518553658426708768757511094273","primeFactors":["3618757","106979941","168410989","4977454861"]},{"d":336,"f":28,"carrier":"79537642783272737189578932481","primeFactors":["2017","25629623713","1538595959564161"]},{"d":360,"f":30,"carrier":"79247505326224968612036218881","primeFactors":["168692292721","469775495062434961"]},{"d":420,"f":35,"carrier":"64439678971267470274607674381","primeFactors":["421","146919792181","1041815865690181"]},{"d":432,"f":36,"carrier":"22300745198530623141530995906165491860766721","primeFactors":["209924353","4261383649","24929060818265360451708193"]},{"d":540,"f":45,"carrier":"22300830269122352138206822446422676394475521","primeFactors":["541","166242935471754241","165041853060421","30241","49681"]},{"d":576,"f":48,"carrier":"6277101735386680763835789423128438253588091106870490562561","primeFactors":["3457","816769","1562985901350085709953","1422346738975853644793916289"]},{"d":630,"f":105,"carrier":"19862216791445343941138167955238148374298681","primeFactors":["1765891","11247702599676505481447137991664348691"]},{"d":720,"f":60,"carrier":"6277102109531099920545607255275970508361273848859312783361","primeFactors":["8369281","750016890283777055704738227247474485366338380663681"]},{"d":840,"f":70,"carrier":"5909308463143070387023565125357309194045904419102963794161","primeFactors":["127681","1130641","755667361","54169520413224311136354324156824071681"]}];
const eight=[[[3,0],[3,1],[6,5],[8,0],[8,4],[12,2]],[[3,0],[3,1],[6,5],[8,0],[12,2],[24,20]],[[3,0],[3,1],[6,5],[8,2],[8,6],[12,8]],[[3,0],[3,1],[6,5],[8,2],[12,8],[24,14]],[[3,0],[3,1],[6,5],[8,4],[12,2],[24,8]],[[3,0],[3,1],[6,5],[8,6],[12,8],[24,2]],[[3,0],[3,1],[6,5],[9,2],[9,5],[18,8]],[[3,0],[3,1],[6,5],[9,2],[9,8],[18,14]],[[3,0],[3,1],[6,5],[9,2],[18,8],[18,14]],[[3,0],[3,1],[6,5],[9,5],[9,8],[18,2]],[[3,0],[3,1],[6,5],[9,5],[18,2],[18,8]],[[3,0],[3,1],[6,5],[9,8],[18,2],[18,14]],[[3,0],[3,1],[6,5],[10,0],[10,2],[15,11]],[[3,0],[3,1],[6,5],[10,0],[10,2],[30,26]],[[3,0],[3,1],[6,5],[10,0],[10,6],[15,2]],[[3,0],[3,1],[6,5],[10,0],[10,6],[30,2]],[[3,0],[3,1],[6,5],[10,0],[15,2],[15,11]],[[3,0],[3,1],[6,5],[10,0],[15,2],[30,26]],[[3,0],[3,1],[6,5],[10,0],[15,11],[30,2]],[[3,0],[3,1],[6,5],[10,0],[30,2],[30,26]],[[3,0],[3,1],[6,5],[10,2],[10,6],[15,5]],[[3,0],[3,1],[6,5],[10,2],[10,6],[30,20]],[[3,0],[3,1],[6,5],[10,2],[15,5],[15,11]],[[3,0],[3,1],[6,5],[10,2],[15,5],[30,26]],[[3,0],[3,1],[6,5],[10,2],[15,11],[30,20]],[[3,0],[3,1],[6,5],[10,2],[30,20],[30,26]],[[3,0],[3,1],[6,5],[10,6],[15,2],[15,5]],[[3,0],[3,1],[6,5],[10,6],[15,2],[30,20]],[[3,0],[3,1],[6,5],[10,6],[15,5],[30,2]],[[3,0],[3,1],[6,5],[10,6],[30,2],[30,20]],[[3,0],[3,1],[6,5],[12,2],[12,8]],[[3,0],[3,1],[6,5],[12,2],[24,8],[24,20]],[[3,0],[3,1],[6,5],[12,8],[24,2],[24,14]],[[3,0],[3,1],[6,5],[15,2],[15,5],[30,26]],[[3,0],[3,1],[6,5],[15,2],[15,11],[30,20]],[[3,0],[3,1],[6,5],[15,2],[30,20],[30,26]],[[3,0],[3,1],[6,5],[15,5],[15,11],[30,2]],[[3,0],[3,1],[6,5],[15,5],[30,2],[30,26]],[[3,0],[3,1],[6,5],[15,11],[30,2],[30,20]],[[3,0],[3,1],[9,2],[9,5],[9,8]],[[3,0],[3,1],[9,2],[9,5],[18,8],[18,17]],[[3,0],[3,1],[9,2],[9,8],[18,5],[18,14]],[[3,0],[3,1],[9,5],[9,8],[18,2],[18,11]],[[3,0],[3,1],[10,0],[10,5],[15,2],[15,11]],[[3,0],[3,1],[10,0],[15,2],[15,11],[30,5]],[[3,0],[3,1],[10,1],[10,6],[15,2],[15,5]],[[3,0],[3,1],[10,1],[15,2],[15,5],[30,26]],[[3,0],[3,1],[10,2],[10,7],[15,5],[15,11]],[[3,0],[3,1],[10,2],[15,5],[15,11],[30,17]],[[3,0],[3,1],[10,5],[15,2],[15,11],[30,20]],[[3,0],[3,1],[10,6],[15,2],[15,5],[30,11]],[[3,0],[3,1],[10,7],[15,5],[15,11],[30,2]],[[3,0],[3,1],[15,2],[15,5],[15,11]],[[3,0],[3,1],[15,2],[15,5],[30,11],[30,26]],[[3,0],[3,1],[15,2],[15,11],[30,5],[30,20]],[[3,0],[3,1],[15,5],[15,11],[30,2],[30,17]],[[7,1],[7,2],[7,3],[7,4],[14,5],[14,12]],[[7,1],[7,2],[7,3],[7,4],[35,12],[35,26]],[[7,1],[7,2],[7,3],[7,5],[14,4],[14,11]],[[7,1],[7,2],[7,4],[7,5],[14,3],[14,10]],[[7,1],[7,3],[7,4],[7,5],[14,2],[14,9]],[[7,2],[7,3],[7,4],[7,5],[14,1],[14,8]],[[7,2],[7,3],[7,4],[7,5],[35,1],[35,22]]];
const high=["2521","1711081","430839361","15169173997557864184867895400813639018421","17369459529909057773233442461"].map(BigInt);
const certificates={"2":{"trial":true},"3":{"trial":true},"5":{"trial":true},"7":{"trial":true},"11":{"trial":true},"13":{"trial":true},"17":{"trial":true},"53":{"trial":true},"61":{"trial":true},"79":{"trial":true},"269":{"trial":true},"1009":{"trial":true},"1237":{"trial":true},"5023":{"trial":true},"11059":{"trial":true},"24137":{"trial":true},"33613":{"trial":true},"147583":{"trial":true},"490019":{"trial":true},"1321867":{"witness":"5","factors":["2","3","3","3","7","13","269"]},"3813647":{"witness":"5","factors":["2","79","24137"]},"5876911":{"witness":"3","factors":["2","3","3","5","13","5023"]},"108030757":{"witness":"6","factors":["2","2","3","61","147583"]},"481159589":{"witness":"2","factors":["2","2","7","13","1321867"]},"705229321":{"witness":"7","factors":["2","2","2","3","5","5876911"]},"962319179":{"witness":"2","factors":["2","481159589"]},"8462751853":{"witness":"2","factors":["2","2","3","705229321"]},"34155666478709":{"witness":"2","factors":["2","2","1009","8462751853"]},"68311332957419":{"witness":"2","factors":["2","34155666478709"]},"1787204323666025736575806739":{"witness":"6","factors":["2","7","490019","3813647","68311332957419"]},"15169173997557864184867895400813639018421":{"witness":"6","factors":["2","2","3","3","5","7","7","962319179","1787204323666025736575806739"]},"2939949020999":{"witness":"7","factors":["2","11","1237","108030757"]},"1383487090199751419":{"witness":"2","factors":["2","7","33613","2939949020999"]},"17369459529909057773233442461":{"witness":"6","factors":["2","2","3","3","5","7","17","53","11059","1383487090199751419"]}};
const pinned={"E8":["565816937112231449046422498456967993145423713507953630498210783859635254028760303334681935091331556457718881506315256280763501907784875680395763151997720719067379970570027070179540409558250077981343948428242278928321404110624594938339870952622839738203466336080787902584","1687936861924892928600586207409119244885807147820427360001433994839215745422796726803682778182298630610938914767020505052905678176492395944819775715609631709102151057663437747208438967963071706571533788668993607868086132054664820330703149225461619075408060553229640039633809623"],"C9":["891367955654260167838662075303312503821400208884168994834773162527774157742139539426354281701947845975350589332623262349126951888140998984061346410782878008091694557077117229374950690375875685736971873600055236081256757860971697418674726640640","121503409755993984015616148321221111373884839240032737920700917091193930405855571843553441888683482567125855932208084969920942599744931155615659937379335176649865514730108529380064893402208433789737658884632403620106533536398999682453736988937260886944017"],"C9_exact_total9":["53855506484872057645003998133796427382242466729370130894643879905743250155638310212057615146201407244441517306115111916509501082439289565068382656498281794943752557537133277938404610778455795392216392526078894037197726735790171763266415886599922002566081789252602509130440217271137922955973330580506195769023778616028718416878611714538669069186760705464450068617700385837992950438558590623744","18724934816241943464222087041239018728256714611868669285389411411096127597546640959122647330450828634968880648817089222396405970388765950596481025670606674031790319267213710297556431312694405236265043360510925553721949123394356461041827235798483141236935245724060401616125881709704009406988088253174199993964681199450493782751934702821885595506227506462873593703071110481369806002546142189702590027125874903"]};

function verifyCarriers(low,high,certificates){
  const fixedS2=11356718000553566643685496313583434507970452519839503606327232707476034989690n;
  const H=new Set([1,2,3,4,5,6,7,8,9,10,12,15,16,20,35]), F=new Set([7,10,14,28,35,70]);
  const gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a;
  const power=(a,n,p)=>{let r=1n;for(a%=p;n;n>>=1n){if(n&1n)r=r*a%p;a=a*a%p;}return r;};
  const strip=(a,b)=>{let g;while((g=gcd(a,b))>1n)a/=g;return a;};
  const factors=d=>{const ps=[];for(let p=2;p*p<=d;p++)if(d%p===0){ps.push(p);while(d%p===0)d/=p;}if(d>1)ps.push(d);return ps;};
  const product=xs=>xs.reduce((a,b)=>a*b,1n);
  const proved=new Set();
  function trial(p){if(p<2n)throw Error("bad prime");for(let q=2n;q*q<=p;q++)if(p%q===0n)throw Error("trial prime failed");}
  function lucas(n){
    if(proved.has(n))return;
    const c=certificates[String(n)];
    if(!c)throw Error("missing Lucas node");
    if(c.trial){trial(n);proved.add(n);return;}
    const ps=c.factors.map(BigInt),a=BigInt(c.witness);
    if(product(ps)!==n-1n||ps.some(p=>p<2n||p>=n))throw Error("Lucas factor product");
    for(const p of new Set(ps)){
      lucas(p);
      if(gcd(power(a,(n-1n)/p,n)-1n,n)!==1n)throw Error("Lucas gcd");
    }
    if(power(a,n-1n,n)!==1n)throw Error("Lucas Fermat condition");
    proved.add(n);
  }
  high.slice(0,3).forEach(trial);
  high.slice(3).forEach(lucas);
  const catalog=new Map(low.map(r=>[r.d,r]));
  const unique=new Set();
  let nonempty=0;
  for(let d=1;d<=1260;d++){
    const f=d/Number(gcd(BigInt(d),12n));
    const h=d/Number(gcd(BigInt(d),36n));
    if(!H.has(h)&&!F.has(f))continue;
    const ps=factors(d);
    const carrier=strip(strip((1n<<BigInt(d))-1n,product(ps.map(p=>(1n<<BigInt(d/p))-1n))),fixedS2);
    if(carrier===1n)continue;
    nonempty++;
    const row=catalog.get(d);
    if(d!==1260&&(!row||row.f!==f||BigInt(row.carrier)!==carrier))throw Error("low row mismatch");
    const list=d===1260?high:row.primeFactors.map(BigInt);
    if(product(list)!==carrier)throw Error("carrier not reconstructed exactly at "+d);
    for(const p of list){
      if(unique.has(p)||carrier%p!==0n||gcd(p,fixedS2)!==1n||power(2n,BigInt(d),p)!==1n||
         ps.some(l=>power(2n,BigInt(d/l),p)===1n))throw Error("factor support or exact order");
      unique.add(p);
    }
  }
  if(nonempty!==47||unique.size!==102||proved.size!==34)throw Error("unexpected support or table size");
  return {nonempty,distinct:unique.size,LucasNodes:proved.size};
}


function enumerateTwoW(groups, shift=2, budget=5, alternate=false){
  const A=new Set([1,2,10,11,12,16,17,22,25,26,30,31,32]);
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const H=Object.keys(groups).map(Number).sort((a,b)=>a-b);
  const period=[...H,2,35].reduce((a,b)=>a/gcd(a,b)*b,1);
  const targets=Array.from({length:period},(_,i)=>i).filter(w=>A.has((shift+3*w)%35));
  const basis=targets.map((_,i)=>1n<<BigInt(i));
  const slots=[];
  for(const h of [2,...H]){
    for(let b=0;b<h;b++){
      if(h===2&&b!==1)continue;
      let mask=0n, size=0;
      for(let i=0;i<targets.length;i++)if(targets[i]%h===b){mask|=basis[i];size++;}
      if(size)slots.push({h,b,size,mask});
    }
  }
  slots.sort((a,b)=>b.size-a.size||((a.h-b.h)||(a.b-b.b))*(alternate?-1:1));
  const byPoint=basis.map(p=>slots.map((z,i)=>[z.mask&p,i]).filter(([m])=>m).map(([,i])=>i));
  const pointOrder=basis.map((_,i)=>i).sort((i,j)=>byPoint[i].length-byPoint[j].length||(i-j)*(alternate?-1:1));
  const all=(1n<<BigInt(targets.length))-1n;
  const banned=slots.map((_,i)=>1n<<BigInt(i));
  const used=Object.fromEntries(H.map(h=>[h,0]));
  const path=[], out=new Map(), calls=Array(budget+1).fill(0);
  let prunes=0;
  function visit(open,n,forbidden,sealed){
    calls[budget-n]++;
    if(open===0n){
      const chosen=path.map(i=>slots[i]);
      if(chosen.some((a,i)=>{
        let rest=0n;for(let k=0;k<chosen.length;k++)if(k!==i)rest|=chosen[k].mask;
        return (a.mask&~rest)===0n;
      }))return;
      const keys=chosen.map(z=>[z.h,z.b]).sort((a,b)=>a[0]-b[0]||a[1]-b[1]);
      if(out.has(JSON.stringify(keys)))throw Error("duplicate enumeration");
      out.set(JSON.stringify(keys),keys);
      return;
    }
    if(!n)return;
    if(n===1){
      for(let i=0;i<slots.length;i++){
        if(forbidden&banned[i])continue;
        const row=slots[i];
        if((open&~row.mask)!==0n)continue;
        if(row.h!==2&&used[row.h]>=groups[row.h].length)continue;
        path.push(i);visit(0n,0,forbidden|banned[i],sealed);path.pop();
      }
      return;
    }
    let options;
    for(const i of pointOrder)if((open&basis[i])!==0n){
       options=byPoint[i];break;
    }
    let exclude=forbidden;
    for(const i of options){
      if(exclude&banned[i])continue;
      const r=slots[i];
      if(r.h!==2&&used[r.h]>=groups[r.h].length)continue;
      exclude|=banned[i];
      const left=open&~r.mask;
      // An already chosen slot must retain a private point after adding this one.
      const newSealed=sealed.map(x=>x&~r.mask);
      if(newSealed.some(p=>p===0n)){prunes++;continue;}
      if(r.h!==2)used[r.h]++;
      path.push(i);
      visit(left,n-1,exclude,[...newSealed,open&r.mask]);
      path.pop();
      if(r.h!==2)used[r.h]--;
    }
  }
  visit(all,budget,0n,[]);
  return {period,targets:targets.length,slots:slots.length,calls,prunes,templates:[...out.values()]};
}

function commonTemplates(){
 const A=[1,2,10,11,12,16,17,22,25,26,30,31,32], row=[1,2,3,4,5], shapes=[];
 const one=(f,b)=>[[f],b], s=b=>[[10,70],b];
 const keep=c=>row.filter(k=>k!==c).map(k=>one(7,k));
 const halfs=c=>[c,c+7];
 const rowA=c=>A.filter(a=>a%7===c);
 for(const c of row){
   shapes.push([...keep(c),...halfs(c).map(v=>one(14,v))]);
   if(c===1||c===5)shapes.push([...keep(c),...rowA(c).map(v=>one(35,v))]);
 }
 for(const big of [2,3,4])for(const small of [1,5])
   shapes.push([...row.filter(k=>k!==big&&k!==small).map(k=>one(7,k)),...halfs(big).map(v=>one(14,v)),...rowA(small).map(v=>one(35,v))]);
 const points=Array.from({length:70},(_,i)=>i).filter(i=>A.includes(i%35)&&[1,5].includes(i%7));
 const options=[];
 for(const f of [10,14,35])for(let b=0;b<f;b++){
   const members=points.filter(v=>v%f===b);
   if(members.length===2)options.push({f,b,members});
 }
 function cube(left,path){
   if(left.length===0){
     if(path.filter(x=>x.f===10).length>2||path.filter(x=>x.f===14).length>3)return;
     shapes.push([2,3,4].map(k=>one(7,k)).concat(path.map(({f,b})=>one(f,b))));
     return;
   }
   for(const x of options)if(x.members.includes(left[0])&&x.members.every(v=>left.includes(v)))cube(left.filter(v=>!x.members.includes(v)),[...path,x]);
 }
 cube(points,[]);
 for(const c of row)for(const half of halfs(c)){
   const other=half===c?c+7:c;
   shapes.push([...keep(c),one(14,half),one(28,other),one(28,other+14)]);
 }
 for(const c of [2,3,4])shapes.push([...keep(c),...rowA(c).map(v=>one(35,v))]);
 for(const c of [1,5]){
   const pp=rowA(c);
   for(const half of halfs(c)){
     const other=v=>[v,v+35].find(t=>t%14!==half);
     shapes.push([...keep(c),one(14,half),...pp.map(v=>s(other(v)))]);
     for(const whole of pp)shapes.push([...keep(c),one(14,half),one(35,whole),s(other(pp.find(v=>v!==whole)))]);
   }
   for(const whole of pp){
     const other=pp.find(v=>v!==whole);
     shapes.push([...keep(c),one(35,whole),s(other),s(other+35)]);
   }
 }
 if(shapes.length!==49)throw Error("common family count "+shapes.length);
 return shapes;
}

function countTwoW(lowOrders,localTemplates,eightTemplates,options={}){
 const gcd=(a,b)=>b?gcd(b,a%b):a;
 const primes=lowOrders.flatMap(({f,primeFactors})=>primeFactors.map(q=>({q:BigInt(q),f,h:f/gcd(f,3)})));
 const byF=new Map(),byH=new Map();
 for(const [i,p] of primes.entries()){
   if(!byF.has(p.f))byF.set(p.f,[]);byF.get(p.f).push(i);
   if(!byH.has(p.h))byH.set(p.h,[]);byH.get(p.h).push(i);
 }
 const W=localTemplates.map(t=>t.filter(([h])=>h!==2).map(([h,b])=>byH.get(h).map(i=>[i,(2+3*b)%primes[i].f])));
 const defineEight=eightTemplates.map(t=>t.filter(([f])=>f!==3&&f!==6).map(([f,b])=>byF.get(f).map(i=>[i,b])));
 const E=defineEight.filter((_,i)=>eightTemplates[i].some(([f])=>f===3));
 const EC=defineEight.filter((_,i)=>eightTemplates[i].every(([f])=>f!==3));
 const C=(options.common??[]).map(t=>t.map(([fs,b])=>fs.flatMap(f=>byF.get(f).map(i=>[i,b%f]))));
 const T=Array.from({length:7},(_,k)=>k+1).map(mask=>[
   ...[0,3].map(b=>byH.get(5).map(i=>[i,(2+3*b)%primes[i].f])),
   ...[21,26,31].filter((_,i)=>!(mask&(1<<i))).map(b=>[...byH.get(7),...byH.get(35)].map(i=>[i,(2+3*b)%primes[i].f])),
 ]);
 const domains=primes.map(()=>new Set());
 for(const t of [...W,...E,...EC,...C,...T])for(const s of t)for(const [i,b] of s)domains[i].add(b);
 const ps=primes.map((p,i)=>({...p,old:i,colors:[...domains[i]].sort((a,b)=>a-b)})).filter(p=>p.colors.length);
 const priority=new Map([3,5,7,8,4,6,9,10,12,15,16,20,35,14,28,70].map((h,i)=>[h,i]));
 const isShared=p=>[7,10,35].includes(p.f);
 ps.sort((a,b)=>Number(isShared(b))-Number(isShared(a))||(priority.get(a.h)??100)-(priority.get(b.h)??100)||a.f-b.f||(a.q<b.q?-1:1)*(options.flipPrimeOrder?-1:1));
 const location=new Map(ps.map((p,i)=>[p.old,i]));
 const sharedN=ps.filter(isShared).length;
 const N=ps.length, nodes=[{v:N},{v:N}];
 const uniq=new Map(), memo=new Map(), atoms=new Map();
 const limit=1800000;
 function node(v,ch){
   if(ch.every(a=>a===ch[0]))return ch[0];
   const key=v+":"+ch.join(",");
   const old=uniq.get(key);if(old!==undefined)return old;
   if(nodes.length>limit)throw Error("decision diagram size cap "+nodes.length);
   const n=nodes.length;uniq.set(key,n);nodes.push({v,ch});return n;
 }
 function apply(isAnd,a,b){
   if(a>b)[a,b]=[b,a];
   if(a===b)return a;
   if(a<2)return isAnd?(a===0?0:b):(a===0?b:1);
   const key=(a*2097152+b)*(isAnd?1:-1);
   const known=memo.get(key);if(known!==undefined)return known;
   const x=nodes[a],y=nodes[b],v=Math.min(x.v,y.v);
   const children=Array.from({length:ps[v].colors.length+1},(_,i)=>apply(isAnd,x.v===v?x.ch[i]:a,y.v===v?y.ch[i]:b));
   const result=node(v,children);memo.set(key,result);return result;
 }
 const inverses=new Map();
 function invert(a){
   if(a<2)return 1-a;
   if(inverses.has(a))return inverses.get(a);
   const result=node(nodes[a].v,nodes[a].ch.map(invert));
   inverses.set(a,result);return result;
 }
 function atom(i,b){
   const v=location.get(i), key=v*128+b;
   const old=atoms.get(key);if(old!==undefined)return old;
   const p=ps[v], ch=Array(p.colors.length+1).fill(0);ch[p.colors.indexOf(b)]=1;
   const id=node(v,ch);atoms.set(key,id);return id;
 }
 const slotMemo=new Map();
 function slot(x){
   const key=x.map(([i,b])=>i*128+b).join(",");
   if(!slotMemo.has(key))slotMemo.set(key,x.map(([i,b])=>atom(i,b)).reduce((s,a)=>apply(false,s,a),0));
   return slotMemo.get(key);
 }
 function build(templates,label){
   let id=0,k=0;
   const sorted=[...templates].sort((a,b)=>a.length-b.length);
   for(const t of sorted){
     const pr=t.map(slot).reduce((s,a)=>apply(true,s,a),1);
     id=apply(false,id,pr);
     k++;if(options.progress&&k%25===0)options.progress({label,k,nodes:nodes.length,memo:memo.size});
   }
   return id;
 }

 const e=build(E,"splitEight"),ec=build(EC,"commonEight"),w=build(W,"bothW"),c=build(C,"common");
 if(apply(true,e,invert(w))!==0||apply(true,ec,invert(c))!==0)throw Error("budget-eight escaped low union");
 const w9=apply(true,w,invert(e)),c9=apply(true,c,invert(ec));
 const topGain=T.map(template=>apply(true,template.map(slot).reduce((s,a)=>apply(true,s,a),1),invert(w)));
 const tail=Array(N+1).fill(1n);for(let i=N-1;i>=0;i--)tail[i]=ps[i].q*tail[i+1];
 const weights=new Map();
 function sum(a){
   if(a<2)return BigInt(a);
   if(weights.has(a))return weights.get(a);
   const {v,ch}=nodes[a],p=ps[v];
   let value=0n;
   for(let j=0;j<ch.length;j++){
     const w=j<p.colors.length?2n:p.q-2n*BigInt(p.colors.length);
     value+=w*sum(ch[j])*tail[v+1]/tail[nodes[ch[j]].v];
   }
   weights.set(a,value);return value;
 }

 const pairs=new Map();
 function joint(a,b){
   if(a>b)[a,b]=[b,a];
   const x=nodes[a],y=nodes[b],v=Math.min(x.v,y.v);
   if(a===0)return 0n;
   if(a===1||a===b)return sum(b);
   if(v>=sharedN){
     const n=sum(a)*sum(b)*tail[v], d=tail[x.v]*tail[y.v];
     if(n%d!==0n)throw Error("exclusive supports must multiply integrally");
     return n/d;
   }
   const key=a*2097152+b;
   if(pairs.has(key))return pairs.get(key);
   const p=ps[v];let res=0n;
   for(let j=0;j<=p.colors.length;j++){
     const ca=x.v===v?x.ch[j]:a, cb=y.v===v?y.ch[j]:b;
     const weight=j<p.colors.length?2n:p.q-2n*BigInt(p.colors.length);
     const m=Math.min(nodes[ca].v,nodes[cb].v);
     res+=weight*joint(ca,cb)*(tail[v+1]/tail[m]);
   }
   pairs.set(key,res);return res;
 }
 function mass(a){return sum(a)*(tail[0]/tail[nodes[a].v]);}
 function together(a,b){return joint(a,b)*(tail[0]/tail[Math.min(nodes[a].v,nodes[b].v)]);}
 function frac(n){
   const d=tail[0];
   const gcd=(x,y)=>y?gcd(y,x%y):x;
   const g=gcd(n,d),p=n/g,q=d/g;
   return {numerator:String(p),denominator:String(q),decimalFloor:String(p/q)+"."+String((p%q)*10n**48n/q).padStart(48,"0")};
 }
 const wExact=together(w9,invert(ec)),cExact=together(c9,invert(e)),overlap=together(w9,c9);
 const result={primes:N,sharedN,nodes:nodes.length,calls:memo.size,jointCalls:pairs.size,W9:frac(mass(w)),
   E8:frac(mass(e)+mass(ec)-together(e,ec)),C9:frac(mass(c)),
   exactW:frac(wExact),exactCommon:frac(cExact),overlap:frac(overlap),union:frac(wExact+cExact-overlap),
   gain:topGain.map(a=>frac(together(a,invert(c))))};
 result.jointCalls=pairs.size;
 return result;

}

function exactDensity(count,lowOrders,high){
 const gcd=(a,b)=>b?gcd(b,a%b):a<0n?-a:a;
 const rat=(n,d=1n)=>{const g=gcd(n,d);return [n/g,d/g];};
 const add=(a,b)=>rat(a[0]*b[1]+a[1]*b[0],a[1]*b[1]);
 const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
 const div=(a,b)=>rat(a[0]*b[1],a[1]*b[0]);
 const frac=v=>[BigInt(v.numerator),BigInt(v.denominator)];
 const fmt=a=>{return {numerator:String(a[0]),denominator:String(a[1]),decimalFloor:String(a[0]/a[1])+"."+String(a[0]%a[1]*10n**54n/a[1]).padStart(54,"0")};};
 const product=xs=>xs.reduce((a,b)=>a*b,1n);
 const highDen=product(high);
 let masks=Array(8).fill(0n);masks[0]=1n;
 for(const p of high){
  const next=Array(8).fill(0n);
  for(let m=0;m<8;m++){next[m]+=(p-6n)*masks[m];for(let b=0;b<3;b++)next[m|(1<<b)]+=2n*masks[m];}
  masks=next;
 }
 if(masks.reduce((s,v)=>s+v,0n)!==highDen)throw Error("high weighted partition");
 const gainFactors=count.gain.map(frac);
 let gain=rat(0n);
 for(let h=1;h<8;h++)gain=add(gain,mul(gainFactors[h-1],rat(masks[h],highDen)));
 const G=[],C=[];
 for(const {f,primeFactors} of lowOrders){
   const h=f%3===0?f/3:f;
   if(h===5)C.push(...primeFactors.map(BigInt));
   if(h===7||h===35)G.push(...primeFactors.map(BigInt));
 }
 function occ(ps,n){
  const choose=[[1n],[1n,1n],[1n,2n,1n],[1n,3n,3n,1n]][n];
  let c=0n;
  for(let j=0;j<=n;j++)c+=(j%2?-1n:1n)*choose[j]*product(ps.map(p=>p-2n*BigInt(j)));
  return rat(c,product(ps));
 }
 let top=rat(0n);
 for(let h=1;h<8;h++){
  const k=h.toString(2).replace(/0/g,"").length;
  top=add(top,mul(mul(occ(C,2),occ(G,3-k)),rat(masks[h],highDen)));
 }
 const total=add(frac(count.union),gain), share=div(gain,top);
 const p2=product([...lowOrders.flatMap(o=>o.primeFactors.map(BigInt)),...high]);
 const p1=p2*433n*38737n;
 function size(n){return {decimalDigits:String(n).length,bits:n.toString(2).length,modulus:String(n)};}
 return {gain:fmt(gain),top:fmt(top),gainShare:fmt(share),total:fmt(total),
         oneIn:fmt(rat(total[1],total[0])),highWeights:masks.map(n=>fmt(rat(n,highDen))),
         minimumR2:size(p2),minimumR1:size(p1),
         gainsByHammingWeight:[count.gain[0],count.gain[2],count.gain[6]],sameByWeight:
            [[0,1,3],[2,4,5],[6]].every(g=>g.every(i=>count.gain[i].numerator===count.gain[g[0]].numerator&&count.gain[i].denominator===count.gain[g[0]].denominator))};
}
const verified=verifyCarriers(lowOrders,high,certificates);
const H=new Set([1,2,3,4,5,6,7,8,9,10,12,15,16,20,35]), groups={};
for(const {f,primeFactors} of lowOrders){
  const h=f%3===0?f/3:f;
  if(H.has(h))(groups[h]??=[]).push(...primeFactors);
}
const main=enumerateTwoW(groups), alt=enumerateTwoW(groups,2,5,true);
const names=new Set(main.templates.map(x=>JSON.stringify(x)));
if(main.templates.length!==239||alt.templates.length!==239||alt.templates.some(x=>!names.has(JSON.stringify(x))))throw Error("cover census");
const key=t=>JSON.stringify(t.sort((a,b)=>a[0]-b[0]||a[1]-b[1]));
const small=new Set(main.templates.filter(t=>t.length<=4).map(key));
const projected=new Set(eight.filter(t=>t.some(([f])=>f===3)).map(t=>key(t.filter(([f])=>f!==3).map(([f,b])=>{
 const h=f%3===0?f/3:f;
 return [h,Array.from({length:h},(_,w)=>w).find(w=>(2+3*w)%f===b)];
}))));
if(small.size!==24||projected.size!==24||[...projected].some(k=>!small.has(k)))throw Error("budget eight projection");
const mdd=countTwoW(lowOrders,main.templates,eight,{common:commonTemplates(),flipPrimeOrder:process.argv.includes("--alternate")});
for(const [k,v] of [["E8","E8"],["C9","C9"],["exactCommon","C9_exact_total9"]])
  if(mdd[k].numerator!==pinned[v][0]||mdd[k].denominator!==pinned[v][1])throw Error("pinned density "+k);
const result=exactDensity(mdd,lowOrders,high);
if(!result.sameByWeight||!result.total.decimalFloor.startsWith("0.000000027661088300840075588")||
  result.minimumR2.bits!==3265||result.minimumR1.bits!==3289)throw Error("final exact result");
console.log(JSON.stringify({result,mdd,verified,localTemplates:main.templates.length},null,2));
