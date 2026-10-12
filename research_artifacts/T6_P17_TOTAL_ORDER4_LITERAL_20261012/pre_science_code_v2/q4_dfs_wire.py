"""New T6Q4DFS1 byte codec, no mathematical execution or authority."""
import struct
MAGIC=b'T6Q4DFS1'
COUNT=30992

def uleb(value):
    if type(value) is not int or value<0: raise ValueError('Nonnegative integer required')
    output=bytearray()
    while True:
        part=value&127;value>>=7;output.append(part|(128 if value else 0))
        if not value:return bytes(output)

def header(common_sha,input_sha):
    if len(common_sha)!=64 or len(input_sha)!=64:raise ValueError('Complete SHA256 required')
    raw=MAGIC+bytes.fromhex(common_sha)+bytes.fromhex(input_sha)+struct.pack('<I',COUNT)
    if len(raw)!=76:raise ValueError('Exact76byteheader')
    return raw

def encode_actions(actions):
    if not 2<=len(actions)<=272 or len(actions)%2:raise ValueError('Complete two-edge tree action count')
    packed=bytearray((len(actions)+3)//4)
    for i,action in enumerate(actions):
        if type(action) is not int or not 0<=action<=3:raise ValueError('Invalid action')
        packed[i//4]|=action<<(2*(i%4))
    return uleb(len(actions))+packed

def decode_record(data,offset,bound):
    start=offset;value=0;shift=0
    while True:
        if offset>=len(data) or shift>14:raise ValueError('Truncated/excessive ULEB')
        b=data[offset];offset+=1;value|=(b&127)<<shift
        if not b&128:break
        shift+=7
    if data[start:offset]!=uleb(value) or not 2<=value<=bound or value%2:
        raise ValueError('Noncanonical/excessive/odd action count')
    length=(value+3)//4
    if offset+length>len(data):raise ValueError('Truncated action stream')
    packed=data[offset:offset+length]
    if value%4 and packed[-1]>>(2*(value%4)):raise ValueError('Nonzero action padding')
    return [(packed[i//4]>>(2*(i%4)))&3 for i in range(value)],offset+length
