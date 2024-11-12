import os #line:1
try :#line:3
    import cython #line:4
except ModuleNotFoundError :#line:5
    os .system ("pip install cython")#line:6
import cython ,time ,marshal #line:8
def AsepYusup ():#line:11
    print ("1. Encode : Cython")#line:12
    print ("2. Encode : Marshal")#line:13
    O0O0O00OOO0O0O0O0 =input ("\nPILIH : ")#line:14
    if O0O0O00OOO0O0O0O0 in ["1"]:#line:15
        _OO0OO00OO0OOOOOOO ()#line:16
    elif O0O0O00OOO0O0O0O0 in ["2"]:#line:17
        ___marshalx___ ()#line:18
    else :#line:19
        print ("PILIH YANG BENER...!")#line:20
        exit ()#line:21
def _OO0OO00OO0OOOOOOO ():#line:24
    print ("Contoh : asepganteng.py")#line:25
    OOOOO000OOOO00O00 =input ("Ketik File Yang Mau Di Encode : ")#line:26
    print ("Tunggu Sedang Proses...!")#line:27
    os .system (f"cythonize -b {OOOOO000OOOO00O00}")#line:28
    print ("Sukses Cython Encode")#line:29
    exit ()#line:30
def ___marshalx___ ():#line:33
    os .system ("cls"if os .name =="nt"else "clear")#line:34
    print ("Contoh : asepganteng.py")#line:35
    OOOO00O00O00OOOO0 =input ("Masukan File : ")#line:36
    try :#line:37
        OOOO0O0000OOOOOO0 =OOOO00O00O00OOOO0 .split (".")#line:38
        OO00OOO00000OOOOO =OOOO0O0000OOOOOO0 [0 ]+"_enc.py"#line:39
    except :#line:40
        OO00OOO00000OOOOO =input ("FILE HASIL ENCODE : ")#line:41
    OO000OOO00O000O00 =int (input ("MAU BERAPA LAPIS...? : "))#line:42
    O00OO00OO000OOOOO =open (OOOO00O00O00OOOO0 ).read ()#line:43
    try :#line:44
        O0OO00000O0000O0O =0 #line:45
        for O00OOOO0OO0O0OOOO in range (OO000OOO00O000O00 ):#line:46
            O0OO00000O0000O0O +=1 #line:47
            OOOOO00O0O00O00O0 =compile (O00OO00OO000OOOOO ," ","exec")#line:48
            O00O0OO0OO0000000 =marshal .dumps (OOOOO00O0O00O00O0 )#line:49
            OO00O0OO0OOOOOOO0 =("#ENCODED By : Asep Yusup \n#ENCRYPTION : PY3 MARSHAL\n#GITHUB : https://github.com/Asep-Yusup\n#TELEGRAM : https://t.me/AsepYusup\n\nimport marshal\nexec(marshal.loads("+repr (O00O0OO0OO0000000 )+"))")#line:54
            time .sleep (0.004 )#line:55
            print ("ENCODE KE BERAPA : "+str (O0OO00000O0000O0O ))#line:56
    except ValueError :#line:57
        exit ("PILIH YANG BENER")#line:58
    except FileNotFoundError :#line:59
        exit ("FILE "+OOOO00O00O00OOOO0 +"KOSONG")#line:60
    OOOO000000O0OOOO0 =open (OO00OOO00000OOOOO ,"w")#line:61
    OOOO000000O0OOOO0 .write (OO00O0OO0OOOOOOO0 )#line:62
    OOOO000000O0OOOO0 .close ()#line:63
    print (f"Hasil Encode : "+OO00OOO00000OOOOO )#line:64
if __name__ =='__main__':#line:67
	os .system ("cls"if os .name =="nt"else "clear")#line:68
	AsepYusup ()#line:69