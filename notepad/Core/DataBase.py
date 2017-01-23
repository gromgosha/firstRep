
from PyQt5.QtCore import QObject, QFile
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

SHEMA = 'Resourses.shema.sql'
DATABASE_NAME = 'diary.sqlite'

class DataBase(QObject):
    def __open(self):            #открытие базы
        self.__db = QSqlDatabase().addDatabase('QSQLITE')
        self.__db.setDatabaseName(DATABASE_NAME)
        return self.__db.open()

    def __restore(self):            #восстановление базы
        if not self.__open():
            return False

        queries = open(SHEMA).read().split(';')         #чтение файла, разбитие по ; и запись в список

        for query in queries:
            query = query.strip()           #для отрезания пробельных символов с обеих сторон

            if query:
                sql = QSqlQuery(self.__db)       #чтение базы
                
                if not sql.exec(query):
                    QFile(DATABASE_NAME).remove()
                    return False
        return True

    def connect(self):
        return self.__open() if QFile(DATABASE_NAME).exists() else  self.__restore()