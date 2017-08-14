git init	初始化

git add	将工作区修改放到暂存区

git commit -m “ ” 将暂存区修改提交到库

git status

git diff	库和工作目录的区别

git log	查看历史版本

git log --pretty=oneline 简化查看历史输出

HEAD表示当前版本，HEAD^上个版本, HEAD^^上上个版本......HEAD~100上100个版本

git reset --hard HEAD^	退回上一版本

git reflog	查看过去的每次命令（版本参数 ref-参数  log-版本）

git checkout -- filename	将工作区还原到上一个add 或commit时的状态

git reset HEAD filename	撤销暂存区修改

git remote add origin git@server-name:path/repo-name.git	要关联一个远程库，使用命令

关联后，使用命令git push -u origin master第一次推送master分支的所有内容；

git push origin master	把本地master分支的最新修改推送至GitHub

git clone *git@github.com:username/dirname*   克隆远程库(ssh)

git checkout -b branchname	新建（-b）并切换（checkout）

git branch	查看当前分支

git branch branchname	创建分支

git branch -d branchname	删除当前分支 -d delete

git checkout	切换分支

git merge branchname	合并指定分支到当前分支 merge 融合

git merge --no-ff -m "merge with no-ff" dev 禁用fast forward 以保留分支的更改历史

git log --graph --pretty=oneline --abbrev-commit