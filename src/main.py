import csv


def  load_measurements(file_path : str) : 
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        list_measure_valid = []
        list_measure_non_valid = []
        for measurement in reader:
            try :
                measurement["temperature"] = float(measurement["temperature"])
                list_measure_valid.append(measurement)
            except ValueError:
                list_measure_non_valid.append(measurement)
    return list_measure_valid,list_measure_non_valid


 

"""
measurements = [
    {
        "equipment_id": "EQ001",
        "site": "Toulouse",
        "equipment_type": "Sensor",
        "temperature": 72.4,
        "status": "OK"
    },
    {
        "equipment_id": "EQ002",
        "site": "Bordeaux",
        "equipment_type": "Motor",
        "temperature": 91.8,
        "status": "WARNING"
    },
    {
        "equipment_id": "EQ003",
        "site": "Toulouse",
        "equipment_type": "Sensor",
        "temperature": 68.1,
        "status": "OK"
    },
    {
        "equipment_id": "EQ004",
        "site": "Bordeaux",
        "equipment_type": "Motor",
        "temperature": 87.3,
        "status": "OK"
    },
    {
        "equipment_id": "EQ005",
        "site": "Paris",
        "equipment_type": "Sensor",
        "temperature": 95.2,
        "status": "ERROR"
    }
]
"""

def count_equipment_by_site (measurements : list[dict]) -> dict : 
    nb_equipement_site = {}
    for measurement in measurements : 
        site = measurement["site"]
        nb_equipement_site[site] = nb_equipement_site.get(site,0) + 1
    return nb_equipement_site

def average_temperature_by_site(measurements: list[dict]) -> dict:
    nb_equipement_site = {}
    temp_total_par_site = {}
    moy_temp_site = {}
    for measurement in measurements : 
        site = measurement["site"]
        temperature = measurement["temperature"]
        nb_equipement_site[site] = nb_equipement_site.get(site,0) + 1
        temp_total_par_site[site] = temp_total_par_site.get(site,0) + temperature
    for site, temp  in temp_total_par_site.items():
        moy_temp_site[site] = temp / nb_equipement_site[site] 
    return moy_temp_site

def filter_anomalie (measurements : list[dict], statuses : set[str]) : 
    anomalie = []
    for measurement in measurements : 
        erreur = measurement["status"]
        if erreur in statuses : 
            anomalie.append(measurement)
    return (anomalie)

def generate_equipment_report(measurements: list[dict] , statuses : set[str]) -> dict: 
    equipement_rapport = {}
    equipement_rapport["total_measurements"] = len(measurements)
    equipement_rapport["equipment_by_site"] = count_equipment_by_site (measurements)
    equipement_rapport["average_temperature_by_site"] = average_temperature_by_site(measurements)
    equipement_rapport["anomalies"] = filter_anomalie(measurements, statuses)
    return equipement_rapport

measurements = load_measurements("data/measurements.csv")
report = generate_equipment_report(
    measurements,
    {"ERROR", "WARNING"}
)
print (report)
print("Mesures valides :", len(measurements))