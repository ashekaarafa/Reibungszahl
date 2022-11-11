# Calculation of Friction factor (f):
## About:
This script will allow to calculate **friction factor (f)** and absolute roughness over  
the pipe diameter **(k/D)** from a **.csv** file.  

## Required pakage:
*Pandas* 
## Used Fomulas:
Pressure loss due to incompressible fluid flow formula is used here to  
calculate the friction factor *f*.  [Hakanesh,2014] 

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;
&ensp;&rho;.&ensp;V^2.&ensp;L  
&Delta;P = f&ensp;&ensp;&mdash;&mdash;&mdash;&mdash;&mdash;&mdash; &ensp; &ensp; &ensp; ( eq I )  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;2.&ensp; D
&ensp;&nbsp;   


where,  
&Delta;P = Pressure difference  
f = Friction  
&rho; = Density    
V = Velocity  
L = length  
D = Diameter.

The change of density and velocity of incompressible gas due to heat transfer  
during flox-betrieb can be expressed through state equation of ideal gas:

&ensp; &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;T1&ensp;&ensp;P2 
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; &ensp; &ensp;T2 &ensp; &ensp; P1  
&rho; = &rho;1 &ensp; &mdash;&mdash;&ensp;&mdash;&mdash; &ensp; ; 
&ensp;&ensp;&ensp; V = V1 &ensp; &mdash;&mdash;&ensp;&mdash;&mdash; &ensp; ;  
&ensp; &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;T2&ensp;&ensp;P1&ensp;
&ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp; &ensp;T1 &ensp; &ensp; P2  

Neglecting the effect of pressure on density as well as velocity of incompressible fluid 
Equation (I) Becomes:  

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&Delta;P 2&ensp;D &ensp;&ensp; &ensp; T1  
f = &ensp;&ensp;&mdash;&mdash;&mdash;&mdash;&mdash;&ensp; &mdash;&mdash; &ensp; &ensp; &ensp; ( eq II )  
&ensp;&ensp; &ensp; &ensp;&ensp;&rho;1 V1^2&ensp;L&ensp;&ensp;T2 
&ensp;&nbsp;   



Colebrook equation is used to calculate k/D: [Hakanesh,2014]  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; &ensp;&ensp;
&ensp;&ensp;&ensp;k &ensp;&ensp;&ensp;&ensp;&ensp;2.51  
f = - 2 * log ( &mdash;&mdash;&mdash; + &mdash;&mdash;&mdash; )
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;  
&ensp; &ensp; &ensp; &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;3.71 D&ensp;&ensp;Re &radic;f  

## Guidelines:

The **.csv file** should contain the following column names: 
1. *Druckverlust_mbar*  
2. *Volumendurchfluss_Nm3/h*  
3. *T1_C*  
4. *T2_C*  


Here is an example of `.csv` file:
```
"Methan, Floxbetrieb",,,,,
Pipe dia,16.5 mm,,,,
,,,,,
,,,,,
,,,,,
P1_mbar,P2_mbar,Volumendurchfluss_Nm3/h,Druckverlust_mbar,T1_C,T2_C
13.2,-0.1,25,13.3,25,707
12.3,-0.2,24,12.5,25,729
11.2,-0.1,23,11.3,25,743
10.2,-0.3,22,10.5,25,757
9.5,-0.2,21,9.7,25,801
8.7,-0.1,20,8.8,25,806
7.8,-0.1,19,7.9,25,808
7.2,-0.2,18,7.4,25,805
6.5,-0.2,17,6.7,25,799
5.7,-0.2,16,5.9,25,794
5.2,-0.2,15,5.4,25,783
4.5,-0.3,14,4.8,25,743
3.9,-0.3,13,4.2,25,737
3.4,-0.3,12,3.7,25,725
2.9,-0.4,11,3.3,25,715
2.5,-0.4,10,2.9,25,694
2.1,-0.5,9,2.6,25,686
1.6,-0.5,8,2.1,25,665

```
The **.csv** file can have other columns, it should not create an error message.The 
**header** should be specified like this:

    df = pd.read_csv("put the .csv file directory here", sep=",",
        header=[5], skip_blank_lines=True)`

The pipe **diameter**, **length** should be entered in **mm**.
**Density** and **kinematic viscosity** of the gas should be entered at temperature T1 
with the  units **kg/m3**, **m2 /s** respectively. Such as:

    dia_in_mm = 16.5
    length_mm = 1115
    density_20c_kg_m3 = 0.657
    kn_viscosity = 17.07 * 10 ** -6

If there is no error message, the output should look like this:
```
Drucklust_mbar  Durchfluss_Nm3/h  ...  Reynoldszahl     kd
0             13.3              25.0  ...         31393  0.013
1             12.5              24.0  ...         30137  0.014
2             11.3              23.0  ...         28881  0.013
3             10.5              22.0  ...         27626  0.014
4              9.7              21.0  ...         26370  0.014
5              8.8              20.0  ...         25114  0.014
6              7.9              19.0  ...         23859  0.014
7              7.4              18.0  ...         22603  0.016
8              6.7              17.0  ...         21348  0.016
9              5.9              16.0  ...         20091  0.016
10             5.4              15.0  ...         18835  0.018
11             4.8              14.0  ...         17580  0.019
12             4.2              13.0  ...         16324  0.019
13             3.7              12.0  ...         15068  0.021
14             3.3              11.0  ...         13813  0.025
15             2.9              10.0  ...         12557  0.029
16             2.6               9.0  ...         11302  0.037
17             2.1               8.0  ...         10046  0.039

```
If everything works so far. Uncomment the following section to write it in .xlsx file.  
write down the file directory where it should be saved. If it is  required,  
change the file and sheet name. 
    
    writer = pd.ExcelWriter('Write your file directory here/reibungszahl.xlsx')
    # write dataframe to excel
    pvf.to_excel(writer, sheet_name="Inkom", startrow=5)
    writer.save()

In each run existing file with similar name will be replaced.


 

