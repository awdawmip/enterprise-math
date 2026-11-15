// R749SQM exact integer certificate; Node.js 18+; no external dependencies.
// The function is self-contained and returns exact rational numerical witnesses.
const report=(function certificate(){
  const gcd=(aa,bb)=>{let a=aa<0n?-aa:aa,b=bb<0n?-bb:bb;while(b){const t=a%b;a=b;b=t;}return a||1n;};
  const R=(a,b=1n)=>{a=BigInt(a);b=BigInt(b);if(b<0n){a=-a;b=-b;}const g=gcd(a,b);return [a/g,b/g];};
  const add=(a,b)=>R(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
  const sub=(a,b)=>R(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);
  const mul=(a,b)=>R(a[0]*b[0],a[1]*b[1]);
  const str=x=>x[0].toString()+"/"+x[1].toString();
  const weightCases=[
    {id:"exceptional-h2",weights:[1,2],h:2},
    {id:"exceptional-h1",weights:[1,2],h:1},
    {id:"exceptional-g3",weights:[1,3,3],h:3},
    {id:"gcd-one-one-unit",weights:[1,2,3],h:2},
    {id:"equal-dD-h-A",weights:[1,1,2,4],h:1},
    {id:"equal-dD-h-B",weights:[1,1,3,3],h:1},
    {id:"frozen-R749SQL",weights:[1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,6,6,7],h:3}
  ];
  const getC=(weights,N)=>{const a=Array(N).fill(0n);a[0]=1n;for(const s of weights)for(let k=s;k<N;k++)a[k]+=a[k-s];const c=Array(N+1).fill(0n);for(let r=1;r<=N;r++)c[r]=c[r-1]+a[r-1];return c;};
  const sg=(r,g)=>{if(g<=1)return R(0);const n=(r-1)%g;return add(R((g-1)*(5-g),12),R(n*(g-n-2),2));};
  const gcdNum=(a,b)=>{while(b){const t=a%b;a=b;b=t;}return a;};
  const report={schema:"ENTERPRISE_MATH_R749SQM_SOURCE_SECOND_ORDER_CERT_V1",status:"PASS",scientific_pin:"a72226e2430ffa4786321ac86e7f0c599d5f0389",method:"exact BigInt coin-change DP; independent marked-source deletion test; exact rational residuals",cases:[],comparison:null,previous_SQL_reproduction:null};
  const caseSnapshots={};
  for(const test of weightCases){
    const {id,weights,h}=test,N=1536,d=weights.length,D=weights.reduce((v,s)=>v+s-1,0),Q=weights.reduce((v,s)=>v+s*s-1,0);
    const c=getC(weights,N),k=Array(N+1).fill(0n);
    for(let r=1;r<=N;r++)if(r>h)k[r]=k[r-h]+c[r-h];
    const without=weights.slice();without.splice(without.indexOf(h),1);
    const other=getC(without,128);
    for(let r=1;r<=128;r++){
      let cnt=0n,mom=0n;
      for(let j=0;r-h*j>0;j++){const v=other[r-h*j];cnt+=v;mom+=BigInt(j)*v;}
      if(cnt!==c[r]||mom!==k[r])throw Error("independent marked-count mismatch "+id+" r="+r);
    }
    const a0=R(1,d+1);
    const a1=R(D+d-1-h*(d+1),2*(d+1));
    const a2=R(d*((d+1)*(h*h-1)-Q),12*(d+1));
    const units=weights.filter(s=>s===1).length;
    let g=0;for(const s of weights)if(s>1)g=gcdNum(g,s);if(g===0)g=1;
    const exceptional=units===1&&g>1;
    const beta=exceptional?(h>1?R(2*d,d+1):R(-d*(d-1),d+1)):R(0);
    const snaps=[];
    for(const r of [128,256,512,1024,1536]){
      const mean=R(BigInt(h)*k[r],BigInt(r)*c[r]);
      const residual=mul(sub(sub(mean,a0),mul(a1,R(1,r))),R(BigInt(r)*BigInt(r)));
      const predicted=add(a2,mul(beta,sg(r,g)));
      const error=sub(residual,predicted);
      snaps.push({r,scaled_second_order_residual:str(residual),predicted_second_order_coefficient:str(predicted),remaining_error:str(error),remaining_error_approx:Number(error[0])/Number(error[1])});
      if(id==="equal-dD-h-A"||id==="equal-dD-h-B"){(caseSnapshots[id]??={})[r]=mean;}
    }
    if(id==="exceptional-h2"){
      for(let r=1;r<=N;r++){
        const expected=r%2===0?sub(R(1,3),R(2,3*r)):sub(R(1,3),R(2,3*(r+1)));
        if(k[r]*BigInt(h)*expected[1]!==BigInt(r)*c[r]*expected[0])throw Error("exceptional-h2 closed form mismatch r="+r);
      }
    }
    if(id==="frozen-R749SQL"){
      const B38=72n*k[38]-38n*c[38],B39=72n*k[39]-39n*c[39];
      if(B38!==-87935832n||B39!==34517412n)throw Error("SQL prior boundary reproduction failed");
      report.previous_SQL_reproduction={B38:B38.toString(),B39:B39.toString()};
    }
    report.cases.push({id,weights,h,d,D,Q,unit_weight_count:units,nonunit_gcd:g,second_order_periodic:exceptional,
      smooth_coefficients:[str(a0),str(a1),str(a2)],periodic_multiplier:str(beta),independent_count_check_r:"1..128",
      samples:snaps});
  }
  const diff=[];
  for(const r of [128,256,512,1024,1536]){
    const raw=sub(caseSnapshots["equal-dD-h-A"][r],caseSnapshots["equal-dD-h-B"][r]);
    const scaled=mul(raw,R(BigInt(r)*BigInt(r)));
    diff.push({r,scaled_mean_difference:str(scaled),target:"-2/15",difference_from_target:str(sub(scaled,R(-2,15)))});
  }
  report.comparison={a:"[1,1,2,4],h=1",b:"[1,1,3,3],h=1",same:[4,4,1],different_Q:[18,16],predicted_limit:"-2/15",samples:diff};
  return report;
})();
console.log(JSON.stringify(report,null,2));
