

dheaders = {
    'Origin': 'http://result1.gtu.ac.in',
    'Host': 'result1.gtu.ac.in',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,gu;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    #'Content-Type': 'application/x-www-form-urlencoded',
    #'Content-Length':len(data.format(ns[0],ns[1],'xvT8')),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://result1.gtu.ac.in/default.aspx',
    'Connection': 'keep-alive',
}
import requests
import captcha2
def getval(s,f,t):
	st=s.find(f)+len(f)
	return s[st:s.find(t,st)]
def strtod(s):
	d={}
	for x in s.split('&'):
		xx=x.split('=')
		d[xx[0]]=xx[1]
	return d

inbtw=lambda d,f,t,st=0:d[d.find(f,st)+len(f):d.find(t,d.find(f,st)+len(f))].strip() if d.count(f,st) else ''

def getsess():
	import requests
	r=requests.get('http://result1.gtu.ac.in/default.aspx',headers={
    'Origin': 'http://result1.gtu.ac.in',
    'Host': 'result1.gtu.ac.in',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,gu;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    #'Content-Length':len(data.format(ns[0],ns[1],'xvT8')),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://result1.gtu.ac.in/default.aspx',
    'Connection': 'keep-alive',
})
	sel=inbtw(r.text,'<select name="ddlbatch" id="ddlbatch" class="ddl">','</select>')
	cooked=r.cookies.get_dict()
	vs=getval(r.text,'id="__VIEWSTATE" value="','"')
	vsg=getval(r.text,'id="__VIEWSTATEGENERATOR" value="','"')
	cpu='http://result1.gtu.ac.in/CaptchaImage.axd?guid='+getval(r.text,'<img src="CaptchaImage.axd?guid=','"')
	wb='http://result1.gtu.ac.in/WebResource.axd?'
	wb1=getval(r.text,'/WebResource.axd?','"')
	wb2=getval(r.text.replace('WebResource.axd?',"/",1),'/WebResource.axd?','"')
	requests.get(wb+wb1,cookies=cooked)
	requests.get(wb+wb2,cookies=cooked)
	return (vs,vsg,cpu,sel),cooked

data='__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE={}&__VIEWSTATEGENERATOR={}&ddlbatch={}&txtenroll={}&txtSheetNo=&CodeNumberTextBox={}&btnSearch=Search'
def dsp(zrc):
	print("dsp",len(zrc),zrc)
from subprocess import call
show=lambda x:call(["C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" ,x])
nlize=lambda s:s.replace('.','').replace(' ','').replace('-','').strip().lower().replace('(','').replace(')','')
def findexm (sel,exrgx):
	exrgx=nlize(exrgx)
	if not exrgx:return ''
	opts,fstr,lfs=[],'<option value="',len('<option value="')
	ils=sel.find(fstr,0)
	while ils!=-1:
		iels=sel.find('"',ils+lfs)
		excode=sel[ils+lfs:iels]
		exstr=sel[sel.find('>',iels)+1:sel.find('</',sel.find('>',iels)+1)]
		opts.append((excode,exstr))
		ils=sel.find('<option value="',iels)
		if exrgx in nlize(exstr):return excode
	#for ex,es in opts:
	return ''
	
def getptr(enrol='140280116051',exm='',html=1,tries=3):
	ns,cooked=getsess();#show(ns[2])
	nd=strtod(data)
	if '$current$' not in exm:exm=findexm(ns[3],exm)
	if not exm:return "Result not DECLARED....keep trying"
	nd['ddlbatch']=exm
	nd['txtenroll']=enrol
	nd['__VIEWSTATE']=ns[0]
	nd['__VIEWSTATEGENERATOR']=ns[1]
	#print(nd)
	captchaO=captcha2.solveCaptcha(cookies=cooked)
	for k,v in captchaO['requests'].cookies.get_dict().items():cooked[k]=v
	nd['CodeNumberTextBox']=captchaO['captcha']
	zr=requests.post('http://result1.gtu.ac.in/', headers={
    'Origin': 'http://result1.gtu.ac.in',
    'Host': 'result1.gtu.ac.in',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,gu;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    #'Content-Length':len(data.format(ns[0],ns[1],'xvT8')),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://result1.gtu.ac.in/default.aspx',
    'Connection': 'keep-alive',
    }, data=nd,cookies=cooked)#strtod(data.format(ns[0],ns[1],exm,enrol,captcha.DO(ns[2]))))
	if tries and ('Incorrect captcha code' in zr.text):return getptr(enrol,exm,html,tries-1)
	spi=getval(zr.text,'<span id="lblSPI" class="csstotal">','</span>')
	cpi=getval(zr.text,'<span id="lblCPI" class="csstotal">','</span>')
	relh='''<link rel="Stylesheet" href="http://result1.gtu.ac.in/Style/rescss_min.css" type="text/css">'''
	#if html:return zr.content
	#return str({'spi':spi,'cpi':cpi}) #if len(spi)<5 else getptr(enrol,exm)
	spicpi='<pre>{}</pre>'.format(str({'spi':spi,'cpi':cpi}))
	if len(spicpi)>50:spicpi='<pre>SPI-CPI=404</pre>'
	with open('/home/ubuntu/gtu/pasted/results/'+enrol+'.html','w') as fl:fl.write( spicpi+zr.text)
	if html:return spicpi+zr.text
	return spicpi


if __name__ == "__main__":
	raw_input=input
	print(getptr(enrol=raw_input('Enrol?'),exm=raw_input('Exam regex?')))
	raw_input()


