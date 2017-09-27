
#include <stdio.h>


void output(char *text){
  FILE *file;
  file=fopen("outputfc_10.txt","w");
  fprintf(file, "%s", text);
}


char* scrinc(char* arg){
  char* temp;
  if( arg == "HF" ){
    temp = "\n\\definecolor{codegreen}{rgb}{0,0.6,0}\n\\definecolor{codegray}{rgb}{0.5,0.5,0.5}\n\\definecolor{codepurple}{rgb}{0.58,0,0.82}\n\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}\n\n      \\lstdefinestyle{mystyle10}{\n      backgroundcolor=\\color{codegray},   \n      commentstyle=\\color{magenta},\n      keywordstyle=\\color{blue},\n      linewidth=3.5in,\n      numberstyle=\\tiny\\color{codegray},\n      stringstyle=\\color{codepurple},\n      basicstyle=\\footnotesize,\n      breakatwhitespace=false,         \n      breaklines=true,                 \n      captionpos=b,                    \n      keepspaces=true,                 \n      numbers=left,                    \n      numbersep=5pt,                  \n      showspaces=false,                \n      showstringspaces=false,\n      showtabs=false,                  \n      tabsize=2\n      }\n\\begin{lstlisting}[language=c,style=mystyle10]\n<script=c:action={!!sid=c1!!}>\n#include <stdlib.h>\n#include <string.h>\nvoid main(){\nchar* test = \"Hello World! From c\";\noutput( scrinc(\"HF\") );\n</script>\\end{lstlisting}\n          ";}
  else {
    temp = "\n\\definecolor{codegreen}{rgb}{0,0.6,0}\n\\definecolor{codegray}{rgb}{0.5,0.5,0.5}\n\\definecolor{codepurple}{rgb}{0.58,0,0.82}\n\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}\n\n      \\lstdefinestyle{mystyle10}{\n      backgroundcolor=\\color{codegray},   \n      commentstyle=\\color{magenta},\n      keywordstyle=\\color{blue},\n      linewidth=3.5in,\n      numberstyle=\\tiny\\color{codegray},\n      stringstyle=\\color{codepurple},\n      basicstyle=\\footnotesize,\n      breakatwhitespace=false,         \n      breaklines=true,                 \n      captionpos=b,                    \n      keepspaces=true,                 \n      numbers=left,                    \n      numbersep=5pt,                  \n      showspaces=false,                \n      showstringspaces=false,\n      showtabs=false,                  \n      tabsize=2\n      }\n\\begin{lstlisting}[language=c,style=mystyle10]\n#include <stdlib.h>\n#include <string.h>\nvoid main(){\nchar* test = \"Hello World! From c\";\noutput( scrinc(\"HF\") );\n\\end{lstlisting}\n          ";}
  return temp;
}


#include <stdlib.h>
#include <string.h>
void main(){
char* test = "Hello World! From c";
output( scrinc("HF") );


void output(char *text){
  FILE *file;
  file=fopen("outputfc_11.txt","w");
  fprintf(file, "%s", text);
}


char* scrinc(char* arg){
  char* temp;
  if( arg == "HF" ){
    temp = "\n\\definecolor{codegreen}{rgb}{0,0.6,0}\n\\definecolor{codegray}{rgb}{0.5,0.5,0.5}\n\\definecolor{codepurple}{rgb}{0.58,0,0.82}\n\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}\n\n      \\lstdefinestyle{mystyle11}{\n      backgroundcolor=\\color{codegray},   \n      commentstyle=\\color{magenta},\n      keywordstyle=\\color{blue},\n      linewidth=3.5in,\n      numberstyle=\\tiny\\color{codegray},\n      stringstyle=\\color{codepurple},\n      basicstyle=\\footnotesize,\n      breakatwhitespace=false,         \n      breaklines=true,                 \n      captionpos=b,                    \n      keepspaces=true,                 \n      numbers=left,                    \n      numbersep=5pt,                  \n      showspaces=false,                \n      showstringspaces=false,\n      showtabs=false,                  \n      tabsize=2\n      }\n\\begin{lstlisting}[language=c,style=mystyle11]\n<script=c:action={!!sid=c1!!}>\nchar* temp = malloc(strlen(scrinc(\"HF\"))+strlen(test));\nstrcpy(temp,scrinc(\"HF\"));\nstrcat(temp,test);\noutput( temp );\n}\n</script>\\end{lstlisting}\n          ";}
  else {
    temp = "\n\\definecolor{codegreen}{rgb}{0,0.6,0}\n\\definecolor{codegray}{rgb}{0.5,0.5,0.5}\n\\definecolor{codepurple}{rgb}{0.58,0,0.82}\n\\definecolor{backcolour}{rgb}{0.95,0.95,0.92}\n\n      \\lstdefinestyle{mystyle11}{\n      backgroundcolor=\\color{codegray},   \n      commentstyle=\\color{magenta},\n      keywordstyle=\\color{blue},\n      linewidth=3.5in,\n      numberstyle=\\tiny\\color{codegray},\n      stringstyle=\\color{codepurple},\n      basicstyle=\\footnotesize,\n      breakatwhitespace=false,         \n      breaklines=true,                 \n      captionpos=b,                    \n      keepspaces=true,                 \n      numbers=left,                    \n      numbersep=5pt,                  \n      showspaces=false,                \n      showstringspaces=false,\n      showtabs=false,                  \n      tabsize=2\n      }\n\\begin{lstlisting}[language=c,style=mystyle11]\nchar* temp = malloc(strlen(scrinc(\"HF\"))+strlen(test));\nstrcpy(temp,scrinc(\"HF\"));\nstrcat(temp,test);\noutput( temp );\n}\n\\end{lstlisting}\n          ";}
  return temp;
}


char* temp = malloc(strlen(scrinc("HF"))+strlen(test));
strcpy(temp,scrinc("HF"));
strcat(temp,test);
output( temp );
}
