

from __future__ import division


def imagedisp(input):
  return("\includegraphics[width=3in]{"+input+"}")


def output(content):
  file=open("outputfc_2.txt","w")
  file.write(content)
  file.close()


def scrinc(*options):
   if len(options)==0:
      x="""
      !bs!definecolor{codegreen}{rgb}{0,0.6,0}
      !bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
      !bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
      !bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}
      !bs!lstdefinestyle{mystyle2}{
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
!bs!begin{lstlisting}[language=python,style=mystyle2]
a=2
output(scrinc('HF'))
!bs!end{lstlisting}
          """
   elif "HF" in options:
      x="""
      !bs!definecolor{codegreen}{rgb}{0,0.6,0}
      !bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
      !bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
      !bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}
      !bs!lstdefinestyle{mystyle2}{
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
!bs!begin{lstlisting}[language=python,style=mystyle2]
<script=python2.7:action={!!sid=2!!}>
a=2
output(scrinc('HF'))
</script>!bs!end{lstlisting}
          """
   findrep={'!bs!b':'\\b','!bs!n':'\\\\n','!bs!':'\\'}
   for key in findrep:
      x=x.replace(key,findrep[key])
   return(x)


a=2
output(scrinc('HF'))


def output(content):
  file=open("outputfc_4.txt","w")
  file.write(content)
  file.close()


def scrinc(*options):
   if len(options)==0:
      x="""
      !bs!definecolor{codegreen}{rgb}{0,0.6,0}
      !bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
      !bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
      !bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}
      !bs!lstdefinestyle{mystyle4}{
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
!bs!begin{lstlisting}[language=python,style=mystyle4]
output(scrinc('HF')+\"output: \"+str(a))
!bs!end{lstlisting}
          """
   elif "HF" in options:
      x="""
      !bs!definecolor{codegreen}{rgb}{0,0.6,0}
      !bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
      !bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
      !bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}
      !bs!lstdefinestyle{mystyle4}{
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
!bs!begin{lstlisting}[language=python,style=mystyle4]
<script=python2.7:action={!!sid=2!!}>
output(scrinc('HF')+\"output: \"+str(a))
</script>!bs!end{lstlisting}
          """
   findrep={'!bs!b':'\\b','!bs!n':'\\\\n','!bs!':'\\'}
   for key in findrep:
      x=x.replace(key,findrep[key])
   return(x)


output(scrinc('HF')+"output: "+str(a))
