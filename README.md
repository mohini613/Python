python project using docker 
Used <docker build -t my-python-app . > to build the Docker image.
-t my-python-app  us the name of image

. tells Docker to use the current folder

to create project directly :
 <mkdir python-docker> 

this creates dedicated folder for docker and pyhton files 

<docker run my-python-app> runs docker image  

<docker run -it my-python-app bash> bash opens terminsal insidee the container 

<cd python-docker> : docker builds and runs based on the current directory 

if using normal terminal nano <filename.py> 
used 

<pwd> checks the directory 

<ls> lists the file

<docker run -it -v $(pwd):/usr/src/app my-python-app python file.py>
 this command was so long so just use <drun filename,py>
 we have to create alias for this short commands 
for that open normal terminal and 
add this <~/.bashrc> and add this line 
<alias drun='docker run -it -v $(pwd):/usr/src/app my-python-app python'> 

att the end  the save and enter 

then rerun <source ~/.bashrc>

CKOSE VS CODE BEFORE ~/.bashrc THIS VS CONDE DOSENT AUTORELOAD 
and now open vs code and run <drun filename,py>
