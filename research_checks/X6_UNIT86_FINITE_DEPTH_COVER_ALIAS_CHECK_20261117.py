#!/usr/bin/env python3
"""Exact integer checks of first native Cell-return alias through finite diagonal covers.

Research-only six-axis signed X6; reuses the verified Unit85 endpoint census.
Finite covers are derived observers, never alternate native Cell identities.
"""
from math import factorial
import json
from X6_UNIT85_THREE_RETURN_SEMANTICS_CHECK_20261117 import run as signed_census


def require(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def first_alias_extra(modulus):
    require(type(modulus) is int and modulus>=1, 'finite positive modulus')
    return 2*factorial(6*modulus)//(factorial(modulus)**6)


def compute():
    native=signed_census()['results']
    first_alias=[]
    table=[]
    checked=0
    for m in range(1,6):
        first_alias.append({'modulus':m,'first_alias_length':6*m,
                            'exact_extra_signed_return_mass':first_alias_extra(m),
                            'diagonal_alias_endpoints':[[-m]*6,[m]*6]})
        for row in native:
            L=row['length']
            mass=sum(count for h,count in row['signed_diagonal_depth_multiplicity'].items()
                     if int(h)%m==0)
            require(mass>=row['signed_native_zero'], f'lower bound m={m} L={L}')
            require(mass<=row['signed_minzero_relative_return'], f'upper bound m={m} L={L}')
            if L<6*m:
                require(mass==row['signed_native_zero'], f'premature alias m={m} L={L}')
            if L==6*m:
                require(mass-row['signed_native_zero']==first_alias_extra(m),
                        f'first alias discrepancy m={m} L={L}')
            table.append({'modulus':m,'length':L,'finite_cover_return':mass,
                          'native_cell_return':row['signed_native_zero'],
                          'extra_over_native':mass-row['signed_native_zero']})
            checked+=1
    by={(r['modulus'],r['length']):r for r in table}
    require(by[(1,6)]['finite_cover_return']==21360, 'm=1 length6')
    require(by[(2,12)]['finite_cover_return']==8190738864, 'm=2 length12')
    return {'schema':'X6_UNIT86_FINITE_DEPTH_SIGNED_RETURN_ALIAS_V1',
            'native_model':'P000 V5 signed six-axis primitive labeled steps',
            'observer':'rho(z), min(z) modulo positive integer m',
            'first_alias_table':first_alias,
            'bounded_census':table,'checked_cover_horizons':checked,
            'test_horizons':'0..12','failures':0,
            'review':'AUTHOR_EXACT_UNREVIEWED_NOT_ADMITTED'}

if __name__=='__main__':
    print(json.dumps(compute(),sort_keys=True,separators=(',',':')))
