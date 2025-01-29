mydict={
        "name": "Hashith",
        "id": 111,
        "domain": ["devops", "cloud engineer", "SRE"],
        "tools":{"os": ["Linux", "Windows"], "cloud": "AWS"}
        }
print(mydict)
print(mydict["id"])
print(mydict["domain"])
print(mydict["domain"][1])
print(mydict["tools"])
print(mydict["tools"]["os"])
print(mydict["tools"]["os"][1])
mydict["place"]="Bengaluru"
print(mydict)
mydict1={
        "name1": "Divya"
        }
mydict.update(mydict1)
print(mydict)
