import psycopg2

class BD():

    def __init__(self, user="postgres", password="785623", host="127.0.0.1", port="5432", database= "data_amostra"):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def insert(self,G_ID,G_DATamostra, AccX, AccY, AccZ):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)
            cursor = connection.cursor()

            postgres_insert_query = """INSERT INTO amostra_t (id,data,accx,accy,accz) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (G_ID, G_DATamostra, AccX, AccY, AccZ)
            cursor.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            count = cursor.rowcount
            print(count, "amostras inseridas com sucesso na tabela amostra_t")

        except (Exception, psycopg2.Error) as error:
            print("falha na entrada de dados na tabela amostra_t", error)

        finally:

            if connection:
                cursor.close()
                connection.close()
                print("Conecção com o banco PostgreSQL encerrada")

    def InsertMuitas(self, records):

        try:
            connection = psycopg2.connect(user= self.user,
                                          password= self.password,
                                          host= self.host,
                                          port= self.port,
                                          database= self.database)
            cursor = connection.cursor()
            sql_insert_query = """INSERT INTO amostra_t (id,data,accx,accy,accz) VALUES (%s,%s,%s,%s,%s)"""

            cursor.executemany(sql_insert_query, records)
            connection.commit()
            print(cursor.rowcount, "amostras inseridas com sucesso na tabela amostra_t")

        except (Exception, psycopg2.Error) as error:
            print("falha na entrada de muitos dados na tabela amostra_t: {}".format(error))

        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Conecção com o banco PostgreSQL encerrada")

    def updateTable(self, amostra_tId, price):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()

            print("Table Before updating record ")
            sql_select_query = """select * from amostra_t where id = %s"""
            cursor.execute(sql_select_query, (amostra_tId,))
            record = cursor.fetchone()
            print(record)

            # Update single record now
            sql_update_query = """Update amostra_t set price = %s where id = %s"""
            cursor.execute(sql_update_query, (price, amostra_tId))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record Updated successfully ")

            print("Table After updating record ")
            sql_select_query = """select * from amostra_t where id = %s"""
            cursor.execute(sql_select_query, (amostra_tId,))
            record = cursor.fetchone()
            print(record)

        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)

        finally:
            # closing self.database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def deleteData(self, amostra_tId):
        try:
            connection = psycopg2.connect(user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port,
                                          database=self.database)

            cursor = connection.cursor()

            # Update single record now
            sql_delete_query = """Delete from amostra_t where id = %s"""
            cursor.execute(sql_delete_query, (amostra_tId,))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record deleted successfully ")

        except (Exception, psycopg2.Error) as error:
            print("Error in Delete operation", error)

        finally:
            # closing self.database connection.
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")