from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "e94c6093eemshfb18806af50648fp17539djsn5e9b9ef05acf",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


def index(request):
    noofresults = response['results']
    mylist = []
    for i in range(0, noofresults):
        mylist.append(response['response'][i]['country'])
        mylist.sort()
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                population = response['response'][x]['population']
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                death = int(total)-int(active)-int(recovered)

                context = {'selectedcountry': selectedcountry, 'mylist': mylist, 'population': population, 'new': new,
                           'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'death': death}
                return render(request, 'index.html', context)

    context = {'mylist': mylist}
    return render(request, 'index.html', context)
