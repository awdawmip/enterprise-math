#!/usr/bin/env node
"use strict";
function verify(){
const m=(x,n)=>((x%n)+n)%n,gcd=(a,b)=>{while(b)[a,b]=[b,a%b];return a};
const inv=(a,n)=>{for(let x=1;x<n;x++)if(m(a*x,n)===1)return x;throw Error("no inverse")};
const pow=(a,e,n)=>{let v=1;for(let j=0;j<e;j++)v=m(v*a,n);return v};
const p=11,u=m(4822040484,p)*inv(m(8132285009,p),p)%p,gamma=m(141024,p)*inv(m(1653649,p),p)%p;
const i637=inv(m(637,p),p),rows=[];
for(let z=0;z<11;z++){let la=m((637-3*z)*i637,p),lb=m(u*(1+gamma*z),p);rows.push({z,la,lb,aa:m(1-(1-z)*la,p),bb:m(1-(1-z)*lb,p)})}
const c=m(-3*i637,p),d=m(u*gamma,p),P10=new Set();
for(let h=0;h<10;h++)for(let n=0;n<10;n++){
 let ok=rows.filter(r=>r.z!==3).every(r=>m((pow(r.aa,h,p)*pow(r.la,n,p)-pow(r.bb,h,p)*pow(r.lb,n,p))*inv(m(r.la-r.lb,p),p),p)!==0);
 ok=ok&&m((pow(c,h+n,p)-pow(d,h+n,p))*inv(m(c-d,p),p),p)!==0;
 if(ok)P10.add(10*h+n)
}
if(P10.size!==44)throw Error("P10");
const C=(h,n)=>P10.has(10*m(h,10)+m(n,10))&&m(9*h+10*n,11)!==0;
function direct(h,n){
 for(const r of rows){let v;
  if(r.z===3)v=m(pow(r.la,n-1,p)*pow(r.aa,h-1,p)*(n*r.aa-h*(1-r.z)*r.la),p);
  else v=m((pow(r.aa,h,p)*pow(r.la,n,p)-pow(r.bb,h,p)*pow(r.lb,n,p))*inv(m(r.la-r.lb,p),p),p);
  if(!v)return false
 }
 return m((pow(c,h+n,p)-pow(d,h+n,p))*inv(m(c-d,p),p),p)!==0
}
for(let h=1;h<=110;h++)for(let n=1;n<=110;n++)if(C(h,n)!==direct(h,n))throw Error(`projective ${h},${n}`);
const row10=[],table=new Map();
for(let b=0;b<10;b++)for(let a=0;a<10;a++){
 if(gcd(gcd(a,b),10)!==1)continue;
 let h0,n0;outer:for(let h=0;h<10;h++)for(let n=0;n<10;n++)if(m((b-a)*h-a*n+1,10)===0){h0=h;n0=n;break outer}
 let w=Array.from({length:10},(_,t)=>+P10.has(10*m(h0+a*t,10)+m(n0+(b-a)*t,10)));
 let dif=Array.from({length:10},(_,k)=>w.reduce((s,x,t)=>s+(x!==w[m(k-t,10)]),0));
 let D=Math.min(...dif),N=dif.filter(v=>v===D).length,yes=b%2===0&&(a%5===0||m(2*a-b,5)===0);
 if(D!==(yes?0:2))throw Error(`mod10 ${a},${b},${D}`);
 let row={a,b,D,N,weight:w.reduce((x,y)=>x+y,0)};
 row10.push(row);table.set(`${a}|${b}`,row)
}
const count=(rows,fn)=>{let o={};for(const x of rows){let k=fn(x);o[k]=(o[k]||0)+1}return o};
const H10=count(row10,r=>`${r.D}|${r.N}`);
for(const [k,v] of Object.entries({"0|1":8,"2|1":24,"2|2":24,"2|4":16}))if(H10[k]!==v)throw Error(`H10 ${k}`);
const classes=[];
for(let b=0;b<110;b++)for(let a=0;a<110;a++){
 if(gcd(gcd(a,b),110)!==1)continue;
 const r=table.get(`${a%10}|${b%10}`),q=(a+b)%11===0?11:10;
 classes.push({D:r.D*q,N:r.N*(q===11?11:1)});
}
const H110=count(classes,r=>r.D), HN=count(classes,r=>`${r.D}|${r.N}`);
if(classes.length!==8640||H110[0]!==960||H110[20]!==7040||H110[22]!==640)throw Error("H110");
const anchors=[];
for(let b=2;b<=30;b++)for(let a=1;a<b;a++){
 if(gcd(a,b)!==1)continue;
 let T=110*b,L=new Set(),R=new Set();
 for(let q=0;q<T;q++){
  if((a*q-1)%b===0){let h=(a*q-1)/b;if(C(h,q-h))L.add(q)}
  if((a*q+1)%b===0){let h=(a*q+1)/b;if(C(h,q-h))R.add(q)}
 }
 if(L.size!==R.size)throw Error("marginal");
 let q0=inv(a,b),ds=[];
 for(let t=0;t<110;t++){let shift=m(-2*q0+b*t,T),overlap=0;
  for(const q of L)if(R.has((q+shift)%T))overlap++;
  ds.push(L.size+R.size-2*overlap)
 }
 let D=Math.min(...ds),N=ds.filter(x=>x===D).length;
 const r=table.get(`${a%10}|${b%10}`),q=(a+b)%11===0?11:10;
 if(D!==r.D*q||N!==r.N*(q===11?11:1))throw Error(`anchor ${a}/${b}`);
 anchors.push({D,N})
}
if(anchors.length!==277)throw Error("anchors");
return {status:"ALL PASS",projective_checked:12100,P10_cells:44,primitive_mod10:row10.length,mod10_defect_optimal_shift_histogram:H10,primitive_mod110:classes.length,mod110_defect_histogram:H110,mod110_defect_optimal_shift_histogram:HN,direct_rational_anchors:anchors.length,direct_rational_defect_histogram:count(anchors,r=>r.D)}
}
console.log(JSON.stringify(verify(),null,2));
