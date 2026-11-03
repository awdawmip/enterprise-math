/* PREFIX-475 pure-run-gate BRC exact BigInt certificate, no external packages. */
"use strict";
const ORD="aAbBcCdDeE", WG=[6n,1n,12n,1n,18n,1n,24n,1n,36n,1n];
const ACO=[0,1,0,2,1], CCO=[0,0,1,0,1], Z=Array(9).fill(0);
function step(st,c,k){
 let a=st.slice();if(c==="x"){a[0]++;a[8]=0;return a}
 const ix=ORD.indexOf(c), ax=Math.floor(ix/2),sgn=ix%2===0?1:-1,y=a[ax+1];a[ax+1]+=sgn;
 if(sgn*y<0){a[6]+=ACO[ax];a[7]+=CCO[ax]}
 a[8]=c==="a"?Math.min(k,a[8]+1):0;return a;
}
function baseKey(st){return st.slice(0,8).join(",")}
function wkey(s){return s.join(",")}
function padBase(key,j,k){let s=key.split(",").map(Number).concat([0]);for(let i=0;i<j;i++)s=step(s,"a",k);return baseKey(s)}
function pure(word,k){let s=Z;for(const c of word)s=step(s,c,k);return baseKey(s)}
function mulPoly(a,b){let c=Array(a.length+b.length-1).fill(0);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return c}
function choose(n,r){if(n<r||r<0)return 0n;let a=1n;for(let i=1;i<=r;i++)a=a*BigInt(n-r+i)/BigInt(i);return a}
function B(n,k){if(n<0)return 0;let w=Array(k+2).fill(0);w[0]=1;w[1]=1;w[k+1]=-1;let num=mulPoly(mulPoly([1,0,2],[1,2,1]),w);let ans=0n;for(let i=0;i<num.length;i++)if(num[i])for(let t=0;n-i-(k+1)*t>=0;t++)ans+=BigInt(num[i])*choose(n-i-(k+1)*t+7,7);return Number(ans)}
function u(n,k){return Number(n>=1)+Number(n>=2&&n<=k)}
function E(n,k,r){return Number(n>=r+1)+Number(n>=r+2&&n<=k)}
function N(n,k,h){if(h===0)return B(n,k);if(h>=k){let z=0;for(let j=0;j<=k;j++)z+=B(n-j,k);for(let j=0;j<k;j++)z-=u(n-j,k);return z}let r=k-h,z=B(n,k)-E(n,k,r)+B(n-k,k);for(let j=r+1;j<k;j++)z+=B(n-j,k)-u(n-j,k);return z}
function direct(n,k){const out=new Map();function visit(word){if(word.length===n){
 const st=Array(9).fill(0);st[0]=word.split("x").length-1;let cnt=Array.from({length:5},()=>[0,0]);
 for(let ch of word){let t=ORD.indexOf(ch);if(t>=0)cnt[Math.floor(t/2)][t%2]++}
 for(let i=0;i<5;i++){st[i+1]=cnt[i][0]-cnt[i][1];st[6]+=ACO[i]*Math.min(...cnt[i]);st[7]+=CCO[i]*Math.min(...cnt[i])}
 for(let i=word.length-1;i>=0&&word[i]==="a";i--)st[8]++;st[8]=Math.min(k,st[8]);
 let mass=1n;for(const ch of word){const t=ORD.indexOf(ch);mass*=t>=0?WG[t]:1n}
 const key=wkey(st),cur=out.get(key)||[0n,0n];out.set(key,[cur[0]+1n,cur[1]+mass]);return;
 }
 for(const ch of ORD)visit(word+ch);if(word.length===0||word.endsWith("a".repeat(k)))visit(word+"x");
 }visit("");return out}
