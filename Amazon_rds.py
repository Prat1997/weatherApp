#from ensurepip import version
import pymysql

try:
    conn = pymysql.connect(
            host= 'weatherdb.crqb95iv4yuh.ap-south-1.rds.amazonaws.com',
            port = 3306,
            user = 'admin',
            password = '12345678'
            #db = rds.db #test
    )
except Exception as e:
    print(e)

try:

    #Getting version of RDS DB instance
    cursor=conn.cursor()
    cursor.execute("select version()")
    version = cursor.fetchall()
    print("AWS RDS Instance Version :- " , version)

except Exception as e:
    print(e)

#DB Creation
def db_create():
    
    create_db_sql="""
    create database if not exists Student_Info 
    """
    cursor.execute(create_db_sql)
    conn.commit()
    print("DB created Successfully")

#Show All Databases
def show_databases():
    show_db_sql="""
    show databases
    """
    cursor.execute(show_db_sql)
    db = cursor.fetchall()
    print (db)

# Use Databases
def use_database():
    use_db_sql="""
    use weatherApp
    """
    cursor.execute(use_db_sql)

#Table Creation
def table_create():
    #cursor=conn.cursor()
    create_table_sql="""
    create table if not exists Student_Details(
    id int primary key auto_increment not null,
    `Time` datetime,
    Name varchar(30),
    email varchar(30),
    comment varchar(100),
    gender varchar(10)
    );
    """
    cursor.execute(create_table_sql)
    print("Table created Successfully")


# Get data
def get_details():
    #cursor=conn.cursor()
    get_details_sql="""
    SELECT * FROM Weather_Details
    """
    cursor.execute(get_details_sql)
    details = cursor.fetchall()
    print(type(details))
    print (details)


#Put Data
#def insert_details(name,email,comment,gender):
def insert_details():
    #cursor=conn.cursor()
    insert_details_sql="""
    insert into Weather_Details values
    (0,CURRENT_TIMESTAMP,22.75,'Sun',275.777,40.35683,'INDIA',
    'Kanpur',89.76,78,99,85,0)
    """
    cursor.execute(insert_details_sql)
    conn.commit()
    print("Data Inserted Successfully")



def insert_weather_details(temprature,description,humidiy,wind_speed,country,
                            city,longitute,latitute,visibility,pressure,wind_degree):
    # insert_weather_details_sql="""
    # ("INSERT INTO Weather_Details VALUES (0,CURRENT_TIMESTAMP,%f,%s,%f,%f,%s,%s,%f,%f,%f,%f,%f)", (temp_city,desc,humidiy,wind_speed,country,
    # city_name,lon,lat,visibility,pressure,sea_level))
    # """
    # insert_weather_details_sql="""
    # ("INSERT INTO `Weather_Details` (id,`Time`,temprature,`description`,humidiy,wind_speed,country,city,
    # longitute,latitute,visibility,pressure,wind_degree) 
    # VALUES (0,CURRENT_TIMESTAMP,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
    # (temp_city,desc,humidiy,wind_speed,country,
    # city_name,lon,lat,visibility,pressure,sea_level))
    # """
    # cursor.execute(insert_weather_details_sql)
    sql = "INSERT INTO `Weather_Details` (Time,temprature,`description`,humidiy,wind_speed,country,city,longitute,latitute,visibility,pressure,wind_degree) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val=(temprature,description,humidiy,wind_speed,country,city,longitute,latitute,visibility,pressure,wind_degree)
    cursor.execute(sql, val)
    conn.commit()
    print("New Weather Data Inserted Successfully")


#use_database()
#insert_details()
#insert_weather_details()
#get_details()

#temp=temp_city,desc=desc,pressure=pressure,humidiy=humidiy,wind_speed=wind_speed,
                             #country=country,date_time=date_time,city_name=city_name,lon=lon,
                             #lat=lat,visibility=visibility,sea_level=sea_level)
# a='Prateek'
# b='singhprateek21sept@gmail.com'
# c='Prateek is a good developer'
# d='Male'
# e=int(45.89)
# print(type(e))


# def insert_details_demo(name,email,comment,gender,marks):
#     cur=conn.cursor()
#     cur.execute("INSERT INTO Student_Details (name,time,email,comment,gender,marks) VALUES (%s,CURRENT_TIMESTAMP,%s,%s,%s,%s)", (name,email,comment,gender,marks))
#     conn.commit()



# #db_create()
use_database()
# #table_create()

# insert_details_demo(a,b,c,d,e)