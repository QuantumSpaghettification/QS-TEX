import sys
import re
import string
import itertools
import os
import os.path
#Read file
f = open(sys.argv[1],"r")
contents = f.read()
f.close()
  #//////////////////////////////////////////////////////////////////////////////
  #............................Gets info from Config...........
  #//////////////////////////////////////////////////////////////////////////////
f = open("QS.config","r")
Config_Contents = f.read()
f.close()
Config_Info={}
par=re.findall(r'!!!(.*?)={(.*?)}!!!',Config_Contents,re.DOTALL)
for y in par:
  Config_Info[y[0]]=y[1]
  #//////////////////////////////////////////////////////////////////////////////
  #............................Gets info from LANG directory...........
  #//////////////////////////////////////////////////////////////////////////////
path_to_LANG=Config_Info['Path']+"/LANG"
LangFiles = [x for x in os.listdir(path_to_LANG)]
Lang_Info={}
for x in LangFiles:
  key=x.replace('.lang','')
  f=open(path_to_LANG+"/"+x,"r")
  lang_contents=f.read()
  f.close()
  Lang_Info[key]={}
  par=re.findall(r'!!!(.*?)={(.*?)}!!!',lang_contents,re.DOTALL)
  for y in par:
    Lang_Info[key][y[0]]=y[1]

