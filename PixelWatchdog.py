import time
import win32serviceutil

#TODO: add logger..

def pxlRestartServiceIfNotHealthy(serviceName,
                isServiceHealthyCallback,
                serviceIsHealthyCallback=None,
                serviceNotHealthyCallback=None,
                maxRetries=3, retryTimeoutSec=1):

    currentRetryNum = 0

    while (currentRetryNum < maxRetries):
        print('Retry number {0}:'.format(str(currentRetryNum)))

        if (isSerivceHealthyCallback()):
            print("- Service: '{0}' is OK".format(serviceName))
            serviceIsHealthyCallback()
            break

        print("- Service: '{0}' is NOT responding".format(serviceName))
        time.sleep(retryTimeoutSec)
        currentRetryNum += 1

    if (currentRetryNum >= maxRetries):
        print("Service: '{0}' is not healthy".format(serviceName))
        serviceNotHealthyCallback()
        _pxlRestartService(serviceName)


def _pxlRestartService(serviceName):
    print("Trying to restart service: '{0}'".format(serviceName))
    try:
        win32serviceutil.RestartService(serviceName)
        print("'{0}' is restarted".format(serviceName))
    except win32serviceutil.error as e:
        print("Could not restart service: '{0}'".format(serviceName))
        print(e)

def serviceNotHealthyCallback():
    print('i am ill, efshar gimel?')

def isSerivceHealthyCallback():
    return False

pxlRestartServiceIfNotHealthy('XboxNetApiSvc', isSerivceHealthyCallback, serviceNotHealthyCallback=serviceNotHealthyCallback)
