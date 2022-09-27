# ВИДЕО ХОСТИНГ

### Сценарий использования
Пользователь может загрузить видео (сами данные, название, описание и т.д.), при необходимости может удалить его, изменить и, конечно, поделиться ссылкой на него.

### Эндпоинты
* `/upload` - загрузить видео на сервис
* `/watch?video=<id>` - посомтреть видео
* `/info?video=<id>` - мета информация про видео
* `/delete?video=<id>` - удалить видео
* `/change?video=<id>&param=<new-param>` - измениьт мета информацию  
`param` =
    * content
    * name
    * description