import sched, time
from Analytics import Analytics
from datetime import datetime
import os
from analyticConfigs import config


scheduler_obj = sched.scheduler(time.time, time.sleep)
def start_App(sc): 
    print("*******************************************  Job Started at {}  **".format(datetime.now()))
    Analytics().run_Analytic_Engine()
    print("*******************************************  Job Finished at {}  **",datetime.now())
    scheduler_obj.enter(int(config['Start_Delay']),int( config['Interval']), start_App, (sc,))

scheduler_obj.enter(int(config['Start_Delay']),int( config['Interval']), start_App, (scheduler_obj,))
scheduler_obj.run()

Analytics().run_Analytic_Engine()


