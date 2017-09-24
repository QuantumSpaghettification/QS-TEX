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
#Get Languages
path_to_LANG="./LANG"
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
  par=re.findall(r'<script=(.*?):action={(.*?)}>(.*?)</script>',contentin,re.DOTALL)
  newcontents=contentin
  #script needs to be the end point of the file.
  langarray=[key for key in Lang_Info]
  #/////////////////////////////////////////////
  #////// Segments for code ///////////
  def var_rep(string,var):
    temp=string
    for key in var:
      temp=temp.replace("!!"+key+"!!",str(var[key]))
    return(temp)
  def include_script(lang,script,action,indscriptid): #Function used to include scripts into page.
    def latexcode_func(pre_post):
      pre=''
      post=''
      script_escaped=script
      for x in Lang_Info[lang]["back_slash_escape"]:
        script_escaped=script_escaped.replace(x,"\\"+x)
      if pre_post=='HF':
        pre=pre+"\n<script="+lang+":action={"+action+"}>"
        post=post+"</script>"
      latexcode="""
      !bs!definecolor{codegreen}{rgb}{0,0.6,0}
      !bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
      !bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
      !bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}
      !bs!lstdefinestyle{mystyle"""+str(indscriptid)+"""}{
      backgroundcolor=!bs!color{white},   
      commentstyle=!bs!color{codegreen},
      keywordstyle=!bs!color{magenta},
      linewidth=5in,
      numberstyle=!bs!tiny!bs!color{codegray},
      stringstyle=!bs!color{codepurple},
      basicstyle=!bs!footnotesize,
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
!bs!begin{lstlisting}[language="""+Lang_Info[lang]["lstlisting"]+""",style=mystyle"""+str(indscriptid)+"""]"""+pre+script_escaped+post+"""!bs!end{lstlisting}
          """#The } and { before and after begin{...} and end{...} are to close the newsubject enviroment in which lstlisting does not work.
      return(latexcode)
    return(var_rep(Lang_Info[lang]['func.scrinc'],{"norm":latexcode_func(''),"HF":latexcode_func('HF')}))
    
  #/////////////////////////////////////////////// Creating and Running Scripts
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
  #Forming the total scripts
  scripts={}
  alonecount=0
  for partsc_id, ps in part_script.iteritems():
    lang=ps[1]
    prearray=[lang,Lang_Info[lang]["func.preamble"],Lang_Info[lang]["func.imagedisp"]]
    if ps[0] == "alone":
      scripts['alone'+str(alonecount)]=prearray+[var_rep(Lang_Info[lang]['func.output'],{"i":partsc_id}),include_script(lang,ps[3],ps[2],partsc_id)]+[ps[3]]
      alonecount=alonecount+1
    else:
      try:
        scripts[ps[0]].extend([var_rep(Lang_Info[lang]['func.output'],{"i":partsc_id}) ,include_script(lang,ps[3],ps[2],partsc_id),ps[3]])
      except KeyError:
        scripts[ps[0]]=prearray
        scripts[ps[0]].extend([var_rep(Lang_Info[lang]['func.output'],{"i":partsc_id}) ,include_script(lang,ps[3],ps[2],partsc_id),ps[3]])
  #/////// Runs scripts
  for scr_run in scripts.itervalues():
    scr_final=''
    i=1
    while i<len(scr_run):
      scr_final=scr_final+'\n'+scr_run[i]
      i=i+1
    file=open("tempcode."+Lang_Info[scr_run[0]]['file_ext'],"w")
    file.write(scr_final)
    file.close()
    os.system(Lang_Info[scr_run[0]]['run_command']+' '+'tempcode.'+Lang_Info[scr_run[0]]['file_ext'])
  #/////// forms find and replace to replace <script...>...</script>with output.
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