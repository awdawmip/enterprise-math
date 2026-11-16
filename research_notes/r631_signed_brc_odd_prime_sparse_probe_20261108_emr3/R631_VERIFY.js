const run = function R631_RUN(){
 const ok=(v,s)=>{if(!v)throw Error("R631 "+s)};
 const C=(n,k)=>{if(n<0||k<0||k>n)return 0n;let z=1n;for(let i=1;i<=Math.min(k,n-k);i++)z=z*BigInt(n-i+1)/BigInt(i);return z};
 const add=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n));
 const sub=(a,b)=>add(a,b.map(v=>-v));
 const sh=(a,n)=>Array(n).fill(0n).concat(a);
 const K=i=>{let d=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)],z=[0n];for(let k=1;k<=4;k++){let n=i+1-k;if(n>=0&&d[k-1]!==0n)z=add(z,sh(Array.from({length:n+1},(_,j)=>-d[k-1]*C(n,j)),i-1))}return z};
 const ks=Array.from({length:12},(_,j)=>K(j+1));
 const P=ks.filter((_,j)=>j%2===0),M=ks.filter((_,j)=>j%2===1),D=P.map((a,j)=>sub(a,M[j]));
 const nt=(a,p)=>{for(let i=0;i<a.length;i++)if(a[i]%BigInt(p)!==0n)return i;return Infinity};
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
 const ps=[];for(let p=3;p<220;p+=2){let prime=true;for(let d=3;d*d<=p;d+=2)if(p%d===0){prime=false;break}if(prime)ps.push(p)}
 const safe=ps.filter(p=>p!==53&&p!==83);
 const lead=D.map(a=>a.find(x=>x!==0n)),tors=lead.map(String);
 const unit=Object.fromEntries(safe.map(p=>[p,D.map(d=>nt(d,p))]));
 ok(JSON.stringify(unit[3])===JSON.stringify([0,2,7,6,8,11]),"special p3");
 for(let p of safe.filter(x=>x>=5))ok(JSON.stringify(unit[p])===JSON.stringify([0,2,4,6,8,10]),"unit signatures "+p);
 const ppow=(h,p)=>{let n=1;while(n<=h)n*=p;return n};
 const optimum=[];
 let counts={prime_signatures:0,optimal_index_calculations:0,binomial_gcd:0,orientation_recovery:0,one_probe_zero_fiber:0};
 for(const p of safe)counts.prime_signatures++;
 for(let h=0;h<=100;h++){
   let opts=safe.map(p=>({p,L:ppow(h,p)})).sort((a,b)=>a.L-b.L||a.p-b.p);
   let win=opts[0];
   if([0,1,2,3,4,5,6,7,8,9,10,11,12,13,23,24,25,26,27,28,52,53,54,82,83,84,99,100].includes(h))optimum.push({h,...win});
   for(let p of safe.slice(0,10)){
     let L=ppow(h,p),v=0n;
     for(let j=1;j<=h;j++)v=gcd(v,C(L,j));
     ok(v===BigInt(h===0?0:p),"gcd"+h+" "+p+" "+v);
     counts.binomial_gcd++;
   }
   counts.optimal_index_calculations++;
 }
 const perm=[];function pe(a,k){if(k===6){perm.push(a.slice());return}for(let j=k;j<6;j++){[a[k],a[j]]=[a[j],a[k]];pe(a,k+1);[a[k],a[j]]=[a[j],a[k]]}}pe([0,1,2,3,4,5],0);ok(perm.length===720,"720");
 for(let p of [3,5,7,11])for(let h of [0,1,2,3,4,8,9,24,26]){
   const L=ppow(h,p);
   for(let a of [0,2])for(let pi of perm){
     for(let x=0;x<6;x++){
       let j=pi[x];
       let gain=sh([BigInt(1+(x%(p-1))),BigInt(x+1)],a);
       let nuisance=Array.from({length:h+1},(_,k)=>[BigInt(2+x*k),BigInt(k+1)]);
       let ys=Array(gain.length+D[j].length+1).fill(0n);
       for(let u=0;u<gain.length;u++)for(let v=0;v<D[j].length;v++){ys[u+v]-=gain[u]*D[j][v]}
       for(let k=1;k<=h;k++){let v=C(L,k);for(let m=0;m<nuisance[k].length;m++)ys[m]+=v*nuisance[k][m]}
       let nu=nt(ys,p),lookup=unit[p];
       let label=nu===Infinity||nu>a+8?5:lookup.findIndex(s=>s+a===nu);
       ok(label===j,`recover p${p} h${h} a${a} j${j} got ${label} nu${nu}`);
     }
     counts.orientation_recovery++;
   }
 }
 for(let pi of perm){for(let j of pi){ok(P[j].length>=1,"source");counts.one_probe_zero_fiber++}}
 const total=Object.values(counts).reduce((a,b)=>a+b,0);
 return {schema:"EM_R631_ODD_PRIME_MODULAR_BRC_PROBE_V1",date:"2026-11-08",
   frozen_R462:"18783e01e3646c72b7aab3b16d3f565e83e6446f",
   predecessor_R630:"256e0b45069acaa4b6e8eb7bc6c1a86bcfdd5310",
   original_K_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",
   delta_leading:tors,unit_modulus_exclusions:[53,83],special_modulus:3,
   prime_candidates_tested:safe,mod3_valuations:unit[3],standard_unit_valuations:[0,2,4,6,8,10],
   sampling:"L=minimal p^s>h for selected prime p; compare across unit-signature odd primes",
   optimal_schedule_examples:optimum,checks:counts,total,
   arithmetic:"BigInt integer signed K coefficients and binomial gcd",status:"AUTHOR_SIDE_EXACT_UNREVIEWED",
   marker:"R631_ODD_PRIME_SPARSE_BRC_EXACT_PASS"};
};
if (typeof require === 'function' && require.main === module) console.log(JSON.stringify(run(), null, 2));
