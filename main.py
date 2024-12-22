#basic programs to scan for VNC's across the interwebs

import requests
from bs4 import BeautifulSoup # this import will be used to scrape one of the sites as there is no API
import os

#coming soon
#def idtoip():
    #vnc_api = f"https://computernewb.com/vncresolver/api/scans/vnc/search?country={country}" 

    #r = requests.get(vnc_api)
    #print("\nAPI Status\n\n", r.status_code, "\n")
    #print("VNC Output\n\n", r.text, "\n\n")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
██╗   ██╗███╗   ██╗ ██████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██║   ██║████╗  ██║██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║   ██║██╔██╗ ██║██║         ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚██╗ ██╔╝██║╚██╗██║██║         ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
 ╚████╔╝ ██║ ╚████║╚██████╗    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
  ╚═══╝  ╚═╝  ╚═══╝ ╚═════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
          
                                Made by: RobinCodes''')
    
    country = input("\nCountry code scan for VNC's: ")
    print("")
    #check for existing ip and ports so if duplicates are found they are not outputted twice
    existing_entries = set()
    try:
        with open('vncs.txt', 'r') as file:
            existing_entries = {line.strip() for line in file}
    except FileNotFoundError:
        pass
    output_lines = []

    #website we will be scraping, using the lastest 500 VNC's
    vnc_wtf = f"https://vnc.wtf/search?query=host.country+%3D+%22{country}%22+ORDER+BY+services.updated_at+DESC&amt=500"

    r = requests.get(vnc_wtf)
    
    soup = BeautifulSoup(r.text, 'html.parser')

    links = soup.find_all('a', href=True)

    for link in links:
        host_info = link['href'].split('/host/')[1]
        
        ip, port = host_info.split('#')

        output = (f"IP: {ip} Port: {port}")

        if output not in existing_entries:  
            with open('vncs.txt', 'a') as file:
                file.write(f"{output}\n")  # Write the output to the file
        output_lines.append(output)
        
    print("VNC list saved to 'vncs.txt'")

if __name__ == "__main__":
    main()
