#!/usr/bin/env node
"use strict";
/* PREFIX-463 exact native eleven-letter BRC weight signature certificate. */
function ok(a,msg){if(!a)throw Error(msg||"ASSERT");}
function fact(n){let r=1n;for(let i=2;i<=n;i++)r*=BigInt(i);return r;}
function* comps(k,n,p=[]){if(k===1){yield p.concat(n);return;}for(let j=0;j<=n;j++)yield* comps(k-1,n-j,p.concat(j));}
function add(M,k,x){M.set(k,(M.get(k)||0n)+x);}
function factors(x){let a=x,z={};for(let p=2;p*p<=a;p++)while(a%p===0){z[p]=(z[p]||0)+1;a/=p;}if(a>1)z[a]=(z[a]||0)+1;return z;}
function rank(B){if(!B.length)return 0;let a=B.map(row=>row.map(BigInt)),r=0;
 for(let j=0;j<a[0].length;j++){let q=a.findIndex((row,i)=>i>=r&&row[j]!==0n);if(q<0)continue;
 [a[r],a[q]]=[a[q],a[r]];let v=a[r][j];for(let i=r+1;i<a.length;i++){let u=a[i][j];if(!u)continue;
 for(let h=j;h<a[i].length;h++)a[i][h]=v*a[i][h]-u*a[r][h];}r++;if(r===a.length)break;}return r;}
function matrix(rho){let cols=rho.slice(1).map(x=>factors(x/rho[0]));
 let primes=[...new Set(cols.flatMap(x=>Object.keys(x)))].map(Number).sort((a,b)=>a-b);
 let B=primes.map(p=>cols.map(c=>c[p]||0));return {primes,B,rank:rank(B)};}
function occupation(m,rho){let out=new Map(),F=Array.from({length:m+1},(_,i)=>fact(i)),n=0;
 for(let c of comps(11,m)){n++;let point=[c[0]],w=5n**BigInt(c[0]),a=F[m];
 for(let j=0;j<5;j++){point.push(c[2*j+1]-c[2*j+2]);w*=BigInt(rho[j])**BigInt(c[2*j+2]);}
 for(let v of c)a/=F[v];add(out,point.join(",")+"|"+w,a);
 }return {out,n};}
function dynamic(m,rho){let cur=new Map([["0,0,0,0,0,0|1",1n]]),moves=[[[1,0,0,0,0,0],5n]];
 for(let j=1;j<=5;j++){let p=[0,0,0,0,0,0],n=p.slice();p[j]=1;n[j]=-1;moves.push([p,1n],[n,BigInt(rho[j-1])]);}
 for(let step=0;step<m;step++){let nxt=new Map();
 for(let [key,a] of cur){let [pos,w]=key.split("|"),v=pos.split(",").map(Number);
 for(let [d,b] of moves)add(nxt,v.map((x,j)=>x+d[j]).join(",")+"|"+(BigInt(w)*b),a);}cur=nxt;}return cur;}
function signatures(rho){let {primes,B,rank:r}=matrix(rho), seen=new Map(),back=new Map(),checked=0,merged=0;
 for(let p=0;p<=4;p++)for(let pi of comps(5,p)){let u=pi.slice(1);
 let v=B.map(row=>row.reduce((x,c,j)=>x+c*u[j],0)), sig=p+"|"+v.join(",");
 let w=pi.reduce((a,c,j)=>a*BigInt(rho[j])**BigInt(c),1n), val=p+"|"+w;
 if(seen.has(sig)){ok(seen.get(sig)===val);merged++;}else seen.set(sig,val);
 if(back.has(val))ok(back.get(val)===sig);else back.set(val,sig);
 let decoded=BigInt(rho[0])**BigInt(p);
 for(let j=0;j<primes.length;j++)decoded*=BigInt(primes[j])**BigInt(v[j]);
 ok(decoded===w);checked++;
 }return {primes,rank:r,checked,merged};}
function run(){let log=[],families={
 rank0:[6,6,6,6,6],rank1:[6,12,24,48,96],
 rank2:[6,12,18,24,36],rank4:[6,12,18,30,42]};
 for(let [name,rho] of Object.entries(families)){
 let t=signatures(rho);ok(t.rank===Number(name.slice(4)));
 log.push("FAMILY "+name+" primes="+t.primes+" rank="+t.rank+" signatures="+t.checked+" collisions="+t.merged);
 for(let m=0;m<=6;m++){let {out,n}=occupation(m,rho),w=dynamic(m,rho);
 ok(out.size===w.size,"states");let words=0n;
 for(let [key,val] of out)ok(w.get(key)===val,"hist "+name+" "+m+" "+key);
 for(let a of w.values())words+=a;ok(words===11n**BigInt(m),"mass");
 log.push("PASS "+name+" m="+m+" occupations="+n+" weighted_states="+w.size+" words="+words);}
 }
 let rho=families.rank2,a=[0,2,0,0,0],b=[1,0,0,1,0];
 let wt=x=>x.reduce((w,c,j)=>w*BigInt(rho[j])**BigInt(c),1n);
 let mult=x=>24n/x.reduce((d,c)=>d*fact(c)**2n,1n);
 ok(wt(a)===144n&&wt(b)===144n&&mult(a)===6n&&mult(b)===24n);
 log.push("COLLISION m=4 endpoint=(0,0,0,0,0,0) A="+a+" B="+b+" weight=144 counts=6,24");
 log.push("ALL_CHECKS_PASS");return log.join("\n");
}
if(typeof require!=="undefined"&&require.main===module)console.log(run());
