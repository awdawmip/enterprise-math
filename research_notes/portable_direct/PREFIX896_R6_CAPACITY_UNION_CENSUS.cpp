#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using i64=long long;
constexpr i64 P=32, N=1LL<<P, TRANS=(P+1)*N;
constexpr int A=262145, B=524287, QN=131072;
int main(){
  const set<int> oldrows={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285};
  set<int> axis;
  for(int q=A;q<=B;q+=2) for(int h=1;h<P;h++){
    i64 pow=1LL<<h;
    if((pow-1)%q==0||(pow+1)%q==0){axis.insert(q);break;}
  }
  set<int> strips;
  for(int j=0;j<256;j++){strips.insert(400011+2*j); strips.insert(480011+2*j);}
  set<int> U=oldrows;
  U.insert(axis.begin(),axis.end()); U.insert(strips.begin(),strips.end());
  assert(oldrows.size()==16&&axis.size()==24&&strips.size()==512&&U.size()==552);
  vector<uint8_t> isU(B+1);
  for(int u:U)isU[u]=1;
  auto capacity_neighbors=[](i64 q)->i64 {
    i64 hi=min<i64>(B,(TRANS-1)/q);
    return hi<A?0:(hi-A)/2+1;
  };
  i64 capacity=0, capacity_U_rows=0, capacity_UU=0;
  for(i64 q=A;q<=B;q+=2)capacity+=capacity_neighbors(q);
  for(int u:U){capacity_U_rows+=capacity_neighbors(u);
    for(int v:U)capacity_UU+=(i64)u*v<TRANS;
  }
  i64 rowcol=2LL*U.size()*QN-(i64)U.size()*U.size();
  i64 rowcol_in_capacity=2*capacity_U_rows-capacity_UU;
  i64 rowcol_outside_capacity=rowcol-rowcol_in_capacity;
  i64 zz_outside_capacity=0, zz_outside_capacity_outside_U=0, zz_outside_capacity_inside_U=0;
  i64 candidate_pairs=0;
  for(i64 g=35;g<=B;g+=2){
    i64 amin=(A+g-1)/g, amax=B/g;
    amin+=!(amin&1); amax-=!(amax&1);
    for(i64 a=amin;a<=amax;a+=2){
      const i64 qa=g*a;
      i64 bmin=max(amin,(TRANS+g*g*a-1)/(g*g*a));
      i64 bmax=min(amax,(N-1)/(g*a));
      bmin+=!(bmin&1); bmax-=!(bmax&1);
      for(i64 b=bmin;b<=bmax;b+=2){
        ++candidate_pairs;
        if(gcd(a,b)!=1)continue;
        ++zz_outside_capacity;
        if(isU[qa]||isU[g*b])++zz_outside_capacity_inside_U;
        else ++zz_outside_capacity_outside_U;
      }
    }
  }
  const i64 total=capacity+rowcol_outside_capacity+zz_outside_capacity_outside_U;
  assert(capacity==7364142398LL);
  assert(capacity_U_rows==18312436LL&&capacity_UU==11996);
  assert(rowcol==144398784LL&&rowcol_outside_capacity==107785908LL);
  assert(zz_outside_capacity==95365328LL);
  assert(zz_outside_capacity_inside_U==1050532LL);
  assert(zz_outside_capacity_outside_U==94314796LL);
  assert(total==7566243102LL);
  cout<<"{\"schema\":\"PREFIX896_R6_CAPACITY_UNION_V1\","
      <<"\"p\":"<<P<<",\"N\":"<<N<<",\"named_trajectory_count\":"<<TRANS
      <<",\"modulus_count\":"<<QN<<",\"parameter_pairs\":"<<(i64)QN*QN
      <<",\"old_rows\":"<<oldrows.size()<<",\"axis_moduli\":"<<axis.size()
      <<",\"strip_moduli\":"<<strips.size()<<",\"union_special_moduli\":"<<U.size()
      <<",\"capacity_positive_pairs\":"<<capacity
      <<",\"capacity_special_first_port\":"<<capacity_U_rows
      <<",\"capacity_special_both_ports\":"<<capacity_UU
      <<",\"special_row_column_pairs\":"<<rowcol
      <<",\"special_outside_capacity\":"<<rowcol_outside_capacity
      <<",\"lcm_collision_outside_capacity\":"<<zz_outside_capacity
      <<",\"lcm_outside_capacity_touching_special\":"<<zz_outside_capacity_inside_U
      <<",\"lcm_outside_capacity_outside_special\":"<<zz_outside_capacity_outside_U
      <<",\"gcd_candidates_inspected\":"<<candidate_pairs
      <<",\"deduplicated_union\":"<<total
      <<",\"unexcluded\":"<<(i64)QN*QN-total
      <<",\"increment_relative_to_prefix895\":"<<total-351837696LL
      <<"}"<<'\n';
}
