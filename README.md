# Event planner


Чтобы запустить приложение на локальной машине нужно:

* склонировать этот репозиторий
* перейти в папку репозиторием
* Выполнить в командной строке команду docker-compose up -d
* После того как команда выполнена успешна, на 127.0.0.1:5000
* Чтобы редактировать события нужно перейти в директорию app 
* и в файле edit_delete_events.py набрать команду cursorObj.execute("UPDATE events SET theme = 'xxxxxxx' where _id = 1;")
* Чтобы удалить событие набрать команду cursorObj.execute("DELETE FROM events WHERE _id = 2")
