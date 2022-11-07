
import pandas as pd
if __name__ == '__main__':
    print("hello")
    data = pd.read_csv('C:\Bigmarket.csv')
    print(data)
    print(type(data))
    print(data.head())
    print(data.tail())
    print(data.shape)
    print(data.info())
    print(data.iloc[2:4])
    print(data.iloc[2:4]['Sales'])
    print(data.iloc[2:4,2])

    print(data[data.Sales > 40000])
    print(data[(data.Sales > 40000) & (data.Month == 'Feb')])
    print(data.sort_values('Sales', ascending=True))
    print(data.sort_values('Sales', ascending=False).iloc[:5])#higest sales top 5
    print(data.sort_values(['Store','Sales']))
 #-----------------------------------------
 #Dictionary

if __name__ == '__main__':
    print("hello")
    data = pd.read_csv('C:\Bigmarket.csv') # 2 records adding
    dict = {'Month': ['June','June'], 'Store': ['A', 'B'], 'Sales': [30000, 56000]}
    newdata = pd.DataFrame(dict)
    print(newdata)
    #appending this newdata to the  file

    print(data.append(newdata))
    print(pd.concat([data,newdata], ignore_index=True))#0,1 index will go 24,25 index come

    #adding column cities
    states = ['Alaska', 'Texas', 'california', 'Montana', 'New Mexico']
    states1 = states*5
    statedic = {'State': states1}
    newcol = pd.DataFrame(statedic)
    print(newcol)

    # add this column to existing data

    print(pd.concat([data, newcol], axis=1)) #coulumn axis=1  row axis =0 ; need to give axis =1 for adding column

    #total sales
    print(data['Sales'].sum())
    #i want sum of store A
    #print(data[data.Store == 'A'].sum())
    print(data[data['Store'] == "A"]['Sales'].sum())
    #----------------------------------------------
    #compare the sales of store B and E share output in %
    #data1 = data[data.Store == 'E']['Sales'].sum()
    #data2 = data[data.Store == 'D']['Sales'].sum()
    #print((data1 / data2) * 100)
#    ------------------------------------------------

    B = (data[data['Store'] == 'B']['Sales'].sum())
    E = (data[data['Store'] == 'E']['Sales'].sum())

    print(B / E * 100)
#-------------------------------------------------------

    StoreA = (data[data['Store'] == "A"]['Sales'].sum())
    print(StoreA)
    StoreB = (data[data['Store'] == "B"]['Sales'].sum())
    print(StoreB)
    StoreE = (data[data['Store'] == "E"]['Sales'].sum())
    print(StoreE)
    print((StoreB / StoreE) * 100)
    #----------------------------------------
    #word count
    print(data['Month'].value_counts())#group by in python important
    print(data['Store'].value_counts())

    #print(data['Sales'].replace([31037],50000))# changing value of sales column value,one value change
    data['Sales']=data['Sales'].replace([31037], 50000)#shows the change with all columns
    print(data.head())
# delete a record
    print(data.drop([0])) #first row deleted 0 index is deleted that is first row
    data = data.rename(columns={"Store":"NewStore"}) #rename the coulumn value stores to new store
    print(data.head())
