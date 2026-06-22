from database.DB_connect import DBConnect
from model.arco import Arco
from model.pilota import Pilota


class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getPiloti(a,b):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT distinct d.*
                    FROM results rs , drivers d , races r
                    where rs.`position` is not null and d.driverId =rs.driverId and r.raceId =rs.raceId and r.`year` between %s and %s 
                    """

        cursor.execute(query,(a,b,))

        for row in cursor:
            results.append(Pilota(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getArchi(a,b,idMap):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
    rs1.driverId AS pilota1,
    rs2.driverId AS pilota2,
    COUNT(r.raceId) AS peso
FROM 
    results rs1,
    results rs2,
    races r,
    status s1,
    status s2
WHERE 
    rs1.raceId = rs2.raceId 
    AND rs1.constructorId = rs2.constructorId 
    AND r.raceId = rs1.raceId
    AND rs1.statusId = s1.statusId
    AND rs2.statusId = s2.statusId
    
    AND rs1.driverId < rs2.driverId 
    
    AND r.`year` BETWEEN %s AND %s
    

    AND (s1.`status` = 'Finished' OR s1.`status` LIKE '+%Lap%')
    AND (s2.`status` = 'Finished' OR s2.`status` LIKE '+%Lap%')
GROUP BY 
    rs1.driverId, 
    rs2.driverId
                            """

        cursor.execute(query, (a, b,))

        for row in cursor:
            results.append(Arco(idMap.get(row["pilota1"]),idMap.get(row["pilota2"]),row["peso"]))

        cursor.close()
        conn.close()
        return results



