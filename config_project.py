import tkinter as tk

from tkinter import ttk

import pandas as pd

import numpy as np


#Have to make it look nicer
#Have to be able to update answers and resubmit and reset button



infile = 'C://users//alayn//desktop//config.xlsx'



names=('application',

                'trans_mfg',

                'trans_model',

                'trans_opening',

                'pto_mfg',

                'basic_model',

                'mtg_option_code',

                'gear_ratio',

                'prto_ratio_code',

                'input_gear_code',

                'lube_option_code',

                'shift_option',

                'shift_option_code',

                'assy_arngnmt',

                'output_option_desc',

                'output_option_code',

                'pump_rotation',

                'mfg')



df = pd.read_excel(infile, sheetname = 'PTO', parse_cols="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R",names=('application',

                                                         'trans_mfg',

                                                         'trans_model',

                                                         'trans_opening',

                                                         'pto_mfg',

                                                         'basic_model',

                                                         'mtg_option_code',

                                                         'gear_ratio',

                                                         'prto_ratio_code',

                                                         'input_gear_code',

                                                         'lube_option_code',

                                                         'shift_option',

                                                         'shift_option_code',

                                                         'assy_arngnmt',

                                                         'output_option_desc',

                                                         'output_option_code',

                                                         'pump_rotation',

                                                         'mfg'))





tmfg = df.trans_mfg.dropna().unique().tolist()



tmfl = df.trans_model.dropna().unique().tolist()

topn = df.trans_opening.dropna().unique().tolist()

ptom = df.pto_mfg.dropna().unique().tolist()



gratt = df.gear_ratio

grat=[]

for i in gratt:

        i = str(i)

        grat.append(i)



sopt = df.shift_option.dropna().unique().tolist()





win = tk.Tk()

win.resizable(0,0)

win.title("Configurator")
win.configure(background = 'white')




#Tabs

tabs = ttk.Notebook(win)



tab1 = ttk.Frame(tabs)

tabs.add(tab1,text='PTO')

tabs.pack(expand=1, fill='both')



tab2 = ttk.Frame(tabs)

tabs.add(tab2, text = 'Pump')

tabs.pack(expand=1, fill='both')



tab3 = ttk.Frame(tabs)

tabs.add(tab3, text = 'Resevoir')

tabs.pack(expand=1, fill = 'both')



tab4 = ttk.Frame(tabs)

tabs.add(tab4, text = 'Cab Controls')

tabs.pack(expand=1, fill = 'both')



tab5 = ttk.Frame(tabs)

tabs.add(tab5, text = 'Accessories')

tabs.pack(expand=1, fill = 'both')



#Frames

frame1 = ttk.LabelFrame(tab1,text='PTO:')

frame1.grid(column=0,row=0)

framea1 = ttk.LabelFrame(tab1, text='Codes')
framea1.grid(column=1,row=0)



frame2 = ttk.LabelFrame(tab2, text = 'Pump')

frame2.grid(column = 0, row = 0)

framea2 = ttk.LabelFrame(tab2, text='Codes')
framea2.grid(column=1,row=0)



frame3 = ttk.LabelFrame(tab3, text = 'Resevoir')

frame3.grid(column = 0, row = 0)

framea3 = ttk.LabelFrame(tab3, text='Codes')
framea3.grid(column=1,row=0)



frame4 = ttk.LabelFrame(tab4, text = 'Cab Controls')

frame4.grid(column = 0, row = 0)

framea4 = ttk.LabelFrame(tab4, text='Codes')
framea4.grid(column=1,row=0)




#ACCESSORY FRAMES
frame5 = ttk.LabelFrame(tab5)
frame5.grid(column=0,row=6)
framea5 = ttk.LabelFrame(tab5, text='Codes')
framea5.grid(column=1,row=0)
aframe1 = ttk.LabelFrame(tab5, text = '2 LINE')

aframe1.grid(column = 0, row = 0,sticky = tk.W)



aframe2 = ttk.LabelFrame(tab5, text = '3 LINE W/O FILTER')

aframe2.grid(column = 0, row = 1,sticky = tk.W)



aframe3 = ttk.LabelFrame(tab5, text = 'LINE W/FILTER')

aframe3.grid(column = 0, row = 2,sticky = tk.W)



aframe4 = ttk.LabelFrame(tab5, text = 'ALL')

aframe4.grid(column = 0, row = 3,sticky = tk.W)





#create widgets

