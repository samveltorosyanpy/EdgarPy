from das_35_class import Premium

A1_address = Premium(address="A1", level=9)
A2_address = Premium(address="A2", level=9)

# A1_address.matakararum()


A1_address.lift(start_leve=6, end_level=8)
A2_address.lift(start_leve=9, end_level=1)

A1_address.lift(start_leve=9, end_level=0)
A2_address.lift(start_leve=1, end_level=6)

