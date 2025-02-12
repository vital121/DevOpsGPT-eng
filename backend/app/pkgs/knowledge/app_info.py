from app.pkgs.knowledge.app_info_basic import AppInfoBasic
from app.pkgs.knowledge.app_info_pro import AppInfoPro
from config import GRADE


def getAppArchitecture(appID):
    if GRADE == "base":
        obj = AppInfoBasic()
    else:
        obj = AppInfoPro()
        
    return obj.getAppArchitecture(appID)

def getServiceSwagger(appID, serviceName):
    if GRADE == "base":
        obj = AppInfoBasic()
    else:
        obj = AppInfoPro()
        
    return obj.getServiceSwagger(appID, serviceName)

def getServiceBasePrompt(appID, serviceName):
    if GRADE == "base":
        obj = AppInfoBasic()
    else:
        obj = AppInfoPro()
        
    return obj.getServiceBasePrompt(appID, serviceName)

def getServiceIntro(appID, serviceName):
    if GRADE == "base":
        obj = AppInfoBasic()
    else:
        obj = AppInfoPro()
        
    return obj.getServiceIntro(appID, serviceName)

def getServiceLib(appID, serviceName):
    if GRADE == "base":
        obj = AppInfoBasic()
    else:
        obj = AppInfoPro()
        
    return obj.getServiceLib(appID, serviceName)

def getServiceStruct(appID, serviceName):
    if GRADE == "base":
        obj = AppInfoBasic()
    else:
        obj = AppInfoPro()
        
    return obj.getServiceStruct(appID, serviceName)

def getServiceSpecification(appID, serviceName, LibName):
    if GRADE == "base":
        obj = AppInfoBasic()
    else:
        obj = AppInfoPro()
        
    return obj.getServiceSpecification(appID, serviceName, LibName)