import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np

# mfglist = ['CHELSEA','MUNCIE','BEZARES']

infile = '/users/alayn/desktop/alayna.xlsx'

df = pd.read_excel(infile, sheetname = 0, parse_cols="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q", skiprows=0, skipfooter=0,
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
                             'pump_rotation'),thousands=None)


tmfg = df.trans_mfg.dropna().unique().tolist()
tmfl = df.trans_model.dropna().unique().tolist()
topn = df.trans_opening.dropna().unique().tolist()
ptom = df.pto_mfg.dropna().unique().tolist()
grat = df.gear_ratio.dropna().unique().tolist()
sopt = df.shift_option.dropna().unique().tolist()

win = tk.Tk()
win.resizable(0,0)
win.title("Configurator")

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

frame2 = ttk.LabelFrame(tab2, text = 'Pump')
frame2.grid(column = 0, row = 0)

frame3 = ttk.LabelFrame(tab3, text = 'Resevoir')
frame3.grid(column = 0, row = 0)

frame4 = ttk.LabelFrame(tab4, text = 'Cab Controls')
frame4.grid(column = 0, row = 0)

frame5 = ttk.LabelFrame(tab5, text = 'Accessories')
frame5.grid(column = 0, row = 0)



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


output =[]
def submit_button():
	for i in varlist:
		out = i.get()
		output.append(out)

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

qvar2 = tk.StringVar()
varlist.append(qvar2)
label = ttk.Label(frame1,text=qlist[1]).grid(column=0, row=2)
box2 = ttk.Combobox(frame1,width=12, textvariable=qvar2, state='readonly')
box2['values'] = tmfl
box2.grid(column=1,row=2)

qvar3 = tk.StringVar()
varlist.append(qvar3)
label = ttk.Label(frame1,text=qlist[2]).grid(column=0, row=3)
box3 = ttk.Combobox(frame1,width=12, textvariable=qvar3, state='readonly')
box3['values'] = topn
box3.grid(column=1,row=3)

qvar4 = tk.StringVar()
varlist.append(qvar4)
label = ttk.Label(frame1,text=qlist[3]).grid(column=0, row=4)
box4 = ttk.Combobox(frame1,width=12, textvariable=qvar4, state='readonly')
box4['values'] = ptom
box4.grid(column=1,row=4)

qvar5 = tk.StringVar()
varlist.append(qvar5)
label = ttk.Label(frame1,text=qlist[4]).grid(column=0, row=5)
box5= ttk.Combobox(frame1,width=12, textvariable=qvar5, state='readonly')
box5['values'] = grat
box5.grid(column=1,row=5)

qvar6 = tk.StringVar()
varlist.append(qvar6)
label = ttk.Label(frame1,text=qlist[5]).grid(column=0, row=6)
box6 = ttk.Combobox(frame1,width=12, textvariable=qvar6, state='readonly')
box6['values'] = sopt
box6.grid(column=1,row=6)

pumpRotation = 'CCW'

####PUMP

