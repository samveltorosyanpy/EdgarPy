def create_at(msg):
    stop = True
    while True:
        if stop is True:
            for x in msg:
                if x not in '0123456789':
                    print("ogtagorceq miayn tver")
                    msg = input('krkin porceq: -> ')
                    stop = False
                    break

                if stop is True:
                    return True
                else:
                    stop = True

def car_name(msg):
    stop = True
    while True:
        for x in msg:
            if x in '!@#$%^&*()_+={[}]':
                print('duq cheq karox ogtagorcel nshaner')
                msg = input('krkin porceq: -> ')
                stop = False
                break

            if stop is True:
                return True
            else:
                stop = True

def car_model(msg):
    stop = True
    while True:
        for x in msg:
            if x in '!@#$%^&*()_+={[}]':
                print('duq cheq karox ogtagorcel nshaner')
                msg = input('krkin porceq: -> ')
                stop = False
                break

            if stop is True:
                return True
            else:
                stop = True

def car_description(msg):
    stop = True
    while True:
        for x in msg:
            if x in '!@#$%^&*()_+={[}]':
                print('duq cheq karox ogtagorcel nshaner')
                msg = input('krkin porceq: -> ')
                stop = False
                break

            if stop is True:
                return True
            else:
                stop = True