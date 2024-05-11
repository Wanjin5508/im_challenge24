import json
import pandas as pd

class InstanceInput:
    def __init__(self, filepath, UseMainTask=False):
        # 在初始化时读取并解析 JSON 文件
        self.filepath = filepath
        self.ID = None
        self.Cohorts = None
        self.Days = None
        self.MaxRouteDuration = None
        self.MainTasks = []
        
        self.UseMainTask = UseMainTask  # 默认为 False

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
            return (f"Szenario Flexi\n-------------------\n"
                    f"Instance ID: {self.ID}\n"
                    f"Cohorts: {self.Cohorts}\n"
                    f"Days: {self.Days}\n"
                    f"Max Route Duration: {self.MaxRouteDuration}\n")
        
        # 如果使用 main task, 则输出所有属性
        main_tasks_summary = f"{len(self.MainTasks)} tasks loaded"
        return (f"Szenario Operative\n-------------------\n"
                f"Instance ID: {self.ID}\n"
                f"Cohorts: {self.Cohorts}\n"
                f"Days: {self.Days}\n"
                f"Max Route Duration: {self.MaxRouteDuration}\n"
                f"{main_tasks_summary}\n"
                f"Use Main Task: {self.UseMainTask}")
        
        
        
    def get_main_tasks_df(self) ->:
        # 仅当 UseMainTask 为 True 时，才将 MainTasks 转换为 DataFrame 并返回
        if self.UseMainTask:
            return pd.DataFrame(self.MainTasks)
        else:
            return "UseMainTask 未设置为 True。设置 UseMainTask 为 True 以将 MainTasks 输出为 DataFrame。"
        
        
        
