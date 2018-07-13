  ubuntu上传方法
--------------------------- 
  1.github: creat a repository's-name
  
  2.git clone https://github.com/XingXL/repository's-name.git  
  ***一般第一步clone***   
  3.将待上传文件复制到文件夹repository's-name中
    
  4.git add .
  
  5.git commit -m "added ."
  
  6.git push  
  Username for 'https://github.com': XingXL  
  Password for 'https://XingXL@github.com':
    
  7.更新文件或文件夹:
  
  git pull
  
  git push
  
  windows上传方法
--------------------------- 
  1.github: creat a repository's-name
  
  2.In ~/Documents/git_repository: git clone https://github.com/XingXL/repository's-name.git
  
  3.In ~/Documents/git_repository/repository's-name: 
      
      git init
      
      git add .
      
      git commit -m "first commit ."  // git commit -m "added"
      
      git remote add origin https://github.com/XingXL/repository's-name.git
      
      if  fatal: remote origin already exists. --> git remote rm origin --> repeat 上一步
      
      git push -u origin master
