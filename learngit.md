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

git push origin master	把本地master分支的最新修改推送至GitHub



