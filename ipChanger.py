import tkinter as tk
import subprocess
import csv
import time
   
root=tk.Tk()

root.title("FusTech IP Changer")
  
# declaring string variable 
# for storing name and password 
Device_var=tk.StringVar() 
IpAddress_var=tk.StringVar()
Subnet_var=tk.StringVar() 
Gateway_var=tk.StringVar()
dnsOne_var=tk.StringVar()
dnsTwo_var=tk.StringVar()

currentIpv4 = "192.168.x.x"
currentSubnet = "255.255.255.0"
currentGateway = "192.168.x.x"

def GetNetworkInfo():
    global currentIpv4
    global currentSubnet
    global currentGateway
    
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    tmpStr = "ipconfig"

    #CHANGE THIS ASAP ----------------Change to subprocess.Popen() and save output to txt file to read 
    tmpIpConfigs = subprocess.check_output(tmpStr, startupinfo=si)

    myTxt = tmpIpConfigs.decode("utf-8")

    #get current Ipv4 Address
    try:
        beforTxt = "Autoconfiguration IPv4 Address. . : "
        afterTxt = " "
        currentIpv4 = (myTxt.split(beforTxt))[1].split(afterTxt)[0]
    except:
        beforTxt = "IPv4 Address. . . . . . . . . . . : "
        afterTxt = "\r\n"
        currentIpv4 = (myTxt.split(beforTxt))[1].split(afterTxt)[0]    
    #Get current
    try:
        beforTxt = "Subnet Mask . . . . . . . . . . . : "
        afterTxt = "\r\n"
        currentSubnet = (myTxt.split(beforTxt))[1].split(afterTxt)[0]
    except:
        time.sleep(0.1)
    #Get current
    try:
        beforTxt = "Default Gateway . . . . . . . . . : "
        afterTxt = "\r\n\r\n"
        currentGateway = (myTxt.split(beforTxt))[1].split(afterTxt)[0]
    except:
        time.sleep(0.1)
   
GetNetworkInfo()    

def changeEthernetIp(tmpDevice, tmpIpAddress, tmpSubnet, tmpGateway, tmpDnsOne, tmpDnsTwo):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    #Changing Ip, Subnet and Gateway
    tmpStr = "netsh interface ipv4 set address name=" + str(tmpDevice) + " static " + str(tmpIpAddress) + " " + str(tmpSubnet) + " " + str(tmpGateway)
    subprocess.Popen(tmpStr, startupinfo=si)
    #Changing Preffered DNS Server
    tmpStr = "netsh interface ipv4 set dns name=" + str(tmpDevice) + " static " + str(tmpDnsOne)
    subprocess.Popen(tmpStr, startupinfo=si)
    #Changing Alternative DNS Server
    tmpStr = "netsh interface ipv4 add dns name =" + str(tmpDevice) + " " + str(tmpDnsTwo) + " index=2"
    subprocess.Popen(tmpStr, startupinfo=si)
    
    

def SubmitBut():
    GetNetworkInfo()
    tmpDevice = "\"" + Device_var.get() + "\""
    tmpIpAddress = IpAddress_var.get() 
    tmpSubnet = Subnet_var.get()
    tmpGateway = Gateway_var.get()
    tmpDnsOne =dnsOne_var.get()
    tmpDnsTwo =dnsTwo_var.get()

    changeEthernetIp(tmpDevice, tmpIpAddress, tmpSubnet, tmpGateway, tmpDnsOne, tmpDnsTwo)
      
# creating a label for  
# name using widget Label
device_label = tk.Label(root, text = 'Device', 
                      font=('calibre', 
                            10, 'bold')) 
# creating a entry for input 
# name using widget Entry
Device_var.set("Ethernet")
device_entry = tk.Entry(root, 
                      textvariable = Device_var,
                      font=('calibre',10,'normal')) 


   
# creating a label for password 
IpAddress_label = tk.Label(root, 
                       text = 'IP Address', 
                       font = ('calibre',10,'bold')) 
# creating a entry for password
IpAddress_var.set(currentIpv4)
IpAddress_entry=tk.Entry(root, 
                     textvariable = IpAddress_var, 
                     font = ('calibre',10,'normal')) 



# creating a label for  
# name using widget Label 
Subnet_label = tk.Label(root, text = 'Subnet', 
                      font=('calibre', 
                            10, 'bold')) 
# creating a entry for input 
# name using widget Entry
Subnet_var.set(currentSubnet)
Subnet_entry = tk.Entry(root, 
                      textvariable = Subnet_var,
                      font=('calibre',10,'normal')) 




# creating a label for  
# name using widget Label 
Gateway_label = tk.Label(root, text = 'Gateway', 
                      font=('calibre', 
                            10, 'bold')) 
# creating a entry for input 
# name using widget Entry
Gateway_entry = tk.Entry(root, 
                      textvariable = Gateway_var,
                      font=('calibre',10,'normal'))


# creating a label for  
# name using widget Label 
dnsOne_label = tk.Label(root, text = 'Preferred DNS Server', 
                      font=('calibre', 
                            10, 'bold')) 
# creating a entry for input 
# name using widget Entry 
dnsOne_entry = tk.Entry(root, 
                      textvariable = dnsOne_var,
                      font=('calibre',10,'normal'))

# creating a label for  
# name using widget Label 
dnsTwo_label = tk.Label(root, text = 'Alternative DNS Server', 
                      font=('calibre', 
                            10, 'bold')) 
# creating a entry for input 
# name using widget Entry 
dnsTwo_entry = tk.Entry(root, 
                      textvariable = dnsTwo_var,
                      font=('calibre',10,'normal'))





# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Fuckin Commit Cunt', 
                  command = SubmitBut)



   
# placing the label and entry in 
# the required position using grid 
# method 
device_label.grid(row=0,column=0) 
device_entry.grid(row=0,column=1) 
IpAddress_label.grid(row=1,column=0) 
IpAddress_entry.grid(row=1,column=1)
Subnet_label.grid(row=2,column=0) 
Subnet_entry.grid(row=2,column=1)
Gateway_label.grid(row=3,column=0) 
Gateway_entry.grid(row=3,column=1)
dnsOne_label.grid(row=4,column=0)
dnsOne_entry.grid(row=4,column=1)
dnsTwo_label.grid(row=5,column=0)
dnsTwo_entry.grid(row=5,column=1)

sub_btn.grid(row=6,column=1)

   
# performing an infinite loop  
# for the window to display 
root.mainloop() 
