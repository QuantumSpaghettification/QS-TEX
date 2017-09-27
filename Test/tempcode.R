


imagedisp <-function(input){
  text=c("\\includegraphics[width=3in]{",input,"}")
  return(paste(text,collapse=""))}


output <- function(content){
   cat(content, file = "outputfc_7.txt")
   }


scrinc <-function(options){
  if(options==""){
    x="
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle7}{
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
!bs!begin{lstlisting}[language=R,style=mystyle7]
test=\"Hello World! From R\"
output(scrinc(\"HF\"))
!bs!end{lstlisting}
          "
    }
  else if(options=="HF"){
    x="
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle7}{
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
!bs!begin{lstlisting}[language=R,style=mystyle7]
<script=R:action={!!sid=R1!!}>
test=\"Hello World! From R\"
output(scrinc(\"HF\"))
</script>!bs!end{lstlisting}
          "
    }
   return(gsub('!bs!','\\\\',x))
  }


test="Hello World! From R"
output(scrinc("HF"))


output <- function(content){
   cat(content, file = "outputfc_8.txt")
   }


scrinc <-function(options){
  if(options==""){
    x="
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle8}{
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
!bs!begin{lstlisting}[language=R,style=mystyle8]
output(paste(scrinc(\"HF\"),test,sep=''))
!bs!end{lstlisting}
          "
    }
  else if(options=="HF"){
    x="
!bs!definecolor{codegreen}{rgb}{0,0.6,0}
!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}
!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}
!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}

      !bs!lstdefinestyle{mystyle8}{
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
!bs!begin{lstlisting}[language=R,style=mystyle8]
<script=R:action={!!sid=R1!!}>
output(paste(scrinc(\"HF\"),test,sep=''))
</script>!bs!end{lstlisting}
          "
    }
   return(gsub('!bs!','\\\\',x))
  }


output(paste(scrinc("HF"),test,sep=''))
