from datetime import datetime
import json
import random
import os
import sys
import time

class logGenerator:
    USERS = []
    ACTIVITIES = {}
    CD = os.environ["LOG_GENERATOR_DIR"]
    LogLevels = ["ALL" , "DEBUG" , "INFO" , "WARN" , "ERROR" , "FATAL" ,"OFF"]

    def __init__(self):
        self.getUsersAndActivities()
 
    def getUsersAndActivities(self):
        json_text = open(self.CD + 'data/Users.json', 'r').read()
        users = json.loads(json_text)
        for user in users:
            self.USERS.append({user["user_id"] : user["user_name"]})
            self.ACTIVITIES[user['user_name']] = user["ActivitiesPerformed"]
    
    def write_qps(self, dest, qps):
        sleep = 1.0 / qps
        while True:
            self.write(dest, 1)
            time.sleep(sleep)

    def getRandomUser(self,users):
        x= random.choice(users)
        idNo = int(x.keys()[0])
        name = str(x.values()[0])
        user = [idNo,name]
        return user
   
    def getActivitiesOfUser(self,data, user_name):
        activityList = data[user_name]
        return activityList
 
    def getRandomValue(self,loglevel):
        loglevel = random.choice(loglevel)
        return loglevel
 
    def write(self, dest, count):
        self.getUsersAndActivities()
        for i in range(count):
            user    = self.getRandomUser(self. USERS)
            user_id  = user[0]
            user_name = user[1]
            activities     = self.getActivitiesOfUser(self.ACTIVITIES, user_name)
            LogLevel = self.getRandomValue(self.LogLevels)
            date = datetime.now().strftime("%d/%b/%Y:%H:%M:%S -0800") # Hard-coded as Python has no standard timezone implementation
            dest.write("%(date)s   -------  [%(LogLevel)s]  ------   user[%(user_id)s  : %(user_name)s]  ----------  {Activities : %(activities)s}\n" % {'date': date, 'LogLevel': LogLevel, 'user_id': user_id, 'user_name': user_name, 'activities': activities})
            dest.flush()

LG = logGenerator()    
LG.write_qps(sys.stdout, 1)
