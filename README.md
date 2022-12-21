<p align="center">
<img title="Logo" src="images/Wikipedia.svg">
</p>

## Демо-проект по автоматизации тестирования мобильного приложения: Wikipedia APP
:earth_americas: https://ru.wikipedia.org/

<p>К тестам прилагается бонусный функционал:</p>
* графический визуальный отчет
* возможность запуска с любого компьютера без установки спец.софта


## :watermelon: Реализованы следующие проверки:

<br>:white_check_mark: Поисковый запрос Browser Strack с проверкой
<br>:white_check_mark: Очистка данных 
<br>:white_check_mark: Новый поисковый запрос Erik Bruhn с проверкой

## :four_leaf_clover: Languages and Tools:
<code><img src="images/logo/python.svg" width="40" height="40"  alt="olgakos" title="Python"></code>
<code><img src="images/logo/pycharm.png" width="40" height="40"  alt="olgakos" title="PyCharm"></code>
<code><img src="images/logo/browserstack.png" width="40" height="40"  alt="olgakos" title="BrowserStack"></code>
<code><img src="images/logo/pytest.png" width="40" height="40"  alt="olgakos" title="PyTest"></code>
<code><img src="images/logo/selene.png" width="40" height="40"  alt="olgakos" title="Selene"></code>
<code><img src="images/logo/Jenkins.svg" width="40" height="40"  alt="olgakos" title="Jenkins"></code>
<code><img src="images/logo/Allure.svg" width="40" height="40"  alt="olgakos" title="Allure Report"></code>
<code><img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" width="40" height="40" alt="Git" title="Git"></code>
<code><img src="images/logo/GitHub.svg" width="40" height="40"  alt="olgakos" title="Github"></code>


## :watermelon: Jenkins. Удаленный запуск тестов (онлайн) 
Не требует установки программ на компьютер пользователя! Работает "как есть" онлайн.

Способ 1. Быстрый вариант, только просмотр:
1. <i>Не зарегистрированным</i> пользователем перейти на страницу сборки проекта по ссылке: 
<a target="_blank" href="https://jenkins.autotests.cloud/job/C02_OlgaKos_python_wikipedia_app_test/">Jenkins project</a>
2. Kликнуть на желтую иконку "Allure Report" и ознакомиться в графическим отчетом о результатах последнего запуска тестов.  
<p align="center">
<img title="Allure Graphics" src="images/jenkins_see_allure.jpg" alt="jenkins_see_allure" width="600">
</p>

Способ 2. Запустить тесты самостоятельно: 
1. <i>Зарегистрированным/Не зарегистрированным</i> пользователем перейти на страницу сборки проекта по ссылке: 
<a target="_blank" href="https://jenkins.autotests.cloud/job/C02_OlgaKos_python_wikipedia_app_test/">Jenkins project</a>
4. Запустить выполнение тестов кнопкой "Собрать"
5. Дождаться окончания прогона (~2 минуты)
6. Кликнуть на желтую иконку "Allure Report" и получить свежий Allure Report. NB! срок хранения демо-сборки ограничен. Сборка может быть деактвирована ~через 8 недель.  
<p align="center">
<img title="Allure Graphics" src="images/jenkins_do_allure.jpg" alt="jenkins_do_allure" width="600">
</p>

###### Главный экран Allure отчета (Owerwiev)
<p align="center">
<img title="Allure Graphics" src="images/Allure1.jpg" alt="Allure Graphics" width="600">
</p>

###### Страница с проведенными тестами (Suites)
<p align="center">
<img title="Allure Graphics" src="images/Allure2.jpg" alt="Allure Graphics" width="600">
</p>

<details>
    <summary><i>Легенда</i></summary>
###  Легенда: 
###### Главная страница Allure-отчета содержит следующие информационные блоки:
- `ALLURE REPORT` отображает: Дату и время прохождения теста. Общее количество пройденных кейсов. Диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
- `TREND` - отображает тренд прохождения тестов от сборки к сборке
- `SUITES` - отображает распределение результатов тестов по тестовым наборам
- `ENVIRONMENT` - отображает тестовое окружение (стенд), на котором запускались тесты. <i>В данном демо-примере информация не задана.</i>
- `CATEGORIES` - отображает распределение неуспешно прошедших тестов по видам дефектов
- `FEATURES BY STORIES` - отображает распределение тестов по функционалу, который они проверяют
- `EXECUTORS` - отображает исполнителя текущей сборки (ссылка на сборку в Jenkins)
</details>

## :watermelon: Видео прохождения тестов
К каждому тесту (в отчете) прилагается автоматически сгенерированное видео. Пример:
<p align="center">
  <img title="Selenoid Video" src="images/Video_bs2.mp4) alt="Video" width="400">
</p>

-------
2022-12-21
Сборка в Дженкинс: https://jenkins.autotests.cloud/job/C02_OlgaKos_python_wikipedia_app_test/
Аллюр отчет: https://jenkins.autotests.cloud/job/C02_OlgaKos_python_wikipedia_app_test/7/allure/#