def codefind(contentin):
  #//////////////////////////////////////////////////////////////////////////////
  #.....Finds Scripts pre defined.......
  #//////////////////////////////////////////////////////////////////////////////
  par=re.findall(r'!!!(.*?)={(.*?)}!!!',contentin,re.DOTALL)
  precontents=contentin
  for x in par:
    precontents=precontents.replace('!!!'+x[0]+'={'+x[1]+'}!!!','')
    precontents=precontents.replace('<'+x[0]+'>',x[1])
    precontents=precontents.replace('</'+x[0]+'>','</script>')
  #//////////////////////////////////////////////////////////////////////////////
  #.....Finds Scripts .......
  #//////////////////////////////////////////////////////////////////////////////  
  par=re.findall(r'<script=(.*?):action={(.*?)}>(.*?)</script>',precontents,re.DOTALL)
  newcontents=precontents
  #script needs to be the end point of the file.
  langarray=[key for key in Lang_Info]
  #//////////////////////////////////////////////////////////////////////////////
  #.....Creates function to replace varibles in lang files with py varibles.......
  #//////////////////////////////////////////////////////////////////////////////
  def var_rep(string,var):
    temp=string
    for key in var:
      temp=temp.replace("!!"+key+"!!",str(var[key]))
    return(temp)
  #//////////////////////////////////////////////////////////////////////////////
  #............................Creates Function to Include Script................
  #//////////////////////////////////////////////////////////////////////////////
  def include_script(lang,script,action,indscriptid,*other): #Function used to include scripts into page.
    def latexcode_func(pre_post):
      pre=''
      post=''
      script_escaped=script
      for x in Lang_Info[lang]["back_slash_escape"]:
        script_escaped=script_escaped.replace(x,"\\"+x)
      if pre_post=='HF':
        pre=pre+"\n<script="+lang+":action={"+action+"}>"
        post=post+"</script>"
      latexcode=Config_Info['ListingPre']+"""
      !bs!lstdefinestyle{mystyle"""+str(indscriptid)+"""}{"""+Config_Info['ListingIn']+"""
      }
!bs!begin{lstlisting}[language="""+Lang_Info[lang]["lstlisting"]+""",style=mystyle"""+str(indscriptid)+"""]"""+pre+script_escaped+post+"""!bs!end{lstlisting}
          """+Config_Info['ListingPost']
      try:
          par=re.findall(r'!!(.*?)\|(.*?)!!',Lang_Info[lang]['listing_replace'],re.DOTALL)
          for x_lr in par:
            latexcode=latexcode.replace(x_lr[0],x_lr[1])
      except KeyError:
        pass
      return(latexcode)
    if len(other)==0:
      return(var_rep(Lang_Info[lang]['func.scrinc'],{"norm":latexcode_func(''),"HF":latexcode_func('HF')}))
    elif other[0]=='':
      return(latexcode_func(''))
    elif other[0]=='HF':
      return(latexcode_func('HF'))
  #//////////////////////////////////////////////////////////////////////////////
  #............................Creating Directory of Partial scripts....
  #//////////////////////////////////////////////////////////////////////////////
  
  part_script={}
  partsc_id=0
  for x in par:
    lang=x[0]
    action=x[1]
    script=x[2]
    #Script ID - allowing for combined scripts.
    sid=re.findall(r'!!sid=(.*?)!!',action,re.DOTALL)
    if len(sid) == 0:
      sid="alone"
    else:
      sid=sid[0]
    part_script[partsc_id]=[sid,lang,action,script] #This array contains information about the indivudual scripts
    partsc_id=partsc_id+1
  #//////////////////////////////////////////////////////////////////////////////
  #............................Getting Functions from FUNC.........
  #//////////////////////////////////////////////////////////////////////////////
  def pre_functions(lang):
    path_to_FUNC=Config_Info['Path']+"/FUNC/"+lang
    Func_Files = [x for x in os.listdir(path_to_FUNC)]
    Func_String=''
    for x in Func_Files:
      f=open(path_to_FUNC+"/"+x,"r")
      Func_Contents=f.read()
      f.close()
      Func_String= Func_String+Func_Contents+'\n'
    return(Func_String)
  #//////////////////////////////////////////////////////////////////////////////
  #........................... Creating Output if in Action.........
  #//////////////////////////////////////////////////////////////////////////////
  for partsc_id, ps in part_script.iteritems(): 
    action=ps[2]
    #outputs given in action.
    outputted=re.findall(r'!!output=(.*?)!!',action,re.DOTALL)
    if len(outputted)!=0:
      To_be_outputted=outputted[0].replace('scrinc()', include_script(ps[1],ps[3],ps[2],partsc_id,'').replace('!bs!','\\'))
      To_be_outputted=To_be_outputted.replace("scrinc('HF')", include_script(ps[1],ps[3],ps[2],partsc_id,'HF').replace('!bs!','\\'))
      file=open("outputfc_"+str(partsc_id)+".txt","w")
      file.write(To_be_outputted)
      file.close()
      
  #//////////////////////////////////////////////////////////////////////////////
  #............................Forming the total scripts...........
  #//////////////////////////////////////////////////////////////////////////////
  
  scripts={}
  alonecount=0
  for partsc_id, ps in part_script.iteritems():
    lang=ps[1]
    prearray=[lang,Lang_Info[lang]["func.preamble"],pre_functions(lang)]
    #defines function to add
    toadd=[]
    if len(re.findall('\noutput', ps[3],re.DOTALL))!=0:
       toadd=toadd+[var_rep(Lang_Info[lang]['func.output'],{"i":partsc_id})]
    if len(re.findall('scrinc', ps[3],re.DOTALL))!=0:
       toadd=toadd+[include_script(lang,ps[3],ps[2],partsc_id)]
    toadd=toadd+[ps[3].replace('from __future__ import division','')]
    #end of defining function to add
    if ps[0] == "alone":
      scripts['alone'+str(alonecount)]=prearray+toadd
      alonecount=alonecount+1
    else:
      try:
        scripts[ps[0]].extend(toadd)
      except KeyError:
        scripts[ps[0]]=prearray
        scripts[ps[0]].extend(toadd)
  #//////////////////////////////////////////////////////////////////////////////
  #............................Runs the Scripts...........
  #//////////////////////////////////////////////////////////////////////////////
  for scr_run in scripts.itervalues():
    scr_final=''
    i=1
    while i<len(scr_run):
      scr_final=scr_final+'\n'+scr_run[i]
      i=i+1
    file=open("tempcode."+Lang_Info[scr_run[0]]['file_ext'],"w")
    file.write(scr_final)
    file.close()
    os.system(Lang_Info[scr_run[0]]['run_command'].replace('!!i!!','tempcode.'+Lang_Info[scr_run[0]]['file_ext']))
  #//////////////////////////////////////////////////////////////////////////////
  #.............Finds and Replaces <script...>... </script> with output..........
  #//////////////////////////////////////////////////////////////////////////////
  for partsc_id,ps in part_script.iteritems():
    file=open('outputfc_'+str(partsc_id)+'.txt',"r")
    replace=file.read()
    file.close()
    find='<script='+ps[1]+':action={'+ps[2]+'}>'+ps[3]+'</script>'
    newcontents=newcontents.replace(find,replace)
  #//////////////////////////////////////////////////////////////////////////////
  #........................Line Numbering of Lsting........................
  #//////////////////////////////////////////////////////////////////////////////
  line_collections={}
  for partsc_id,ps in part_script.iteritems():
    action=ps[2]
    linenumber=re.findall('!!LinNoId=(.*?)!!', action,re.DOTALL)
    if len(linenumber)!=0:
      ToEnter=ps[3].rstrip()#removes trailing lines.
      toappend=[partsc_id,ToEnter.count('\n')]
      try: 
          line_collections[linenumber[0]].append(toappend)
      except KeyError:
          line_collections[linenumber[0]]=[]
          line_collections[linenumber[0]].append(toappend)
  for key,array in line_collections.iteritems():
    totalno=1
    for x in array:
      if totalno==0:
         inno=1
          
      newcontents=newcontents.replace("style=mystyle"+str(x[0]), "style=mystyle"+str(x[0])+",firstnumber="+str(totalno))
      totalno=totalno+x[1]
  return(newcontents)

contentout=codefind(contents)
file=open("temp.tex","w")
file.write(contentout)
file.close()