###applications available

varlist = []



application_list=['END DUMP']

applicationLabel = ttk.Label(frame1, text='APPLICATION')

applicationLabel.grid(column=0,row=0)



application_var = tk.StringVar()

varlist.append(application_var)

applications = ttk.Combobox(frame1, width=12, state='readonly',textvariable=application_var)

applications['values'] = application_list

applications.grid(column=1,row=0)


codeFrames = [framea1, framea2, framea3, framea4, framea5]


output =[]
pumpRotation = ''

def submit_button():

        for i in varlist:

                out = i.get()

                output.append(out)

        code = ''
        #company = output[4]
        #Theres only 3 companies
        dfindex = df.set_index(['application','trans_mfg','trans_model','trans_opening','pto_mfg'])
        index = dfindex.ix[output[0],output[1],output[2],output[3],output[4]]

        basic = index['basic_model'].unique().tolist()
        #code += str(basic[0])

        mtg_o = index['mtg_option_code'].unique().tolist()
        #code += str(mtg_o[0])


        dfindex = df.set_index(['application','trans_mfg','trans_model','trans_opening','pto_mfg','gear_ratio'])
        index = dfindex.ix[output[0],output[1],output[2],output[3],output[4],output[5]]

        prto = index['prto_ratio_code']
        #code += prto

        inpt = index['input_gear_code']
        #code += inpt

        lube = index['lube_option_code']
        #code += lube

        dfindex = df.set_index(['application', 'trans_mfg','trans_model','trans_opening','pto_mfg','shift_option'])
        index = dfindex.ix[output[0],output[1],output[2],output[3],output[4],output[6]] #keyerror

        sft = index['shift_option_code'].unique().tolist()
        #code += str(sft[0])

        arng =index['assy_arngnmt'].unique().tolist()
        #code += str(int(arng[0]))

        op = index['output_option_code'].unique().tolist()
        #code += str(op[0])

        if output[4] == 'CHELSEA':
                code = str(basic[0]) + str(mtg_o[0]) + prto + inpt + lube + str(sft[0]) + arng[0] + str(op[0])
        elif output[4] == 'MUNCIE':
                code = str(basic[0]) + str(mtg_o[0]) + inpt + prto + str(sft[0]) + arng[0] + str(op[0]) + lube
        elif output[4] == 'BEZARES':
                code  = str(basic[0]) + str(mtg_o[0]) + prto + str(sft[0]) + inpt + arng[0] + str(op[0])
        else:
                code = 'Not found'

        pumpRotation = dfindex.ix[output[0],output[1],output[2]]
        pumpRotation = pumpRotation['pump_rotation']
        
        for i in codeFrames:
                ttk.Label(i, text = "PTO: " + code).grid(row=0,column=0)
                ttk.Label(i, text = 'Pump Rotation: ' + pumpRotation).grid(row=0, column = 1)
        

        
        



#question widgets

qlist = []



q1 = 'TRANSMISSIONGMFG'

q2 = 'TRANSMISSION MODEL'

q3 = 'TRANSMISSION OPENING'

q4 = 'PTO MFG'

q5 = 'GEAR RATIO DESCRIPTION'

q6 = 'SHIFT OPTION DESCRIPTION'



qlist.append(q1)

qlist.append(q2)

qlist.append(q3)

qlist.append(q4)

qlist.append(q5)

qlist.append(q6)



submit = ttk.Button(frame1, text='Submit', command=submit_button)

submit.grid(row=7, column=1)





qvar1 = tk.StringVar()

varlist.append(qvar1)

label = ttk.Label(frame1,text=qlist[0]).grid(column=0, row=1)

box1 = ttk.Combobox(frame1,width=12, textvariable=qvar1, state='readonly')

box1['values'] = tmfg

box1.grid(column=1,row=1)



#############################################

#############################################

def qvar1_callback(*ignoredArgs):

        if qvar1.get():

                box2.configure(state='normal')

                index =df.set_index(['application', 'trans_mfg'])

                index = index.ix[varlist[0].get(),varlist[1].get()]

                index = index['trans_model'].unique().tolist()

                box2['values'] = index

        else:		box2.configure(state='disabled')



qvar1.trace('w', lambda unused0, unused1, unused2: qvar1_callback())



#############################################

##############################################


code = []


# dftmfl = df.ix[df.trans_mfg == qvar2.get(), ('trans_model')]

qvar2 = tk.StringVar()

