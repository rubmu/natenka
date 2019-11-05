import sys
import textfsm
from tabulate import tabulate
import io
from pprint import pprint

template = '''Value Name (\w+)
Value Type (\w+)
Value Required,List Binding (\w+)
Value Description (\w+)

Start
  ^---- -> Data

Data
  ^\S+ -> Continue.Record
  ^${Name} +${Type} +${Binding} +${Description}
  ^ +${Binding}
'''

f = io.StringIO(template)

output = '''
Name        Type       Binding    Description
----------  ---------  ---------  -------------
EVERFLOW    MIRROR     Ethernet1  EVERFLOW
                       Ethernet2
                       Ethernet3
                       Ethernet4
SNMP_ACL    CTRLPLANE  SNMP       SNMP_ACL
SSH_ONLY    CTRLPLANE  SSH        SSH_ONLY
EVERFLOWV6  MIRRORV6   Ethernet1  EVERFLOWV6
                       Ethernet2
                       Ethernet3
                       Ethernet4
'''

re_table = textfsm.TextFSM(f)
header = re_table.header
result = re_table.ParseText(output)
print(tabulate(result, headers=header), end='\n\n')

# create dict
results = []
for row in result:
    results.append(dict(zip(header, row)))
pprint(results)

