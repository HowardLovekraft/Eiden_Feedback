# How to set up a project  
There is 2 ways how to set up this bot:  
1. Using Docker (or batch script)
2. Using main.py

## Using Docker  
1. Run ```poetry lock``` (to install all requirements)
2. Place code into Docker container:  
```docker build -t eiden_feed```  
   * IF YOU'RE WINDOWS USER: 
     1. Rename ```start_docker_example.bat``` to ```start_docker.bat```
     2. Fill in your ```.bat``` file
     3. Run ```start_docker.bat```  
     (by click on .bat file or using alias in root folder)
   * IF YOU'RE LINUX USER:  
   There's no way except rewrite batch script to bash :-(

## Using main.py
1. Fill in your .env file (example.env will help you)
2. Run main.py by your Python interpreter

### ENJOY!
