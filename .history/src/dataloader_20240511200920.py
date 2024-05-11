import json

class InstanceInput:
    def __init__(self, filepath, Use):
        # 在初始化时读取并解析 JSON 文件
        self.filepath = filepath
        self.ID = None
        self.Cohorts = None
        self.Days = None
        self.MaxRouteDuration = None
        self.MainTasks = []
        self.UseMainTask = False  # 默认为 False

        self.load_data()

    def load_data(self):
        # 读取 JSON 文件并将内容设置到类的属性中
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            self.ID = data.get('ID')
            self.Cohorts = data.get('Cohorts')
            self.Days = data.get('Days')
            self.MaxRouteDuration = data.get('MaxRouteDuration')
            self.MainTasks = data.get('MainTasks')


