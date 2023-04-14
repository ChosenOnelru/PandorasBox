# PandorasBox
PandorasBox group training repository

Порядок действий:
1. Подключить GitHub в PyCharm (File > Settings > Version Control > GitHub)
2. Склонировать проект из удаленного репозитория (Close project > Get from VCS > [project URL])
3. Создать окружение (File > Settings > Project > Add)
4. Создать локальную ветку из склонированного проекта (New Branch) и переключиться на нее
5. Внести изменения в локальной ветке
6. Сделать коммит и запушить изменения в удаленный репозиторий (Commit > Commit and Push)
7. Создать Merge Request на GitHub для слияния нашей ветки и main-ветки проекта
8. При возникновении конфликтов при выполнении Merge Request необходимо:
          
          8.1 Обновить локальную ветку main (Main > Update)
          
          8.2 Объединить обновленный main и свою ветку (Main > Merge main into [branch_name])
          
          8.3 Разрешить конфликт
          
          8.4 Запушить измененную ветку

9. После разрешения кофликтов и прохождения ревью кода ветка с изменениями мерджиться в main
10. Обновить локальную main (Main > Update) ипереключиться на нее


Для командной строки:

2 git clone url [folder]
4 git checkout -b [branch_name]
6 git add . (если создавали новые файлы)
  git commit -m "Added beautiful fixes"
  git push --set-upstream origin [branch_name]  # при первом пуше
  git push                                      # когда ветка создана
10 git checkout main
    
   git pull

тренажер по Git
https://learngitbranching.js.org/?locale=ru_RU
