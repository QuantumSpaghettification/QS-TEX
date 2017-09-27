

from __future__ import division

def imagedisp(input):
  return("\includegraphics[width=3in]{"+input+"}")
#Takes input of sympy matrix and outputs pmatrix in LaTeX.
def display_matrix(matrix):
  a=matrix
  i=0
  matsri='\\begin{pmatrix}'
  while i < len(a[0,:]):
    j=0
    while j < len(a[:,0]):
      matsri=matsri+str(a[i,j])
      if j !=len(a[:,0])-1:
        matsri=matsri+'&'
      j=j+1
    if i !=  len(a[0,:])-1:
      matsri=matsri+'\\\\'
    i=i+1
  matsri=matsri+'\end{pmatrix}'
  return(matsri)
    


def output(content):
  file=open("outputfc_13.txt","w")
  file.write(content)
  file.close()


def scrinc(*options):
   if len(options)==0:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle13}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=3.5in,
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
!bs!begin{lstlisting}[language=python,style=mystyle13]
test="Hello world! From python2.7"
output(scrinc())
!bs!end{lstlisting}
          """
   elif "HF" in options:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle13}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=3.5in,
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
!bs!begin{lstlisting}[language=python,style=mystyle13]
<script=python2.7:action={!!sid=PDS!!}>
test="Hello world! From python2.7"
output(scrinc())
</script>!bs!end{lstlisting}
          """
   findrep={'!bs!b':'\\b','!bs!n':'\\\\n','!bs!':'\\'}
   for key in findrep:
      x=x.replace(key,findrep[key])
   return(x)


test="Hello world! From python2.7"
output(scrinc())


def output(content):
  file=open("outputfc_14.txt","w")
  file.write(content)
  file.close()


def scrinc(*options):
   if len(options)==0:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle14}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=3.5in,
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
!bs!begin{lstlisting}[language=python,style=mystyle14]
output(scrinc()+test)
!bs!end{lstlisting}
          """
   elif "HF" in options:
      x="""
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle14}{
      backgroundcolor=!bs!color{codegray},   
      commentstyle=!bs!color{magenta},
      keywordstyle=!bs!color{blue},
      linewidth=3.5in,
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
!bs!begin{lstlisting}[language=python,style=mystyle14]
<script=python2.7:action={!!sid=PDS!!}>
output(scrinc()+test)
</script>!bs!end{lstlisting}
          """
   findrep={'!bs!b':'\\b','!bs!n':'\\\\n','!bs!':'\\'}
   for key in findrep:
      x=x.replace(key,findrep[key])
   return(x)


output(scrinc()+test)
