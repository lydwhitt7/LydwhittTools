def Harker_Plot1(All, Volc, colour):
    
    #Titanium plot
    plt.subplot(2, 3, 1)
    plt.scatter(All['MgO'], All['TiO2'], marker='.', color='lightgray', s=100)
    plt.scatter(Volc['MgO'], Volc['TiO2'], marker='o', color= colour, s=200, edgecolors= "black")
    plt.xlabel('MgO')
    plt.ylabel('TiO2')
    #Aluminium plot
    plt.subplot(2, 3, 2)
    plt.scatter(All['MgO'], All['Al2O3'], marker='.', color='lightgray')
    plt.scatter(Volc['MgO'], Volc['Al2O3'], marker='o', color= colour, s=200, edgecolors= "black")
    plt.xlabel('MgO')
    plt.ylabel('Al2O3')
    #Chromium plot
    plt.subplot(2, 3, 3)
    plt.scatter(All['MgO'], All['K2O'], marker='.', color='lightgray')
    plt.scatter(Volc['MgO'], Volc['K2O'], marker='o', color= colour, s=200, edgecolors= "black") 
    plt.xlabel('MgO') 
    plt.ylabel('K2O')
    #Iron plot
    plt.subplot(2, 3, 4)
    plt.scatter(All['MgO'], All['FeOT'], marker='.', color='lightgray') 
    plt.scatter(Volc['MgO'], Volc['FeOT'], marker='o', color= colour, s=200, edgecolors= "black") 
    plt.xlabel('MgO')
    plt.ylabel('FeOT')
    #Calcium plot
    plt.subplot(2, 3, 5)
    plt.scatter(All['MgO'], All['CaO'] , marker='.', color='lightgray')
    plt.scatter(Volc['MgO'], Volc['CaO'], marker='o', color= colour, s=200, edgecolors= "black") 
    plt.xlabel('MgO')
    plt.ylabel('CaO')
    #Sodium plot
    plt.subplot(2, 3, 6)
    plt.scatter(All['MgO'], All['Na2O'], marker='.', color='lightgray') 
    plt.scatter(Volc['MgO'], Volc['Na2O'], marker='o', color= colour, s=200, edgecolors= "black") 
    plt.xlabel('MgO')
    plt.ylabel('Na2O')

    plt.subplots_adjust(bottom=2, right=5, top=4, left=2)
    plt.rcParams.update({'font.size': 20})
    
def Harker_Plot2(All, Volc1, colour1, Volc2, colour2):
    
    #Titanium plot
    plt.subplot(2, 3, 1)
    plt.scatter(All['MgO'], All['TiO2'], marker='.', color='lightgray', s=100)
    plt.scatter(Volc1['MgO'], Volc1['TiO2'], marker='o', color= colour1, s=200, edgecolors= "black")
    plt.scatter(Volc2['MgO'], Volc2['TiO2'], marker='o', color= colour2, s=200, edgecolors= "black")
    plt.xlabel('MgO')
    plt.ylabel('TiO2')
    #Aluminium plot
    plt.subplot(2, 3, 2)
    plt.scatter(All['MgO'], All['Al2O3'], marker='.', color='lightgray')
    plt.scatter(Volc1['MgO'], Volc1['Al2O3'], marker='o', color= colour1, s=200, edgecolors= "black")
    plt.scatter(Volc2['MgO'], Volc2['Al2O3'], marker='o', color= colour2, s=200, edgecolors= "black")
    plt.xlabel('MgO')
    plt.ylabel('Al2O3')
    #Chromium plot
    plt.subplot(2, 3, 3)
    plt.scatter(All['MgO'], All['K2O'], marker='.', color='lightgray')
    plt.scatter(Volc1['MgO'], Volc1['K2O'], marker='o', color= colour1, s=200, edgecolors= "black") 
    plt.scatter(Volc2['MgO'], Volc2['K2O'], marker='o', color= colour2, s=200, edgecolors= "black") 
    plt.xlabel('MgO') 
    plt.ylabel('K2O')
    #Iron plot
    plt.subplot(2, 3, 4)
    plt.scatter(All['MgO'], All['FeOT'], marker='.', color='lightgray') 
    plt.scatter(Volc1['MgO'], Volc1['FeOT'], marker='o', color= colour1, s=200, edgecolors= "black") 
    plt.scatter(Volc2['MgO'], Volc2['FeOT'], marker='o', color= colour2, s=200, edgecolors= "black") 
    plt.xlabel('MgO')
    plt.ylabel('FeOT')
    #Calcium plot
    plt.subplot(2, 3, 5)
    plt.scatter(All['MgO'], All['CaO'] , marker='.', color='lightgray')
    plt.scatter(Volc1['MgO'], Volc1['CaO'], marker='o', color= colour1, s=200, edgecolors= "black") 
    plt.scatter(Volc2['MgO'], Volc2['CaO'], marker='o', color= colour2, s=200, edgecolors= "black")
    plt.xlabel('MgO')
    plt.ylabel('CaO')
    #Sodium plot
    plt.subplot(2, 3, 6)
    plt.scatter(All['MgO'], All['Na2O'], marker='.', color='lightgray') 
    plt.scatter(Volc1['MgO'], Volc1['Na2O'], marker='o', color= colour1, s=200, edgecolors= "black") 
    plt.scatter(Volc2['MgO'], Volc2['Na2O'], marker='o', color= colour2, s=200, edgecolors= "black") 
    plt.xlabel('MgO')
    plt.ylabel('Na2O')

    plt.subplots_adjust(bottom=2, right=5, top=4, left=2)
    plt.rcParams.update({'font.size': 20})