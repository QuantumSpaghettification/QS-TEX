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

def codefind(contentin):
  par=re.findall(r'<script=(.*?):action={(.*?)}>(.*?)</script>',contentin,re.DOTALL)
  newcontents=contentin
  #script needs to be the end point of the file.
  langarray=['py','R','php']
  #/////////////////////////////////////////////
  #////// Segments for code ///////////
  def preable(lang):
    preable1={}
    preable1['py']='from __future__ import division \n'
    return preable1[lang]
  def outputfunc(lang,i):
    outputfuns={}
    outputfuns['py']='def output(content): \n \t file=open("outputfc_'+str(i)+'.txt","w")\n\t file.write(content)\n\t file.close()\n'
    return outputfuns[lang]
  def include_script(lang,script,action,indscriptid):
    languges={'py':'Python'}
    def latexcode_func(pre_post):
      pre=''
      post=''
      if pre_post=='HF':
        pre=pre+"\n<script="+lang+":action={"+action+"}>"
        post=post+"</script>"
      latexcode="""
      \definecolor{codegreen}{rgb}{0,0.6,0}
      \definecolor{codegray}{rgb}{0.5,0.5,0.5}
      \definecolor{codepurple}{rgb}{0.58,0,0.82}
      \definecolor{backcolour}{rgb}{0.95,0.95,0.92}
      \lstdefinestyle{mystyle"""+str(indscriptid)+"""}{
      backgroundcolor=\color{white},   
      commentstyle=\color{codegreen},
      keywordstyle=\color{magenta},
      linewidth=3in,
      numberstyle=\\\\tiny\color{codegray},
      stringstyle=\color{codepurple},
      basicstyle=\\\\footnotesize,
      breakatwhitespace=false,         
      breaklines=true,                 
      captionpos=b,                    
      keepspaces=true,                 
      numbers=left,                    
      numbersep=5pt,                  
      showspaces=false,                
      showstringspaces=false,
      showtabs=false,                  
      tabsize=2
      }
      %.................................................
\\\\begin{lstlisting}[language="""+languges[lang]+""",style=mystyle"""+str(indscriptid)+"""]"""+pre+script+post+"""\end{lstlisting}
          """#The } and { before and after begin{...} and end{...} are to close the newsubject enviroment in which lstlisting does not work.
      return(latexcode)
    script={"py":"""
def scrinc(*options):
   if len(options)==0:
      return(\"\"\""""+latexcode_func('')+"""\"\"\")
   elif "HF" in options:
      return(\"\"\""""+latexcode_func('HF')+"""\"\"\")
   """}
    return(script[lang])
    
  def imagedisp_fun(lang):
    imagedisp1={}
    imagedisp1['py']='def imagedisp(input):\n\t return(" \\\\includegraphics[width=3in]{"+input+"} ")\n'
    return imagedisp1[lang]
  #///////////////////////////////////////////////
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
    part_script[partsc_id]=[sid,lang,action,script]
    partsc_id=partsc_id+1
  #Forming the total scripts
  scripts={}
  alonecount=0
  for partsc_id, ps in part_script.iteritems():
    prearray=[lang,preable(lang),imagedisp_fun(lang)]
    if ps[0] == "alone":
      scripts['alone'+str(alonecount)]=prearray+[outputfunc(lang,partsc_id),include_script(lang,ps[3],ps[2],partsc_id)]+[ps[3]]
      alonecount=alonecount+1
    else:
      try:
        scripts[ps[0]].extend([outputfunc(lang,partsc_id),include_script(lang,ps[3],ps[2],partsc_id),ps[3]])
      except KeyError:
        scripts[ps[0]]=prearray
        scripts[ps[0]].extend([outputfunc(lang,partsc_id),include_script(lang,ps[3],ps[2],partsc_id),ps[3]])
  #/////// Runs scripts
  for scr_run in scripts.itervalues():
    scr_final=''
    i=1
    while i<len(scr_run):
      scr_final=scr_final+'\n'+scr_run[i]
      i=i+1
    file=open("tempcode."+scr_run[0],"w")
    file.write(scr_final)
    file.close()
    for lt,y in zip(langarray,['python2.7 tempcode.py','Rscript tempcode.R']):
      if scr_run[0]==lt:
        os.system(y)
  #/////// forms find and replace
  for partsc_id,ps in part_script.iteritems():
    file=open('outputfc_'+str(partsc_id)+'.txt',"r")
    replace=file.read()
    file.close()
    find='<script='+ps[1]+':action={'+ps[2]+'}>'+ps[3]+'</script>'
    newcontents=newcontents.replace(find,replace)
  return(newcontents)

contentout=codefind(contents)
file=open("temp.tex","w")
file.write(contentout)
file.close()