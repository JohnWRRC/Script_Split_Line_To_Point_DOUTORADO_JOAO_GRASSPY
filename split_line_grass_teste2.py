import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
from datetime import tzinfo, timedelta, datetime
import win32gui
from win32com.shell import shell, shellcon
import wx
import Tkinter
import tkMessageBox

        
def selecdirectori():
        mydocs_pidl = shell.SHGetFolderLocation (0, shellcon.CSIDL_DESKTOP, 0, 0)
        pidl, display_name, image_list = shell.SHBrowseForFolder (
                win32gui.GetDesktopWindow (),
                mydocs_pidl,
                "Select a file or folder",
                shellcon.BIF_BROWSEINCLUDEFILES,
                None,
                None
        )
   
        if (pidl, display_name, image_list) == (None, None, None):
                print "Nothing selected"
        else:
                path = shell.SHGetPathFromIDList (pidl)
                #print "Opening", #path
                a=(path)
      
                return a
   



dir1=selecdirectori()
dirsRaiz1=os.listdir(dir1)#primeira raizprint dirs
os.chdir(dir1)

#sempre iniciar o indice
list_rast_resist=grass.mlist_grouped ('rast', pattern='*resist*') ['PERMANENT']
for i in range(len(dirsRaiz1)):
    os.chdir(dir1+'\\'+dirsRaiz1[i])
    dirsRaiz2=os.listdir(dir1+'\\'+dirsRaiz1[i])
    o=0
    for o in range(len(dirsRaiz2)):
        os.chdir(dir1+"\\"+dirsRaiz1[i]+'\\'+dirsRaiz2[o])
        dirsRaiz3=os.listdir(dir1+"\\"+dirsRaiz1[i]+'\\'+dirsRaiz2[o])
        cont=0
        for p in dirsRaiz3:
            #print p
            
            
            if p.endswith('.txt'):
                continue
            else:
                temp=p
                #print p
                os.chdir(dir1+"\\"+dirsRaiz1[i]+'\\'+dirsRaiz2[o]+'\\'+temp)
                os.mkdir('Split_'+dirsRaiz3[cont])
               
                lista_arquivos=[]
                for root, dirs, files in os.walk(dir1+"\\"+dirsRaiz1[i]+'\\'+dirsRaiz2[o]+'\\'+temp):
                    for file in files:
                        #print file
                        if file.endswith('.shp'):
                            #print os.path.join(root, file)
                            #print file
                            lista_arquivos.append(file)
                
                for q in lista_arquivos:
                    os.chdir(dir1+"\\"+dirsRaiz1[i]+'\\'+dirsRaiz2[o]+'\\'+temp)
                    outvect=q.replace('.shp','_shp')
                    grass.run_command('v.in.ogr',dsn=q,out=outvect,overwrite=True,verbose=False)
                    grass.run_command('v.to.points',input=outvect,out=outvect+'_SpltPnt',overwrite=True)
                    for g in list_rast_resist:
                        if g in outvect+'_SpltPnt':
                            grass.run_command('g.region',rast=g)
                            grass.run_command('v.to.rast',input=outvect+'_SpltPnt',out=outvect+'_SplPntRast',use="cat",overwrite=True)
                            expressao=outvect+'_SplPntRastVl='+outvect+'_SplPntRast*'+g
                            grass.mapcalc(expressao, overwrite = True, quiet = True)
                            print "---------------Mapas em multiplicacao-------------------------"
                            print "--------------------------------------------------------------"
                            print "---------", expressao,"---------------------------------------"
                            print "--------------------------------------------------------------"
                            print "--------------------------------------------------------------"
                            print "--------------------------------------------------------------"
                            grass.run_command('r.to.vect',input=outvect+'_SplPntRastVl',out=outvect+'_SplPntRastVlVct',feature='point',overwrite=True)
                            os.chdir(dir1+"\\"+dirsRaiz1[i]+'\\'+dirsRaiz2[o]+'\\'+temp+'\\Split_'+dirsRaiz3[cont])
                            grass.run_command('v.out.ogr',input=outvect+'_SplPntRastVlVct',dsn=outvect+'_SplPntRastVlVct.shp',type='point')
                            grass.run_command('g.remove',flags='f',vect=outvect+'_SplPntRastVlVct,'+outvect+','+outvect+'_SpltPnt')
                            grass.run_command('g.remove',flags='f',rast=outvect+'_SplPntRast')
                        else:
                            continue
                    
                
                
                
                    
                    
                
                
            cont=cont+1        
                    

        

    
        
     
                
    