function ck(x,msg){if(!x)throw Error(msg)}
function run(){
 const log=[];for(let k=1;k<=4;k++){
 let cur=new Map([[wkey(Z),[1n,1n]]]),bases=[],cnts=[],masses=[],totalstates=0;
 for(let n=0;n<=8;n++){
 const supp=Array.from({length:k+1},()=>new Set()),histCount=Array(k+1).fill(0n),histMass=Array(k+1).fill(0n);
 let all=new Set();for(const [key,v] of cur){let a=key.split(",").map(Number),f=baseKey(a);supp[a[8]].add(f);all.add(f);histCount[a[8]]+=v[0];histMass[a[8]]+=v[1]}
 bases.push(all);totalstates+=cur.size;ck(all.size===B(n,k),"B k="+k+" n="+n);
 let excluded=new Set();if(n>=1)excluded.add(pure("a".repeat(n),k));if(n>=2&&n<=k)excluded.add(pure("x"+"a".repeat(n-1),k));
 ck(supp[0].size===all.size-excluded.size && [...all].every(x=>supp[0].has(x)===!excluded.has(x)),"q0 k="+k+" n="+n);
 for(let j=1;j<k;j++){
 let expected=new Set();if(n>=j){let m=n-j;let missing=new Set();if(m>=1)missing.add(pure("a".repeat(m),k));if(m>=2&&m<=k)missing.add(pure("x"+"a".repeat(m-1),k));
 for(const f of bases[m])if(!missing.has(f))expected.add(padBase(f,j,k));}
 ck(expected.size===supp[j].size&&[...expected].every(x=>supp[j].has(x)),"q"+j+" k="+k+" n="+n);
 ck(supp[j].size===B(n-j,k)-u(n-j,k),"q_count k="+k+" n="+n+" j="+j);
 }
 if(n>=k){let expected=new Set([...bases[n-k]].map(f=>padBase(f,k,k)));ck(expected.size===supp[k].size&&[...expected].every(x=>supp[k].has(x)),"qfull k="+k+" n="+n)}else ck(supp[k].size===0,"qfull edge");
 for(let h=0;h<=k+1;h++){
 const r=k-h,classes=new Set();
 for(const key of cur.keys()){let st=key.split(",").map(Number);classes.add(baseKey(st)+":"+(h===0?"N":st[8]>r?st[8]:"L"))}
 ck(classes.size===N(n,k,h),"N k="+k+" n="+n+" h="+h+" actual="+classes.size+" calc="+N(n,k,h));
 if(h>0&&h<=k){let low=new Set(supp.slice(0,r+1).flatMap(z=>[...z])),exc=new Set();if(n>=r+1)exc.add(pure("a".repeat(n),k));if(n>=r+2&&n<=k)exc.add(pure("x"+"a".repeat(n-1),k));
 ck(low.size===all.size-exc.size&&[...all].every(f=>low.has(f)===!exc.has(f)),"low_support k="+k+" n="+n+" h="+h)}
 }
 let ct=histCount.reduce((a,b)=>a+b,0n),mt=histMass.reduce((a,b)=>a+b,0n);cnts.push(ct);masses.push(mt);
 let prev=i=>i<0?0n:cnts[i],prevm=i=>i<0?0n:masses[i];
 if(n>=1){ck(ct===10n*prev(n-1)+(n===1?1n:n>=k+1?prev(n-k-1):0n),"count-series k="+k+" n="+n);
 ck(mt===101n*prevm(n-1)+(n===1?1n:n>=k+1?6n**BigInt(k)*prevm(n-k-1):0n),"mass-series k="+k+" n="+n)}
 for(let j=0;j<k;j++){
 ck(histCount[j]===prev(n-j)-prev(n-j-1),"suffix-count k="+k+" n="+n+" j="+j);
 let a=prevm(n-j)-6n*prevm(n-j-1);ck(histMass[j]===6n**BigInt(j)*a,"suffix-mass k="+k+" n="+n+" j="+j)}
 ck(histCount[k]===prev(n-k)&&histMass[k]===6n**BigInt(k)*prevm(n-k),"suffix-full k="+k+" n="+n);
 if(n<=4){let ord=direct(n,k);ck(ord.size===cur.size,"direct-size k="+k+" n="+n);for(const [key,val] of ord){let a=cur.get(key);ck(a&&a[0]===val[0]&&a[1]===val[1],"direct-hist k="+k+" n="+n)}}
 if(n===8){log.push("k="+k+" n=8 B="+all.size+" supports="+supp.map(s=>s.size).join(",")+" F="+cur.size+" N="+Array.from({length:k+1},(_,h)=>N(n,k,h)).join(",")+" paths="+ct+" mass="+mt);break}
 const nxt=new Map();const add=(st,count,mass)=>{let key=wkey(st),old=nxt.get(key);if(old){old[0]+=count;old[1]+=mass}else nxt.set(key,[count,mass])};
 for(const [key,[c,m]] of cur){let st=key.split(",").map(Number);for(let i=0;i<10;i++)add(step(st,ORD[i],k),c,m*WG[i]);if(n===0||st[8]===k)add(step(st,"x",k),c,m)}
 cur=nxt;
 }
 log.push("CERTIFICATE k="+k+" n=0..8 checked_tagged_states="+totalstates+" direct_ordered_n=0..4");
 }
 log.push("UNIVERSAL_PROOF_IN_PAPER; EXACT_FINITE_CHECKS_ALL_PASS");log.push("ALL_CHECKS_PASS");return log.join("\n")+"\n";
}
if(typeof module!=="undefined"&&require.main===module)console.log(run());
