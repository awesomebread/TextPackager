import YamlReader

def getOrder():
    order = YamlReader.read('./order.yml')

    assert order, "No order.yml could be found"
    assert (order['title']), "Improperly formatted order.yml: Missing 'title'"
    assert (order['order']), "Improperly formatted order.yml: Missing 'order'"

    return order
