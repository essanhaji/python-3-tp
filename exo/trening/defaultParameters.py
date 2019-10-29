import datetime as dt


def currentTime(record, time=dt.datetime.now()):
    string = str(record) + "  " + str(time)
    return string


def enterParameters(*parameters):
    total = ''
    for index in parameters:
        total += str(index)
    return total


print(enterParameters(1, 2, 'ii'))
print(currentTime(414))
