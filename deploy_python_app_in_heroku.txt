Deploying python app in Heroku :
================================

1. create a folder and name it (eg.myproject)

2. change directory to that folder and type "git init" command

3. create an empty file __init__.py file

4. create a requirements.txt file and add all the required modules for that project

5. create a runtime.txt file and add runtime (eg.python-3.9.5)

6. add all your python files and project files

7. create a "Procfile" and add [worker: python main.py] you can add any worker command

8. type "git add ." and "git commit" and commit it

9. now login to your heroku-cli

10. create an heroku app by "heroku create app_name" command

11. Then add git remote by "heroku git:remote -a app_name"

12. Now finally push your python app to heroku by "git push heroku master" command

13. Now you can see your python app may be running

14. If not , type "heroku ps:scale worker=0"

15. Then type "heroku ps:scale worker=1"

16. Now the app will run ...

