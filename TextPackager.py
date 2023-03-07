import sys

import FileFinder
import OrderProcessor
import OdtProcessor

sysArgs = sys.argv[1:]

print("***** Starting Text Packaging Processing")
if len(sysArgs) > 0:
    print("**** Processing args: " + str(sysArgs))
print()

order = OrderProcessor.getOrder()

print("*** Found order document")
print("*** Starting to combine")

baseDoc = OdtProcessor.getBaseDocument()
for doc in list(order["order"]):
    currentFile = FileFinder.findFile(doc)
    baseDoc = OdtProcessor.merge(currentFile, baseDoc)

baseDoc.save(order["title"] + ".odt")
