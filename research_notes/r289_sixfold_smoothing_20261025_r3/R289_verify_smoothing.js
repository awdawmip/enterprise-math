const evidence=(function verify(){
  const N=96, DPN=110;
  const assert=(ok,msg)=>{if(!ok)throw Error("FAIL "+msg)};
  const z=()=>Array(N+1).fill(0n);
  const at=(v,n)=>n>=0&&n<=N?v[n]:0n;
  const mul=(a,b)=>{const o=z();for(let i=0;i<=N;i++)if(a[i])for(let j=0;j+i<=N;j++)if(b[j])o[i+j]+=a[i]*b[j];return o};
  let h=z();
  for(let n=1;n<=N;n++){
    let v=n===4?1n:0n;
    for(const [off,c] of [[1,1n],[2,2n],[3,1n],[4,1n]])if(n>=off)v+=c*h[n-off];
    for(const [off,c] of [[1,1n],[2,2n],[3,1n]])if(n>=off)for(let j=0;j<=n-off;j++)v+=c*h[j]*h[n-off-j];
    h[n]=v;
  }
  assert(h.slice(0,9).join(",")==="0,0,0,0,1,1,3,6,14","h start");
  const dh=z();for(let n=0;n<=N;n++)dh[n]=h[n]-at(h,n-1);
  assert(dh.every(x=>x>=0n),"h nondecreasing coefficients");
  let w=z();w[0]=1n;w[1]=1n;for(let n=2;n<=N;n++)w[n]=h[n]+h[n-1];
  assert(w.slice(0,9).join(",")==="1,1,0,0,1,2,4,9,20","w start");
  const powers=[z()];powers[0][0]=1n;
  for(let r=1;r<=22;r++)powers.push(mul(powers[r-1],w));
  const quot=(numerator)=>{let out=z();for(let n=0;n<=N;n++)out[n]=numerator[n]-at(out,n-1);return out};
  const T=[];
  for(let r=1;r<=20;r++){
    let num=z();for(let n=0;n<=N;n++)num[n]=powers[r][n]-at(powers[r],n-1);
    T[r]=quot(num);
  }
  const bad={};
  for(let r=1;r<=5;r++){const i=T[r].findIndex(v=>v<0n);assert(i>=0,"minimal threshold r="+r);bad[r]={first_negative_degree:i,coefficient:T[r][i].toString()};}
  assert(T[6].slice(0,7).join(",")==="1,4,5,0,1,26,71","T6 initial coefficients");
  for(let r=6;r<=20;r++){
    assert(T[r].every(v=>v>=0n),"T positivity "+r);
    const pred=mul(T[6],powers[r-6]);
    assert(T[r].every((v,i)=>v===pred[i]),"T propagation "+r);
  }
  let Gplus={},Gminus={};
  for(let m=1;m<=18;m++){
    let num=z();for(let j=0;j<=N;j++)num[j]=at(powers[m+1],j)-at(powers[m+1],j-1)+at(powers[m+1],j-2)-at(powers[m+2],j-1);
    Gplus[m]=quot(num);
  }
  for(let m=2;m<=18;m++){
    let num=z();for(let j=0;j<=N;j++)num[j]=at(powers[m-1],j)-at(powers[m],j-1);
    Gminus[m]=quot(num);
  }
  let adjacent_checks=0,cross_checks=0;
  for(let m=1;m<=17;m++){const next=mul(w,Gplus[m]);for(let j=0;j<=N;j++){assert(next[j]===Gplus[m+1][j],"plus one-step");adjacent_checks++;}}
  for(let m=2;m<=17;m++){const next=mul(w,Gminus[m]);for(let j=0;j<=N;j++){assert(next[j]===Gminus[m+1][j],"minus one-step");adjacent_checks++;}}
  for(let m=3;m<=15;m++){
    const shifted=mul(powers[4],Gminus[m]);
    for(let j=0;j<=N;j++){assert(shifted[j]-Gplus[m+2][j]===at(T[m+3],j-1),"cross-sign m="+m+" j="+j);cross_checks++;}
  }
  const EDGES=[[[2,-1,-1],[2,1,-1]],[[0,-1,-1],[0,1,-1]],[[1,1,1],[2,1,-1]]];
  let states=new Map([["0,1,0,0",1n]]),dp_checks=0;
  for(let n=0;n<=DPN;n++){
    let out=new Map();
    for(const [key,cnt] of states){
      const [q,eps,k]=key.split(",").map(Number);
      if(q===0){const key2=eps+","+k;out.set(key2,(out.get(key2)||0n)+cnt);}
    }
    for(let m=1;m<=16;m++)for(const eps of [1,-1]){
      if(eps===-1&&m<2)continue;
      let got=(out.get(eps+","+(-m))||0n)-(out.get(eps+","+(-m-2))||0n);
      let index=(n-m-2)/2;
      let expected=Number.isInteger(index)&&index>=0 ? (eps===1?Gplus[m][index]:Gminus[m][index]) : 0n;
      assert(got===expected,"raw DP gap n="+n+" m="+m+" eps="+eps);
      dp_checks++;
    }
    const next=new Map();
    for(const [key,cnt] of states){
      const [q,eps,k,prev]=key.split(",").map(Number);
      for(let b=0;b<2;b++){
        if(prev===1&&b===0)continue;
        const [q2,eta,d]=EDGES[q][b];
        const dest=[q2,eta*eps,eta*k+d,b===0?1:0].join(",");
        next.set(dest,(next.get(dest)||0n)+cnt);
      }
    }
    states=next;
  }
  return {schema:"EM_R289_SIXFOLD_SMOOTHING_EXACT_V1",status:"PASS",model:"ordered positive clean-reset six-edge BRC auxiliary",scope:"finite machine checks plus separate all-length formal proof",coeff_end:N,original_dp_end:DPN,dp_gap_checks:dp_checks,one_step_checks:adjacent_checks,cross_sign_convolution_checks:cross_checks,h_first:["0","0","0","0","1","1","3","6","14"],T6_first:T[6].slice(0,12).map(String),minimality_negative_witnesses:bad,all_length_proof_method:"(1-y)h has coefficientwise-positive quadratic recurrence; explicit T6 degrees <=6; T_r=T6*w^(r-6); exact R288 gap formulas",dependencies:["R283 exact Green source formula","R286 positive h equation","R288 exact radical cancellation"],math_admitted:false,driver_review:"NOT_DONE",native_owner_verified:false}
})();
if(typeof console!=='undefined')console.log(JSON.stringify(evidence,null,2));
