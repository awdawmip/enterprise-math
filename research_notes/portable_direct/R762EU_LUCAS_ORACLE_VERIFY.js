/* R762EU exact positive six-named-terminal BRC oracle and validation.
   Run: node R762EU_LUCAS_ORACLE_VERIFY.js [R762EU_Q9_PACKED_TRITS.hex]
   No floating point, trigonometry or physical signed-event model. */
"use strict";
const S=[[0,0,0],[1,0,0],[0,0,1],[1,1,0],[0,1,1],[1,1,1]];
const ix=(q,x,y,z)=>(x*q+y)*q+z;
const K=Array.from({length:3},()=>new Uint8Array(27));K[0][0]=1;
for(let d=1;d<=2;d++)for(let x=0;x<d;x++)for(let y=0;y<d;y++)for(let z=0;z<d;z++){
 const v=K[d-1][ix(3,x,y,z)];if(!v)continue;
 for(const [a,b,c] of S){const k=ix(3,x+a,y+b,z+c);K[d][k]=(K[d][k]+v)%3}
}
function digit(r,x,y,z){
 let t=1;while(r||x||y||z){
  t=(t*K[r%3][ix(3,x%3,y%3,z%3)])%3;
  r=Math.floor(r/3);x=Math.floor(x/3);y=Math.floor(y/3);z=Math.floor(z/3);
 }return t;
}
function digitBig(r,x,y,z){
 let t=1;while(r||x||y||z){
  t=(t*K[Number(r%3n)][ix(3,Number(x%3n),Number(y%3n),Number(z%3n))])%3;
  r/=3n;x/=3n;y/=3n;z/=3n;
 }return t;
}
function direct(q,maxn,M){
 let a=new Uint16Array(q**3);a[0]=1;let rows=[];
 for(let n=0;n<=maxn;n++){
  const pow=3**Math.max(0,Math.floor(3*n/q)-2);
  if(pow>=M)throw Error("insufficient modulus");
  let t=new Uint8Array(q**3);
  for(let i=0;i<t.length;i++){
   if(a[i]%pow)throw Error("not divisible q="+q+" n="+n);
   t[i]=(a[i]/pow)%3;
  }rows.push(t);if(n===maxn)break;
  let b=new Uint16Array(q**3);
  for(let x=0;x<q;x++)for(let y=0;y<q;y++)for(let z=0;z<q;z++){
   let v=a[ix(q,x,y,z)];if(!v)continue;
   for(const [dx,dy,dz] of S){
    const j=ix(q,(x+dx)%q,(y+dy)%q,(z+dz)%q);b[j]=(b[j]+v)%M;
   }
  }a=b;
 }return rows;
}
function pack(rows){
 if(rows.length!==26)throw Error("need exactly 26 q9 shadows");
 const table=new Uint8Array(26*146);
 for(let m=0;m<26;m++)for(let i=0;i<729;i+=5){
  let t=0,p=1;
  for(let j=0;j<5&&i+j<729;j++){t+=p*rows[m][i+j];p*=3}
  table[m*146+Math.floor(i/5)]=t;
 }return table;
}
const toHex=table=>Array.from(table,b=>b.toString(16).padStart(2,"0")).join("");
function fromHex(hex){
 hex=hex.trim();if(hex.length!==7592||!/^[0-9a-f]+$/i.test(hex))throw Error("bad table hex");
 const t=new Uint8Array(3796);for(let i=0;i<t.length;i++)t[i]=parseInt(hex.slice(i*2,i*2+2),16);return t;
}
function entry(table,row,cell){
 return Math.floor(table[row*146+Math.floor(cell/5)]/(3**(cell%5)))%3;
}
function validateQ(q){q=BigInt(q);if(q<9n)throw Error("q must >=9");
 let r=q;while(r%3n===0n)r/=3n;if(r!==1n)throw Error("q not 3^a");
 return q;
}
function oracleBig(q,n,x,y,z,table){
 q=validateQ(q);n=BigInt(n);x=BigInt(x);y=BigInt(y);z=BigInt(z);
 if(n<0n||x<0n||y<0n||z<0n||x>=q||y>=q||z>=q)throw Error("bad query");
 if(table.length!==3796)throw Error("bad table bytes");
 const h=q/9n,m=n/h,r=n%h;
 const row=m<8n?Number(m):8+Number((m-8n)%18n);
 const cell=ix(9,Number(x/h),Number(y/h),Number(z/h));
 return (entry(table,row,cell)*digitBig(r,x%h,y%h,z%h))%3;
}
const count=row=>{
 let o=0,t=0;for(const v of row){if(v===1)o++;else if(v===2)t++}
 return [o,t];
};
function signature(q,n,counts){
 q=validateQ(q);n=BigInt(n);if(n<0n)throw Error("bad exponent");
 const h=q/9n,m=n/h,i=m<8n?Number(m):8+Number((m-8n)%18n);
 let r=n%h,[a,b]=counts[i],A=BigInt(a+b),D=BigInt(a-b);
 while(r){const k=Number(r%3n);A*=BigInt([1,6,18][k]);D*=BigInt([1,6,-6][k]);r/=3n}
 return {support:A,one:(A+D)/2n,two:(A-D)/2n};
}
function verify(){
 const nine=direct(9,26,2187),q27=direct(27,78,2187);
 const table=pack(nine.slice(0,26)),counts=nine.slice(0,26).map(count);
 const support=K.map(v=>v.reduce((a,b)=>a+Number(b!==0),0));
 if(support.join(",")!=="1,6,18"||count(K[2]).join(",")!=="6,12"||K[2][ix(3,1,1,1)]!==0)throw Error("digit kernel wrong");
 let localChecks=0;
 for(let r=0;r<=14;r++){
  let p=new Map([["0,0,0",1]]);
  for(let n=0;n<r;n++){
   const next=new Map();
   for(const [key,value] of p)for(const v of S){
    const t=key.split(",").map((x,j)=>Number(x)+v[j]).join(",");
    next.set(t,((next.get(t)||0)+value)%3);
   }p=next;
  }
  for(let x=0;x<=r;x++)for(let y=0;y<=r;y++)for(let z=0;z<=r;z++){
   localChecks++;
   if(digit(r,x,y,z)!==(p.get([x,y,z].join(","))||0))throw Error("digit Lucas mismatch");
  }
 }
 let cells=0,bigChecks=0,samples=[];
 for(let n=0;n<=78;n++){
  let r=n%3,m=Math.floor(n/3),A=0,B=0;
  for(let x=0;x<27;x++)for(let y=0;y<27;y++)for(let z=0;z<27;z++){
   const actual=q27[n][ix(27,x,y,z)];
   const predicted=(nine[m][ix(9,Math.floor(x/3),Math.floor(y/3),Math.floor(z/3))]*digit(r,x%3,y%3,z%3))%3;
   if(actual!==predicted)throw Error("q27 mismatch n="+n+" xyz="+[x,y,z]);
   cells++;if(actual===1)A++;else if(actual===2)B++;
   if((n%9===0||n===78)&&((31*x+17*y+z)%53===0)){
    bigChecks++;
    if(oracleBig(27n,BigInt(n),BigInt(x),BigInt(y),BigInt(z),table)!==actual)throw Error("BigInt mismatch");
   }
  }
  const sig=signature(27n,BigInt(n),counts);
  if(sig.support!==BigInt(A+B)||sig.one!==BigInt(A)||sig.two!==BigInt(B))throw Error("support mismatch");
  if([23,24,25,26,27,28,30,50,51,54,78].includes(n))samples.push({n,support:A+B,one:A,two:B});
 }
 if(!nine[8].every((v,i)=>v===nine[26][i]))throw Error("q9 endpoint period witness failed");
 if(!nine[7].some((v,i)=>v!==nine[25][i]))throw Error("q9 transient witness failed");
 return {report:{
  status:"PASS",six_branch_source:S,kernel_support:support,kernel2_ones:6,kernel2_twos:12,
  exact_unwrapped_digit_checks:localChecks,exact_q27_full_coefficient_checks:cells,
  big_integer_oracle_checks:bigChecks,full_support_sign_checks:79,
  q9_shadow_support_0_to_25:counts.map(a=>a[0]+a[1]),q27_samples:samples,
  q9_boundary:{S9_8_eq_S9_26:true,S9_7_neq_S9_25:true},
  q9_rows:26,each_row_trits:729,row_bytes:146,packed_bytes:table.length,
  arithmetic:"named-branch modular integer convolution, modulus 3^7 = 2187",
  q9_n_range:[0,26],q27_n_range:[0,78],
  dependencies:"R762ER normalized lift; R762ET exact eventual q9 period; both NOT_REVIEWED",
  scope:"complete 3-coordinate positive terminal BRC; not primitive signed Cell/Link/Port dynamics"
 },packedHex:toHex(table)};
}
if(typeof module!=="undefined"&&module.exports)
 module.exports={S,K,digit,digitBig,direct,pack,toHex,fromHex,oracleBig,signature,verify};
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module){
 const a=verify();
 if(process.argv[2]){
  const fs=require("fs");
  if(a.packedHex!==fs.readFileSync(process.argv[2],"utf8").trim())throw Error("published hex table differs");
 }
 console.log(JSON.stringify(a.report,null,2));
}