varlist.append(qvar2)

label = ttk.Label(frame1,text=qlist[1]).grid(column=0, row=2)

box2 = ttk.Combobox(frame1,width=12, textvariable=qvar2, state='disabled')

box2['values'] = []

box2.grid(column=1,row=2)



def qvar2_callback(*ignoredArgs):

        if qvar2.get():

                box3.configure(state='normal')

                index =df.set_index(['application', 'trans_mfg','trans_model'])

                index = index.ix[varlist[0].get(),varlist[1].get(),varlist[2].get()]

                index = index['trans_opening'].unique().tolist()

                box3['values'] = index

        else:		box3.configure(state='disabled')



qvar2.trace('w', lambda unused0, unused1, unused2: qvar2_callback())



qvar3 = tk.StringVar()

varlist.append(qvar3)

label = ttk.Label(frame1,text=qlist[2]).grid(column=0, row=3)

box3 = ttk.Combobox(frame1,width=12, textvariable=qvar3, state='disabled')

box3['values'] = topn

box3.grid(column=1,row=3)



def qvar3_callback(*ignoredArgs):

        if qvar3.get():

                box4.configure(state='normal')

                index = df.set_index(['application', 'trans_mfg','trans_model','trans_opening'])

                index = index.ix[varlist[0].get(),varlist[1].get(),varlist[2].get(),varlist[3].get()]

                index = index['pto_mfg'].unique().tolist()

                box4['values'] = index

        else:		box4.configure(state='disabled')



qvar3.trace('w', lambda unused0, unused1, unused2: qvar3_callback())



qvar4 = tk.StringVar()

varlist.append(qvar4)

label = ttk.Label(frame1,text=qlist[3]).grid(column=0, row=4)

box4 = ttk.Combobox(frame1,width=12, textvariable=qvar4, state='disabled')

box4['values'] = ptom

box4.grid(column=1,row=4)



def qvar4_callback(*ignoredArgs):

        if qvar4.get():

                box5.configure(state='normal')

                index =df.set_index(['application', 'trans_mfg','trans_model','trans_opening','pto_mfg'])

                index = index.ix[varlist[0].get(),varlist[1].get(),varlist[2].get(),varlist[3].get(),varlist[4].get()]

                index = index['gear_ratio']

                indexList = []

                for i in index:

                        i = str(i)

                        indexList.append(i)

                box5['values'] = indexList

        else:		box5.configure(state='disabled')



qvar4.trace('w', lambda unused0, unused1, unused2: qvar4_callback())



qvar5 = tk.DoubleVar()

varlist.append(qvar5)

label = ttk.Label(frame1,text=qlist[4]).grid(column=0, row=5)

box5= ttk.Combobox(frame1,width=12, textvariable=qvar5, state='disabled')

box5['values'] = grat

box5.grid(column=1,row=5)



def qvar5_callback(*args):

        if qvar5.get():

                box6.configure(state='normal')

                index =df.set_index(['application', 'trans_mfg','trans_model','pto_mfg'])

                index = index.ix[varlist[0].get(),varlist[1].get(),varlist[2].get(),varlist[4].get()]

                index = index['shift_option'].dropna().tolist()

                box6['values'] = index

        else:		box6.configure(state='disabled')



qvar5.trace('w', qvar5_callback)



qvar6 = tk.StringVar()

varlist.append(qvar6)

label = ttk.Label(frame1,text=qlist[5]).grid(column=0, row=6)

box6 = ttk.Combobox(frame1,width=12, textvariable=qvar6, state='disabled')

box6['values'] = sopt

box6.grid(column=1,row=6)






####PUMP



dfPump = pd.read_excel(infile, sheetname = 'PUMP', parse_cols = "D,E,F",

                                           names = ('pump_mfg','shift_type','model_num'),

                                           thousands = None)

pumpMFG = dfPump.pump_mfg.dropna().unique().tolist()

shiftType = dfPump.shift_type.dropna().unique().tolist()

modelNum = dfPump.model_num.dropna().unique().tolist()



pumpOutput = []

pumpModel = ''

