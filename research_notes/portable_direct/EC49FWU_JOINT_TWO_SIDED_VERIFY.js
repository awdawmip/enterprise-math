#!/usr/bin/env node
// EC49FWU, frozen BRC16943. Run: node EC49FWU_JOINT_TWO_SIDED_VERIFY.js
const verify = function verify(){
  const mod=(x,m)=>((x%m)+m)%m;
  const gcd=(a,b)=>{while(b){let z=a%b;a=b;b=z;}return a};
  const inv=(a,m)=>{for(let x=0;x<m;x++)if(mod(a*x,m)===1)return x;throw Error("inverse missing "+a+" "+m)};
  const group=[[[1,4,6,9],[1,4,6,9]],[[2,7],[3,8]],[[3,8],[2,7]]];
  const p10=(H,N)=>{
    const h=mod(H,10),n=mod(N,10);if(h%5===0&&n%5===0)return false;
    const slope=h%5===0?5:mod(n*inv(h,5),5);
    const sets=[[[3],[0,3,4,5]],[[2,3,4,5],[2,3]]];
    return sets[h%2][n%2].includes(slope)
  };
  const c11=(h,n)=>p10(h,n)&&mod(9*h+10*n,11)!==0;
  const roots=new Map;
  for(let a=0;a<10;a++)for(let y=0;y<10;y++)for(const sign of [-1,1]){
    let root=null;
    for(let h=0;h<10&&root===null;h++)for(let n=0;n<10;n++)if(mod(y*h-a*n-sign,10)===0){root=[h,n];break}
    roots.set(`${a},${y},${sign}`,root)
  }
  const maskAt=(h,n,a,y)=>{let u=0;for(let t=0;t<10;t++)if(p10(h+a*t,n+y*t))u|=1<<t;return u};
  const trace=(a,b,sign)=>{
    const y=b-a,h0=a>1?mod(sign*inv(y,a),a):0,n0=(y*h0-sign)/a;
    const [x,z]=roots.get(`${mod(a,10)},${mod(y,10)},${sign}`);
    let t0=-1;
    for(let t=0;t<10;t++)if(mod(h0+a*t-x,10)===0&&mod(n0+y*t-z,10)===0){t0=t;break}
    if(t0<0)throw Error("origin phase missing");
    const h=h0+a*t0,n=n0+y*t0,D=mod(9*a+10*y,11),L=mod(9*h+10*n,11);
    if(D===0&&L===0)throw Error("unimodular contradiction");
    const hole=D===0?null:mod(-L*inv(D,11),11);
    return {u:maskAt(h,n,a,y),hole,h,n}
  };
  const bits=(v,i)=>(v>>i)&1;
  const corr=(u,n)=>Array.from({length:n},(_,c)=>{let k=0;for(let i=0;i<n;i++)k+=bits(u,i)*bits(u,mod(c-i,n));return k});
  const specCache=new Map;
  const spec=(s)=>{
    let key=`${s.u},${s.hole}`;if(specCache.has(key))return specCache.get(key);
    const v=s.hole===null?2047:2047^(1<<s.hole),ku=corr(s.u,10),kv=corr(v,11);
    const pop=x=>{let n=0;while(x){n+=x&1;x>>=1;}return n};
    const mass=pop(s.u)*pop(v),res=ku.flatMap(x=>kv.map(y=>2*(mass-x*y))).join(",");
    specCache.set(key,res);return res
  };
  const flag=(s,t)=>bits(s.u,mod(t,10))===1&&(s.hole===null||mod(t,11)!==s.hole);
  const diffRows=(a,b)=>{const o=[];for(let j=0;j<10;j++)if(bits(a.u^b.u,j))o.push(j);return o.join(",")};
  const keyState=s=>`${s.left.u}:${s.left.hole}|${s.right.u}:${s.right.hole}`;
  const actualFibers=new Map;
  let anchors=0;
  for(let b=2;b<=80;b++)for(let a=1;a<b;a++){
    if(gcd(a,b)!==1)continue;anchors++;
    const left=trace(a,b,-1),right=trace(a,b,1),state={left,right,anchor:[a,b]};
    const sig=spec(left)+"|"+spec(right), sk=keyState(state);
    if(!actualFibers.has(sig))actualFibers.set(sig,new Map);
    if(!actualFibers.get(sig).has(sk))actualFibers.get(sig).set(sk,state)
  }
  const witnessed=new Map;
  for(const f of actualFibers.values()){
    const arr=[...f.values()];
    for(let i=0;i<arr.length;i++)for(let j=i+1;j<arr.length;j++){
      const x=arr[i],y=arr[j];
      if(x.left.hole!==y.left.hole||x.right.hole!==y.right.hole)continue;
      for(let g=0;g<3;g++){
        if(diffRows(x.left,y.left)!==group[g][0].join(",")||
           diffRows(x.right,y.right)!==group[g][1].join(","))continue;
        const h=x.left.hole;
        if(h===null||x.right.hole!==mod(1-h,11))continue;
        const key=`${g}:${h}`;
        if(!witnessed.has(key))witnessed.set(key,[x,y])
      }
    }
  }
  if(witnessed.size!==33)throw Error("missing authentic witness: "+witnessed.size);
  let directChecks=0;
  const witnesses=[];
  for(let g=0;g<3;g++)for(let hole=0;hole<11;hole++){
    const [x,y]=witnessed.get(`${g}:${hole}`),L=group[g][0],R=group[g][1];
    for(const s of [x,y])for(const [sign,side] of [[-1,"left"],[1,"right"]]){
      const t=trace(...s.anchor,sign);
      if(t.u!==s[side].u||t.hole!==s[side].hole)throw Error("anchor trace mismatch");
      for(let i=0;i<110;i++){
        if(flag(t,i)!==c11(t.h+s.anchor[0]*i,t.n+(s.anchor[1]-s.anchor[0])*i))
          throw Error("direct C11 != CRT");
        directChecks++;
      }
    }
    if(spec(x.left)!==spec(y.left)||spec(x.right)!==spec(y.right))throw Error("spectral collision failed");
    for(let t=0;t<110;t++){
      if((flag(x.left,t)!==flag(y.left,t))!== (L.includes(t%10)&&t%11!==hole))
        throw Error("left difference support failed");
      if((flag(x.right,t)!==flag(y.right,t))!== (R.includes(t%10)&&t%11!==mod(1-hole,11)))
        throw Error("right difference support failed")
    }
    witnesses.push({block:g+1,left_hole:hole,right_hole:mod(1-hole,11),anchors:[x.anchor,y.anchor]})
  }
  const paired=new Map,frozenLeft=new Set;
  let directions=0;
  for(let a=0;a<10;a++)for(let y=0;y<10;y++){
    if(gcd(gcd(a,y),10)!==1)continue;
    directions++;
    const [lx,lz]=roots.get(`${a},${y},-1`),[rx,rz]=roots.get(`${a},${y},1`);
    const ul=maskAt(lx,lz,a,y),ur=maskAt(rx,rz,a,y);
    frozenLeft.add(ul);
    let k0=-1;
    for(let k=0;k<10;k++)if(mod(lx+rx-k*a,10)===0&&mod(lz+rz-k*y,10)===0){k0=k;break}
    if(k0<0)throw Error("k mod10 not found");
    for(let k=k0;k<20;k+=10){
      for(let t=0;t<10;t++)if(bits(ur,t)!==bits(ul,mod(-k-t,10)))throw Error("mirror phase wrong");
      for(const hole of [null,...Array.from({length:11},(_,j)=>j)]){
        const rightHole=hole===null?null:mod(-k-hole,11);
        const state={left:{u:ul,hole},right:{u:ur,hole:rightHole}};
        paired.set(keyState(state),state)
      }
    }
  }
  if(directions!==72||frozenLeft.size!==50||paired.size!==1150)throw Error("finite carrier mismatch");
  const fibers=new Map;
  for(const s of paired.values()){
    const k=spec(s.left)+"|"+spec(s.right);
    if(!fibers.has(k))fibers.set(k,[]);
    fibers.get(k).push(s)
  }
  const ambiguous=[...fibers.values()].filter(x=>x.length>1);
  if(fibers.size!==964||ambiguous.length!==186||ambiguous.some(x=>x.length!==2))
    throw Error("universal fiber count failed");
  let minLeft=220,minJoint=440;
  const opt={};
  for(const r of Array.from({length:10},(_,i)=>i+1))opt[r]={sites:3*(r+1),min_distance:999};
  for(const f of ambiguous){
    const [s,t]=f;
    if(s.left.u===t.left.u&&s.left.hole===t.left.hole)throw Error("unresolved left-same fiber");
    let dl=0,dr=0;
    for(let t0=0;t0<110;t0++){
      dl+=flag(s.left,t0)!==flag(t.left,t0)?1:0;
      dr+=flag(s.right,t0)!==flag(t.right,t0)?1:0;
    }
    minLeft=Math.min(minLeft,dl);minJoint=Math.min(minJoint,dl+dr);
    for(const [r,rr] of Object.entries(opt)){
      let d=0;
      for(const row of [1,2,3])for(let col=0;col<=+r;col++){
        const t0=mod(11*row+100*col,110);
        if(flag(s.left,t0)!==flag(t.left,t0))d++
      }
      rr.min_distance=Math.min(rr.min_distance,d)
    }
  }
  if(minLeft!==20||minJoint!==40||Object.entries(opt).some(([r,v])=>v.min_distance!==+r))
    throw Error("distance upper certificate failed");
  const leftFibers=new Map;
  for(const u of frozenLeft)for(const hole of [null,...Array.from({length:11},(_,j)=>j)]){
    const s={u,hole},k=spec(s);
    if(!leftFibers.has(k))leftFibers.set(k,[]);
    leftFibers.get(k).push(s)
  }
  if(leftFibers.size!==478||[...leftFibers.values()].filter(f=>f.length===2).length!==122)
    throw Error("left inherited census failed");
  return {
    status:"ALL PASS",unit:"EC49FWU",frozen_pin:"BRC16943",
    anchor_bound:80,anchors_enumerated:anchors,lower_bound_actual_witnesses:witnesses.length,
    direct_C11_vs_CRT_site_checks:directChecks,primitive_mod10_directions:directions,
    frozen_left_masks:frozenLeft.size,universal_paired_superset_states:paired.size,
    universal_paired_spectrum_fibers:fibers.size,universal_paired_doubletons:ambiguous.length,
    min_left_hamming_distance:minLeft,min_paired_hamming_distance:minJoint,
    inherited_left_fibers:leftFibers.size,inherited_left_doubletons:122,
    sharp_fixed_joint_N_r:opt,sharp_adaptive_joint_N_r:"r for 1<=r<=10",
    groups:group,witnesses,review:"AUTHOR_PROVED / EXACT_INTEGER_CERTIFICATE / NOT_REVIEWED"
  }
};
console.log(JSON.stringify(verify(),null,2));
