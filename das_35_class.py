import time

class Premium:
    def __init__(self, address, level):
        self.address = address
        self.level = level
        self.lift_level = 0

    def lift(self, start_leve, end_level):

        if self.lift_level < start_leve:
            self.lift_up(start_leve)
        elif self.lift_level > start_leve:
            self.lift_down(start_leve)

        if self.lift_level > end_level:
            self.lift_down(end_level)
        elif self.lift_level < end_level:
            self.lift_up(end_level)

    def lift_up(self, lift_level_up):
        print('lifty barcanuma: ', end=' ')
        for a in range(self.lift_level, lift_level_up+1):
            print(a, end=' ')
            time.sleep(0.1)
            self.lift_level = a
        print('\n')

    def lift_down(self, lift_level_down):
        print('lifty ichnuma: ', end=' ')
        for a in range(self.lift_level, lift_level_down-1, -1):
            print(a, end=' ')
            time.sleep(0.1)
            self.lift_level = a
        print('\n')




    def matakararum(self):
        self.jri_matakararum()
        self.hosaanqi_matakararum()
        self.gazi_matakararum()

    def jri_matakararum(self):
        print("jury hasav :", end=' ')
        for i in range(self.level+1):
            print(i, end=' ')
            time.sleep(0.3)
        print('\n', end='')

    def hosaanqi_matakararum(self):
        print(f"hosanqy ka michev {self.level}")


    def gazi_matakararum(self):
        print(f"gazy hasav :", end=" ")
        for i in range(self.level + 1):
            print(i, end=' ')
            time.sleep(0.1)
        print('\n', end='')

    def get_info(self):
        return """


        """

A1_address = Premium(address="A1", level=9)
A2_address = Premium(address="A2", level=9)

# A1_address.matakararum()

A1_address.lift(start_leve=6, end_level=8)
A2_address.lift(start_leve=9, end_level=1)

A1_address.lift(start_leve=9, end_level=0)
A2_address.lift(start_leve=1, end_level=6)

#                    poxvox
# qar
# harkeri qanak
# senqi guyny
# hasce
#                    gorcoxutyune
# jri matakararim
# hossanqi matakararum
# gaz matakararum
# lift