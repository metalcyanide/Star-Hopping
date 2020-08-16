import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Circle
from svgpath2mpl import parse_path


def telescope(fov,a):
    
    fig =plt.figure(figsize=(10,10))
    ax1=fig.add_subplot(111)
   
    
    # to prevent error occuring while zooming in at the poles 2 conditions r used
    if (dec_in+fov<80 and dec_in-fov>-80):
         m = Basemap(projection = "stere",
            llcrnrlon=ra_in-fov,llcrnrlat=dec_in-fov,
            urcrnrlon=ra_in+fov,urcrnrlat=dec_in+fov,
            resolution = "i",lat_0=dec_in,lon_0=ra_in,
            celestial=True,fix_aspect=False)
         
         m.drawparallels(range(-90,90,1),color='white',labels=[1,1,0,0],dashes=[1,1],latmax=90)
         m.drawmeridians(range(0,360,1),color='white',labels=[0,0,1,1],dashes=[1,1],latmax=90)
         if a==1:
             plt.title('Field of view through eyepiece',pad=30,size=20)
         else:
             plt.title('Field of view through finder scope',pad=30,size=20)
        
         ra_crc=360-ra_in if ra_in>180 else -ra_in 
         dec_crc=dec_in
         x_crc,y_crc=m(ra_crc,dec_crc,inverse=False)
         s1=m(ra_crc,dec_crc)
         s2=m(ra_crc+1,dec_crc)
         r=(s1[0]-s2[0])*(fov/2)
        
         circle = Circle((x_crc, y_crc), r,color='r',fill=False,ls='--',lw=2)
         ax1.add_patch(circle)
    
   
    else:
        
        m = Basemap(width=8000000,height=8000000,projection = "stere",
            lat_0=dec_in,lon_0=ra_in,resolution = "i",celestial=True)
        
        m.drawparallels(range(-90,90,3),color='white',labels=[1,1,0,0],dashes=[1,1],latmax=90)
        m.drawmeridians(range(0,360,10),color='white',labels=[0,0,0,1],dashes=[1,1],latmax=90)
        plt.title('Projection of sky at Pole',pad=30,size=20)
    
    m.drawmapboundary(color='white',linewidth=1.5,fill_color='k')
    
    star_size=500
    x,y=m(RA_2,DEC_2)
    stars=m.scatter(x,y,color='white',s=star_size/2.5**V_2)
    
    lw = 0
    plw = 1 
    
    x_m,y_m=m(np.array(oc_ms['RAJ2000']),np.array( oc_ms['DEJ2000']))
    ocms = m.scatter(x_m,y_m, color='yellow', marker="o", s=150,
                 linewidth = lw,label='clusters')
    
    x_m,y_m=m(np.array(gc_ms['RAJ2000']),np.array( gc_ms['DEJ2000']))
    gcms = m.scatter(x_m,y_m, color='black', marker="+", s=150,
               zorder=2, linewidth=plw)
   
    x_m,y_m=m(np.array(gc_ms['RAJ2000']),np.array( gc_ms['DEJ2000']))
    gcms1 = m.scatter(x_m,y_m, color='yellow', marker="o", s=150,
               edgecolor="grey",  linewidth=lw)
   
    x_m,y_m=m(np.array(ga_ms['RAJ2000']),np.array(ga_ms['DEJ2000']))    
    gams = m.scatter(x_m,y_m, color='red', marker=ell, s=150,
                linewidth = lw)
    
    x_m,y_m=m(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms = m.scatter(x_m,y_m, color='green', marker="o", s=150,
                zorder=2,linewidth = lw)
    
    x_m,y_m=m(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms1 = m.scatter(x_m,y_m, color='white', marker="+",
               s=400, linewidth=plw)
    
    x_m,y_m=m(np.array(ot_ms['RAJ2000']),np.array( ot_ms['DEJ2000']))
    otms = m.scatter(x_m,y_m, c='yellow', marker="^",
               s=150,linewidth=plw)
    
    xcb,ycb=m(ra_cb,dec_cb)
    m.scatter(xcb,ycb,s=20,color='g',marker='_')
    plt.legend([ocms,(gcms1, gcms),(nbms, nbms1),gams, otms,stars ],
               [" Open Cluster", "Globular Cluster", "Nebula",'Galaxy', 
                "Other Messier", "Tycho-1 Stars"],labelspacing=5, ncol=6, 
               borderpad=.5, loc=8,facecolor='grey')
    plt.show()



def hop_sequence_plot(lon,lat):
    
    fig2=plt.figure(figsize=(60,60))
    #RA values of hops are converted to the celestial coordinates 
    lon=[(360-i) if i>180 else (-i) for i in lon]
    ax2=fig2.add_subplot(1,1,1)
    
    
    n = Basemap(width=7000000,height=7000000,projection = "stere",
            lat_0=dec_in,lon_0=ra_in,resolution = "i",celestial=True
            ,fix_aspect=False)
    
    plt.title('Hops',pad=30,size=20)
    n.drawmapboundary(color='grey',linewidth=1.,fill_color='k')
    
    star_size=200
    x,y=n(RA,DEC)
    stars=n.scatter(x,y,color='white',s=star_size/2.5**V_1)
    
   
    lw = 0
    plw = 1 
    
    x_m,y_m=n(np.array(oc_ms['RAJ2000']),np.array( oc_ms['DEJ2000']))
    ocms = n.scatter(x_m,y_m, color='yellow', marker="o", s=150,
                 linewidth = lw,label='clusters')
    
    x_m,y_m=n(np.array(gc_ms['RAJ2000']),np.array( gc_ms['DEJ2000']))
    gcms = n.scatter(x_m,y_m, color='black', marker="+", s=150,
               zorder=2, linewidth=plw)
   
    x_m,y_m=n(np.array(gc_ms['RAJ2000']),np.array( gc_ms['DEJ2000']))
    gcms1 = n.scatter(x_m,y_m, color='yellow', marker="o", s=150,
               edgecolor="grey",  linewidth=lw)
   
    x_m,y_m=n(np.array(ga_ms['RAJ2000']),np.array(ga_ms['DEJ2000']))    
    gams = n.scatter(x_m,y_m, color='red', marker=ell, s=150,
                linewidth = lw)
    
    x_m,y_m=n(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms = n.scatter(x_m,y_m, color='green', marker="o", s=150,
                zorder=2,linewidth = lw)
    
    x_m,y_m=n(np.array(nb_ms['RAJ2000']), np.array(nb_ms['DEJ2000']))
    nbms1 = n.scatter(x_m,y_m, color='white', marker="+",
               s=400, linewidth=plw)
    
    x_m,y_m=n(np.array(ot_ms['RAJ2000']),np.array( ot_ms['DEJ2000']))
    otms = n.scatter(x_m,y_m, c='yellow', marker="^",
               s=150,linewidth=plw)
    
 
    xcb,ycb=n(ra_cb,dec_cb)
    n.scatter(xcb,ycb,s=10,color='g')
    
    n.drawparallels(range(-90,90,10),color='white',labels=[1,1,0,0],latmax=90)
    n.drawmeridians(range(0,360,10),color='white',labels=[0,0,1,1],latmax=90)
    
    #adding star hops 
    for i in range(1,len(lon)):
        n.drawgreatcircle(lon[i-1],lat[i-1],lon[i],lat[i],
                          color='white',linewidth=1.9)
    lon,lat=n(lon,lat)
    n.scatter(lon,lat,color='dimgrey',s=100,marker='o')
 
     
   
    #adding prominenet star names. 
    name_lim=300
    Ra,Dec=n(RA,DEC)
    for i in range(name_lim):
        if name[i]!='-':
            ax2.text(Ra[i],Dec[i]+100000,name[i],fontsize=10,
                     fontweight='bold',color='deeppink').set_clip_on(True)
           
        else:
            ax2.text(Ra[i],Dec[i]+100000,name_bayer[i],fontsize=10,
                     fontweight='bold',color='deeppink').set_clip_on(True)
    
    #adding messier main id
    Ra,Dec=n(ra_m,dec_m)
    for i in range(len(ra_m)):
        ax2.text(Ra[i]+20000,Dec[i]-200000,name_m[i],fontsize=10,
                    fontweight='bold',color='yellow').set_clip_on(True)
       
    
    #adding constellation names with location manually found
    #that best suits the figure
    
    const_name=np.array(pd.unique(data_cb['Constellation']))
    #const_name=np.sort(const_name)
    ra_const=[-20,18,-45,-60,-38,-20,10,-140,-160,160,160,100,60,95,95,128,
              155,60,20,-10,20,35,85,98,95,65,44,60,76,112,100,60,-45,
              -80,-100,-110,-130,-110,138,150,160,155,180,114,-74,-90,-88,
              -95,10,115,100,-165,-122,-135,-110,-125,-112,38,-150,-120,170,
              123,45,-30,-65,-45,-125,72,167,-175,72,41,-69,-110,39,-80,-90,
              -61,-50,-20,20,33,-10,-160,125,-20,-165,-140]
    dec_const=[43,45,65,45,32,15,20,0,-35,-40,-80,-75,-65,-50,-65,-58,
               -70,0,-10,-30,-30,-20,-11,-8,22,18,18,-35,-14,-52,-40,-50,20,
               25,40,70,40,20,25,-5,25,35,40,30,-40,-65,-50,-40,70,70,60,
               20,3,25,-20,-28,-5,-40,-50,-60,-60,-32,50,-10,-20,-30,-70,-40,
               -20,-20,40,25,-65,-80,5,10,-20,-50,-75,-50,-42,-58,-65,0,-20,
               -89,30,-30]
    ra_const,dec_const=n(ra_const,dec_const)
    
    for i in range(len(ra_const)):
        
        ax2.text(ra_const[i],dec_const[i],'  '.join(const_name[i]),
                 fontsize=20,fontweight='bold',alpha=0.3
                 ,color='white').set_clip_on(True)
        
    plt.gca().invert_xaxis()
    plt.legend([ocms,(gcms1, gcms),(nbms, nbms1),gams, otms,stars ],
               [" Open Cluster", "Globular Cluster", "Nebula",'Galaxy', 
                "Other Messier", "Tycho-1 Stars"],labelspacing=5, ncol=6, 
               borderpad=.5, loc=8,facecolor='grey')
    plt.show()
'''
ra_in=float(input('enter RA of object in degrees  (0 and 360 '))

dec_in=float(input('enter DEC f object in degrees (-90 and +90 '))
#a_fov=float(input('enter the apparent field of view of eyepiece in degrees'))
#f_eyep=float(input('enter the focal length of eye piece'))
#f_obj=float(input('enter the focal length of  objective'))
#D=float(input('enter diameter of telescope in mm'))

#fov=float(a_fov/(f_obj/f_eyep)) #true field of view
#m_lim=2+5*np.log10(D)
#app_fov_finder_scope=float(input('enter apparent field of view of finder scope'))
#mag_fov_finder_scope=float(input('enter magnification of finder scope'))
#fov_finder_scope=float(app_fov_finder_scope/mag_fov_finder_scope)
fov=float(input('enter true fov in degrees'))
fov_finder_scope=float(input('enter fov of finder scope'))
m_lim=float(input('enter lim mag'))'''
ra_in,dec_in,fov,fov_finder_scope,m_lim=[265,-32.2,2,3,10]

#visual magnitude limit
v_mag=6

#constellation borders
data_cb=pd.read_csv('constellation_borders.csv',encoding='latin1')
dec_cb=np.array(data_cb['DEJ2000'])
ra_cb=np.array(data_cb['RAJ2000'])
#converting the ra to celestial coordinate conventions.
ra_cb=[(360-i) if i>=180 else (-i) for i in ra_cb]

#messier objects
data_m=pd.read_csv("messier_objects.csv",encoding='latin1')
data_m['RAJ2000']=[(360-i) if i >=180 else (-i) for i in data_m['RAJ2000']]

#globular clusters
gc_ms = data_m[(data_m["TYPE"] == 'GlC')]

#open clusters
oc_ms = data_m[(data_m["TYPE"] == 'OpC') | (data_m["TYPE"] == 'Cl*')]

#galaxies
ga_ms = data_m[(data_m["TYPE"] == 'G') | (data_m["TYPE"] == 'Sy2') |
        (data_m["TYPE"] == 'IG') | (data_m["TYPE"] == 'GiG') | (
        data_m["TYPE"] == 'GiP') | (data_m["TYPE"] == 'SyG') |
        (data_m["TYPE"] == 'SBG') | (data_m["TYPE"] == 'BiC') | (
        data_m["TYPE"] == 'H2G')]

#nebula and supernova remnant
nb_ms = data_m[(data_m["TYPE"] == 'PN') | (data_m["TYPE"] == 'RNe') | 
               (data_m["TYPE"] == 'HII') | (data_m["TYPE"] == 'SNR')]            

#other messiers
ot_ms = data_m[(data_m["TYPE"] == 'As*') | (data_m["TYPE"] == 'LIN') | 
        (data_m["TYPE"] == 'mul') | (data_m["TYPE"] == 'AGN')]


ra_m =np.array( data_m['RAJ2000'])
dec_m =np.array (data_m['DEJ2000'])
name_m=np.array(data_m['ID (for resolver)'])

#star data
file=pd.read_csv('tycho-1.csv',low_memory=False)

#stars below visual magnitude of 6, to be used for hop sequence
loc=max(fov,fov_finder_scope)
data_1=file[(file['V']<=v_mag) ]
#converting to celestial coordinates
data_1['RAJ2000']=[(360-i) if i>=180 else (-i) for i in data_1['RAJ2000']]
RA=np.array(data_1['RAJ2000'])
DEC=np.array(data_1['DEJ2000'])
name=np.array(data_1['Name'])
V_1=np.array(data_1['V'])
name_bayer=np.array(data_1['Bayer'])

#stars below the limting magnitude of telescope, used for telescope plot
data_2=file[(file['V']<=m_lim) & (file['RAJ2000']<=ra_in+loc) &
            (file['RAJ2000']>=ra_in-loc) & (file['DEJ2000']<=dec_in+loc)
            & (file['DEJ2000']>=dec_in-loc)]

#converting to celestial coordinates
data_2['RAJ2000']=[(360-i) if i>=180 else (-i) for i in data_2['RAJ2000']]
RA_2=np.array(data_2['RAJ2000'])
DEC_2=np.array(data_2['DEJ2000'])
V_2=np.array(data_2['V'])

ell = parse_path("""M 490.60742,303.18917 A 276.31408,119.52378 28.9 0 1 190.94051,274.29027 276.31408,119.52378 28.9 0 1 6.8010582,36.113705 276.31408,119.52378 28.9 0 1 306.46799,65.012613 276.31408,119.52378 28.9 0 1 490.60742,303.18917 Z""")
ell.vertices -= ell.vertices.mean(axis=0)


telescope(fov,1)
telescope(fov_finder_scope,2)

Lon=[247.3519107541,252.54268738,263.4021631364,265]
Lat=[-26.432003770300003,-34.29260982,-37.1038285483,-32.2]
#pass the longitude and latitude array of the hops created
hop_sequence_plot(Lon,Lat)


