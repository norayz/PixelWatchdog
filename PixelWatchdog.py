def pxlWatchdog(serviceName,
                isSerivceHealthyCallback, serverIsHealthyCallback=None, serviceNotHealthyCallback=None,
                maxRetries=3, retryTimeoutMS=1000):
    if (isSerivceHealthyCallback()):
        print(serviceName + ' is healthy')
    else:
        print(serviceName + ' not healthy')

def isSerivceHealthyCallback():
    return True

pxlWatchdog('yaronsss', isSerivceHealthyCallback)
