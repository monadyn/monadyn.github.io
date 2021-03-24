import socket,struct
 
'''
 转换为子网地址,并检验和输出正确的子网地址
 192.168.2.1 -> 192.168.2.1/255.255.255.255
 192.168.2.1/24 -> 192.168.2.0/255.255.255.0
 192.168.2.1/255.255.255.0 -> 192.168.2.0/255.255.255.0
 '''
def format_subnet(subnet_input):
    # 如果输入的ip，将掩码加上后输出
    if subnet_input.find("/") == -1:
        return subnet_input + "/255.255.255.255" 
    else:
        # 如果输入的是短掩码，则转换为长掩码
        subnet = subnet_input.split("/")
        if len(subnet[1]) < 3:
            mask_num = int(subnet[1])
            last_mask_num = mask_num % 8
            last_mask_str = ""
            for i in range(last_mask_num):
                last_mask_str += "1"
            if len(last_mask_str) < 8:
                for i in range(8-len(last_mask_str)):
                    last_mask_str += "0"
            last_mask_str = str(int(last_mask_str,2))
            if mask_num / 8 == 0:
                subnet = subnet[0] + "/" + last_mask_str +"0.0.0"
            elif mask_num / 8 == 1:
                subnet = subnet[0] + "/255." + last_mask_str +".0.0"
            elif mask_num / 8 == 2 :
                subnet = subnet[0] + "/255.255." + last_mask_str +".0"
            elif mask_num / 8 == 3:
                subnet = subnet[0] + "/255.255.255." + last_mask_str
            elif mask_num / 8 == 4:
                subnet = subnet[0] + "/255.255.255.255"
            subnet_input = subnet
 
        # 计算出正确的子网地址并输出
        subnet_array = subnet_input.split("/")
        subnet_true = socket.inet_ntoa(\
            struct.pack("!I",struct.unpack("!I",socket.inet_aton(subnet_array[0]))[0] & \
            struct.unpack("!I",socket.inet_aton(subnet_array[1]))[0]))\
            + "/" + subnet_array[1]
        return subnet_true
 
 
# 判断ip是否属于某个网段
def ip_in_subnet(ip,subnet):
    subnet = format_subnet(str(subnet))
    subnet_array = subnet.split("/")
    ip = format_subnet(ip + "/" + subnet_array[1])
    print('\tip=', ip)
    print('\tsubnet=', subnet)
    return ip == subnet

#要判断两个IP地址是不是在同一个网段，就将它们的IP地址分别与子网掩码做与运算，得到的结果一网络号，如果网络号相同，就在同一子网，否则，不在同一子网。
#            128.14.35.7/20 (10000000 00001110 00100011 00000111)
#最小地址是：128.14.32.0 = 10000000 00001110 00100000 00000000
#最大地址是：128.14.47.255 = 10000000 00001110 00101111 11111111
#子网掩码是：255.255.240.0 = 11111111 11111111 11110000 00000000
#可以得到这各CIDR地址块可以指派（47-32+1）*256=4096个地址，包含全0和全1地址。

print(ip_in_subnet("192.168.2.252","192.168.0.0/255.255.0.0"))
print(ip_in_subnet("192.168.2.252","192.168.3.0/255.255.255.0"))
#print(ip_in_subnet("192.168.2.252","192.168.2.0/23"))
print(ip_in_subnet("192.168.2.252","192.168.2.0/255.255.254.0"))
#print(ip_in_subnet("192.168.2.252","192.168.2.0/29"))
print(ip_in_subnet("192.168.2.252","192.168.2.0/255.255.255.248"))
print(ip_in_subnet("192.168.2.2","192.168.2.2"))
print(ip_in_subnet("192.168.2.2","192.168.2.3"))

