const fs=require('node:fs'), o=require('./observer.json'), known=require('./known-factors.json');
for(const [d,q] of [[1120,"16824641"],[6720,"16141441"],[10080,"20161"]])(known[d]??=[]).push(q);
const gcd=(a,b)=>b?gcd(b,a%b):a, limit=10_000_000, sieve=new Uint8Array(limit+1);
for(let p=2;p*p<=limit;++p)if(!sieve[p])for(let q=p*p;q<=limit;q+=p)sieve[q]=1;
const out=[];
for(const [h,rs] of Object.entries(o.orders))for(const [d,carrier] of rs){
 let remaining=BigInt(carrier), found=[], primes=[];
 const strip=p=>{let e=0;while(remaining%p===0n){remaining/=p;e++}return e;};
 for(const q of new Set(known[d]??[]))if(strip(BigInt(q)))primes.push(q);
 for(let q=d+1;q<=limit&&remaining>1n;q+=d)if(q>1&&!sieve[q]&&strip(BigInt(q))){found.push(''+q);primes.push(''+q);}
 out.push({h:+h,d,primes,found,remaining:''+remaining});
}
fs.writeFileSync('r4-twelve-factor-trial.json',JSON.stringify(out,null,2)+'\n');
console.log(out.map(x=>[x.d,x.found]).filter(x=>x[1].length));
console.log({known:out.reduce((s,x)=>s+x.primes.length,0),unfactored:out.filter(x=>x.remaining!=='1').length,limit});
