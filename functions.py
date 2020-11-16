


def get_lat(location):
    lat = location.get("latitude")
    return lat

def get_long(location):
    long = location.get("longitude")
    return long

def create_geopoint_from_office(location):
    lat = get_lat(location)
    long = get_long(location)
    geop = {'type': 'Point', 'coordinates': [lat, long]}
    return geop

def single_rater(dist, max_dist):
    if dist< max_dist:
        return dist/max_dist
    else:
        return 2

#model which will give lower scores to offices which are better located

def overall_rater(row):
    formula = single_rater(row["starb_dist"],300) + single_rater(row["airport_distance"],15000) + single_rater(row["school_distance"],4000) + single_rater(row["nightclub_distance"],1000) + single_rater(row["vegan_distance"],300) + single_rater(row["basketball_distance"],10000) + single_rater(row["dobby_distance"],4000)
    return formula