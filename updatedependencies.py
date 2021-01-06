from lxml import etree
from collections import defaultdict

root = etree.parse('pom.xml') #or .parse('pom.xml') if you read it from that file
tree = etree.ElementTree(root)

depend = tree.xpath("//*[local-name()='dependency']")
dependencyInfo = defaultdict(dict)

for dep in depend:
    infoList = []
    for child in dep.getchildren():
        infoList.append(child.tag.split('}')[1])
        infoList.append(child.text)


    dependencyInfo[infoList[1]].update({infoList[2] : infoList[3],infoList[4] : infoList[5]})

dependencyInfo

#TODO
#- Go to POM
#- Go to dependencies
#- For each dependency
#    - check if it has a version tag
#    - if yes
#        - store group id, artifact id and version
#        - use group and artifact id to find version on maven or local repo
#        - match versions
#        - if version is updated
#            -update version
    