// PREFIX-893: exhaustive disjoint 16x131072 strict-19-bit pair classification.
// Requires adjacent PREFIX892_R6_DYADIC_COMPLEMENT_CENSUS.cpp (frozen pin).
// Compile: g++ -O2 -std=c++17 PREFIX893_R6_FULL_PANEL_EXCLUSION.cpp -o prefix893
#define main prefix892_uninvoked_main
#include "PREFIX892_R6_DYADIC_COMPLEMENT_CENSUS.cpp"
#undef main
#include <numeric>
using namespace std;

struct FF {bool yes=false;int i=-1,j=-1;U a=0;};
// Under LCM(q1,q2)>=2^32, M=q2/g > floor((N-1)/q1): at most one k per (d,e).
FF zero_anchored_ff(int q1,int q2,int g) {
  U K=(N-1)/q1;int M=q2/g;
  assert(U(q1)*M>=N && U(M)>K);
  int inv=(M==1 ? 0:inverse(q1/g,M));assert(M==1||inv>=0);
  for(int i=0;i<P;i++)for(int j=0;j<P;j++){
    U bi=U(1)<<i,bj=U(1)<<j;
    for(int s=0;s<2;s++) {
      int64_t d=s ? int64_t(bi)-int64_t(bj) : int64_t(bi)+int64_t(bj);
      if(d%g)continue;
      int64_t t=d/g;t%=M;if(t<0)t+=M;
      U k=(M==1?0:(U(t)*inv)%M);
      if(!k || k>K)continue;
      U a=k*q1;
      if(s && (a&bj))continue;
      if(!s && !(a&bj))continue;
      assert(a<N && (a^bj)<N && (a^bj)%q2==bi%q2);
      assert(0%q1==a%q1);
      return {true,i,j,a};
    }
  }
  return {};
}
void verify_zf(int q1,int q2,int inv) {
  assert(inv>=0);U K=(N-1)/q1,r=inv;
  for(int i=0;i<P;i++) {
    U b=U(1)<<i,k=0,u=0;
    if(r<=K){k=r;u=N-1;}
    else if(U(q2-r)*q1+b<N){k=q2-r;u=N-1-b;}
    else{r=(2*r)%q2;continue;}
    U x=u-k*q1;
    assert(x<N&&u<N&&x%q1==u%q1&&x%q2==(u^b)%q2);
    return;
  }
  assert(false);
}
int main(){
  vector<int> Q;for(int q=262145;q<=524287;q+=2)Q.push_back(q);
  U sum_z=0,sum_p=0,sum_s=0,sum_f=0,sum_r=0;
  vector<pair<int,int>> unresolved;
  cout<<"{\n \"schema\":\"PREFIX893_R6_PANEL_EXCLUSION_V1\",\n \"p\":32,\n"
      <<" \"frozen_scientific_pin\":\"f42f2906d77f24085c123f3ccfe9667d41caa96d\",\n"
      <<" \"rows\":[\n";
  bool first=true;
  for(int q1:PANEL){U z=0,pos=0,zero=0,ff=0,rem=0;
    for(int q2:Q){
      int g=gcd(q1,q2);int inv=(g==1 ? inverse(q1,q2):-1);
      if(zero_flip(q1,q2,inv)){verify_zf(q1,q2,inv);z++;continue;}
      auto w=positive_completion(q1,q2,inv);
      if(w.valid){verify_witness(q1,q2,w);pos++;continue;}
      U lcm=U(q1/g)*q2;
      if(lcm<N){assert(lcm%q1==0&&lcm%q2==0);zero++;continue;}
      auto a=zero_anchored_ff(q1,q2,g);
      if(a.yes){assert(a.a%q1==0 && (a.a^(U(1)<<a.j))%q2 == (U(1)<<a.i)%q2);ff++;continue;}
      rem++;unresolved.push_back({q1,q2});
    }
    assert(z+pos+zero+ff+rem==Q.size());
    if(!first)cout<<",\n";first=false;
    cout<<"  {\"q1\":"<<q1<<",\"pairs\":"<<Q.size()
        <<",\"zf\":"<<z<<",\"positive_completion_only\":"<<pos
        <<",\"zero_step_only\":"<<zero<<",\"zero_anchored_ff_only\":"<<ff
        <<",\"requires_general_ff\":"<<rem<<"}";
    sum_z+=z;sum_p+=pos;sum_s+=zero;sum_f+=ff;sum_r+=rem;
  }
  cout<<"\n ],\n \"totals\":{\"pairs\":"<<Q.size()*16ULL
      <<",\"zf\":"<<sum_z<<",\"positive_completion_only\":"<<sum_p
      <<",\"zero_step_only\":"<<sum_s<<",\"zero_anchored_ff_only\":"<<sum_f
      <<",\"requires_general_ff\":"<<sum_r<<"},\n \"remainder\":[";
  for(size_t i=0;i<unresolved.size();i++){
    if(i)cout<<",";
    cout<<"["<<unresolved[i].first<<","<<unresolved[i].second<<"]";
  }
  cout<<"]\n}\n";
  assert(sum_z+sum_p+sum_s+sum_f+sum_r==Q.size()*16ULL);
}
