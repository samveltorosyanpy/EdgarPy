from datetime import datetime
from CarsApp_das_36_37_38_39.db.User import UserClass
def val_date(msg):
    while True:
        try:
            birthdate = datetime.strptime(msg, '%Y-%m-%d')
            if datetime.now().year - birthdate.year > 9:
                return True
            else:
                print("duq der cheq karx grancvel mer cragrum, duq shat poqr eq")
                return False
        except ValueError:
            msg = input("veranayeq dzer grvac taretivy, ev greq nshvac formatov (YYYY-MM-DD): -> ")


def val_login(msg):
    stop = True
    while True:
        if msg in UserClass().get_user_logins():
            print("ays loginy arden goyutyun uni, porceq urishy")
            msg = input("stexceq login: -> ")
            stop = False

        if stop is True:
            for w in msg:
                if w in "$?*&^!#)(":
                    print("duq cheq karox ogtagorcel ays nshanery $?*&^!#)(")
                    msg = input("stexceq login: -> ")
                    stop = False
                    break

        if len(msg) < 6 or len(msg) > 20:
            print("logini mech chi karox linel 6 pakas kam 20 avel nish")
            msg = input("stexceq login: -> ")
            stop = False

        if stop is True:
            return True
        else:
            stop = True


def val_password(pass1, pass2):
    stop = True
    while True:
        if stop is True:
            for w in pass1:
                if w in "$?*&^!#)(":
                    print("duq cheq karox ogtagorcel ays nshanery $?*&^!#)(")
                    pass1 = input("stexceq password: -> ")
                    pass2 = input("krkneq nor paroly: -> ")
                    stop = False
                    break

        if (len(pass1) < 6 or len(pass1) > 20) and stop is True:
            print("logini mech chi karox linel 6 pakas kam 20 avel nish")
            pass1 = input("stexceq password: -> ")
            pass2 = input("krkneq nor paroly: -> ")
            print("xndiry 2 rd  puli mecha: -> ")

            stop = False

        if stop is True:
            s = False
            for x in pass1:
                if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    s = True
                    break

            if s is False:
                print("oktagorceq mecatar")
                pass1 = input("stexceq password: -> ")
                pass2 = input("krkneq nor paroly: -> ")

                stop = False

        if pass1 != pass2 and stop is True:
            print("erkrord angam sxal eq grel paroly")
            pass2 = input("krkneq nor paroly: -> ")

        if stop is True:
            return True
        else:
            stop = True

def val_phone(msg):
    user_phone = []
    stop = True

    while True:
        if msg in user_phone:
            print('nman hamar goyutyun uni')
            msg = input('noric greq: -> ')
            stop = False

        if stop is True:
            for x in msg:
                if x not in '0123456789':
                    print('duq cheq karox ogtagorcel tarer ev nisher ')
                    msg = input('krkin porceq (+374): -> ')
                    stop = False
                    break

        if len(msg) < 6 or len(msg) > 9:
             print('hamari erkarutyuny chpetqe cacr lini 6ic ev mec 20ic')
             msg = input('krkin porceq (+374): -> ')
             stop = False

        if stop is True:
            return True
        else:
            stop = True





















