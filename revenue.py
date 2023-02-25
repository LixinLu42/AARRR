class Revenue():
    def __init__(self) -> None:
        self.pay_user = 0
        self.active_user = 0

        self.APA = 0
        self.MAU = 0
        self.MPR = 0

        self.ARPU = 0
        self.revenue = 0
        self.user_num = 0

        self.ARPPU = 0
        self.pay_user_num = 0

        self.LTV = 0                    #生命周期价值，APRU * LT
        self.LT = 0                     #用户的生命周期，第一次使用时间 -- 最后一次使用时间，以月计。

    # 付费率
    def getPUR(self):
        self.PUR = self.pay_user / self.active_user
        return self.PUR

    # 活跃用户付费数
    def getAPA(self):
        self.APA = self.MAU * self.MPR
        return self.APA

    # 平均每用户收入
    def getARPU(self):
        self.ARPU = self.revenue / self.user_num
        return self.ARPU

    # 平均每付费用户收入
    def getARPPU(self):
        self.ARPPU = self.revenue / self.pay_user_num 
        return self.ARPPU

    # 生命周期价值
    def getLTV(self):
        self.LT = 0  
        self.LTV = self.ARPU * self.LT
        return self.LTV

