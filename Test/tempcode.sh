

#!/bin/bash



output() { 
temp=$@
temp=${temp//!bsp!b/\\\\b}
temp=${temp//!bsp!e/\\\\e}
temp=${temp//!bsp!f/\\\\f}
temp=${temp//!bsp!t/\\\\t}

printf "$temp" > outputfc_4.txt
}


scrinc(){
input=$@
temp='newline!bs!definecolor{codegreen}{rgb}{0,0.6,0}newline!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}newline!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}newline!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}newlinenewline      !bs!lstdefinestyle{mystyle4}{newline      backgroundcolor=!bs!color{codegray},   newline      commentstyle=!bs!color{magenta},newline      keywordstyle=!bs!color{blue},newline      linewidth=3.5in,newline      numberstyle=!bs!tiny!bs!color{codegray},newline      stringstyle=!bs!color{codepurple},newline      basicstyle=!bs!footnotesize,newline      breakatwhitespace=false,         newline      breaklines=true,                 newline      captionpos=b,                    newline      keepspaces=true,                 newline      numbers=left,                    newline      numbersep=5pt,                  newline      showspaces=false,                newline      showstringspaces=false,newline      showtabs=false,                  newline      tabsize=2newline      }newline!bs!begin{lstlisting}[language=bash,style=mystyle4]newlinetest="Hello World! From bash"newlineoutput "$( scrinc "HF" )"newline!bs!end{lstlisting}newline          '
if [[ "$input" == "HF" ]]; then
temp='newline!bs!definecolor{codegreen}{rgb}{0,0.6,0}newline!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}newline!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}newline!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}newlinenewline      !bs!lstdefinestyle{mystyle4}{newline      backgroundcolor=!bs!color{codegray},   newline      commentstyle=!bs!color{magenta},newline      keywordstyle=!bs!color{blue},newline      linewidth=3.5in,newline      numberstyle=!bs!tiny!bs!color{codegray},newline      stringstyle=!bs!color{codepurple},newline      basicstyle=!bs!footnotesize,newline      breakatwhitespace=false,         newline      breaklines=true,                 newline      captionpos=b,                    newline      keepspaces=true,                 newline      numbers=left,                    newline      numbersep=5pt,                  newline      showspaces=false,                newline      showstringspaces=false,newline      showtabs=false,                  newline      tabsize=2newline      }newline!bs!begin{lstlisting}[language=bash,style=mystyle4]newline<script=bash:action={!!sid=ba1!!}>newlinetest="Hello World! From bash"newlineoutput "$( scrinc "HF" )"newline</script>!bs!end{lstlisting}newline          '
fi
temp=${temp//!bs!b/!bsp!b}
temp=${temp//!bs!e/!bsp!e}
temp=${temp//!bs!f/!bsp!f}
temp=${temp//!bs!t/!bsp!t}
temp=${temp//!bs!/\\}
temp=${temp//newline/\\n}
printf "$temp"
}


test="Hello World! From bash"
output "$( scrinc "HF" )"


output() { 
temp=$@
temp=${temp//!bsp!b/\\\\b}
temp=${temp//!bsp!e/\\\\e}
temp=${temp//!bsp!f/\\\\f}
temp=${temp//!bsp!t/\\\\t}

printf "$temp" > outputfc_5.txt
}


scrinc(){
input=$@
temp='newline!bs!definecolor{codegreen}{rgb}{0,0.6,0}newline!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}newline!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}newline!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}newlinenewline      !bs!lstdefinestyle{mystyle5}{newline      backgroundcolor=!bs!color{codegray},   newline      commentstyle=!bs!color{magenta},newline      keywordstyle=!bs!color{blue},newline      linewidth=3.5in,newline      numberstyle=!bs!tiny!bs!color{codegray},newline      stringstyle=!bs!color{codepurple},newline      basicstyle=!bs!footnotesize,newline      breakatwhitespace=false,         newline      breaklines=true,                 newline      captionpos=b,                    newline      keepspaces=true,                 newline      numbers=left,                    newline      numbersep=5pt,                  newline      showspaces=false,                newline      showstringspaces=false,newline      showtabs=false,                  newline      tabsize=2newline      }newline!bs!begin{lstlisting}[language=bash,style=mystyle5]newlineoutput "$( scrinc "HF" )"$testnewline!bs!end{lstlisting}newline          '
if [[ "$input" == "HF" ]]; then
temp='newline!bs!definecolor{codegreen}{rgb}{0,0.6,0}newline!bs!definecolor{codegray}{rgb}{0.5,0.5,0.5}newline!bs!definecolor{codepurple}{rgb}{0.58,0,0.82}newline!bs!definecolor{backcolour}{rgb}{0.95,0.95,0.92}newlinenewline      !bs!lstdefinestyle{mystyle5}{newline      backgroundcolor=!bs!color{codegray},   newline      commentstyle=!bs!color{magenta},newline      keywordstyle=!bs!color{blue},newline      linewidth=3.5in,newline      numberstyle=!bs!tiny!bs!color{codegray},newline      stringstyle=!bs!color{codepurple},newline      basicstyle=!bs!footnotesize,newline      breakatwhitespace=false,         newline      breaklines=true,                 newline      captionpos=b,                    newline      keepspaces=true,                 newline      numbers=left,                    newline      numbersep=5pt,                  newline      showspaces=false,                newline      showstringspaces=false,newline      showtabs=false,                  newline      tabsize=2newline      }newline!bs!begin{lstlisting}[language=bash,style=mystyle5]newline<script=bash:action={!!sid=ba1!!}>newlineoutput "$( scrinc "HF" )"$testnewline</script>!bs!end{lstlisting}newline          '
fi
temp=${temp//!bs!b/!bsp!b}
temp=${temp//!bs!e/!bsp!e}
temp=${temp//!bs!f/!bsp!f}
temp=${temp//!bs!t/!bsp!t}
temp=${temp//!bs!/\\}
temp=${temp//newline/\\n}
printf "$temp"
}


output "$( scrinc "HF" )"$test
