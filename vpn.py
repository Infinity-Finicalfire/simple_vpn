import os
from pytun import TunTapDevice, IFF_TUN, IFF_NO_PI

def create_vpn_tunnel():
    tun = TunTapDevice(flags=IFF_TUN | IFF_NO_PI)
    tun.addr = '10.8.0.1'
    tun.dstaddr = '10.8.0.2'
    tun.netmask = '255.255.255.0'
    tun.mtu = 1500
    tun.up()

    print("VPN Tunnel Created:", tun.name)

    try:
        while True:
            buf = os.read(tun.fileno(), 1500)
            os.write(tun.fileno(), buf)
    except KeyboardInterrupt:
        tun.down()
        tun.close()

if __name__ == "__main__":
    create_vpn_tunnel()
