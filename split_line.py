import arcpy
import arcpy
from arcpy import env
import os





#ofile=unicode(""+os.path.splitext(fc)[0]+".tif")

#k=''
#for root, dirs, files in os.walk("F:\data\Joao_BH\resultados\arboreas\exp_1neg\Line_MSP_arboreas_exp_1neg_S_00001_T_00020"):
                #for file in files:
                                #if file.endswith(k):
                                                #print os.path.join(root, file)
                                                #lista_arquivos.append(os.path.join(root, file))



env.workspace = r"F:\data\Joao_BH\resultados\arboreas\exp_1neg\Line_MSP_arboreas_exp_1neg_S_00001_T_00020"
arcpy.env.extent = "607661.39391228 7787724.43347498 616341.39391228 7798114.43347498"

List_lines=arcpy.ListFeatureClasses ()
teste=List_lines[1]
arcpy.SplitLineAtPoint_management(in_features=None, point_features=None, 
                                 out_feature_class=None, 
                                 search_radius=None)
