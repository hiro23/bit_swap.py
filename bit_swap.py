def main():  
    print("start")
    cnv_tbl = [0]*256
    for i in range(256):
        cnv_tbl[i] = (i&1)<<7 | (i&2)<<5  | (i&4)<<3  | (i&8)<<1 | (i&16)>>1 | (i&32)>>3 | (i&64)>>5 | (i&128)>>7

    print("convert table set done, bit swap start")
    f_i = open("test_indata.bin","rb")
    f_o = open("test_outdata.bin","wb")
    while True:
        rdata = f_i.read(1)
        if not rdata:
            break
        else:
            wdata = cnv_tbl[ord(rdata)].to_bytes(1,"little") 
            f_o.write(wdata)

    print("all done")

if __name__ == '__main__':
    main()
