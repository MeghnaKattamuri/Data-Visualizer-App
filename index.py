import tkinter as tk
from tkinter.filedialog import askopenfilename
from matplotlib import *
import tkinter
from tkinter import *
from matplotlib import pyplot as plt
from tkinter import ttk
import numpy as np
import pymysql

count=0
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page2(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        val=[]
        a=[]
        count=0
        global button
        def openF():
           def selchart():
              global count
              count=count+1
              if count==2:
                 s="You can't change the chart type! Restart the application"
                 L3.config(text=s,fg="red")
              if count<2 and c.get()!="":
                 s="You selected "+c.get()+" chart"
                 L3.config(text=s)
                 def create():
                    n=int(var4.get())
                    s=var3.get()
                    if(len(a)<=n):
                       a.append(s)
                       if len(a)==1 and len(a)<n:
                          button.destroy()
                          button2 = Button(self,text="Add y column", command=create)
                          button2.place(x=10,y=400)
                       if(len(a)==n):
                          button.destroy()
                          button3 = Button(self,text="         Draw        ", command=create)
                          button3.place(x=10,y=400)
                       if n==1 and len(a)==2:
                          temp=str(a[0])
                          for xindex in range(0,len(val)):
                             temp3=str(tuple(val[xindex],))
                             if temp==temp3:
                                break
                          xaxis=first_sheet.col_values(xindex,1)
                          if c.get()=="Histogram":
                                num_bins = 5
                                nu, bins, patches = plt.hist(xaxis, num_bins, facecolor='blue', alpha=0.5)
                                plt.show()
                          else:
                                L11.config(text="Except histogram, all charts need minimum of two columns!",fg="red")
                       
                       if n==2 and len(a)==3:
                          temp=str(a[0])
                          temp1=str(a[1])
                          for xindex in range(0,len(val)):
                             temp3=str(tuple(val[xindex],))
                             if temp==temp3:
                                break
                          for yindex in range(0,len(val)):
                             temp4=str(tuple(val[yindex],))
                             if temp1==temp4:
                                break
                          xaxis=first_sheet.col_values(xindex,1)
                          yaxis=first_sheet.col_values(yindex,1)
                          if(c.get()=="line"):
                             plt.plot(xaxis,yaxis)
                             plt.xlabel(str(a[0]))
                             plt.ylabel(str(a[1]))
                             plt.title("Python line chart")
                             plt.grid(True)
                             plt.show()
                          elif c.get()=="bar":
                             plt.bar(xaxis, yaxis, align='center')
                             plt.xticks(xaxis, yaxis)
                             plt.ylabel(str(a[1]))
                             plt.title('Python bar chart')
                             plt.show()
                          elif c.get()=="Scatter":
                                import numpy as np
                                colors = (0,0,0)
                                area = np.pi*3
                                plt.scatter(xaxis, yaxis, s=area, c=colors, alpha=0.5)
                                plt.title('Scatter plot')
                                plt.xlabel(str(a[0]))
                                plt.ylabel(str(a[1]))
                                plt.show()
                          elif c.get()=="HeatMap":
                                import numpy as np
                                try:
                                    heatmap, xedges, yedges = np.histogram2d(xaxis, yaxis, bins=(64,64))
                                    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
                                     
                                    # Plot heatmap
                                    plt.clf()
                                    plt.title('Pythonspot.com heatmap example')
                                    plt.ylabel('y')
                                    plt.xlabel('x')
                                    plt.imshow(heatmap, extent=extent)
                                    plt.show()
                                except(ValueError):
                                    L3.config("Numerics only",fg="red")
                       if n==3 and len(a)==4:
                          temp=str(a[0])
                          temp1=str(a[1])
                          temp5=str(a[2])
                          for xindex in range(0,len(val)):
                             temp3=str(tuple(val[xindex],))
                             if temp==temp3:
                                break
                          for yindex1 in range(0,len(val)):
                             temp4=str(tuple(val[yindex1],))
                             if temp1==temp4:
                                break
                          for yindex2 in range(0,len(val)):
                             temp6=str(tuple(val[yindex2]))
                             if temp5==temp6:
                                break
                          xaxis=first_sheet.col_values(xindex,1)
                          yaxis1=first_sheet.col_values(yindex1,1)
                          yaxis2=first_sheet.col_values(yindex2,1)
                          if(c.get()=="line"):
                             plt.plot(xaxis,yaxis1)
                             plt.plot(xaxis,yaxis2)
                             plt.xlabel(str(a[0]))
                             plt.ylabel(str(a[1])+str(a[2]))
                             plt.title("Python line chart")
                             plt.grid(True)
                             plt.show()
                          if c.get()=="bar":
                                import numpy as np
                                fig, ax = plt.subplots()
                                index = np.arange(len(xaxis))
                                bar_width = 0.35
                                opacity = 0.8
                                 
                                rects1 = plt.bar(index, yaxis1, bar_width,
                                                 alpha=opacity,
                                                 color='b',
                                                 label=str(a[1]))
                                 
                                rects2 = plt.bar(index + bar_width, yaxis2, bar_width,
                                                 alpha=opacity,
                                                 color='g',
                                                 label=str(a[2]))
                                 
                                plt.xlabel(str(a[0]))
                                ylabel=str(a[1])+"VS"+str(a[2])
                                plt.ylabel(ylabel)
                                plt.title('Python Double Bar')
                                plt.xticks(index + bar_width, xaxis)
                                plt.legend()
                                plt.tight_layout()
                                plt.show()
                          
                 for i in range(col):
                       choices.append(val[i])
                 L4=Label(self,text="Enter how many columns you are gonna select?")
                 L4.place(x=10,y=250)
                 Rm3=Radiobutton(self,text="1(for histogram only)",variable=var4,value="1")
                 Rm3.place(x=10,y=290)
                 R3=Radiobutton(self,text="2(first one on x-axis and next one on y-axis)",variable=var4,value="2")
                 R3.place(x=200,y=290)
                 R4=Radiobutton(self,text="3(first one x-axis, next two columns on y-axis)",variable=var4,value="3")
                 R4.place(x=10,y=320)
                 option = OptionMenu(self, var3, *choices)
                 option.place(x=10,y=360 )
                 button = Button(self,text="Add x column", command=create)
                 button.pack()
                 button.place(x=10,y=400)
           if var.get()==".xlsx" or var.get()==".csv":
              name = askopenfilename()
           else:
              L3.config(text="You must select a file type!")
           if var.get()==".csv":
              import numpy as np      
           if var.get()==".xlsx":
              import xlrd
              workbook = xlrd.open_workbook(name)
              first_sheet = workbook.sheet_by_index(0)
              for row in range(first_sheet.nrows):
                 for col in range(first_sheet.ncols):
                    val.append([first_sheet.cell_value(row,col)])
              col=col+1
              row=row+1
           L3.config(text="Select the type of chart you want to draw!!")
           c=StringVar()
           values=["bar", "line","Histogram","HeatMap","Scatter"]
           option3=OptionMenu(self,c,*values)
           option3.place(x=10,y=210)
           gb=tk.Button(self,text="sel chart",command=selchart)
           gb.place(x=80,y=210)
        def sel(): 
           selection = "You selected the option " + var.get() 
           label.config(text = selection)
        L1 = Label(self, text="Choose your file type:") 
        L1.place(x=10,y=10)
        label=Label(self)
        label.place(x=150,y=10)
        var = StringVar() 
        R1 = Radiobutton(self, text="CSV File (.csv)", variable=var, value=".csv", 
                          command=sel) 
        R1.pack( anchor = W ) 
        R1.place(x=10,y=50)
        R2 = Radiobutton(self, text="Workbook (.xlsx)", variable=var, value=".xlsx", 
                          command=sel) 
        R2.pack( anchor = W )
        R2.place(x=10,y=90)
        L2=Label(self,text="Enter your file name:") 
        L2.place(x=10,y=110)
        B1=Button(self,text="Open File:",command=openF)
        B1.place(x=150,y=150)
        L3=Label(self)
        L3.place(x=10,y=180)
        var3 = StringVar(self)
        var4=StringVar(self)
        choices = [] 




       

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       l=tk.Label(self,text="WELCOME!",font="comicsansms 15 bold")
       l.place(x=180,y=100)
       label = tk.Label(self,image=imag)
       label.place(x=120,y=130)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       count=0
       var7 = StringVar()
       var8=StringVar()
       li=[]
       def conn():
           def dbsel():
               def tablesel():
                   def chartsel():
                         global count
                         count=count+1
                         if(count<2):
                            def chartcreate():
                                xaxis=[]
                                yaxis=[]
                                yaxis1=[]
                                yaxis2=[]
                                n=var9.get()
                                if(len(li)<=n):
                                   li.append(var8.get())
                                   if len(li)==1 and len(li)<n:
                                      button.destroy()
                                      button2 = tk.Button(self,text="Add y column", command=chartcreate)
                                      button2.place(x=100,y=400)
                                   if(len(li)==n):
                                      button.destroy()
                                      button3 = tk.Button(self,text="         Draw        ", command=chartcreate)
                                      button3.place(x=100,y=400)
                                   if n==1 and len(li)==2:
                                      c.execute("select "+li[0]+" from "+table)
                                      arr=c.fetchall()
                                      for i in range(len(arr)):
                                          xaxis.append(arr[i][0])
                                      if var7.get()=="Histogram":
                                            num_bins = 5
                                            nu, bins, patches = plt.hist(xaxis, num_bins, facecolor='blue', alpha=0.5)
                                            plt.show()
                                      else:
                                          L11.config(text="Except histogram, all charts need minimum of two columns!",fg="red")
                                   if n==2 and len(li)==3:
                                      c.execute("select "+li[0]+","+li[1]+" from "+table)
                                      arr=c.fetchall()
                                      for i in range(len(arr)):
                                          xaxis.append(arr[i][0])
                                          yaxis.append(arr[i][1])
                                      if(var7.get()=="Histogram"):
                                          L11.config(text="Histogram is possible with one column only!",fg="Red")
                                      elif(var7.get()=="line"):
                                         plt.plot(xaxis,yaxis)
                                         plt.xlabel(str(li[0]))
                                         plt.ylabel(str(li[1]))
                                         plt.title("Python line chart")
                                         plt.grid(True)
                                         plt.show()
                                      elif var7.get()=="bar":
                                         plt.bar(xaxis, yaxis, align='center')
                                         plt.xticks(xaxis, yaxis)
                                         plt.ylabel(str(li[1]))
                                         plt.title('Python bar chart')
                                         plt.show()
                                      elif var7.get()=="Scatter":
                                            import numpy as np
                                            colors = (0,0,0)
                                            area = np.pi*3
                                            plt.scatter(xaxis, yaxis, s=area, c=colors, alpha=0.5)
                                            plt.title('Scatter plot')
                                            plt.xlabel(str(li[0]))
                                            plt.ylabel(str(li[1]))
                                            plt.show()
                                      elif var7.get()=="HeatMap":
                                            import numpy as np
                                            try:
                                                heatmap, xedges, yedges = np.histogram2d(xaxis, yaxis, bins=(64,64))
                                                extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
                                                 
                                                # Plot heatmap
                                                plt.clf()
                                                plt.title('Pythonspot.com heatmap example')
                                                plt.ylabel('y')
                                                plt.xlabel('x')
                                                plt.imshow(heatmap, extent=extent)
                                                plt.show()
                                            except(ValueError):
                                                L11.config("Numerics only!",fg="red")
                                   if n==3 and len(li)==4:
                                      c.execute("select "+li[0]+","+li[1]+","+li[2]+" from "+table)
                                      arr=c.fetchall()
                                      for i in range(len(arr)):
                                          xaxis.append(arr[i][0])
                                          yaxis1.append(arr[i][1])
                                          yaxis2.append(arr[i][2])
                                      if(var7.get()=="Histogram"):
                                          L11.config(text="Histogram is possible with one column only!",fg="Red")
                                      elif(var7.get()=="Scatter"):
                                          L11.config(text="ScatterPlot is possible with two columns only!",fg="Red")
                                      elif(var7.get()=="HeatMap"):
                                          L11.config(text="HeatMap is possible with two columns only!",fg="Red")
                                      elif(var7.get()=="line"):
                                         plt.plot(xaxis,yaxis1)
                                         plt.plot(xaxis,yaxis2)
                                         plt.xlabel(str(li[0]))
                                         plt.ylabel(str(li[1])+" and "+str(li[2]))
                                         plt.title("Python line chart")
                                         plt.grid(True)
                                         plt.show()
                                      elif var7.get()=="bar":
                                            import numpy as np
                                            fig, ax = plt.subplots()
                                            index = np.arange(len(xaxis))
                                            bar_width = 0.35
                                            opacity = 0.8
                                             
                                            rects1 = plt.bar(index, yaxis1, bar_width,
                                                             alpha=opacity,
                                                             color='b',
                                                             label=str(li[1]))
                                             
                                            rects2 = plt.bar(index + bar_width, yaxis2, bar_width,
                                                             alpha=opacity,
                                                             color='g',
                                                             label=str(li[2]))
                                             
                                            plt.xlabel(str(li[0]))
                                            ylabel=str(li[1])+"VS"+str(li[2])
                                            plt.ylabel(ylabel)
                                            plt.title('Python Double Bar')
                                            plt.xticks(index + bar_width, xaxis)
                                            plt.legend()
                                            plt.tight_layout()
                                            plt.show()
                                      
                            c.execute("show columns from "+table)
                            colnames=c.fetchall()
                            choi3=[]
                            for i in range(len(colnames)):
                                choi3.append(colnames[i][0])
                            option4=OptionMenu(self,var8,*choi3)
                            option4.place(x=15,y=400)
                            button = tk.Button(self,text="Add x column", command=chartcreate)
                            button.place(x=100,y=410)
                   table=var6.get()
                   c.execute("show columns from "+table)
                   L11=tk.Label(self,text="Select the type of chart and number of columns:")
                   L11.place(x=10,y=280)
                   var9=IntVar()
                   ra0=tk.Radiobutton(self,text="1column:for histogram or pie chart",variable=var9,value=1)
                   ra0.place(x=10,y=320)
                   ra1=tk.Radiobutton(self,text="2columns: x->1 and y->1",variable=var9,value=2)
                   ra1.place(x=10,y=350)
                   ra2=tk.Radiobutton(self,text="3columns: x->1 and y->2",variable=var9,value=3)
                   ra2.place(x=10,y=380)
                   values=["bar", "line","Histogram","HeatMap","Scatter"]
                   option3=OptionMenu(self,var7,*values)
                   option3.place(x=250,y=320)
                   counts=0
                   chsel=tk.Button(self,text="Select chart",command=chartsel)
                   chsel.place(x=250,y=350)
               """db=list(var5.get())
               del(db[0])
               del(db[0])
               del(db[len(db)-1])
               del(db[len(db)-1])
               del(db[len(db)-1])
               str1 = ''.join(str(e) for e in db)"""
               str1=var5.get()
               c.execute("use "+str1)
               c.execute("show tables")
               t=c.fetchall()
               choi2=[]
               for i in range(len(t)):
                   choi2.append(t[i][0])
               L10=tk.Label(self,text="Select a database in the list and click on 'select' button")
               L10.place(x=10,y=210)
               option2 = OptionMenu(self, var6, *choi2)
               option2.place(x=15,y=240)
               bdb=tk.Button(self,text="select a table",command=tablesel)
               bdb.place(x=150,y=240)
               
           try:
               con=pymysql.connect(server,un,pwd)
               c=con.cursor()
               c.execute("show databases")
               d=c.fetchall()
               choi=[]
               for i in range(len(d)):
                   choi.append(d[i][0])
               L8=tk.Label(self,text="Select a database in the list and click on 'select' button")
               L8.place(x=10,y=150)
               var5=StringVar()
               var6=StringVar()
               option1 = OptionMenu(self, var5, *choi)
               option1.place(x=15,y=180)
               bdb=tk.Button(self,text="select",command=dbsel)
               bdb.place(x=150,y=180)
           except:
               L9=Label(self,fg="red",text="Not connected")
               L9.place(x=10,y=150)
            
           
       L5=tk.Label(self,text="Enter your server name:")
       L5.place(x=10,y=10)
       E1=tk.Entry(self)
       E1.place(x=10,y=30)
       server=str(E1.get())
       L6=tk.Label(self,text="Enter your username:")
       L6.place(x=10,y=50)
       E2=tk.Entry(self)
       E2.place(x=10,y=70)
       un=str(E1.get())
       L7=tk.Label(self,text="Enter your password:")
       L7.place(x=10,y=90)
       E3=tk.Entry(self)
       E3.place(x=10,y=120)
       pwd=str(E1.get())
       bcon=tk.Button(self,text="connect",command=conn)
       bcon.place(x=120,y=120)
       

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="  Home  ", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Excel Data Visualizer", command=p2.lift)
        b3 = tk.Button(buttonframe, text="MySQL Data Visualizer", command=p3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Python Data Visualizer")
    imag = tk.PhotoImage(file="download.png")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x500")
    root.mainloop()
