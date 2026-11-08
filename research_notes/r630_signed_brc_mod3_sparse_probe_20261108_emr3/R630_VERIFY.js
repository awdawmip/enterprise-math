const run = function R630_RUN(){
 const ok=(x,s)=>{if(!x)throw Error("R630: "+s)};
 const choose=(n,k)=>{if(n<0||k<0||k>n)return 0n;let z=1n;for(let i=1;i<=Math.min(k,n-k);i++)z=z*BigInt(n-i+1)/BigInt(i);return z};
 const trim=a=>{a=a.slice();while(a.length>1&&a.at(-1)===0n)a.pop();return a.length?a:[0n]};
 const add=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
 const neg=a=>a.map(v=>-v),sub=(a,b)=>add(a,neg(b)),scale=(a,n)=>trim(a.map(v=>v*n));
 const mul=(a,b)=>{let v=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)v[i+j]+=a[i]*b[j];return trim(v)};
 const sh=(a,n)=>Array(n).fill(0n).concat(a),jet=(a,d)=>trim(a.slice(0,d+1).length?a.slice(0,d+1):[0n]);
 const same=(a,b)=>{a=trim(a);b=trim(b);return a.length===b.length&&a.every((v,j)=>v===b[j])};
 const nu3=a=>{for(let i=0;i<a.length;i++)if(a[i]%3n!==0n)return i;return Infinity};
 const K=i=>{let d=[-choose(4,i)+choose(2,i-1),choose(5,i-1)-choose(5,i-2),choose(7,i-2),-choose(9,i-3)],z=[0n];for(let k=1;k<=4;k++){let n=i+1-k;if(n>=0&&d[k-1]!==0n)z=add(z,sh(Array.from({length:n+1},(_,j)=>-d[k-1]*choose(n,j)),i-1))}return z};
 const arr=Array.from({length:12},(_,j)=>K(j+1)),P=arr.filter((_,j)=>j%2===0),M=arr.filter((_,j)=>j%2===1),D=P.map((p,j)=>sub(p,M[j]));
 const v3=D.map(nu3);
 ok(v3.join(",")==="0,2,7,6,8,11","mod 3 valuation signatures");
 const gg=(a,b)=>{a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t}return a};
 const xgcd=(a,b)=>{let [r0,r1,s0,s1,t0,t1]=[a,b,1n,0n,0n,1n];while(r1!==0n){let q=r0/r1;[r0,r1]=[r1,r0-q*r1];[s0,s1]=[s1,s0-q*s1];[t0,t1]=[t1,t0-q*t1]}return [r0,s0,t0]};
 const bezout=cs=>{let g=0n,coeff=[];for(let c of cs){let [d,u,v]=xgcd(g,c);coeff=coeff.map(z=>z*u);coeff.push(v);g=d}return {g,coeff}};
 const perms=[];const rec=(a,k)=>{if(k===6){perms.push(a.slice());return}for(let j=k;j<6;j++){[a[k],a[j]]=[a[j],a[k]];rec(a,k+1);[a[k],a[j]]=[a[j],a[k]]}};rec([0,1,2,3,4,5],0);
 ok(perms.length===720,"perms");
 const Lof=h=>{let L=1;while(L<=h)L*=3;return L};
 const checks={integral_binomial_gcd_h0_to_80:0,full_orientation_two_probe:0,one_probe_zero_fiber:0,sharp_jet_collision:0};
 const cert=[];
 for(let h=0;h<=80;h++){
   let L=Lof(h),bs=Array.from({length:h},(_,i)=>choose(L,i+1)),g=bs.reduce((a,b)=>gg(a,b),0n);
   ok(L%2===1&&L>h,"odd-power");
   ok(h===0?g===0n:g===3n,"binomial gcd3");
   ok(bs.every(z=>z%3n===0n),"binomial divisibility");
   if(h===0||[1,2,3,8,9,26,27,80].includes(h))cert.push({h,L,gcd:String(g)});
   checks.integral_binomial_gcd_h0_to_80++;
 }
 for(let pi of perms){
   for(let j of pi){let H0=neg(P[j]);ok(same(add(P[j],H0),[0n]),"one sample zero");checks.one_probe_zero_fiber++}
 }
 for(let h of [0,1,2,3,8,9]){
   const L=Lof(h),bs=Array.from({length:h},(_,i)=>choose(L,i+1));
   for(let a of [0,2])for(let pi of perms){
     let ids=[];
     for(let x=0;x<6;x++){
       let j=pi[x],g=sh([BigInt((x+h)%2?2:1),BigInt(x+2)],a);
       let H=Array.from({length:h+1},(_,i)=>[BigInt((x+1)*(i+1)),BigInt(i+2)]);
       let H0=H[0],HL=H.reduce((sum,coef,i)=>add(sum,scale(coef,choose(L,i))),[0n]);
       let Y0=add(mul(g,P[j]),H0),YL=add(mul(g,M[j]),HL);
       let z=jet(sub(YL,Y0),a+8),v=nu3(z);
       let read=v===Infinity?5:v3.indexOf(v-a);
       ok(read===j,"orientation id");
       ids.push(read);
     }
     ok(ids.join(",")===pi.join(","),"full pi recovered");
     checks.full_orientation_two_probe++;
   }
   if(h===0)continue;
   const bz=bezout(bs);
   ok(bz.g===3n&&bs.reduce((v,b,i)=>v+b*bz.coeff[i],0n)===3n,"Bezout exact");
   for(let a of [0,2]){
     let i=4,j=5,g=sh([1n],a),d=a+7;
     let Y0old=mul(g,P[i]),YLold=mul(g,M[i]);
     let H0=sub(Y0old,mul(g,P[j]));
     let target=jet(sub(sub(YLold,mul(g,M[j])),H0),d);
     ok(target.every(z=>z%3n===0n),"target divisible3");
     let oneThird=target.map(z=>z/3n);
     let Bs=[H0].concat(bz.coeff.map(v=>scale(oneThird,v)));
     let alt0=add(mul(g,P[j]),Bs[0]);
     let altL=add(mul(g,M[j]),Bs.reduce((sum,b,k)=>add(sum,scale(b,choose(L,k))),[0n]));
     ok(same(jet(alt0,d),jet(Y0old,d))&&same(jet(altL,d),jet(YLold,d)),"sharp collision");
     checks.sharp_jet_collision++;
   }
 }
 return {schema:"EM_R630_MOD3_SPARSE_BRC_TOMOGRAPHY_V1",date:"2026-11-08",
  frozen_R462:"18783e01e3646c72b7aab3b16d3f565e83e6446f",
  inherited_R629:"ec2f19f968fbab2270615cbf21f45d0164624828",
  original_K_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",
  mod3_delta_valuations:v3,probe_indices:"0 and L=least power of 3 strictly greater than h",verified_h_gcd:cert,
  tested_two_probe_h:[0,1,2,3,8,9],gain_valuations:[0,2],
  checks,total:Object.values(checks).reduce((a,b)=>a+b,0),
  arithmetic:"exact BigInt signed BRC polynomials, integral Newton interpolation, binomial modular tests",
  marker:"R630_MOD3_SPARSE_TWO_PROBE_EXACT_PASS",status:"AUTHOR_SIDE_EXACT_UNREVIEWED"};
};
if (typeof require === 'function' && require.main === module) console.log(JSON.stringify(run(), null, 2));
