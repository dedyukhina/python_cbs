from collections import OrderedDict
from collections import defaultdict
from collections import ChainMap

# Ознайомтеся за допомогою документації з класами OrderedDict, defaultdict та ChainMap модуля collections.


new_dict = OrderedDict()

new_dict["first"] = 'hey'
new_dict["second"] = 1
new_dict["third"] = 'order'

print(new_dict)

new_dict_1 = defaultdict(int)

new_dict_1["film1"] = 1
new_dict_1["fiml2"] = 2

print(new_dict_1["film3"])

new_dict_3 = ChainMap(new_dict, new_dict_1)
print(new_dict_3)

print(new_dict_3['film1'])
