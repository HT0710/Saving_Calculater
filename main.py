class CALC:
    def __init__(self, fund):
        self.fund = fund
        self.apr = 0
        self.day = 0
        self.apy = 0
        self.calc = 0

    def get_calc(self):
        return self.calc

    def get_apy(self):
        return self.apy

    def set_fund(self, fund):
        self.fund = fund

    def set_apr(self, apr):
        self.apr = apr

    def set_apy(self, apy):
        self.apy = apy

    def set_day(self, day):
        self.day = day

    def annual_apr(self):
        self.calc = self.fund * (1 + self.apr / 100)
        return self.calc

    def annual_apy(self, day_compound):
        self.calc = self.fund * pow(1 + (self.apr / 100) / day_compound, day_compound)
        return self.calc

    def calc_apy(self, day_compound):
        self.apy = pow(1 + ((self.apr / 100) / day_compound), self.day / 365 * day_compound) * 100
        return self.apy

    def apr_decrease(self, apr_per_time, per_time: str, apr=None, day=None):
        """
        Calculate profit if apr decrease per time

        :param apr_per_time: How many apr decrease per time
        :param per_time: How long per decrease, must be String. Ex: 1 day, 2 week, 3 month, 4 year
        :param apr: Set or None for current object values
        :param day: Set or None for current object values
        :return: Calculate values
        """
        if apr is None:
            apr = self.apr
        if day is None:
            day = self.day
        self.calc = self.fund * (1 + apr / 100)
        return self.calc

    def apy_decrease(self, apr_per_time, day_per_time=1, apy=None, day=None):
        # self.calc = self.fund*(1+self.apr/day_per_compound)**(self.day/365*day_per_compound)
        pass


def main():
    calc = CALC(100)
    calc.set_apy(200)
    calc.set_apr(100)

    print(calc.annual_apy(365))


if __name__ == '__main__':
    main()
