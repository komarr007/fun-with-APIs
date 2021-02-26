import requests

#get the API
response = requests.get('https://indodax.com/api/tickers')
responseJson = response.json()
#listing dict
keys = list(responseJson['tickers'].keys())
values = list(responseJson['tickers'].values())

def interface():
    print("="*10,"source indodax","="*10)
    cryptoCurr=str(input("please input the abbreviation : "))
    exchange=str(input("idr or usdt :"))

    currencies = cryptoCurr+'_'+exchange

    if exchange == 'idr':
        if currencies in keys:
            print('\n',"="*10,currencies,"="*10,'\n')
            getindex = keys.index(currencies)
            for i in values[getindex]:
                if 'vol' in i :
                    print('{} : {}'.format(i,values[getindex][i]))
                elif 'server' in i:
                    print('{} : {}'.format(i,values[getindex][i]))
                else:
                    print('{} : Rp{:,.2f}'.format(i,int(values[getindex][i])))
        else:
            raise Exception('sorry we cannot found the cryptocurrencies')

    elif exchange == 'usdt':
        if currencies in keys:
            print('\n',"="*10,currencies,"="*10,'\n')
            getindex = keys.index(currencies)
            for i in values[getindex]:
                print('{} : {}'.format(i,values[getindex][i]))
        else:
            raise Exception('sorry we cannot found the crypto currencies')

    else:
        raise Exception('please input idr or usdt')
                    

if __name__ == "__main__":
    interface()