def pump_submit():

        for i in pumpVarList:

                pumpOutput.append(i.get())

        pumpRotation = pumpOutput[1]



        if pumpOutput[0] == 'NO':

                ttk.Label(frame2, text = "No pump").grid(column=1,row=3)

        else:

                if pumpOutput[2] == 'OTR':

                        if pumpRotation == 'CCW':

                                if pumpOutput[3] == 'AIR':

                                        pumpModel = modelNum[0]

                                else:

                                        pumpModel = modelNum[2]

                        else:

                                if pumpOutput[3] == 'AIR':

                                        pumpModel = modelNum[3]

                                else:

                                        pumpModel = modelNum[4]

                elif pumpOutput[2] == 'PARKER':

                        if pumpRotation == 'CCW':

                                if pumpOutput[3] == 'AIR':

                                        pumpModel = modelNum[5]

                                else:

                                        pumpModel = modelNum[6]

                        else:

                                if pumpOutput[3] == 'AIR':

                                        pumpModel = modelNum[7]

                                else:

                                        pumpModel = modelNum[8]

                else:

                        if pumpRotation == 'CCW':

                                if pumpOutput[3] == 'AIR':

                                        pumpModel = modelNum[9]

                                else:

                                   pumpModel = modelNum[10]



                        else:

                                if pumpOutput[3] == 'AIR':

                                        pumpModel = modelNum[11]

                                else:

                                        pumpModel = modelNum[12]

                for i in codeFrames:
                        ttk.Label(i, text='Pump Model: ' + pumpModel).grid(column=0,row=2)







pumpVarList = []

pumpYN_var = tk.StringVar()

pumpVarList.append(pumpYN_var)

pumpYNLabel = ttk.Label(frame2, text = 'Do you want a pump?')

pumpYNLabel.grid(column = 0, row = 0)

pumpYN = ttk.Combobox(frame2, width=12, state='readonly',textvariable=pumpYN_var)

pumpYN['values'] = ['YES','NO']

pumpYN.grid(column=1,row=0)


p_varC = tk.StringVar()
pumpVarList.append(p_varC)
pvarCLabel = ttk.Label(frame2, text = 'Rotation')
pvarCLabel.grid(column = 0, row = 1)
pvarC = ttk.Combobox(frame2, width=12, state='readonly', textvariable=p_varC)
pvarC['values'] = ['CW','CCW']
pvarC.grid(column=1,row=1)




p_var1 = tk.StringVar()

pumpVarList.append(p_var1)

pvar1Label = ttk.Label(frame2, text = 'MFG')

pvar1Label.grid(column = 0, row = 2)

pvar1 = ttk.Combobox(frame2, width=12, state='normal',textvariable=p_var1)

pvar1['values'] = pumpMFG

pvar1.grid(column=1,row=2)



p_var2 = tk.StringVar()

pumpVarList.append(p_var2)

pvar2Label = ttk.Label(frame2, text = 'SHIFT TYPE')

pvar2Label.grid(column = 0, row = 3)

pvar2 = ttk.Combobox(frame2, width=12, state='normal',textvariable=p_var2)

pvar2['values'] = shiftType

pvar2.grid(column=1,row=3)



submit = ttk.Button(frame2, text='Submit', command=pump_submit)

submit.grid(row=4, column=1)



###RESERVOIR

dfRes = pd.read_excel(infile, sheetname = 'RESERVOIR', parse_cols = "C,D,E,G,I",

                                           names = ('cyl_size','gallons','material',

                                                                'mount_loc','strap'))

cylSize = dfRes.cyl_size.dropna().unique().tolist()

gal = dfRes.gallons.dropna().tolist()

mat = dfRes.material.dropna().unique().tolist()

mount = dfRes.mount_loc.dropna().unique().tolist()

strp = dfRes.strap.dropna().unique().tolist()

strp.append('NA')



resVarList = []

resOutput = []

def res_submit():

        resCode = ''

        for i in resVarList:

                resOutput.append(i.get())

        j = -1

        for i in range(len(gal) - 1):

                if resOutput[0] == cylSize[i]:

                        j = i

        resCode += str(gal[i])

        if resOutput[1] == 'ALUMINUM':

                resCode += 'A'

        else:

                resCode += 'S'



        if resOutput[2] == 'SADDLE-SIDE FRAME':

                resCode += 'SM'

        else:

                resCode += 'UR'



        if resOutput[3] == 'CARBON STEEL':

                resCode += '0SG'

        elif resOutput[3] == 'STAINLESS STEEL':

                resCode += 'SSSG'

        else:

                resCode += 'SG'

        for i in codeFrames:
                        ttk.Label(i, text='Resevoir: ' + resCode).grid(column=0,row=3)



r_var1 = tk.StringVar()

resVarList.append(r_var1)

