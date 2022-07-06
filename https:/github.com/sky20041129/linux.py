
import os 

def raid_linux_fw_update():
    '''
    linux is base on python2
    '''
    os.system("./storcli64 show |grep -i PRAID")
    os.system("./storcli64 show |grep -i PSAS")
    
    x = raw_input("Please inpurt your controller number:")

    os.system("ls |grep -i .bin")
    os.system("ls |grep -i .rom")

    y = raw_input("Please input your file:")


    if x < 1:
        #os.system("./storcli64 /c"+str(x)+ " "+"download file="+y+ " " + "noverchk")
        os.system("./storcli64 /c%s download file=%s noverchk" %(x,y))
        os.system("./storcli64 /c%s show |grep -i FW" %(x)
        #os.system("./storcli64 /c"+str(x)+ " "+ "|grep -i FW")

    else:
        os.system("./storcli64 /c%s download file=%s noverchk" %(x,y))
        os.system("./storcli64 /c%s show |grep -i FW" %(x)
        #os.system("./storcli64 /c"+str(x)+ " "+"download file="+y+ " " + "noverchk")
        #os.system("./storcli64 /c"+str(x)+ " "+ "|grep -i FW")


raid_linux_fw_update()

