class Refer():
    def __init__(self, k, invit_num, accept_num, data_file) -> None:
        #invit_num, accept_num可选输入或者自己计算
        self.k = k
        self.invit_num = invit_num
        self.accept_num = accept_num
        self.data_file = data_file

    # 处理数据，返回accept_num，data_file，
    def process_data():
        pass
        

    def referFactorK(self):
        self.k = self.invit_num * self.accept_num
        return self.k

