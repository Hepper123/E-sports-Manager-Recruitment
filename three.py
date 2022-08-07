import pymysql as sql
import environment as envir

connect = sql.connect(host = envir.host, port = envir.port, user = envir.user, password = envir.password, database = envir.database)

cursor = connect.cursor()

def three_a():
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

    team = ["EDG", "RNG", "JDG", "FPX", "V5", "RA", "IG", "AL", "BLG", "LNG", "TES", "OMG", "WE", "WBG", "UP", "TT"]
    print("1.EDG 2.RNG 3.JDG 4.FPX 5.V5 6.RA 7.IG 8.AL 9.BLG 10.LNG 11.TES 12.OMG 13.WE 14.WBG 15.UP 16.TT")
    t1 = int(input("选择team1:"))
    t2 = int(input("选择team2:"))
    t3 = int(input("选择team3:"))
    t4 = int(input("选择team4:"))

    team_a = []
    team_a.append(team[t1 - 1])
    team_a.append(team[t2 - 1])
    team_a.append(team[t3 - 1])
    team_a.append(team[t4 - 1])

    tag_2 = ["大心脏", "操作", "状态", "头脑", "训练态度", "节目效果", "高光"]
    print("1.大心脏 2.操作 3.状态 4.头脑 5.训练态度 6.节目效果 7.高光")
    ta1 = int(input("选择tag1:"))
    ta2 = int(input("选择tag2:"))
    ta3 = int(input("选择tag3:"))

    tag_a = []
    tag_a.append(tag_2[ta1 - 1])
    tag_a.append(tag_2[ta2 - 1])
    tag_a.append(tag_2[ta3 - 1])

    # 地区+战队+tag
    for t in team_a:
        for ta in tag_a:
            sql = "select * from 招聘 where location = %s and team = %s and tag2 = %s"
            cursor.execute(sql, (location, t, ta))
            result = cursor.fetchall()
            for row in result:
                name = row[1]
                if(row[6]):
                    SSR = "SSR"
                else:
                    SSR = "SR"
                print("name = %s, location = %s, team = %s, tag = %s, %s"%(name, location, t, ta, SSR))

if __name__ == "__main__":
    three_a()