git init	初始化

git add	将工作区修改放到暂存区

git commit -m “ ” 将暂存区修改提交到库

git status

git diff	库和工作目录的区别

git diff --staged	staged 和 HEAD 的区别



git log	查看历史版本

git log --pretty=oneline 简化查看历史输出

HEAD表示当前版本，HEAD^上个版本, HEAD^^上上个版本......HEAD~100上100个版本

git reset filename			unstage file

git reset --hard HEAD^	退回上一版本

git reflog	查看过去的每次命令（版本参数 ref-参数  log-版本）

git checkout -- filename	将工作区还原到上一个add 或commit时的状态

git reset HEAD filename	撤销暂存区修改

git remote add origin git@server-name:path/repo-name.git	要关联一个远程库，使用命令

关联后，使用命令git push -u origin master第一次推送master分支的所有内容；



git push origin master	把本地master分支的最新修改推送至GitHub

如果push出错，原因可能是github上更改过，可用 git pull --rebase origin master

git clone *git@github.com:username/dirname*   克隆远程库(ssh)

git checkout -b branchname	新建（-b）并切换（checkout）

git branch	查看当前分支

git branch branchname	创建分支

git branch -d branchname	删除当前分支 -d delete

git checkout	切换分支

git merge branchname	合并指定分支到当前分支 merge 融合

git merge --no-ff -m "merge with no-ff" dev 禁用fast forward 以保留分支的更改历史

git log --graph --pretty=oneline --abbrev-commit

git stash 储藏工作区修改

git stash list 查看储藏

git stash apply 恢复但不删除stash

git stash pop 恢复并删除stash

开发一个新feature，最好新建一个分支

git push origin branch-name 推送

git pull 更新本地（将远程与本地的合并）如有冲突，先手动解决冲突

git remote 查看远程库信息

git remote -v 更详细的信息

git tag <name> 为当前版本库打标签

git tag 查看所有标签

git tag <tagname> <commit id> 补打标签

git tag -a v0.1 -m "version 0.1 released" 3628164		-a （？）指定标签名 -m 制定说明文字

git show <tagname> 看说明文字

git tag -d <tagname> 删除标签

git push origin <tagname> 推送标签至远程

git push origin --tags 一次推送全部标签至远程

git push origin :refs/tags/<tagname> 删除远程标签(先要删除本地标签)

git config --global alias.st status 将status命令简化为st

