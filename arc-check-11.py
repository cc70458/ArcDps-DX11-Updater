import os
import requests
import urllib.request
import wget
import colorama
colorama.init()

# Get current arc md5
url = 'https://www.deltaconnected.com/arcdps/x64/d3d9.dll' 
response = requests.get(url+'.md5sum')
curr_arc = response.text.split("  ")[0]

def get_arc (c,o):
    # upsert arc!
    print(colorama.Back.BLUE+'Current arc hash:'+c+colorama.Style.RESET_ALL)
    if(not(o) or c!=o):
        if(not(not(o)) and c!=o):
            print(colorama.Fore.YELLOW+"Arc Needs Updating"+colorama.Style.RESET_ALL)
            print("Deleting OLD ArcDPS..")
            os.system('del d3d11.dll')

        print("Downloading NEW ArcDPS")
        wget.download('https://www.deltaconnected.com/arcdps/x64/d3d9.dll')
        os.system('ren d3d9.dll d3d11.dll')
        print(colorama.Back.GREEN+"Done!"+colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.GREEN+'Arc is up to date!'+colorama.Style.RESET_ALL)
        quit()

if(os.path.exists('d3d11.dll')):
    print(colorama.Back.MAGENTA+'Opening d3d11.dll for analysis'+colorama.Style.RESET_ALL)
    stream = os.popen('certutil -hashfile d3d11.dll MD5')
    output = stream.read()
    my_arc = output.split('\n')[1]
    print(colorama.Back.CYAN+"My arc hash     :"+my_arc+colorama.Style.RESET_ALL)
    get_arc(curr_arc,my_arc)
    # arc exists
else:
    print(colorama.Back.RED+"ERR"+colorama.Style.RESET_ALL+" We can't find a current d3d11.dll in this directory.\nWould you like to download one instead?\n(y/n)")
    ans = input()
    if(str(ans).lower() != 'y'):
        #no arc, don't download
        print(colorama.Fore.RED+'Exiting'+colorama.Style.RESET_ALL)
        quit()
    else:
        #just download new arc
        get_arc(curr_arc,False)
