import json

class InstanceInput:
    def __init__(self, filepath, UseMainTask=False):
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


    def __str__(self):
        '''
            打印实例信息
        '''
        
        if not self.UseMainTask:
            # 如果不使用 main task, 则只输出前4个属性
            return (f"Instance ID: {self.ID}\n"
                    f"Cohorts: {self.Cohorts}\n"
        
        
        main_tasks_summary = f"{len(self.MainTasks)} tasks loaded"
        return (f"Instance ID: {self.ID}\n"
                f"Cohorts: {self.Cohorts}\n"
                f"Days: {self.Days}\n"
                f"Max Route Duration: {self.MaxRouteDuration}\n"
                f"{main_tasks_summary}\n"
                f"Use Main Task: {self.UseMainTask}")