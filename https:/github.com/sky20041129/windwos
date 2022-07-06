
import os 

def raid_windows_fw_update():


    os.system("storcli64.exe show |findstr /c:PRAID")
    os.system("storcli64.exe show |findstr /c:PSAS")

    x = int(input ("Please inpurt your controller number:"))

    os.system("dir |findstr /c:.bin")
    os.system("dir |findstr /c:.rom")

    y = input ("Please input your file:")


    if x < 1:
        os.system(f"storcli64.exe /c{x} download file={y} noverchk")
        os.system(f"storcli64.exe /c{x} show |findstr /c:FW")
        os.system("pause")

    else:
        os.system(f"storcli64.exe /c{x} download file={y} noverchk")
        os.system(f"storcli64.exe /c{x} show |findstr /c:FW")
        os.system("pause")


raid_windows_fw_update()

