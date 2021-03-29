#Author: Maria Ferrara 
#26/03/2021

#Import libraries 
import operator


# This function will read the text file, line by line, and extract the IPs
# The IPs will be saved into a dict
def analyse_log(filename):
    file=open(filename, 'r')
    IPs = dict()
   
    with open(filename, "r") as f:
        line = file.readline()
        lines = 0

        while line:
            print("Line " + str(lines) + ": " + line)
            lines += 1
        
            # Because of the log format, the IP Addres is separated from other data by a '-'
            # We can split each line by that character
            
            splitted = line.split(' - ')
            # The ip address is going to be the first element
            ip_str = splitted[0]
            if ip_str:
                print(ip_str)
                IPs[ip_str] = IPs.get(ip_str, 0) + 1
            
            line = file.readline()
        print("Read " + str(lines) + " IP-Addresses.")
        
    return IPs

# This function will extract the key with the higher value from a dict
def find_most_frequent(IPS_dict):
    return max(IPS_dict.items(), key=operator.itemgetter(1))[0]


def main(): 
    filename = r'C:\Users\marif\Downloads\Final\sample_log_3.txt' # define the file name
    
    IPs = analyse_log(filename) # Construct the dictionary

    ip_mf = find_most_frequent(IPs)  # Find most frequent
    print('The most frequent IP is ' + ip_mf + ' with ' + str(IPs[ip_mf]) + ' records.')

if __name__ == "__main__":
    main()
