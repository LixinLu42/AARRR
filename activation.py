class Activation():
    def __init__(self, k, invit_num, accept_num, data_file) -> None:
        #invit_num, accept_num??选输入或者自己???算
        self.DAU = 0     #日活用户数
        self.WAU = 0     #周活用户数
        self.MAU = 0     #月活用户数
        self.DAOT = 0    #日均使用时长
        self.user_stickiness = 0.0   #用户粘性
        self.data_file = data_file

    # 处理数据，返回类内变量
    def process_data():
        pass