r1Label = ttk.Label(frame3, text = 'CYLINDER SIZE')

r1Label.grid(column = 0, row = 1)

rvar1 = ttk.Combobox(frame3, width=18, state='normal',textvariable=r_var1)

rvar1['values'] = cylSize

rvar1.grid(column=1,row=1)





r_var2 = tk.StringVar()

resVarList.append(r_var2)

r2Label = ttk.Label(frame3, text = 'MATERIAL DESCRIPTION')

r2Label.grid(column = 0, row = 2)

rvar2 = ttk.Combobox(frame3, width=18, state='normal',textvariable=r_var2)

rvar2['values'] = mat

rvar2.grid(column=1,row=2)





r_var3 = tk.StringVar()

resVarList.append(r_var3)

r3Label = ttk.Label(frame3, text = 'MOUNTING LOCATION')

r3Label.grid(column = 0, row = 3)

rvar3 = ttk.Combobox(frame3, width=18, state='normal',textvariable=r_var3)

rvar3['values'] = mount

rvar3.grid(column=1,row=3)



r_var4 = tk.StringVar()

resVarList.append(r_var4)

r4Label = ttk.Label(frame3, text = 'STRAP MATERIAL')

r4Label.grid(column = 0, row = 4)

rvar4 = ttk.Combobox(frame3, width=18, state='normal',textvariable=r_var4)

rvar4['values'] = strp

rvar4.grid(column=1,row=4)



submit = ttk.Button(frame3, text='Submit', command=res_submit)

submit.grid(row=7, column=1)







####CAB CONTROLS



dfCC = pd.read_excel(infile, sheetname = 3, parse_cols = "D,E,F,G",

                                           names = ('dash','dash_desc','console','console_desc'))



dsh = dfCC.dash.dropna().unique().tolist()

dshD = dfCC.dash_desc.dropna().unique().tolist()

con = dfCC.console.dropna().unique().tolist()

conD = dfCC.console_desc.dropna().unique().tolist()





ccVarList = []



def cc_submit():

        ccCode = ''

        ccOutput = []

        for i in ccVarList:

                ccOutput.append(i.get())



        if ccOutput[0] == 'DASH':

                j = -1

                for i in range(len(dsh) - 1):

                        if dshD[i] == ccOutput[0]:

                                j = i

                ccCode = dsh[j]

        else:

                j = -1

                for i in range(len(con) - 1):

                        if conD[i] == ccOutput[0]:

                                j = i

                ccCode = con[j]

        for i in codeFrames:
                        ttk.Label(i, text='Cab Control: ' + ccCode).grid(column=0,row=4)

def opt_submit():

        if ccVarList[0].get() == 'DASH':

                cc_var2 = tk.StringVar()

                ccVarList.append(cc_var2)

                cc2Label = ttk.Label(frame4, text = 'Dash options')

                cc2Label.grid(column = 0, row = 2)

                ccvar2 = ttk.Combobox(frame4, width=24, state='readonly', textvariable=cc_var2)

                ccvar2['values'] = dshD

                ccvar2.grid(column=1,row=2)



        if ccVarList[0].get() == 'CONSOLE':

                cc_var3 = tk.StringVar()

                ccVarList.append(cc_var3)

                cc3Label = ttk.Label(frame4, text = 'Console options')

                cc3Label.grid(column = 0, row = 2)

                ccvar3 = ttk.Combobox(frame4, width=24, state='readonly' ,textvariable=cc_var3)

                ccvar3['values'] = conD

                ccvar3.grid(column=1,row=2)



        submit = ttk.Button(frame4, text='Submit', command=cc_submit)

        submit.grid(row=5, column=1)





cc_var1 = tk.StringVar()

ccVarList.append(cc_var1)

cc1Label = ttk.Label(frame4, text = 'Where will the controls be mounted?')

cc1Label.grid(column = 0, row = 1)

ccvar1 = ttk.Combobox(frame4, width=12, state='readonly',textvariable=cc_var1)

ccvar1['values'] = ['DASH','CONSOLE']

ccvar1.grid(column=1,row=1)



submit = ttk.Button(frame4, text='Options', command=opt_submit)

submit.grid(row=5, column=1)

###ACC
dfA = pd.read_excel(infile, sheetname = 4, parse_cols = "C,E",
                     names = ('want','part'))
acc = dfA.want.dropna().unique().tolist()
prt = dfA.part.dropna().unique().tolist()

