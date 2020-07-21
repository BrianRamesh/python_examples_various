import pandas as pd
pd.set_option('display.max_columns',None) # used to make all columns to be printed

all_pokemon_data = pd.read_csv('pokemon_data.csv')
#all_pokemon_data = pd.read_csv('pokemon_data.csv',delimiter='\t') use it for txt files that are tabe seperated
#delimiter can be changed e.g =xx or \n
#pd.read_excel   function might also be used fro excel files


#get first 5 rows
print(all_pokemon_data.head(5))

#get last 5 rows
print(all_pokemon_data.tail(5))

#get all columns
print(all_pokemon_data.columns)

#get 5 values of a specific column
#print(all_pokemon_data['Name'])   in order to get all values
print(all_pokemon_data['Name'][0:10])

#get multiple columns
print(all_pokemon_data[['Name','Attack','Defense']][5:8])

#read specific rows
print(all_pokemon_data.iloc[7:13])  # starts 7 but ends 12
print(all_pokemon_data.iloc[7:8])  # reads only row7

#read specific row and columns only
print(all_pokemon_data[['Name','Attack','Defense']].iloc[7:13])

#read with cordinates
print(all_pokemon_data.iloc[2,3])

#lets say we have to go through each row to do a sort of calculation then
fw=open('pandas_pokemon_list.txt','w')
for x,y in all_pokemon_data.iterrows(): # y is column
    s,m=(x,y['Name']) #this is not calculation it is just an example to see how wwe itterate through each row
    fw.write(str(s)+"  "+str(m)+"\n")
fw.close()

#save pokemons that have type1=fire into a new csv file
m=all_pokemon_data.loc[all_pokemon_data['Type 1']=='Fire']

m.to_csv('pandas_data_of_pok_with_type1_fire.csv')
type1_fire_pok_data=pd.read_csv('pandas_data_of_pok_with_type1_fire.csv')
m.to_csv('pandas_data_of_pok_with_type1_fire.txt',index=False, sep='\t' )
m.to_excel('pandas_data_of_pok_with_type1_fire.xlsx', index=False)

#get min max etc
print("\n\n\n")
print(all_pokemon_data.mean())
print(all_pokemon_data.describe())

#sort data by using one column
print(m.sort_values('Name'))
print(m.sort_values('Name',ascending=False))

#sort data by using multiple columns
print(m.sort_values(['Type 1', 'HP']))  # both ascending
print(m.sort_values(['Type 1', 'HP'],ascending=False)) #both descending
print(m.sort_values(['Type 1','HP'],ascending=[1,0])) # type1 ascending and hp descending

#adding a new column called total in our data
all_pokemon_data['Total']=all_pokemon_data['HP']+all_pokemon_data['Attack']+all_pokemon_data['Defense']+all_pokemon_data['Sp. Atk']+all_pokemon_data['Sp. Def']+all_pokemon_data['Speed']
all_pokemon_data['total_second_method']=all_pokemon_data.iloc[:,4:10].sum(axis=1)
print(all_pokemon_data.head(3))

#delete a column
all_pokemon_data=all_pokemon_data.drop(columns=['total_second_method'])
# must put all_pokemon_data=... so that it will be deleted
# only writting :all_pokemon_data.drop(columns=['total_second_method']), is not enough
print(all_pokemon_data.head(3))

#rearange columns new column total must no be at the end
cols = list(all_pokemon_data.columns)
all_pokemon_data=all_pokemon_data[cols[0:10]+[cols[-1]]+cols[10:12]]
print(all_pokemon_data.columns)
all_pokemon_data.to_csv('pandas_pokemondata_with_new_column.csv')
all_pokemon_data.to_excel("pandas_pokemondata_with_new_column.xlsx",index=False)

#data filtering multiple condition
#normal python and, or but in pandas &,|
n=all_pokemon_data.loc[(all_pokemon_data['Type 1']=='Grass') &(all_pokemon_data['Type 2']=='Poison')&(all_pokemon_data['HP']>60)]
n.to_csv('pandas_type1Grass_type2Poison_HPmorethan60.csv')
n.to_excel("pandas_type1Grass_type2Poison_HPmorethan60.xlsx",index=False)

z=all_pokemon_data.loc[(all_pokemon_data['Type 1']=='Grass') |(all_pokemon_data['Type 2']=='Poison')]
z.to_csv('pandas_type1Grass_or_type2Poison.csv')
z.to_excel("pandas_type1Grass_or_type2Poison.xlsx",index=False)

#index reset on data filter n and z(see above z and n)
n=n.reset_index(drop=True)
z=z.reset_index(drop=True)
n.to_csv('pandas_resetindex_type1Grass_type2Poison_HPmorethan60.csv')
z.to_csv('pandas_resetindex_type1Grass_or_type2Poison.csv')

#textual filtering with regexp
import  re
n=all_pokemon_data.loc[all_pokemon_data['Name'].str.contains('Mega')]
n.to_csv('pandas_Mega_pokemon_data.csv')
n.to_excel("pandas_Mega_pokemon_data.xlsx",index=False)

n=all_pokemon_data.loc[all_pokemon_data['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)]
#flage=re.I ignore case
n.to_csv('pandas_pokemonthat_startwith_pi.csv')
n.to_excel("pandas_pokemonthat_startwith_pi.xlsx",index=False)

#if and else in pandas
m=all_pokemon_data
m.loc[m['Type 1']=='Fire','Type 1']='Flamer'
m.to_csv('panda_change_fire_toFlame.csv')
m.to_excel('panda_change_fire_toFlame.xlsx',index=False)

m=all_pokemon_data
m.loc[m['Total']>500,['Generation', 'Legendary']]=['test1','test2']
m.to_csv('panda_change_gen_leg_if_total_greater500.csv')
m.to_excel('panda_change_gen_leg_if_total_greater500.xlsx',index=False)

#statistic by group
x= all_pokemon_data.groupby(['Type 1']).mean()#mean values of all columns for each diferent kind of type1
x.to_csv('pandas_meanvalues_of_each_diferent_type1.csv')
x.to_excel('pandas_meanvaluess_of_each_diferent_type1.xlsx',index=True) #index true beacuse group is index

m=all_pokemon_data
m['count']=1 # i did this so that i dont add column count on all_pokemon_data
x= m.groupby(['Type 1']).count()['count']#count values of all columns for each diferent kind of type1
x.to_csv('pandas_number_of_each_diferent_type1.csv')
x.to_excel('pandas_number_of_each_diferent_type1.xlsx',index=True) #index true beacuse group is index

x= m.groupby(['Type 1','Type 2']).count()['count']#count values of all columns for each diferent kind of type1
x.to_csv('pandas_number_of_each_diferent_type1_related_to_type2.csv')
x.to_excel('pandas_number_of_each_diferent_type1related_to_type2.xlsx',index=True) #index true beacuse group is index






