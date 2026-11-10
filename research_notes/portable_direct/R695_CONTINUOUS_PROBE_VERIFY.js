/* R695 exact BRC observer certificate. R692C immutable source Git blob 0c6d51f99eac5903a30770c8c393c972a68d93ad. */
const result=(function verify(){
 const N=[[[6,9,0,0],[6,6,3,0],[6,3,0,6],[6,0,3,6]],[[6,0,6,3],[9,0,6,0],[12,0,0,3],[15,0,0,0]],[[15,0,0,0],[12,3,0,0],[9,6,0,0],[6,9,0,0]]];
 const I=[0,1,3,2],assert=(c,m)=>{if(!c)throw Error(m)},dot=(x,y)=>x.reduce((s,v,k)=>s+v*y[I[k]],0),kernel=(a,c)=>N[a][0].map((_,k)=>c.reduce((s,v,j)=>s+v*N[a][j][k],0)),same=(x,y)=>x.every((z,i)=>z===y[i]),gcd=(x,y)=>y?gcd(y,x%y):x;
 const classes=[],stats={masks:0,pairs:0,mixtures:0};
 for(let a=0;a<3;a++){
  const uniq=new Set;
  for(let m=1;m<16;m++){const c=[0,1,2,3].map(j=>(m>>j)&1),d=c.reduce((u,v)=>u+v),s=kernel(a,c),g=gcd(...s.reduce((u,v)=>[gcd(u[0],v)], [0]));assert(s.reduce((u,v)=>u+v)===15*d,"mass");uniq.add(s.map(x=>x/g).join(","));stats.masks++}
  assert(uniq.size===[13,13,9][a],"mask class "+a+" "+uniq.size);classes.push(uniq.size);
  for(let m=1;m<16;m++)for(let n=1;n<16;n++){
    const c=[0,1,2,3].map(j=>(m>>j)&1),f=[0,1,2,3].map(j=>(n>>j)&1),d=c.reduce((u,v)=>u+v),h=f.reduce((u,v)=>u+v),x=kernel(a,c),y=kernel(a,f);
    const eq=x.every((v,i)=>v*h===y[i]*d),check=(a===0?[x[0],dot(x,N[a][0]),dot(x,N[a][2])].every((v,i)=>v*h===[y[0],dot(y,N[a][0]),dot(y,N[a][2])][i]*d):a===1?[x[0],dot(x,N[a][0])].every((v,i)=>v*h===[y[0],dot(y,N[a][0])][i]*d):x[0]*h===y[0]*d);
    assert(eq===check,"mask comparison "+a+" "+m+" "+n);stats.pairs++;
  }
  for(let q0=0;q0<=8;q0++)for(let q1=0;q1<=8;q1++)for(let q2=0;q2<=8;q2++)for(let q3=0;q3<=8;q3++){
    const d=q0+q1+q2+q3;if(d===0||d>8)continue;
    const x=kernel(a,[q0,q1,q2,q3]);let recon;
    if(a===0){const p1=dot(x,N[a][0]),p4=dot(x,N[a][2]),t=(p1-36*d)/9,c=(p4-36*d-3*t)/6;assert(Number.isInteger(t)&&Number.isInteger(c),"integer inversion");recon=[6*d,t,c,9*d-t-c]}
    else if(a===1){const p1=dot(x,N[a][0]),c=(90*d-p1)/3;assert(Number.isInteger(c),"int inversion");recon=[x[0],0,c,15*d-x[0]-c]}
    else recon=[x[0],15*d-x[0],0,0];
    assert(same(x,recon),"mixture inversion "+a);stats.mixtures++;
  }
 }
 assert(stats.masks===45&&stats.pairs===675&&stats.mixtures===1482,"coverage");
 const first=N[0][1],second=kernel(0,[3,0,5,0]),probe=N[0][0].map((v,i)=>v+N[0][1][i]);
 assert(dot(first,probe)*8===dot(second,probe),"fiber equality");
 assert(dot(first,probe)*25===9*450,"9/25 exact");
 assert(8*dot(first,N[0][0])-dot(second,N[0][0])===54,"3/100 split");
 return {schema:"R695_CONTINUOUS_ESTAR_TOMOGRAPHY_JS_V1",science_source:"3dacca5010104893d96301af4d61608d5a5a0879",source_blob:"0c6d51f99eac5903a30770c8c393c972a68d93ad",status:"R695_ALL_EXACT_ASSERTIONS_PASS",arithmetic:"safe exact integers",checks:stats,classes,affine_dimensions:[2,2,1],optimal_probes:{phase0:[1,4],phase1:"one_step+mask1",phase2:"one_step"},witness:{r1:"2/5",r2_with_mask3:"9/25",difference_with_mask1:"3/100"}};
})();
console.log(JSON.stringify(result,null,2));
