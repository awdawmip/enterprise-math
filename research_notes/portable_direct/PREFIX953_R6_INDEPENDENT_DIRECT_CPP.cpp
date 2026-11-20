// Independent direct Q19 check of PREFIX-953 named-source bit correlations.
#include <cstdint>
#include <iostream>
using namespace std;
int main(){
  constexpr int p=19, H=1<<(p-1), M=2*H, k=21, l=23;
  uint64_t low=0, lbTop=0, topLb=0, topTop=0, zz=0, ww=0;
  uint64_t same[17]={};
  for(int a=H+1;a<M;a+=2){
    int Lk=0,Ll=0;
    for(int j=1;j<=p-2;j++) {
      int b1=((k*a>>j)&1)==0;
      int b2=((l*a>>j)&1)==0;
      Lk+=b1; Ll+=b2; same[j-1]+=(b1&&b2);
    }
    int Tk=((k*a>>(p-1))&1)==0, Tl=((l*a>>(p-1))&1)==0;
    int Zk=Lk+Tk,Zl=Ll+Tl;
    int Wk=Zk+(a==H+1?2:0),Wl=Zl+(a==H+1?2:0);
    low+=(uint64_t)Lk*Ll;lbTop+=(uint64_t)Lk*Tl;topLb+=(uint64_t)Tk*Ll;topTop+=(uint64_t)Tk*Tl;
    zz+=(uint64_t)Zk*Zl;ww+=(uint64_t)Wk*Wl;
  }
  cout<<"low="<<low<<" lowerTop="<<lbTop<<" topLower="<<topLb<<" topTop="<<topTop
      <<" zeroProduct="<<zz<<" namedProduct="<<ww<<"\n";
  cout<<"same_bit=";
  for(int i=0;i<17;i++) cout<<(i?",":"")<<same[i];
  cout<<"\n";
  return (low==9448558 && lbTop==532848 && topLb==530485 && topTop==29848 && zz==10541739 && ww==10541801)?0:1;
}
