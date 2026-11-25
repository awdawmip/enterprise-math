
const gcd=(a,b)=>b?gcd(b,a%b):a;
const assert=(v,m)=>{if(!v)throw Error(m);};
const fraction=(num,den)=>{const g=gcd(num,den);return [num/g,den/g];};
const compare=(a,b)=>a[0]*b[1]-a[1]*b[0];
const fmt=a=>a[0]+'/'+a[1];
const phi=new Map();
function C(d){if(!phi.has(d)){let n=(1n<<BigInt(d))-1n;for(let j=1;j<d;j++)if(d%j===0)n/=C(j);phi.set(d,n);}return phi.get(d);}
function prime(q){for(let p=2n;p*p<=q;p++)if(q%p===0n)return false;return q>=2n;}
const inventory={
 11:[23,89],13:[8191],22:[683],26:[2731],27:[262657],33:[599479],
 44:[397,2113],52:[53,157,1613],54:[3,87211],64:[641,6700417],
 66:[67,20857],80:[4278255361],88:[353,2931542417],108:[246241,279073],
 132:[312709,4327489],240:[394783681,46908728641],264:[7393,1761345169,98618273953]
};
for(const [d,pr] of Object.entries(inventory)){
 const q=pr.map(BigInt);
 assert(q.every(prime)&&q.reduce((a,b)=>a*b,1n)===C(+d),'proof of cyclotomic factors '+d);
}
const K=[36,23,11,7,6,4,2,1],gs=[1,3,5,7,15,21,35,105];
assert([17,33,25,28,45,42,35,105].every((e,i)=>5*K[i]*gs[i]<=11*e),'new generic cap');
const scaleBoth=143n*4752n;
let mBoth=[0n,1n], mSingle=[0n,1n], bothCase=[], singleCase=[],nBoth=0,nSingle=0;
for(let j=0;j<=3;j++)for(let k=0;k<=2;k++)for(let w=0;w<=2;w++){
 const rem=BigInt(14-j-k-w), p=BigInt((11-j)*(13-k));
 const c=scaleBoth*p/(143n*16n),r=scaleBoth*23n/396n;
 const top=scaleBoth*(143n-p)/143n+scaleBoth*p*13n*BigInt(w)/(143n*108n)+rem*(c>r?c:r);
 const f=fraction(top,scaleBoth);
 if(compare(f,mBoth)>0n){mBoth=f;bothCase=[j,k,w];}
 nBoth++;
}
const s=143n*1980n;
for(let j=0;j<=5;j++)for(let k=0;k<=5;k++)for(let w=0;w<=2;w++)for(let r=0;r<=1;r++)for(let z=0;z<=1;z++)for(let y=0;y<=1;y++){
 const rem=13-j-k-w-r-z-y;if(rem<0)continue;
 const p=BigInt((11-j)*(13-k));
 const c=s*p*11n/(143n*5n),f=s*23n/11n;
 const a=s*36n*(143n-p)/143n+s*p*(BigInt(w)*13n*6n+BigInt(r)*23n*3n)/(143n*18n)
       +s*p*BigInt(z)*11n/(143n*4n)+s*p*BigInt(y)*23n/(143n*9n);
 const top=fraction(a+BigInt(rem)*(c>f?c:f),s);
 if(compare(top,mSingle)>0n){mSingle=top;singleCase=[j,k,w,r,z,y];}
 nSingle++;
}
assert(compare(mBoth,[1n,1n])<0n&&compare(mSingle,[36n,1n])<0n,'strict caps');
const coScale=11n*572n;
const ties=[];let noTie=[0n,1n],nShared=0;
for(let j=0;j<=10;j++)for(let z=0;z<=3;z++){
 const rem=12-j-z;if(rem<0)continue;
 const D=BigInt(11-j);
 const c=coScale*D/(11n*13n),f=coScale/22n;
 const a=coScale*BigInt(j)/11n+coScale*D*BigInt(z)*5n/(11n*52n)+BigInt(rem)*(c>f?c:f);
 if(a===coScale)ties.push([j,z]);
 else if(compare(fraction(a,coScale),noTie)>0n)noTie=fraction(a,coScale);
 assert(a<=coScale,'shared mass cap');
 nShared++;
}
assert(JSON.stringify(ties)==='[[10,0]]','unique shared equality');
const s11=[11,22,33,44,66,132].flatMap(d=>inventory[d]).map(BigInt);
const s22=[88,264].flatMap(d=>inventory[d]).map(BigInt);
const mul=xs=>xs.reduce((a,b)=>a*b,1n);
const h11=11n*mul(Array.from({length:10},(_,j)=>BigInt(j+1)))*2n**10n;
const d11=mul(s11),d22=mul(s22);
const h22=d22-2n*mul(s22.map(q=>q-2n))+mul(s22.map(q=>q-4n));
const density=fraction(h11*h22,d11*d22);
const dec=(n,d,k=85)=>{
 const a=String(n*10n**BigInt(k)/d).padStart(k+1,'0');
 return a.slice(0,-k)+'.'+a.slice(-k);
};
const report={both:{max:fmt(mBoth),case:bothCase,nBoth},one:{max:fmt(mSingle),case:singleCase,nSingle},shared:{ties,nextMax:fmt(noTie),nShared,primes:s22.map(String),density:fmt(density),decimal:dec(...density),phaseDictionaries:String(11n*mul(Array.from({length:10},(_,j)=>BigInt(j+1)))*20n)}};

console.log(JSON.stringify(report,null,2));
