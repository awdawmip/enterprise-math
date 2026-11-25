const fixedPrimes = ["5","7","11","13","17","19","31","37","41","61","71","73","97","109","113","127","151","181","241","257","281","331","337","433","577","631","641","673","1321","14449","23311","29191","38737","54001","65537","87211","246241","262657","279073","6700417","18837001","29247661","487824887233","29","43","193","211","421","1153","1429","3361","5419","6337","61681","86171","106681","122921","152041","664441","1564921","7416361","15790321","22253377","33975937","47392381","4562284561","38941695937","88959882481","146919792181","168692292721","278452876033","138991501037953","1041815865690181","469775495062434961"].map(BigInt);
const B=[0,3,5,8,10,15,21,23,26,28,30,31,33],fixed=[[2,1],[3,1],[4,2]];
const gcd=(a,b)=>b?gcd(b,a%b):a;
const lcm=(a,b)=>a/gcd(a,b)*b;
const assert=(p,s)=>{if(!p)throw Error(s);};
const A4=427862534250255874142059986311712045208460862156242374709749146714880029585009065541265479726658295808843521086362454718047435496681465110551998259577542161622793500228931578210883591253490428068977896911616949921393222257268332228484808322449966505904395308464777304242195893590213416972267332840402564470159978966396652296385533697227114107008635433673n,S4=555913265364989619697873741372709588670986629522837781333836453228687923187421391074561543226863273773190894562567333918792362053445593573850052370953876739565216134323755512367030826851461448887445240358521194430339039575739758436657254293728498346839912662754165409451691836095700927934351172974265672180517614278948584699085275521666505271546605819230n;
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

function inverse(a,m){
 let x=1n,y=0n,u=(a%m+m)%m,v=m;
 while(v){const d=u/v;[u,v]=[v,u-d*v];[x,y]=[y,x-d*y];}
 assert(u===1n,'inverse');return (x%m+m)%m;
}
function crt(a,m,b,n){
 if(n===1n)return [a,m];
 return [a+m*((((b-a)%n+n)%n)*inverse(m,n)%n),m*n];
}
function rootCat(w,n){return powmod(inverse(2n,n),16+18*w,n)}





const picks=[
 [14,0,504,1009n],[14,10,504,21169n],[20,0,80,4278255361n],[20,8,240,394783681n],
 [280,236,1120,16824641n],[560,376,2240,primitive(2240)],[1120,656,4480,primitive(4480)],
 [2240,96,8960,primitive(8960)],[2240,1216,26880,primitive(26880)]
];
const target=[1120,96,40320,primitive(40320)];
const active=[...picks,target];
for(const [h,b,d,q] of active){
 assert(d/gcd(d,36)===h&&q>1n&&primitive(d)%q===0n,'period layer');
 assert(powmod(2n,d,q)===1n,'carrier target power');
 if(q<10000000000n)assert(trialPrime(Number(q)),'named prime');
}
assert(active.every((x,i)=>active.every((y,j)=>i===j||bigGcd(x[3],y[3])===1n)),'coprime layers');
const period=active.reduce((p,[h])=>lcm(p,h),420);
const D=Array.from({length:period},(_,w)=>w).filter(w=>B.includes(w%35));
function min(xs){
 const terms=[...fixed,...xs.map(([h,b])=>[h,b])];
 const masks=terms.map(([h,b])=>D.reduce((r,w,i)=>w%h===b?r|(1n<<BigInt(i)):r,0n));
 const full=(1n<<BigInt(D.length))-1n;
 let best=terms.length+1, chosen=[];
 for(let p=0;p<1<<masks.length;p++){
  let r=0n,k=0;
  for(let i=0;i<masks.length;i++)if(p>>i&1){k++;r|=masks[i];}
  if(r===full&&k<best){best=k;chosen=terms.filter((_,i)=>p>>i&1);}
 }
 return {best,chosen};
}
const on=min(active),off=min(picks);
assert(on.best===10&&off.best===11,'tail 10/11');
const compatible=active.every(([h,b,d,q])=>{
 const f=d/gcd(d,12);return f!==11&&f!==22&&bigGcd(q,S4)===1n;
});
assert(compatible,'none of these coordinates can realize shared fourteen dictionary');
const fields=active.map(([h,b,d,q])=>({h,b,d,carrier:q.toString(),residue:rootCat(b,q).toString()}));
console.log(JSON.stringify({period,holes:D.length,on,off,fields},null,2));
