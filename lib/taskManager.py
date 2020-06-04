# -*-coding:UTF-8 -*-
import os,time
import config as CONFIG
import lib.taskFileHandler as taskFileHandler
from lib.runner import UiRunner, ApiRunner

class uiTaskManager():
    def __init__(self,task):
        self.id = task['id']
        self.runSlave = task['slave']
        self.version = task['version']
        self.project = task['project']
        self.cases = task['cases']
        self.work_dir = None
    
    def _create_work_dir(self):
        wt = time.strftime("%Y-%m-%d-%H-%M-%S")
        self.work_dir = os.path.join(CONFIG.LOCAL_CASE_PATH,self.version,wt)
        
    def download_case(self):
        self._create_work_dir()
        taskFileHandler.download_tasklist(self.cases,self.work_dir)
    
    def serach_case_ftppath(self,caselist):
        #寻找uicase路径并返回
        for i in caselist:
            pass
    
    def run(self):
        self.download_case()
        runner = UiRunner(task)
        return runner.run(casedir)