dfPump = pd.read_excel(infile, sheetname = 1, parse_cols = "D,E,F",
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

    if pumpOutput[0] == 'NO':
        ttk.Label(frame2, text = "No pump").grid(column=1,row=3)
    else:
        if pumpOutput[1] == 'OTR':
            if pumpRotation == 'CCW':
                if pumpOutput[2] == 'AIR':
                    pumpModel = modelNum[0]
                else:
                    pumpModel = modelNum[1]
            else:
                if pumpOutput[2] == 'AIR':
                    pumpModel = modelNum[3]
                else:
                    pumpModel = modelNum[4]
        elif pumpOutput[1] == 'PARKER':
            if pumpRotation == 'CCW':
                if pumpOutput[2] == 'AIR':
                    pumpModel = modelNum[5]
                else:
                    pumpModel = modelNum[6]
            else:
                if pumpOutput[2] == 'AIR':
                    pumpModel = modelNum[7]
                else:
                    pumpModel = modelNum[8]
        else:
            if pumpRotation == 'CCW':
                if pumpOutput[2] == 'AIR':
                    pumpModel = modelNum[9]
                else:
                   pumpModel = modelNum[10]
                    
            else:
                if pumpOutput[2] == 'AIR':
                    pumpModel = modelNum[11]
                else:
                    pumpModel = modelNum[12]
        ttk.Label(frame2, text=pumpModel).grid(column=1,row=3)
            
        

pumpVarList = []
pumpYN_var = tk.StringVar()
pumpVarList.append(pumpYN_var)
pumpYNLabel = ttk.Label(frame2, text = 'Do you want a pump?')
pumpYNLabel.grid(column = 0, row = 0)
pumpYN = ttk.Combobox(frame2, width=12, state='readonly',textvariable=pumpYN_var)
pumpYN['values'] = ['YES','NO']
pumpYN.grid(column=1,row=0)
    
p_var1 = tk.StringVar()
pumpVarList.append(p_var1)
pvar1Label = ttk.Label(frame2, text = 'MFG')
pvar1Label.grid(column = 0, row = 1)
pvar1 = ttk.Combobox(frame2, width=12, state='normal',textvariable=p_var1)
pvar1['values'] = pumpMFG
pvar1.grid(column=1,row=1)

p_var2 = tk.StringVar()
pumpVarList.append(p_var2)
pvar2Label = ttk.Label(frame2, text = 'SHIFT TYPE')
pvar2Label.grid(column = 0, row = 2)
pvar2 = ttk.Combobox(frame2, width=12, state='normal',textvariable=p_var2)
pvar2['values'] = shiftType
pvar2.grid(column=1,row=2)

submit = ttk.Button(frame2, text='Submit', command=pump_submit)
submit.grid(row=4, column=1)

###RESERVOIR
dfRes = pd.read_excel(infile, sheetname = 2, parse_cols = "C,D,E,G,I",
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

    ttk.Label(frame3, text='Resevoir Model: ' + resCode).grid(column=0,row=5)
    
r_var1 = tk.StringVar()
resVarList.append(r_var1)
r1Label = ttk.Label(frame3, text = 'CYLINDER SIZE')
r1Label.grid(column = 0, row = 1)
rvar1 = ttk.Combobox(frame3, width=12, state='normal',textvariable=r_var1)
rvar1['values'] = cylSize
rvar1.grid(column=1,row=1)


r_var2 = tk.StringVar()
resVarList.append(r_var2)
r2Label = ttk.Label(frame3, text = 'MATERIAL DESCRIPTION')
r2Label.grid(column = 0, row = 2)
rvar2 = ttk.Combobox(frame3, width=12, state='normal',textvariable=r_var2)
rvar2['values'] = mat
rvar2.grid(column=1,row=2)


r_var3 = tk.StringVar()
resVarList.append(r_var3)
r3Label = ttk.Label(frame3, text = 'MOUNTING LOCATION')
r3Label.grid(column = 0, row = 3)
rvar3 = ttk.Combobox(frame3, width=12, state='normal',textvariable=r_var3)
rvar3['values'] = mount
rvar3.grid(column=1,row=3)

r_var4 = tk.StringVar()
resVarList.append(r_var4)
r4Label = ttk.Label(frame3, text = 'STRAP MATERIAL')
r4Label.grid(column = 0, row = 4)
rvar4 = ttk.Combobox(frame3, width=12, state='normal',textvariable=r_var4)
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

    ttk.Label(frame4, text='Cab Control: ' + ccCode).grid(column=0,row=4)
def opt_submit():
    if ccVarList[0].get() == 'DASH':
        cc_var2 = tk.StringVar()
        ccVarList.append(cc_var2)
        cc2Label = ttk.Label(frame4, text = 'Dash options')
        cc2Label.grid(column = 0, row = 2)
        ccvar2 = ttk.Combobox(frame4, width=12, state='readonly', textvariable=cc_var2)
        ccvar2['values'] = dshD
        ccvar2.grid(column=1,row=2)

    if ccVarList[0].get() == 'CONSOLE':
        cc_var3 = tk.StringVar()
        ccVarList.append(cc_var3)
        cc3Label = ttk.Label(frame4, text = 'Console options')
        cc3Label.grid(column = 0, row = 2)
        ccvar3 = ttk.Combobox(frame4, width=12, state='readonly' ,textvariable=cc_var3)
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

submit = ttk.Button(frame4, text='Options', command=cc_submit)
submit.grid(row=5, column=1)




win.mainloop()




# frequency_values =['Single Occurance','Daily','Weekly','Monthly','Quarterly', 'Biannualy','Annualy']
# ttk.Label(frame2, text='Frequency:').grid(column=0, row=8, sticky=tk.W)
# frequencyEntered = ttk.Combobox(frame2, width=14, textvariable=enter_frequency)
# frequencyEntered['values'] = frequency_values
# frequencyEntered.grid(column=0, row=9, sticky=tk.W)
# frequencyEntered.current(0)
# frequencyEntered.configure(state='disabled')
