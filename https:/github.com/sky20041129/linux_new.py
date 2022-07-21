
import os 

def raid_linux_fw_update():
    '''
    Linux is base on python2
    '''
    os.system("./storcli64 show |grep -i PRAID")
    os.system("./storcli64 show |grep -i PSAS")
    
    x = raw_input("Please inpurt your controller number:")

    lin = os.popen("ls |grep -i .bin").readlines()
    lin = os.popen("ls |grep -i .rom").readlines()
    print (lin)
    y = raw_input("Please input the line of file:")
    linefile = lin[int(y)].rstrip()

    if x < 1:
        print("Current version:")
        os.system("./storcli64 /c%s show |grep -i FW" %(x))
        os.system("./storcli64 /c%s download file=%s noverchk" %(x,linefile))
        print("Update version:")
        os.system("./storcli64 /c%s show |grep -i FW" %(x))
       

    else:
        print("Current version:")
        os.system("./storcli64 /c%s show |grep -i FW" %(x))
        os.system("./storcli64 /c%s download file=%s noverchk" %(x,linefile))
        print("Update version:")
        os.system("./storcli64 /c%s show |grep -i FW" %(x))


raid_linux_fw_update()

