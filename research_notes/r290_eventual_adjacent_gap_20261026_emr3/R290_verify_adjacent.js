const verify = function verify() {
 const N=400, DP_N=110, z=()=>Array(N+1).fill(0n);
 const at=(v,i)=>i>=0&&i<=N?v[i]:0n;
 const assert=(v,msg)=>{if(!v)throw Error("FAIL "+msg)};
 const mul=(a,b)=>{const o=z();for(let i=0;i<=N;i++)if(a[i])for(let j=0;j+i<=N;j++)if(b[j])o[i+j]+=a[i]*b[j];return o};
 const h=z();
 for(let n=1;n<=N;n++){
   let v=n===4?1n:0n;
   for(const [off,c] of [[1,1n],[2,2n],[3,1n],[4,1n]])v+=c*at(h,n-off);
   for(const [off,c] of [[1,1n],[2,2n],[3,1n]])if(n>=off)for(let j=0;j<=n-off;j++)v+=c*h[j]*h[n-off-j];
   h[n]=v;
 }
 const w=z();for(let n=0;n<=N;n++)w[n]=at(h,n)+at(h,n-1)+(n===0?1n:0n)+(n===1?1n:0n);
 const w2=mul(w,w);
 for(let n=0;n<=N;n++)assert(at(w2,n-1)-w[n]-2n*at(w,n-2)+at(w,n-3)+(n===0?1n:0n)===0n,"algebraic w degree "+n);
 const pw=[z()];pw[0][0]=1n;for(let k=1;k<=17;k++)pw[k]=mul(pw[k-1],w);
 const gaps={};
 for(const s of ["+","-"])for(let m=s==="+"?1:2;m<=15;m++){
    const q=z(),H=z();for(let j=0;j<=N;j++){
       H[j]=s==="+"?at(pw[m+1],j)-at(pw[m+1],j-1)+at(pw[m+1],j-2)-at(pw[m+2],j-1):
                          at(pw[m-1],j)-at(pw[m],j-1);
       q[j]=H[j]-at(q,j-1);
    }
    gaps[s+m]=q;
 }
 const EDGES=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
 let states=new Map([["0,1,0,0",1n]]),dp_checks=0;
 for(let n=0;n<=DP_N;n++){
    const count=new Map();
    for(const [key,c] of states){
       const [q,e,k]=key.split(",").map(Number);
       if(q===0){const a=e+","+k;count.set(a,(count.get(a)||0n)+c);}
    }
    for(const s of ["+","-"])for(let m=s==="+"?1:2;m<=15;m++){
       const e=s==="+"?1:-1, j=(n-m-2)/2;
       const actual=(count.get(e+","+(-m))||0n)-(count.get(e+","+(-m-2))||0n);
       const expected=Number.isInteger(j)&&j>=0?gaps[s+m][j]:0n;
       assert(actual===expected,"raw DP "+n+" "+s+m);
       dp_checks++;
    }
    const next=new Map();
    for(const [key,c] of states){
       const [q,e,k,prev]=key.split(",").map(Number);
       for(let b=0;b<2;b++){if(prev===1&&b===0)continue;
          const [q1,eta,d]=EDGES[q][b];const a=[q1,eta*e,eta*k+d,b===0?1:0].join(",");
          next.set(a,(next.get(a)||0n)+c);}
    }
    states=next;
 }
 const checked={};
 for(const [s,m] of [["+",3],["+",4],["+",13],["+",14],["-",2],["-",3],["-",11],["-",12]]){
    const a=gaps[s+m],positive=(s==="+"?m>=4:m>=3);
    for(let j=250;j<=N;j++)assert((positive&&a[j]>0n)||(!positive&&a[j]<0n),"late sign "+s+m+" j"+j);
    if((s==="+"&&m>=13)||(s==="-"&&m>=11))assert(a.every(x=>x>=0n),"base prefix "+s+m);
    let lastNegative=-1;for(let j=0;j<=N;j++)if(a[j]<0n)lastNegative=j;
    checked[s+m]={asymptotic_sign:positive?"POSITIVE":"NEGATIVE",last_negative_through_400:lastNegative,first_10:a.slice(0,10).map(String)};
 }
 const rho=(3-Math.sqrt(5))/2,phi=(1+Math.sqrt(5))/2;
 const beta=(1-rho)/(2*rho)*Math.sqrt((1-rho*rho)*(1+rho+rho*rho));
 const C=(s,m)=>{const der=s==="+"?Math.pow(phi,m)/ (1+rho)*((m+1)*rho*rho-(1-rho)):
   Math.pow(phi,m-2)/(1+rho)*(m*rho-1);
   return beta*der/(2*Math.sqrt(Math.PI));};
 return {schema:"EM_R290_EVENTUAL_ADJACENT_GAP_V1",status:"PASS",model:"ordered positive six-edge BRC clean-reset, full affine effects",h_coeff_end:N,source_dp_end:DP_N,dp_gap_checks:dp_checks,quadratic_identity_checks:N+1,independent_base_check:"R288 radical-cancellation versus source-bit DP",asymptotic_constants:{minus11:C("-",11),plus13:C("+",13),minus2:C("-",2),plus3:C("+",3)},finite_observation:checked,mathematical_proof:"unique smallest positive discriminant singularity rho and nonzero Puiseux sqrt coefficient; fixed-m transfer only",global_uniform_threshold_claimed:false,math_admitted:false,native_owner_verified:false,driver_review:"NOT_DONE"};
};
console.log(JSON.stringify(verify(),null,2));
