const run = function R629_RUN() {
  const ok=(v,s)=>{if(!v)throw new Error("R629 "+s)};
  const C=(n,k)=>{if(n<0||k<0||k>n)return 0n;let a=1n;for(let j=1;j<=Math.min(k,n-k);j++)a=a*BigInt(n-j+1)/BigInt(j);return a};
  const T=a=>{a=a.slice();while(a.length>1&&a.at(-1)===0n)a.pop();return a.length?a:[0n]};
  const plus=(a,b)=>T(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
  const neg=a=>a.map(v=>-v), minus=(a,b)=>plus(a,neg(b));
  const sc=(a,x)=>T(a.map(v=>v*x));
  const mul=(a,b)=>{let v=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)v[i+j]+=a[i]*b[j];return T(v)};
  const sh=(a,k)=>Array(k).fill(0n).concat(a);
  const cut=(a,d)=>T(a.slice(0,d+1).length?a.slice(0,d+1):[0n]);
  const nu=a=>a.findIndex(x=>x!==0n)===-1?Infinity:a.findIndex(x=>x!==0n);
  const eq=(a,b)=>{a=T(a);b=T(b);return a.length===b.length&&a.every((v,j)=>v===b[j])};
  const K=i=>{let ds=[-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3)],z=[0n];for(let k=1;k<=4;k++){let n=i+1-k;if(n>=0&&ds[k-1]!==0n)z=plus(z,sh(Array.from({length:n+1},(_,j)=>-ds[k-1]*C(n,j)),i-1))}return z};
  const Ks=Array.from({length:12},(_,i)=>K(i+1));
  const P=Ks.filter((_,i)=>i%2===0),M=Ks.filter((_,i)=>i%2===1),D=P.map((p,i)=>minus(p,M[i]));
  const ord=D.map(nu),c=D.map((z,i)=>z[ord[i]]);
  ok(ord.join(",")==="0,2,4,6,8,10","valuation");
  ok(c.join(",")==="2,-8,6,106,83,9","leading");
  const dif=a=>a.slice(1).map((v,i)=>minus(v,a[i]));
  const delta=(a,r)=>{for(let i=0;i<r;i++)a=dif(a);ok(a.length===1,"delta-length");return a[0]};
  const nc=a=>{let out=[];while(a.length){out.push(a[0]);a=dif(a)}return out};
  const ne=(a,k)=>a.reduce((v,b,j)=>plus(v,sc(b,C(k,j))),[0n]);
  const response=(j,g,H,h)=>Array.from({length:h+2},(_,k)=>plus(mul(g,k%2?M[j]:P[j]),ne(H,k)));
  const perms=[];const perm=(a,j)=>{if(j===6){perms.push(a.slice());return}for(let i=j;i<6;i++){[a[i],a[j]]=[a[j],a[i]];perm(a,j+1);[a[i],a[j]]=[a[j],a[i]]}};perm([0,1,2,3,4,5],0);
  ok(perms.length===720,"permutations");
  const count={finite_difference_per_axis:0,full_orientation_band:0,full_orientation_normalized:0,minimal_probe_zero_fibers:0,sharp_depth_collision:0,wide_band_full_collision:0};
  const abs=v=>v<0n?-v:v;
  for(let h=0;h<=4;h++){
    let r=h+1;
    for(let j=0;j<6;j++){
      let g=sh([BigInt((j%2?-1:1)*(j+2)),BigInt(j+1)],h%3);
      let H=Array.from({length:h+1},(_,q)=>[BigInt(3*j+q+1),BigInt(q%2?-1:1)]);
      ok(eq(delta(response(j,g,H,h),r),sc(mul(g,D[j]),BigInt((r%2?-1:1)*2**h))),"finite-difference");
      count.finite_difference_per_axis++;
    }
    for(let [a,b] of [[0,0],[1,2]])for(let pi of perms){
      let ids=[];
      for(let x=0;x<6;x++){
        let val=a+(x+h)%(b-a+1);
        let g=sh([BigInt((x+1)*(x%2?-1:1)),2n],val);
        let H=Array.from({length:h+1},(_,q)=>[BigInt(x+q+2),1n]);
        let v=nu(cut(delta(response(pi[x],g,H,h),r),b+8));
        let j=v===Infinity?5:-1;
        if(v!==Infinity)for(let u=0;u<5;u++)if(a+2*u<=v&&v<=b+2*u)j=u;
        ok(j===pi[x],"band-j");
        ids.push(j);
      }
      ok(ids.join(",")===pi.join(","),"band-perm");count.full_orientation_band++;
    }
    for(let R of [0,3])for(let pi of perms){
      let ids=[];
      for(let x=0;x<6;x++){
        let g=sh([BigInt((x+h)%2?-1:1),BigInt(x+2)],(x+h)%(R+1));
        let H=Array.from({length:h+1},(_,q)=>[BigInt(x+q+4),-1n]);
        let z=cut(delta(response(pi[x],g,H,h),r),R+8),v=nu(z);
        let j=v===Infinity?null:c.findIndex(q=>abs(q)*BigInt(2**h)===abs(z[v]));
        ok(j===null||j!==-1,"normalized-label");
        ids.push(j);
      }
      ok(ids.filter(v=>v===null).length<=1,"at-most-one-unseen");
      if(ids.includes(null))ids[ids.indexOf(null)]=5;
      ok(ids.join(",")===pi.join(","),"normalized-perm");
      count.full_orientation_normalized++;
    }
    for(let pi of perms)for(let j of pi){
      let g=sh([1n],h%2),old=Array.from({length:h+1},(_,k)=>mul(g,k%2?M[j]:P[j]));
      let H=nc(old.map(neg));
      let ys=response(j,g,H,h);
      ok(ys.slice(0,h+1).every(z=>eq(z,[0n])),"lower-probe-zero");
      count.minimal_probe_zero_fibers++;
    }
    for(let [i,j] of [[4,5],[5,4]]){
      let g=sh([1n],4),old=Array.from({length:h+2},(_,k)=>mul(g,k%2?M[i]:P[i]));
      let alt=Array.from({length:h+2},(_,k)=>mul(g,k%2?M[j]:P[j]));
      let H=nc(old.slice(0,h+1).map((z,k)=>minus(z,alt[k])));
      ok(old.every((z,k)=>eq(cut(z,11),cut(plus(alt[k],ne(H,k)),11))),"sharp-depth");
      count.sharp_depth_collision++;
    }
    let U5=D[4].slice(8),U6=D[5].slice(10);
    for(let [i,j,g,v] of [[4,5,sh(U6,2),U5],[5,4,U5,sh(U6,2)]]){
      let old=Array.from({length:h+2},(_,k)=>mul(g,k%2?M[i]:P[i]));
      let alt=Array.from({length:h+2},(_,k)=>mul(v,k%2?M[j]:P[j]));
      let H=nc(old.slice(0,h+1).map((z,k)=>minus(z,alt[k])));
      ok(old.every((z,k)=>eq(z,plus(alt[k],ne(H,k)))),"full-series-collision");
      count.wide_band_full_collision++;
    }
  }
  const total=Object.values(count).reduce((a,b)=>a+b,0);
  ok(total===36050,"total");
  return {schema:"EM_R629_NEWTON_DRIFT_BRC_PROBE_V1",date:"2026-11-08",
    frozen_R462:"18783e01e3646c72b7aab3b16d3f565e83e6446f",
    reused_R628:"5c711f09b8420505d29be363003448d4c1d7469e",
    source_K_blob:"7fa7a762f758b30c6090468ac43487daa34abad8",
    nuisance:"H_x(k)=sum_{j=0}^h B_xj binomial(k,j); B_xj in Z[[t]]",
    probe_schedule:"P,M,P,M,..., k=0..h+1",
    exact_difference:"Delta^(h+1)Y=(-1)^(h+1)*2^h*A_x*(P_j-M_j)",
    delta_orders:ord,delta_leading:c.map(String),verified_h:[0,1,2,3,4],
    permutations:perms.length,checks:count,total,
    status:"AUTHOR_SIDE_EXACT_UNREVIEWED",marker:"R629_NEWTON_DRIFT_BRC_EXACT_PASS"};
};
if (typeof require === 'function' && require.main === module) console.log(JSON.stringify(run(), null, 2));
