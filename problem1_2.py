import json

# Open sample.json to read data:
json_file = open("sample.json", "r+")
data = json_file.read()
jsonObj = json.loads(data)

# A). Changing Protocol to udp:
jsonObj["featureConfigs"]["features"][2]['firewallRules']['firewallRules'][0]['application']['service'][0]['protocol'] =\
    "udp"

# B). Changing portgroupName:
jsonObj['vnics']['vnics'][2]['portgroupName'] = "EXT_VLAN_201b"

# C). Changing OSPF-enabled to True:
jsonObj["featureConfigs"]["features"][5]['ospf']['enabled'] = True

# D). Changing holdDownTimer Values:
jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][0]['holdDownTimer'] = \
    jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][0]['holdDownTimer'] +\
    jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][0]['keepAliveTimer']

jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][1]['holdDownTimer'] = \
    jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][1]['holdDownTimer'] +\
    jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][1]['keepAliveTimer']

jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][2]['holdDownTimer'] = \
    jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][2]['holdDownTimer'] +\
    jsonObj["featureConfigs"]["features"][5]['bgp']["bgpNeighbours"]["bgpNeighbours"][2]['keepAliveTimer']

# Closing sample.json file
json_file.close()

# Re-open sample.json file again to write Json_data:
with open('sample.json', 'w') as json_file:
    json_file.write(json.dumps(jsonObj))