# AFRAME1 = 2 LINE
# AFRAME2 = 3 LINE W/O
# AFRAME3 = 3 LINE W/
# AFRAME4 = ALL
aVarList = []

chkvar1 = tk.IntVar()
aVarList.append(chkvar1)
chk1 = tk.Checkbutton(aframe1, text=acc[0], variable=chkvar1)
chk1.grid(column=0, row=0)

chk1.deselect()



chkvar2 = tk.IntVar()
aVarList.append(chkvar2)
chk2 = tk.Checkbutton(aframe1, text=acc[1], variable=chkvar2)

chk2.grid(column= 1, row=0)

chk2.deselect()



chkvar3 = tk.IntVar()
aVarList.append(chkvar3)
chk3 = tk.Checkbutton(aframe2, text=acc[2], variable=chkvar3)

chk3.grid(column=0, row=0)

chk3.deselect()



chkvar4	 = tk.IntVar()
aVarList.append(chkvar4)
chk4 = tk.Checkbutton(aframe3, text=acc[3], variable=chkvar4)

chk4.grid(column=0, row=0)

chk4.deselect()


chkvar5	 = tk.IntVar()
aVarList.append(chkvar5)
chk5 = tk.Checkbutton(aframe4, text=acc[4], variable=chkvar5)

chk5.grid(column=0, row=0)

chk5.deselect()


chkvar6	 = tk.IntVar()
aVarList.append(chkvar6)
chk6 = tk.Checkbutton(aframe4, text=acc[5], variable=chkvar6)

chk6.grid(column=0, row=1)

chk6.deselect()


chkvar7	 = tk.IntVar()
aVarList.append(chkvar7)
chk7 = tk.Checkbutton(aframe4, text=acc[6], variable=chkvar7)

chk7.grid(column=0, row=2)

chk7.deselect()


chkvar8	 = tk.IntVar()
aVarList.append(chkvar8)
chk8 = tk.Checkbutton(aframe4, text=acc[7], variable=chkvar8)

chk8.grid(column=0, row=3)

chk8.deselect()

chkvar9	 = tk.IntVar()
aVarList.append(chkvar9)
chk9 = tk.Checkbutton(aframe4, text=acc[8], variable=chkvar9)

chk9.grid(column=0, row=4)

chk9.deselect()

chkvar10 = tk.IntVar()
aVarList.append(chkvar10)
chk10 = tk.Checkbutton(aframe4, text=acc[9], variable=chkvar10)

chk10.grid(column=0, row=5)

chk10.deselect()

chkvar11= tk.IntVar()
aVarList.append(chkvar11)
chk11 = tk.Checkbutton(aframe4, text=acc[10], variable=chkvar11)

chk11.grid(column=0, row=6)

chk11.deselect()


chkvar12 = tk.IntVar()
aVarList.append(chkvar12)
chk12 = tk.Checkbutton(aframe4, text=acc[11], variable=chkvar12)

chk12.grid(column=0, row=7)

chk12.deselect()

chkvar13 = tk.IntVar()
aVarList.append(chkvar13)
chk13 = tk.Checkbutton(aframe4, text=acc[12], variable=chkvar13)

chk13.grid(column=0, row=8)

chk13.deselect()

chkvar14 = tk.IntVar()
aVarList.append(chkvar14)
chk14 = tk.Checkbutton(aframe3, text=acc[13], variable=chkvar14)

chk14.grid(column=0, row=1)

chk14.deselect()

chkvar15= tk.IntVar()
aVarList.append(chkvar15)
chk15 = tk.Checkbutton(aframe3, text=acc[14], variable=chkvar15)

chk15.grid(column=0, row=2)

chk15.deselect()


chkvar16 = tk.IntVar()
aVarList.append(chkvar16)
chk16 = tk.Checkbutton(aframe3, text=acc[15], variable=chkvar16)

chk16.grid(column=0, row=3)

chk16.deselect()



partList = []
def acc_submit():
        for i in range(len(aVarList)):
                if aVarList[i].get() == 1:
                        partList.append(prt[i])

        for i in codeFrames:
                ttk.Label(i, text = 'Accessory Part Numbers:').grid(column=0,row=5)
                for j in range(len(partList)):
                        ttk.Label(i, text = partList[j]).grid(column=1,row = 6 + j)

submit = ttk.Button(frame5, text='Submit', command=acc_submit)

submit.grid(row=7, column=1)


win.mainloop()

