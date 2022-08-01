import pymysql as sql

host = "127.0.0.1"
port = 3306
user = "root"
password = ""
database = "电竞经理"

connect = sql.connect(host = host, port = 3306, user = user, password = password, database = database)

cursor = connect.cursor()

def two_a():
    position = ["上路", "打野", "中路", "下路", "辅助"]
    print("1.上路 2.打野 3.中路 4.下路 5.辅助")
    p_1 = int(input("选择分路1:"))
    p_2 = int(input("选择分路2:"))
    position_a = []
    position_a.append(position[p_1 - 1])
    position_a.append(position[p_2 - 1])
    
    print("1.华中 2.华东 3.华南 4.华北 5.西南 6.东北 7.外援")
    l = int(input("选择地区："))
    if(l == 1):
        location = "华中"
    elif(l == 2):
        location = "华东"
    elif(l == 3):
        location = "华南"
    elif(l == 4):
        location = "华北"
    elif(l == 5):
        location = "西南"
    elif(l == 6):
        location = "东北"
    elif(l == 7):
        location = "外援"
    else:
        exit()

    tag_1 = ["直播天才", "经验丰富", "上分机器", "排位王者"]
    print("1.直播天才 2.经验丰富 3.上分机器 4.排位王者")
    ta1_1 = int(input("选择第一个tag1:"))
    ta1_2 = int(input("选择第二个tag1:"))


    tag_2 = ["大心脏", "操作", "状态", "头脑", "训练态度", "节目效果", "流量"]
    print("1.大心脏 2.操作 3.状态 4.头脑 5.训练态度 6.节目效果 7.流量")
    ta2_1 = int(input("选择第一个tag2:"))
    ta2_2 = int(input("选择第二个tag2:"))
    ta2_3 = int(input("选择第三个tag2:"))

    tag_a = []
    tag_a.append(tag_1[ta1_1 - 1])
    tag_a.append(tag_1[ta1_2 - 1])
    tag_a.append(tag_2[ta2_1 - 1])
    tag_a.append(tag_2[ta2_2 - 1])
    tag_a.append(tag_2[ta2_3 - 1])

    # 位置+地区+tag
    for p, ta in zip(position_a, tag_a):
        sql = "select * from 招聘 where position = %s and location = %s and (tag1 = %s or tag2 = %s)"
        cursor.execute(sql, (p, location, ta, ta))
        result = cursor.fetchall()
        for row in result:
            name = row[1]
            if(row[6]):
                SSR = "SSR"
            else:
                SSR = "SR"
            print("name = %s, position = %s, location = %s, tag = %s, %s"%(name, p, location, ta, SSR))
    # 位置+2tag
    for p, ta_1, ta_2 in zip(position_a, tag_a[0:2], tag_a[2:5]):
        sql = "select * from 招聘 where position = %s and tag1 = %s and tag2 = %s"
        cursor.execute(sql, (p, ta_1, ta_2))
        result = cursor.fetchall()
        for row in result:
            name = row[1]
            if(row[6]):
                SSR = "SSR"
            else:
                SSR = "SR"
            print("name = %s, position = %s, tag1 = %s, tag2 = %s, %s"%(name, p, ta_1, ta_2, SSR))
    # 地区+2tag
    for ta_1, ta_2 in zip(tag_a[0:2], tag_a[2:5]):
        sql = "select * from 招聘 where location = %s and tag1 = %s and tag2 = %s"
        cursor.execute(sql, (location, ta_1, ta_2))
        result = cursor.fetchall()
        for row in result:
            name = row[1]
            if(row[6]):
                SSR = "SSR"
            else:
                SSR = "SR"
            print("name = %s, location = %s, tag1 = %s, tag2 = %s, %s"%(name, location, ta_1, ta_2, SSR))