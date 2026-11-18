// PREFIX-892, frozen-science pin f42f2906d77f24085c123f3ccfe9667d41caa96d
// Exact finite p=32, strict 19-bit odd moduli, no external libraries.
// Compile: g++ -O2 -std=c++17 PREFIX892_R6_DYADIC_COMPLEMENT_CENSUS.cpp -o prefix892
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using U = uint64_t;
static const int P=32;
static const U N=(U(1)<<P);
static const int PANEL[]={262147,280001,300001,320003,340007,360007,380003,
  400009,420001,440003,460001,480007,500383,510007,520001,524285};

int inverse(int a,int m) { // -1 when no inverse
  int64_t r=m,nr=a,t=0,nt=1;
  while(nr) {auto q=r/nr; auto rr=r-q*nr,tt=t-q*nt;
    r=nr;nr=rr;t=nt;nt=tt;}
  if(r!=1)return -1;
  t%=m;if(t<0)t+=m;return int(t);
}
bool axis(int q) {
  U v=1;for(int h=1;h<P;h++){v=(2*v)%q;if(v==1||v==U(q-1))return true;}
  return false;
}
bool zero_flip(int q1,int q2,int inv) { // PREFIX-891 exact endpoint criterion
  if(inv<0)return false;
  U K=(N-1)/q1, r=inv;
  for(int i=0;i<P;i++) {
    U b=U(1)<<i;
    if(r<=K || U(q2-r)*q1+b<=N-1)return true;
    r=(2*r)%q2;
  }
  return false;
}
struct Complement {U k=0,l=0,a=0,c=0;bool valid=false;};
Complement positive_completion(int q1,int q2,int inv) {
  if(inv<0)return {};
  assert(U(q1)*q2>N); // strict 19-bit domain: single CRT representative is exhaustive
  U k=(N*U(inv))%q2;
  if(k==0 || k*U(q1)>=N)return {};
  U a=k*U(q1), rem=N-a;
  assert(rem>0 && rem%q2==0);
  U l=rem/q2;
  assert(l>=1);
  return {k,l,a,rem,true};
}
void verify_witness(int q1,int q2,const Complement& w) {
  assert(w.valid && w.k*U(q1)+w.l*U(q2)==N);
  const U b=N/2;
  U s1,t1,s2,t2;
  if(w.a>b) {s1=0;t1=b;s2=w.a;t2=w.a-b;}
  else {assert(w.c>b);s1=b;t1=0;s2=w.c-b;t2=w.c;}
  assert(s1<N&&t1<N&&s2<N&&t2<N);
  assert((s1^b)==t1 && (s2^b)==t2);
  assert(s1!=s2);
  assert(s1%q1==s2%q1 && t1%q2==t2%q2);
}
int main(){
  // An independent tiny-domain k-enumeration crosscheck of the CRT criterion.
  U small=0;
  for(int p=2;p<=10;p++) for(int q1=3;q1<=79;q1+=2)
    for(int q2=3;q2<=79;q2+=2) {
      U n=U(1)<<p; if(U(q1)*q2<=n)continue;
      int inv=inverse(q1,q2);bool brute=false;
      for(U k=1;k*U(q1)<n;k++)
        if((n-k*U(q1))%q2==0){brute=true;break;}
      U k=inv<0?0:(n*U(inv))%q2;
      bool predicted=inv>=0 && k!=0 && k*U(q1)<n;
      assert(brute==predicted);small++;
    }
  vector<int> Q;for(int q=262145;q<=524287;q+=2)Q.push_back(q);
  vector<int> A(524288);for(int q:Q)A[q]=axis(q);
  U az=accumulate(A.begin(),A.end(),U(0));assert(az==24);
  U tz=0,tp=0,tnew=0,tleft=0,tright=0;
  cout<<"{\n  \"schema\": \"PREFIX892_R6_DYADIC_COMPLEMENT_V1\",\n"
      <<"  \"frozen_scientific_pin\": \"f42f2906d77f24085c123f3ccfe9667d41caa96d\",\n"
      <<"  \"p\": 32, \"modulus_range\": [262145,524287],\n"
      <<"  \"odd_moduli\": "<<Q.size()<<", \"axis_moduli\": "<<az<<",\n"
      <<"  \"small_crt_brute_cases\": "<<small<<",\n  \"rows\": [\n";
  bool firstrow=true;
  for(int q1:PANEL) {
    assert(!A[q1]);
    U z=0,pos=0,newc=0,left=0,right=0,overlap=0;
    int firstq=0;Complement sample;
    for(int q2:Q){
      int inv=inverse(q1,q2);
      bool Z=zero_flip(q1,q2,inv);
      auto w=positive_completion(q1,q2,inv);
      if(Z)z++;
      if(w.valid){
        pos++; verify_witness(q1,q2,w);
        if(w.a>N/2)left++;else right++;
        if(Z)overlap++;
        else if(!A[q2]){newc++;if(!firstq){firstq=q2;sample=w;}}
        else assert(false); // if reached, print remaining overlap in the next release
      }
    }
    assert(pos==left+right && pos==overlap+newc);
    if(!firstrow)cout<<",\n";firstrow=false;
    cout<<"    {\"q1\": "<<q1<<", \"pairs\": "<<Q.size()
        <<", \"zero_flip\": "<<z<<", \"positive_completion\": "<<pos
        <<", \"completion_already_zero_flip\": "<<overlap
        <<", \"new_axis_and_zero_flip_free\": "<<newc
        <<", \"left_orientation\": "<<left<<", \"right_orientation\": "<<right
        <<", \"sample\": {\"q2\": "<<firstq<<", \"k\": "<<sample.k
        <<", \"ell\": "<<sample.l<<", \"a\": "<<sample.a<<", \"c\": "<<sample.c<<"}}";
    tz+=z;tp+=pos;tnew+=newc;tleft+=left;tright+=right;
  }
  cout<<"\n  ],\n  \"totals\": {\"pairs\": "<<Q.size()*16ULL
      <<", \"zero_flip\": "<<tz<<", \"positive_completion\": "<<tp
      <<", \"new_axis_and_zero_flip_free\": "<<tnew
      <<", \"left_orientation\": "<<tleft<<", \"right_orientation\": "<<tright
      <<"}\n}\n";
}
