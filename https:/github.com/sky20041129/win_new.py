
import os 

def raid_windows_fw_update():
    '''
    Windows is base on python3
    '''

    os.system("storcli64.exe show |findstr /c:PRAID")
    os.system("storcli64.exe show |findstr /c:PSAS")

    x = int(input ("Please inpurt your controller number:"))

    lin= os.popen("dir /b |findstr /c:.bin").readlines()
    lin= os.popen("dir /b |findstr /c:.rom").readlines()
    print (lin)
    y = input ("Please input your file:")
    linefile = lin[int(y)].rstrip()


    if x < 1:
        print("Current version:")
        os.system(f"storcli64.exe /c{x} show |findstr /c:FW")
        print("-------------------------------")
        os.system(f"storcli64.exe /c{x} download file={linefile} noverchk")
        print("Update version:")
        os.system(f"storcli64.exe /c{x} show |findstr /c:FW")
        os.system("pause")

    else:
        print("Current version:")
        os.system(f"storcli64.exe /c{x} show |findstr /c:FW")
        print("-------------------------------")
        os.system(f"storcli64.exe /c{x} download file={linefile} noverchk")
        print("Update version:")
        os.system(f"storcli64.exe /c{x} show |findstr /c:FW")
        os.system("pause")


raid_windows_fw_update()

