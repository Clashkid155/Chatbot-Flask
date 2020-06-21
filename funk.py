from re import search
from covid import Covid

covid=Covid()

def Covi(coun=None):
    coun =str(coun)
    global result
    result = []
    rq =""
    try:
        with open('countries.txt') as country:
            country = country.read()
        # check if covid is in user input and slice it
        if search(r"(?i)^covid", coun) and coun[6:] in country:
            ms = coun[6:]
            rona = covid.get_status_by_country_name(ms)
            for key, value in rona.items():
                if not search((".tude|id|._."),key):
                    ko= key+":"+str(value)
                    result.append(ko)
            rq=" ".join(str(i) for i in result)
            if True:
                return rq
    except ValueError:
        return "Not working"
