
def extractIpFromLog():
    try:
        ipList = {}
        with open("input.txt",'r') as file:
            data = file.readlines()
            for line in data:
                content = line.split(';')
                ip = extractIp(line)
                ipList[ip] +=1
            print(f"content: ",content)

    except Exception as exception:
        print(f"Error occured: ", str(exception))

def extractIp(input):
    ip = None
    for i in input:
        if(i.count('.') == 3):
            ip = i
    return ip

extractIpFromLog()
