# -*- coding:utf-8 -*-
__author__ = 'Ban'

import os,time,sys,glob

def judgeCaseLevel(case,level):
    caselevel=case[2]
    if caselevel in level:
        return 1
    else:
        return 0

def getTime_s():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())

def printCaseStart(case):
    msg="TestcaseNo.:"+case[0]+' Start'
    msg+=' TestcaseName:'+case[1]+' TestcaseLevel:'+case[2]+""
    return msg

def printCaseEnd(case):
    msg="TestcaseNo.:"+case[0]+' End'
    return msg

def getLogfile(fname):
    Nowtime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    Newname=''.join([os.path.split(fname)[0].replace('Scripts','Log'),'/','Log_',Nowtime,'.log'])
    return Newname

def getReportfile(fname):
    Nowtime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    Newname=''.join([os.path.split(fname)[0].replace('Scripts','Log'),'/','Report_',Nowtime,'.log'])
    return Newname

def getAllPy(folder):
    tstr=folder+"\\*.py"
    delstr=folder+"\\__init__.py"
    fileList=glob.glob(tstr)
    try:
        fileList.remove(delstr)
    except Exception as e:
        pass
    return fileList

def updateGlobal(fname,LogFile='',ReportFile='',TestLevel=['level 1','level 2','level 3','level 4','level 5'],*args):
    with open(fname,'w+') as f:
        tstr='Logfile='+'\''+LogFile+'\''+'\n'        
        f.write(tstr)
        tstr='ReportFile='+'\''+ReportFile+'\''+'\n'           
        f.write(tstr)
        tlist='['
        for i in TestLevel:
            tlist+='\''+i+'\''+','
        tlist=tlist.rstrip(',')
        tlist+=']'
        tstr='TestLevel='+tlist+'\n'           
        f.write(tstr)
        for i in args:
            tstr=i[0]+'='+'\''+i[1]+'\''+'\n'   
            f.write(tstr)

def checkArgs(length,*args):
    if len(args) != length:
        print 'len args:',len(args)
        return 0
    return 1

def setTcStatus(tcno,status):
    if status==0:
        result='FAILED'
    elif status==1:
        result='PASS'
    else:
        result='BLOCK'
    msg="TestcaseNo.:"+tcno+' result:'+result+""
    return msg

def reportMsgGenerate(logf,runtime):
    pcount=0
    fcount=0
    bcount=0
    count=0
    msg=''
    with open(logf,'r+') as f:
        for i in f:
            if i.find('result:')!=-1:
                count+=1
                treslut=i[i.find('result:')+7:].strip()
                if treslut=='PASS':
                    pcount+=1
                elif treslut=='FAILED':
                    fcount+=1
                elif treslut=='BLOCK':
                    bcount+=1
                else:
                    bcount+=1
    rate="%.2f%%" % (float(pcount)/float(count)*100)
    rtime="%.2f" % runtime
    rtime=secondsToTime(float(rtime))
    msg='本轮测试共运行测试用例'+str(count)+'个,共计用时:'+str(rtime[0])+'时'+str(rtime[1])+'分'+str(rtime[2])+'秒,其中PASS:'+str(pcount)+'个,FAILED:'+str(fcount)+'个,BLOCK:'+str(bcount)+'个,通过率:'+str(rate)
    return msg

def secondsToTime(iItv):

    if type(iItv)==type(0.1):
        h=int(iItv/3600)
        sUp_h=int(iItv-3600*h)
        m=sUp_h/60
        sUp_m=iItv-3600*h-60*m
        s=sUp_m
        tlist=[str(h),str(m),str(s)]
        return tlist
    else:
        return "[InModuleError]:itv2time(iItv) invalid argument type"

