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


def count_equipment_by_site (measurements : list[dict]) -> dict : 
    nb_equipement_site = {}
    for measurement in measurements : 
        site = measurement["site"]
        nb_equipement_site[site] = nb_equipement_site.get(site,0) + 1
    return nb_equipement_site


"""    {
        "equipment_id": "EQ005",
        "site": "Paris",
        "equipment_type": "Sensor",
        "temperature": 95.2,
        "status": "ERROR"
    }"""


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

print (nb_equipement_site )

print (moy_temp_site)

"""result = count_equipment_by_site (measurements)
print (result)"""

