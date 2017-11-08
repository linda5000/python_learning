from source.recharge_test import RechargeTest
from source.register_test import RegisterTest

class runner:
    def __init__(self,test_interface):
        self.test_interface = test_interface


    def run(self):
        interface = {
            'recharge':RechargeTest,
            'register':RegisterTest
        }

        interface[self.test_interface]().run()


def main():
    r = runner('recharge')
    r.run()
    r = runner('register')
    r.run()

if __name__ == '__main__':
    main()

