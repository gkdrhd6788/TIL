# About git

* 브랜치 명은 소문자로!!

 

```bash
cd ..

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git add .
warning: in the working copy of 'front-end/src/App.jsx', LF will be replaced by CRLF the next time Git touches it    

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git commit -m "Feat: MainPage 수정 중"
[front-feat/sidebar 6cf5789] Feat: MainPage 수정 중
 4 files changed, 26 insertions(+), 11 deletions(-)
 create mode 100644 front-end/src/pages/workspace/components/WorkspaceBody.jsx

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git remote -v
origin  https://ssafy05@i10B310.p.ssafy.io:8989/a/S10P12B310 (fetch)
origin  https://ssafy05@i10B310.p.ssafy.io:8989/a/S10P12B310 (push)

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git push origin
fatal: The current branch front-feat/sidebar has no upstream branch.
To push the current branch and set the remote as upstream, use      

    git push --set-upstream origin front-feat/sidebar

To have this happen automatically for branches without a tracking   
upstream, see 'push.autoSetupRemote' in 'git help config'.

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git push --set-upstream origin front-feat/sidebar 
Enumerating objects: 20, done.
Counting objects: 100% (20/20), done.
Delta compression using up to 12 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (11/11), 1.14 KiB | 1.14 MiB/s, done.
Total 11 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6)
remote: Processing changes: refs: 1, done
To https://i10B310.p.ssafy.io:8989/a/S10P12B310
   e87f343..6cf5789  front-feat/sidebar -> front-feat/sidebar
branch 'front-feat/sidebar' set up to track 'origin/front-feat/sidebar'.

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git branch
  front-feat/card
  front-feat/header

* front-feat/sidebar
  master

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git remote update
remote: Counting objects: 181, done
remote: Finding sources: 100% (132/132)
remote: Total 132 (delta 49), reused 132 (delta 49)
Receiving objects: 100% (132/132), 1.11 MiB | 20.99 MiB/s, done.
Resolving deltas: 100% (49/49), completed with 7 local objects.
From https://i10B310.p.ssafy.io:8989/a/S10P12B310
   abd2532..2c3616c  develop           -> origin/develop
   64f8560..4257fbf  front-feat/card   -> origin/front-feat/card

 * [new branch]      front-feat/design -> origin/front-feat/design

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git branch
  front-feat/card
  front-feat/header

* front-feat/sidebar
  master

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git branch -a
  front-feat/card
  front-feat/header

* front-feat/sidebar
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/develop
  remotes/origin/front-feat/card
  remotes/origin/front-feat/design
  remotes/origin/front-feat/header
  remotes/origin/front-feat/sidebar
  remotes/origin/master

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/sidebar)
$ git checkout front-feat/design
Switched to a new branch 'front-feat/design'
branch 'front-feat/design' set up to track 'origin/front-feat/design'.

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/design)
$ git merge front-feat/sidebar
Auto-merging front-end/src/App.jsx
CONFLICT (content): Merge conflict in front-end/src/App.jsx
Automatic merge failed; fix conflicts and then commit the result.

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/design|MERGING)
$ git add .

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/design|MERGING)
$ git push origin
Everything up-to-date

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/design|MERGING)
$ 



SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/design|MERGING)
$ git remote update

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/design)
$ git branch
  front-feat/card

* front-feat/design
  front-feat/header
  front-feat/sidebar
  master

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (front-feat/design)
$ git switch -c front-feat/mainpage
Switched to a new branch 'front-feat/mainpage'

SSAFY@DESKTOP-LL7FDJ6 MINGW64 ~/Desktop/class/S10P12B310 (fro
```



# Gerrit

* review를 위한 push

git push <remote명> HEAD:refs/for/<branch명>  

예시: git push origin HEAD:refs/for/develop
